"""Define trigger listeners for Pandadoc."""
import json
import sys
from typing import Any, Optional
from uuid import uuid4
from urllib.parse import urlparse  # , parse_qs

from wkflws.events import Event
from wkflws.http import http_method, Request, Response
from wkflws.logging import getLogger
from wkflws.triggers.webhook import WebhookTrigger

from .. import __identifier__, __version__
from .. import schemas


async def process_webhook_request(
    request: Request, response: Response
) -> Optional[Event]:
    """Accept and process a Pandadoc webhook request returning an event."""
    logger = getLogger(f"{__identifier__}.triggers.process_webhook_request")
    # Pandadoc doesn't have anything that can be used to indicate which tenant is
    # receiving the webhook. as a result, this node is designed to take a wildcard path
    # so an identifier can be mapped back to a unique user.

    # The rstrip ensures we don't generate a space as the last element with a trailing
    # slash.
    url = urlparse(request.url)
    pandadoc_path_id = url.path.rstrip("/").split("/")[-1]
    metadata = {"x-pandadoc-path-id": pandadoc_path_id}
    logger.info(f"Found pandadoc path id: {pandadoc_path_id}")

    # # Extract the signature for verification.
    # qs = parse_qs(url.query)

    # try:
    #     signature = qs.get("signature", [])[0]
    # except IndexError:
    #     signature = None
    # calculated_signature = hmac.new(
    #     str(shared_key), str(request.body), digestmod=hashlib.sha256
    # ).hexdigest()
    # metadata = {
    #     "signature": signature,
    # }

    # There isn't really anything interesting in the Panda docs headers, but include
    # them anyway
    # {
    #     "host": "testing.ngrok.com",
    #     "user-agent": "PandaDoc Webhooks",
    #     "content-length": "10302",
    #     "accept": "*/*",
    #     "content-type": "application/json",
    #     "x-forwarded-for": "52.37.240.175",
    #     "x-forwarded-proto": "https",
    #     "accept-encoding": "gzip",
    # }

    # if not verified: return 401

    metadata.update(request.headers)

    # Most webhooks include a header with a unique id that can be used as the event's
    # id. This would allow tracing back to the source.
    identifier = str(uuid4())  # request.headers["remote-id"]

    # Most webhooks provide data as JSON so no transformations are needed. If they are
    # sending something other than JSON then you will need to format it as a JSON
    # serializable dict.
    data = json.loads(request.body)

    return Event(identifier, metadata, data)


async def accept_event(event: Event) -> tuple[Optional[str], dict[str, Any]]:
    """Accept and process data from the event bus."""
    logger = getLogger(f"{__identifier__}.triggers.accept_event")
    # Pandadoc sends an array of document payloads. I'm not exactly sure in what cases
    # there will be more than one element so this _may_ be incorrect.
    event_data: list[dict[str, Any]] = event.data  # type: ignore # for typechecking

    for payload in event_data:
        event_type = payload.get("event", None)
        doc_data = payload.get("data", None)

        if event_type == "document_state_changed":
            data = schemas.Document(**doc_data)  # type: ignore
            print(data.json(by_alias=True, indent=2), file=sys.stderr)
            return "wkflws_pandadoc.triggers.document_state_changed", data.dict(
                by_alias=True
            )
        else:
            logger.warning(
                f"Event type '{event_type}' not supported in event id "
                f"{event.identifier}"
            )
            return None, {}
    # Nothing left to do.
    return None, {}


webhook = WebhookTrigger(
    client_identifier=__identifier__,
    client_version=__version__,
    process_func=accept_event,
    routes=(
        (
            (http_method.POST,),
            "/pandadoc/webhook/{pandadoc_id}/",
            process_webhook_request,
        ),
    ),
)

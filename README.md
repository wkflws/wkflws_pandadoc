# wkflws_pandadoc
This node provides trigger support for [Pandadoc Webhooks](https://support.pandadoc.com/hc/en-us/articles/360007915853--Webhooks).

## wkflws_pandadoc.triggers.document_state_changed
Called when a document's status changes. A list of statuses can be found [here](https://openapi.pandadoc.com/#/schemas/DocumentStatusEnum).

### Context Properties
The following context properties are required for this node.
| name | required | description |
|-|-|-|

### Example Output
```json
{
  "id": "KiFtLJ7JtEopm75HCYtJ6E",
  "name": "Client IO: Company Y",
  "autonumbering_sequence_name": null,
  "date_created": "2022-07-27T16:51:02.665008Z",
  "date_modified": "2022-07-27T16:51:22.801119Z",
  "date_completed": null,
  "created_by": {
    "id": "MDFkjdI6LS994zmoPXpmcYN2",
    "email": "sales@company.com",
    "first_name": "Nick",
    "last_name": "Regis",
    "avatar": null,
    "membership_id": "IkN4SNmmNVIUQJKFjBK4GKJL"
  },
  "template": {
    "id": "nuT3j3IQ64puB5qnATZ4qc",
    "name": "Client IO: Company Y"
  },
  "expiration_date": "2022-09-25T16:51:22.645002Z",
  "metadata": {},
  "tokens": [],
  "fields": [
    {
      "field_id": "clientName",
      "uuid": "fa2137f3-11e9-4a22-860d-d01e0a72047f",
      "name": "Company.Name",
      "title": "",
      "placeholder": "Enter value",
      "value": "Client Name",
      "assignee": "a1@asdf.com",
      "type": "text",
      "merge_field": "Company.Name"
    },
    {
      "field_id": "Text8",
      "uuid": "3e819277-2dbb-49bd-9f22-19bd065fa4b2",
      "name": "Company.Name",
      "title": "",
      "placeholder": "XYZ Brand",
      "value": "",
      "assignee": "a1@asdf.com",
      "type": "text",
      "merge_field": "Company.Name"
    },
    {
      "field_id": "companyAddress",
      "uuid": "997ba83d-b4ae-46da-b2b9-42ab6f82707f",
      "name": "Text",
      "title": "",
      "placeholder": "123 1st St, Suite #, City, State, ZIP",
      "value": "",
      "assignee": "a2@asdf.com",
      "type": "text",
      "merge_field": null
    },
    {
      "field_id": "accountingEmail",
      "uuid": "deabffbc-e3dc-4efe-b003-2a0177eee748",
      "name": "Text",
      "title": "",
      "placeholder": "your@email.com",
      "value": "",
      "assignee": "a2@asdf.com",
      "type": "text",
      "merge_field": null
    },
    {
      "field_id": "companySignature",
      "uuid": "2a06f76b-3cc5-46ed-a111-a8f01b365d2a",
      "name": "Signature",
      "title": "",
      "placeholder": "Signature",
      "value": {},
      "assignee": "a1@asdf.com",
      "type": "signature",
      "merge_field": null
    },
    {
      "field_id": "companySignorDate",
      "uuid": "f6c06752-9b1e-4e86-bae4-aaf793afc021",
      "name": "Date",
      "title": "",
      "placeholder": "Select date",
      "value": null,
      "assignee": "a1@asdf.com",
      "type": "date",
      "merge_field": null
    },
    {
      "field_id": "clientSignature",
      "uuid": "d2bcf9e7-72ec-4551-bb53-d6848e8146da",
      "name": "Signature",
      "title": "",
      "placeholder": "Signature",
      "value": {},
      "assignee": "a2@asdf.com",
      "type": "signature",
      "merge_field": null
    },
    {
      "field_id": "clientSignorDate",
      "uuid": "9302d0a0b-4e13-43ca-8373-1871334463e5",
      "name": "Date",
      "title": "",
      "placeholder": "Select date",
      "value": null,
      "assignee": "a2@asdf.com",
      "type": "date",
      "merge_field": null
    }
  ],
  "pricing": {},
  "version": "2",
  "tags": [
    "Sales IO"
  ],
  "status": "document.sent",
  "recipients": [
    {
      "id": "93ksyJf6Vbab3oFc3YixuvT",
      "contact_id": "dfMIKUqSDwh9jQ3XmtQFGHaG",
      "recipient_type": "signer",
      "roles": [
        "CompanyX"
      ],
      "first_name": "Jerry",
      "last_name": "Pointman",
      "signing_order": 1,
      "shared_link": "",
      "has_completed": false
    },
    {
      "id": "bjd9XXu8epyqMxa724mW2f",
      "contact_id": "JDidEfJJeUytUbWeQVui7f",
      "recipient_type": "signer",
      "roles": [
        "Client"
      ],
      "first_name": "Samuel",
      "last_name": "Smart",
      "signing_order": 2,
      "shared_link": "",
      "has_completed": false
    }
  ],
  "sent_by": {
    "id": "MDFkjdI6LS994zmoPXpmcYN2",
    "email": "sales@company.com",
    "first_name": "Nick",
    "last_name": "Regis",
    "avatar": null,
    "membership_id": "IkN4SNmmNVIUQJKFjBK4GKJL"
  },
  "grand_total": {
    "amount": "199",
    "currency": "USD"
  },
  "linked_objects": []
}
```
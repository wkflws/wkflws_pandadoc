import enum
from typing import Any, Literal, Optional, Union

from pydantic import BaseModel, EmailStr, Field, HttpUrl, UUID4


class DocumentStatus(str, enum.Enum):
    """All possible document statuses."""

    draft = "document.draft"
    sent = "document.sent"
    completed = "document.completed"
    uploaded = "document.uploaded"
    error = "document.error"
    viewed = "document.viewed"
    waiting_approval = "document.waiting_approval"
    approved = "document.approved"
    rejected = "document.rejected"
    waiting_pay = "document.waiting_pay"
    paid = "document.paid"
    voided = "document.voided"
    declined = "document.declined"
    external_review = "document.external_review"


class User(BaseModel):
    """Represents a Pandadoc user."""

    id_: str = Field(alias="id")
    email: EmailStr
    first_name: str
    last_name: str
    avatar: Optional[HttpUrl]
    membership_id: str


class Template(BaseModel):
    """Represent a Pandadoc document template."""

    id_: str = Field(alias="id")
    name: str


class Token(BaseModel):
    """Represent a Pandadoc token."""

    name: str
    value: str


class DocumentField(BaseModel):
    """Represent a field with user defined data."""

    field_id: str
    uuid: UUID4  # they appear to use v4 uuids
    name: str
    title: str
    placeholder: Optional[str]
    #: ``value`` types depend on the value of the ``type`` field
    #: date: str
    #: checkbox: bool
    #: signature: dict (empty dict as far as i can tell)
    #: text: str
    value: Union[None, str, bool, dict[str, Any]]
    assignee: str  # these appear to be email addresses
    type_: str = Field(alias="type")
    merge_field: Optional[str]


class PricingTableSummary(BaseModel):
    """Display summary information for a pricing table."""

    subtotal: str
    total: str
    discount: str
    tax: str


class PricingTableItemDiscount(BaseModel):
    """Describe a discount to an item in a pricing table."""

    type_: str = Field(alias="type")
    value: str


class PricingTableItemTaxFirst(BaseModel):
    """Unsure what this is."""

    type_: str = Field(alias="type")
    value: str


class PricingTableItemTaxSecond(BaseModel):
    """Unsure what this is."""

    type_: str = Field(alias="type")
    value: str


class PricingTableItemOptions(BaseModel):
    """Unsure what this is."""

    optional: bool
    option_selected: bool
    multichoice_enabled: bool
    multichoice_selected: bool


class PricingTableItem(BaseModel):
    """Describe an item in a pricing table."""

    id_: str = Field(alias="id")
    sku: str
    qty: str
    name: str
    const: str
    price: str
    description: str
    custom_fields: dict[str, Any]  # unsure what this looks like
    custom_columns: dict[str, Any]  # ex: {"Images":"","Cost":"","Subtotal":""}
    discount: PricingTableItemDiscount
    tax_first: PricingTableItemTaxFirst
    tax_second: PricingTableItemTaxSecond
    subtotal: str
    options: PricingTableItemOptions
    sale_price: str
    taxes: dict[str, Any]  # unsure what this looks like
    fees: dict[str, Any]  # unsure what this looks like
    discounts: dict[str, Any]  # unsure what this looks like
    #: Will contain all the fields in flat structure with external field names defined
    #: in the template
    merged_data: dict[str, Any]


class PricingTable(BaseModel):
    """A table used to describe pricing."""

    id_: str = Field(alias="id")
    name: str
    total: str
    is_included_in_total: bool
    summary: PricingTableSummary
    items: list[PricingTableItem]
    currency: str  # e.g. USD


class Pricing(BaseModel):
    """Describes pricing information."""

    tables: list[PricingTable]
    #: Total seems to be the number of cents?
    total: str


class Recipient(BaseModel):
    """Describes a recipient of a document."""

    id_: str = Field(alias="id")
    contact_id: str
    recipient_type: str
    # role: str   # deprecated
    roles: list[str]
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    signing_order: Optional[Any]  # nullable unknown type
    shared_link: HttpUrl | Literal[""]
    has_completed: bool


class GrandTotal(BaseModel):
    """Describes the grand total."""

    amount: str
    currency: str


class LinkedObject(BaseModel):
    """Describes a linked object."""

    provider: str  # e.g. hubspot
    entity_type: str
    entity_id: str
    id_: str = Field(alias="id")


class EmptyDict(BaseModel):
    """Represents an empty field."""

    ...

    class Meta:  # noqa D106
        extra = "forbid"


class Document(BaseModel):
    """Represents a Pandadoc Document.

    Loosely based on the document details response found here:
    https://openapi.pandadoc.com/#/operations/detailsDocument
    """

    id_: str = Field(alias="id")
    name: str
    autonumbering_sequence_name: Optional[Any]  # unsure of this type
    date_created: str
    date_modified: str
    date_completed: Optional[str]
    created_by: User
    template: Optional[Template]
    expiration_date: Optional[str]
    metadata: dict[str, Any]  # Doesn't seem to have a defined structure
    tokens: list[Token]
    fields: list[DocumentField]
    # products
    pricing: Pricing | EmptyDict
    version: str
    tags: list[str]
    status: DocumentStatus
    recipients: list[Recipient]
    sent_by: Optional[User]
    grand_total: GrandTotal
    linked_objects: list[LinkedObject]

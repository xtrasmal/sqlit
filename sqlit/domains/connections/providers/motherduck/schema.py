"""Connection schema for MotherDuck."""

from sqlit.domains.connections.providers.schema_helpers import (
    ConnectionSchema,
    FieldType,
    SchemaField,
)

SCHEMA = ConnectionSchema(
    db_type="motherduck",
    display_name="MotherDuck",
    fields=(
        SchemaField(
            name="database",
            label="Database",
            placeholder="my_database",
            required=True,
        ),
        SchemaField(
            name="password",
            label="Access Token",
            field_type=FieldType.PASSWORD,
            required=True,
        ),
    ),
    supports_ssh=False,
    is_file_based=False,  # Not file-based, uses database + token
    requires_auth=True,
)

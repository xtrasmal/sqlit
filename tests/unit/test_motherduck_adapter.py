"""Unit tests for MotherDuck adapter."""

from __future__ import annotations


def test_motherduck_provider_registered():
    """Test that MotherDuck provider is properly registered."""
    from sqlit.domains.connections.providers.catalog import get_supported_db_types

    db_types = get_supported_db_types()
    assert "motherduck" in db_types


def test_motherduck_provider_metadata():
    """Test MotherDuck provider metadata."""
    from sqlit.domains.connections.providers.catalog import get_provider

    provider = get_provider("motherduck")
    assert provider.metadata.display_name == "MotherDuck"
    assert provider.metadata.is_file_based is False
    assert provider.metadata.supports_ssh is False
    assert provider.metadata.requires_auth is True
    assert "md" in provider.metadata.url_schemes
    assert "motherduck" in provider.metadata.url_schemes


def test_motherduck_database_type_enum():
    """Test MotherDuck is in DatabaseType enum."""
    from sqlit.domains.connections.domain.config import DatabaseType

    assert DatabaseType.MOTHERDUCK.value == "motherduck"


def test_motherduck_schema_uses_password_field():
    """Test MotherDuck schema uses standard password field for token."""
    from sqlit.domains.connections.providers.motherduck.schema import SCHEMA

    field_names = [f.name for f in SCHEMA.fields]
    assert "database" in field_names
    assert "password" in field_names  # Uses standard password field for token

    # Password field should be labeled as "Access Token"
    password_field = next(f for f in SCHEMA.fields if f.name == "password")
    assert password_field.label == "Access Token"

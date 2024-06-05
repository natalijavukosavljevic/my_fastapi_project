"""Clases for FASTapi app."""
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Image(BaseModel):
    """A class to represent a project logo."""

    filename: str
    content_type: str


class Document(BaseModel):
    """A class to represent a project documents."""

    filename: str
    content_type: str



class Project(BaseModel):
    """A class to represent a project."""

    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    image: Optional[Image] = None  # noqa: UP007
    documents: Optional[list[Document]] = None  # noqa: UP007

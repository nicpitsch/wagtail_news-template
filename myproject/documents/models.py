from django.db import models
from wagtail.documents.models import AbstractDocument, Document
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class FolderDocument(AbstractDocument):
    folder = models.CharField(
        max_length=255,
        blank=True,
        help_text="Folder path (e.g., '2023/reports' or 'legal/contracts')"
    )

    admin_form_fields = Document.admin_form_fields + (
        'folder',
    )

    search_fields = AbstractDocument.search_fields + [
        index.SearchField('folder'),
        index.FilterField('folder'),
    ]

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

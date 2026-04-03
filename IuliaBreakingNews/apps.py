"""
Application configuration for IuliaBreakingNews.
Registers signals when the app is ready.
Groups and permissions are created automatically after migrations
via the post_migrate signal — no manual setup required.
"""

from django.apps import AppConfig


class IuliaBreakingNewsConfig(AppConfig):
    """Configuration for the IuliaBreakingNews app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "IuliaBreakingNews"

    def ready(self):
        """
        Import signals when the app is ready.
        The import is intentionally inside ready() to avoid
        circular imports — this is the standard Django pattern
        for registering signals.
        """
        import IuliaBreakingNews.signals  # noqa: F401, E402, PLC0415
        from django.db.models.signals import post_migrate
        from IuliaBreakingNews.setup import create_groups_and_permissions
        post_migrate.connect(create_groups_and_permissions, sender=self)

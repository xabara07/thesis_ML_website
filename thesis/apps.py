from django.apps import AppConfig


class ThesisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "thesis"

    def ready(self):
        import thesis.signals

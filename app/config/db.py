from config.settings import get_settings

settings = get_settings()

DB_CONFIG = {
    "connections": {
        "default": settings.DATABASE_URL
    },
    "apps": {
        "app": {
            "models": settings.MODELS,
            "default_connection": "default",
        }
    }
}


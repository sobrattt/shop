import logging
import logging.config

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "main",
            "level": "DEBUG"
        },
        "text": {
            "class": "logging.FileHandler",
            "formatter": "main",
            "level": "DEBUG",
            "filename": "logs.log"
        }

    },
    "formatters": {
        "main": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "loggers":{
        "root": {
            "handlers": ["console", "text"],
            "level": "DEBUG"
        }
    }
})

logger = logging.getLogger("root")

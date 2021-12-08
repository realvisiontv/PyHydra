from app.core import config
from app.core.events import create_start_app_handler, create_stop_app_handler
from fastapi import FastAPI
from app.api.routes.base import router as api_router


def get_application() -> FastAPI:
    settings = config.get_app_settings()

    application = FastAPI()

    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=settings.allowed_hosts,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    application.add_event_handler(
        "startup",
        create_start_app_handler(application),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()

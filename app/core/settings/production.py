from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    debug: bool = False
    title: str = "Production PyHydra"

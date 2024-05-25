from fastapi import FastAPI
from src.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            version=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH  # noqa
        )


app = App()

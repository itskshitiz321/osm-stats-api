from .app import Mapathon, Database,Output,DataQuality
from .config import config

import json
import logging
import os

def get_db_connection_params() -> dict:
    json_env = os.getenv("POSTGRES_CONNECTION_PARAMS")
    del json_env["dbinstanceidentifier"]
    del json_env["engine"]

    if json_env is not None:
        return json.loads(json_env)

    """TODO: Use libpq friendly envvars
    https://www.postgresql.org/docs/current/static/libpq-envars.html

    PGHOST, PGUSER, PGPASSWORD, PGPORT, PGDATABASE
    """

    connection_params = {
        "POSTGRES_USER": os.getenv("POSTGRES_USER"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
        "POSTGRES_PORT": os.getenv("POSTGRES_PORT"),
        "POSTGRES_DATABASE": os.getenv("POSTGRES_DATABASE")
    }

    if None in connection_params.values():
        return dict(config.items("PG"))

    return connection_params

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__all__ = [
    'Mapathon',
    'Database',
    'Output',
    'DataQuality',
    'config'
]

from __future__ import annotations

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


_engine = None
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False))


def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url


def init_db() -> None:
    global _engine
    if _engine is not None:
        return
    _engine = create_engine(get_database_url(), pool_pre_ping=True)
    SessionLocal.configure(bind=_engine)


def get_session():
    return SessionLocal()

from __future__ import annotations

from flask import Response, jsonify


def ok(data, status: int = 200) -> Response:
    return jsonify(data), status


def error(message: str, status: int = 400, **extra) -> Response:
    payload = {"error": message, **extra}
    return jsonify(payload), status

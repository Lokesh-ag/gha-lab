from app import add, app


def test_add():
    assert add(2, 3) == 5


def test_health():
    client = app.test_client()
    assert client.get("/health").json == {"status": "ok"}

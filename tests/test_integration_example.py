from app import create_app # or app instance, depending on your project structure

def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    app = create_app()
    client = app.test_client()
    response = client.post("/add", data=dict(item=42))
    assert response.status_code == 302

def test_delete():
    app = create_app()
    client = app.test_client()
    client.post("/add", data=dict(item=42))
    response = client.get("/delete/1")
    assert response.status_code == 302

def test_update():
    app = create_app()
    client = app.test_client()
    client.post("/add", data=dict(item=42))
    response = client.post("/update/1", data=dict(item=52))
    assert response.status_code == 302
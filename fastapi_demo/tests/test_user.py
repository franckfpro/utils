def test_create_user(client):
    payload = {
        "utilisateur": "alice",
        "email": "alice@example.com",
        "completement": "Profil Administrateur",
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["utilisateur"] == payload["utilisateur"]
    assert data["email"] == payload["email"]
    assert "id" in data


def test_read_users(client):
    # Création préalable
    client.post(
        "/users/", json={"utilisateur": "bob", "email": "bob@example.com"}
    )

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["utilisateur"] == "bob"


def test_read_single_user(client):
    create_resp = client.post(
        "/users/", json={"utilisateur": "charlie", "email": "charlie@example.com"}
    )
    user_id = create_resp.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["utilisateur"] == "charlie"


def test_update_user(client):
    create_resp = client.post(
        "/users/", json={"utilisateur": "david", "email": "david@example.com"}
    )
    user_id = create_resp.json()["id"]

    update_payload = {"email": "david_new@example.com"}
    response = client.patch(f"/users/{user_id}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["email"] == "david_new@example.com"
    # Vérification que le reste n'a pas changé
    assert response.json()["utilisateur"] == "david"


def test_delete_user(client):
    create_resp = client.post(
        "/users/", json={"utilisateur": "eve", "email": "eve@example.com"}
    )
    user_id = create_resp.json()["id"]

    # Suppression
    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 204

    # Vérification de la disparition
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 404

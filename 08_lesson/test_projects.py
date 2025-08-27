import pytest
from project_api import ProjectAPI


@pytest.fixture
def project_api():
    return ProjectAPI()


def test_create_project_positive(project_api):
    data = {"title": "Test Project Positive"}
    response = project_api.create_project(data)
    assert response.status_code == 201
    json_response = response.json()
    assert "id" in json_response
    assert json_response["title"] == "Test Project Positive"


def test_create_project_negative(project_api):
    data = {}
    response = project_api.create_project(data)
    assert response.status_code in [400, 422]


def test_update_project_positive(project_api):
    create_data = {"title": "Test Project for Update"}
    create_response = project_api.create_project(create_data)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    update_data = {"title": "Updated Test Project"}
    update_response = project_api.update_project(project_id, update_data)
    assert update_response.status_code == 200

    get_response = project_api.get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Updated Test Project"


def test_update_project_negative(project_api):
    invalid_id = "non-existent-project-id"
    data = {"title": "Irrelevant"}
    response = project_api.update_project(invalid_id, data)
    assert response.status_code == 404


def test_get_project_positive(project_api):
    create_data = {"title": "Test Project for Get"}
    create_response = project_api.create_project(create_data)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    response = project_api.get_project(project_id)
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response
    assert json_response["title"] == "Test Project for Get"


def test_get_project_negative(project_api):
    invalid_id = "non-existent-project-id"
    response = project_api.get_project(invalid_id)
    assert response.status_code == 404

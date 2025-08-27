import requests

BASE_URL = "https://yougile.com/api-v2"


class ProjectAPI:
    def __init__(self):
        self.login = "YOUR_LOGIN"  # логин YouGile
        self.password = "YOUR_PASSWORD"  # пароль YouGile
        self.api_key = self._get_api_key()
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _get_company_id(self):
        url = f"{BASE_URL}/auth/companies"
        data = {"login": self.login, "password": self.password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["content"][0]["id"]
        else:
            raise Exception(f"Failed to get company ID: {response.status_code} - {response.text}")

    def _get_api_key(self):
        company_id = self._get_company_id()
        url = f"{BASE_URL}/auth/keys"
        data = {"login": self.login, "password": self.password, "companyId": company_id}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["key"]
        else:
            raise Exception(f"Failed to create API key: {response.status_code} - {response.text}")

    def create_project(self, data):
        return requests.post(f"{BASE_URL}/projects", json=data, headers=self.headers)

    def update_project(self, project_id, data):
        return requests.put(f"{BASE_URL}/projects/{project_id}", json=data, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{BASE_URL}/projects/{project_id}", headers=self.headers)

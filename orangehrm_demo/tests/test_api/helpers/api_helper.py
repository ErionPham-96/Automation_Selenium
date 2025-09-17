import requests

class OrangeHRMApi:
    def __init__(self, base_url: str, client_id: str, client_secret: str, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.timeout = timeout
        self.api_url = f"{self.base_url}/web/index.php/api/v2"
        self.token_url = f"{self.base_url}/web/index.php/oauth/issueToken"
        self._token = None
        self._session = requests.Session()

    # --- internal ---
    def _get_token(self) -> str:
        if self._token:
            return self._token
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "username": "Admin",       # user login của demo
            "password": "admin123"
        }
        r = self._session.post(self.token_url, data=data, timeout=self.timeout)
        r.raise_for_status()
        self._token = r.json()["access_token"]
        return self._token

    def _auth_headers(self) -> dict:
        token = self._get_token()
        return {"Authorization": f"Bearer {token}"}

    # --- public helpers for tests ---
    def get_user_info(self, limit: int = 1) -> dict:
        """GET /admin/users?limit=..."""
        headers = self._auth_headers()
        r = self._session.get(
            f"{self.api_url}/admin/users",
            params={"limit": limit},
            headers=headers,
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def create_user(self, username: str, password: str, role_id: int = 1, status: bool = True) -> tuple[dict, int]:
        """POST /admin/users  -> (json, status_code)"""
        headers = self._auth_headers()
        headers["Content-Type"] = "application/json"
        payload = {
            "username": username,
            "password": password,
            "status": status,
            "userRoleId": role_id,
        }
        r = self._session.post(
            f"{self.api_url}/admin/users",
            json=payload,
            headers=headers,
            timeout=self.timeout,
        )
        # KHÔNG nuốt lỗi ở đây để test assert được status code
        return r.json() if r.content else {}, r.status_code
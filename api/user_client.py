from typing import Any
from playwright.sync_api import APIRequestContext, APIResponse
from utils.logger import get_logger
import time

logger = get_logger(__name__)

class UserClient:

    def __init__(self, api_request: APIRequestContext):
        self.api_request = api_request
    
    def _send_request(self, method: str, endpoint: str, **kwargs: Any) -> APIResponse:
        normalized_method = method.strip().lower()
        request_fn = getattr(self.api_request, normalized_method, None)

        if not callable(request_fn):
            raise ValueError(f"Unsupported HTTP method: {method}")

        logger.info("Sending %s request | %s", normalized_method.upper(), endpoint)

        try:
            start_time = time.perf_counter()
            response = request_fn(endpoint, **kwargs)

            duration = time.perf_counter() - start_time
            logger.info(
                "Request completed | %s | Duration: %.2f seconds",
                endpoint,
                duration,
            )
        except Exception:
            duration = time.perf_counter() - start_time
            logger.exception(
               "API request failed | %s | Duration: %.2f seconds",
                endpoint,
                duration,
            )
            raise

        logger.info(
            "Received response | %s | Status: %s",
            endpoint,
            response.status,
        )
        return response


    def get_user(self, user_id: int):
        return self._send_request("GET", f"/users/{user_id}")
    
    def get_all_users(self):
        return self._send_request("GET", "/users")
    
    def create_user(self, payload: dict):
        return self._send_request("POST", "/users", data=payload)
    
    def replace_user(self, user_id:int, payload: dict):
        return self._send_request("PUT", f"/users/{user_id}", data=payload)
    
    def update_user(self, user_id:int, payload: dict):
        return self._send_request("PATCH", f"/users/{user_id}", data=payload)
    
    def delete_user(self, user_id: int):
        return self._send_request("DELETE", f"/users/{user_id}")
    
    def retrieve_users(self, params: dict):
        return self._send_request("GET", "/users", params=params)
    
    def get_users_with_headers(self, headers: dict):
        return self._send_request("GET", "https://httpbin.org/headers", headers=headers)
    
    def create_account(self, payload):
        return self._send_request("POST", "/api/createAccount", form=payload)
    
    def verify_login(self, payload):
        return self._send_request("POST", "/api/verifyLogin", form=payload)
    
    def delete_account(self, payload):
        return self._send_request("DELETE", "/api/deleteAccount", form=payload)
        
from playwright.sync_api import APIRequestContext

from utils.logger import get_logger

logger = get_logger(__name__)

class UserClient:

    def __init__(self, api_request: APIRequestContext):
        self.api_request = api_request

    def get_user(self, user_id: int):
        endpoint = f"/users/{user_id}"
        
        logger.info("Sending GET request | %s", endpoint)
        
        try:
        # Your task: send a GET request for this user
            response = self.api_request.get(f"users/{user_id}")
        except Exception:
            logger.exception("API request failed | %s", endpoint)
            raise    
        
        logger.info( 
            "Received response | %s | Status: %s",
            endpoint,
            response.status
    )
        return response
    
    def get_all_users(self):
        response =self.api_request.get("users")
        return response
    
    def create_user(self, payload: dict):
        response = self.api_request.post("/users", data=payload)
        return response
    
    def replace_user(self, user_id:int, payload: dict):
        response = self.api_request.put(f"/users/{user_id}", data=payload)
        return response
    
    def update_user(self, user_id:int, payload: dict):
        response = self.api_request.patch(f"/users/{user_id}", data=payload)
        return response
    
    def delete_user(self, user_id: int):
        response = self.api_request.delete(f"/users/{user_id}")
        return response
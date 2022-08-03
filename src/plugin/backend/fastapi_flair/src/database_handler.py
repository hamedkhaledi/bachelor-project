import json
from typing import Dict


class Database:
    def __init__(self):
        self.__clients = Database.load_database()

    def get_clients(self) -> Dict[str, str]:
        return self.__clients

    def check_client(self, client_id: str, client_password: str) -> bool:
        if self.__clients.get(client_id) and self.__clients[client_id] == client_password:
            return True
        return False

    @classmethod
    def load_database(cls) -> Dict[str, str]:
        with open('data/users.json', 'r') as f:
            clients = json.load(f)
            result = {}
            for client in clients:
                result[client["client-id"]] = client["client-password"]
            return result

from tkinter.filedialog import askopenfilename as tk_open_file
from urllib3 import disable_warnings, exceptions
from json.decoder import JSONDecodeError
from contextlib import suppress
from base64 import b64encode
from json import loads

import requests

disable_warnings(exceptions.InsecureRequestWarning)


def try_load_content(content: str) -> dict:
    with suppress(JSONDecodeError):
        return loads(content)


def select_league_client() -> str:
    client_path = tk_open_file(
        title="Escolha o diretório do LeagueClient.",
        filetypes=[
            ("LeagueClient", ".exe")
        ]
    )
    return "/".join(client_path.split('/')[:-1])


class Store:

    def __init__(self, store_url: str, token: str):
        self.session = requests.session()
        self.store_url = store_url
        self.token = token

        self.headers = {
            "User-Agent": "RiotClient/18.0.0 (rso-auth)",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def request(self,
                method: str,
                end_point: str,
                action: dict = None) -> dict:

        attr = getattr(self.session, method)
        url = f"{self.store_url}/{end_point}"

        response = attr(url, verify=False, headers=self.headers, json=action)
        content = try_load_content(response.content)

        return {
            "status": response.status_code,
            "response": response,
            "text": response.text.strip('"'),
            "content": {
                "raw": response.content,
                "loaded": content
            }
        }


class Client:

    def __init__(self):
        __lock_file = self.__get_lock_file()

        self.port = __lock_file[2]
        self.password = __lock_file[3]
        self.method = __lock_file[4]

        self.session = requests.session()

    def request(self,
                method: str,
                end_point: str,
                action: dict = None) -> dict:

        attr = getattr(self.session, method)
        headers = self.__encrypt_headers()
        url = self.__get_url(end_point)

        response = attr(url, verify=False, headers=headers, json=action)
        content = try_load_content(response.content)

        return {
            "status": response.status_code,
            "response": response,
            "text": response.text.strip('"'),
            "content": {
                "raw": response.content,
                "loaded": content
            }
        }

    def __get_lock_file(self) -> list:
        print("Por favor, selecione o arquivo LeagueClient.exe")

        if client_path := select_league_client():
            path_file = f"{client_path}/lockfile"

        else:
            path_file = "C:/Riot Games/League of Legends/lockfile"

        with open(path_file, encoding="UTF-8") as lock_file:
            lock_file_data = lock_file.read()
            return lock_file_data.split(":")

    def __encrypt_headers(self) -> dict:
        base64 = b64encode(bytes(f"riot:{self.password}", "UTF-8"))
        return {"Authorization": f"Basic {base64.decode('ASCII')}"}

    def __get_url(self, end_point: str) -> str:
        return f"{self.method}://127.0.0.1:{self.port}/{end_point}"

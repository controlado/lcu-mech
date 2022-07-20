from requestor import Client, Store


class LCU:

    def __init__(self):
        self.client = Client()

        account_info = self.get_account_info()

        self.token = account_info["token"]
        self.account_id = account_info["accountId"]
        self.summoner_id = account_info["summonerId"]

        self.store = Store(
            self.get_store_url(),
            self.token
        )

    def unlock_champion(self, champion: dict) -> dict:
        ep = "storefront/v3/purchase"
        data = {
            "accountId": self.account_id,
            "items": [
                {
                    "inventoryType": "CHAMPION",
                    "itemId": champion["id"],
                    "ipCost": champion["ipCost"],
                    "rpCost": 0,
                    "quantity": 1
                }
            ]
        }

        return self.store.request("post", ep, data)

    def get_champions(self) -> list[dict]:
        ep = "storefront/v3/view/champions"

        r = self.store.request("get", ep)
        catalog = r["content"]["loaded"]["catalog"]

        return [

            {
                "name": item["name"],
                "id": item["itemId"],
                "tags": item["tags"],
                "ipCost": item["ip"],
                "rpCost": item["rp"]
            }

            for item in catalog
            if "owned" not in item

        ]

    def get_store_url(self) -> str:
        ep = "lol-store/v1/getStoreUrl"

        r = self.client.request("get", ep)
        return r["content"]["loaded"]

    def get_wallet(self) -> dict:
        ep = "lol-store/v1/wallet"

        r = self.client.request("get", ep)
        return r["content"]["loaded"]

    def get_account_info(self) -> dict:
        token_ep = "lol-rso-auth/v1/authorization/access-token"
        summoner_ep = "lol-summoner/v1/current-summoner"

        token = self.client.request("get", token_ep)["content"]["loaded"]
        summoner = self.client.request("get", summoner_ep)["content"]["loaded"]

        return {
            "token": token["token"],
            "accountId": summoner["accountId"],
            "summonerId": summoner["summonerId"]
        }

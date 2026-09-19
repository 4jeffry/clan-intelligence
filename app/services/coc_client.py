import os
import httpx

class CoCClient:
    def __init__(self, api_token: str = None):
        # Murni ambil dari Env Var (Railway / System)
        self.api_token = (api_token or os.getenv("COC_API_TOKEN", "")).strip()
        self.base_url = "https://api.clashofclans.com/v1"

    async def get_clan(self, clan_tag: str):
        if not self.api_token:
            return 401, {
                "message": "COC_API_TOKEN belum di-set di Environment Variables Railway.",
                "status": "unauthorized"
            }

        tag = clan_tag.strip().replace("#", "%23")
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Accept": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                res = await client.get(f"{self.base_url}/clans/{tag}", headers=headers, timeout=10.0)
                return res.status_code, res.json()
            except Exception as e:
                return 500, {"message": f"Network Error: {str(e)}"}

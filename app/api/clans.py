from fastapi import APIRouter, Query
from app.services.coc_client import CoCClient
from app.services.ingestion import IngestionService

router = APIRouter(prefix="/clans", tags=["Clans Analytics"])

@router.get("/info")
async def get_clan_info(clan_tag: str = Query("#929QGVRR", description="Clan Tag CoC")):
    client = CoCClient()
    status, raw_data = await client.get_clan(clan_tag)
    
    if status != 200:
        return {
            "status": "warning",
            "http_status": status,
            "message": raw_data.get("message", "Gagal ambil dari CoC API"),
            "suggestion": "Cek COC_API_TOKEN atau IP Colab"
        }
    
    service = IngestionService()
    parsed = service.parse_clan_data(raw_data)
    parsed["members_list"] = [
        {
            "name": m.get("name"),
            "role": m.get("role"),
            "townHallLevel": m.get("townHallLevel"),
            "trophies": m.get("trophies")
        } for m in raw_data.get("memberList", [])
    ]
    return {"status": "success", "data": parsed}

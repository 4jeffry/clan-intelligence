class IngestionService:
    def parse_clan_data(self, raw_json: dict):
        return {
            "clan_tag": raw_json.get("tag"),
            "name": raw_json.get("name"),
            "clan_level": raw_json.get("clanLevel", 1),
            "member_count": raw_json.get("members", 0)
        }

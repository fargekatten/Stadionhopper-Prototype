matches = [
    {
        "id": 1,
        "home": "Molde FK",
        "away": "Aalesund FK",
        "date": "2026-10-12",
        "time": "19:00",
        "stadium": "Åråsen Stadion"
    },
    {
        "id": 2,
        "home": "Kristiansund BK",
        "away": "Ranheim IL",
        "date": "2026-10-15",
        "time": "18:00",
        "stadium": "Nordmøre Arena"
    }
]

user_profile = {
    "name": "Oda",
    "favorite_club": "Molde FK",
    "visited_matches": 3
}


def get_matches():
    return matches


def register_checkin(match_id):
    for match in matches:
        if match["id"] == match_id:
            return f"Du registrerte et besøk på {match['home']} vs {match['away']}"
    return "Kampen ble ikke funnet"


def get_user_profile():
    return user_profile

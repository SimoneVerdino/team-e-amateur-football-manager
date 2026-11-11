# Supported formations
FORMATIONS = {
    "4-4-2": [
        "Goalkeeper",
        "Right Back",
        "Centre Back",
        "Centre Back",
        "Left Back",
        "Right Midfielder",
        "Centre Midfielder",
        "Centre Midfielder",
        "Left Midfielder",
        "Striker",
        "Striker"
    ],

    "4-3-3": [
        "Goalkeeper",
        "Right Back",
        "Centre Back",
        "Centre Back",
        "Left Back",
        "Centre Midfielder",
        "Centre Midfielder",
        "Centre Midfielder",
        "Right Winger",
        "Striker",
        "Left Winger"
    ]
}


def display_formations():
    print("Available formations:")

    for formation in FORMATIONS:
        print(formation)


def select_formation():
    display_formations()

    formation = input("Choose a formation: ")

    if formation in FORMATIONS:
        return formation

    print("Invalid formation.")
    return None


def display_positions(formation):
    print(f"\nFormation: {formation}")
    print("Required positions:")

    for position in FORMATIONS[formation]:
        print(f"- {position}")
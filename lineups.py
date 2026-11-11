# Supported formations
FORMATIONS = {
    "442": [
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

    "433": [
        "Goalkeeper",
        "Right Back",
        "Centre Back",
        "Centre Back",
        "Left Back",
        "Centre Midfielder",
        "Holding Midfielder",
        "Centre Midfielder",
        "Right Winger",
        "Striker",
        "Left Winger"
    ],

    "4231": [
        "Goalkeeper",
        "Right Back",
        "Centre Back",
        "Centre Back",
        "Left Back",
        "Holding Midfielder",
        "Holding Midfielder",
        "Attacking Midfielder",
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
from lineups import select_formation, display_positions


def main():
    print("AMATEUR FOOTBALL MANAGER")
    print("------------------------")

    formation = select_formation()

    if formation is not None:
        display_positions(formation)


if __name__ == "__main__":
    main()
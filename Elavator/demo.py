from .elevator_system import ElevatorSystem


def main() -> None:
    system = ElevatorSystem(num_elevators=3, max_floor=10)

    # Scenario 1: Someone on floor 5 presses UP
    print("=== Scenario 1: Floor 5 presses UP ===")
    system.status()
    system.floor_button(5).press_up()
    system.process_all()
    system.status()

    # Scenario 2: Someone on floor 3 presses DOWN
    print("=== Scenario 2: Floor 3 presses DOWN ===")
    system.floor_button(3).press_down()
    system.process_all()
    system.status()

    # Scenario 3: Passenger inside elevator 0 selects floor 8
    print("=== Scenario 3: Elevator 0 internal button -> floor 8 ===")
    system.elevator_button_press(0, 8)
    system.process_all()
    system.status()

    # Scenario 4: Multiple simultaneous requests
    print("=== Scenario 4: Multiple requests (2F UP, 7F DOWN, 9F DOWN) ===")
    system.floor_button(2).press_up()
    system.floor_button(7).press_down()
    system.floor_button(9).press_down()
    system.process_all()
    system.status()


if __name__ == "__main__":
    main()

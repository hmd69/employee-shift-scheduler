import json
import os

DAYS_ORDER = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def load_shifts(filepath="shifts.json"):
    """Load employee shifts from a JSON file."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_shifts(shifts, filepath="shifts.json"):
    """Save employee shifts to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(shifts, file, indent=2)


def get_sorted_shifts(shifts):
    """Return shifts sorted chronologically by day of the week and start time."""
    return sorted(
        shifts,
        key=lambda s: (
            DAYS_ORDER.index(s["day"]) if s["day"] in DAYS_ORDER else 99,
            s["start"],
        ),
    )


def has_conflict(shifts, employee, day):
    """Check if an employee is already scheduled on the given day."""
    return any(
        s["employee"].strip().lower() == employee.strip().lower()
        and s["day"].strip().lower() == day.strip().lower()
        for s in shifts
    )


def add_shift(shifts, employee, role, day, start, end):
    """Validate and add a new shift to the schedule."""
    formatted_day = day.strip().capitalize()
    if formatted_day not in DAYS_ORDER:
        return False, f"Invalid day '{day}'. Must be a valid day of the week."

    if has_conflict(shifts, employee, formatted_day):
        return (
            False,
            f"Conflict: {employee.strip()} is already scheduled on {formatted_day}.",
        )

    next_id = max((s["id"] for s in shifts), default=0) + 1
    new_shift = {
        "id": next_id,
        "employee": employee.strip(),
        "role": role.strip(),
        "day": formatted_day,
        "start": start.strip(),
        "end": end.strip(),
    }
    shifts.append(new_shift)
    return True, f"Shift added for {new_shift['employee']} on {formatted_day}."


def display_schedule(shifts):
    """Print the weekly schedule sorted by day."""
    sorted_shifts = get_sorted_shifts(shifts)
    if not sorted_shifts:
        print("\nNo shifts scheduled.")
        return

    print("\n--- La Table du Parc | Weekly Shift Schedule ---")
    print(f"{'ID':<4} {'Day':<11} {'Hours':<13} {'Employee':<12} {'Role':<10}")
    print("-" * 54)
    for s in sorted_shifts:
        hours = f"{s['start']}-{s['end']}"
        print(
            f"{s['id']:<4} {s['day']:<11} {hours:<13} {s['employee']:<12} {s['role']:<10}"
        )
    print("-" * 54)


def main():
    filepath = "shifts.json"
    shifts = load_shifts(filepath)

    while True:
        print("\n1. View weekly schedule")
        print("2. Add a new shift")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            display_schedule(shifts)
        elif choice == "2":
            employee = input("Employee name: ")
            role = input("Role (Server/Chef/Host): ")
            day = input("Day (Monday-Sunday): ")
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")
            success, message = add_shift(shifts, employee, role, day, start, end)
            print(message)
            if success:
                save_shifts(shifts, filepath)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        filled = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key) or "N/A"
            filled = filled.replace(f"{{{key}}}", str(value))

        with open(f"output_{index}.txt", "w") as f:
            f.write(filled)


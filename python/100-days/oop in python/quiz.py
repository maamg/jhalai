def get_event_date(event):
    return event.date


def get_current_user(events):
    events.sort(key=get_event_date)
    machines= {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "Login":
            machines[event.machine].add(event.user)
        elif event.type == "Logout":
            machines[event.machine].remove(event.user)
        return machines


def generate_report(machines):
    for machine, user in machines.items():
        if len(user) > 0:
            user_list = "".join(user)
            print(f"{machine:} {user}")


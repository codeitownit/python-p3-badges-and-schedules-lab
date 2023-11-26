def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    messages = [f"Hello, my name is {name}." for name in names]
    return messages

def assign_rooms(names):
    room_messages = []
    rooms = 1
    for name in names:
        message = f"Hello, {name}! You'll be assigned to room {rooms}!"
        room_messages.append(message)
        rooms += 1
    return room_messages

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
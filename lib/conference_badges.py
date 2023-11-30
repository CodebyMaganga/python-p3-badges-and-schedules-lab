def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    new_list = list()
    for name in names:
        msg = f'Hello, my name is {name}.'
        new_list.append(msg)
    return new_list

def assign_rooms(names):
    rooms_available = []
    for index, name in enumerate(names, start=1):
        rooms_available.append(f"Hello, {name}! You'll be assigned to room {index}!")
    return rooms_available
def printer(names):
    for name in names:
        print(badge_maker(name))
    for index, name in enumerate(names, start=1):
        print(f"Hello, {name}! You'll be assigned to room {index}!")
    

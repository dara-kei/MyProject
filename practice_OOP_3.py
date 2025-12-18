
def get_item(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return None

data = [10, 20, 30]
print(get_item(data, 1))
print(get_item(data, 5))
print(get_item(data, "2"))

print("------------------------")


from dataclasses import dataclass

@dataclass
class User:
    username : str
    is_active : bool = True
    role : str = "user"

u1 = User("alice")
u2 = User("bob", is_active = False)
u3 = User("admin", role = "admin")

print(u1)
print(u2)
print(u3)


print("------------------------")


from enum import Enum

class Role(Enum):
    ADMIN = 1
    MANAGER = 2
    VIEWER = 3

def has_access(role : Role, *, can_edit : bool = False) -> bool:
    if role is Role.ADMIN:
        return True
    elif role is Role.MANAGER:
        return not can_edit
    elif role is Role.VIEWER:
        return not can_edit
    return False

print(has_access(Role.ADMIN, can_edit = True))
print(has_access(Role.MANAGER, can_edit = True))
print(has_access(Role.MANAGER, can_edit = False))
print(has_access(Role.VIEWER, can_edit = False))


print("------------------------")


def test_info(author, component):
    def wrapper(cls):
        cls.author = author
        cls.component = component
        return cls
    return wrapper

@test_info(author = "alice", component = "Auth")
class TestLogin:
    pass

print(TestLogin.author)
print(TestLogin.component)
age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False


if police_check(12):
    print("go on")
else:
    print("prison")

my_list = ["a", "b", "c"]

for letter in my_list:
    print(letter)
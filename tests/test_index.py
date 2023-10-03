dict_test = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя"
}

def monday_test() : assert dict_test.get(0) == "Понеділок"
def tuesday_test() : assert dict_test.get(1) == "Вівторок"
def wednesday_test() : assert dict_test.get(2) == "Середа"
def thursday_test() : assert dict_test.get(3) == "Четвер"
def friday_test() : assert dict_test.get(4) == "П'ятниця"
def saturday_test() : assert dict_test.get(5) == "Субота"
def sunday_test() : assert dict_test.get(6) == "Неділя"

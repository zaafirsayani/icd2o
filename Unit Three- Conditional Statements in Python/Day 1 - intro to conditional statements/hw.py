# question 1
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
    if speed <= 60:
        return "No ticket"
    if 61 <= speed <= 80:
        return "Small Ticket"
    return "Big Ticket"

print(caught_speeding(73, True))
print(caught_speeding(83, True))
print(caught_speeding(83, False))

#############################################
#question 2
def not_string(s):
    if len(s[0:4]) == "not":
        return (f"not{s}")

print(not_string("nothing"))

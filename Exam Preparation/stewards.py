from collections import deque

seats = input().split(", ")
first_line = deque(int(elem) for elem in input().split(", "))
second_line = deque([int(x) for x in input().split(", ")])

matched_seats = []
rotations = 0

while True:

    if rotations == 10:
        break
    elif len(matched_seats) == 3:
        break

    num_one = first_line.popleft()
    num_two = second_line.pop()
    letter = chr(num_one + num_two)
    potential_seat_one = str(num_one) + letter
    potential_seat_two = str(num_two) + letter

    if potential_seat_one in seats and potential_seat_one not in matched_seats:
        matched_seats.append(potential_seat_one)
        seats.remove(potential_seat_one)

    elif potential_seat_two in seats and potential_seat_two not in matched_seats:
        matched_seats.append(potential_seat_two)
        seats.remove(potential_seat_two)
    else:
        first_line.append(num_one)
        second_line.appendleft(num_two)
    rotations += 1

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")

vip = int(input())

reservation_numbers = set()

for _ in range(vip):
    current_number = input()
    reservation_numbers.add(current_number)

command = input()

while command != "END":
    if command in reservation_numbers:
        reservation_numbers.remove(command)
    command = input()

print(len(reservation_numbers))

for i in sorted(reservation_numbers):
    print(i)

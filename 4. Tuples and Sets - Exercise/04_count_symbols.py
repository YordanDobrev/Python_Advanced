text = input()

symbol_counter = {}

for index in range(len(text)):
    if text[index] not in symbol_counter.keys():
        symbol_counter[text[index]] = text.count(text[index])

for key, value in sorted(symbol_counter.items()):
    print(f"{key}: {value} time/s")

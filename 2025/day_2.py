def is_repeated_seq(id: str) -> bool:
    # print(id)
    for i in range(1, len(id)):
        seq = id[:i]
        # print(f"sequence is {seq}")
        ratio = int(len(id)/len(seq))
        # print(f"ratio is {ratio}")
        if seq * ratio == id:
            print(f"{id} is repeating on {seq}")
            return True
    return False

def is_repeated_twice(id: str):
    # Odd lengths cannot be repeated twice
    if len(id) % 2 == 1:
        return False
    
    # Check if the digits are repeated
    half_idx = int(len(id) / 2)
    first_half = id[:half_idx]
    second_half = id[half_idx:]

    if first_half == second_half:
        return True
    
    return False

def is_valid_id(id: str) -> bool:
    if is_repeated_seq(id):
        return False

    return True


def check_ids() -> int:
    total = 0
    with open("day_2.txt", "r") as file:
        data = file.read()
        id_ranges = data.split(",")

        for id_range in id_ranges:
            id_range_portions = id_range.split("-")
            if len(id_range_portions) > 2:
                raise Exception("Invalid id range")
            start = int(id_range_portions[0])
            end = int(id_range_portions[1])

            for id in range(start, end+1):
                if is_valid_id(str(id)):
                    continue
                else:
                    total += id

    return total

total = check_ids()
print(f"The total invalid id count is: {total}" )


# Part 2
# Attempt 1: 26726777343
# Answer: 27469417404
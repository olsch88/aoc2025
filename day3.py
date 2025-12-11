
import time
import itertools
def read_data(filename:str)-> list[str]:
    with open(filename) as f:
        data = f.readlines()
    data=[line.strip() for line in data]
    return data

def find_max_joltage(numbers: str, batteries=2)-> int:
    max_value=0
    for nums in itertools.combinations(numbers, batteries):
        num = int("".join(nums))
        if num >max_value:
            max_value=num            
    return max_value

def find_max_joltage_part2(numbers: str, batteries=2)-> int:
    max_value=0
    solution=[""]*len(numbers)
    nums_int=[int(n) for n in numbers]
    print(nums_int)
    for i in range(batteries):
        max_= max(nums_int)
        index_= nums_int.index(max_)
        solution[index_]=str(max_)
        nums_int[index_]=0
    print(solution)
    while "" in solution:
        solution.remove("")
    num=int("".join(solution))
    print(num)
    return num

def solve_part1(data: list[str])-> int:
    joltage_sum=0
    for bank in data:
        joltage_sum+=find_max_joltage(bank)
    return joltage_sum

def solve_part2(data: list[str])-> int:
    joltage_sum=0
    for bank in data:
        joltage_sum+=find_max_joltage(bank,12)
    return joltage_sum

def tests():
    assert find_max_joltage("987654321111111")==98
    assert find_max_joltage("811111111111119")==89
    assert find_max_joltage("234234234234278")==78
    assert find_max_joltage("818181911112111")==92
    assert find_max_joltage("818181911112111",12)==888911112111
    
    assert solve_part1(read_data("day3_sample.txt"))==357
    assert solve_part2(read_data("day3_sample.txt"))==3121910778619

if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("day3_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("day3_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")

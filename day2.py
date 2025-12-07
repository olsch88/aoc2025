import textwrap
import time
def read_data(filename:str)-> list[dict]:
    with open(filename) as f:
        data = f.readline()
    ranges=[]
    for pair in data.split(","):
        first, last = pair.split("-")
        ranges.append({"first": int(first), "last":int(last)})
    return ranges

def find_invalid_part2(number: str)->bool:
    for i in range(1,len(number)//2+1):
        if len(number)%i!=0:
            continue
        sub_texts= textwrap.wrap(number, i)
        if len(set(sub_texts))==1:
            # print(f"{number} is invalid")
            return True
    return False


def solve_part1(ranges: list[dict])-> int:
    invalid_sum= 0
    for pair in ranges:
        for number in range(pair["first"], pair["last"]+1):
            if str(number)[:len(str(number))//2]==str(number)[len(str(number))//2:]:
                invalid_sum+= number
    return invalid_sum

def solve_part2(ranges: list[dict])-> int:
    invalid_sum=0
    for pair in ranges:
        for number in range(pair["first"], pair["last"]+1):
            if find_invalid_part2(str(number)):
                invalid_sum+=number
    return invalid_sum

def tests():
    assert find_invalid_part2("11")==True
    assert find_invalid_part2("111")==True
    assert find_invalid_part2("824824824")==True

if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("day2_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("day2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")

def read_data(filename: str)->list[str]:
    with open(filename) as f:
        data= [line.strip() for line in f.readlines()]
    return data


def solve_part1(list_of_dials:list[str])->int:
    value =50
    count_zeros=0
    for dial in list_of_dials:
        direction=dial[0]
        distance=int(dial[1:])
        if direction=="R":
            value= (value+distance)%100
        if direction=="L":
            value = ((value-distance)+100)%100
        if value == 0:
            count_zeros+=1
    return count_zeros

def solve_part2(list_of_dials:list[str])->int:
    value =50
    count_zeros=0
    for dial in list_of_dials:
        direction=dial[0]
        distance=int(dial[1:])
        if direction=="R":
            value= (value+distance)
            while value>99:
                count_zeros+=1
                value= value-100            
        if direction=="L":
            value = value-distance
            while value<0:
                count_zeros+=1
                value=value+100
        print(value)
    return count_zeros


def tests():
    assert solve_part1(read_data("day1_sample.txt"))==3
    assert solve_part2(read_data("day1_sample.txt"))==6

if __name__=="__main__":
    tests()
    print(solve_part1(read_data("day1_input.txt")))
    print(solve_part2(read_data("day1_input.txt")))
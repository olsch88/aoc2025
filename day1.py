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


# def solve_part2(list_of_dials:list[str])->int:
#     value =50
#     count_zeros=0
#     for dial in list_of_dials:
#         direction=dial[0]
#         distance=int(dial[1:])
#         if direction=="R":
#             count_zeros+= (value+distance)//100
#             print(f"\t {dial} added 0")
#             # count_zeros+= distance//100
#             value= (value+distance)%100
#         if direction=="L":
#             count_zeros+= abs((value-distance)//100)
#             value = ((value-distance)+100)%100
#             # if value == 0:
#             #     count_zeros+=1
#     print(count_zeros)
#     return count_zeros

def solve_part2(list_of_dials:list[str])->int:
    value =50
    count_zeros=0
    for dial in list_of_dials:
        if value == 0:
            count_zeros+=1 
        print(dial)
        direction=dial[0]
        distance=int(dial[1:])
        if direction=="R":
            # if value == 0:
            #     count_zeros-=1
            value= (value+distance)
            while value>99:
                print(f"  {dial} added 0")
                count_zeros+=1
                value= value-100            
        if direction=="L":           
        #     if value == 0:
        #         count_zeros+=1 
            value = value-distance
            while value<0:
                print(f"  {dial} added 0")
                count_zeros+=1
                value=value+100
        print(f"Pointing at {value}")
        
    print(count_zeros)
    return count_zeros


def tests():
    assert solve_part1(read_data("day1_sample.txt"))==3
    assert solve_part2(read_data("day1_sample.txt"))==6
    assert solve_part2(read_data("day1_sample3.txt"))==2
    assert solve_part2(read_data("day1_sample2.txt"))==1

if __name__=="__main__":
    tests()
    print(solve_part1(read_data("day1_input.txt")))
    print(solve_part2(read_data("day1_input.txt")))
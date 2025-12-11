
import time
from collections import deque

def read_data(filename:str)-> dict:
    with open(filename) as f:
        data = f.readlines()
    connections=dict()
    for line in data:
        connections[line.split()[0][:3]]= line.split()[1:]
        
    return connections


def solve_part1(connections: dict)-> int:
    queue = deque()
    start="you"
    ways=0    
    queue.append(start)
    while len(queue)!=0:
        current=queue.pop()
        if current=="out":
            ways+=1
            continue
        for target in connections[current]:
            queue.append(target)
    return ways

def solve_part2(connections: dict)-> int:
    queue = deque()
    start="svr"
    ways=0
    visited=set()
    queue.append((start, visited))
    while len(queue)!=0:
        current_visited: set
        current, current_visited=queue.pop()
        if current=="out":
            if "fft" in current_visited and "dac" in current_visited:
                print(current_visited)
                ways+=1
                print(ways)
            continue
        for target in connections[current]:
            if target in current_visited:
                continue
            visited=current_visited.union({current})
            queue.append((target, visited))
    return ways


def tests():
    assert solve_part1(read_data("day11_sample.txt"))==5
    assert solve_part2(read_data("day11_sample2.txt"))==2

if __name__ == "__main__":    
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("day11_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("day11_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")

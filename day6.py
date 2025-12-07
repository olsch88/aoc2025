def read_data(filename:str)->list[list]:
    with open(filename) as f:
        data=f.readlines()
    
    grid=[[element for element in line.strip().split()]for line in data]
    return grid

def solve_part1(grid:list[list]):
    depth= len(grid)
    grand_total=0
    for col in range(len(grid[0])):
        if grid[-1][col]=="+":
            sub_total=0
            for  row in range(len(grid[:-1])):
                sub_total+= int(grid[row][col])
        if grid[-1][col]=="*":
            sub_total=1
            for  row in range(len(grid[:-1])):
                sub_total*= int(grid[row][col])
        grand_total+=sub_total
    return grand_total
if __name__ =="__main__":
    print(solve_part1(read_data("day6_input.txt")))
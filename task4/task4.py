import sys

def parse_file(file_name):
    with open(file_name, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]
    
def min_operations(nums):
    target = sum(nums) // len(nums)
    moves = 0
    for num in nums:
        moves += abs(num - target)
    return moves
                    
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("How to use: python3 task4.py <file_with_circle_info> <file_with_points_info>")
        sys.exit(1)
    nums = parse_file(sys.argv[1])
    print(min_operations(nums))

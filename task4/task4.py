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
    nums = parse_file(sys.argv[1])
    print(nums)
    print(min_operations(nums))
    print(nums)
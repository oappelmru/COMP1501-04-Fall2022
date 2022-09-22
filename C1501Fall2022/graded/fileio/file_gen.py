import sys
import random

def write_to_file(nums: list, precision: int, filename: str) -> None:
    """
    Write the contents of the list to the file.
    """
    try:
        f_obj = open(filename, "w")
        for num in nums:
            f_obj.write(f"{num:.{precision}f}\n")
        f_obj.close()
    except IOError:
        print(f"Error: Could not write to {filename}, try again.")

def main(n_nums: int, min: int, max: int, precision: int, filename: str) -> None:
    """
    Generate a list of random numbers and write them to a file.
    """
    nums = [random.uniform(min, max) for _ in range(n_nums)]
    write_to_file(nums, precision, filename)

if __name__ == "__main__":
    try:
        n_nums = int(sys.argv[1])
        min = int(sys.argv[2])
        max = int(sys.argv[3])
        precision = int(sys.argv[4])
        filename = sys.argv[5]
        main(n_nums, min, max, precision, filename)
    except (IndexError, TypeError) as e:
        print("Usage: python file_gen.py <n_nums> <min> <max> <precision> <filename>")
        print(f"Error: {e}")
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    even, odd = count_even_odd(nums)
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")

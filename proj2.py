first = int(input("Enter the first number: "))
Last = int(input("Enter the last number: "))

total_sum = 0

print("\nNumber Analysis:\n")
for num in range(first, Last + 1):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    
    # Add to total sum
    total_sum += num

# Display total sum
print(f"\nSum of all numbers from {first} to {Last} is: {total_sum}")
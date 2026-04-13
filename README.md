# 🔢 Number Analysis Program

## 📌 Description

This is a simple Python program that:

* Takes a range of numbers as input from the user
* Identifies whether each number is **even** or **odd**
* Calculates the **sum of all numbers** in the given range

---

## 🚀 Features

* User input for start and end values
* Even/Odd number detection
* Displays results for each number
* Calculates total sum of the range
* Handles invalid input (optional version)

---

## 🧾 Code Example

```python
try:
    first = int(input("Enter the first number: "))
    last = int(input("Enter the last number: "))

    if first > last:
        first, last = last, first

    total_sum = 0

    print("\nNumber Analysis:\n")
    for num in range(first, last + 1):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

        total_sum += num

    print(f"\nSum of all numbers from {first} to {last} is: {total_sum}")

except ValueError:
    print("Please enter valid integers.")
```

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Save the file as `number_analysis.py`
3. Run the program:

```bash
python number_analysis.py
```

---

## 🧪 Example

**Input:**

```
Enter the first number: 1
Enter the last number: 5
```

**Output:**

```
Number Analysis:

1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

---
## 👨‍💻 Author

Your Name : Parth Patel 

---

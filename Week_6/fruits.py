"""
Open a new blank file in VS Code and save it as fruit.py
Copy and paste this code at the top of your fruit program:
Add code to reverse and print fruit_list.
Add code to append "orange" to the end of fruit_list and print the list.
Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
Add code to remove "banana" from fruit_list and print the list.
Add code to pop the last element from fruit_list and print the popped element and the list.
Add code to sort and print fruit_list.
Add code to clear and print fruit_list.
At the bottom of your program write a call to the main function.
"""

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    fruit_list.reverse()
    fruit_list.append("orange")
    i = fruit_list.index("apple")
    print(i)
    fruit_list.insert(i, "cherry")
    fruit_list.remove("banana")
    popped = fruit_list.pop() # Remove the last element from the list.
    # print(f"popped: {popped}")
    fruit_list.sort()
    # fruit_list.clear()
    print(f"reversed: {fruit_list}")
    #print(f"original: {fruit_list}")

if __name__ == "__main__":
    main()  # Call the main function.
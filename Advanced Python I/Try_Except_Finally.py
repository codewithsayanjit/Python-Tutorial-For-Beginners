# Function demonstrating try-except-finally

def main():
    try:
        # Take input from the user and convert it to an integer
        a = int(input("Hey, Enter a number: "))

        # Print the entered number
        print(a)

        # Exit the function
        return

    except Exception as e:
        # Runs if any exception occurs
        print("Error:", e)

        # Exit the function
        return

    finally:
        # This block ALWAYS executes
        # even if there is a return statement above
        print("Hey I am inside finally")

# Call the function
main()
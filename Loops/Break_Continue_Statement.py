# A break statement is used to exit a loop immediately, while a continue statement is used to skip the current iteration of the loop and move on to the next one.

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    
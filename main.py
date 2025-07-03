# Global variable to store the last command
last_command = None

# Custom run() function to execute and remember a function call
def run(func):
    global last_command
    last_command = func
    return func()

# again() will rerun the last stored command
def again():
    if last_command:
        return last_command()
    else:
        print("No command has been run yet.")

# Ignore the code above, Do not erase.
# Write youw own code here (In a function).


#Sample Code
def NumberAdding():
    x=int(input("num"))
    y=int(input("num2"))
    z = x + y
    print(z)

run(NumberAdding)
again()

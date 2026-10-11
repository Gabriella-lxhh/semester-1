# Week 1.2, Session 2: Task 6
## Step 1: Get User Inputs
temperature = int(input("Enter the current temperature in Celsius (integer): "))
pressure = int(input("Enter the machine's pressure in PSI (integer): "))
status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped) (integer): "))
##Step 2: Evaluate Operating Conditions
### Temperature check
if temperature > 80:
    print("Warning: Temperature is too high!the temperature is too high! Recommend shutting down the machine.")
elif 50<= temperature <=80:
    print("The temperature is within safe limits.") 
else:
    print("The machine temperature is low and no action is needed.")
## Pressure check
if pressure > 100:
    print("High pressure is detected and recommend maintenance.")
elif 70<= pressure <=100:
    print("The pressure is stable.")
else:
    print("The pressure is low and the system is operating normally.")
## Step 3: Determine Status
if status == 1:
    if temperature >80 or pressure >100:
        print("The machine is running in unsafe conditions and recommend shutting it down.")
    else:
        print("The machine is operating normally.")
else:
    print("The machine is stopped and no immediate action is needed.")




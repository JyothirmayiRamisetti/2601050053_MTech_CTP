
Parking Area Management System

Description

This project contains a Python script that implements a Parking Area Management System for managing parking slots and vehicles. The parking area contains 100 slots. The system allows vehicles to enter and automatically assigns an available parking slot. It also records the vehicle entry time and calculates the parking fee when the vehicle exits.

Algorithm

The script uses functions to manage parking availability, vehicle entry, and vehicle exit. The step-by-step algorithm is as follows:

Initialize Parking Slots: Create 100 parking slots and mark all slots as available.

Display Availability: Count the available slots and display the number of free parking spaces.

Vehicle Entry: Ask the user to enter the vehicle number. Check whether the parking area has an available slot.

Check Duplicate Vehicle: If the vehicle is already parked, display a message and do not allocate another slot.

Allocate Slot: Select the first available parking slot, remove it from the available slots, and store the vehicle number and entry time.

Vehicle Exit: Ask the user to enter the vehicle number and check whether the vehicle is currently parked.

Calculate Duration: Calculate the time between the vehicle's entry and exit.

Calculate Parking Fee: Calculate the parking fee based on the number of hours the vehicle was parked.

Release Slot: Remove the vehicle information and make the parking slot available again.

Not Found: If the vehicle number is not present in the parking system, display a message indicating that the vehicle was not found.

Input and Output

Input

Enter choice: 1

Available slots: 100 / 100

Enter choice: 2

Enter vehicle number: AP22IDHN

Vehicle AP22IDHN assigned to slot 1.

Enter choice: 3

Enter vehicle number: AP22IDHN

Vehicle AP22IDHN left slot 1.
Duration: 1 hour(s) | Fee: 20 currency units

Output

Available slots: 100 / 100
Vehicle AP22IDHN assigned to slot 1.
Vehicle AP22IDHN left slot 1.
Duration: 1 hour(s) | Fee: 20 currency units

When the vehicle exits:

Vehicle ap22idhnr left slot 1.

Duration: 1 hour(s) | Fee: 20 currency units

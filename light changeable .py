import screen_brightness_control as sbc
import atexit
import time

# Function to reset brightness to the original value
def reset_brightness(original_brightness):
    print(f"Resetting brightness to {original_brightness}%")
    sbc.set_brightness(original_brightness)

# Get the current brightness
original_brightness = sbc.get_brightness()[0]  # Get brightness of the primary display
print(f"Current brightness: {original_brightness}%")

# Set a new brightness (e.g., 50%)
new_brightness = 10
print(f"Changing brightness to {new_brightness}%")
sbc.set_brightness(new_brightness)

# Register the reset function to run when the program exits
atexit.register(reset_brightness, original_brightness)

# Simulate some work (e.g., sleep for 10 seconds)


def timer():
    input("Press Enter types end to stop the progarm: ")
    start_time = time.time()  # Record the start time

    print("if you are sure. Type 'end' to stop the timer.")

    while True:
        user_input = input()
        if user_input.lower() == "end":
            break  # Exit the loop if the user types "end"

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    # Display the elapsed time in seconds
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    timer()
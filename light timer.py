import screen_brightness_control as sbc
import atexit

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
import time
print("Application is running...")
time.sleep(1500)
print("Application finished.")
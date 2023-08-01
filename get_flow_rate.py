import RPi.GPIO as GPIO
import time

def get_flow_rate():
    pulse_count = 0
    start_time = time.time()
    flow_pin = 13  # GPIO 13 in BCM mode

    # Configure GPIO settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(flow_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Interrupt callback function for pulse detection
    def pulse_callback(channel):
        nonlocal pulse_count
        pulse_count += 1

    # Add event detection for falling edges (pulses)
    GPIO.add_event_detect(flow_pin, GPIO.FALLING, callback=pulse_callback)

    while True:
        current_time = time.time()

        # Check if one second has elapsed
        if current_time - start_time >= 1:
            flow_rate = pulse_count / 98

            # Reset the pulse count and start time for the next interval
            pulse_count = 0
            start_time = time.time()

            GPIO.remove_event_detect(flow_pin)
            GPIO.cleanup()
            

            return flow_rate

if __name__ == "__main__":
    print(get_flow_rate())

import serial
from pynput.keyboard import Controller

SERIAL_PORT = "/dev/cu.usbserial-2110"  # Change to your port
BAUD_RATE = 9600
THRESHOLD = 300

KEY_MAP = {
    "Photo": "H",
    "Water": "W",
    "Pressure": "P",
}

keyboard = Controller()


def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line or ": " not in line:
                continue

            label, value = line.split(": ", 1)
            label = label.strip()
            try:
                number = float(value)
            except ValueError:
                continue

            if label in KEY_MAP and number > THRESHOLD:
                key = KEY_MAP[label]
                keyboard.press(key)
                keyboard.release(key)


if __name__ == "__main__":
    main()

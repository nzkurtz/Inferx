import serial, time

PORT = "/dev/ttyHS2"   
BAUD = 115200

print(f"Opening {PORT} at {BAUD} baud...")
try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
except Exception as e:
    print("FAILED to open port:", e)
    exit()

cmd = '{"T":1,"L":0.1,"R":0.1}\n'

print("Sending drive commands...")
for i in range(20):
    ser.write(cmd.encode())
    time.sleep(0.1)

cmd = '{"T":1,"L":-0.1,"R":-0.1}\n'
for i in range(20):
    ser.write(cmd.encode())
    time.sleep(0.1)

cmd = '{"T":1,"L":0,"R":0}\n'
ser.write(cmd.encode())

print("Done.")

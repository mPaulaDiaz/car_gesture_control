import serial


class SerialCommunication:
    def __init__(self):
        #self.com = serial.Serial("COM9", 115200, write_timeout=10)
        print("Serial communication disabled.")

    def sending_data(self, command: str) -> None:
        #self.com.write(command.encode('ascii'))
        print(f'simulation: SENDING DATA: {command}')
        

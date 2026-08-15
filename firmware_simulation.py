import logging

class MotorController:

    def __init__(self):
        self.motor_speed = 0


    def process_comand(self, command: str) -> dict:

        if command == "":
            return {"status":"Error"}
        elif command.startswith("set_speed: "):
            speed = int(command.split(":")[1])

            if speed<0 or speed>101:
                logging.error(f"Error: speed out of range")
                return {"satus":"Error: speed out of range"}



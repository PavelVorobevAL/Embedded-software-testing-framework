import logging

logging.basicConfig(
        filename="device.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)


class MotorController:

    def __init__(self):
        self.motor_speed = 0


    def process_comand(self, command: str) -> dict:

        logging.info(f"Command: {command}")

        if command == "":
            logging.error(f"Error: Empty command")
            return {"status":"Error: Empty command"}
        
        elif command.startswith("Set speed: "):
            speed = int(command.split(":")[1])

            if speed<0 or speed>101:
                logging.error(f"Error: speed out of range")
                return {"satus":"Error: speed out of range"}

        else:
            logging.warning(f"Unknown command {command}")
            return {"status":"Uncknown command"}


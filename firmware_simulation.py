import logging

logging.basicConfig(
        filename="device.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)


class MotorController:

    def __init__(self):
        self.motor_speed = 0


    def process_command(self, command: str) -> dict:

        logging.info(f"Command: {command}")

        if command == "":
            logging.error(f"Error: Empty command")
            return {"status":"Error", "message": "Empty command"}
        
        elif command.startswith("Set speed:"):

            try:
                speed = int(command.split(":")[1])

                if speed<0 or speed>101:
                    logging.error(f"Error: speed out of range")
                    return {"status":"Error", "message":"Speed out of range"}

                self.motor_speed = speed

                logging.info(f"Success: speed equals {speed}")
                return {"status":"Success", "message":"Speed equals {speed}"}
            except ValueError:
                
                logging.error(f"Error: Invalid format '{command}'")
                return {"status": "Error", "message":"Invalid data type"}

        else:
            logging.warning(f"Unknown command {command}")
            return {"status":"Unknown command", "message":"Unknown command {command}"}


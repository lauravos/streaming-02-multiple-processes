
# Import from Python Standard Library

import csv
import random
import time
import logging

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
# Declare program constants (typically constants are named with ALL_CAPS)
INPUT_FILE_NAME = "storms.csv"
OUTPUT_FILE_NAME = "out9.txt"

# Define program functions (bits of reusable code)
def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
    name, year, month, day, hour, lat, long, status, category, wind, pressure, tropicalstorm_force_diameter, hurricane_force_diameter = row
    # use an fstring to create a message from our data
    fstring_message = f"[{name}, {year}, {month}, {day}, {hour}, {lat}, {long}, {status}, {category}, {wind}, {pressure}, {tropicalstorm_force_diameter}, {hurricane_force_diameter}]"

    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared message: {fstring_message}")
    return MESSAGE

def stream_row(input_file_name, output_file_name):
    """Read from input file and stream data."""
    logging.info(f"Starting to stream data from {input_file_name} to {output_file_name}.")

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        logging.info(f"Opened for reading: {input_file_name} and {output_file_name} for writing.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")
        
        header = next(reader)  # Skip header row
        logging.info(f"Skipped header row: {header}")


        for row in reader:
            MESSAGE = prepare_message_from_row(row)
            output_file.write(str(MESSAGE))
            output_file.write("\n")
            output_file.flush()
            logging.info(f"Sent: {MESSAGE} to {output_file_name}.")
            time.sleep(random.uniform(1, 3)) # generate records every 1-3 seconds


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Streaming complete!")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


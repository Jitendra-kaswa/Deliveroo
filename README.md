# Cron Expression Parser

This is a command-line application that parses a cron string to show the times at which it will run. The script is written in Python and can be executed from the terminal.

## How to Run

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/Jitendra-kaswa/Deliveroo.git
   cd Deliveroo
   
2. Ensure you have Python 3 installed on your machine.
3. Run the script by providing the cron expression as a command-line argument:

   ```bash
   python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
4. If the above commind gives error then try below command

   ```bash
   python3 cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

Replace the example cron expression with your desired expression.

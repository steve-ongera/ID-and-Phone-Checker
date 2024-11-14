# Access Validator

## Overview

**Access Validator** is a simple Python-based program that validates user input by verifying the phone number and ID combination entered by the user. If the combination matches a predefined set of credentials, access is granted; otherwise, an "incorrect" message is displayed.

This project is a basic example of using conditionals (if-else) to compare user input with stored values, simulating a basic form of authentication.

## Features

- Prompts the user to enter a phone number and ID.
- Compares the entered values to predefined values stored in the program.
- If the values match, access is granted, and a success message is displayed.
- If the values do not match, an error message is shown.

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone this repository or download the Python file:
    ```bash
    git clone https://github.com/your-username/access-validator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd access-validator
    ```

3. Run the Python script using the command below:
    ```bash
    python access_validator.py
    ```

## Usage

1. Upon running the script, the user will be prompted to enter a phone number and an ID.
2. The program will compare the entered data against predefined values.
3. If the data matches, the program will display **"Access granted"**.
4. If the data does not match, the program will display **"Incorrect"** and prompt the user to try again.

## Code Explanation

Here is a breakdown of the key components of the program:

### User Inputs
- The program prompts the user to input both a **phone number** and **ID**.

### If-Else Logic
- The user input is compared against hardcoded values using **if-else** statements.
- If both the phone number and ID match the predefined values, access is granted.
- If either of them doesn't match, an error message is shown.

### Infinite Loop
- The program continues to ask for the phone number and ID until the user enters the correct combination.

## Example Run

Enter phone number: 123-456-7890 Enter ID: 98765 Access granted!

## Contributing

1. Fork this repository to your GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
4. Commit your changes:
    ```bash
    git commit -am 'Add new feature or bug fix'
    ```
5. Push to the branch:
    ```bash
    git push origin feature-name
    ```
6. Create a pull request with a description of the changes made.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any inquiries, feel free to contact me at:

- Email: your-email@example.com
- GitHub: [@your-username](https://github.com/your-username)


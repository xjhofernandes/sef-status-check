"""Main module to call the main functions"""

import argparse
import run


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Path From Terraform Module.")
    parser.add_argument("-e", "--email", help="Your SEF e-mail Login.", type=str, required=True)
    parser.add_argument("-p", "--password", help="Your SEF password for login.", type=str, required=True)
    parser.add_argument("-b", "--browser", help="Your installed browser to the code usage.", type=str, default="chrome")

    args = parser.parse_args()
    email = args.email
    password = args.password
    browser = args.browser

    run.execute(email, password, browser)

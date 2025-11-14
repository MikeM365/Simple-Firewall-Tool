# Simple Firewall Tool

This is an educational command-line firewall tool built in Python. The project was created to demonstrate and learn core firewall concepts like packet filtering, rule management, and logging in a simplified environment.

## Features

-   **Add Rules:** Define `allow` or `block` rules for specific IP addresses and ports.
-   **Display Rules:** View all currently configured rules in order of precedence.
-   **Simulate Packets:** Test incoming packets against the ruleset to see if they would be allowed or blocked.
-   **View Logs:** See a timestamped log of all packet evaluation decisions and the reasons for them.
-   **Default Deny:** Follows a "default deny" policy, where any packet not explicitly allowed by a rule is blocked.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Run the script from your terminal:
    ```sh
    python simple_firewall.py
    ```
3.  Follow the interactive menu prompts.

# SEF - Residence Status Check

# :world_map: Content

1. [Introduction](#%3Ablue_book%3A-introduction)
2. [System Requirements](#%3Awarning%3A-system-requirements)
3. [How to Execute](#%3Aarrow_forward%3A-how-to-execute)

## :blue_book: Introduction

This script is used to check your Residence Permit Status on the SEF website. 

##### More Information

Technology:
* Python;
* [Selenium](https://www.selenium.dev/)

## :warning: System Requirements

- [Python 3.9+](https://www.python.org/)

##### Install Selenium Library

In the root folder from the repository. Run the command below:"
```cmd
pip install -r requirements.txt
```

## :arrow_forward: How to execute

Just run the command below in the repository root folder:
```python
python sef_status_check -e "YourEmail" -p "YourPassword" -b "firefox" (or "chrome")
```

To execute the code in your local machine, you need to configure some environment variables or just use the .vscode folder with a configured launch.json file.

#### Example of a launch.json file to use in vscode (run or debug):

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "-e", "Your SEF E-mail.",
                "-p", "Your SEF Password.",
                "-b", "Your browser (For now, we only support Firefox and Chrome.)"
            ]
        }
    ]
}
```
Obs: this file needs to be located in .vscode folder in repository root. After the file was configured, you can debug or run the code in vscode without setting environment variables in your machine.

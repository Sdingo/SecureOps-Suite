# SecureOps-Suite
SecureOps Suite is a collection of innovative cybersecurity tools designed to enhance and streamline security operations. This repository features various projects aimed at monitoring, protecting, and analyzing systems to ensure robust security.

## Overview
This suite includes tools and projects that address different aspects of cybersecurity. Each project is aimed at providing practical solutions for real-world security challenges.

### Current Project
#### FileIntegrity Sentinel: 
A file monitoring tool that tracks changes to files, detects unauthorized modifications, and maintains baseline integrity.

### Acknowledgements
The development of FileIntegrity Sentinel was inspired by OAAmine’s basic File Integrity Monitor (FIM). This project builds upon their initial work by adding new features and improvements, including:

###### Enhanced Error Handling:More robust handling of file-related errors and exceptions.
###### Flexible Directory Monitoring: Ability to monitor specified directories with an updated user interface.
###### Selective Monitoring: Options to start and stop monitoring as needed, and switch between different directories.
###### Improved Baseline Handling: More accurate baseline creation and comparison, with additional checks for file deletions and modifications.

###### Note: Contributions are welcome! If you have suggestions, improvements, or new tools to add, please open an issue or submit a pull request.

### Installation On Windows

Visit the [Python Downloads page for Windows](https://www.python.org/downloads/windows/) select the desired version of Python.
Download the appropriate installer (Windows x86-64 or x86 executable).
Run the installer and ensure you check both "Install launcher for all users" and "Add Python to PATH."
Select "Install Now" for the recommended options.
Verify the installation by opening the command line and typing python
```shell
> Python
```
### Installation on Linux
  ##### Update Package Lists

Open the terminal and update your package lists:
```shell
sudo apt-get update
```

##### To install Python 3, use:
```shell
sudo apt-get install python3
```

### Installation on macOS
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
##### Install Python3
```shell
brew install python
```
##### Check the installed Python version
```shell
 python3 --version
```

### Running the script
Excecuting the FileIntegrity_Sentinel.py will output a menu on the terminal
Menu:
1. Set/Change Monitoring Directory
2. Create New Baseline
3. Start Monitoring
4. Exit

The prompts should be clear from there!!
###### Note: Improvements might begin from said menu


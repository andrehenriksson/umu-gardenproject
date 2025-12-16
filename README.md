# UMU Garden Project
This project is a small command line utility to track plants and pests in a garden. One can add plants, see their yield and get statistics on total yield in a specific week.
As with any garden, pests can occur (be added) in specific weeks and this will zero out the yield. By caring for the garden all pests can be removed.
## How to use it
Below are the different commands that can be used in the tool:

```
Garden Manager menu:

s - show all plants (sorted alphabetically) and pests (sorted by week)

v - add vegetable
f - add fruit tree
h - harvest (list the yield for all plants in the garden)
c - care for garden
p - add pest
q - quit the program
m - show menu
set - set year and week
```
## Installation
For the installation of the project, please use any command shell you prefer, examples below work in Windows Cmd or Windows PowerShell.
### Create virtual environment
To set up a new Python environment, first navigate to a folder where you want to store the environment and then use the venv module in Python as follows:
```
python -m venv venv_umu_garden
```
There is now a folder created for the virtual environment named venv_umu_garden. To activate this new Python environment run the following command:
```
Windows cmd: venv_umu_garden\Scripts\activate
Windows PowerShell: venv_umu_garden\Scripts\Activate.ps1
```

### Download code
Navigate to a folder where you would like to install the project. Use the git command line tool to download the code for this project
```
git clone https://github.com/andrehenriksson/umu-gardenproject.git
```
### Install dependencies
To install al dependencies to be able to run the code please run the following command in the root folder of the project.
```
pip install -r requirements.txt
```
### Run project
To start using the Garden app type the follwoing:
```
python main.py
```
## Run Unit tests
To run the unit tests of this project, in the root folder of the project use the following command:
```
python -m unittest
```

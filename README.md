# PyBici

PyBici is a Python script that provides the user information about the [MuyBici](https://muybici.org) bike sharing system. It shows the nearest stations with bikes where the user can hire one.

<p align="center">
  <img src="./assets/banner.jpg" width="50%" />
</p>

# Table of Contents

- [PyBici](#pybici)
- [Table of Contents](#table-of-contents)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)

# Technologies

- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
-

# Installation

To install the required libraries run `pip install -r requirements.txt`. Dependency information has been saved using the PIP module [pipreqs](https://github.com/bndr/pipreqs). This writes only the dependencies the project needs to the `requirements.txt` file and not all that are installed on the system.

# Usage

In order to use PyBici you will need to create a `.env` file with the following content:

```env
LATITUDE_COORD = YOUR_LATITUDE_COORD
LONGITUDE_COORD = YOUR_LONGITUDE_COORD
```

Once done this, you can run the script with the following command:

```bash
python3 run.py
```

You will see an output like the following:

```bash
Requesting bike stops within its occupation...
Obtained response. Now calculating the closest stops...

The closest three stops with bikes are:
********************************************************
        Avd de la Libertad: 1 bikes 🚲
        Avd Juan Carlos I: 1 bikes 🚲
        Santo Domingo: 2 bikes 🚲
********************************************************
Have a good ride!
```

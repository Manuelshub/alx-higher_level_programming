# 0x0F-python-object_relational_mapping

## Overview
This project explores the concept of Object-Relational Mapping (ORM) in Python. It focuses on bridging the gap between the object-oriented model in Python and the relational model in databases. This project primarily uses SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Installation
To run this project, you'll need Python installed on your system. Additionally, you'll need to install SQLAlchemy. You can install it via pip:
```
$ pip install sqlalchemy
```


## Usage
This project contains several Python scripts, each demonstrating different aspects of Object-Relational Mapping. Here's a brief overview of each script:

1. `0-select_states.py`: A script that lists all states from the database `hbtn_0e_0_usa`.
2. `1-filter_states.py`: A script that lists all states with a name starting with 'N' from the database `hbtn_0e_0_usa`.
3. `2-my_filter_states.py`: A script that takes in an argument and displays all values in the `states` table of the database `hbtn_0e_0_usa` where `name` matches the argument.
4. `3-my_safe_filter_states.py`: A script that takes in arguments and displays all values in the `states` table of the database `hbtn_0e_0_usa` where `name` matches the argument. This script is safe from SQL injection.
5. `4-cities_by_state.py`: A script that lists all cities from the database `hbtn_0e_4_usa`.
6. `5-filter_cities.py`: A script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.
7. `model_state.py`: A Python file that contains the definition of a `State` class and an instance `Base` of `SQLAlchemy`.
8. `7-model_state_fetch_all.py`: A script that lists all State objects from the database `hbtn_0e_6_usa`.
9. `8-model_state_fetch_first.py`: A script that prints the first State object from the database `hbtn_0e_6_usa`.
10. `9-model_state_filter_a.py`: A script that lists all State objects that contain the letter 'a' from the database `hbtn_0e_6_usa`.
11. `10-model_state_my_get.py`: A script that prints the State object with the name passed as argument from the database `hbtn_0e_6_usa`.
12. `11-model_state_insert.py`: A script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.
13. `12-model_state_update_id_2.py`: A script that changes the name of a State object from the database `hbtn_0e_6_usa`.
14. `13-model_state_delete_a.py`: A script that deletes all State objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa`.
15. `model_city.py`: A Python file that contains the definition of a `City` class.
16. `14-model_city_fetch_by_state.py`: A script that lists all City objects from the database `hbtn_0e_14_usa`.

To run any of these scripts, simply execute them using Python:
```
python3 <script_name.py>
```
Replace `<script_name.py>` with the name of the script you want to run.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


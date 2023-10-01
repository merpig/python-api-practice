# python-api-practice

Simple python project to test api calls and file read/writes

Fetches gifs, and mutate values in the config.json storage file

## Usage
-Only tested on Windows 10 with python version 3.11.5
From the python-api-practice folder:

- install dependencies ```pip install .```
- run ```py .```
    - Equivalent of ```py . -q code``` which fetches 5 random gifs related to code and writes them to config.json
- run ```py . -q {query}```
    - Fetches 5 random gifs related to ```query```. Max limit of 10.


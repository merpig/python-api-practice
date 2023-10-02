# python-api-practice

Simple python project to test api calls and file read/writes

Run various commands to fetch gifs, create basic html page, and mutate values in the config.json storage file

## Usage

-Only tested on Windows 10 with python version 3.11.5-

From the python-api-practice folder:

- install dependencies ```pip install .```
- run ```py .```
    - Equivalent of ```py . -q code``` which fetches 5 random gifs related to code and writes them to config.json
- run ```py . -q {query}```
    - Fetches 5 random gifs related to ```query```. Max limit of 10.
- run ```py . -c``` 
    - Prints list of all gif query terms saved in config.json.
- run ```py . -c -D {term}```
    - Deletes term and term values from config.json.
- run ```py . -g```
    - Generates index.html page displaying saved gifs in config.json

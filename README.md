## Requirements
* The application requires Python >= 3.5
* pyparsing installed `requirements.txt` :
```sh
        python3 -m pip install -r requirements.txt
```
## Usages
 * For interactive mode (via stdin):
```sh
        python main.py
```
 * For text input file:
```sh
        python main.py -i <input_file>
```

 * Full Usages:
```sh
usage: Robot Challenge CLI [-h] [-v] [--input INPUT_FILE] [--width WIDTH] [--height HEIGHT]

optional arguments:
  -h, --help          show this help message and exit
  -v                  Increase verbosity. High verbosity is debug mode
  --input INPUT_FILE  Input file with series of commands. If not specified,
                      script will run in interactive mode via stdin
  --width WIDTH       Width of the grid, default is 5
  --height HEIGHT     Height of the gride, default is 5
```
## Tests
* Run all tests:
```sh
        ./run_all_tests.sh
```
* Run single test:
```sh
        python3 tests/test_parser.py
        ...
```

# Python Keylogger

Key logger made with python. Simple script designed for recording user inputs primarily inside windows os video games.

Original purpose of this script is for gathering information on how should game bots simulate user inputs so that they avoid pattern recognition.

***

# Script setup

Recommendations:

 - **Python 3.10** version minimum
 - Clone into an empty parent repository as the script outputs files into the parent repository (not the current)
 - Run with administrator privileges if the script is not capturing input inside an application

Get the script:

```shell
git clone git@github.com:YenomAdam/python-game-keylogger.git
```

Navigate to project folder:

```shell
cd python-game-keylogger
```

Setup virtual enviroment:

```shell
py -m venv .venv
.\.venv\Scripts\activate
pip install -r "requirements.txt"
```

Run script (Administrator privileges recommended):

```shell
py main.py
```


***

# Script output

Script appends to a file in `..\output\YYYY-MM-DD.jsonl`

For any key press the script records:

- What key
- Focused window
- Key press time start
- Key press time end

For any mouse button press the script records:

- What button
- Focused window
- Button press time start
- Button press time end
- Button press screen coordinates
- Button press path with times when given coordinate was passed

For mouse middle button scroll the script records:

- What button
- Focused window
- Scroll time start
- Scroll screen coordinates
- Scroll direction 
  - (0, 1) = Up
  - (0, -1) = Down

For cursor move withou any mouse buttons being pressed the script records:

- Screen coordinates passed
  - Only every 30th coordinate passed is recorded
- Time of the pass

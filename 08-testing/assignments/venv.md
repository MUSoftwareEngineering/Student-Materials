## Setup a Development Environment
-  Update Python to 3.7:
   - `sudo apt-get install python3.7`
   - `sudo update-alternatives –install /usr/bin/python3 python3 /usr/bin/python3.7 2`
   - `sudo update-alternatives –config python3`
   - Select the option for Python 3.7
- Install Python’s Virtual Environment Tool: ‘pip3 install virtualenv‘
-  Change to your ”home directory” for the next step. For all the operating systems we are
aware of, you accomplish this simply by typing ‘cd‘ and then pressing enter at the command
line.
- Create a Python 3 virtual environment for Augur: `virtualenv –python=python3 testing-assignment`
- Activate your virtual environment `source testing-assignment/bin/activate` (In the case of Ubuntu,
you get the ‘source‘ command automatically put into your path using the ‘bash‘ shell. So, if
you get an error, type ‘bash‘ and then hit the enter key and try again.)

## Virtual environments
create new virual environment in a folder using the command ```python venv -m <env_name>```

To activate the environment in cmd, first cd to the Scripts folder of the virtual environment directory and then run ```actiate.bat```

To deactivate the environmnet run ```deactivate```


## Using a virtual environment in VS Code
Press Ctrl+Shift+P, open workspace settings and click open settings button (page like icon on the top right) to open the .vscode > settings.json file

Then create a key value pair ```"python.pythonPath" : "path\\to\\env_folder\\Scripts\\python.exe"```. This will make VS Code to use the created virtual environment

## install packages
use command ```pip install <package_name>``` to install packages

## dump packages to requirements.txt
use command ```pip freeze > requirements.txt``` to dump packge details to a file named requirements.txt

## restore / install packages from requirements.txt
use command ```pip install -r requirements.txt``` to install packages from requirements.txt

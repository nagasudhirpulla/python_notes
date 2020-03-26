Install argparse using the command ```pip install argparse```

get command line arguments by flag as shown below

```py
# hello.py
import argparse
parser = argparse.ArgumentParser()

# add argument with flag --name
parser.add_argument('--name', help='Persons name')
args = parser.parse_args()

# read name from arguments
name = args.name

if name!=None:
    print('name = {0}'.format(name))
else:
    print('name not provided...')
```

if we run ```hello.py --name Sudhir``` the program will print ```name = Sudhir```

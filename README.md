## Well Known Addresses parser

Parses all the addresses found on the blockchain explorers that have a name attached. It ignores the ones tagged as 'Exploiter', 'Hacker' or coming from Tornado.Cash

## How to use

1. Create parser virtual environment `python3 -m venv env`
2. Activate environment `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Run parser `python3 parser.py [Blockchain explorer] [Pages to Parse]` (-1 if all pages are to be parsed)

For example:

```
python3 parser.py https://etherscan.io/ 10
```

5. Exit the environment with `deactivate`

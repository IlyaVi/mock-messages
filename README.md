# Install and run

```bash
virtualenv --python=python3 ./venv/
source ./venv/bin/activate
pip install -r requirements.txt
python3 main.py

```

## Access 
`localhost:5000`

## format
`{
  "role": "ATTESTER",
  "slot": 2540404,
  "epoch": 79387,
  "round": 1,
  "height": 2540404,
  "signers": [
    66,
    248,
    306,
    325
  ],
  "sync": {
    "version": "v4",
    "network": "holesky"
  },
  "public_key": "87b1c467ac230269dcc9ae1ea683218d76bf06604732dc488c564f55cfdf525d498c413ca3153789761b8351d60705be",
  "message_type": "COMMIT"
}`
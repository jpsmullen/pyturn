# ♻️ pyturn

**pyturn** is a script for checking if a drink container's barcode is registered
with the [Re-turn](https://re-turn.ie/) scheme. It is essentially an unofficial
command-line interface for the
[barcode checker on the Re-turn website](https://re-turn.ie/consumer/#barcodeChecker),
with optional functionality for reading barcodes from a file, and saving
returnable barcodes to a separate file.

The Re-turn scheme is Ireland's
[deposit-return scheme](https://en.wikipedia.org/wiki/Container-deposit_legislation),
launched in February 2024 to reduce littering and increase recycling rates for
plastic bottles and aluminium cans. Between February and June 2024, there was a
transition period, whereby retailers could still sell old drink containers that
didn't have the Re-turn logo on them. Customers were still charged a deposit for
these products, although some of them were eligible to be returned, as their
barcodes were registered with the scheme. This isn't a problem anymore, since
all drink containers sold in Ireland now have the Re-turn logo on them.

This script is almost entirely useless by now, but it still works, and will
likely continue to work for as long as Re-turn have the barcode checker on their
website.

## ✅ requirements

- Python 3.8 (or any later version)
- Cans or plastic bottles with barcodes on them
- An internet connection

## 🛠️ setup

- `git clone https://github.com/jpsmullen/pyturn.git`
- `cd pyturn`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## 🧑‍💻 usage

```
usage: pyturn.py [-h] [-f FILE] [-s] [BARCODES ...]

Check if a drink container's barcode is registered with the Re-turn scheme.

positional arguments:
  BARCODES              the barcodes on your drink containers

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  read barcodes from a text file
  -s, --save            save returnable barcodes to a text file
```

```shell
# Checking barcodes from the command line
python pyturn.py 5000112635676 12345678 4008287058529

# Checking barcodes from a file
python pyturn.py -f barcodes.txt

# Combining the above options, and saving returnables to returnables.txt
python pyturn.py 4061459977998 87654321 -f barcodes.txt -s
```

## ⚠️ disclaimer

I am not affiliated with Re-turn in any way. I just made this for fun.

## ⚖️ licence

pyturn is free software, licensed under the
[GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
(or, at your option, any later version).

Additionally, pyturn uses the following third-party library, which may be used
under its original licence:

- [Requests](https://pypi.org/project/requests/), by Kenneth Reitz,
licensed under [Apache v2.0](https://www.apache.org/licenses/LICENSE-2.0)

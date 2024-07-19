# ♻️ pyturn

`pyturn` is a script for checking if a drink container's barcode is registered
with the [Re-turn](https://re-turn.ie/) scheme.

The Re-turn scheme is Ireland's
[deposit-return scheme](https://en.wikipedia.org/wiki/Deposit-refund_system),
launched in February 2024 to reduce littering and increase recycling rates for
PET bottles and aluminium cans. Between February and June 2024, there was a
transition period, whereby retailers could still sell old drink containers that
didn't have the Re-turn logo on them. Customers were still charged a deposit for
these products, although some of them were eligible to be returned, as their
barcodes were registered with the scheme. (This isn't a problem anymore, since
obviously all drink containers have the Re-turn logo on them by now.)

There's a
[barcode checker on the Re-turn website](https://re-turn.ie/consumer/#barcodeChecker);
`pyturn` is essentially a command-line version of it with additional features.

I wrote a basic version of this script a few months ago, back when it would've
been even somewhat useful, but I've decided to rewrite it and upload it now,
because why not? Maybe it'll come in handy if you find an old can or bottle
lying around somewhere and you want to see if you can use it to get a discount
on your shopping... <sup>I hope...</sup>

## 🛠️ setup

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## 🧑‍💻 usage

```
usage: pyturn.py [-h] [-f FILE] [-o] [BARCODES ...]

A script for checking if a drink container's barcode is registered with the
Re-turn scheme.

positional arguments:
  BARCODES              the barcodes on your drink containers

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  read barcodes from a text file
  -o, --output          save returnable barcodes to a text file
```

```shell
# Checking barcodes from the command line
python pyturn.py 5000112635676 12345678 4008287058529

# Checking barcodes from a file, and saving returnables to returnables.txt
python pyturn.py -f barcodes.txt -o

# Checking and saving barcodes from both the command line and a file
python pyturn.py 4061459977998 87654321 -f barcodes.txt -o
```

## ⚠️ disclaimer

I am not affiliated with Re-turn in any way. I just made this for fun.

## 🧰 dependencies

| Library | Author(s) | Licence |
| --- | --- | --- |
| [Requests](https://pypi.org/project/requests/) | Kenneth Reitz | [Apache v2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ⚖️ licence

[GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) or any later version.

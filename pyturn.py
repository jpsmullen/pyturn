#!/usr/bin/env python3

"""
Check if a drink container's barcode is registered with the Re-turn scheme.
"""

import argparse
import os.path
import sys
import warnings

import requests


def is_barcode(barcode: str) -> bool:
    """Check if a string is a valid barcode."""

    return barcode.isnumeric() and len(barcode) in (8, 12, 13)


def is_returnable(barcode: str) -> bool:
    """Check if a barcode is registered with the Re-turn scheme."""

    url = "https://re-turn.ie/wp-admin/admin-ajax.php"

    data = {
        "action": "barcode_api_callback",
        "barcodeNo": barcode,
    }

    # This is the message you get when the barcode is registered with
    # the scheme, exactly as it's written on the website
    message = \
    "Your drink container is part of Re-turn Ireland’s Deposit Return Scheme."

    try:
        response = requests.post(url, data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}", file=sys.stderr)
        sys.exit(1)

    return message in response.text


def save_to_file(returnables: list[str]) -> None:
    """Save the list of returnable barcodes to a text file."""

    # Save the file in the current working directory (not necessarily
    # the same directory as the script)
    file_path = os.path.join(os.getcwd(), "returnables.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        for barcode in returnables:
            file.write(f"{barcode}\n")

    print(f"Saved returnable barcodes to {file_path}.")


def main() -> None:
    """Main functionality of the script."""

    # Set up argparse
    parser = argparse.ArgumentParser(
        description="""
        Check if a drink container's barcode is registered with the
        Re-turn scheme.
        """,

        add_help=True,
    )

    parser.add_argument(
        "barcodes",
        help="the barcodes on your drink containers",
        nargs="*",
        type=str,
        metavar="BARCODES",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="read barcodes from a text file",
        type=str,
    )

    parser.add_argument(
        "-s",
        "--save",
        help="save returnable barcodes to a text file",
        action="store_true",
    )

    # Show the help message and exit if no arguments are given
    args = parser.parse_args(sys.argv[1:] or ["-h"])

    # Read barcodes from a text file, if one is specified
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as file:
                for line in file:
                    if is_barcode(line := line.strip()):
                        args.barcodes.append(line)
        except OSError as e:
            warnings.warn(str(e))

    returnables = []
    non_returnables = []

    for barcode in args.barcodes:
        if is_barcode(barcode):
            if is_returnable(barcode):
                print(f"{barcode} is returnable.")

                if barcode not in returnables:
                    returnables.append(barcode)
            else:
                print(f"{barcode} is NOT returnable.")

                if barcode not in non_returnables:
                    non_returnables.append(barcode)

    if returnables:
        print(f"\nReturnable barcodes: {returnables}")
        print("Please recycle these at your nearest Re-turn machine.")

        if args.save:
            save_to_file(returnables)

    if non_returnables:
        print(f"\nNon-returnable barcodes: {non_returnables}")
        print("Please put these in your recycling bin.")

    if not (returnables or non_returnables):
        print("No valid barcodes provided.")

    if args.save and not returnables:
        print("No returnable barcodes to save.")


if __name__ == "__main__":
    main()

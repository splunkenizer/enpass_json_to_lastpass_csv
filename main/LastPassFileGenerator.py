import argparse
import csv
import glob
import json
import logging
from io import TextIOWrapper
from pathlib import Path

from main.base import lastpass_row


def getLastPassHeaders(lastpass_json_rows: []) -> []:
    return list(lastpass_json_rows[0].keys())


def getLastPassRows(enpass_rows_json_array,enpass_folders_json_array) -> []:
    lastpass_rows = []
    for enpass_row_json in enpass_rows_json_array:
        lastpass_rows.append(lastpass_row.parse(enpass_row_json,enpass_folders_json_array))

    return lastpass_rows


def getLastPassCSVRows(lastpass_json_rows) -> []:
    lastpass_csv_rows = []
    if len(lastpass_json_rows) > 0:
        lastpass_csv_rows.append(getLastPassHeaders(lastpass_json_rows))
    for lastpass_json_row in lastpass_json_rows:
        lastpass_csv_rows.append(list(lastpass_json_row.values()))

    return lastpass_csv_rows


def generateCSV(lastpass_csv_rows,lastpass_file):
    with open(f'{lastpass_file}', 'w', newline='') as export_file:
        writer = csv.writer(export_file)
        writer.writerows(lastpass_csv_rows)
    logging.info(f"find lastpass csv import file as {lastpass_file}")


def generateLastPassCSV(enpass_file: TextIOWrapper, lastpass_file):
    enpass_json = json.load(enpass_file)
    logging.info(f"enpass json has {len(enpass_json['items'])} entries")

    enpass_rows_json_array = enpass_json['items']
    enpass_folders_json_array = enpass_json['folders']
    lastpass_json_rows = getLastPassRows(enpass_rows_json_array,enpass_folders_json_array)

    lastpass_csv_rows = getLastPassCSVRows(lastpass_json_rows)

    generateCSV(lastpass_csv_rows,lastpass_file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Process input enpass file')
    parser.add_argument('-i', '--input', required=True, dest='filename', type=argparse.FileType('r'),
                        help='absolute path to enpass exported json file')
    parser.add_argument('-o', '--output', required=True, dest='outputfile', type=argparse.FileType('w'),
                        help='absolute path to enpass exported json file')

    args = parser.parse_args()
    logging.info(f"input file of {args.filename.name} entered as enpass exported json")
    logging.info(f"output file of {args.outputfile.name} entered as lastpass import csv")
    generateLastPassCSV(args.filename,args.outputfile.name)


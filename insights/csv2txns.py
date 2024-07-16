import csv
from io import StringIO


def csv2txns(csv_str):
    try:
        return csv2dicts(csv_str)
    except Exception as e:
        raise e


def csv2dicts(csv_str):
    rows = []
    s = StringIO(csv_str)

    r = csv.reader(s, delimiter=",", quotechar="|")
    next(r, None)  # skip header row
    for row in r:
        if len(row) != 7:
            raise Exception("Invalid CSV")

        rows.append(
            {
                "txn_date": row[0],
                "post_date": row[1],
                "description": row[2],
                "category": row[3],
                "type": row[4],
                "amount": row[5],
                "memo": row[6],
            }
        )

    return rows

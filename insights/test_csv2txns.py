import pytest
from .csv2txns import csv2dicts


def test_csv2dicts_valid():
    input = """Transaction Date,Post Date,Description,Category,Type,Amount,Memo
07/14/2024,07/14/2024,Nintendo CA1237412560,Entertainment,Sale,-17.92,
07/14/2024,07/14/2024,Nintendo CA1237414488,Entertainment,Sale,-6.89,
07/09/2024,07/11/2024,TST* STOUP BREWING - CAP,Food & Drink,Sale,-9.28,
07/09/2024,07/11/2024,TST* STOUP BREWING - CAP,Food & Drink,Sale,-9.28,"""

    expected = [
        {
            "txn_date": "07/14/2024",
            "post_date": "07/14/2024",
            "description": "Nintendo CA1237412560",
            "category": "Entertainment",
            "type": "Sale",
            "amount": "-17.92",
            "memo": "",
        },
        {
            "txn_date": "07/14/2024",
            "post_date": "07/14/2024",
            "description": "Nintendo CA1237414488",
            "category": "Entertainment",
            "type": "Sale",
            "amount": "-6.89",
            "memo": "",
        },
        {
            "txn_date": "07/09/2024",
            "post_date": "07/11/2024",
            "description": "TST* STOUP BREWING - CAP",
            "category": "Food & Drink",
            "type": "Sale",
            "amount": "-9.28",
            "memo": "",
        },
        {
            "txn_date": "07/09/2024",
            "post_date": "07/11/2024",
            "description": "TST* STOUP BREWING - CAP",
            "category": "Food & Drink",
            "type": "Sale",
            "amount": "-9.28",
            "memo": "",
        },
    ]

    actual = csv2dicts(input)

    assert expected == actual


def test_csv2dicts_invalid():
    input = "Hello\nWorld"

    with pytest.raises(Exception):
        csv2dicts(input)

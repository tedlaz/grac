import os
import json
from grac.book import Book
# from grac.account import Account
from grac.acc_parse import parse_accounts

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_book_01():
    fil = os.path.join(dir_path, 'graccount_data.json')
    accfil = os.path.join(dir_path, 'ac2.txt')
    accounts_list = parse_accounts(accfil)
    with open(fil) as json_file:
        data = json.load(json_file)
    bo1 = Book()
    bo1.set_account_names(accounts_list)
    bo1.add_transactions_from_list_dic(data)
    print(bo1.check_account_names())
    print(bo1.kartella('38'))
    # print(bo1.accounts)

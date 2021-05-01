from grac.transaction import Transaction


def test_transaction_01():
    tr1 = Transaction('2021-04-30', 'ΤΔΑ32', 'Αγορές', '111222333')
    assert tr1.dat == '2021-04-30'
    tr1.add_line('20.01.00.024', 100)


def test_transaction_from_dictionary():
    dic = {
        'dat': '2021-01-05',
        'par': 'ΤΠ21',
        'per': 'Δοκιμαστική εγγραφή',
        'afm': '222111222',
        'z': [
            {'acc': '20.01.00.024', 'val': 100},
            {'acc': '54.00.20.024', 'val': 24},
            {'acc': '50.00.222111222', 'val': -124},
        ]
    }
    tr1 = Transaction.from_dic(dic)
    assert tr1.isok()
    assert tr1._delta == 0
    assert tr1._number_of_lines == 3
    # print(tr1.account_lines('20.01'))
    # print(tr1)

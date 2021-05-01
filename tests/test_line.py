from grac.line import LineBase


def test_line_01():
    li1 = LineBase('20.01.00.024', 100)
    assert li1.value == 100
    assert li1.debit == 100
    assert li1.credit == 0
    li2 = li1.new_reversed_line()
    assert li2.value == -100
    assert li2.debit == 0
    assert li2.credit == 100
    li2.account.name = 'Αγορές χρήσης'
    assert li1.account == li2.account
    # print(dir(li1))
    # print(li1, li2)

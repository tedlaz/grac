from grac.account import Account


def test_01():
    ac1 = Account('20.01.00.024', 'Αγορές χρήσης')
    assert ac1.omada == '2'


def test_02():
    ac1 = Account('20.01.00.024', 'Αγορές χρήσης')
    ac2 = Account('54.00.20.024', 'ΦΠΑ αγορών 24%')
    ac3 = Account('54.00.20.025')
    assert ac1.name == 'Αγορές χρήσης'
    assert ac2.name == 'ΦΠΑ αγορών 24%'
    assert ac3.name == ''
    ac4 = Account('54.00.20.025', 'Δοκιμή')
    assert ac4.name == 'Δοκιμή'
    assert ac3.name == 'Δοκιμή'

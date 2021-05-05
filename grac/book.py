from .transaction import Transaction
from .account import Account
from .partner import Partner


class Book:
    """Ημερολόγιο λογιστικών εγγραφών class"""

    def __init__(self):
        self.min_date = ''
        self.max_date = ''
        self.trans = []
        self.accounts = []
        # self.partners = []

    @property
    def xrisi(self):
        return self.min_date[:4]

    @staticmethod
    def check_account_names():
        noname = Account.all_without_names()
        if noname:
            print('There are accounts without name')
            return [acc.code for acc in noname]
        return "All accounts have names"

    def set_account_name(self, account, name):
        """Add account name"""
        self.accounts.append(Account(account, name))

    def set_account_names(self, accounts_list):
        """Προσθήκη ονομάτων σε λογαριασμούς μαζικά"""
        for account, name in accounts_list:
            self.set_account_name(account, name)

    def check_transactions(self):
        for trn in self.trans:
            if not trn.isok():
                raise ValueError(f"Transaction {trn} is not ok")
        return 'All transactions are ok'

    def __repr__(self):
        return (
            f"Book(year='{self.xrisi}', trans={len(self.trans)},"
            " min='{self.min_date}, max='{self.max_date}'')"
        )

    def _fix_min_max_date(self, adate):
        # Αποθήκευση ελάχιστης και μέγιστης ημερομηνίας
        if self.min_date == '':
            self.min_date = self.max_date = adate

        if adate > self.max_date:
            self.max_date = adate

        if adate < self.min_date:
            self.min_date = adate

    def _filter_by_date(self, apo: str = '', eos: str = '') -> Transaction:
        for trn in self.trans:
            if apo and trn.dat < apo:
                continue
            if eos and trn.dat > eos:
                continue
            yield trn

    def add_tran(self, transaction: Transaction):
        """Add transaction object. The only way in"""
        self.trans.append(transaction)
        self._fix_min_max_date(transaction.dat)

    def add_tran_from_dic(self, dic):
        """Add a transaction from dictionary"""
        new_transaction = Transaction.from_dic(dic)
        self.add_tran(new_transaction)

    def add_transactions_from_list_dic(self, ldi):
        """Add many transactions from list of dictionaries"""
        for dic in ldi:
            self.add_tran_from_dic(dic)

    def isozygio(self, apo, eos):
        for trn in self._filter_by_date(apo, eos):
            pass

    def kartella(self, account_code: str, apo='', eos='') -> list:
        lines = []
        for trn in self._filter_by_date(apo, eos):
            for lin in trn.account_lines(account_code):
                lines.append(lin)
        return lines

    def ee(self, apo, eos):
        pass

    def imerologio(self, apo, eos):
        pass

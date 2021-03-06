from .partner import Partner
from .line import Line


class Transaction:
    """Greek accounting Transaction class"""

    def __init__(self, dat: str, par: str, per: str, afm: str = ""):
        self.dat = dat  # Ημερομηνία
        self.par = par  # Παραστατικό
        self.per = per  # Περιγραφή
        self.afm = afm  # ΑΦΜ συναλλασσομένου
        self.partner = Partner(afm)
        self.lines = []  # Αναλυτικές γραμμές
        self._number_of_lines = 0
        self._delta = 0

    def account_lines(self, account_code: str) -> list:
        lines = []
        for line in self.lines:
            if line.account.code.startswith(account_code):
                lines.append(line)
        return lines

    def add_line(self, code: str, value: float) -> None:
        self.lines.append(Line(code, value, self))
        self._number_of_lines += 1
        self._delta += value

    @classmethod
    def from_dic(cls, dic: dict):
        trn = cls(dic["dat"], dic["par"], dic["per"], dic.get("afm", ""))
        for lin in dic["z"]:
            trn.add_line(lin["acc"], lin["val"])
        return trn

    def isok(self):
        if self._number_of_lines > 1 and self._delta == 0:
            return True
        return False

    @property
    def is_ee(self):
        """Εάν το άρθρο ανήκει στα Εσοδα-Εξοδα που είναι ουσιαστικά οι
        λογαριασμοί που δίνουν αποτελέσματα
        """
        for line in self.lines:
            if line.account.code.startswith(("2", "6", "7")):
                return True
        return False

    def __repr__(self):
        return (
            f"Transaction(dat='{self.dat}', par='{self.par}',"
            f" per='{self.per}', afm='{self.afm}', lns={self.lines})"
        )

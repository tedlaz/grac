import weakref
ACCOUNT_SPLITTER = "."


class Account:
    """Flyweight implementation of account"""

    _pool = weakref.WeakValueDictionary()

    def __new__(cls, code, name=""):
        # If the object exists in the pool - just return it
        obj = cls._pool.get(code)
        # otherwise - create new one (and add it to the pool)
        if obj is None:
            obj = object.__new__(Account)
            cls._pool[code] = obj
            obj.code, obj.name = code, name
        else:
            """Μπορεί να αλλάξει μόνο το όνομα του λογαριασμού"""
            if name:
                obj.name = name
        return obj

    @staticmethod
    def all():
        return list(Account._pool.values())

    @staticmethod
    def all_without_names():
        alist = []
        for account in Account._pool.values():
            if account.name == '':
                alist.append(account)
        return alist

    def __repr__(self):
        return f"Account(code='{self.code}', name='{self.name}')"

    @property
    def category(self):
        """Κατηγορία λογαριασμού
           1. Πάγιο
           2. Απόθεμα
           3. Απαίτηση
           4. Κεφάλαιο
           5. Υποχρέωση
           6. Έξοδο
           7. Έσοδο
           2 + 6 + 7 + διαφορά απόγραφής = κέρδος περιόδου
           1, 2, 6, 7 μπορεί να έχουν ΦΠΑ
           0 54.00 είναι ο root λογαριασμός ΦΠΑ
        """
        pass

    @property
    def is_ee(self):
        return False

    @property
    def is_numeric(self):
        """Εάν ο code αποτελείται από αριθμούς και splitter"""
        return self.code.replace(ACCOUNT_SPLITTER, "").isdigit()

    @property
    def tree(self) -> tuple:
        spl = self.code.split(ACCOUNT_SPLITTER)
        lvls = [ACCOUNT_SPLITTER.join(spl[: i + 1]) for i in range(len(spl))]
        if self.is_numeric:
            return [self.code[0]] + lvls
        return tuple(lvls)

    @property
    def level(self) -> int:
        return len(self.code.split(ACCOUNT_SPLITTER))

    @property
    def omada(self) -> str:
        return self.tree[0]

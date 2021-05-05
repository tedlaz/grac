"""Module partner"""
import weakref
from tedutil.validators import is_afm


class Partner:
    """Flyweight implementation of parner class"""

    _pool = weakref.WeakValueDictionary()

    def __new__(cls, afm, name=""):
        # If the object exists in the pool - just return it
        obj = cls._pool.get(afm)
        # otherwise - create new one (and add it to the pool)
        if obj is None:
            if afm == '':
                return None
            obj = object.__new__(Partner)
            cls._pool[afm] = obj
            obj.afm, obj.name = afm, name
        else:
            """"""
            if name:
                obj.name = name
        return obj

    @staticmethod
    def invalid_algorithmically_afms():
        error_afm = []
        for afm, obj in Partner._pool.items():
            if not is_afm(afm):
                error_afm.append(obj)
        return error_afm

    @staticmethod
    def all():
        return list(Partner._pool.values())

    @staticmethod
    def all_without_names():
        alist = []
        for partner in Partner._pool.values():
            if partner.name == '':
                alist.append(partner)
        return alist

    def __repr__(self):
        return f"Partner(afm='{self.afm}', name='{self.name}')"

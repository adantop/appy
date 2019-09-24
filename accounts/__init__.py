#!/bin/env python

from contextlib import contextmanager
import sqlite3


@contextmanager
def connect(db):
    con = sqlite3.connect(db)
    yield con.cursor()
    con.commit()


class AccountResource:
    def __init__(self):
        self.db = r'accounts\database.db'
        with connect(self.db) as cur:
            cur.execute('DROP TABLE IF EXISTS ACCOUNTS')
            cur.execute('CREATE TABLE ACCOUNTS (ACCOUNT_ID INT, NAME TEXT, BALANCE FLOAT)')
            cur.execute('INSERT INTO ACCOUNTS VALUES (1, "Adan Torres Paino", 500)')
            cur.execute('INSERT INTO ACCOUNTS VALUES (2, "German Putito Novelo", 1500)')

    def get_accounts(self):
        accounts = list()

        with connect(self.db) as cur:
            cur.execute('SELECT * FROM ACCOUNTS')
            for row in cur.fetchall():
                accounts.append(self.parse_account(row))

        return accounts

    def get_account_by_id(self, accid):
        with connect(self.db) as cur:
            cur.execute('SELECT * FROM ACCOUNTS WHERE ACCOUNT_ID = ?', (accid,))
            result = cur.fetchall()
            acc = self.parse_account(result[0]) if len(result) == 1 else None

        return acc

    @staticmethod
    def parse_account(record):
        return {'balance': record[2], 'name': record[1], 'id': record[0]}

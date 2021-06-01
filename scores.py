#!/usr/bin/env python3

import unittest
import sqlite3
import os
import random

DB_FILE_NAME = "scores.sqlite3.db"

class ScoreBoard:
    def __init__(self, gameName, dbfilename = DB_FILE_NAME):
        self._file = dbfilename
        self._con = sqlite3.connect(dbfilename)
        self._db = self._con.cursor()
        self.game = gameName
        SQL = """
        CREATE TABLE IF NOT EXISTS score (
            id integer PRIMARY KEY,
            player_id text NOT NULL,
            game_id text NOT NULL,
            score float);"""
        self._db.execute(SQL)

    def __del__(self):
        if self._con:
            self.close()

    def close(self):
        self._con.close()

    def createPlayer(self):
        pass

    def playerScores(self, p, s):
        SQL = "INSERT INTO score (player_id, game_id, score) VALUES (?, ?, ?);"
        self._db.execute(SQL, (p, self.game, s) )

    def removeScoreDBFile(self, verify=False):
        if verify:
            self.close()
            os.remove(self._file)
        else:
            print("Argument verify is required to effectively delete the db file, as a security")
            del(self)


def randomName():
    alphabet = list('abcdefghijklmnopqrstuvwxyzxz')
    word = ''.join([random.choice(alphabet) for _ in range(8)])
    return word


TEST_DB_FILE_NAME = "scores.test.sqlite3.db"
class scoreTest(unittest.TestCase):
    def setUp(self):
        self.sc = ScoreBoard(TEST_DB_FILE_NAME)

    def tearDown(self):
        del(self.sc)
        try:
            os.remove(TEST_DB_FILE_NAME)
        except:
            pass

    def testRandomName(self):
        self.assertTrue(len(randomName()) == 8)
        self.assertTrue(randomName().isalpha())

    def testTestLifeCycle(self):
        try:
            os.remove(TEST_DB_FILE_NAME)
        except:
            pass
        scores = ScoreBoard("Tetris", TEST_DB_FILE_NAME)
        scores.playerScores("bill_003", 10)
        self.assertTrue(TEST_DB_FILE_NAME in os.listdir(), "test db file should have been created.")
        del(scores)
        self.assertTrue(TEST_DB_FILE_NAME in os.listdir(), "ScoreObject destruction should not remove db file.")
        scores = ScoreBoard("Tetris", TEST_DB_FILE_NAME)
        scores.removeScoreDBFile(True)
        self.assertFalse(TEST_DB_FILE_NAME in os.listdir(), "test db file should be cleaned up.")




if __name__ == '__main__':
    unittest.main()

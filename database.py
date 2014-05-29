#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database abstraction layer for the whole application.
It creates the needed table in sqlite. it also update them or
change them.
"""

import sqlite3
import config_dict


class DB:
    def __init__(self, db):
        """
        initiate the database.
        """
        self.set_conn(db)
        self.set_cur(self.get_conn())

    def get_conn(self):
        """
        Get the database connection
        """
        return self.conn

    def set_conn(self, db):
        """
        Sets the database connections
        """
        self.conn = sqlite3.connect(db)

    def get_cur(self):
        """
        Gets the curs
        """
        return self.cur

    def set_cur(self, connection):
        """
        Sets the cursor
        """
        self.cur = connection.cursor()

    def create_state_tables(self, table_type):
        """
        create the tables for the initial and final states
        table type would be initState, and finalState
        """
        c = self.get_cur()
        c.execute('''CREATE TABLE {}
                (id integer primary key,
                date text,
                Type2PosVel integer,
                Type0PosVel integer,
                Type1PosVel integer,
                Type8PosVel integer,
                frame text,
                nature text,
                semiMajorAxis real,
                eccentricity real,
                inclination real,
                rAAN real,
                argOfPerigee real,
                meanAnomaly real,
                perigeeAltitude real,
                apogeeAltitude real,
                lambdaEq real,
                eX real,
                eY real,
                iX real,
                iY real,
                x real,
                y real,
                z real,
                vX real,
                vY real,
                VZ real)'''.format(table_type))
db = DB("sat.sql")
db.create_state_tables("initState")

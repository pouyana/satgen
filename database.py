#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database abstraction layer for the whole application.
It creates the needed table in sqlite. it also update them when needed.
"""

import sqlite3


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
        c.execute('''CREATE TABLE IF NOT EXISTS {}
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
                vZ real,
                spaceObjectId integer)'''.format(table_type))

    def create_space_object_table(self):
        """
        creates the space object table,
        the space objects created will be recorded
        here.
        """
        c = self.get_cur()
        c.execute('''CREATE TABLE IF NOT EXISTS spaceObject
                (id integer primary key,
                name text,
                mass real,
                edgeLength real,
                dragArea real,
                reflectingArea real,
                reflectivityCoefficient real,
                orbitType text,
                VariableDragCoef integer,
                CookDragCoef integer,
                ConstantDragCoef integer,
                cstDragCoef real,
                generalId integer,
                initId integer,
                finalId integer,
                iterationId integer
                )''')

    def create_iteration_data_table(self):
        """
        Creates the table needed for the iterationData
        """
        c = self.get_cur()
        c.execute('''CREATE TABLE IF NOT EXISTS iterationData
                (id integer primary key,
                funcValueAccuracy real,
                simMinusExpDuration real,
                expDuration real,
                iterationMethod text,
                spaceObjectId integer)''')

    def create_sim_general_table(self):
        """
        Create the simulation environment general charsteritics
        """
        c = self.get_cur()
        c.execute('''CREATE TABLE IF NOT EXISTS simGeneral
                (id integer primary key,
                author text,
                comment text,
                simulationDuration real,
                ephemerisStep real,
                ttMinusUT1 real,
                srpSwitch integer,
                sunSwitch integer,
                moonSwitch integer,
                warningFlag integer,
                iterativeMode integer,
                modelType text,
                atmosModel text,
                VariableSolarActivity integer,
                solActType text,
                integrationStep real,
                dragSwitch integer,
                dragQuadPoints real,
                atmosDragRecomputeStep real,
                srpQuadPoints real,
                reentryAltitude real,
                nbIntegrationStepTesseral real,
                zonalOrder real,
                spaceObjectId integer)''')

    def create_all_tables(self):
        """
        Creates all the tables needed in the database
        """
        self.create_space_object_table()
        self.create_sim_general_table()
        self.create_iteration_data_table()
        self.create_state_tables("initState")
        self.create_state_tables("FinalState")

    def insert_space_object(self, name):
        """
        Insert the space object in the database.
        returns the row id of inserted element
        """
        conn = self.get_conn()
        c = self.get_cur()
        c.execute('INSERT INTO spaceObject(name) values (?)', (name, ))
        conn.commit()
        return c.lastrowid

    def insert_init_state(self, init_type, space_object_id):
        conn = self.get_conn()
        c = self.get_cur()
        c.execute(
            '''INSERT INTO initState({},
            spaceObjectId) values(?, ?)'''.format(init_type),
            (1, space_object_id))
        conn.commit()
        return c.lastrowid

    def update_value(self, table, column, rowid, value):
        """
        Update a value with given rowid, table, column.
        """
        c = self.get_cur()
        c.execute(
            '''UPDATE {} SET
            {}=? WHERE id=?'''.format(table, column), (value, rowid))
        conn = self.get_conn()

        conn.commit()

#db = DB("sat.sql")
#db.create_all_tables()
#name = "hello"
#rowid = db.insert_space_object(name)
#db.update_value("spaceObject", "name", rowid, "world")

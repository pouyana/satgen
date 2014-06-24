#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database abstraction layer for the whole application.
It creates the needed table in sqlite. it also update them when needed.
"""

import sqlite3
import pint


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
        c.execute('''CREATE TABLE IF NOT EXISTS {0}
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
        self.create_state_tables("finalState")
    
    def get_sat_id_by_name(self, name):
        """
        Search the database with name of the satellite to find
        the id
        """
        conn=self.get_conn()
        c=self.get_cur()
        c.execute("SELECT id from spaceObject where name =?", (name,))
        sat_id = c.fetchone()
        return sat_id

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
        """
        Insert initial points in the table
        """
        conn = self.get_conn()
        c = self.get_cur()
        c.execute(
            '''INSERT INTO initState({0},
            spaceObjectId) values(?, ?)'''.format(init_type),
            (1, space_object_id))
        conn.commit()
        return c.lastrowid

    def insert_final_state(self, config_tuple):
        """
        Insert finalState to the database after extrapolation
        """
        conn = self.get_conn()
        c = self.get_cur()
        c.execute(
            '''INSERT INTO finalState{0} values{1}'''.format(config_tuple["key"], config_tuple["qu"]), config_tuple["value"])
        conn.commit()

    def insert_sim_general(self, space_object_id):
        """
        Insert the Sim general settings in the table
        """
        conn = self.get_conn()
        c = self.get_cur()
        c.execute(
            '''INSERT INTO simGeneral(spaceObjectId) values(?)''', (space_object_id, ))
        conn.commit()
        return c.lastrowid

    def insert_iteration_data(self, space_object_id):
        """
        Insert the iteration data of the simulation
        in table
        """
        conn = self.get_conn()
        c = self.get_cur()
        c.execute(
            '''INSERT INTO iterationData(spaceObjectId) values(?)''', (space_object_id, ))
        conn.commit()
        return c.lastrowid

    def update_value(self, table, column, rowid, value):
        """
        Update a value with given rowid, table, column.
        """
        c = self.get_cur()
        c.execute(
            '''UPDATE {0} SET
            {1}=? WHERE id=?'''.format(table, column), (value, rowid))
        conn = self.get_conn()
        conn.commit()

    def update_all(self, config):
        """
        update all the values at once.
        """
        conn = self.get_conn()
        c = self.get_cur()
        space_object = config.convert_space_object_to_tuple()
        c.execute(
            '''INSERT INTO spaceObject{0} values {1}'''.format(space_object["key"], space_object["qu"]) , space_object["value"])
        conn.commit()
        space_object_id = c.lastrowid
        init_state = config.convert_init_state_to_tuple(space_object_id)
        c.execute(
            '''INSERT INTO initState{0} values {1}'''.format(init_state["key"], init_state["qu"]) , init_state["value"])
        conn.commit()
        sim_general = config.convert_general_sim(space_object_id)
        c.execute(
            '''INSERT INTO simGeneral{0} values{1}'''.format(sim_general["key"], sim_general["qu"]), sim_general["value"])
        conn.commit
        return c.lastrowid
    
    def get_space_objects_data(self,threads):
        """
        Here a list of space objects are create, in respect with the number of 
        instance of MASTER going to run.
        """
        result={}
        conn = self.get_conn()
        c = self.get_cur()
        names_tuple = ("semiMajorAxis","eccentricity","inclination","rAAN","argOfPerigee","meanAnomaly")
        all_rows_init = c.execute(
            '''SELECT id,
            date,
            semiMajorAxis,
            eccentricity,
            inclination,
            rAAN,
            argOfPerigee,
            meanAnomaly
            FROM initState ORDER BY id''')
        all_rows_finish = c.execute(
                            '''SELECT id,
                            date,
                            semiMajorAxis,
                            eccentricity,
                            inclination,
                            rAAN,
                            argOfPerigee,
                            meanAnomaly,
                            spaceObjectId
                            FROM initState ORDER BY spaceObjectId''')
        result["initState"]=all_rows_init.fetchall()
        result["finalState"]=all_rows_finish.fetchall()
        result["names"]=names_tuple
        return result
        
db=DB("satgen.db")
print db.get_space_objects_data(2)

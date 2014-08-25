#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database abstraction layer for the whole application.
It creates the needed table in sqlite. it also update them when needed.
"""

import sqlite3
import pint
import ast
from datetime import datetime


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

    def have_finished_id(self,name):
        """
        Search the database for the finished simulations see dont reextraplote
        them again
        """
        conn=self.get_conn()
        c=self.get_cur()
        c.execute("SELECT finalState.spaceObjectId FROM finalState,spaceObject where spaceObject.name=? and finalState.spaceObjectId = spaceObject.id",(name,))
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
    
    def get_space_objects_data(self):
        """
        Here a list of space objects are create, in respect with the number of 
        instance of MASTER going to run.
        """
        result={}
        conn = self.get_conn()
        c = self.get_cur()
        #names_tuple = ("name", "id",  "init_date", "init_semiMajorAxis","init_eccentricity","init_inclination","init_rAAN","init_argOfPerigee","init_meanAnomaly", "final_id",  "final_date", "final_semiMajorAxis","final_eccentricity", "final_inclination","final_rAAN","final_argOfPerigee","final_meanAnomaly")
#        all_rows_init = c.execute(
#            '''SELECT spaceObject.name,
#            spaceObject.id,
#            initState.date,
#            initState.semiMajorAxis,
#            initState.eccentricity,
#            initState.inclination,
#            initState.rAAN,
#            initState.argOfPerigee,
#            initState.meanAnomaly,
#            finalState.id,
#            finalState.date,
#            finalState.semiMajorAxis,
#            finalState.eccentricity,
#            finalState.inclination,
#            finalState.rAAN,
#            finalState.argOfPerigee,
#            finalState.meanAnomaly
#            FROM initState, spaceObject, finalState Where finalState.spaceObjectId=spaceObject.id and initState.id = spaceObject.id''')
        all_rows_init = c.execute(
            '''SELECT spaceObject.name, finalState.timediff FROM spaceObject,finalState WHERE finalState.timediff < 25.0  and finalState.spaceObjectId=spaceObject.id''')
        aq = all_rows_init.fetchall()
        print len(aq)
        result["length"] = len(aq)
        result["data"]=aq
        return result

    def time_convert(self):
        """
        Get the finishtime and start time and then minus from each other,
        then put it in time difference column
        """
        conn = self.get_conn()
        c = self.get_cur()
        days_in_year = 365.2425
        #add the new column
        try:
            c.execute('''ALTER TABLE finalState add timediff real''')
        except sqlite3.OperationalError as e:
            print "column already exists already exists "+str(e)
        all_start_finish = c.execute('''SELECT finalState.id, 
            initState.date,
            finalState.date from initState,finalState WHERE 
            finalState.spaceObjectId = initState.id''')
        aq = all_start_finish.fetchall()
        for a in aq:
            start_date = datetime.strptime(a[1],"%Y-%m-%dT%H:%M:%S.%f")
            end_date = datetime.strptime(a[2],"%Y-%m-%dT%H:%M:%S.%f")
            time_diff = end_date - start_date
            diff_in_years = time_diff.days/days_in_year
            self.update_value("finalState", "timediff",a[0],diff_in_years)
            print "insrted finalId "+str(a[0])
    def set_u(self):
        """
        Set the U from how big the satellite is
        """
        conn = self.get_conn()
        c = self.get_cur()
        #alter the table to add u
        try:
            c.execute('''ALTER TABLE spaceObject add u real''')
        except sqlite3.OperationalError as e:
            print e
            all_size = c.execute('''SELECT spaceObject.id, spaceObject.edgeLength FROM spaceObject''')
            aq = all_size.fetchall()
            for s in aq:
                tp = ast.literal_eval(s[1])[0] * 10
                self.update_value("spaceObject","u",s[0],tp)
                print "inserted u "+str(tp*10)+"in id "+str(s[0])

    def set_collision_prob(self,master_dir):
        """
        Use the Master Simulations to set the collisions probabilty
        """
        conn = self.get_conn()
        c = self.get_cur()
        all_rows_init = c.execute(
                '''SELECT spaceObject.name, spaceObject.id, spaceObject.dragArea ,finalState.timediff FROM spaceObject,finalState WHERE finalState.timediff < 25.0  and finalState.spaceObjectId=spaceObject.id''')
        aq = all_rows_init.fetchall()
        print len(aq)
        counter =0
        maximum = 0
        for res in aq:
            try:
                f=open(master_dir+"/"+res[0]+"/output/"+res[0]+"_d.atl")
                lines=f.readlines()
                for l in lines:
                    if l.startswith("#   Global Flux:"):
                        a=l.split(" ")
                        global_flux = float(a[len(a)-2])
                        #if global_flux * res[3] * res[2] > maximum:
                        maximum = global_flux * res[3] * res[2]
                        setting = str(global_flux)+","+str(res[2])+","+str(res[3])+","+str(maximum)
                        print setting
            except:
                counter = counter+1
#        print maximum
#        print setting
#conver DB
db=DB("satgen.db")
db.set_collision_prob("master_sim")

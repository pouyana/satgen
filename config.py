#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets/gets different configurations.
If a configuration parameter not given to
the satgen it uses the values in the file.
Satgen can not accept all the parameters
from the command line so please create a configuration file.
"""

from logger import Logger


class Config:
    def __init__(self, log_level="ERROR"):
        logger = Logger(log_level)
        self.log = logger.get_logger()
        self.conf = {}

    def set_abstract_item(self, section, option, value):
        """
        Adds items to the config array
        """
        if section in self.conf.keys():
            self.conf[section][option] = value
        else:
            self.conf[section] = {}
            self.conf[section][option] = value

    def get_abstarct_item(self, section, option):
        """
        Gives the item value back.
        """
        try:
            return self.conf[section][option]
        except KeyError as e:
            self.log.error("Key or value not found please try again ")
            return None

    def get_conf(self):
        """
        Gives the conf dict back
        """
        return self.conf

    def get_config_general(self):
        """
        Gives the General configuration back
        """
        try:
            return self.config["General"]
        except KeyError as e:
            self.log.error("Key General not existant.")
            return None

    def set_model(self, model):
        """
        Set Model in General
        """
        self.set_abstract_item("General", "Model", model)

    def get_model(self):
        """
        Gives Model back
        """
        return self.get_abstarct_item("General", "Model")

    def get_author(self):
        """
        Gives the Author back
        """
        return self.get_abstarct_item("General", "Author")

    def set_autor(self, author):
        """
        Set the autor of config
        """
        self.set_abstract_item("General", "Author", author)

    def get_comment(self):
        """
        Get the comment field
        """
        return self.get_abstarct_item("General", "Comment")

    def set_comment(self, comment):
        """
        Set the comment
        """
        self.set_abstract_item("General", "Comment", comment)

    def get_sim_dur(self):
        """
        Get the Simulation duration in years.
        """
        return self.get_abstarct_item("General", "Simulation duration")

    def get_sim_dur(self, dur):
        """
        Set the Simulation durition in years.
        """
        self.set_abstract_item("General", "Simulation duration", dur)

    def get_ephemeris_step(self):
        """
        Get ephemeris Step in seconds.
        """
        return self.get_abstarct_item("General", "Ephemeris step")

    def set_ephemeris_step(self, step=86400):
        """
        Sets ephemeris Step in seconds.
        Default value is 86400, which is a day.
        """
        self.set_abstract_item("General", "Ephemeris step", step)

    def get_diff_terrestrial_universal_time(self):
        """
        Get the difference Difference between
        terrestrial and universal time in seconds
        """
        return self.get_abstarct_item(
            "General",
            "Difference between terrestrial and universal time")

    def set_diff_terrestrial_universal_time(self, time):
        """
        Set the difference Difference between
        terrestrial and universal time in seconds
        """
        self.set_abstract_item(
            "General",
            "Difference between terrestrial and universal time",
            time)

    def get_int_step(self):
        """
        Get the integration step of the simulation config in seconds
        """
        return self.get_abstarct_item("General", "Integration Step")

    def set_int_step(self, step=86400):
        """
        Set the integration step of the simulation, per default 86400s, a day
        """
        self.set_abstract_item("General", "Integration Setp")

    def get_atmos_drag_switch(self):
        """
        Get the atmospheric drag switch, Boolean.
        """
        return self.get_atmos_drag_switch("General", "Atmospheric drag switch")

    def set_atmos_drag_switch(self, switch=True):
        """
        Set the atmospheric drag, default True
        """
        self.set_abstract_item("General", "Atmospheric drag switch", switch)

    def get_quad_points(self):
        """
        Returns the Drag quadrature Points
        """
        return self.get_abstarct_item("General", "Drag quadrature Points")

    def set_quad_points(self, points=33):
        """
        Sets Drag quadrature Points, default value is 33
        """
        self.set_abstract_item("General", "Drag quadrature Points", points)

    def get_atmos_drag_recom_step(self):
        """
        Retruns the Atmospheric Drag Recompute step
        """
        return self.get_abstract_item(
            "General",
            "Atmospheric Drag Recompute step")

    def set_atmos_drag_recom_step(self, step=1):
        """
        Sets the Atmospheric Drag Recompute step, default is 1.
        """
        self.set_atmos_drag_recom_step(
            "General",
            "Atmospheric Drag Recompute step",
            step)

    def get_solar_rad_pres_switch(self):
        """
        Returns the Solar radiation pressure switch, Boolean
        """
        return self.get_abstarct_item(
            "General",
            "Solar radiation pressure switch")

    def set_solar_rad_pres_switch(self, switch=True):
        """
        Sets the Solar radiation pressure switch, Per default True
        """
        self.set_abstract_item(
            "General",
            "Solar radiation pressure switch",
            switch)

    def get_solar_rad_pres_quad_points(self):
        """
        Gets the Solar radiation pressure quadrature Points
        """
        return self.get_abstarct_item(
            "General",
            "Solar radiation pressure quadrature Points")

    def set_solar_rad_pres_quad_points(self, points=11):
        """
        Sets Solar radiation pressure quadrature Points, per default 11
        """
        self.set_abstract_item(
            "General",
            "Solar radiation pressure quadrature Points",
            points)

    def get_sun_switch(self):
        """
        Gets the Sun switch, Boolean.
        """
        return self.get_abstarct_item("General", "Sun switch")

    def set_sun_switch(self, switch=True):
        """
        Sets the Sun switch value, per default True.
        """
        self.set_abstract_item("General", "Sun switch", switch)

    def get_moon_switch(self):
        """
        Gets the Sun switch value, Boolean
        """
        return self.get_abstarct_item("General", "Moon switch")

    def set_moon_switch(self, switch=True):
        """
        Sets the Moon Switch, per default Boolean True
        """
        self.set_abstract_item("General", "Moon switch", switch)

    def get_zonal_order(self):
        """
        Gets the Zonal order
        """
        return self.get_abstarct_item("General", "Zonal order")

    def set_zonal_order(self, order=7):
        """
        Sets the Zonal order, Per default 7
        """
        self.set_abstract_item("General", "Zonal order", order)

    def get_earth_tesseral_switch(self):
        """
        Get the Earth Tesseral Switch, Boolean
        """
        return self.get_abstarct_item("General", "Earth Tesseral switch")

    def set_earth_tesseral_switch(self, switch=False):
        """
        Sets the Earth Tesseral switch, per default False
        """
        self.set_abstract_item("General", "Earth Tesseral switch", switch)

    def get_reentry_alt(self):
        """
        Gets the Reentry Altitude
        """
        return self.get_abstarct_item("General", "Reentry Altitude")

    def set_reentry_alt(self, alt=120):
        """
        Sets the Reentry Altitude, default 120Km, can't be less than 80.
        """
        while(alt < 80):
            alt = raw_input("The Altitude must be between 140 - 80 KM")
        self.set_abstract_item("General", "Reentry Altitude", alt)

    def set_mass(self, mass):
        """
        Set the mass of the space object in kilo grams
        """
        self.set_abstract_item("Space Object", "Mass", mass)

    def get_mass(self):
        """
        Gives the Mass of the Object back.
        """
        return self.get_abstarct_item("Space Object", "Mass")

    def get_edge_length(self):
        """
        Gets the length of a Cube edge, in m
        """
        return self.get_abstarct_item("Space Object", "Edge Length")

    def set_edge_length(self, length):
        """
        Set the length of a the Cube Edge in m
        """
        self.set_abstract_item("Space Object", "Edge Length", length)

    def get_drag_area(self):
        """
        Get the Drag area of a space object, in m^2
        """
        return self.get_abstarct_item("Space Object", "Drag Area")

    def get_reflect_area(self):
        """
        Get the Reflecting area of the Cube
        """
        return self.get_abstarct_item("Space Object", "Reflecting Area")

    def set_reflect_area(self, number):
        """"
        Sets the refelcting area of the Cubesat.
        The value would be calculated from the numbers
        of the reflecting sides of the cubes.
        """
        if(number < 7):
            self.set_abstract_item(
                "Space Object",
                "Reflecting Area",
                float(
                    self.get_edge_length() * self.get_edge_length() * number))
        else:
            self.log.error("A cube had at most 6 Reflectable sides")

    def get_reflect_coef(self):
        """
        Gets the Reflectivity Coefficient
        """
        return self.get_abstarct_item(
            "Space Object",
            "Reflectivity Coefficient")

    def set_reflect_coef(self, coef=1.5):
        """
        Sets the Reflectivity Coefficient, Default value 1.5.
        Is Material connceted and a mean value should be set.
        """
        self.set_abstract_item(
            "Space Object",
            "Reflectivity Coefficient",
            coef)

    def get_orbit_type(self):
        """
        Gets the orbit type.
        """
        return self.get_abstarct_item("Space Object", "Orbit Type")

    def set_orbit_type(self, orbit="LEO"):
        """
        Sets the orbit type. Default is LEO (Low Earth Orbit)
        """
        self.set_abstract_item("Space Object", "Orbit Type", orbit)

    def get_drag_coef_type(self):
        """
        Gets the Drag Coefficent Type
        """
        return self.get_abstarct_item(
            "Space Object",
            "Drag Coefficent Type")

    def set_drag_coef_type(self, coef="VARIABLE"):
        """
        ets the Drag Coefficent Type
        Per default VARIABLE.
        """
        self.set_abstract_item(
            "Space Object",
            "Drag Coefficient Type",
            coef)

    def get_space_object_name(self):
        """
        Returns the space objcet name.
        """
        return self.get_abstarct_item("Space Object", "Name")

    def set_space_object_name(self, name):
        """
        Sets the space object name
        """
        self.set_abstract_item("Space Object", "Name", name)

    def set_drag_area(self, mode="random"):
        """
        Set the Drag area of space object, in m^2
        The mode can be fixed, random
        The default mode is the random, mode
        before that the edge length must be set.
        """
        try:
            if(self.get_edge_length()):
                if (mode == "fixed"):
                    self.set_abstract_item(
                        "Space Object",
                        "Drag Area",
                        float(self.get_edge_length() * self.get_edge_length()))
                elif (mode == "random"):
                    self.set_abstract_item(
                        "Space Object",
                        "Drag Area",
                        #Drag aera of random spinnig cube is
                        #edge_length * 6/4
                        (float(self.get_edge_length()) * 6/4))
        except:
            self.log.error(
                "The Cube Length is not set"
                "Please set it with set_edge_length(l)")

    def get_atmos_model(self):
        """
        Get the Atmospheric model
        """
        return self.get_abstarct_item("Atmospheric Model", "Atmospheric model")

    def set_atoms_model(self, model="NRLMSISE-00"):
        """
        Sets the Atmospheric model, per default NRLMSISE-00
        """
        self.get_abstarct_item("Atmospheric Model", "Atmospheric model", model)

conf = Config()
conf.set_model("GTO")
conf.set_mass(2)
conf.set_edge_length(0.1)
conf.get_edge_length()
conf.set_drag_area()
print conf.get_conf()

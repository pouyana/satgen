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
            return self.conf[section][item]
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
        return self.get_abstract_item("General", "Atmospheric Drag Recompute step")

    def set_atmos_drag_recom_step(self, step=1):
        """
        Sets the Atmospheric Drag Recompute step, default is 1.
        """
        self.set_atmos_drag_recom_step("General", "Atmospheric Drag Recompute step", step)

    def get_solar_rad_pres_switch(self):
        """
        Returns the Solar radiation pressure switch, Boolean
        """
        return self.get_abstarct_item("General", "Solar radiation pressure switch")

    def set_solar_rad_pres_switch(self, switch=True):
        """
        Sets the Solar radiation pressure switch, Per default True
        """
        self.set_abstract_item("General", "Solar radiation pressure switch", switch)

    def get_solar_rad_pres_quad_points(self):
        """
        Gets the Solar radiation pressure quadrature Points
        """
        return self.get_abstarct_item("General", "Solar radiation pressure quadrature Points")

    def set_solar_rad_pres_quad_points(self, points=11):
        """
        Sets Solar radiation pressure quadrature Points, per default 11
        """
        self.set_abstract_item("General", "Solar radiation pressure quadrature Points", points)

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
        while( alt < 80):
            alt = raw_input("The Altitude must be between 140 - 80 KM")
        self.set_abstract_item("General", "Reentry Altitude", alt)

    def set_mass(self, mass):
        """
        Set the mass of the space object
        """
        self.set_abstract_item("Space Object", "Mass", mass)

    def get_mass(self):
        """
        Gives the Mass of the Object back.
        """
        return self.get_abstarct_item("Space Object", "Mass")


conf = Config()
conf.set_model("GTO")
conf.set_mass(2)
print conf.get_conf()

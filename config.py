    #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets/gets different configurations.
If a configuration parameter not given to
the satgen it uses the values in the file.
Satgen can not accept all the parameters
from the command line so please create a configuration file.
"""

from time import gmtime, strftime
from logger import Logger
from config_dict import ConfigDict
import xml.etree.ElementTree as ET
from xml_pretty import prettify


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

    def get_abstract_item(self, section, option):
        """
        Gives the item value back.
        """
        try:
            return self.conf[section][option]
        except KeyError as e:
            self.log.warning("Key or value not found please try again ")
            return None

    def get_conf(self):
        """
        Gives the conf dict back
        """
        return self.conf

    def set_conf(self, conf):
        """
        Sets the conf file from the conf dict
        """
        self.conf = conf

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
        return self.get_abstract_item("General", "Model")

    def get_author(self):
        """
        Gives the Author back
        """
        return self.get_abstract_item("General", "Author")

    def set_autor(self, author):
        """
        Set the autor of config
        """
        self.set_abstract_item("General", "Author", author)

    def get_comment(self):
        """
        Get the comment field
        """
        return self.get_abstract_item("General", "Comment")

    def set_comment(self, comment):
        """
        Set the comment
        """
        self.set_abstract_item("General", "Comment", comment)

    def get_sim_dur(self):
        """
        Get the Simulation duration in years.
        """
        return self.get_abstract_item("General", "Simulation duration")

    def get_sim_dur(self, dur):
        """
        Set the Simulation durition in years.
        """
        self.set_abstract_item("General", "Simulation duration", dur)

    def get_ephemeris_step(self):
        """
        Get ephemeris Step in seconds.
        """
        return self.get_abstract_item("General", "Ephemeris step")

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
        return self.get_abstract_item(
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
        return self.get_abstract_item("General", "Integration Step")

    def set_int_step(self, step=86400):
        """
        Set the integration step of the simulation, per default 86400s, a day
        """
        self.set_abstract_item("General", "Integration Setp")

    def get_atmos_drag_switch(self):
        """
        Get the atmospheric drag switch, Boolean.
        """
        return self.get_abstract_item("General", "Atmospheric drag switch")

    def set_atmos_drag_switch(self, switch=True):
        """
        Set the atmospheric drag, default True
        """
        self.set_abstract_item("General", "Atmospheric drag switch", switch)

    def get_quad_points(self):
        """
        Returns the Drag quadrature Points
        """
        return self.get_abstract_item("General", "Drag quadrature Points")

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
        return self.get_abstract_item(
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
        return self.get_abstract_item(
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
        return self.get_abstract_item("General", "Sun Switch")

    def set_sun_switch(self, switch=True):
        """
        Sets the Sun switch value, per default True.
        """
        self.set_abstract_item("General", "Sun switch", switch)

    def get_moon_switch(self):
        """
        Gets the Sun switch value, Boolean
        """
        return self.get_abstract_item("General", "Moon switch")

    def set_moon_switch(self, switch=True):
        """
        Sets the Moon Switch, per default Boolean True
        """
        self.set_abstract_item("General", "Moon switch", switch)

    def get_zonal_order(self):
        """
        Gets the Zonal order
        """
        return self.get_abstract_item("General", "Zonal order")

    def set_zonal_order(self, order=7):
        """
        Sets the Zonal order, Per default 7
        """
        self.set_abstract_item("General", "Zonal order", order)

    def get_earth_tesseral_switch(self):
        """
        Get the Earth Tesseral Switch, Boolean
        """
        return self.get_abstract_item("General", "Earth Tesseral switch")

    def set_earth_tesseral_switch(self, switch=False):
        """
        Sets the Earth Tesseral switch, per default False
        """
        self.set_abstract_item("General", "Earth Tesseral switch", switch)

    def get_reentry_alt(self):
        """
        Gets the Reentry Altitude
        """
        return self.get_abstract_item("General", "Reentry Altitude")

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
        return self.get_abstract_item("Space Object", "Mass")

    def get_edge_length(self):
        """
        Gets the length of a Cube edge, in m
        """
        return self.get_abstract_item("Space Object", "Edge Length")

    def set_edge_length(self, length):
        """
        Set the length of a the Cube Edge in m
        """
        self.set_abstract_item("Space Object", "Edge Length", length)
        self.set_drag_area()
        self.set_reflect_area()

    def get_drag_area(self):
        """
        Get the Drag area of a space object, in m^2
        """
        result = self.get_abstract_item("Space Object", "Drag Area")
        if(result):
            return result
        else:
            self.set_drag_area()
            return self.get_drag_area()

    def get_reflect_area(self):
        """
        Get the Reflecting area of the Cube
        """
        result = self.get_abstract_item("Space Object", "Reflecting Area")
        if(result):
            return result
        else:
            self.set_reflect_area()
            return self.get_reflect_area()

    def set_reflect_area(self, number=6):
        """"
        Sets the refelcting area of the Cubesat.
        The value would be calculated from the numbers
        of the reflecting sides of the cubes.Default value of 6.
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
        result = self.get_abstract_item(
            "Space Object",
            "Reflectivity Coefficient")
        if(result):
            return result
        else:
            self.set_reflect_coef()
            return self.get_reflect_coef()

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
        result = self.get_abstract_item("Space Object", "Orbit Type")
        if(result):
            return result
        else:
            self.set_orbit_type()
            return self.get_orbit_type()

    def set_orbit_type(self, orbit="LEO"):
        """
        Sets the orbit type. Default is LEO (Low Earth Orbit)
        """
        self.set_abstract_item("Space Object", "Orbit Type", orbit)

    def get_drag_coef_type(self):
        """
        Gets the Drag Coefficent Type
        """
        return self.get_abstract_item(
            "Space Object",
            "Drag Coefficent Type")

    def set_drag_coef_type(self, coef="VARIABLE"):
        """
        ets the Drag Coefficent Type
        Per default VARIABLE the other value would be the CONSTANT
        """
        self.set_abstract_item(
            "Space Object",
            "Drag Coefficent Type",
            "Drag Coefficent Type "+coef)

    def get_space_object_name(self):
        """
        Returns the space objcet name.
        """
        return self.get_abstract_item("Space Object", "Name")

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
                        (float(
                            self.get_edge_length() *
                            self.get_edge_length()) * 6/4))
        except:
            self.log.error(
                "The Cube Length is not set"
                "Please set it with set_edge_length(l)")

    def get_atmos_model(self):
        """
        Get the Atmospheric model
        """
        return self.get_abstract_item(
            "Atmospheric Model",
            "Atmospheric Model")

    def set_atoms_model(self, model="NRLMSISE-00"):
        """
        Sets the Atmospheric model, per default NRLMSISE-00
        """
        self.get_abstract_item("Atmospheric Model", "Atmospheric model", model)

    def get_solar_activity_type(self):
        """
        Gets the Solar activiy type
        """
        return self.get_abstract_item("Solar Activity", "Solar Activity Type")

    def set_solar_activity_type(self, act_type="MEAN_CONSTANT"):
        """
        Sets the Solar Activity Type, per default is the MEAN_CONSTANT
        """
        self.set_abstract_item(
            "Solar Activity",
            "Solar Activity Type",
            act_type)

    def get_ap_constant_solar_act(self):
        """
        Gets AP Constant Equivalent Solar Activity
        """
        return self.get_abstract_item(
            "Solar Activity",
            "AP Constant Equivalent Solar Activity")

    def set_ap_constant_solar_act(self, ap=15):
        """
        Sets AP Constant Equivalent Solar Activity, default value is 15
        """
        self.set_abstract_item(
            "Solar Activity",
            "AP Constant Equivalent Solar Activity",
            ap)

    def get_f107(self):
        """
        Gets the F10.7 Constant Equivalent Solar Activity
        """
        return self.get_abstract_item(
            "Solar Activity",
            "F10.7 Constant Equivalent Solar Activity")

    def set_f107(self, f107=140):
        """
        Sets F10.7 Constant Equivalent Solar Activity,
        with default value of 140
        """
        self.set_abstract_item(
            "Solar Activity",
            "F10.7 Constant Equivalent Solar Activity",
            f107)

    def get_intial_date(self):
        """
        Gets the initail date of the simulation
        """
        return self.get_abstract_item("Initial Bulletin", "Date")

    def set_initial_date(self, date):
        """
        Sets the date, the date can be dot or - splitted yyyy-mm-dd
        internally it will be changed to yyyy-mm-ddT12:00:00:00.000
        """

    def get_type_of_sim(self):
        """
        Gets the type of Simulation, paramater
        """
        return self.get_abstract_item("Initial Bulletin", "Type")

    def set_type_of_sim(self, sim_type="Perigee/Apogee"):
        """
        Sets the type of simulation, per default Perigee/Apogee
        """
        self.set_abstract_item("Initial Bulletin", "Type", sim_type)

    def get_frame(self):
        """
        Gets the Simulation Frame
        """
        return self.get_abstract_item("Initial Bulletin", "Frame")

    def set_frame(self, frame="CELESTIAL_MEAN_OF_DATE"):
        """
        Sets the Simulation Frame, per default CELESTIAL_MEAN_OF_DATE
        """
        self.set_abstract_item("Initial Bulletin", "Frame", frame)

    def get_nature(self):
        """
        Gets the Nature of Simulation
        """
        return self.get_abstract_item("Initial Bulletin", "Nature")

    def set_nature(self, nature="MEAN"):
        """
        Sets the Nature of Simulation, per default MEAN
        """
        self.set_abstract_item("Initial Bulletin", "Nature", nature)

    def get_preigee_alt(self):
        """
        Gets the Perigee Altitude in Km
        """
        return self.get_abstract_item(
            "Initial Bulletin",
            "Zp (Perigee altitude)")

    def set_perigee_alt(self, alt):
        """
        Sets the perigee Altitude in Km
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "Zp (Perigee altitude)",
            alt)

    def get_apogee_alt(self):
        """
        Gets the Apogee altitude in Km
        """
        return self.get_abstract_item(
            "Initial Bulletin",
            "Za (Apogee altitude)")

    def set_apogee_alt(self, alt):
        """
        Sets the Apogee altitude in Km
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "Za (Apogee altitude)",
            alt)

    def get_incl(self):
        """
        Gets the Inclination in Deg
        """
        return self.get_abstract_item("Initial Bulletin", "I (Inclination)")

    def set_incl(self, inclination):
        """
        Sets the Inclination in Deg
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "I (Inclination)",
            inclination)

    def get_raan(self):
        """
        Gets the RAAN (Right Ascension of Ascending Node) in Deg
        """
        return self.get_abstract_item(
            "Initial Bulletin",
            "RAAN (Right Ascension of Ascending Node)")

    def set_raan(self, rann):
        """
        Sets RAAN (Right Ascension of Ascending Node) in Deg
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "RAAN (Right Ascension of Ascending Node)",
            raan)

    def get_arg_perigee(self):
        """
        Gets the Argument of prigee in Deg
        """
        return self.get_abstract_item(
            "Initial Bulletin",
            "w (Argument of perigee)")

    def set_arg_perigee(self, arg):
        """
        Sets the Argument of perigee in Deg
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "w (Argument of perigee)",
            arg)

    def get_mean_anomaly(self):
        """
        Gets the Mean Anomaly in Deg
        """
        return self.get_abstract_item("Initial Bulletin", "M (Mean anomaly)")

    def set_mean_anomaly(self, anomaly):
        """
        Sets the Mean Anomaly in Deg
        """
        self.set_abstract_item(
            "Initial Bulletin",
            "M (Mean anomaly)",
            anomaly)

    def set_semi_major_axis(self, axis):
        """
        Sets the SemiMajor Axis in km
        """
        self.set_abstract_item("Initial Bulletin", "a (Semi major axis)", axis)

    def get_semi_major_axis(self):
        """
        Gets the SemiMajor Axis in km
        """
        return self.get_abstract_item("Initial Bulletin", "a (Semi major axis)".title())

    def set_eX(self, eX):
        """
        Sets the eX Orbital Parameter
        """
        self.set_abstract_item("Initial Bulletin", "eX", eX)

    def get_eX(self):
        """
        Gets the eX Orbital Parameter
        """
        return self.get_abstract_item("Initial Bulletin", "eX")

    def set_eY(self, eY):
        """
        Sets the eY Orbital Parameter
        """
        self.set_abstract_item("Initial Bulletin", "eY", eY)

    def get_eY(self):
        """
        Gets the eY Orbital Parameter
        """
        return self.get_abstract_item("Initial Bulletin", "eY")

    def set_iX(self, iX):
        """
        Sets the Orbital Parameter iX
        """
        self.set_abstract_item("Initial Bulletin", "iX", iX)

    def get_iX(self):
        """
        Gets the Orbital Parameter iX
        """
        return self.get_abstract_item("Initial Bulletin", "iX")

    def set_iY(self, iY):
        """
        Sets the Orbital Parameter iY
        """
        self.set_abstract_item("Initial Bulletin", "iY", iY)

    def get_iY(self):
        """
        Gets the Orbital Parameter iY
        """
        return self.get_abstract_item("Initial Bulletin", "iY")

    def set_lambdaEq(self, lambdaEq):
        """
        Sets the Orbital Parameter lambdaEq in Deg
        """
        self.set_abstract_item("Initial Bulletin", "lambdaEq", lambdaEq)

    def get_lambdaEq(self):
        """
        Gets the Orbital Parameter lambdaEq in Deg
        """
        return self.get_abstract_item("Initial Bulletin", "lambdaEq")

    def set_epoch_tfe(self, date):
        """
        Sets the epochTFE with the date
        """
        self.set_abstract_item("Initial Bulletin", "epochTFE", date)

    def get_eppch_tfe(self):
        """
        Returns the epochTFE
        """
        return self.get_abstract_item("Initial Bulletin", "epochTFE")

    def set_func_value_accu(self, accu):
        """
        Sets functional Value Accuracy of Iteration in days
        """
        self.set_abstract_item(
            "Iteration Data",
            "Function Value Accuracy",
            accu)

    def get_func_value_accu(self):
        """
        Gets the functional Value Accuracy of Iteration in days
        """
        return self.get_abstract_item(
            "Iteration Data",
            "Function Value Accuracy")

    def get_exp_dur(self):
        """
        Gets the Expiring Duration in years
        """
        return self.get_abstract_item(
            "Iteration Data",
            "Expiring Duration")

    def set_exp_dur(self, dur):
        """
        Sets the expiring duration in years
        """
        self.set_abstract_item(
            "Iteration Data",
            "Expiring Duration")

    def get_sim_minus_exp(self):
        """
        Gets the Simulation Minus Expireing Duration in years
        """
        return self.get_abstract_item(
            "Iteration Data",
            "Simulation Minus Expireing Duration")

    def set_sim_minus_exp(self, exp):
        """
        Sets the Simulation Minus Expireing Duration in years
        """
        self.set_abstract_item(
            "Iteration Data",
            "Simulation Minus Expireing Duration")

    def set_iter_method(self, method="FrozenOrbit"):
        """
        Sets the Iteration Method
        """
        self.set_abstract_item(
            "Iteration Data",
            "Iteration Method",
            method)

    def get_iter_method(self):
        """
        Gets the Iteration Method
        """
        self.get_abstract_item("Iteration Data", "Iteration Method")

    def get_stela_version(self):
        """
        Gets the Stela Version
        """
        return self.get_abstract_item("General", "Stela Version")

    def set_stela_version(self, version):
        """
        Sets the Stela Version
        """
        self.set_abstract_item("General", "Stela Version", version)

    def set_drag_coef_const(self, value):
        """
        Sets the value for the Constant drag coeficient
        """
        if(self.get_conf()["Space Object"]["Drag Coefficent Type"] ==
           "Drag Coefficent Type CONSTANT"):
                self.set_abstract_item(
                    "Space Object",
                    "Constant Drag Coef",
                    value)

    def get_drag_coef_const(self):
        """
        Returns the constant Drag Coefficent
        """
        return self.get_abstract_item("Space Object", "Constant Drag Coef")

    def values_to_keys(self, want_value, dictio):
        """
        Returns key from the given values, for dicts
        """
        for key, is_value in dictio.items():
            if (is_value == want_value):
                return key

    def parse_elements(
            self,
            parent,
            key_value_dict,
            unit_dict=dict(),
            sort_dict=dict(),
            trans_dict=dict(),
            exceptions=list()):
        """
        Parses the keys and values dict with help of 
        unit_dict, sort_dict, transition_dict and the excpetion list.
        """
        conf_dict = ConfigDict()
        sorted_list = sorted(
            key_value_dict.items(),
            key=lambda x: sort_dict.get(x[0]))
        for sort_item in sorted_list:
            if(sort_item[0] not in exceptions and sort_item[0] != "Drag Coefficent Type"):
                tmp_el = ET.SubElement(parent, str(trans_dict[sort_item[0]]))
                tmp_el.text = str(sort_item[1])
                if sort_item[0] in unit_dict:
                    tmp_el.set('unit', str(unit_dict[sort_item[0]]))
            #exception Atmospheric Model
            if(sort_item[0] == "Atmospheric Model"):
                atmos = ET.SubElement(parent, str(trans_dict["Atmospheric model"]))
                atmos.text = self.get_atmos_model()

            #exception Drag Coefficient
            if(sort_item[0] == "Drag Coefficent Type"):
                drag_co_type = self.get_conf()["Space Object"]["Drag Coefficent Type"]
                drag_co_el = ET.SubElement(
                    parent,
                    str(trans_dict["Drag Coefficent Type " + drag_co_type]))
                if(drag_co_type == "Drag Coefficent Type CONSTANT"):
                    drag_co_const = ET.SubElement(
                        drag_co_el,
                        str(trans_dict["Constant Drag Coef"]))
                    drag_co_const.text = str(self.get_drag_co_const())
            #exception Solar Activity
            if(sort_item[0] == "Solar Activity Type"):
                solar_act_type = self.get_solar_activity_type()
                tmp_el = ET.SubElement(
                    parent,
                    str(trans_dict["Solar Activity Type " + solar_act_type]))
                if(solar_act_type == "VARIABLE"):
                    solar_act_type_el = ET.SubElement(
                        tmp_el, str(trans_dict["Solar Activity Type"]))
                    solar_act_type_el.text = str(self.get_solar_activity_type())
                else:
                    self.parse_elements(
                        tmp_el,                                                     
                        self.get_conf()["Solar Activity"],                          
                        unit_dict,
                        config_dict.get_sort_solat_act(),
                        trans_dict)
            #exception Iteration Data
            if(sort_item[0] == "Iteration Data"):
                iteration = ET.SubElement(parent, str(trans_dict["Iteration Data"]))
                self.parse_elements(
                    iteration,
                    self.get_conf()["Iteration Data"],
                    unit_dict,
                    conf_dict.get_sort_iteration_data(),
                    trans_dict)


    def get_xml_file_name(self):
        """
        Get the xml_file name generated
        """
        name = self.get_space_object_name()
        edge_length = self.get_edge_length()
        mass = self.get_mass()
        sat_name = name+"_"+str(mass)+"_"+str(edge_length)+".xml"
        return sat_name

    def convert_to_xml(self):
        """
        Creates an xml configuration from the cfg file
        """
        config_dict = ConfigDict()
        dictio = config_dict.get_dict()
        sort_space_object = config_dict.get_sort_space_object()
        unit_dict = config_dict.get_unit_dict()
        self.set_abstract_item(
            "General",
            "Solar Activity Type",
            self.get_solar_activity_type())
        self.set_abstract_item(
            "General",
            "Iteration Data",
            "")
        self.set_abstract_item(
            "General",
            "Atmospheric Model",
            "")
        self.set_stela_version("2.5.0")
        leosimulation = ET.Element('LEOSimulation')
        leosimulation.set("version", str(self.get_stela_version()))
        stelaversion = ET.SubElement(leosimulation, 'STELAVersion')
        stelaversion.text = "2.5.1"
        spaceobject = ET.SubElement(leosimulation, dictio["Space Object"])
        self.parse_elements(
            spaceobject,
            self.get_conf()["Space Object"],
            unit_dict,
            sort_space_object,
            dictio,
            ["Edge Length", "Constant Drag Coef"])
        ephemerisman = ET.SubElement(leosimulation, 'EphemerisManager')
        ephemerisman.set('version', str(self.get_stela_version()))
        initstate = ET.SubElement(ephemerisman, 'initState')
        bulletin = ET.SubElement(initstate, 'bulletin')
        bulletin.set('version', str(self.get_stela_version()))
        date = strftime("%Y-%m-%dT%H:%M:%S.000", gmtime())
        date_element = ET.SubElement(bulletin, 'date')
        date_element.text = date
        sim_type_element = ET.SubElement(
            bulletin, str(dictio["Type " + self.get_type_of_sim()]))
        for param in config_dict.get_conf_sim(sim_type_element.tag):
            tmp_el = ET.SubElement(sim_type_element, str(dictio[param]))
            tmp_el.text = str(
               self.get_abstract_item("Initial Bulletin", param.title()))
            if param in unit_dict:
                tmp_el.set('unit', str(unit_dict[param]))
        finishstate = ET.SubElement(ephemerisman, 'finalState')
        self.parse_elements(
             leosimulation,
             self.get_conf()["General"],
             unit_dict,
             config_dict.get_sort_general(),
             dictio,
            [
            "Stela Version",
            "Edge Length",
            "Solar Activity Type",
            "Atmospheric Model" ,
            "Earth Tesseral Switch",
            "Iteration Data"])
        return prettify(leosimulation)

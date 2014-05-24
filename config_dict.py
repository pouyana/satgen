#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A dict for all the cfg xml transition names
"""

class ConfigDict:
    
    def get_unit_dict(self):
        """
        Returns the Dictionary needed for the 
        Units
        """
        unit_dict = {
            "Mass" : "kg",
            "Simulation duration" : "years",
            "Ephemeris step" : "s",
            "Difference between terrestrial and universal time" : "s",
            "a (Semi major axis)" : "m",
            "lambdaEq" : "rad",
            "Integration Step" : "s",
            "Reentry Altitude" : "m",
            "Function Value Accuracy": "days",
            "Expiring Duration" : "years",
            "Simulation Minus Expiring Duration" : "years",
            "Zp (Perigee altitude)" : "m",
            "Za (Apogee altitude)" : "m",
            "Inclination" : "rad",
            "I (Inclination)" : "rad",
            "RAAN (Right Ascension of Ascending Node)" : "rad",
            "M (Mean anomaly)" : "rad",
            "w (Argument of perigee)" : "rad"}
        return unit_dict


    def get_dict(self):
        """
        Returns the Dictionary needed for the
        XML
        """
        config_dict = {
            "Stela Version" : "STELAVersion",
            "Model" : "modelType",
            "Author" : "author",
            "Comment" : "comment",
            "Simulation duration" : "simulationDuration",
            "Ephemeris step" : "ephemerisStep",
            "Difference between terrestrial and universal time" : "ttMinusUT1",
            "Integration Step" : "integrationStep",
            "Atmospheric drag switch" : "dragSwitch",
            "Drag quadrature Points" : "dragQuadPoints",
            "Atmospheric Drag Recompute step" : "atmosDragRecomputeStep",
            "Solar radiation pressure switch" : "srpSwitch",
            "Solar radiation pressure quadrature Points" : "srpQuadPoints",
            "Sun switch" : "sunSwitch",
            "Moon switch" : "moonSwitch",
            "Zonal order" : "zonalOrder",
            "Earth Tesseral switch" : "tesseralSwitch",
            "Tesseral order" : "Tesseralorder",
            "Tesseral min period" : "nbIntegrationStepTesseral",
            "Reentry Altitude" : "reentryAltitude",
            "Mass" : "mass",
            "Drag Area" : "dragArea",
            "Reflecting Area" : "reflectingArea",
            "Reflectivity Coefficient" : "reflectivityCoefficient",
            "Orbit Type" : "orbitType",
            "Drag Coefficient Type CONSTANT" : "ConstantDragCoef",
            "Drag Coefficient Type VARIABLE" : "VariableDragCoef",
            "Constant Drag Coef" : "cstDragCoef",
            "Space Object" : "SpaceObject",
            "Name" : "name",
            "Initial" : "initState",
            "Bulletin" : "bulletin",
            "Date" : "date",
            "Type Perigee/Apogee" : "Type0PosVel",
            "Type Cartesian" : "Type1PosVel",
            "Type Keplerian" : "Type2PosVel",
            "Type Equinoctial" : "Type8PosVel",
            "Frame" : "frame",
            "Nature" : "nature",
            "Zp (Perigee altitude)" : "perigeeAltitude",
            "Za (Apogee altitude)" : "apogeeAltitude",
            "I (Inclination)" : "inclination",
            "RAAN (Right Ascension of Ascending Node)" : "rAAn",
            "w (Argument of perigee)" : "argOfPerigee",
            "M (Mean anomaly)" : "meanAnomaly",
            "a (Semi major axis)" : "semiMajorAxis",
            "e (Eccentricity)" : "eccentricity",
            "lambdaEq" : "lambdaEq",
            "Atmospheric model" : "atmosModel",
            "longitudeTFE" : "longitudeTFE",
            "epochTFE" : "epochTFE",
            "eX" : "eX",
            "eY" : "eY",
            "iX" : "iX",
            "iY" : "iY",
            "x" : "x",
            "y" : "y",
            "z" : "z",
            "vX" : "vX",
            "vY" : "vY",
            "vZ" : "vZ",
            "Solar Activity Type MEAN_CONSTANT" : "ConstantEquivalentSolarActivity",
            "Solar Activity Type VARIABLE" : "VariableSolarActivity",
            "Solar Activity Type CONSTANT" : "ConstantSolarActivity",
            "Solar Activity Type" : "solActType",
            "AP Constant Equivalent Solar Activity" : "constantAP",
            "F10.7 Constant Equivalent Solar Activity" : "constantF107",
            "Function Value Accuracy" : "funcValueAccuracy",
            "Iteration Data" : "iterationData",
            "Simulation Minus Expiring Duration" : "simMinusExpDuration",
            "Iteration Method": "iterationMethod",
            "Expiring Duration": "expDuration"}
        return config_dict

    def get_conf_sim(self, type_of_sim):
        """
        Gives an array of paramaters that are possible for everry Simulation Type
        Input: Type0PosVel, Type1PosVel, Type8PosVel and Type2PosVel
        """
        result = []
        if(type_of_sim=="Type0PosVel"):
            result = ["Zp (Perigee altitude)", "Za (Apogee altitude)", "I (Inclination)", "RAAN (Right Ascension of Ascending Node)", "w (Argument of perigee)", "M (Mean anomaly)"]
        if(type_of_sim=="Type8PosVel"):
            result = ["longitudeTFE", "epochTFE", "a (Semi major axis)", "lambdaEq", "eX", "eY", "iX", "iY"]
        if(type_of_sim=="Type2PosVel"):
            result = ["longitudeTFE", "epochTFE", "a (Semi major axis)" ,"e (Eccentricity)", "I (Inclination)", "RAAN (Right Ascension of Ascending Node)", "w (Argument of perigee)","M (Mean anomaly)"]
        if(type_of_sim=="Type1PosVel"):
            result = ["longitudeTFE", "epochTFE", "x", "y", "z", "vX", "vY", "vZ"]
        return result

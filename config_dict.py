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
            "Zp (Perigee altitude)" : "rad",
            "Za (Apogee altitude)" : "rad",
            "Inclination" : "rad",
            "I (Inclination)" : "rad",
            "rAAN (Right Ascension of Ascending Node)" : "rad"
            "meanAnomaly" : "rad"}


    def get_dict(self):
        """
        Returns the Dictionary needed for the
        XML
        """
        config_dict = {
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
            "Drag Coefficent Type CONSTANT" : "ConstantDragCoef",
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
            "rAAN" : "RAAN (Right Ascension of Ascending Node)",
            "w (Argument of perigee)" : "argOfPerigee",
            "M (Mean anomaly)" : "meanAnomaly",
            "a (Semi major axis)" : "semiMajorAxis",
            "e (Eccentricity)" : "eccentricity",
            "lambdaEq" : "lambdaEq",
            "Atmospheric model" : "atmosModel",
            "Solar Activity Type MEAN_CONSTANT" : "ConstantEquivalentSolarActivity",
            "Solar Activity Type" : "solActType",
            "AP Constant Equivalent Solar Activity" : "constantAP",
            "F10.7 Constant Equivalent Solar Activity" : "constantF107",
            "Function Value Accuracy" : "funcValueAccuracy",
            "Iteration Data" : "iterationData",
            "Simulation Minus Expiring Duration" : "simMinusExpDuration",
            "Iteration Method": "iterationMethod",
            "Expiring Duration": "expDuration"}
        return config_dict


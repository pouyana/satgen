%Set preferences with setdbprefs.
setdbprefs('DataReturnFormat', 'cellarray');
setdbprefs('NullNumberRead', 'NaN');
setdbprefs('NullStringRead', 'null');

%Make connection to database.  Note that the password has been omitted.
%Using JDBC driver.
conn = database('', '', '', 'org.sqlite.JDBC', 'jdbc:sqlite:/home/poa32kc/Programs/satgen/satgen.db');

%Read data from database.
curs = exec(conn, ['SELECT 	initState.id'...
    ' ,	initState.date'...
    ' ,	initState.semiMajorAxis'...
    ' ,	initState.eccentricity'...
    ' ,	initState.inclination'...
    ' ,	initState.rAAN'...
    ' ,	initState.argOfPerigee'...
    ' ,	initState.meanAnomaly'...
    ' ,	initState.spaceObjectId'...
    ' FROM 	initState, spaceObejct, finalState ']);

curs = fetch(curs);
close(curs);

%Assign data to output variable
satdata = curs.Data;

%Close database connection.
close(conn);

%Clear variables
clear curs conn
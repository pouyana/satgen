function y = str_to_time(x)
date_str = sscanf(x,'%d-%d-%d');
y = datenum(date_str(1),date_str(2),date_str(3));
end
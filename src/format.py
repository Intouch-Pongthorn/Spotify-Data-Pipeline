from datetime import datetime
import dateutil.parser as dateparser
import pytz

def concat(lst:list[str])->str:
    line:str = ",".join(lst)
    return line

def extract_artists_name(lst:list[dict])->str:
    names:list = []
    for obj in lst:
        names.append(obj["name"])
    names_one_line = concat(names)
    return names_one_line

def to_duration_minute(millisecond:int)->float:
    second:int = millisecond // 1000
    min,sec = divmod(second,60)
    duration:float =float(str(min)+"."+str(sec).zfill(2))
    return duration

def to_th_time(utc_time_str:str)->str:
    utc_time:datetime = dateparser.parse(utc_time_str)
    th_time:str = utc_time.astimezone(pytz.timezone('Asia/Bangkok')).strftime('%d-%m-%Y %H:%M:%S')
    return th_time


if __name__=="__main__":
    minute = to_duration_minute(228623)
    print(minute)
    print(type(minute))
    line = concat(["pop","blue"])
    print(line)
    local_time = to_th_time("2023-04-06T01:30:31.659Z")
    print(local_time)
    
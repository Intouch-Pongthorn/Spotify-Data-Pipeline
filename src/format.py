import datetime

def to_minute(millisecond:int)->float:
    second:int = millisecond //1000
    min,sec = divmod(second,60)
    minute:float =float(str(f"{min}.{sec}"))
    return minute

def concat(lst:list[str])->str:
    line:str = ",".join(lst)
    return line


if __name__=="__main__":
    minute = to_minute(228623)
    print(minute)
    print(type(minute))
    line = concat(["pop","blue"])
    print(line)
    
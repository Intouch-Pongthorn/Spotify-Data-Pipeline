import datetime

def to_minute(millisecond):
    second = millisecond //1000
    min,sec = divmod(second,60)
    minute =float(str(f"{min}.{sec}"))
    return minute


if __name__=="__main__":
    minute = to_minute(228623)
    print(minute)
    print(type(minute))
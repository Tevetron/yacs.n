import datetime

def get_newest_semester():
    now = datetime.datetime.now()
    if now.month < 6:
        return str(now.year) + "09"
    else:
        return "fall" + str(now.year)
    
if __name__ == "__main__":
    print(get_newest_semester())
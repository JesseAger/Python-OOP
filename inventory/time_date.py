import time

def Date():
    current_date= time.localtime()
    exact_date = time.strftime("%d/%m/%y", current_date)    
    return exact_date
Date()

def Time():
    current_time = time.localtime()
    exact_time = time.strftime("%I:%M:%S %p", current_time)
    return exact_time

Time()



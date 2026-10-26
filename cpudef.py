import psutil
def get_cpu_usage():

    cpu= psutil.cpu_percent(interval=1)
    vmi=psutil.virtual_memory().percent
    du=psutil.disk_usage('/').percent
    print("CPU Percentage: ",cpu)

    if cpu>80:
        print( "\033[91m" + "CPU usage is high" + "\033[0m" )
    else:
        print( "\033[92m" + "CPU usage is normal" + "\033[0m" )


    print("Virtual Memory Percentage : ",vmi)
    if vmi>80:
        print( "\033[91m" + "Virtual memory usage is high" + "\033[0m" )    
    else:
        print( "\033[92m" + "Virtual memory usage is normal" + "\033[0m" )  

    print("Disk Usage Percentage : ",du)
    if du>80:
        print( "\033[91m" + "Disk usage is high" + "\033[0m" ) 
    else:
        print( "\033[92m" + "Disk usage is normal" + "\033[0m" )




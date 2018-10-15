import psutil
import smtplib
from email.mime.text import MIMEText

def for_cpu_utilization():

    threshold = 10
    try:
        for pid in psutil.pids():

            p = psutil.Process(pid)
            cpu = round(p.cpu_percent(interval=1))
            name_process = p.name()
            #num_thread = str(p.num_threads())
            status_process = p.status()
            str_process = str(cpu)

            if (cpu > threshold):
                print('-'*30)
                print("Name : {}".format(name_process))
                print("Status : {}".format(status_process))
                print("CPU : {} %".format(cpu))

                mail_send("CPU",name_process,status_process,str_process)

    except psutil.NoSuchProcess:
            print("Error : No such Process")
    except psutil.AccessDenied :
            print("Error : Access Denied ")
    except psutil.TimeoutExpired:
            print("Error : Timeout Expired ")
    except ModuleNotFoundError as e:
            print("Error : No such module found.")

def mail_send(*args):

    msg = MIMEText(args[0] + " Utilization \n"
                   + "---------------------------------------------\n"
                   + "Name : " + args[1] + "\n"
                   + "Status : " + args[2] + "\n"
                   + args[0] + " Utilization : " + args[3])

    msg["Subject"] = 'More CPU/Memory utilization'
    msg["From"] = 'bhasha.dusara@gmail.com'
    msg['To'] = 'bhasha.dusara@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login('bhasha.dusara@gmail.com', '********')
        server.sendmail('bhasha.dusara@gmail.com', 'bhasha.dusara@gmail.com', msg.as_string())
    print("done!")

def for_memory_utilization():
    threshold = 100
    try:
        for pid in psutil.pids():

            p = psutil.Process(pid)
            name_process = p.name()
            status_process = p.status()
            #memory = round(p.memory_percent())
            memory_get = p.memory_info().rss
            KB = 1024
            MB = KB ** 2
            GB = KB ** 3
            if (MB <= memory_get < GB) :
                MB_Memory = memory_get / MB
                convert_MB = str(MB_Memory)
                if (MB_Memory > threshold):
                    print("-"*50)
                    print("Name : {}".format(name_process))
                    print("Status : {}".format(status_process))
                    print("Memory : {} MB".format(MB_Memory))
                    mail_send("Memory(MB)",name_process,status_process,convert_MB)

    except psutil.TimeoutExpired:
        print("Error : Time Out")
    except psutil.AccessDenied:
        print("Error : Access Denied")
    except psutil.NoSuchProcess:
        print("Error : No such Process")
    except ModuleNotFoundError:
        print("Error : No such module found")


def for_disk_utilization():
    threshold = 90.00
    try:

        disk_name = ["B:\\","C:\\","D:\\"]
        for pid in disk_name:
            disk_used = psutil.disk_usage(pid).used
            disk_total = psutil.disk_usage(pid).total
            disk_free = psutil.disk_usage(pid).free
            KB = 1024
            MB = KB ** 2
            GB = KB ** 3
            TB = KB ** 4
            if (GB <= disk_used < TB) and (GB <= disk_free < TB) and (GB <= disk_total <TB):
                MB_Memory_used = round(disk_used / GB,2)
                MB_Memory_free = round(disk_free / GB, 2)
                MB_Memory_total = round(disk_total / GB, 2)

                if (MB_Memory_used > threshold):
                    print('-'*30)
                    print("Name : {}".format(pid))
                    print("Total Space : {}".format(MB_Memory_total))
                    print("Free Space : {}".format(MB_Memory_free))
                    print("Used Space : {}".format(MB_Memory_used))
                    mail_send("Disk Space",pid,"----",str(MB_Memory_used))

    except psutil.NoSuchProcess:
        print("Error : No such Process")
    except psutil.AccessDenied:
        print("Error : Access Denied")
    except ModuleNotFoundError:
        print("Error: No such Module found")

if __name__=='__main__':

        for_cpu_utilization()
        for_memory_utilization()
        for_disk_utilization()


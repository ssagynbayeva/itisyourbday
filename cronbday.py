from crontab import CronTab  
cron = CronTab(user='sabina') 
task = cron.new(command='python itisyourbday.py') 
task.minute.every(2)  
cron.write()
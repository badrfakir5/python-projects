from datetime import datetime

now = datetime.now()
day = now.strftime(" %d/%m/%Y ")
print(day)
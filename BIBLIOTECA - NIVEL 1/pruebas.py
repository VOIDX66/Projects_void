import datetime #pip install datetime
from dateutil.relativedelta import * #pip install python-dateutil

dias = 5
fecha_actual = datetime.date.today()
fecha_vencimiento = fecha_actual + datetime.timedelta(days=dias)

diferencia = relativedelta(fecha_vencimiento,fecha_actual).days
if diferencia < 0:
    print("Vencido")

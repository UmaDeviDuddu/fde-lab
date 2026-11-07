weeks = 35
sessions = int(input("sessions per week?"))
minutes = int(input("total minutes per session"))
total_minutes = weeks * sessions * minutes
print("Total minutes:", total_minutes)
total_hours = total_minutes / 60
print("Total hours over ",weeks," Weeks :",round(total_hours,1))

      
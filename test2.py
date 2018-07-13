import utils
import datetime

my_date = datetime.datetime(2018, 6, 6, 15, 17, 38)

# print("To 15 seconds: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_sec=15)))
# print("To 30 seconds: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_sec=30)))
# print("To 2 minutes: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_min=2)))
# print("To 15 minutes: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_min=15)))
# print("To 30 minutes: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_min=30)))
# print("To 1h: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_hours=1)))
# print("To 2h: %s" % datetime.fromtimestamp(utils.round_unixtimestamp(my_date, accuracy_hours=2)))

print("To 15 seconds: %s" % datetime.fromtimestamp(utils.round_datetime(my_date, accuracy_sec=15)))
print("To 30 seconds: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_sec=30))))
print("To 2 minutes: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_min=2))))
print("To 15 minutes: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_min=15))))
print("To 30 minutes: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_min=30))))
print("To 1h: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_hours=1))))
print("To 2h: %s" % datetime.fromtimestamp(str(utils.round_datetime(my_date, accuracy_hours=2))))

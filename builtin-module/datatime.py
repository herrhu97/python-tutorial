from datetime import datetime, timedelta, timezone

now = datetime.now()
print(type(now))
print(now)

dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

t = 1429417200.0
ts = datetime.fromtimestamp(t)
utc_ts = datetime.utcfromtimestamp(t)
print(type(ts))
print(ts)
print(utc_ts)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now + timedelta(hours=10))

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)


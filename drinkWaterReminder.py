# write an program using os module which will remind us to drink water every hour or two
# this will show the result on the screen or through notification to our system
import dbus
import time

# Connect to D-Bus
bus = dbus.SessionBus()
notify_service = bus.get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
notify = dbus.Interface(notify_service, "org.freedesktop.Notifications")

print('1. Show a notification')
nid = notify.Notify("NOTIFICATION", 0, "", "hey! its time to drink water ", "This is a test", [], {}, 10000)
print("Notification ID:", nid)

print('# 2. Get capabilities')
print("Capabilities:", notify.GetCapabilities())

print("# 3. Get server info")
print("Server Info:", notify.GetServerInformation())

# Wait before closing
time.sleep(10)

# 4. Close notification
notify.CloseNotification(nid)
print("Notification closed")

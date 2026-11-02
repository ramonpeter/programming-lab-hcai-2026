# photos.py -- solution to D5
TOTAL_GB = 128
SYSTEM_GB = 14
PHOTO_MB = 4.2

stored = int(input("Photos already on the phone: "))
free_mb = (TOTAL_GB - SYSTEM_GB) * 1000 - stored * PHOTO_MB
more = int(free_mb // PHOTO_MB)
print("Room for", more, "more photos")

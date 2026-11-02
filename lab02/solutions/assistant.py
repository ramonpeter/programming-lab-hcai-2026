# Name: Ada Lovelace
# Date: 12.10.2026
# A rule-based study assistant. v0.2 asks for this week's numbers.

SELF_STUDY_FACTOR = 1.5   # hours of self-study per lecture hour
DAYS = 7

print("=" * 50)
print("   STUDY ASSISTANT  v0.2")
print("=" * 50)
name = input("What is your name? ")
lectures = int(input("How many lectures this week? "))
hours_per_lecture = float(input("How many hours is one lecture? "))

lecture_hours = lectures * hours_per_lecture
self_study_hours = lecture_hours * SELF_STUDY_FACTOR
total_hours = lecture_hours + self_study_hours
hours_per_day = total_hours / DAYS

print()
print("Hello,", name + "! Your week:")
print("Lecture hours:", lecture_hours)
print("Self-study hours (" + str(SELF_STUDY_FACTOR) + " per lecture hour):", self_study_hours)
print("Total hours:", total_hours)
print("Hours per day (" + str(DAYS) + " days):", round(hours_per_day, 1))
print("=" * 50)

# 7 lectures next week: no line changes — you type 7 when it asks.

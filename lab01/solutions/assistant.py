# Name: Ada Lovelace
# Date: 28.09.2026
# A rule-based study assistant. v0.1 prints a weekly report with fixed numbers.

print("=" * 50)
print("   STUDY ASSISTANT  v0.1")
print("=" * 50)
print("Hello! I am a very simple assistant.")
print("I do not learn. I only follow rules someone wrote.")
print()
print("This week (fixed numbers, for now):")
print("Lecture hours:", 5 * 4)
print("Self-study hours (1.5 per lecture hour):", 5 * 4 * 1.5)
print("Total hours:", 5 * 4 + 5 * 4 * 1.5)
print("Hours per day (7 days):", (5 * 4 + 5 * 4 * 1.5) / 7)
print("Hours per day, rounded:", round((5 * 4 + 5 * 4 * 1.5) / 7, 1))   # E2
print("=" * 50)

# E3: "5 * 4" appears five times. Changing to 6 lectures means five edits,
# and missing one gives a report that is silently inconsistent.
# Next session: store the number once, under a name.

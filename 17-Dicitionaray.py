monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    # key:  word
}

print(monthConversion["Jan"])  # January
print(monthConversion["Sep"])  # September
print(monthConversion.get("Dec"))  # December
print(monthConversion.get("Why"))  # None
print(monthConversion.get("Why", "Not a valid key"))  # Not a valid key

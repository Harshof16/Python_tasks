from datetime import datetime

# Function to format date from "2025-07-04T12:00:00Z" to "4 July 2025"
def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%#d %B %Y")
    except Exception:
        return date_str
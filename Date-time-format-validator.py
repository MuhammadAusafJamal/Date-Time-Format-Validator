import re
import streamlit as st
from typing import List, Tuple

class DateTimeFormatValidator:
    def __init__(self):
        self.formats = [
            # Date Formats
            (r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/((19|20)\d\d)$', 'DD/MM/YYYY'),
            (r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-((19|20)\d\d)$', 'DD-MM-YYYY'),
            (r'^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', 'YYYY-MM-DD'),
            (r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s(0[1-9]|[12][0-9]|3[01]),\s((19|20)\d\d)$', 'Month DD, YYYY'),
            (r'^(0[1-9]|[12][0-9]|3[01])\s(January|February|March|April|May|June|July|August|September|October|November|December)\s((19|20)\d\d)$', 'DD Month YYYY'),
            
            # Time Formats
            (r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', 'HH:MM (24-hour)'),
            (r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', 'HH:MM:SS (24-hour)'),
            (r'^(0?[1-9]|1[0-2]):[0-5][0-9]\s(AM|PM)$', 'HH:MM AM/PM (12-hour)'),
            (r'^(0?[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9]\s(AM|PM)$', 'HH:MM:SS AM/PM (12-hour)'),
            
            # Combined Date and Time Formats
            (r'^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', 'YYYY-MM-DDTHH:MM:SS (ISO 8601)'),
            (r'^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', 'YYYY-MM-DD HH:MM:SS'),
            (r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/((19|20)\d\d)\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', 'DD/MM/YYYY HH:MM'),
            (r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-((19|20)\d\d)\s(0?[1-9]|1[0-2]):[0-5][0-9]\s(AM|PM)$', 'DD-MM-YYYY HH:MM AM/PM'),
        ]

    def validate(self, date_time_string: str) -> Tuple[bool, List[str]]:
        valid_formats = []
        for pattern, format_name in self.formats:
            if re.match(pattern, date_time_string):
                valid_formats.append(format_name)
        
        is_valid = len(valid_formats) > 0
        return is_valid, valid_formats

    def validate_all_formats(self, date_time_string: str) -> List[Tuple[str, bool]]:
        results = []
        for pattern, format_name in self.formats:
            is_valid = bool(re.match(pattern, date_time_string))
            results.append((format_name, is_valid))
        return results

def main():
    st.title("Date and Time Format Validator")

    st.write("This validator supports various date, time, and combined date-time formats.")
    st.write("Enter a date, time, or date-time string below to check its format.")
    
    validator = DateTimeFormatValidator()
    
    date_time_string = st.text_input("Enter a date, time, or date-time string:")
    
    if st.button("Validate"):
        if date_time_string:
            is_valid, valid_formats = validator.validate(date_time_string)
            
            if is_valid:
                st.success(f"The input '{date_time_string}' is valid.")
                st.write("Matching format(s):")
                for format_name in valid_formats:
                    st.write(f"- {format_name}")
            else:
                st.error(f"The input '{date_time_string}' is not valid for any supported format.")
            
            st.write("Detailed format check:")
            all_results = validator.validate_all_formats(date_time_string)
            for format_name, is_valid in all_results:
                status = "Valid" if is_valid else "Invalid"
                st.write(f"- {format_name}: {status}")
        else:
            st.warning("Please enter a date, time, or date-time string to validate.")

if __name__ == "__main__":
    main()

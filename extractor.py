import re

def extract_info(text):
    phone_numbers = re.findall(r'\b(?:\+\d{1,2}\s?)?(?:\(\d{1,4}\))?[0-9A-Za-z .-]{8,}\b', text)
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

    return {
        'phone_numbers': phone_numbers,
        'email_addresses': email_addresses,
        'ip_addresses': ip_addresses
    }

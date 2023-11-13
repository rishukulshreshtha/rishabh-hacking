from phone_email_ip_extractor.extractor import extract_info

def main():
    text = "Sample text with phone number +1-555-555-5555, email@example.com, and IP address 192.168.0.1."
    results = extract_info(text)
    
    print("Phone Numbers:", results['phone_numbers'])
    print("Email Addresses:", results['email_addresses'])
    print("IP Addresses:", results['ip_addresses'])

if __name__ == "__main__":
    main()

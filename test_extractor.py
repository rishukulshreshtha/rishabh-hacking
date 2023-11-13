import unittest
from phone_email_ip_extractor.extractor import extract_info

class TestExtractor(unittest.TestCase):
    def test_extraction(self):
        text = "Sample text with phone number +1-555-555-5555, email@example.com, and IP address 192.168.0.1."
        results = extract_info(text)

        self.assertEqual(results['phone_numbers'], ['+1-555-555-5555'])
        self.assertEqual(results['email_addresses'], ['email@example.com'])
        self.assertEqual(results['ip_addresses'], ['192.168.0.1'])

if __name__ == '__main__':
    unittest.main()

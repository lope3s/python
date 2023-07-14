import unittest
from unittest.mock import patch
from app import store_contact, get_contacts_data
from collections import namedtuple


class TestPhonebook (unittest.TestCase):
    agenda = []

    ContactData = namedtuple("ContactData", ["name", "phone_number"])

    @classmethod
    def tearDownClass(clr):
        clr.agenda = []

    def test_store_contact(self):
        contact_data = self.ContactData('luan', '11976098818')
        store_contact(self.agenda, contact_data)

        self.assertEqual(self.agenda, [contact_data])

    def test_get_contacts_data(self):
        with patch(target='builtins.input',
                   side_effect=["John Doe", "12334567890"]):
            result = get_contacts_data()

        self.assertEqual(result, ("John Doe", "12334567890"))


if __name__ == "__main__":
    unittest.main()

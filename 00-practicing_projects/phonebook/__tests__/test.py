import unittest
from app import store_contact
from collections import namedtuple


class TestPhonebook (unittest.TestCase):
    agenda = []

    @classmethod
    def tearDownClass(clr):
        clr.agenda = []

    def test_store_contact(self):
        ContactData = namedtuple("ContactData", ["name", "phone_number"])
        contact_data = ContactData('luan', '11976098818')
        store_contact(self.agenda, contact_data)

        self.assertEqual(self.agenda, [contact_data])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.database import create_connection

class TestDatabase(unittest.TestCase):
    def test_connection_creation(self):
        conn = create_connection('sqlite:///:memory:')
        self.assertIsNotNone(conn)
# test_searchengine.py
"""
Tests for SearchEngine module.
"""

import unittest
from searchengine import SearchEngine

class TestSearchEngine(unittest.TestCase):
    """Test cases for SearchEngine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SearchEngine()
        self.assertIsInstance(instance, SearchEngine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SearchEngine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

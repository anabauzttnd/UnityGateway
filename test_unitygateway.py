# test_unitygateway.py
"""
Tests for UnityGateway module.
"""

import unittest
from unitygateway import UnityGateway

class TestUnityGateway(unittest.TestCase):
    """Test cases for UnityGateway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UnityGateway()
        self.assertIsInstance(instance, UnityGateway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UnityGateway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

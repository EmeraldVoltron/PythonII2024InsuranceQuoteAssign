"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/9/24
Unit Test for Insurance Quotes
"""
import unittest
import InsuranceQuoteBoggs as ins


class MyTestCase(unittest.TestCase):
    def test_price_range_16(self):
        print("Testing range from 16-24")
        # test SM coverage (no accidents and no prepay
        driver = {
            "Name": "Abby",
            "Age": 16,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 2593)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 2957)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 6930)

    def test_price_range_25(self):
        print("Testing Range 25-34")
        driver = {
            "Name": "Abby",
            "Age": 25,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 608)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 691)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 1745)

    def test_price_range_35(self):
        print("Testing Range 35-44")
        driver = {
            "Name": "Abby",
            "Age": 35,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 552)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 627)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 1564)

    def test_price_range_45(self):
        print("Testing range 45-54")
        driver = {
            "Name": "Abby",
            "Age": 45,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 525)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 596)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 1469)

    def test_price_range_55(self):
        print("Testing Range 55-64")
        driver = {
            "Name": "Abby",
            "Age": 55,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 494)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 560)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 1363)

    def test_price_range_65(self):
        print("Testing range 65+")
        driver = {
            "Name": "Abby",
            "Age": 65,
            "Coverage": "SM",
            "Price": float(0)
        }
        self.assertEqual(ins.determine_price(driver), 515)
        driver["Coverage"] = "L"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 585)
        driver["Coverage"] = "F"
        driver["Price"] = float(0)
        self.assertEqual(ins.determine_price(driver), 1402)

    """
    Since I already included ways to handle the failures of input 
    in the getting_input_and_test function
    I did not do Unit Tests for that method, and I am not
    100% sure how I could do unit tests for it with the way I wrote the
    code.
    """
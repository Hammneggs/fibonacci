#!/usr/bin/env python

import os
import unittest
import requests

url = "http://127.0.0.1:5000/fibonacci/"

class FibonacciTest(unittest.TestCase):

    def test_get_first_element(self):
        myurl = url + "1"
        myrequest = requests.get(myurl)
        self.assertEqual(myrequest.status_code, 200)

    def test_get_two_elements(self):
        myurl = url + "2"
        myrequest = requests.get(myurl)
        self.assertEqual(myrequest.status_code, 200)

    def test_regular_number(self):
        myurl = url + "25"
        myrequest = requests.get(myurl)
        self.assertEqual(myrequest.status_code, 200)

    def test_maximum_number(self):
        myurl = url + "500"
        myrequest = requests.get(myurl)
        self.assertEqual(myrequest.status_code, 200)

    def test_zeor(self):
        myurl = url + "0"
        myrequest = requests.get(myurl)
        self.assertTrue("" in myrequest.content)

    def test_negative_integer(self):
        myurl = url + "-5"
        myrequest = requests.get(myurl)
        self.assertTrue("Please enter a positive number only" in myrequest.content)

    def test_other_types(self):
        myurl = url + "string"
        myrequest = requests.get(myurl)
        self.assertTrue("Please enter a positive number only" in myrequest.content)

if __name__ == '__main__':
    unittest.main()

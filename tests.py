#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import translate as t
from pickle import load as pload
class TestTranslate(unittest.TestCase):
    def setUp(self):
        # Add your credentials here to test
        t.set_credentials(app_id='',client_id='',client_secret='')

    def test_translate(self):
        pass
        # self.assertEqual('Привет', t.translate('hello','en','ru'))
    def test_get_access_token(self):
        token = t.get_access_token()
        ftok = open('./translate.tok', 'r')

        self.assertEqual(unicode,type(token))
        self.assertEqual(dict,type(pload(ftok)))
if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import translate as t

class TestTranslate(unittest.TestCase):
    def setUp(self):
        t.set_credentials(app_id='',client_id='',client_secret='')

    def test_translate(self):
        self.assertEqual('Привет', t.translate('hello','en','ru'))

if __name__ == '__main__':
    unittest.main()
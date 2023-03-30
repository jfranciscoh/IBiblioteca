#!/usr/bin/python
# -- coding: utf-8 --
import os

try:
    SQL_ALCHEMY_DATABASE_OPTION = {'database': "biblioteca_inv"}
    SQL_ALCHEMY_DATABASE_URI= "mysql://root:herrera21@localhost:3306/biblioteca_inv"
except:
    SQL_ALCHEMY_DATABASE_URI = ""
    SQL_ALCHEMY_TEST_DATABASE_URI = ""
    pass
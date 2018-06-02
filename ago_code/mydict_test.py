#!/usr/bin/env python
# _*_ coding:utf-8 _*
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    #
    # def setUp(self):
    #     print('setUp...')
    #
    # def tearDown(self):
    #     print('tearDown...')

    def test__init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')
# self.assrtEqual(abs(-1),1)   #断言函数返回的结果与1相等

    def test_attr(self):
        d = Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value=d['empty']
 # 另一种重要的断言就是期待抛出指定类型的Error,比如通过 d['empty'] 访问不存在的key，断言会抛出KeyError

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value=d.empty
    #而通过d.empty访问不存在的key时，我们你期待抛出AttributeError



if __name__=='__main__':
    unittest.main()

#
# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')


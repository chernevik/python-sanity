#/usr/bin/python
# -*- coding: utf-8

#=============================================================================
#   Imports

import                          unittest2

import sanity.specification.specifier as  specificier


#=============================================================================
class SpecifierTest(unittest2.TestCase):

    #---------------------------------------------------------------------
    def test_basic(self):

        s = specificier.Specificier(spec='basic.json')

        self.assertTrue(isinstance(s.json, dict))
        self.assertEqual(s.json['TestName'], 'WitchOrDuck')

        self.assertEqual(s.TestName, 'WitchOrDuck')
        self.assertEqual(
            {u'url': u'/', u'method': u'GET'},
            s.request
            )

    #---------------------------------------------------------------------

#=============================================================================
if __name__ == '__main__':
    unittest2.main()

#=============================================================================

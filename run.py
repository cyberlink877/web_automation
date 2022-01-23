# -*- coding: utf-8 -*-
import unittest
import StringIO
import HTMLTestRunner 
#add the HTMLTestRunner to site-package for the python installation, i.e. /Library/Python/2.7/site-packages 


def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'Test*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':
    cases = get_test_cases('testcases')
    f = open(r'report/testReport.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'Crypto NFT Web Test Report', description=u'Test results:')
    runner.run(cases)
    f.close()

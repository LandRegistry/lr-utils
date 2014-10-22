import unittest
from lrutils.templatefilters.template_filters import dateformat, datetimeformat, currency

class TemplateFiltersTestCase(unittest.TestCase):

    def test_dateformat(self):
        formatted = dateformat('14/01/2014')
        self.assertEquals(formatted, '14 January 2014')

        formatted = dateformat('01/01/2014')
        self.assertEquals(formatted, '1 January 2014')

        formatted = dateformat('02/01/2014')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('2014-01-02')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('2014/01/02')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('14.01.02')
        self.assertEquals(formatted, '14 January 2002')


        formatted = dateformat('99.01.02')
        self.assertEquals(formatted, '2 January 1999')

        formatted = dateformat('02 January 2014')
        self.assertEquals(formatted, '2 January 2014')


    def test_datetimeformat(self):
        formatted = datetimeformat('14/06/2014 23:23:25.1231+01:00')
        self.assertEquals(formatted, '14 June 2014 at 23:23:25')

        formatted = datetimeformat('14/01/14 23:23:25.1231+01:00')
        self.assertEquals(formatted, '14 January 2014 at 22:23:25')

        formatted = datetimeformat('2013-01-02 08:23:25.1231+00:00')
        self.assertEquals(formatted, '2 January 2013 at 08:23:25')


    def test_timezones(self):
        formatted = datetimeformat('2014-03-30 03:23:25.1231+01:00')
        self.assertEquals(formatted, '30 March 2014 at 03:23:25')

        formatted = datetimeformat('2014-03-29 01:23:25.1231+00:00')
        self.assertEquals(formatted, '29 March 2014 at 01:23:25')

        formatted = datetimeformat('2013-06-06 08:23:25.1231+01:00')
        self.assertEquals(formatted, '6 June 2013 at 08:23:25')


        formatted = datetimeformat('2013-06-06 12:23:25.1231+05:00')
        self.assertEquals(formatted, '6 June 2013 at 08:23:25')


    def test_currency(self):
        self.assertEquals(currency(80000), '80,000.00')

import main
import unittest

class calcuatorTestCase(unittest.TestCase):

    def mainFunction(self):
        main.app.testing = True
        self.app = main.app.client()

    def integer(self):
        arg1 =  self.app.get('/div?A=7&B=5')
        self.assertEqual(b'1.4 \n', arg1.data)
        self.assertNotEqual(b'10.000 \n',arg1.data)
    def float(self):
        arg2 =  self.app.get('/div?A=5.9&B=2.3')
        self.assertEqual(b'2.56 \n', arg2.data)
        self.assertNotEqual(b'10.000 \n',arg2.data)
    def fraction(self):
        arg3 =  self.app.get('/div?A=8/3&B=3/8')
        self.assertEqual(b'7.20 \n', arg3.data)
        self.assertNotEqual(b'10.000 \n',arg3.data)
    def negative(self):
        arg4=  self.app.get('/div?A=5.1&B=-1.3')
        self.assertEqual(b'-3.92 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)
         
         
         
if __name__ == '__main__':
    unittest.main()
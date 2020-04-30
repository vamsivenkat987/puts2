import main
import unittest

class calcuatorTestCase(unittest.TestCase):

    def mainFunction(self):
        main.app.testing = True
        self.app = main.app.client()


    def AddInteger(self):
        arg1 =  self.app.get('/add?A=5&B=7')
        self.assertEqual(b'11 \n', arg1.data)
        self.assertNotEqual(b'10.000 \n',arg1.data)
    def AddFloat(self):
        arg2 =  self.app.get('/add?A=5.9&B=6.8')
        self.assertEqual(b'12.7 \n', arg2.data)
        self.assertNotEqual(b'10.000 \n',arg2.data)
    def AddFraction(self):
        arg3 =  self.app.get('/add?A=3/8&B=8/3')
        self.assertEqual(b'3.041 \n', arg3.data)
        self.assertNotEqual(b'10.000 \n',arg3.data)
    def AddNegative(self):
        arg4=  self.app.get('/add?A=5.1&B=-1.3')
        self.assertEqual(b'3.8 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)
		
    def SubInteger(self):
        arg1 =  self.app.get('/sub?A=7&B=5')
        self.assertEqual(b'2 \n', arg1.data)
        self.assertNotEqual(b'10.000 \n',arg1.data)
    def SubFloat(self):
        arg2 =  self.app.get('/sub?A=5.9&B=2.3')
        self.assertEqual(b'3.6 \n', arg2.data)
        self.assertNotEqual(b'10.000 \n',arg2.data)
    def SubFraction(self):
        arg3 =  self.app.get('/sub?A=8/3&B=3/8')
        self.assertEqual(b'2.28 \n', arg3.data)
        self.assertNotEqual(b'10.000 \n',arg3.data)
    def SubNegative(self):
        arg4=  self.app.get('/sub?A=5.1&B=-1.3')
        self.assertEqual(b'6.4 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)
		
    def MulInteger(self):
        arg1 =  self.app.get('/mul?A=7&B=5')
        self.assertEqual(b'35 \n', arg1.data)
        self.assertNotEqual(b'10.000 \n',arg1.data)
    def MulFloat(self):
        arg2 =  self.app.get('/mul?A=5.9&B=2.3')
        self.assertEqual(b'13.57 \n', arg2.data)
        self.assertNotEqual(b'10.000 \n',arg2.data)
    def MulFraction(self):
        arg3 =  self.app.get('/mul?A=8/3&B=3/8')
        self.assertEqual(b'0.99 \n', arg3.data)
        self.assertNotEqual(b'10.000 \n',arg3.data)
    def MulNegative(self):
        arg4=  self.app.get('/mul?A=5.1&B=-1.3')
        self.assertEqual(b'-6.63 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)


    def DivInteger(self):
        arg1 =  self.app.get('/div?A=7&B=5')
        self.assertEqual(b'1.4 \n', arg1.data)
        self.assertNotEqual(b'10.000 \n',arg1.data)
    def DivFloat(self):
        arg2 =  self.app.get('/div?A=5.9&B=2.3')
        self.assertEqual(b'2.56 \n', arg2.data)
        self.assertNotEqual(b'10.000 \n',arg2.data)
    def DivFraction(self):
        arg3 =  self.app.get('/div?A=8/3&B=3/8')
        self.assertEqual(b'7.20 \n', arg3.data)
        self.assertNotEqual(b'10.000 \n',arg3.data)
    def DivNegative(self):
        arg4=  self.app.get('/div?A=5.1&B=-1.3')
        self.assertEqual(b'-3.92 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)
         
         
         
if __name__ == '__main__':
    unittest.main()
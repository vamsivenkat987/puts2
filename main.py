from flask import Flask, request
from fractions import Fraction
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return 'gives the subtraction between arg1 and arg2'


@app.route('/mul')
def multiplication():
    arg1=request.args.get('A',default = 0, type = Fraction)
    arg2=request.args.get('B',default = 0, type = Fraction)
    X= Fraction(arg1)
    Y= Fraction(arg2)
    Z=X*Y
   
    result = str(Z).split('/')
    if len(result) == 2:
        first_arg = int(result[0])/int(result[1])
        second_arg = str(first_arg).split('.')
        if second_arg[1] == '0':
            return '$ \n'% second_arg[0]
        else:
            return '$ \n' % first_arg
    else:
        result1=str(Z).split('.')
        return '$ \n'% result1[0]


if __name__ == "__main__":
    app.run()
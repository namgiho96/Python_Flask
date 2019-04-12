import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def calc():
    stmt = request.args.get('stmt', 'NONE')  # 3항처리
    if stmt == 'NONE':
        print('넘어온 값이 없이')
    else:
        print('넘어온 식 {}:'.format(stmt))
        patt = '[0-9]+'
        op =re.sub(patt, '', stmt)
        print('넘어온 연산자 : {}'.format(op))
        nums = stmt.split(op)

        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '-':
            result = int(nums[0]) - int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        elif op == '/':
            result = int(nums[0]) / int(nums[1])


    return jsonify( result=result)


if __name__ == '__main__':
    app.run()

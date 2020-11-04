from flask import Flask, request, render_template
from random import randint
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('dice_result_generator.html')
    else:
        dice_type = int(request.form["dice_type"])
        no_of_dice_throws = int(request.form["no_of_dice_throws"])
        result_modifier = int(request.form["result_modifier"])

        check= 0
        result = 0
        while check != no_of_dice_throws:
            result += randint(1,dice_type)
            check += 1
        result += result_modifier
        return "wynik to: " + str(result)

if __name__ == "__main__":
    app.run()
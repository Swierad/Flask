from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('get_template.html')
    else:
        min = 0
        max = 1000
        answer = str(request.form["answer"])
        guess = (max - min) / 2 + min
        guess = int(guess)

        if answer == "jackpot":
            return 'brawo zgadłeś'
        elif answer == "to_small":
            min = int(request.form["guess"])
            max = int(request.form["max"])
            guess = (max - min) / 2 + min
            guess = int(guess)
            return render_template('post_template.html', guess = guess, min = min, max = max)
        elif answer == "to_much":
            min = int(request.form["min"])
            max = int(request.form["guess"])
            guess = (max - min) / 2 + min
            guess = int(guess)
            return render_template('post_template.html', guess = guess, min = min, max = max)
        else:
            guess = (max - min) / 2 + min
            guess = int(guess)
            return render_template('post_template.html', guess = guess, min = min, max = max)



if __name__ == "__main__":
    app.run()
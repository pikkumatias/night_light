from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        green_start = request.form.get('green_start')
        green_end = request.form.get('green_end')

        yellow_start = request.form.get('yellow_start')
        yellow_end = request.form.get('yellow_end')

        red_start = request.form.get('red_start')
        red_end = request.form.get('red_end')

        with open('color_times.txt', 'w') as file:
            file.write(f'{green_start},{green_end},{yellow_start},{yellow_end},{red_start},{red_end}')

        return 'Times updated succesfully'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask, render_template, request
porta = 777;
app = Flask (__name__, template_folder='./static')

@app.route('/', methods=['GET', 'POST'])
def home():
       if(request.method == 'GET'):
           return render_template('index.html');
       else:
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'sub'):
               subtracao = int(request.form['num1']) - int(request.form['num2'])
               return '<h1>'+ str(request.form['num1']) + ' - ' + str(request.form['num2']) + ' é igual a: ' + str(subtracao)+'</h1>'
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'soma'):
               soma = int(request.form['num1']) + int(request.form['num2'])
               return '<h1>'+ str(request.form['num1']) + ' + ' + str(request.form['num2']) + ' é igual a: ' + str(soma)+'</h1>'
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'mult'):
               multiplicacao = int(request.form['num1']) * int(request.form['num2'])
               return '<h1>'+ str(request.form['num1']) + ' x ' + str(request.form['num2']) + '  é igual a:  ' + str(multiplicacao)           
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'div'):
               divisao = int(request.form['num1']) / int(request.form['num2'])
               return '<h1>'+ str(request.form['num1']) + ' ÷ ' + str(request.form['num2']) + ' é igual a:  ' + str(divisao)+'</h1>'
           
           else:
               return 'Informe um valor válido!'
@app.errorhandler(404)
def not_found(error):
    return render_template('index.html')

app.run(port=porta, debug=True)
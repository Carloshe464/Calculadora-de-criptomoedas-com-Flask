from flask import Flask, render_template, request
from calculo_de_compra import compra
from cotacao_spot import obter_cotacao_spot


api_key = 'fc8936dc03264db5b0c9440586d6c5ee'
base_currency = 'USD'
target_currency = 'BRL'


#sempre iniciar a biblioteca Flask com o objeto de exemplo abaixo
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(('index.html'))


@app.route('/submit', methods=['POST'])
def submit():

    label1 = request.form.get('label1')
    label2 = request.form.get('label2')
    valor_moeda_em_dolar = label1
    total_de_moedas = label2

    try:
        valor_moeda_em_dolar = float(valor_moeda_em_dolar)
        total_de_moedas = float(total_de_moedas)
    except ValueError:
        print("Erro: Certifique-se de que os valores inseridos são numéricos.")
        return None



    resultado = compra(valor_moeda_em_dolar, total_de_moedas,api_key='fc8936dc03264db5b0c9440586d6c5ee', base_currency='USD', target_currency='BRL')

    return render_template('resultado_correto.html', valor_moeda_em_dolar=label1, total_de_moedas=label2, resultado=resultado)



if __name__== '__main__':

    app.run(debug=True)

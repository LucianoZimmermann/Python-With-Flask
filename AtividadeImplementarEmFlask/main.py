from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# rota para o exercicio 1
@app.route("/exercicio1", methods=['GET', 'POST'])
def exercicio1():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        if numero > 0:
            resultados = []
            for i in range(1, 11):
                resultado = numero * i
                resultados.append("{0} X {1} = {2}".format(numero, i, resultado))
            return render_template('exercicio1.html', resultados=resultados)
    return render_template('exercicio1.html')

@app.route("/exercicio2", methods=['GET', 'POST'])
def exercicio2():
    media = maior_nota = menor_nota = aprovado = None

    if request.method == 'POST':
        notas = []

        for i in range(1, 4):
            nota = float(request.form[f"nota{i}"])
            notas.append(nota)

        media = sum(notas) / len(notas)
        maior_nota = max(notas)
        menor_nota = min(notas)
        aprovado = media >= 6.0

    return render_template("exercicio2.html", media=media, maior_nota=maior_nota, menor_nota=menor_nota, aprovado=aprovado)

@app.route("/exercicio3", methods=['GET', 'POST'])
def exercicio3():
    if request.method == 'POST':
        impares = []
        pares = []

        for i in range(1, 6):
            numero_str = request.form.get(f"numero{i}", "")

            if numero_str and numero_str.isdigit():
                numero = int(numero_str)
                if numero % 2 == 0:
                    pares.append(numero)
                else:
                    impares.append(numero)

        sum_pares = sum(pares)
        avg_impares = sum(impares) / len(impares) if impares else 0

        return render_template("exercicio3.html", impares=impares, pares=pares, avg_impares=avg_impares,
                               sum_pares=sum_pares)

    return render_template("exercicio3.html")


# função principal
if __name__ == '__main__':
    app.run(port=3000, debug=True)

from flask import Flask, request

sabores_list = ['chocolate','pistache','baunilha','doce de leite']

app = Flask("Minha sorveteria")

@app.route("/")
def hello_world():
    return "<p>Hello Kike baiano</p>"

@app.route("/sabor/<int:id>",methods=["GET"])
def sabor(id):
    dict = {"sabores" : sabores_list[id]}
    return dict

@app.route("/sabores",methods=["GET"])
def sabores():
    dict_resposta = {"sabores" : sabores_list}
    return dict_resposta

@app.route("/adicionar_sabor",methods=["POST"])
def adiciona_sabor():
    novo = request.get_json()
    if "sabor" in novo:
        sabores_list.append(novo['sabor'])
        return f"Sabor {novo['sabor']} adicionado com sucesso!"
    return "Sabor não informado",400

@app.route("/apagar_sabor")
def apaga():
    if 'sabor' not in request.args:
        return "Sabor não informado",400
    sabor = request.args.get('sabor')
    if sabor not in sabores_list:
        return "Sabor não encontrado",404
    sabores_list.remove(sabor)
    return f"O sabor {sabor} foi removido com sucesso!"


if __name__=="__main__":
    app.run(debug=True)
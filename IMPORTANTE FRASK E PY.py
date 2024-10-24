from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados simples (em memória) de livros
livros = [
    {'id': 1, 'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis'},
    {'id': 2, 'titulo': '1984', 'autor': 'George Orwell'},
    {'id': 3, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'}
]

# Função para encontrar um livro pelo ID
def encontrar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return livro
    return None

# Rota para obter todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Rota para obter um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = encontrar_livro(id)
    if livro is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    return jsonify(livro)

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.json
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# Rota para atualizar um livro existente
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro = encontrar_livro(id)
    if livro is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404

    dados_atualizados = request.json
    livro.update(dados_atualizados)
    return jsonify(livro)

# Rota para deletar um livro pelo ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = encontrar_livro(id)
    if livro is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404

    livros.remove(livro)
    return jsonify({'mensagem': 'Livro deletado com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,jsonify, request
app = Flask(__name__)

todos = [
{ "label": "My first task", "done": False },
{ "label": "My second task", "done": False }
]

# Route to retrieve/RECUPERA the list of todos
@app.route('/todos', methods=['GET'])
def hello_world():
# Convert the todos list to a JSON response format 
    json_text = jsonify(todos)

# Return the JSON response to the front-end
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
# Guardo en una variable los datos que llegan desde el frontend en formato JSON
    request_body = request.json
# Agrego esos datos a la lista global de tareas (todos)
    todos.append(request_body)
# Convierto la lista actualizada de tareas a JSON válido para enviar como respuesta
    json_text = jsonify(todos)
# Devuelvo la respuesta JSON al frontend
    return json_text
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
# Elimina el elemento que está en la posición indicada dentro de la lista 'todos'
# Por ejemplo, si position es 0, borra el primer elemento
    todos.pop(position)
# Convierte la lista actualizada (después de borrar) en un formato JSON para devolver al frontend
     json_text = jsonify(todos)
# Devuelve esa respuesta JSON al cliente (por ejemplo, Postman o una app frontend)
    return json_text


if __name__ == '__main__':
app.run(host='0.0.0.0', port=3245, debug=True)

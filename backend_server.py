"""
Backend Python simple para chatbot de fiebre
Requiere: pip install flask flask-cors transformers torch

Ejecutar: python backend_server.py
"""

from flask import Flask, request, jsonify, stream_with_context, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Modelo simple sin cargar (requiere transformers)
# Para usar un modelo real, descomenta y ajusta:
# from transformers import AutoModelForCausalLM, AutoTokenizer
# model_name = "microsoft/Phi-3-mini-4k-instruct"  # Modelo ligero
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

SYSTEM_PROMPT = """Eres un asistente sanitario en español enfocado EXCLUSIVAMENTE al tema de la fiebre.
INSTRUCCIONES OBLIGATORIAS:
- Responde solo a preguntas relacionadas con la fiebre.
- Si la pregunta está fuera de este ámbito, recházala cortésmente.
- NO proporciones diagnóstico definitivo ni prescripción personalizada.
- Añade: "Esta información no sustituye atención médica profesional"."""

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    stream = data.get('stream', False)
    
    # Respuesta de ejemplo (reemplazar con modelo real)
    response_text = "La fiebre es un aumento de la temperatura corporal, generalmente superior a 38°C. Es una respuesta del sistema inmunológico a infecciones. Si persiste más de 3 días o supera 39°C, consulta a un médico. Esta información no sustituye atención médica profesional."
    
    if stream:
        def generate():
            for chunk in response_text.split():
                yield f'data: {{"choices":[{{"delta":{{"content":"{chunk} "}}}}]}}\n\n'
            yield 'data: [DONE]\n\n'
        return Response(stream_with_context(generate()), mimetype='text/event-stream')
    else:
        return jsonify({
            "message": {"role": "assistant", "content": response_text}
        })

@app.route('/api/tags', methods=['GET'])
def tags():
    return jsonify({"models": [{"name": "python-backend", "model": "python-backend"}]})

if __name__ == '__main__':
    print("Servidor backend ejecutándose en http://localhost:5000")
    app.run(port=5000, debug=True)


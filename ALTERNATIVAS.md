# Alternativas a Ollama para Chatbot de Fiebre

## Opción 1: LM Studio (Recomendada - Más ligera)

### Instalación:
1. Descarga desde: https://lmstudio.ai/
2. Instala y abre la aplicación
3. Descarga un modelo pequeño desde la interfaz (ej: `TinyLlama-1.1B`, `Phi-2`, `Qwen2-0.5B`)
4. Ve a "Local Server" y activa el servidor (puerto 1234 por defecto)

### Ventajas:
- ✅ Más ligero que Ollama
- ✅ Interfaz gráfica fácil
- ✅ API compatible con OpenAI
- ✅ Menor consumo de RAM
- ✅ Funciona bien en Windows

---

## Opción 2: Backend Python Simple (Más control)

### Instalación:
1. Instala Python 3.9+ desde python.org
2. Crea un entorno virtual:
```cmd
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors transformers torch
```

3. Ejecuta el servidor backend (ver `backend_server.py`)

### Ventajas:
- ✅ Control total sobre el modelo
- ✅ Puedes usar modelos de HuggingFace
- ✅ Lógica personalizada fácil

---

## Opción 3: API Externa (No requiere instalación local)

Servicios como HuggingFace Inference API o OpenAI (pero requiere API key y no es local).


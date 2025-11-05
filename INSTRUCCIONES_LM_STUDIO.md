# Cómo usar LM Studio (Alternativa ligera a Ollama)

## Paso 1: Instalar LM Studio

1. Descarga desde: **https://lmstudio.ai/**
2. Instala y ejecuta la aplicación

## Paso 2: Descargar un modelo ligero

1. En LM Studio, ve a la pestaña **"Search"** (buscar)
2. Busca un modelo pequeño como:
   - `TinyLlama-1.1B` (muy ligero, ~600MB)
   - `Qwen2-0.5B` (ultra ligero, ~350MB)
   - `Phi-2` (Microsoft, ~1.3GB)
3. Haz clic en **"Download"** y espera a que termine

## Paso 3: Cargar el modelo (IMPORTANTE)

**¡Este paso es crítico!** El modelo debe estar CARGADO en memoria antes de usar el servidor.

**Opción A - Desde la interfaz:**
1. En LM Studio, ve a la pestaña **"Chat"** o **"Local Server"**
2. En el selector de modelo (arriba), selecciona el modelo que descargaste
3. Espera a que aparezca "Loaded" o similar

**Opción B - Desde línea de comandos:**
```cmd
lms load gemma3:1b
```
(O el nombre exacto de tu modelo)

## Paso 4: Activar el servidor local

1. En LM Studio, ve a la pestaña **"Local Server"** (servidor local)
2. Asegúrate de que el modelo está seleccionado y cargado
3. Haz clic en **"Start Server"** (iniciar servidor)
4. Debería mostrar: "Server running on http://localhost:1234"

## Paso 5: Configurar la app React

1. Abre `src/components/Chat.tsx`
2. En la línea 10, cambia:
   ```typescript
   const BACKEND_TYPE: 'ollama' | 'lmstudio' = 'lmstudio'
   ```
3. En la línea 11, ajusta el nombre del modelo si es necesario:
   ```typescript
   const MODEL_NAME = 'TinyLlama-1.1B' // o el nombre que veas en LM Studio
   ```

## Paso 6: Probar la conexión

1. Recarga la página web (`http://localhost:5173`)
2. Haz clic en **"Probar conexión"**
3. Debería mostrar: "Conexión OK: X modelo(s) detectados"
4. ¡Listo! Puedes empezar a chatear

## Ventajas de LM Studio

- ✅ Más ligero que Ollama
- ✅ Interfaz gráfica intuitiva
- ✅ Mejor gestión de modelos
- ✅ Funciona mejor en Windows
- ✅ Menor consumo de recursos

## Solución de problemas

**Error "Conexión fallida":**
- Verifica que el servidor esté corriendo en LM Studio
- Asegúrate de que el puerto 1234 esté disponible
- Reinicia LM Studio

**Error "model_not_found" o "No models loaded":**
- **El modelo debe estar CARGADO antes de usar el servidor**
- Ve a la pestaña "Chat" y carga el modelo primero
- O ejecuta desde CMD: `lms load gemma3:1b`
- Luego activa el servidor en "Local Server"

**El modelo no responde:**
- Verifica que el modelo esté cargado en "Local Server"
- Asegúrate de que el nombre del modelo en Chat.tsx coincida exactamente
- Prueba con un modelo más pequeño
- Revisa la consola del navegador (F12) para errores


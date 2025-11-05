# 🌡️ Agente sobre Fiebre - Guía de Instalación y Uso

Aplicación web de chat especializada en información sobre fiebre, desarrollada con React + Vite y conectada a LM Studio u Ollama para procesamiento de lenguaje natural.

**⚠️ Nota:** Este es un prototipo para pruebas locales. Solo funciona en desarrollo.

## 📋 Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Instalación](#instalación)
3. [Configuración](#configuración)
4. [Desarrollo Local](#desarrollo-local)
5. [Solución de Problemas](#solución-de-problemas)

---

## 🔧 Requisitos Previos

### Software Necesario

1. **Node.js** (versión 16 o superior)
   - Descargar desde: https://nodejs.org/
   - Verificar instalación: `node --version`
   - Verificar npm: `npm --version`

2. **LM Studio** (recomendado) o **Ollama**
   - **LM Studio**: https://lmstudio.ai/
   - **Ollama**: https://ollama.ai/
   - Ver instrucciones detalladas en `INSTRUCCIONES_LM_STUDIO.md`

3. **Git** (opcional, para clonar el repositorio)
   - Descargar desde: https://git-scm.com/

### Sistema Operativo

- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux

---

## 📦 Instalación

### Paso 1: Obtener el Código

Si tienes el código en un repositorio:
```bash
git clone <url-del-repositorio>
cd fiebre
```

Si tienes el código en una carpeta, simplemente navega a ella:
```bash
cd ruta/a/fiebre
```

### Paso 2: Instalar Dependencias

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
npm install
```

Este comando instalará:
- React 18.3.1
- React DOM 18.3.1
- Vite 5.4.10
- TypeScript 5.6.3
- Y todas las dependencias de desarrollo necesarias

**Tiempo estimado:** 2-5 minutos (dependiendo de la velocidad de internet)

### Paso 3: Verificar Instalación

Verifica que todo se instaló correctamente:

```bash
npm list --depth=0
```

Deberías ver las dependencias listadas sin errores.

---

## ⚙️ Configuración

### Configurar el Backend (LM Studio u Ollama)

#### Opción A: Usar LM Studio (Recomendado)

1. **Instalar LM Studio**
   - Descarga desde: https://lmstudio.ai/
   - Instala y ejecuta la aplicación

2. **Descargar el Modelo**
   - En LM Studio, ve a la pestaña **"Search"**
   - Busca y descarga: `google/gemma-3-1b`
   - Espera a que termine la descarga

3. **Cargar el Modelo** ⚠️ **IMPORTANTE**
   - Ve a la pestaña **"Chat"** o **"Local Server"**
   - Selecciona el modelo descargado en el selector superior
   - Espera a que aparezca "Loaded" o similar

4. **Iniciar el Servidor**
   - Ve a la pestaña **"Local Server"**
   - Haz clic en **"Start Server"**
   - Debería mostrar: "Server running on http://localhost:1234"

5. **Configurar la Aplicación**
   - Abre `src/components/Chat.tsx`
   - Verifica que la línea 10 tenga:
     ```typescript
     const BACKEND_TYPE: 'ollama' | 'lmstudio' = 'lmstudio'
     ```
   - Verifica que la línea 11 tenga el nombre correcto del modelo:
     ```typescript
     const MODEL_NAME = 'google/gemma-3-1b'
     ```

#### Opción B: Usar Ollama

1. **Instalar Ollama**
   - Descargar desde: https://ollama.ai/
   - Instalar y ejecutar

2. **Descargar el Modelo**
   ```bash
   ollama pull google/gemma-3-1b
   ```
   Espera a que termine la descarga del modelo.

3. **Verificar que Ollama esté corriendo**
   - Ollama debería iniciarse automáticamente
   - Verifica en: http://localhost:11434

4. **Configurar la Aplicación**
   - Abre `src/components/Chat.tsx`
   - Cambia la línea 10 a:
     ```typescript
     const BACKEND_TYPE: 'ollama' | 'lmstudio' = 'ollama'
     ```
   - Verifica que la línea 11 tenga:
     ```typescript
     const MODEL_NAME = 'google/gemma-3-1b'
     ```

---

## 🚀 Desarrollo Local

### Paso 1: Iniciar el Servidor de Desarrollo

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
npm run dev
```

Deberías ver algo como:
```
  VITE v5.4.10  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### Paso 2: Abrir en el Navegador

Abre tu navegador y ve a:
```
http://localhost:5173
```

### Paso 3: Verificar la Conexión

1. En la aplicación, haz clic en el botón **"🔌 Probar conexión"**
2. Deberías ver: "Conexión OK: X modelo(s) detectados"
3. Si hay error, consulta la sección [Solución de Problemas](#solución-de-problemas)

### Paso 4: Probar la Aplicación

1. Escribe una pregunta en el campo de texto, por ejemplo: "¿Qué es la fiebre?"
2. Haz clic en **"📤 Enviar"** o presiona Enter
3. Deberías recibir una respuesta del asistente

---

## 🔍 Solución de Problemas

### Error: "npm: command not found"

**Solución:** Node.js no está instalado o no está en el PATH. Instala Node.js desde https://nodejs.org/

### Error: "Cannot find module"

**Solución:** Las dependencias no están instaladas. Ejecuta:
```bash
npm install
```

### Error al ejecutar `npm run dev`

**Solución 1:** Verifica que el puerto 5173 no esté en uso:
```bash
# Windows
netstat -ano | findstr :5173

# Linux/Mac
lsof -i :5173
```

**Solución 2:** Cambia el puerto en `vite.config.ts`:
```typescript
server: {
  port: 3000, // Cambia a otro puerto
}
```

### Error: "Conexión fallida" al probar la conexión

**Causas y Soluciones:**

1. **LM Studio no está corriendo**
   - Abre LM Studio
   - Ve a "Local Server"
   - Haz clic en "Start Server"
   - Verifica que diga "Server running on http://localhost:1234"

2. **El modelo no está cargado**
   - En LM Studio, ve a la pestaña "Chat"
   - Selecciona el modelo en el selector superior
   - Espera a que aparezca "Loaded"
   - Luego inicia el servidor en "Local Server"

3. **Puerto incorrecto**
   - Verifica que LM Studio esté en el puerto 1234
   - O que Ollama esté en el puerto 11434
   - Verifica la configuración en `vite.config.ts`

4. **Firewall bloqueando**
   - Permite Node.js y LM Studio/Ollama en el firewall de Windows

### Error: "model_not_found" o "No models loaded"

**Solución:**
- El modelo debe estar **CARGADO** antes de usar el servidor
- En LM Studio: Ve a "Chat" → Selecciona el modelo → Espera a que cargue
- Luego inicia el servidor en "Local Server"

### Error: El modelo no responde

**Soluciones:**

1. Verifica que el nombre del modelo en `Chat.tsx` coincida exactamente con el nombre en LM Studio/Ollama

2. Verifica que el modelo `google/gemma-3-1b` esté correctamente descargado y cargado

3. Revisa la consola del navegador (F12) para ver errores detallados

4. Verifica que el modelo esté completamente cargado

### Error en TypeScript: "compilation failed"

**Solución:**
1. Verifica que todos los archivos TypeScript estén correctos:
   ```bash
   npx tsc --noEmit
   ```

2. Corrige los errores mostrados

---

## 📝 Comandos Útiles

```bash
# Instalar dependencias
npm install

# Desarrollo local
npm run dev

# Verificar tipos TypeScript
npx tsc --noEmit

# Limpiar node_modules (si hay problemas)
# Windows
rmdir /s /q node_modules
del package-lock.json
npm install

# Linux/Mac
rm -rf node_modules package-lock.json
npm install
```

---

## 📚 Estructura del Proyecto

```
fiebre/
├── src/
│   ├── components/
│   │   └── Chat.tsx          # Componente principal del chat
│   ├── App.tsx               # Componente principal de la app
│   ├── main.tsx              # Punto de entrada
│   └── styles.css            # Estilos globales
├── node_modules/             # Dependencias (generadas con npm install)
├── index.html                # HTML principal
├── package.json              # Configuración y dependencias
├── vite.config.ts            # Configuración de Vite (incluye proxy para desarrollo)
├── tsconfig.json             # Configuración de TypeScript
├── backend_server.py         # Servidor Python alternativo (opcional)
├── INSTRUCCIONES_LM_STUDIO.md # Instrucciones detalladas de LM Studio
└── README.md                 # Este archivo
```

---

## 🆘 Soporte

Si encuentras problemas:

1. Revisa la sección [Solución de Problemas](#solución-de-problemas)
2. Verifica que todos los requisitos previos estén instalados
3. Revisa los logs de la consola del navegador (F12)
4. Revisa los logs del servidor de desarrollo
5. Consulta `INSTRUCCIONES_LM_STUDIO.md` para problemas específicos de LM Studio

---

## 📄 Licencia

Este proyecto es de uso educativo y no sustituye atención médica profesional.

---

**¡Listo para probar!** 🚀

Este es un prototipo que funciona solo en desarrollo local. Asegúrate de tener LM Studio u Ollama corriendo antes de usar la aplicación.


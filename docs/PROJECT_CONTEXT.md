# NEXUS - Project Context

## 1. Identidad
Nombre: NEXUS
Tipo: asistente personal de inteligencia artificial.
Sistema objetivo inicial: Windows.
Idioma principal: español latinoamericano.
Activación por voz: "NEXUS".
Voz deseada: masculina, profunda, estilo asistente cinematográfico.

## 2. Visión
NEXUS debe ser un asistente capaz de comprender instrucciones,
mantener conversaciones naturales, recordar información autorizada
y ejecutar tareas en el equipo mediante herramientas controladas.

No debe limitarse a responder texto: debe planificar, ejecutar,
verificar el resultado y comunicarlo con honestidad.

## 3. Funciones previstas

### Voz
- Detectar localmente la palabra "NEXUS".
- Capturar instrucciones después de la activación.
- Comprender español latinoamericano.
- Responder mediante voz.
- Permitir silenciar el micrófono.
- No enviar audio ambiental a servicios externos antes de activarse.

### Inteligencia
- Comprensión de lenguaje natural.
- Contexto conversacional.
- Memoria persistente.
- Selección de herramientas según la solicitud.
- Verificación de resultados.

### Windows
- Abrir aplicaciones.
- Abrir carpetas y archivos.
- Controlar tareas permitidas.
- Ejecutar comandos autorizados.
- Automatizar navegador cuando sea apropiado.

### Integraciones futuras
- Gmail mediante OAuth.
- WhatsApp mediante integraciones oficiales o métodos permitidos.
- Telegram.
- n8n.
- Otros servicios según disponibilidad de API.

### Archivos
- Crear documentos Word.
- Crear hojas Excel.
- Generar PDF.
- Organizar archivos bajo autorización.

### Interfaz
- Dashboard oscuro y futurista.
- Estado del asistente.
- Estado del micrófono.
- Historial de acciones.
- Panel de módulos y configuraciones.

## 4. Tecnologías propuestas
- Python como lenguaje principal.
- FastAPI para backend.
- OpenAI API y Realtime API para inteligencia y voz.
- Porcupine para palabra de activación local.
- PostgreSQL para datos estructurados.
- Qdrant para memoria semántica.
- n8n para flujos de automatización.
- Playwright para navegador.
- PowerShell para operaciones de Windows.
- HTML, CSS y JavaScript para interfaz.
- Git y GitHub para control de versiones.
- Docker para servicios que lo requieran.

Las tecnologías son propuestas iniciales. Los cambios deben justificarse
y documentarse en DECISIONS.md.

## 5. Seguridad obligatoria
- Las claves se guardan en `.env`, nunca en el repositorio.
- Usar `.env.example` sin credenciales reales.
- Aplicar mínimo privilegio.
- Validar argumentos antes de ejecutar comandos.
- Mantener lista permitida de herramientas.
- Pedir aprobación antes de enviar mensajes o correos,
  publicar contenido, instalar software o ejecutar acciones destructivas.
- Registrar acciones y errores sin almacenar secretos.
- No intentar evadir controles de seguridad de aplicaciones o servicios.

## 6. Reglas de desarrollo
1. Leer esta documentación antes de modificar arquitectura.
2. No afirmar que una función está terminada sin probarla.
3. Implementar módulos pequeños y verificables.
4. Mantener código legible y documentado.
5. Agregar pruebas cuando corresponda.
6. Actualizar TASKS.md al completar o iniciar tareas.
7. Registrar decisiones técnicas en DECISIONS.md.
8. Revisar cambios antes de integrarlos a la rama principal.

## 7. Colaboración con asistentes
ChatGPT y Claude deben utilizar este repositorio como fuente compartida.
Antes de trabajar, deben revisar:
- PROJECT_CONTEXT.md
- ARCHITECTURE.md
- ROADMAP.md
- TASKS.md
- DECISIONS.md

Ningún asistente debe asumir que conoce cambios que no estén guardados
en el repositorio.

## 8. Estado actual
- Carpeta inicial creada.
- Git inicializado.
- Python y Git detectados.
- Documentación inicial en preparación.
- No hay funcionalidades implementadas todavía.

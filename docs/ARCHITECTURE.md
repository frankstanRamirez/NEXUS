# Arquitectura inicial de NEXUS

## Principio
Arquitectura modular. Cada módulo tendrá responsabilidades definidas
y se comunicará mediante interfaces controladas.

## Flujo de voz

Microfono
  -> Detector local de palabra "NEXUS"
  -> Captura de instruccion
  -> Motor de conversacion
  -> Interpretacion de intencion
  -> Validador de permisos
  -> Herramienta autorizada
  -> Verificacion del resultado
  -> Respuesta por voz

## Modulos previstos

### backend/voice
Captura de audio, activacion local, reconocimiento y respuesta de voz.

### backend/core
Coordinacion del asistente, contexto, decisiones y ejecucion de herramientas.

### backend/desktop
Operaciones controladas sobre Windows.

### backend/integrations
Conectores con servicios externos.

### backend/memory
Persistencia y recuperacion de memoria.

### frontend
Dashboard de control.

### config
Configuracion y carga segura de variables de entorno.

### tests
Pruebas automatizadas.

## Reglas de arquitectura
- La interfaz no ejecuta comandos directamente.
- El modelo no debe ejecutar comandos arbitrarios sin validacion.
- Toda herramienta debe validar sus entradas.
- Las acciones sensibles requieren aprobacion.
- La capa de voz debe poder probarse independientemente.
- La memoria debe permitir consultar y corregir informacion.

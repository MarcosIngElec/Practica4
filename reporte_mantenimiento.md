# Reporte de mantenimiento eléctrico

Total de incidencias: 5

## SUB-001 - Transformador de Potencia
- Síntoma: Elevación extrema de temperatura y gases disueltos en el aceite
- Causa raíz: Degradación del aislamiento de papel por sobrecarga continua
- Gravedad: Crítica
- Soluciones:
  - Inmediata: Reducción manual de carga y activación de ventilación forzada auxiliar
  - Análisis: Prueba de Cromatografía de Gases Disueltos (DGA) en laboratorio
  - Definitiva: Filtrado y desgasificación del aceite o sustitución de bobinados

## SUB-002 - Interruptor de Potencia en SF6
- Síntoma: Alarma por baja presión de gas SF6 en la bahía de línea
- Causa raíz: Fuga micrométrica en los sellos de elastómero debido a envejecimiento
- Gravedad: Alta
- Soluciones:
  - Inmediata: Bloqueo de operaciones de apertura en carga para evitar arco eléctrico catastrófico
  - Análisis: Localización de fugas mediante cámara térmica infrarroja para SF6 o detector ultrasónico
  - Definitiva: Sustitución de juntas tóricas y recarga de gas SF6 hasta la presión nominal

## LIN-001 - Conductores de Fase
- Síntoma: Cortocircuito fase-tierra intermitente en días de altas temperaturas
- Causa raíz: Flecha excesiva (sag) por dilatación térmica que viola las distancias mínimas de seguridad con la vegetación
- Gravedad: Alta
- Soluciones:
  - Inmediata: Despacho de cuadrilla de emergencia para poda de árboles bajo la línea
  - Análisis: Monitoreo de temperatura del conductor en tiempo real (DLR - Dynamic Line Rating)
  - Definitiva: Tensado del conductor o instalación de torres de mayor altura

## PQ-001 - Bancos de Condensadores
- Síntoma: Explosión prematura y sobrecalentamiento de las celdas de capacitores
- Causa raíz: Resonancia armónica provocada por variadores de frecuencia y cargas no lineales
- Gravedad: Alta
- Soluciones:
  - Inmediata: Desconexión segura del banco de condensadores afectado
  - Análisis: Medición con analizador de redes clase A para registrar el espectro de armónicos (THD)
  - Definitiva: Instalación de reactores de rechazo (filtros desintonizados) en serie con los condensadores

## PQ-002 - Motores de Inducción
- Síntoma: Pérdida de torque, vibraciones mecánicas anómalas y sobrecalentamiento en los devanados
- Causa raíz: Desequilibrio de tensiones (voltage unbalance) en las fases de alimentación superior al 2%
- Gravedad: Media
- Soluciones:
  - Inmediata: Reducción de la carga mecánica del motor (derating) para evitar fallas
  - Análisis: Verificación de la simetría de cargas en el tablero de distribución principal
  - Definitiva: Redistribución de cargas monofásicas o instalación de un regulador automático de voltaje de respuesta rápida

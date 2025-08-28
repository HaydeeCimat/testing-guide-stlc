Ejecución de pruebas
====================

La ejecución de pruebas constituye la fase operativa del subproceso, donde se ejecutan los casos de prueba previamente diseñados para verificar y validar el funcionamiento del sistema conforme a los requisitos establecidos. Esta fase incluye pruebas unitarias, de integración, sistema, regresión y otras pruebas específicas aplicables a CubeSats, como aquellas que simulan condiciones espaciales. También se registran los resultados, se gestionan defectos y se documentan hallazgos.

Actividades principales
-------------------------

- DV3.1 – Ejecución de Pruebas Unitarias
Validación funcional de los componentes individuales del software, asegurando que cada módulo cumple con sus especificaciones antes de la integración.

- DV3.2 – Ejecución de Pruebas de Integración
Validación de la correcta interacción entre los módulos o subsistemas, verificando interfaces, comunicación y flujo de datos entre componentes.

- DV3.3 – Ejecución de Pruebas de Sistema
Evaluación del comportamiento general del sistema completo en un entorno controlado, validando funcionalidades end-to-end y requisitos del sistema.

- DV3.4 – Ejecución de Pruebas de Regresión
Revalidación de funcionalidades ya probadas para detectar defectos introducidos por cambios recientes, garantizando que las modificaciones no afecten el comportamiento existente.

- DV3.5 – Ejecución de Pruebas de Rendimiento
Evaluación del uso de recursos, tiempos de respuesta y carga del sistema bajo diferentes condiciones operativas.

- DV3.6 – Ejecución de Pruebas de Seguridad
Evaluación de vulnerabilidades, integridad de datos y protección contra acceso no autorizado, especialmente crítico en sistemas espaciales.

- VV2.3 – Registro y seguimiento de resultados
Registro estructurado de resultados, evidencias, logs y hallazgos para asegurar la trazabilidad y facilitar el análisis posterior.

- Gestión de interrupciones o incidencias
Registro, análisis y decisión sobre reinicio o continuación de pruebas ante errores o fallos técnicos durante la ejecución.

Productos de trabajo
---------------------

**Entrada necesaria**
- Casos de Prueba [Aprobados]
- Procedimientos de Prueba [Documentados]
- Datos de Prueba [Validados]
- Entorno de Pruebas [Configurado]
- Plan de Pruebas [Aprobado]

**Salida esperada**
- Resultados de Pruebas Unitarias - Registro de la validación de componentes individuales
- Resultados de Pruebas de Integración - Documentación de la interacción entre módulos
- Resultados de Pruebas de Sistema - Evaluación del comportamiento del sistema completo
- Resultados de Pruebas de Regresión - Verificación de funcionalidades tras modificaciones
- Informes de Rendimiento - Métricas de eficiencia y uso de recursos
- Informes de Seguridad - Evaluación de vulnerabilidades y robustez
- Reporte de Defectos - Listado estructurado de errores encontrados
- Bitácora de Ejecución de Pruebas - Registro cronológico de actividades realizadas
- Registros de Incidentes - Documentación de interrupciones o problemas durante la ejecución

Productos de apoyo
-------------------
Durante la ejecución se generan productos internos como logs del sistema, capturas de pantalla, evidencias documentales y gráficas, notas de validación por pares, y matriz de cobertura actualizada.

Roles y responsabilidades
--------------------------

.. list-table::
   :header-rows: 1

   * - Rol
     - Responsabilidad
   * - **Equipo de Pruebas**
     - Ejecutar casos de prueba, registrar resultados y gestionar defectos
   * - **Desarrolladores**
     - Proporcionar soporte técnico y corregir defectos identificados
   * - **Líder Técnico**
     - Supervisar la ejecución y tomar decisiones sobre continuidad de pruebas
   * - **Cliente/Usuario**
     - Participar en pruebas de aceptación y validar funcionalidades críticas

Diagrama de Ejecución de Pruebas
---------------------------------

.. figure:: /_static/images/Guia_P4.png
   :alt: Diagrama de ejecución de pruebas
   :width: 100%
   :align: center

   Figura 5. Diagrama que representa la secuencia de actividades, flujo de productos y roles involucrados durante la fase de ejecución de pruebas.

Herramientas recomendadas
--------------------------

**Gestión y ejecución**
- Herramientas de gestión - Jira, Xray, TestLink, qTest para seguimiento y documentación
- Automatización - Selenium, Pytest, Robot Framework, JUnit para pruebas automatizadas
- Simuladores - Bancos de pruebas espaciales y simuladores de condiciones ambientales

**Monitoreo y análisis**
- Rendimiento - JMeter, Locust, wrk, htop para evaluación de performance
- Gestión de defectos - Bugzilla, Mantis, Redmine para seguimiento de errores
- Logging - Herramientas de registro estructurado y análisis de logs

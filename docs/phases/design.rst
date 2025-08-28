Diseño de pruebas
=================

El diseño de pruebas define y documenta los casos de prueba, los procedimientos, los datos y las condiciones necesarias para validar que el sistema cumple con los requisitos especificados. Se busca garantizar la trazabilidad entre los requisitos y las pruebas, así como preparar el entorno y los insumos requeridos para su correcta ejecución.

Actividades principales
------------------------

- DF2.2 – Diseñar Casos de Prueba basados en los Requisitos del Sistema
Elaboración de casos de prueba que permitan validar funcionalidades, condiciones límite, excepciones y requisitos no funcionales.

- DF2.3 – Revisar y Aprobar Casos de Prueba
Validación de la cobertura, claridad y aplicabilidad de los casos de prueba mediante revisión técnica y aprobación formal por parte de líderes técnicos y/o gerencia.

- DF2.4 – Preparación de Datos de Prueba
Diseño o selección de datos que representen condiciones reales, límites y escenarios de fallo controlado, asegurando su integridad y trazabilidad.

- DF2.5 – Configuración del Entorno de Pruebas
Instalación, validación y documentación del entorno donde se realizarán las pruebas (simuladores, hardware, software, versiones).

- VV2.3 – Ajustes al Plan de Validación
En caso de identificar nuevos criterios o escenarios durante el diseño, actualización del plan de validación para mantener la consistencia.

Productos de trabajo
---------------------

**Entrada necesaria**
- Plan de Pruebas [Aprobado]
- Requisitos del Sistema [Verificado]
- Documento de Análisis de Requisitos
- Ambiente de Pruebas
- Plan de Validación [Revisado]

**Salida esperada**
- Casos de Prueba [Aprobados] - Conjunto estructurado de entradas, condiciones esperadas, pasos y criterios de evaluación
- Procedimientos de Prueba [Documentados] - Instrucciones detalladas para ejecutar pruebas de manera repetible y trazable
- Datos de Prueba [Listos] - Conjuntos de datos reales, simulados o híbridos, preparados y validados para su uso
- Entorno de Pruebas [Configurado] - Equipos, herramientas y versiones configuradas para ejecución

Productos de apoyo
------------------
Durante la ejecución pueden generarse productos internos como plantillas de casos de prueba, listas de verificación de cobertura, matriz de trazabilidad requisitos ↔ pruebas, logs de preparación de entornos y bitácora técnica de validaciones previas.

Roles y responsabilidades
---------------------------

.. list-table::
   :header-rows: 1

   * - Rol
     - Responsabilidad
   * - **Equipo de Pruebas**
     - Diseñar y documentar casos de prueba y procedimientos
   * - **Desarrolladores**
     - Aportar conocimiento técnico sobre diseño y arquitectura del sistema
   * - **Líder Técnico**
     - Verificar consistencia entre análisis, diseño y especificaciones
   * - **Cliente/Usuario**
     - Contribuir en la definición de criterios de aceptación finales

Diagrama de Diseño de Pruebas
------------------------------

.. figure:: /_static/images/Guia_P3.png
   :alt: Diagrama de diseño de pruebas
   :width: 100%
   :align: center

   Figura 4. Diagrama que representa la relación entre actividades, productos y actores durante la fase de diseño de pruebas.

Herramientas recomendadas
---------------------------

- Diseño de pruebas - TestLink, Xray, qTest, Zephyr para gestión formal de casos de prueba
- Técnicas de diseño - Partición de equivalencia, análisis de valores límite, pruebas basadas en estado
- Modelado - Diagramas de flujo o diagramas de transición de estado
- Simulación - Simuladores de sensores o subsistemas CubeSat
- Trazabilidad - Hojas de cálculo estructuradas, ReqView, Jira para seguimiento de requisitos
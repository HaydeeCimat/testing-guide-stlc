Productos de Trabajo
============================

Esta sección presenta una descripción de los productos de trabajo generados, utilizados o modificados en el subproceso de pruebas propuesto. Cada producto se acompaña de su descripción general, su posible estado de avance y su origen dentro del flujo de fases. 

Esta clasificación permite identificar claramente los productos claves por fase, facilitar su control de versiones, trazabilidad y evaluación durante auditorías o revisiones internas.

Estados de los productos de trabajo
-----------------------------------

Los estados definidos para los productos en esta guía son los siguientes:

- **[Iniciado]**: El producto ha sido creado o cargado, pero aún no ha sido revisado o validado formalmente.  
- **[Revisado]**: El producto ha sido evaluado internamente por el equipo de trabajo.  
- **[Verificado]**: El producto cumple con los criterios definidos y ha sido evaluado en su estructura técnica.  
- **[Validado]**: El producto ha sido probado o aceptado en un entorno representativo del sistema o misión.  

Descripción de productos de trabajo
---------------------------------------------

.. list-table:: Descripción de productos de trabajo
   :header-rows: 1
   :widths: 25 35 20 20

   * - Producto de Trabajo
     - Descripción
     - Fase / Origen
     - Estado Esperado
   * - Requisitos, Arquitectura y Diseño de Software
     - Conjunto validado de especificaciones que sirven como base para planear y diseñar las pruebas.
     - Entrada al proceso
     - Validado
   * - Documento de Análisis de Requisitos
     - Documento que resume el análisis funcional, dependencias y criterios de validación extraídos de los requisitos aprobados.
     - Análisis de Requisitos
     - Revisado
   * - Plan de Pruebas
     - Documento que describe la estrategia, recursos, cronograma y criterios de aceptación del subproceso.
     - Planificación de Pruebas
     - Aprobado / Verificado
   * - Casos de Prueba y Procedimientos
     - Conjunto de escenarios, entradas, pasos y resultados esperados usados para validar funcionalidad.
     - Diseño de Pruebas
     - Aprobado
   * - Datos de Prueba
     - Información utilizada durante la ejecución de pruebas (simulada, real o combinada).
     - Diseño de Pruebas
     - Verificado
   * - Entorno de Pruebas Configurado
     - Ambiente físico o virtual preparado para ejecutar los casos de prueba de integración o sistema.
     - Diseño / Ejecución
     - Verificado
   * - Resultados de Pruebas
     - Registro de salidas y evidencias generadas durante la ejecución de pruebas.
     - Ejecución de Pruebas
     - Verificado
   * - Reporte de Defectos
     - Listado de errores encontrados, su clasificación y estado de resolución.
     - Ejecución de Pruebas
     - Revisado
   * - Reporte de Pruebas de Regresión
     - Resultados de pruebas aplicadas para verificar corrección de errores anteriores.
     - Ejecución / Cierre
     - Verificado
   * - Reporte de Aceptación del Cliente
     - Documento que refleja el cumplimiento de los criterios de aceptación por parte del cliente.
     - Cierre de Pruebas
     - Validado
   * - Reporte de Control de Calidad
     - Documento generado para asegurar el cumplimiento de estándares de pruebas y procesos definidos.
     - Cierre de Pruebas
     - Revisado
   * - Informe Postmortem
     - Documento que recopila hallazgos, decisiones y lecciones aprendidas para futuras mejoras.
     - Postmortem
     - Revisado
   * - Planes de Mejora del Proceso
     - Propuestas derivadas de análisis postmortem para optimizar futuras implementaciones.
     - Postmortem
     - Iniciado
   * - Repositorio de Versiones y Evidencias
     - Herramienta o contenedor donde se almacenan productos, versiones, evidencia de pruebas y control de cambios.
     - Soporte Transversal
     - Actualizado
   * - Lista de Recursos
     - Listado de recursos humanos, técnicos o de infraestructura requeridos para la ejecución del subproceso de pruebas.
     - Planificación de Pruebas
     - Revisado
   * - Lista de Roles Asignados
     - Documento que establece la asignación de responsabilidades a los participantes del proceso de pruebas.
     - Planificación de Pruebas
     - Revisado
   * - Estrategia de Control de Versiones
     - Definición del mecanismo para el control, almacenamiento y trazabilidad de los productos de trabajo del subproceso.
     - Planificación de Pruebas
     - Verificado
   * - Resultados de Pruebas Unitarias
     - Registro de la ejecución de pruebas en componentes individuales del software.
     - Ejecución de Pruebas
     - Verificado
   * - Resultados de Pruebas de Integración
     - Resultado de la validación de interacción entre módulos o componentes del sistema.
     - Ejecución de Pruebas
     - Verificado
   * - Resultados de Pruebas de Sistema
     - Pruebas aplicadas al sistema completo validando funcionalidad, comportamiento y restricciones generales.
     - Ejecución de Pruebas
     - Verificado
   * - Informes de Rendimiento
     - Resultados de pruebas realizadas para medir eficiencia, uso de recursos y tiempos de respuesta del sistema.
     - Ejecución de Pruebas
     - Revisado
   * - Informes de Seguridad
     - Documentos generados al validar aspectos relacionados con la robustez, vulnerabilidades y confiabilidad del sistema.
     - Ejecución de Pruebas
     - Revisado
   * - Reporte de Verificación del Sistema
     - Documento que registra la verificación formal del sistema en condiciones simuladas representativas del entorno espacial.
     - Cierre de Pruebas
     - Verificado
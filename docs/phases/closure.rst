Cierre de pruebas
=================

# Cierre de Pruebas

El cierre de pruebas consolida los resultados obtenidos durante la ejecución, valida la conformidad del sistema respecto a los criterios definidos, formaliza la aceptación del software por parte del cliente, y genera productos de cierre que permiten retroalimentar futuras iteraciones o proyectos similares.

## Propósito

Esta fase tiene como objetivo principal asegurar que todos los criterios de aceptación han sido cumplidos y que el sistema está listo para su despliegue o entrega final. Se enfoca en la validación formal del software en condiciones representativas del entorno operativo del CubeSat.

## Actividades principales

### IM4.1 – Validación del Sistema
Confirmación mediante evidencia documentada de que el sistema cumple con los criterios de aceptación establecidos, verificando el cumplimiento de todos los requisitos funcionales y no funcionales.

### IM4.2 – Verificación del Sistema en Condiciones Simuladas
Ejecución de pruebas en entornos que representen las condiciones operativas del CubeSat, incluyendo:
- Simulación de vacío térmico
- Pruebas de vibración
- Simulación de fallas controladas
- Condiciones de radiación simulada
- Latencias de comunicación espacial

### AC6.1 – Ejecución de Pruebas de Aceptación del Cliente
Ejecución de pruebas finales en presencia o bajo aprobación del cliente para formalizar la aceptación del producto, asegurando que todas las expectativas y requisitos del usuario final sean satisfechos.

### MA5.2 – Gestión de Defectos Pendientes
Revisión exhaustiva del estado de defectos encontrados durante todo el proceso, confirmando su resolución o estableciendo un plan de mitigación para aquellos que permanecen abiertos.

### RD5.1 – Revisión de Defectos No Solucionados
Análisis formal de defectos sin resolver, documentando el impacto, riesgos asociados y acordando compromisos con el cliente cuando sea necesario.

### TSR – Generación del Test Summary Report
Consolidación de resultados, cobertura alcanzada, defectos gestionados, métricas clave y observaciones finales del subproceso de pruebas en un documento ejecutivo.

## Productos de trabajo

### Entrada necesaria
- **Resultados de todas las pruebas ejecutadas** - Compilación completa de resultados de pruebas unitarias, integración, sistema, regresión, rendimiento y seguridad
- **Reportes de defectos y trazabilidad** - Historial completo de defectos encontrados y su seguimiento
- **Criterios de aceptación** - Especificaciones formales que debe cumplir el sistema
- **Documentos de validación y verificación** - Evidencia técnica de cumplimiento
- **Plan de Validación del Sistema** - Guía para la validación final

### Salida esperada
- **Resultados de Pruebas de Aceptación** - Documentación formal de la aceptación del cliente
- **Reporte de Verificación del Sistema en Condiciones Simuladas** - Evidencia de funcionamiento bajo condiciones espaciales simuladas
- **Reporte de Aceptación del Cliente** - Documento oficial de conformidad del cliente
- **Plan de Mitigación de Defectos** - Estrategia para manejar defectos no resueltos (si aplica)
- **Test Summary Report (TSR)** - Resumen ejecutivo completo del proceso de pruebas
- **Acta de Cierre del Subproceso de Pruebas** - Documento formal de finalización

### Productos de apoyo
Durante el cierre se generan productos internos como bitácora final de pruebas, checklist de criterios de aceptación, consolidado de métricas por tipo de prueba, cobertura alcanzada, severidad de defectos, y archivos de respaldo con logs y evidencias archivadas.

## Roles y responsabilidades

| Rol | Responsabilidad |
|-----|----------------|
| **Equipo de Pruebas** | Consolidar resultados, generar reportes finales y documentar evidencias |
| **Gerencia** | Validar cumplimiento contractual y supervisar la entrega final |
| **Desarrolladores** | Proporcionar soporte técnico para resolución de defectos finales |
| **Ingenieros de Misión** | Apoyar en validación técnica bajo condiciones simuladas |
| **Cliente/Usuario** | Revisar y aprobar la aceptación final del sistema |

.. figure:: _static/images/Guia_P5.png
   :alt: Diagrama de cierre de pruebas
   :width: 100%
   :align: center

   Figura 6. Diagrama que muestra las actividades, productos y roles clave que intervienen en el cierre del subproceso de pruebas.

## Herramientas recomendadas

### Generación de reportes
- **Allure, ExtentReports** - Para reportes automáticos y visualización de resultados
- **Jira Reports** - Para consolidación de métricas y seguimiento
- **Plantillas de cierre** - Documentos estructurados para formalización

### Gestión y archivo
- **Sistemas de firma digital** - Para aceptación formal y trazabilidad
- **Repositorios seguros** - Control de versiones y almacenamiento de evidencias
- **Checklists de conformidad** - Verificación sistemática de completitud

---


Análisis
========

# Análisis de Requisitos

El análisis de requisitos establece las bases del subproceso de pruebas mediante la evaluación sistemática de los requisitos del software, la arquitectura y el diseño del sistema. Esta fase permite derivar criterios de validación, identificar condiciones críticas y asegurar que los elementos aprobados sean entendidos, trazables y verificables desde el punto de vista de pruebas.

## Actividades principales

### DF2.1 – Análisis de Requisitos, Arquitectura y Diseño Aprobados
Revisión detallada de los requisitos validados, la arquitectura y los diseños aprobados para identificar funcionalidades clave, restricciones operativas, prioridades y riesgos desde la perspectiva del sistema CubeSat.

### VV2.3 – Definición de Criterios de Validación y Aceptación
Establecimiento de los criterios que deben cumplirse para considerar que un componente, módulo o sistema ha sido validado satisfactoriamente. Estos criterios deben estar alineados con los objetivos de misión, condiciones operacionales y expectativas del usuario final.

## Productos de trabajo

### Entrada necesaria
- **Requisitos de Software** [Verificado]
- **Diseño de Software** [Aprobado]  
- **Plan del Proyecto**
- **Enunciado del Trabajo** (si aplica)

### Salida esperada
- **Documento de Análisis de Requisitos de Pruebas** [Revisado] - Registro estructurado de hallazgos, dependencias funcionales, cobertura de pruebas esperada y observaciones técnicas derivadas del análisis
- **Plan de Validación del Sistema** [Revisado] - Documento que resume los criterios de aceptación, el enfoque de validación y las condiciones esperadas para ejecutar dicha validación

### Productos de apoyo
Durante la ejecución pueden generarse productos internos como plantillas de trazabilidad (requisitos ↔ módulos ↔ casos de prueba), checklists de validación de requisitos y notas técnicas internas que ayudan a formalizar el análisis.

## Roles y responsabilidades

| Rol | Responsabilidad |
|-----|----------------|
| **Equipo de Pruebas** | Analizar requisitos y elaborar criterios de validación |
| **Desarrolladores** | Aportar conocimiento técnico sobre diseño y arquitectura del sistema |
| **Líder Técnico** | Verificar consistencia entre análisis, diseño y especificaciones |
| **Cliente/Usuario** | Contribuir en la definición de criterios de aceptación finales |

## Diagrama de Análisis de Requisitos

.. figure:: _static/images/Guia_P1.png
   :alt: Diagrama general del subproceso de pruebas propuesto
   :width: 100%
   :align: center

   Figura 2. Diagrama que ilustra la secuencia lógica de actividades, productos de trabajo y actores involucrados en la fase de análisis de requisitos.

## Herramientas recomendadas

- **Gestión de requisitos** - ReqView, Polarion, IBM DOORS para proyectos formales; hojas de cálculo estructuradas para recursos limitados
- **Modelado visual** - UML, SysML para arquitectura y componentes  
- **Trazabilidad** - Matrices entre requisitos, diseño y pruebas
- **Validación** - Revisión técnica estructurada, checklists de validación, peer review
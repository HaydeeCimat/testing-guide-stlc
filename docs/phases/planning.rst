Planificación de Pruebas
===

# Planificación de Pruebas

La planificación de pruebas establece un plan estructurado que define el enfoque, los recursos, los responsables y los criterios necesarios para llevar a cabo las actividades de pruebas de manera efectiva. Este plan actúa como una guía de ejecución, coordinación y supervisión a lo largo de todo el subproceso de pruebas, adaptado a las necesidades de los sistemas CubeSat.

## Actividades principales

### PL1.1 – Establecimiento de Políticas y Estrategias de Pruebas
Definición del marco general bajo el cual se ejecutarán las pruebas, incluyendo criterios de cobertura, niveles de prueba, herramientas a utilizar y prioridades.

### PL1.2 – Identificación del entorno de prueba y recursos necesarios
Estimación y documentación de los recursos materiales, humanos y técnicos requeridos para las pruebas, considerando limitaciones comunes en entornos CubeSat.

### PL1.3 – Estimación del tiempo y costo requerido para pruebas
Cálculo preliminar de la duración de las actividades de prueba y los costos asociados.

### PL1.4 – Asignación de roles y responsabilidades al equipo de prueba
Definición y comunicación clara de las funciones de cada miembro del equipo de pruebas, incluyendo responsables de ejecución, análisis, documentación y validación.

### GP1.10 – Documentar la Estrategia de Control de Versiones
Incorporación al plan de los lineamientos para el versionado y manejo de los productos de prueba y sus configuraciones.

### PL1.5 – Revisión y aprobación del Plan de Pruebas
Validación del plan con todos los actores involucrados y obtención de la aceptación formal para proceder.

## Productos de trabajo

### Entrada necesaria
- **Requisitos de Prueba** [Verificado]
- **Documento de Análisis de Requisitos de Prueba**
- **Plan del Proyecto**
- **Enunciado del Trabajo** (si aplica)

### Salida esperada
- **Plan de Pruebas** [Aprobado] - Documento central que describe el alcance, estrategia, cronograma, recursos y criterios de éxito de las pruebas
- **Lista de Roles y Responsabilidades** [Revisado] - Documento auxiliar que define funciones y asignaciones dentro del equipo de pruebas
- **Política de Pruebas y Control de Versiones** [Documentada] - Anexo técnico del plan que establece las normas para el manejo, almacenamiento y liberación de productos de prueba

### Productos de apoyo
Durante la ejecución pueden generarse productos internos como estimaciones de esfuerzo y costo, cronograma de pruebas preliminar, matriz de asignación de tareas y hoja de ruta de herramientas requeridas.

## Roles y responsabilidades

| Rol | Responsabilidad |
|-----|----------------|
| **Equipo de Pruebas** | Analizar requisitos y elaborar el plan de pruebas |
| **Gerencia** | Aprobar el plan, analizar viabilidad y asignar recursos |
| **Líder Técnico** | Verificar consistencia entre análisis, diseño y especificaciones |
| **Cliente/Usuario** | Contribuir en la definición de criterios de aceptación finales |

## Diagrama de Planificación de Pruebas

.. figure:: _static/images/Guia_P2.png
   :alt: Diagrama de planificación de pruebas
   :width: 100%
   :align: center

   Figura 3. Diagrama que describe el flujo de actividades y productos de trabajo generados durante la fase de planificación de pruebas.

## Herramientas recomendadas

- **Plantillas de planes** - Plantillas estándar de planes de prueba
- **Gestión de pruebas** - TestRail, qTest, Xray, Zephyr para gestión formal
- **Estimación** - Técnicas como WBS, Three-point estimation, Function Point Analysis
- **Control de versiones** - Git, SVN o herramientas similares para manejo de configuraciones
- **Colaboración** - Hojas de cálculo estructuradas para equipos con recursos limitados
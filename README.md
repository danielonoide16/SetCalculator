# SetCalculator

Aplicación de escritorio en Python enfocada en lógica matemática y teoría de conjuntos, construida con interfaz gráfica en Tkinter.  
El proyecto integra dos módulos principales: una **calculadora de conjuntos** y un **analizador de relaciones/funciones aplicado a un caso de cifrado**.

---

## Resumen para reclutadores

Este proyecto demuestra capacidad para:

- Diseñar interfaces gráficas funcionales con Python.
- Modelar estructuras matemáticas (conjuntos, relaciones y funciones) en código.
- Implementar validaciones de entrada y manejo de errores orientado a usuario.
- Organizar lógica reutilizable en módulos (`sorted_set`, `relation`, `utils`).
- Traducir conceptos académicos (inyectividad, sobreyectividad, transitividad, etc.) a funcionalidades de software.

Es un proyecto útil para evaluar habilidades en **programación orientada a objetos**, **pensamiento lógico**, **desarrollo de producto educativo** y **experiencia de usuario básica**.

---

## Objetivo del proyecto

Crear una herramienta interactiva que permita:

1. Trabajar operaciones de teoría de conjuntos de forma visual.
2. Analizar propiedades de relaciones y funciones a partir de datos ingresados por el usuario.
3. Simular una interpretación de conexiones de cifrado entre emisores, llaves y receptores.

---

## Funcionalidades principales

### 1) Menú principal

- Navegación simple entre módulos:
  - **Calculadora de Conjuntos**
  - **Llaves de Cifrado**

### 2) Calculadora de conjuntos

- Creación de conjuntos:
  - Manual (elementos separados por coma).
  - Aleatoria de números.
  - Aleatoria de caracteres.
  - Aleatoria de cadenas.
- Operaciones binarias:
  - Unión (`A ∪ B`)
  - Intersección (`A ∩ B`)
  - Diferencia (`A - B`)
  - Diferencia simétrica (`A Δ B`)
  - Complemento (`A'`) con universo derivado de los conjuntos creados.
- Validaciones:
  - Subconjunto (`A ⊆ B`)
  - Subconjunto propio (`A ⊂ B`)
  - Disjuntos
  - Igualdad
- Operaciones múltiples:
  - Unión de varios conjuntos.
  - Intersección de varios conjuntos.
- Gestión:
  - Visualización de cardinalidad.
  - Eliminación de un conjunto.
  - Limpieza total.

### 3) Módulo “Llaves de Cifrado”

- Entrada de:
  - Emisores
  - Llaves
  - Receptores
  - Conexiones en formato de tuplas
- Validación de formato con expresiones regulares.
- Verificación de consistencia de conexiones contra los conjuntos definidos.
- Evaluación de propiedades:
  - **Como función:** función, inyectiva, sobreyectiva, biyectiva.
  - **Como relación:** reflexiva, simétrica, transitiva.
- Cálculo adicional de operaciones de conjuntos sobre emisores y receptores.

---

## Arquitectura y diseño técnico

### Estructura de archivos

- `main.py`: ventana principal y navegación entre módulos.
- `set_calculator.py`: lógica de UI y operaciones de la calculadora de conjuntos.
- `encryption.py`: UI y análisis de relaciones/funciones para el caso de cifrado.
- `sorted_set.py`: implementación de estructura `SortedSet` (sin duplicados y ordenada).
- `relation.py`: evaluación de propiedades matemáticas de relaciones y funciones.
- `utils.py`: validaciones de texto y conversión de formatos de entrada.

### Decisiones de implementación destacables

- **Modularidad:** separación de responsabilidades por dominio.
- **Modelo matemático explícito:** `SortedSet` y `Relation` encapsulan reglas de negocio.
- **Reutilización de lógica:** operaciones de conjuntos y validaciones centralizadas.
- **Enfoque UX básico:** mensajes de error/éxito y bloqueos de edición en resultados.

---

## Tecnologías

- **Lenguaje:** Python 3
- **GUI:** Tkinter
- **Librerías estándar:** `random`, `re`, `bisect`
- **Dependencias externas:** ninguna

---

## Cómo ejecutar

1. Clonar el repositorio.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

> Requiere Python 3 con Tkinter disponible en el entorno.

---

## Competencias técnicas evidenciadas

- Programación orientada a objetos.
- Modelado de estructuras abstractas.
- Lógica matemática aplicada.
- Validación y sanitización de entradas.
- Diseño de interfaces de escritorio.
- Separación de capas y organización modular.

---

## Posibles mejoras futuras

- Persistencia de conjuntos y sesiones en archivo o base de datos.
- Batería de pruebas unitarias para `SortedSet`, `Relation` y validadores.
- Exportación de resultados a CSV/PDF.
- Internacionalización (ES/EN).
- Mejoras visuales de UI (temas, accesibilidad y responsive desktop).

---

## Equipo

Proyecto desarrollado por:

- Daniel
- David
- Rahul


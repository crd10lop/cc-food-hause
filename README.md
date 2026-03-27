# C&C Food Hause - Backend MVP

Este proyecto es una API RESTful construida con **FastAPI** para la gestión del menú y procesamiento de pedidos de la marca "C&C Food Hause". 

##  Arquitectura y Buenas Prácticas
El proyecto fue diseñado bajo principios de **Clean Architecture** y **Patrón Repositorio** para garantizar:
- **Desacoplamiento:** La lógica de persistencia está separada de los controladores.
- **Tipado Estricto:** Validación de datos mediante Pydantic.
- **SQA (Software Quality Assurance):** Cobertura de pruebas unitarias con metodología **AAA**.

##  Tecnologías
- **Python 3.9+**
- **FastAPI** (Framework Web)
- **Pytest** (Testing)
- **Pydantic** (Validación de esquemas)

##  Instrucciones de Ejecución
1. Instalar dependencias: `pip install fastapi uvicorn pytest`
2. Correr el servidor: `uvicorn main:app --reload`
3. Documentación interactiva: `http://localhost:8000/docs`
4. Ejecutar pruebas: `pytest -v`
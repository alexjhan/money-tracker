# 🌟 Proyecto de Gestión de Gastos

Bienvenido al proyecto de **Gestión de Gastos**. Esta es una aplicación de consola interactiva que permite gestionar tus gastos personales o de cualquier índole de manera eficiente. Los datos se almacenan en un archivo JSON y las interacciones son dinámicas y fáciles de usar.

---

## ✨ Características

- **🔎 Listar gastos**: Visualiza todos los gastos guardados en formato tabular.
- **➕ Agregar gastos**: Añade nuevos gastos especificando la descripción, monto y categoría.
- **✏️ Modificar gastos**: Cambia detalles de los gastos existentes, como monto, descripción y categoría.
- **❌ Eliminar gastos**: Borra un gasto específico por su ID.
- **💾 Almacenamiento en JSON**: Los gastos se guardan de manera persistente en un archivo `gastos.json` para acceder a ellos en futuras sesiones.

---

## 📋 Requisitos

### ⚙️ Herramientas necesarias:
- **Python 3.7+**: Para ejecutar el programa. Puedes instalar Python desde [aquí](https://www.python.org/downloads/).
- **Rich**: Biblioteca de Python para crear interfaces interactivas en la terminal.

### Instalación de dependencias:
Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install rich
```

---

## 🚀 Instrucciones de uso

### 1. **Clonación del repositorio**:
Primero, clona el repositorio de GitHub a tu máquina local:

```bash
git clone https://github.com/tu_usuario/proyecto_gastos.git
cd proyecto_gastos
```

### 2. **Ejecutar el programa**:
Una vez que tengas el proyecto listo, abre la terminal y ejecuta el archivo principal:

```bash
python main.py
```

### 3. **Interacción con el programa**:
El programa te presentará un menú interactivo donde podrás elegir las siguientes opciones:

- Listar los gastos existentes.
- Agregar un nuevo gasto.
- Modificar un gasto existente.
- Eliminar un gasto.
- Salir del programa.

### 4. **Formato del archivo JSON**:
Los gastos se almacenan en un archivo JSON con el siguiente formato:

```json
{
  "gastos": [
    {
      "descripcion": "Comida",
      "monto": 20.5,
      "categoria": "Alimentación"
    },
    {
      "descripcion": "Transporte",
      "monto": 15.0,
      "categoria": "Transporte"
    }
  ]
}
```

Este archivo se actualizará automáticamente después de cada operación.

---

## 🛠️ Estructura del Proyecto

```plaintext
.
├── gastos.json               # Archivo donde se guardan los gastos
├── limpiezaDePantalla.py     # Funciones para limpiar la terminal
├── funciones/                
│   └── alistarGastos.py      # Funciones para listar y gestionar los gastos
├── main.py                   # Archivo principal del programa
└── README.md                 # Este archivo
```

---

## 🎨 Vista previa del programa

### **Interfaz de usuario interactiva**
El programa utiliza la biblioteca **Rich** para mostrar los gastos de manera visualmente atractiva en la terminal. A continuación, un ejemplo de cómo se ve el listado de gastos:

```
========================================
           GASTOS REGISTRADOS
========================================
ID | Descripción   | Monto | Categoría
----------------------------------------
 1 | Comida        | $20.5 | Alimentación
 2 | Transporte    | $15.0 | Transporte
========================================
```

Puedes interactuar con el programa para modificar, agregar o eliminar gastos de forma sencilla.

---

## 🤝 Contribuciones

Si deseas contribuir al proyecto, puedes seguir estos pasos:

1. **Haz un fork del repositorio**.
2. **Crea una nueva rama**: 
   ```bash
   git checkout -b mi-cambio
   ```
3. **Realiza tus cambios y confirma**: 
   ```bash
   git commit -am 'Añadí nueva funcionalidad'
   ```
4. **Sube tus cambios a tu fork**:
   ```bash
   git push origin mi-cambio
   ```
5. **Abre un Pull Request** para que tus cambios sean revisados y fusionados.

---

## 📑 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Si tienes alguna duda sobre el uso del código, por favor revisa la [Licencia MIT](https://opensource.org/licenses/MIT).

---

## 💡 Contacto

Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en abrir un **issue** o contactar directamente a través de:

- Correo electrónico: **tu_email@dominio.com**
- GitHub: [tu_usuario](https://github.com/tu_usuario)

---

### ¡Gracias por usar este proyecto! 🌍✨
```

### Explicación de las mejoras:
- **Íconos**: He incluido íconos relevantes de `✨`, `💡`, `📋` para hacerlo visualmente atractivo.
- **Colores y formato**: El uso de títulos con emojis y negritas hace que el contenido sea más fácil de leer y visualmente interesante.
- **Instrucciones detalladas**: Explico cómo clonar el repositorio, instalar las dependencias y ejecutar el programa, paso a paso.
- **Vista previa**: Proporcioné una pequeña "captura de pantalla" simulada de la interfaz del programa para mostrar cómo interactúa el usuario.
- **Contribuciones**: He añadido una sección de contribuciones para facilitar la participación de otros desarrolladores.
  
Este formato es atractivo y fácil de leer, lo que hace que tu proyecto se vea más profesional y accesible.
# Plaza Comercial Quetzal - Sitio Web

Este es el sitio web oficial de Plaza Comercial Quetzal, un innovador centro comercial y cultural ubicado en Teotihuacán de Arista, México.

## Características

- Diseño responsivo y moderno
- Información detallada sobre servicios y actividades
- Formulario de contacto
- Galería de imágenes
- Información sobre eventos y talleres

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## Instalación

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd plaza-quetzal
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
plaza-quetzal/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias del proyecto
├── static/            # Archivos estáticos
│   ├── css/          # Hojas de estilo
│   ├── js/           # Scripts JavaScript
│   └── images/       # Imágenes del sitio
└── templates/         # Plantillas HTML
    ├── base.html     # Plantilla base
    ├── index.html    # Página principal
    ├── about.html    # Sobre nosotros
    ├── services.html # Servicios
    ├── contact.html  # Contacto
    ├── coworking.html # Espacios de coworking
    ├── gastronomia.html # Zona gastronómica
    └── artesanias.html  # Mercado de artesanías
```

## Ejecución

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecutar la aplicación:
```bash
python app.py
```

3. Abrir el navegador y visitar:
```
http://localhost:5000
```

## Desarrollo

Para contribuir al desarrollo del sitio:

1. Crear una rama para tu característica:
```bash
git checkout -b feature/nueva-caracteristica
```

2. Hacer los cambios necesarios y confirmarlos:
```bash
git add .
git commit -m "Descripción de los cambios"
```

3. Subir los cambios:
```bash
git push origin feature/nueva-caracteristica
```

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier consulta o sugerencia, por favor contactar a:
- Email: info@plazaquetzal.com
- Teléfono: +52 55 1234 5678 # plaza-quetzal

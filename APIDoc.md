# ❓ Documentación Q-AUNAL API

## v.0.0.1

Para la primera entrega el API maneja multiples endpoints clasificados en dos grupos principales:

- Preguntas
- Comentarios

## 1️⃣ Preguntas

### 1.1. Preguntas

> **[GET]** Renderiza todas las preguntas junto con los comentarios en formato JSON
>
> ```
> /preguntas
> ```

### 1.2. Pregunta por ID

> **[GET]** Recibe por parametro un identificador de pregunta y renderiza todas la pregunta solicitada >junto con los comentarios en formato JSON. Si no se encuentra la pregunta se envia entrega a cambio un >response de no encontrado.

```
/preguntas/<int:preg_id>
```

### 1.3. Crear una nueva pregunta

> **[POST]** Recibe a través de POST un diccionario con los datos a añadir de la pregunta.
> **Nota**: Por ahora permite el ingreso de IDs propios, cuando se incorpore una base de datos el ID es automático

```
/preguntas/nueva
```

### 1.4. Actualizar los datos de una pregunta ya existente

> **[PUT]** Actualiza los datos de una pregunta con un identificador pasado por parametro.

```
dict {
    titulo: str
    contenido: str
}
```

### 1.5 Elimina una pregunta

> **[DELETE]** Elimina la pregunta con identificador dado.

```
/preguntas/actualizar/<int:preg_id>
```

## 2️⃣ Respuestas

### 2.1. Comentarios

> **[GET]** Renderiza todos los comentarios de todas las preguntas.
>
> ```
> /comentarios
> ```

### 2.2. Comentario por ID

> **[GET]** Recibe por parametro un identificador de comentario y renderiza el comentario solicitado > en formato JSON. Si no se encuentra se envia entrega a cambio un response de no encontrado.

```
/comentarios/<int:com_id>
```

### 1.3. Crear un nuevo comentario

> **[POST]** Recibe a través de POST un identificador de pregunta con los datos a añadir del comentario

```
/comentarios/nuevo/<int:preg_id>
```

```
dict = {
    texto: str
}
```

### 1.4. Actualizar el texto de un comentario

> **[PUT]** Actualiza los datos de un comentario en una pregunta con identificadores pasados por parametro.

```
/comentarios/actualizar/<int:preg_id>/<int:com_id>
```

```
dict {
    titulo: str
    contenido: str
}
```

### 1.5 Elimina un comentario

> **[DELETE]** Elimina el comentario con identificador dado.

```
/comentarios/actualizar/<int:preg_id>/<int:com_id>
```

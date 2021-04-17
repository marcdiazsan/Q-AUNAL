import requests

# Clase de fetcher


class Fetcher():
    def __init__(self, base_url):
        self.url = base_url

    def getPreguntas(self):
        req_url = self.url + '/preguntas'
        return requests.get(req_url)

    def getPregunta(self, preg_id):
        req_url = self.url + f'/preguntas/{preg_id}'
        return requests.get(req_url)

    def nuevaPregunta(self, datos):
        req_url = self.url + '/preguntas/nueva'
        return requests.post(req_url, json=datos)

    def actualizarPregunta(self, preg_id, datos):
        req_url = self.url + f'/preguntas/actualizar/{preg_id}'
        return requests.put(req_url, json=datos)

    def borrarPregunta(self, preg_id):
        req_url = self.url + f'/preguntas/actualizar/{preg_id}'
        return requests.delete(req_url)

    # METODOS PARA COMENTARIOS
    def getComentarios(self):
        req_url = self.url + '/comentarios'
        return requests.get(req_url)

    def getComentario(self, com_id):
        req_url = self.url + f'/comentarios/{com_id}'
        return requests.get(req_url)

    def nuevoComentario(self, datos):
        req_url = self.url + 'comentarios/nuevo'
        return requests.post(req_url, json=datos)

    def actualizarComentario(self, preg_id, com_id, datos):
        req_url = self.url + f'/comentarios/actualizar/{preg_id}/{com_id}'
        return requests.put(req_url, json=datos)

    def borrarComentario(self, preg_id, com_id):
        req_url = self.url + f'/comentarios/actualizar/{preg_id}/{com_id}'
        return requests.delete(req_url)


user = True
menu = """Bienvenido a Q&A UNAL.\n¿Qué desea hacer?\n1. Ver todas las preguntas\n2. Ver una pregunta por su ID\n3. Añadir una nueva pregunta.\n4. Actualizar una pregunta\n5. Eliminar una pregunta\n6. Ver todos los comentarios\n7. Ver un comentario por su ID\n8. Añadir una nueva pregunta.\n9. Actualizar un comentario\n10. Eliminar un comentario\n11. Salir"""
fetcher = Fetcher('http://localhost:5000/')
while user:
    print(menu)
    choice = int(input())
    while 1 > choice > 11:
        choice = input("Opcion Invalida. Intentelo de nuevo")
    if choice == 1:
        res = fetcher.getPreguntas()
        print(res.text)
    elif choice == 2:
        preg_id = int(input("Por favor ingresa el id de la pregunta"))
        res = fetcher.getPregunta(preg_id)
        print(res.text)

    elif choice == 3:
        titulo = input("Ingresa el título de tu pregunta")
        texto = input("Ingresa el texto de tu pregunta")
        tema = input("Ingresa el tema de tu pregunta (Facultad)")
        userid = int(input(
            "Ingresa tu id de usuario. (En el futuro no tendrás que hacer esto, nosotros lo verificaremos por ti"))
        datos = {
            "titulo": titulo,
            "texto": texto,
            "tema": tema,
            "userid": userid
        }

        res = fetcher.nuevaPregunta(datos)
        print(res.text)

    elif choice == 4:
        idp = int(input("Ingresa el ID de la pregunta a actualizar "))
        titulo = input("Ingresa el título de tu pregunta ")
        texto = input("Ingresa el texto de tu pregunta ")
        tema = input("Ingresa el tema de tu pregunta (Facultad) ")
        likes = input("¿Añadir likes? S/N ")

        while likes != "N":
            if likes != 'S':
                likes = input("¿Añadir likes? S/N ")
            else:
                pass

        datos = {
            "titulo": titulo,
            "texto": texto,
            "tema": tema,
            "likes": likes
        }
        res = fetcher.actualizarPregunta(preg_id=idp, datos=datos)
        print(res.text)

    elif choice == 5:
        idp = int(input("Ingresa el ID de la pregunta a eliminar"))
        res = fetcher.borrarPregunta(preg_id=idp)
        print(res.text)

    elif choice == 6:
        res = fetcher.getComentarios()
        print(res.text)

    elif choice == 7:
        com_id = int(input("Por favor ingresa el id del comentario"))
        res = fetcher.getComentario(com_id=com_id)
        print(res.text)

    elif choice == 8:
        texto = input("Ingresa el texto de tu pregunta")
        userid = input(
            "Ingresa tu id de usuario. (En el futuro no tendrás que hacer esto, nosotros lo verificaremos por ti")

        datos = {
            "texto": texto,
            "userid": int(userid)
        }
        res = fetcher.nuevoComentario(datos=datos)
        print(res.text)

    elif choice == 9:
        idp = int(input("Ingresa el ID de la pregunta"))
        idc = int(input("Ingresa el ID del comentario"))
        texto = input("Ingresa el texto de tu pregunta")
        datos = {
            "texto": texto
        }
        res = fetcher.actualizarComentario(
            preg_id=idp, com_id=idc, datos=datos)
        print(res.text)

    elif choice == 10:
        idp = int(input("Ingresa el ID de la pregunta"))
        idc = int(input("Ingresa el ID del comentario"))
        res = fetcher.borrarComentario(preg_id=idp, com_id=idc)
        print(res.text)

    else:
        user = False
        print("Adios!")

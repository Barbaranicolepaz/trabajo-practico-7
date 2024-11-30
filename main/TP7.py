"""1"""
# class Rectangulo:  
#     def __init__(self, base, altura):    
#         self.base = base  
#         self.altura = altura  

#     def area(self):   
#         return self.base * self.altura  

# rect = Rectangulo(5, 3)  
    
# print("El área del rectángulo es:", rect.area())

"""2"""
# class Mate:  
#     def __init__(self, max_cebadas): 
#         self.cebadas_restantes = max_cebadas  
#         self.estado = "vacío" 
#         self.max_cebadas = max_cebadas  

#     def cebar(self):    
#         if self.estado == "lleno":  
#             print("¡Cuidado! ¡Te quemaste!")  
#         else:  
#             self.estado = "lleno"  
#             print("Mate cebado.")  

#     def beber(self):  
#         if self.estado == "vacío":  
#             if self.cebadas_restantes > 0:  
#                 self.cebadas_restantes -= 1  
#                 print("¡El mate está vacío!")  
#             else:  
#                 print("Advertencia: el mate está lavado.")  
#         else:  
#             self.estado = "vacío"  
#             if self.cebadas_restantes > 0:  
#                 self.cebadas_restantes -= 1  
#             print("Has bebido del mate.")  

# mi_mate = Mate(3)  
# mi_mate.cebar() 
# mi_mate.beber()  
# mi_mate.beber() 
# mi_mate.cebar()  
# mi_mate.cebar()  
# mi_mate.beber()   
# mi_mate.beber()    

"""3"""
# class Corcho:  
#     def __init__(self, bodega):  
#         self.bodega = bodega  

#     def __str__(self):  
#         return (f"Corcho de la bodega: {self.bodega}")  


# class Botella:  
#     def __init__(self, corcho=None):  
#         self.corcho = corcho  

#     def destapada(self):  
#         return self.corcho is None  

#     def __str__(self):  
#         estado = 'destapada' if self.destapada() else f'de corcho: {self.corcho}'  
#         return (f"Botella {estado}")  


# class Sacacorchos:  
#     def __init__(self):  
#         self.corcho = None  

#     def destapar(self, botella):  
#         if botella.destapada():  
#             raise Exception("La botella ya está destapada.")  
#         if self.corcho is not None:  
#             raise Exception("El sacacorchos ya contiene un corcho.")  
        
#         self.corcho = botella.corcho  
#         botella.corcho = None  

#     def limpiar(self):  
#         if self.corcho is None:  
#             raise Exception("No hay un corcho en el sacacorchos para limpiar.")  
#         self.corcho = None   

#     def __str__(self):  
#         return f'Sacacorchos con corcho: {self.corcho}' if self.corcho else 'Sacacorchos vacío'  


# corcho_vino = Corcho("Bodega del Vino")  
# botella = Botella(corcho_vino)  
    
# print(botella)    
    
# sacacorchos = Sacacorchos()  
    
# sacacorchos.destapar(botella)  
    
# print(botella)    
# print(sacacorchos)  
# sacacorchos.limpiar()  
    
# print(sacacorchos)  

"""4"""
# class Restaurante:  
#     def __init__(self, restaurante_nombre, tipo_comida):  
#         self.restaurante_nombre = restaurante_nombre  
#         self.tipo_comida = tipo_comida  

#     def describir_restaurante(self):  
#         print(f"Nombre del restaurante: {self.restaurante_nombre}, Tipo de comida: {self.tipo_comida}")  

#     def abrir_restaurante(self):  
#         print(f"{self.restaurante_nombre} ahora está abierto.")  

# class Heladeria(Restaurante):  
#     def __init__(self, restaurante_nombre, sabores):  
#         super().__init__(restaurante_nombre, "Helados")  
#         self.sabores = sabores  

#     def mostrar_sabores(self):  
#         print("Sabores disponibles:")  
#         for sabor in self.sabores:  
#             print(f"- {sabor}")  

# mi_heladeria = Heladeria("Helados Crispis", ["Chocolate con almendras", "dulce de leche", "marroc"])  
# mi_heladeria.describir_restaurante()  
# mi_heladeria.abrir_restaurante()  
# mi_heladeria.mostrar_sabores()  

"""5"""
# class Personaje:  
#     def __init__(self, vida, posicion, velocidad):  
#         self.vida = vida                     
#         self.posicion = posicion             
#         self.velocidad = velocidad         

#     def recibir_ataque(self, cantidad):    
#         self.vida -= cantidad  
#         if self.vida <= 0:
#             Exception(f"El personaje ha caído. Vida restante: {self.vida}")  

#     def mover(self, direccion):  
#         if direccion == 'arriba':  
#             self.posicion[1] += self.velocidad  
#         elif direccion == 'abajo':  
#             self.posicion[1] -= self.velocidad  
#         elif direccion == 'izquierda':  
#             self.posicion[0] -= self.velocidad  
#         elif direccion == 'derecha':  
#             self.posicion[0] += self.velocidad  
#         else:  
#             print("Dirección no válida.")  


# class Soldado(Personaje):  
#     def __init__(self, vida, posicion, velocidad, ataque):  
#         super().__init__(vida, posicion, velocidad)  
#         self.ataque = ataque               

#     def atacar(self, otro_personaje):  
#         print(f"El soldado ataca causando {self.ataque} de daño.")  
#         otro_personaje.recibir_ataque(self.ataque)  


# class Campesino(Personaje):  
#     def __init__(self, vida, posicion, velocidad, cosecha):  
#         super().__init__(vida, posicion, velocidad)  
#         self.cosecha = cosecha              

#     def cosechar(self):  
#         print(f"El campesino ha cosechado {self.cosecha} unidades.")  
#         return self.cosecha  
  
# soldado = Soldado(100, [0, 0], 5, 20)  
# campesino = Campesino(50, [2, 3], 3, 10)  
 
# print(f"Vida del soldado: {soldado.vida}, Posición: {soldado.posicion}")  
# print(f"Vida del campesino: {campesino.vida}, Posición: {campesino.posicion}")  

# soldado.atacar(campesino)  
  
# print(f"Vida del campesino después del ataque: {campesino.vida}")  
  
# cosecha = campesino.cosechar()  
     
# soldado.mover('derecha')  
# print(f"Nueva posición del soldado: {soldado.posicion}")  

# campesino.recibir_ataque(30)  
# print(f"Vida del campesino después de recibir daño: {campesino.vida}")  
 
# campesino.recibir_ataque(20)  

"""6"""
# class Usuario:  
#     def __init__(self, nombre, apellido, edad, correo, telefono):    
#         self.nombre = nombre               
#         self.apellido = apellido             
#         self.edad = edad                      
#         self.correo = correo               
#         self.telefono = telefono            

#     def describir_usuario(self):  
        
#         resumen =(f"Resumen del usuario: "  
#             f" Nombre: {self.nombre} {self.apellido} "  
#             f" Edad: {self.edad} "  
#             f" Correo: {self.correo} "  
#             f" Teléfono: {self.telefono} ")  
#         print(resumen)  

#     def saludar_usuario(self):  
#         saludo = f"¡Hola, {self.nombre} {self.apellido}! Bienvenido."  
#         print(saludo)  

# usuario1 = Usuario("Barbara", "Palavecino", 23, "barbarapalavecino@gmail.com", "387-524161")  
# usuario2 = Usuario("Nicole", "Paz", 25, "nicolepaz15@gmail.com", "387-638742")  
# usuario3 = Usuario("Gonzalo", "Cortez", 26, "gonzacortez@gmail.com", "387-2221564")  

# for usuario in [usuario1, usuario2, usuario3]:  
#         usuario.describir_usuario()  
#         usuario.saludar_usuario()  
       
"""7"""
# class Usuario:  
#     def __init__(self, nombre, apellido, edad, correo, telefono):   
#         self.nombre = nombre                
#         self.apellido = apellido            
#         self.edad = edad                    
#         self.correo = correo               
#         self.telefono = telefono            

#     def describir_usuario(self):  
#         resumen = (f"Resumen del usuario: "  
#             f" Nombre: {self.nombre} {self.apellido} "  
#             f" Edad: {self.edad} "  
#             f" Correo: {self.correo} "  
#             f" Teléfono: {self.telefono} ")  
#         print(resumen)  

#     def saludar_usuario(self):  
#         saludo = f"¡Hola, {self.nombre} {self.apellido}! Bienvenido."  
#         print(saludo)  

# class Admin(Usuario):  
#     def __init__(self, nombre, apellido, edad, correo, telefono):   
#         super().__init__(nombre, apellido, edad, correo, telefono)  
#         self.privilegios = ["puede postear en el foro",  
#             "puede borrar un post",  
#             "puede banear usuarios",  
#             "puede modificar configuraciones",  
#             "puede acceder a estadísticas del sitio"]  

#     def mostrar_privilegios(self):  
#         print(f"Privilegios de {self.nombre} {self.apellido}:")  
#         for privilegio in self.privilegios:  
#             print(f"- {privilegio}")  


# administrador = Admin("Barbii", "Paz", 23, "Barbii.paz@gmail.com", "387-569876")  
# administrador.describir_usuario()  
# administrador.saludar_usuario()  
# administrador.mostrar_privilegios()


"""8"""
# class Usuario:  
#     def __init__(self, nombre, apellido, edad, correo, telefono):  
#         self.nombre = nombre                
#         self.apellido = apellido            
#         self.edad = edad                   
#         self.correo = correo                
#         self.telefono = telefono         

#     def describir_usuario(self):  
#         resumen = (f"Resumen del usuario:"  
#             f"Nombre: {self.nombre} {self.apellido} "  
#             f"Edad: {self.edad} "  
#             f"Correo: {self.correo} "  
#             f"Teléfono: {self.telefono} ")  
#         print(resumen)  

#     def saludar_usuario(self):  
#         saludo = f"¡Hola, {self.nombre} {self.apellido}! Bienvenido."  
#         print(saludo)  


# class Privilegios:  
#     def __init__(self):  
#         self.privilegios = ["puede postear en el foro",  
#             "puede borrar un post",  
#             "puede banear usuarios",  
#             "puede modificar configuraciones",  
#             "puede acceder a estadísticas del sitio"]  

#     def mostrar_privilegios(self): 
#         print("Privilegios del administrador:")  
#         for privilegio in self.privilegios:  
#             print(f"- {privilegio}")  


# class Admin(Usuario):  
#     def __init__(self, nombre, apellido, edad, correo, telefono):   
#         super().__init__(nombre, apellido, edad, correo, telefono)  
#         self.privilegios = Privilegios()  

# administrador = Admin("Barbii", "Paz", 23, "Barbii.paz@gmail.com", "387-569876")  
# administrador.describir_usuario()  
# administrador.saludar_usuario()  
# administrador.privilegios.mostrar_privilegios()

"""9"""
# from restaurante import Restaurante  
# class Heladeria(Restaurante):  
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):    
#         super().__init__(restaurante_nombre, tipo_comida)  
#         self.sabores = sabores  

#     def mostrar_sabores(self):  
#         print(f"Sabores disponibles en {self.restaurante_nombre}:")  
#         for sabor in self.sabores:  
#             print(f"- {sabor}")  

# heladeria = Heladeria("Helados Chispitas", "Helados", ["vainilla", "chocolate", "frutilla", "dulce de leche"])  
# heladeria.describir_restaurante()  
# heladeria.abrir_restaurante()  
# heladeria.mostrar_sabores()










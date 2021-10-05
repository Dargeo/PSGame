from colored import fg,bg,attr
from  time import sleep
import sys,pygame,os

class Game():

    def __init__(self):
        self.puntos = 0
        self.vidas = 3
    
    def historia(self):
        pygame.mixer.init()
        os.system("cls" if os.name == "nt" else "clear")
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.01)
        c ='Te encuentras a la deriva en una isla luego de luchar contra tu archienemigo,%s EL MEGA ARQUETIPO !!! %s\n' % (fg(1), attr(0))
        for char in c:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(1)
        c = "Luego de revisar a tus alrededores encuentras varias notas con informacion de los arquetipos... \n"
        
        self.tecleo(c)
        a = 0
        a2 = True
        a3 = True
        while a != '1':
            c = ("Escoge que quieres hacer\n"
                    +
                    "%s1)%sVer la informacion\n" % (fg(2), attr(0))
                    +
                    "%s2)%sComerte un coco\n" % (fg(2), attr(0))
                    +
                    "%s3)%sLlorar por el semestre\n") % (fg(2), attr(0))
            self.tecleo(c)
            a = input()
            if a =='1':break
            elif a =='2':
                if a2:
                    c ="%sDisfrutas de un delicioso coco%s. Luego recuerdas que debes salir de la isla a toda costa\n" % (fg(21), attr(0))
                    a2 = False
                    
                else:
                    c ="%sYa no hay mas cocos%s. Hora de aprender!\n" % (fg(1), attr(0))
                    
            elif a == '3' and a3:
                a3 = False
                c ='Luego de llorar por horas %sSIN PARAR%s , recuerdas que tienes una pola en tu bolsillo. Te la embuches y estas listo para la aventura\n' % (fg(1), attr(0))
                
            elif a == '3' and not a3:
                c ='No es momento de lamentos, %sa estudiar%s\n' % (fg(21), attr(0))
               
            else:
                c = "Te confundiste porque pensabas hacer algo que %sno%s podias, piensa en algo que puedas hacer.\n" % (fg(1), attr(0))
                
            self.tecleo(c)
            sleep(1)
        self.informacion()

    def start(self):
        print("Bienvenido")
        self.historia()

    def informacion(self):
        
        c = ("Encuentras tres notas importantes. Sientes que debes de %smemorizar%s todo muy bien... \n")% (fg(1), attr(0))
        
        self.tecleo(c)
        sleep(1)
        self.tecleo(self.informaciones())
        sleep(6)
        c = ("Luego de guardar las notas, decides tomar valor y seguir adelante...\n\n")
        sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        self.historia2()

    def historia2(self):
        c = ("Ya has caminado mucho kilometros en busca de vida. Escuchas %sruidos%s...\n\n"% (fg(164), attr(0))
        + 
        "A medida que te acercas, escuchas cada vez más fuerte. %s\"Creíamos que estábamos en equilibrio, pero luego tomamos una medida excesiva\"%s.\n"% (fg(1), attr(0))
        )
        self.tecleo(c)
        sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        c = ("%sCREIAMOS QUE ESTABAMOS EN EQUILIBRIO, PERO LUEGO TOMAMOS UNA MEDIDA EXCESIVA%s\n\n\n")% (fg(1), attr(0))
        self.tecleo(c)
        sleep(3)
        c =("Ves un arquetipo gigante detras tuyo y sales corriendo mientras piensas que hacer... \n \n")
        self.tecleo(c)
        sleep(1)
        a = 0
        while a != 1:
            self.tecleo(self.ataque1())
            a = input()
            if a == '1':
                break
            elif a == '2':
                self.vidas = self.vidas-1
                c = ("Tratas de perforar la dura coraza del arquetipo con la espada..."+
                "Pero ese arquetipo es inmune. Te falta conocimiento, si fuera un %sArquetipo de Limites de crecimiento %s hubiera sido un ataque efectivo\n" % (fg(21), attr(0)))
                self.tecleo(c)
                sleep(1)
            elif a=='3':
                self.vidas = self.vidas-1
                c = ("Tratas de correr del arquetipo por tu vida..."+
                "Pero ese arquetipo es mas rapido. Te falta conocimiento, si fuera un %sArquetipo de desplazamiento de carga %s hubiera sido una estrategia efectiva\n" % (fg(21), attr(0)))
                self.tecleo(c)
                sleep(1)
            elif a == '4':
                c = self.informaciones()
                self.tecleo(c)
                sleep(6)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                c = ("Te pierdes en tus pensamientos y no recuerdas que ibas a hacer. Escoge una opcion %svalida%s\n" % (fg(21), attr(0)))
                self.tecleo(c)
            
        self.tecleo("Le gritas con todas tus fuerzas. El arquetipo se pone a llorar y sale corriendo abriendote espacio, puedes continuar %s(Revisando tus notas, te das cuenta que era un arquetipo de compensacion entre proceso y demora)%s\n" % (fg(21), attr(0)))
        sleep(1)
        self.tecleo("En el camino te encuentras con unas notas utiles para tu travesia... \n")
        sleep(1)
        self.tecleo(self.informaciones2())
        sleep(6)
        self.tecleo("Llegas a una zona al lado de un rio y te percatas de una manada de arquetipos que intentan pasar. Tu %stambien%s necesitas pasar el rio... \n" % (fg(164), attr(0)))
        sleep(1)
        a = 0
        while a != 1:
            self.tecleo(self.ataque2())
            a = input()
            if a == '3':
                break
            elif a == '1':
                self.vidas = self.vidas-1
                c = ("Bailas como nunca has bailado en tu vida..."+
                "Pero los arquetipos ni se inmutan, solo hiciste una burla de ti. Te falta conocimiento, si fuera un %sArquetipo de desplazamiento de la carga hacia la intervención %s hubiera sido un ataque efectivo\n" % (fg(21), attr(0)))
                self.tecleo(c)
                sleep(1)
            elif a=='2':
                self.vidas = self.vidas-1
                c = ("Te quedas mirando a la manada fijamente..."+
                "Pero nunca pasa nada y te quedas de por vida mirandoles. Te falta conocimiento, si fuera un %sArquetipo de erosión de metas %s hubiera sido una estrategia efectiva\n" % (fg(21), attr(0)))
                self.tecleo(c)
                sleep(1)
            elif a=='4':
                self.vidas = self.vidas-1
                c = ("Tratas de demostrar que eres mas que una manada gritando..."+
                "Pero solo se alteran y te pisotean entre todos. Te falta conocimiento, si fuera un %sArquetipo de exito para quien tiene éxito %s hubiera sido una estrategia efectiva\n" % (fg(21), attr(0)))
                self.tecleo(c)
                sleep(1)
            elif a == '5':
                c = self.informaciones2()
                self.tecleo(c)
                sleep(6)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                c = ("Te pierdes en tus pensamientos y no recuerdas que ibas a hacer. Escoge una opcion %svalida%s\n" % (fg(21), attr(0)))
                self.tecleo(c)
        self.tecleo("Buscas como ayudar a los arquetipos y luego de tumbar un arbol, logran pasar ambos. %s( Buscando en tus notas te das cuenta que era un arquetipo de escalada)%s. Continuas a la parte final de tu viaje\n"  % (fg(21), attr(0)))
        sleep(6)
        self.tecleo("Llegas al final de tu aventura...\n"
        +
        "Te encuentras a tu archienemigo...\n"
        +
        "Tras horas y horas de batalla intensa, recuerdas aquello que te dijo tu abuelo. Un hechizo para derrotarlo de una vez por todas...\n"
        +
        "Con todas tus fuerzas y esperanzas, gritas \n %s\"Bien, éramos los mejores, y lo seremos de nuevo, pero ahora tenemos que conservar los recursos y no invertir en exceso.\"%s \n" % (fg(164), attr(0))
        +
        "Tu archienemigo se ve debil. Aprovechas la oportunidad para darle el golpe final...\n"
        +"En tus oidos retumba %sSE MERECEN UN 5 POR ESTA EXPOSICION%s\n"% (fg(11), attr(0)))
        sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        self.tecleo("Lo has logrado!! Venciste a el %sArquetipo de crecimiento y subinversion%s y aprendiste de los arquetipos mientras tanto." % (fg(11), attr(0)))
        sleep(10)
    
    def informaciones(self):
        return (("%sArquetipo 1: Compensacion entre proceso y demora %s \n"% (fg(21), attr(0))
        +
        "La demora puede provocar el colapso del sistema, siendo una empresa que gira en torno a la maquinaria de producción.\n"
        +
        "%sDebilidades:%s Ataque psicologico \n\n"% (fg(2), attr(0))+

        "%sArquetipo 2: Limites de crecimiento %s \n"% (fg(21), attr(0))
        +
        "Los procesos son necesarios para si mismos, para de ellos producir algo mas elevado.Luego el crecimiento se vuelve más lento y puede detenerse o se revierte e inicia un colapso acelerado\n"
        
        +"%sDebilidades:%s Ataque a distancia \n\n"% (fg(2), attr(0))
        +
        "%sArquetipo 3: Desplazamiento de la carga %s \n"% (fg(21), attr(0))
        +
        "Cuando se usa una solución de corto plazo se usa cada vez más, sus efectos funcionan cada vez menos.\n"
        +"%sDebilidades:%s Ataque cuerpo a cuerpo \n\n"% (fg(2), attr(0))
        ))

    def informaciones2(self):
        return (("%sArquetipo 4: Desplazamiento de la carga hacia la intervención %s \n"% (fg(21), attr(0))
        +
        "Cuando una intervención externa soluciona el problema y los integrantes del sistema solo aprenden esta solución pero no a afrontar los problemas.\n"
        +
        "%sDebilidades:%s Ataque bailarin \n\n"% (fg(2), attr(0))+

        "%sArquetipo 5: Erosión de metas %s \n"% (fg(21), attr(0))
        +
        "Una estructura de desplazamiento de la carga donde la solución de corto plazo significa el deterioro de una meta fundamental de largo plazo.\n"
        
        +"%sDebilidades:%s Ataque de ternura \n\n"% (fg(2), attr(0))
        +
        "%sArquetipo 6: Escalada %s \n"% (fg(21), attr(0))
        +
        "Dos personas u organizaciones creen que su bienestar depende de tener ventaja sobre la otra. Así que concentran sus esfuerzos más en \"Combatir\" con la otra, que en crecerse a su misma.\n"
        +"%sDebilidades:%s Solo ignorar \n\n"% (fg(2), attr(0))
        +
        "%sArquetipo 7: Éxito para quien tiene éxito %s \n"% (fg(21), attr(0))
        +
        "Dos entidades compiten por recursos limitados. A mayor éxito, mayor respaldo, con lo cual la otra se queda sin recursos.\n"
        +"%sDebilidades:%s Demostrar superioridad \n\n"% (fg(2), attr(0))
        ))

    def ataque1(self):
        return ("Escoge que quieres hacer\n"
                    +
                    "%s1)%sGritarle: Eres un arquetipo muy feo, nadie te quiere.\n" % (fg(2), attr(0))
                    +
                    "%s2)%sUsar un arma enmarcada con: \"No presiones el proceso reforzador (de crecimiento)\" \n" % (fg(2), attr(0))
                    +
                    "%s3)%sSal corriendo y concéntrate en la solución fundamental.\n" % (fg(2), attr(0)) 
                    +
                    "%s4)%sRevisa tus notas\n" % (fg(2), attr(0)) 
                    ) 
    def ataque2(self):
        return ("Escoge que quieres hacer\n"
                    +
                    "%s1)%sBaila creyendote el ayuwoki.\n" % (fg(2), attr(0))
                    +
                    "%s2)%sSostén la visión contra la manada de arquetipos a ver si se alejan.\" \n" % (fg(2), attr(0))
                    +
                    "%s3)%sBusca el modo de que ambas partes \"ganen\" o alcancen sus objetivos.\n" % (fg(2), attr(0)) 
                    
                    +
                    "%s4)%sDemuestra que tu todo pequeño eres mas que una manada entera.\n" % (fg(2), attr(0)) 
                    +
                    "%s5)%sRevisa tus notas.\n" % (fg(2), attr(0)) 
                    ) 
    def tecleo(self, c ):
        for char in c:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
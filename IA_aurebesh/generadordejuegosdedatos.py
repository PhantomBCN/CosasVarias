'''
    Traductor de castellano a aurebesh y viceversa.
    Autor (GitHub) : PhantomBCN
    Versión: 1.0
    Fecha: 12 de abril de 2023
'''

import csv
from unidecode import unidecode

datos_iniciales = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "fe", "me", "sol", "mar", "ti", "fez", "paz", "pie", "voz", "ley", "flor", "dios", 
                   "pan", "sal", "rey", "río", "luz", "fiel", "miel", "tren", "ola", "oro", "ojo", "cielo", "hielo", "vino", "lago", 
                   "ruta", "cama", "bar", "luna", "gato", "huevo", "fuego", "juez", "casa", "taza", "paz", "caja", "barco", "perro", "agua", 
                   "llave", "zapato", "foto", "mapa", "hilo", "techo", "mesa", "cine", "tigre", "niño", "mano", "algo", "mesa", 
                   "mal", "feo", "lobo", "tos", "cola", "piso", "nube", "paja", "cero", "alma", "bote", "bondad", "buda", "caro", 
                   "caña", "coco", "cura", "dar", "darlo", "deuda", "doce", "duelo", "duro", "eco", "ego", "emoción", "enero", 
                   "entrada", "error", "este", "euro", "exceso", "extra", "falta", "fama", "faro", "fase", "fino", "fue", "gema", 
                   "genero", "genio", "gitano", "goma", "gorro", "gusto", "hacha", "halcón", "helado", "heroico", "hoy", "humano", 
                   "humo", "huevo", "iba", "iglesia", "imán", "índice", "infierno", "inútil", "irán", "jardín", "jamón", "jazmín", 
                   "joven", "juego", "kilo", "koala", "lazo", "leal", "legal", "león", "letra", "libro", "lima", "lindo", "lista", 
                   "loco", "loro", "lujo", "lunar", "luto", "madre", "magia", "mapa", "marco", "media", "medio", "mesa", "metro", 
                   "miércoles", "mil", "milagro", "minuto", "mitad", "modo", "moho", "mono", "moro", "moto", "mucho", "mudar", 
                   "mujer", "mundo", "música", "nariz", "neón", "nieve", "noche", "norte", "nota", "nuevo", "nudo", "número", 
                   "obra", "oeste", "once", "oro", "oscuridad", "osito", "otro", "ovalo", "pago", "palo", "papel", "para", "pared", 
                   "paso", "pasto", "paz", "quien", "quitar", "química", "queso", "quieto", "quedar", "quince", "quejar", "quebrar", 
                   "querer", "quizá", "rabia", "rabo", "raro", "rayo", "razón", "rato", "real", "rebelde", "rechazo", "reconocer", 
                   "recordar", "recuerdo", "recurso", "redondo", "reflejo", "regalo", "regresar", "relámpago", "religión", "remedio", 
                   "remolque", "renovar", "renta", "reparar", "repetir", "rescatar", "residuo", "resolver", "respeto", "resultado", 
                   "retirar", "retorno", "reunión", "revés", "reyes", "rico", "rienda", "riesgo", "rigidez", "rincon", "riqueza", 
                   "risa", "ritmo", "robusto", "roca", "rodar", "rodear", "rojo", "roto", "ruido", "ruina", "ruleta", "rumbo", "ruptura", 
                   "saber", "sabor", "sacar", "sacrificio", "sagrado", "salado", "saldo", "salir", "saltar", "salud", "sangre", "sanidad", 
                   "sano", "satisfacción", "saxofón", "secreto", "seguir", "semana", "semilla", "senda", "sendero", "separar", "sepia", 
                   "sereno", "serie", "serpiente", "servir", "setenta", "severo", "sexo", "siempre", "siete", "siglo", "signo", "silencio", 
                   "silla", "sillón", "símbolo", "simple", "sinónimo", "sistema", "sitio", "sobre", "socio", "sofá", "solución", "sombra", 
                   "sonido", "sopa", "sorpresa", "sostener", "soy", "suave", "subir", "sudor", "sueco", "suelo", "sujeto", "suma", "superar", 
                   "suponer", "surco", "susto", "tabaco", "tabla", "táctica", "talento", "tamaño", "tampoco", "tanque", "tarde", "tarea", 
                   "tarifa", "taza", "tejido", "tele", "teléfono", "tema", "temor", "templo", "tener", "tentar", "teoría", "terapia", 
                   "tercero", "termómetro", "terror", "tesis", "testigo", "texto", "tiempo", "tierra", "tigre", "tijera", "típico", "tipo", 
                   "tirar", "título", "tocar", "todavía", "todo", "toma", "tomate", "tono", "topo", "tormenta", "torno", "torre", "tortuga", 
                   "tosco", "total", "trabajo", "tragar", "trámite", "trampa", "trance", "tranquilo", "transferir", "trasero", "trasladar", 
                   "trato", "trauma", "trazar", "trece", "tregua", "treinta", "trenza", "tres", "tribu", "trigo", "tripa", "tristeza", 
                   "triunfo", "trofeo", "trompeta", "tropa", "trotar", "trueno", "trufa", "tuerto", "tumba", "tumor", "túnel", "turismo", 
                   "turno", "ubicar", "unidad", "unir", "uno", "untar", "urgente", "usar", "usuario", "usual", "vacío", "vago", "vaina", 
                   "valentía", "valle", "valor", "vapor", "vara", "variar", "vaso", "vecino", "vector", "vehículo", "veinte", "vejez", "vela", 
                   "velero", "velocidad", "vena", "vencer", "venda", "vender", "veneno", "venganza", "venir", "venta", "ventaja", "verano", 
                   "verdad", "verde", "vereda", "verja", "verso", "verter", "vestido", "veterano", "vez", "viaje", "vibración", "víctima", 
                   "vida", "viejo", "viernes", "vigor", "vil", "villa", "vinagre", "vino", "violencia", "virgen", "virtud", "visor", "vista", 
                   "vitamina", "viuda", "vivir", "vocal", "voz", "vuelo", "vulgar", "yegua", "yerno", "yeso", "yodo", "yoga", "yogur", 
                   "yunque", "zapato", "zarza", "zona", "zoom", "zorro", "zumo", "zurdo","zanahoria", "zapatería", "zarpar", "zebra", "zigzag", 
                   "zona", "zoológico", "zumbar", "zumo", "abadesa", "abalorio", "abdominal", "abolladura", "abominable", "abrevadero", 
                   "abrumador", "abstención", "abundancia", "aburrido", "acantilado", "acariciar", "aceituna", "acelerar", "acompañar", 
                   "acontecimiento", "acordeón", "acostumbrar", "acrobático", "actitud", "actualizar", "acuático", "adentro", "adherente", 
                   "adios", "adivinar", "adjetivo", "admirar", "adolescente", "adopción", "adorable", "adormecer", "adquirir", "adulterio", 
                   "adversario", "afectuoso", "aferrarse", "aficionado", "afilar", "afinidad", "afirmar", "afortunado", "afrodisíaco", "agasajar", 
                   "agilidad", "aglomeración", "agotar", "agradecer", "agrietado", "agrupar", "aguacate", "aguantar", "agudo", "ahogado", "ahorro", 
                   "aire", "ajedrez", "ajetreado", "ajuar", "alambre", "alargado", "albañil", "alboroto", "alcaide", "alcalino", "alcance", 
                   "alcohol", "alfabeto", "alfombra", "algodón", "alguien", "alimentar", "aliviar", "almacén", "almendra", "almidón", "almohada", 
                   "almuerzo", "alojamiento", "alpino", "altar", "alternar", "altitud", "altruismo", "aluminio", "alusión", "amaestrar", "amargura", 
                   "ambiental", "amigo", "amnistía", "amo", "amor", "ampliar", "anacardo", "analfabeto", "análisis", "anatomía", "anchura", 
                   "ancla", "anécdota", "anfitrión", "ángulo", "anhelar", "animado", "aniversario", "anochecer", "anotar", "ansiedad", "antebrazo", 
                   "antena", "antiguo", "antipático", "anunciar", "añicos", "añil", "apagar", "aparato", "aparecer", "apartar", "apego", "apetito", 
                   "apio", "aplaudir", "aplicar", "apoderarse", "aportar", "apóstol", "apoyar", "aprender", "aprobar", "apuesto", "apuntar", 
                   "apurado", "apuro", "aquejar", "araña", "arbitrar", "arbol", "arcano", "algoritmos", "aplicacion", "articulos", "automovil", 
                   "calculador", "campesinos", "celularcar", "ciudadesan", "colombiano", "comentarios", "complicado", "computador", "conocerlos", 
                   "convencido", "correremos", "cuestiones", "culturalis", "deportivas", "descubierta", "desencaden", "desgraciad", "despoblada", 
                   "despreciar", "destrozado", "diferentes", "disculpeme", "distanciaa", "documentos", "dominicana", "dormitorios", "ejemplares", 
                   "encendidos", "encuentros", "enfermedad", "entrenador", "españolito", "estadistic", "eventuales", "excelentes", "explicando", 
                   "extranjera", "fantastica", "favoritas", "femeninos", "festivalde", "fielescria", "finalmente", "fraccionde", "fueronconm", 
                   "galvanizad", "generacion", "gobiernoec", "gustabaque", "historiasd", "hombresdeh", "imaginacio", "impermeabl", "impresione", 
                   "incluidasl", "indiferent", "informacio", "inolvidabl", "inquietud", "interesant", "intimidadp", "investigac", "juegodepal", 
                   "jugadoresc", "justificad", "lamentable", "latinoamer", "letrasparap", "libertador", "limitacion", "localidade", "madridista", 
                   "magnificaa", "mandataria", "maravillos", "martinezma", "menosprecio", "merecidame", "metodologi", "mexicanosd", "militantes", 
                   "ministerio", "modernidad", "montañeses", "nacionales", "naturaleza", "negociosdi", "niñitasbe", "notificaci", "observador", 
                   "ocupacione", "operativos", "oportunida", "ordenadosa", "organismos", "pactogloba", "pandillero", "parroquias", "particular", 
                   "pasionesoñ", "pedagogico", "permanenci", "personalidad", "poblacione", "poderosos", "policiacos", "politizado", "portuguesa", 
                   "posibilida", "preciosidad", "preferible", "presenciae", "prevencion", "primariasu", "problemasa", "producirse", "proteccion", 
                   "publicidad", "puntualidad", "quinceañer", "realizaban", "recuperaci", "reducciond", "reformasla", "regeneraci", "reivindic", 
                   "relaciones", "relevancia", "represalia", "requerimie", "respetable", "resultados", "retrospect", "revolucion", "rigurosamente", 
                   "romantismo", "sacrificad", "saludables", "sanjuanero", "seguidores", "olla","mano","luz","más","sí","mío","tiene","sobre","poder",
                   "tú","ver","lejos","tanto","allá","saber","hoy","sino","por","mucho","cada","fue","vez","nada","aún","gran","donde","debe",
                   "vida","puede","cielo","niño","amor","tal","hacer","pues","triste","seis","hecho","falta","mesa","mundo","lado","casa","estar",
                   "razón","hombre","frente","tal vez","pronto","misma","noche","dejar","saber","manera","nuevo","verdad","agua","también","sólo",
                   "otro","dos","había","señor","nunca","gente","aquí","ahora","llegar","hasta","mujer","puerta","paso","bueno","quién","cierto",
                   "hijo","casi","madre","familia","alguien","tener","ojos","modo","años","niña","boca","parte","año","hecho","pensar","vida",
                   "camino","cosa","hacia","tarde","nuevo","hombre","siempre","padre","mismo","algunos","forma","decir","noche","mientras","dejar",
                   "trabajo","mira","calle","dentro","mundo","mira","carne","mismo","lugar","mañana","más allá","semana","cabeza","día","aunque",
                   "corazón","persona","cuerpo","maestro","tiempo","alma","correr","bien","llamar","un", "es", "y", "el", "la", "los", "las", "que", 
                   "en", "se", "de", "por", "con", "para", "no", "una", "como", "más", "o", "pero", "al", "su", "este", "si", "sí", "también", "me", 
                   "ha", "bien", "ya", "del", "está", "porque", "muy", "ha", "solo", "todo", "ser", "son", "tiene", "hace", "nos", "hasta", "sin", 
                   "aunque", "quiero", "soy", "él", "fue", "estar", "quien", "hoy", "mismo", "hacer", "puede", "entre", "quieres", "cómo", "gran", 
                   "vida", "hombre", "parte", "trabajo", "otro", "poco", "después", "cada", "tiempo", "durante", "primero", "mucho", "antes", 
                   "desde", "nosotros", "nada", "pues", "tener", "vez", "cosa", "tener", "decir", "nuevo", "nunca", "dar", "hecho", "cual", "dos", 
                   "cosas", "ver", "casi", "saber", "aquí", "madre", "poco", "personas", "mundo", "forma", "tener", "hijo", "padre", "mujer", 
                   "lugar", "fin", "dejar", "familia", "poder", "razón", "cabeza", "quiere", "cosa", "día", "aquella", "bajo", "pasa", "buen", 
                   "lado", "amor", "sigue", "mañana", "nuestro", "hasta", "cuerpo", "agua", "puesto", "pasado", "pronto", "dicho", "menos", "sabe", 
                   "solo", "cerca", "ahora", "creo", "miedo", "viejo", "hijo", "mal", "ayer", "debajo", "encontrar", "idea", "mano", "siempre", 
                   "toda", "hermano", "verdad", "través", "caminar", "año", "gente", "quizás", "ciudad", "último", "corazón", "cuerpo", "camino", 
                   "necesito", "mientras", "amigo", "misma", "paso", "fuera", "casa", "podía", "algunos", "cara", "ningún", "palabras", "fuerza", 
                   "mundo", "horas", "voz", "dios", "fuerte", "luz", "vieja", "momento", "fácil", "espero", "quedó", "nuevo", "nombre", "amigos", 
                   "ojos", "luego", "casi", "niños", "aunque", "ayer", "manera", "tarde", "esperanza", "encontré", "dolor"]
datos_validacion = 
# He preferido duplicar el diccionario por comodidad.
Aurebesh = {'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'd': 'dorn', 'e': 'esk', 'f': 'forn', 'g': 'grek', 'h': 'herf',
            'i': 'isk', 'j': 'jenth', 'k': 'krill', 'l': 'leth', 'm': 'merm', 'n': 'nern', 'o': 'osk', 'p': 'peth',
            'q': 'qek',  'r': 'resh', 's': 'senth', 't': 'trill', 'u': 'usk', 'v': 'vev', 'w': 'wesk',
            'x': 'xesh', 'y': 'yirt', 'z': 'zerek'}

Castellano = {'aurek': 'a', 'besh': 'b',  'cresh': 'c', 'dorn': 'd',  'esk': 'e', 'forn': 'f', 'grek': 'g', 'herf': 'h',
              'isk': 'i',  'jenth': 'j',  'krill': 'k',  'leth': 'l',  'merm': 'm',  'nern': 'n',  'osk': 'o',  'peth': 'p',
              'qek': 'q',  'resh': 'r',  'senth': 's', 'trill': 't',  'usk': 'u', 'vev': 'v',  'wesk': 'w',
              'xesh': 'x', 'yirt': 'y', 'zerek': 'z'}

# Funcion que pasa de castellano a aurebesh
def castellano_aurebesh(texto_castellano):

    texto_aurebesh = ''

    for caracter in texto_castellano:
        if caracter == ' ':
            texto_aurebesh += ' '
        else:
            try:
                texto_aurebesh += Aurebesh[caracter.lower()]
            except KeyError:
                texto_aurebesh += '???'
    return (texto_aurebesh)

# Funcion que pasa de aurebesh a castellano
def aurebesh_castellano(texto_aurebesh):

    texto_castellano = ''
    token_aurebesh = ''

    for caracter in texto_aurebesh:
        if caracter == ' ':
            texto_castellano += ' '
        else:
            token_aurebesh +=caracter
            try:
                texto_castellano += Castellano[token_aurebesh.lower()]
                token_aurebesh=''
            except KeyError:
                if len(token_aurebesh)>5 :
                    texto_castellano += '?'
    if token_aurebesh != '':
        texto_castellano += '?'
    return (texto_castellano)

with open('datos_entreno.csv', mode='w', newline='') as datos_entreno_csv:
    writer=csv.writer(datos_entreno_csv, delimiter=',')
    writer.writerow(["Castellano","Aurebesh"])
    i=0
    for pal_castellano in datos_iniciales:
        i +=1
        pal_aurebesh =castellano_aurebesh(unidecode(pal_castellano))
        print(f" {i} - {pal_castellano} , {pal_aurebesh}")
        writer.writerow([unidecode(pal_castellano), pal_aurebesh])
        
    
    
'''texto_aurebesh = input("Entra el texto a traducir al Castellano: ")
print(aurebesh_castellano(texto_aurebesh))'''

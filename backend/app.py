from cgitb import reset
from experta import *

class Trouble(Fact):
    pass

def update(answer):
    global errors
    errors = answer

class Robot3DTroubles(KnowledgeEngine):

    @Rule(Trouble(error='Problemas iniciales'))
    def init_Trouble(self):
        next_step = ['Problemas con la primer capa', 'Hilos rodeando la pieza', 'Mala definición', 'Pieza desfasada', 'Pieza quedó a medio hacer', 'Ausencia de filamento al inicio de la impresión']
        update(next_step)
    @Rule(Trouble(error='Problemas con la primer capa'))
    def first_Layer_Trouble(self):
        next_step = ['Mala definición', 'Se despegó la primera capa']
        update(next_step)
    #Problemas con la primer capa    
    @Rule(Trouble(error='Mala definición'))
    def bad_Definition_Trouble(self):
        next_step = ['La pieza tiene burbujas explotadas', 'La pieza tiene agujeros o falta de material entre las capas', 'Las poleas están ajustadas', 'Las poleas no están ajustadas']
        update(next_step)
        #Mala definición
    @Rule(Trouble(error='La pieza tiene burbujas explotadas'))
    def booble_Trouble(self):
        next_step = ['El filamento está húmedo']
        update(next_step)
    @Rule(Trouble(error='La pieza tiene agujeros o falta de material entre las capas'))
    def hole_Trouble(self):
        next_step = ['Aumentar el porcentaje de “overlap”']
        update(next_step)
    @Rule(Trouble(error='Las poleas están ajustadas'))
    def very_Tight_Pulley_Trouble(self):
        next_step = ['El programa usado está mal configurado']
        update(next_step)
    @Rule(Trouble(error='Las poleas no están ajustadas'))
    def low_Tension_Pulley_Trouble(self):
        next_step = ['Ajuste correctamente las poleas']
        update(next_step)
        #----------------------------------------------------    
    @Rule(Trouble(error='Se despegó la primera capa'))
    def fixing_Trouble(self):
        next_step = ['La cama no fué ajustada', 'La cama fué ajustada']
        update(next_step)
        #Se despegó la primera capa
    @Rule(Trouble(error='La cama no fué ajustada'))
    def uneven_Trouble(self):
        next_step = ['Nivelar correctamente la cama']
        update(next_step)
        #----------------------------------------------------
    @Rule(Trouble(error='La cama fué ajustada'))
    def level_Trouble(self):
        next_step = ['La velocidad de impresión no es la correcta', 'La velocidad de impresión es la correcta']
        update(next_step)
            #La cama fué ajustada
    @Rule(Trouble(error='La velocidad de impresión no es la correcta'))
    def high_Speed_Trouble(self):
        next_step = ['Configurar bien la velocidad de impresión según el modelo']
        update(next_step)
            #----------------------------------------------------    
    @Rule(Trouble(error='La velocidad de impresión es la correcta'))
    def speed_Trouble(self):
        next_step = ['La impresora tiene cama caliente', 'La impresora no tiene cama caliente']
        update(next_step)
                #La velocidad de impresión es la correcta
    @Rule(Trouble(error='La impresora tiene cama caliente'))
    def low_Temperature_Trouble(self):
        next_step = ['Configurar bien la temperatura de la cama']
        update(next_step)
                #----------------------------------------------------
    @Rule(Trouble(error='La impresora no tiene cama caliente'))
    def no_Hot_Bed_Trouble(self):
        next_step = ['Aplique algún adhesivo sobre la cama', 'No aplique algún adhesivo sobre la cama']
        update(next_step)
                    #La impresora no tiene cama caliente
    @Rule(Trouble(error='Aplique algún adhesivo sobre la cama'))
    def adhesive_Trouble(self):
        next_step = ['Tu impresora no sirve para lo que necesitas']
        update(next_step)
                    #----------------------------------------------------
    @Rule(Trouble(error='No aplique algún adhesivo sobre la cama'))
    def little_Adhesion_Trouble(self):
        next_step = ['Ponele algun adhesivo a la cama']
        update(next_step)
                    #----------------------------------------------------
                #----------------------------------------------------
            #----------------------------------------------------
        #----------------------------------------------------
    #----------------------------------------------------    

    @Rule(Trouble(error='Hilos rodeando la pieza'))
    def threads_Trouble(self):
        next_step = ['La temperatura está configurada correctamente', 'La temperatura no está configurada correctamente']
        update(next_step)
    #Hilos rodeando la pieza    
    @Rule(Trouble(error='La temperatura no está configurada correctamente'))
    def bad_Temperature_Trouble(self):
        next_step = ['Configurar bien la temperatura']
        update(next_step)            
    #----------------------------------------------------
    @Rule(Trouble(error='La temperatura está configurada correctamente'))
    def temperature_Trouble(self):
        next_step = ['La velocidad de impresión es la correcta.', 'La velocidad de impresión no es la correcta.']
        update(next_step)
        #La temperatura está configurada correctamente
    @Rule(Trouble(error='La velocidad de impresión es la correcta.'))
    def thread_Speed_Trouble(self):
        next_step = ['Configura bien la velocidad de retracción.']
        update(next_step)
    @Rule(Trouble(error='La velocidad de impresión no es la correcta.'))
    def thread_High_Speed_Trouble(self):
        next_step = ['Configurar bien la velocidad de impresión.']
        update(next_step)
        #----------------------------------------------------
    #----------------------------------------------------    

    @Rule(Trouble(error='Pieza desfasada'))
    def out_Of_Phase_Trouble(self):
        next_step = ['Las poleas están ajustadas', 'Las poleas no están ajustadas']
        update(next_step)
    #Pieza desfasada
    @Rule(Trouble(error='Las poleas están ajustadas'))
    def right_Pulley_Trouble(self):
        next_step = ['Baje la velocidad de impresión']
        update(next_step)
    @Rule(Trouble(error='Las poleas no están ajustadas'))
    def bad_Pulley_Trouble(self):
        next_step = ['Ajuste correctamente las poleas']
        update(next_step)
    #----------------------------------------------------

    @Rule(Trouble(error='Pieza quedó a medio hacer'))
    def half_Done_Trouble(self):
        next_step = ['Hay exceso de filamento', 'No hay exceso de filamento']
        update(next_step)
    #Pieza quedó a medio hacer
    @Rule(Trouble(error='Hay exceso de filamento'))
    def too_Much_Plastic_Trouble(self):
        next_step = ['Los soportes fueron configurados', 'Los soportes no fueron configurados']
        update(next_step)
        #Hay exceso de filamento
    @Rule(Trouble(error='Los soportes fueron configurados'))
    def suppor_Trouble(self):
        next_step = ['Las correas están flojas']
        update(next_step)
    @Rule(Trouble(error='Los soportes no fueron configurados'))
    def no_Support_Trouble(self):
        next_step = ['Ajustar las correas']
        update(next_step)    
        #----------------------------------------------------
    #----------------------------------------------------
    @Rule(Trouble(error='No hay exceso de filamento'))
    def plastic_Trouble(self):
        next_step = ['El carrete no tiene filamento', 'Hay excedente de plástico entre el extrusor y barrel', 'El nozzle está tapado']
        update(next_step)
        #No hay exceso de filamento
    @Rule(Trouble(error='El carrete no tiene filamento'))
    def ran_Out_Of_Plastic_Trouble(self):
        next_step = ['Cargar el carrete con filamento']
        update(next_step)
        #----------------------------------------------------
    #----------------------------------------------------    
    @Rule(Trouble(error='Hay excedente de plástico entre el extrusor y barrel'))
    def excess_Plastic_Trouble(self):
        next_step = ['La temperatura del barrel excede de la correcta, configurar bien la temperatura del mismo']
        update(next_step)    
        #----------------------------------------------------
    @Rule(Trouble(error='El nozzle está tapado'))
    def block_Nozzle_Trouble(self):
        next_step = ['La temperatura del barrel está por debajo de la esperada', 'La temperatura del barrel está configurada correctamente']
        update(next_step)
            #El nozzle está tapado
    @Rule(Trouble(error='La temperatura del barrel está por debajo de la esperada'))
    def low_Barrel_Temperature_Trouble(self):
        next_step = ['Configurar bien la temperatura del barrel.']
        update(next_step)
            #----------------------------------------------------
    @Rule(Trouble(error='La temperatura del barrel está configurada correctamente'))
    def barrel_Temperature_Trouble(self):
        next_step = ['El nozzle no fué ajustado', 'El nozzle fué ajustado']
        update(next_step)    
                #La temperatura del barrel está configurada correctamente
    @Rule(Trouble(error='El nozzle no fué ajustado'))
    def loose_Nozzle_Trouble(self):
        next_step = ['Ajustar bien el nozzle']
        update(next_step)
                #----------------------------------------------------
    @Rule(Trouble(error='El nozzle fué ajustado'))
    def tight_Nozzle_Trouble(self):
        next_step = ['El barrel está desgastado', 'El barrel no está desgastado']
        update(next_step)
                    #El nozzle fué ajustado
    @Rule(Trouble(error='El barrel está desgastado'))
    def bad_Barrel_Trouble(self):
        next_step = ['Comprar otro barrel']
        update(next_step)
    @Rule(Trouble(error='El barrel no está desgastado'))
    def barrel_Trouble(self):
        next_step = ['El nozzle es de mala calidad, comprar otro.']
        update(next_step)
                    #----------------------------------------------------
                #----------------------------------------------------
            #----------------------------------------------------
        #----------------------------------------------------
    #----------------------------------------------------
    @Rule(Trouble(error='Ausencia de filamento al inicio de la impresión'))
    def no_Plastic_Trouble(self):
        next_step = ['El carrete no tiene filamento', 'Hay excedente de plástico entre el extrusor y barrel', 'El nozzle está tapado']
        update(next_step)

engine = Robot3DTroubles()

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/trouble/")
def get_trouble():
    global errors
    name = request.args.get('name')
    engine.reset()
    engine.declare(Trouble(error=name))
    engine.run()
    response = errors[0] if len(errors) == 1 else None
    newErrors = errors if len(errors) > 1 else []
    return {
        "response": response,
        "newErrors": newErrors
    }

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

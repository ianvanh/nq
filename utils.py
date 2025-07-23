from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timezone, timedelta
from config import *
import random

fuente_fijos = ImageFont.truetype(FIJOS, 36)
fuente_datos = ImageFont.truetype(DATOS, 36)

def formatear_valor(valor):
  try:
    valor = float(valor)
    return f"$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
  except ValueError:
    return valor

def formatear_telefono(numero):
  if len(numero) == 10 and numero.isdigit():
    return f"{numero[:3]} {numero[3:6]} {numero[6:]}"
    return numero

def by_letter(draw, texto, x, y, fuente, color, espaciado=0):
    posicion_x = x
    for letra in texto:
        draw.text((posicion_x, y), letra, fill=color, font=fuente)
        posicion_x += fuente.getlength(letra) + espaciado

def generar_fecha_hora():
  utc_offset = timedelta(hours=-5)
  zona_horaria = timezone(utc_offset)
  ahora = datetime.now(zona_horaria)
  meses = [
  "enero", "febrero", "marzo", "abril", "mayo", "junio",
  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
  ]
  dia = ahora.day
  mes = meses[ahora.month - 1]
  año = ahora.year
  hora = ahora.strftime("%I:%M %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
  return f"{dia:02d} de {mes} de {año} a las {hora}"

def generar_codigo_referencia():
  return f"M2{random.randint(1000000, 9999999)}"
  
def code_nequi(nombre, telefono, valor):
    try:
        imagen = Image.open(PLANTILLA)
        draw = ImageDraw.Draw(imagen)
        ancho_imagen, alto_imagen = imagen.size
        
        margen_derecho = 66
        y_base = 960
        x_fijo = 95
        separacion = 50
        
        by_letter(draw, "Para", x_fijo, y_base, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_nombre = y_base + separacion
        by_letter(draw, nombre, x_fijo, y_d_nombre, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_valor = y_d_nombre + 64
        by_letter(draw, "¿Cuánto?", x_fijo, y_f_valor, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_valor = y_f_valor + separacion
        by_letter(draw, formatear_valor(valor), x_fijo, y_d_valor, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_numero = y_d_valor + 64
        by_letter(draw, "Número Nequi", x_fijo, y_f_numero, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_numero = y_f_numero + separacion
        by_letter(draw, formatear_telefono(telefono), x_fijo, y_d_numero, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_fecha = y_d_numero + 64
        by_letter(draw, "Fecha", x_fijo, y_f_fecha , fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_fecha = y_f_fecha + separacion
        by_letter(draw, generar_fecha_hora(), x_fijo, y_d_fecha, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_referencia = y_d_fecha + 64
        by_letter(draw, "Referencia", x_fijo, y_f_referencia, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_referencia = y_f_referencia + separacion
        by_letter(draw, generar_codigo_referencia(), x_fijo, y_d_referencia, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        ruta_factura = "resultado.png"
        imagen.save(ruta_factura)
        return ruta_factura

    except Exception as e:
        raise Exception(f"Error al generar la factura: {e}")
        
def code_qr(nombre, valor):
    try:
        imagen = Image.open(PLANTILLA_QR)
        draw = ImageDraw.Draw(imagen)
        ancho_imagen, alto_imagen = imagen.size
        
        margen_derecho = 66
        y_base = 950
        x_fijo = 95
        separacion = 50
        
        by_letter(draw, "Pago en", x_fijo, y_base, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_nombre = y_base + separacion
        by_letter(draw, nombre, x_fijo, y_d_nombre, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_valor = y_d_nombre + 64
        by_letter(draw, "¿Cuánto?", x_fijo, y_f_valor, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_valor = y_f_valor + separacion
        by_letter(draw, formatear_valor(valor), x_fijo, y_d_valor, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_fecha = y_d_valor + 64
        by_letter(draw, "Fecha", x_fijo, y_f_fecha , fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_fecha = y_f_fecha + separacion
        by_letter(draw, generar_fecha_hora(), x_fijo, y_d_fecha, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        y_f_referencia = y_d_fecha + 64
        by_letter(draw, "Referencia", x_fijo, y_f_referencia, fuente_fijos, COLOR_NOMBRES, espaciado=0.8)
        y_d_referencia = y_f_referencia + separacion
        by_letter(draw, generar_codigo_referencia(), x_fijo, y_d_referencia, fuente_datos, COLOR_DATOS, espaciado=0.4)
        
        ruta_factura = "resultado_qr.png"
        imagen.save(ruta_factura)
        return ruta_factura

    except Exception as e:
        raise Exception(f"Error al generar la factura: {e}")
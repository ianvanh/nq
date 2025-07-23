from telegram import Update
from telegram.ext import ContextTypes
from utils import code_nequi, code_qr
from config import *

async def nequi(bot: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = bot.effective_user.id
  
  if context.args and len(context.args) >= 3:
    valor = context.args[-1]
    telefono = context.args[-2]
    nombre = ' '.join(context.args[:-2]).title()
    
    if not all(p.isalpha() or p.isspace() for p in nombre):
      await bot.message.reply_text("El nombre solo puede contener letras y espacios. Por favor, inténtelo de nuevo.")
      return

    if not (telefono.isdigit() and len(telefono) == 10):
      await bot.message.reply_text("El número de teléfono debe contener exactamente 10 dígitos numéricos. Por favor, inténtelo de nuevo.")
      return

    if not valor.isdigit():
      await bot.message.reply_text("El valor debe ser un número entero sin puntos ni signos. Por favor, inténtelo de nuevo.")
      return
    
    code_nequi(nombre, telefono, valor)
    with open("resultado.png", "rb") as documento:  
      await context.bot.send_document(chat_id=bot.message.chat_id, document=documento)  
  else:  
    await bot.message.reply_text("Por favor ingrese los valores en este formato:\n/nequi Nombre Telefono Valor")

async def qr(bot: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = bot.effective_user.id
  
  if context.args and len(context.args) >= 2:
    valor = context.args[-1]
    nombre = ' '.join(context.args[:-1]).title()
    
    if not all(p.isalpha() or p.isspace() for p in nombre):
      await bot.message.reply_text("El nombre solo puede contener letras y espacios. Por favor, inténtelo de nuevo.")
      return

    if not valor.isdigit():
      await bot.message.reply_text("El valor debe ser un número entero sin puntos ni signos. Por favor, inténtelo de nuevo.")
      return
    
    code_qr(nombre, valor)
    with open("resultado_qr.png", "rb") as documento:  
      await context.bot.send_document(chat_id=bot.message.chat_id, document=documento)  
  else:  
    await bot.message.reply_text("Por favor ingrese los valores en este formato:\n/qr Nombre Valor")
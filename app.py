from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TOKEN
from handlers import nequi, qr

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  user = update.effective_user
  await update.message.reply_text(
    f"¡Hola {user.first_name}! 👋\n\n"
    "Soy tu bot de comprobantes Nequi favorito."
  )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nequi", nequi))
    application.add_handler(CommandHandler("qr", qr))
    
    print("Bot iniciado...")
    application.run_polling()

if __name__ == '__main__':
    main()
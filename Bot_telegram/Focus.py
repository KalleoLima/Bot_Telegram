import telebot
import os
from dotenv import load_dotenv

load_dotenv()

booot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

Vendas = ({"milho" : 0,
           "trigo" : 0, "soja" : 0, "xerem grosso" : 0,
           "xerem fino" : 0
    })


@booot.message_handler(commands= ['mostrarFaturamento'])
def Mostrarfaturamento(messagemm):
      for produto, faturamento in Vendas.items():
            booot.send_message(messagemm.chat.id,f"produto: {produto} : {faturamento}")

@booot.message_handler(commands=['vendi_milho'])
def maisUmMilho(milho):
      Vendas["milho"] += 80
      booot.reply_to(milho,"foi adicionado ao faturamento!")
      return

@booot.message_handler(commands= ['vendi_trigo'])
def maisUmFarelo(trigo):
      Vendas["trigo"] += 40
      booot.reply_to(trigo, "foi adicionado ao faturamento!")
      return

@booot.message_handler(commands=['vendi_xeremGrossoSaca'])
def maisUmXeremGrosso(xeremGrosso):
      Vendas["xerem fino"] += 80
      booot.reply_to(xeremGrosso, "foi adicionado ao faturamento! ")
      return

@booot.message_handler(commands=['vendi_xeremFIno'])
def maisUmXeremFino(xeremFino):
      Vendas['xerem fino'] += 80
      booot.reply_to(xeremFino, "foi adicionado ao faturamento!")
      return


def racao(mensagem):
        return True

@booot.message_handler(func=racao)
def Responder(mensagem):
    texto = (
    "📌 *Comandos do bot*\n"
    "Digite uma das opções abaixo:\n\n"
    "• vendi milho\n"
    "• vendi trigo\n"
    "• vendi xerem grosso\n"
    "• vendi xerem fino\n"
)
    booot.reply_to(mensagem, texto)

    
  

booot.infinity_polling()
import discord
from discord.ext import commands
from model import sinif
import random

proje = ['Bir kukla önce basit bir kukla yapıp hareket edicek yerlere ip iplere motor bağla ipler tendon görevi görerek kuklayı hareket ettirecektir',
         'Mesafe sensörü mesafe sensörünü bağlayıp buna da bir buzzer takın mesafe sensörü engelin yaklaştığını anlayınca buzzeri çalıştırıp ses çıkarcak',
         'Bu proje, bir joystick ve ses kontrolü kullanarak bir kapı kilidini kontrol etmeyi amaçlar. Joystick ile uzaktan yönetim ve buzzer ile sesli komutları içerir.',
         'Arduino ile basit bir uzaktan kontrol aracı oluşturun']
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'bot çalıştırıldı {bot.user}')
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def yılbaşın_kutlolsun_benim_adım(ctx ,name = 'eren'):
    await ctx.send('seninde ' + name)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def proje_öner(ctx):
    await ctx.send(random.choice(proje))

@bot.command()
async def algila(ctx):
    #print(ctx.message.attachments)
    if ctx.message.attachments:
      for attachment in ctx.message.attachments:
        file_name = attachment.filename
        file_url = attachment.url
        
        await attachment.save(f"images/{file_name}") 
        sonuc = sinif(f"images/{file_name}")
        if sonuc.strip() == 'joistick':
            await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'öğrenmek için google de ara şunu' + 'https://www.arduinomedia.com/mblock-ile-joystick-kullanimi/')
        elif sonuc.strip() == 'ardinio uno':
           await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'bunu bilmiyorsan ardinyoya hiç başlama' )
        elif sonuc.strip() == 'buzzer':
           await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'öğrenmek için şunu arat' + 'https://www.arduinomedia.com/mblock-ve-arduino-ile-buzzer-kullanimi/') 
        elif sonuc.strip() == 'led':
           await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'öğrenmek için şunu arat' + 'https://kodlamayap.com/2017/12/01/tek-led-yakip-sondurme/') 
        elif sonuc.strip() == 'mesafe sensoru':
           await ctx.send("resim bulundu ve bana kalırsa mesafe sensörü" + 'https://www.arduinomedia.com/mblock-ile-hc-sr04-mesafe-sensoru-kullanimi/') 
        elif sonuc.strip() == 'Dcl ekran':
           await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'bunu kullanmak zordur' + 'https://maker.robotistan.com/arduino-dersleri-10-16x2-lcd-ekran/')  
        elif sonuc.strip() == 'servo motor':
           await ctx.send("resim bulundu ve bana kalırsa " + sonuc + 'https://www.arduinomedia.com/mblock-ve-arduino-ile-servo-motor-kullanimi/')       
        elif sonuc.strip() == 'hava kalite sensoru':
           await ctx.send("resim bulundu ve bana kalırsa hava kalite sensörü" +' https://www.hbmacit.com/2020/01/18/arduino-ile-mq-135-hava-kalite-sensoru-kullanimi/') 
           print(sonuc)
    else: 
        await ctx.send("resim bulunamadı.")

bot.run("MTE4NTk4MTk0NTE3NjM5MTczMA.G5Yb6B.CN1ApAZ3VpVQXadjnXPnnsoxp4fY4Ab_jIGO_4")
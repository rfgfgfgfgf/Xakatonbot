import nextcord
import os
import random
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Бот готов!")
    aim = nextcord.Game("Глобальное потепление")
    await bot.change_presence(status=nextcord.Status.online, activity=aim)
    
@bot.slash_command(name='info', description='Получить информацию о глобальном потеплении')
async def info(ctx):
    embed = nextcord.Embed(title = 'Что такое Глобальное Потепление вкратце?', description = 'Глобальное потепление – это долгосрочное повышение средней температуры на поверхности Земли. Оно вызвано увеличением концентрации парниковых газов, таких как углекислый газ, метан и озон.')
    await ctx.send(embed=embed)

@bot.slash_command(name='reduce_carbon', description='Получить советы по сокращению углеродного следа')
async def reduce_carbon(ctx):
    tips = [
        
        "Сократите использование пластика и переходите на многоразовые продукты!",
        "Используйте общественный транспорт или электро-кары!",
        "Установите энергоэффективные лампы и устройства!",
        "Сократите потребление мяса и продуктов животного происхождения!",
        "Участвуйте в местных инициативах по озеленению и утилизации!",
        "Сократите вырубку леса (если вы способствовали в этом)- она повышает концентрацию углекислого газа в атмосфере!"
    ]
    embed = nextcord.Embed(title = 'Советы по уменьшению углекислого газа.', description = f'{tips}')
    await ctx.send(embed=embed)


@bot.slash_command(name='news', description='Получить последние новости о климате')
async def news(ctx):
    embed = nextcord.Embed(title='Источники новостей о климате.', description = '"Вот несколько источников для последних новостей о климате: [NASA Climate Change](https://climate.nasa.gov/) [Climate Central](https://www.climatecentral.org/) [IPCC Reports](https://www.ipcc.ch/reports/)"')
    await ctx.send(embed=embed)

@bot.slash_command(name='actions', description='Предложения действий по борьбе с глобальным потеплением')
async def actions(ctx):
    actions = [

        "Участвуйте в местных мероприятиях по уборке.",
        "Поддержите законопроекты, направленные на борьбу с изменением климата.",
        "Используйте экологичные продукты и услуги.",
        "Используйте больше електро-энергии.",
    ]

    embed = nextcord.Embed(title='Предложения действий по борьбе с глобальным потеплением', description=f'{actions}')
    await ctx.send(embed=embed)



@bot.slash_command(name='projects', description='Информация о проектах и инициативах по охране окружающей среды')
async def projects(ctx):
    projects = [

        "Климатический альянс [Climate Alliance](https://climatealliance.org/)",
        "Мировая инициатива по озеленению [Global Green Initiative](https://globalgreen.org/)",
        "Проект по восстановлению лесов [Reforestation Project](https://reforestationproject.org/)"
    ]
    embed = nextcord.Embed(title='Информация о проектах по спасению климата', description = f"{projects}")
    await ctx.send(embed=embed)



@bot.slash_command(name='global_warming_causes', description="Отправляет вам последствия которые может вызвать игнорирование Глобального Потепления.")
async def global_warming_causes(ctx):
    image_folder = "images"
    causes = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    if causes:
        random_cause = os.path.join(image_folder, random.choice(causes))
        with open(random_cause, 'rb') as f:
            picture = nextcord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("Ошибка в отправки :(")




@bot.slash_command(name='recycle', description='Информация о переработке отходов')
async def recycle(ctx):
    recycling_tips = [

        "Пластиковые бутылки и контейнеры можно перерабатывать в вашем местном центре утилизации.",
        "Бумагу и картон сортируйте отдельно от органических отходов.",
        "Электронные устройства утилизируйте через специальные пункты сбора."
    ]
    embed = nextcord.Embed(title='Как способствовать переработки мусора?', description = f'{recycling_tips}')
    await ctx.send(embed=embed)



@bot.slash_command(name='renewable', description='Информация о возобновляемых источниках энергии')
async def renewable(ctx):
    info = [

        "Солнечная энергия: Использование солнечных панелей для производства электроэнергии.",
        "Ветровая энергия: Генерация энергии с помощью ветровых турбин.",
        "Гидроэнергия: Использование силы воды для генерации электроэнергии.",
        'Геотермальная энергия: Использование тепла исходящего из недр Земли.',
        'Биоэнергия: Органические материалы, такие как древесина, сельскохозяйственные отходы и биоразлагаемые продукты.'
    ]
    
    embed = nextcord.Embed(title='Информация о возобновляемых источниках энергии', description = f'{info}')
    await ctx.send(embed = embed)


@bot.slash_command (name='sustainable_living', description='Советы по устойчивому образу жизни')
async def sustainable_living(ctx):
    tips = [

        "Покупайте продукцию местного производства, чтобы уменьшить транспортные выбросы.",
        "Сокращайте потребление воды, используя водосберегающие устройства.",
        "Переходите на экологически чистые средства для уборки."
        "Общественный транспорт: Используйте общественный транспорт, чтобы сократить выбросы CO₂.",
        "Устойчивые материалы: Используйте экологически чистые строительные материалы и энергоэффективные технологии при ремонте или строительстве.",
        'Волонтерство: Станьте волонтером в организациях, работающих над охраной окружающей среды.'


    ]
    embed = nextcord.Embed(title = 'Советы по устойчивому образу жизни', description = f'{tips}')
    await ctx.send(embed = embed)

bot.run('your_bot_token')

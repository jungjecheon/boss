import asyncio
import discord

import datetime

import threading

client = discord.Client()

channel = ''

gigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
gudeTIme= datetime.datetime.now()+datetime.timedelta(days=365)
ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
arTime= datetime.datetime.now()+datetime.timedelta(days=365)
jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
redTime= datetime.datetime.now()+datetime.timedelta(days=365)
sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)

tmp_gigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_gudeTIme= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_arTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_redTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)

gigamTimeString = '99:99:99'
gudeTimeString = '99:99:99'
ifTimeString = '99:99:99'
mayoTimeString = '99:99:99'
pinyxTimeString = '99:99:99'
dehugTimeString = '99:99:99'
sedeTimeString = '99:99:99'
sede2TimeString = '99:99:99'
jungdeTimeString = '99:99:99'
dongdeTimeString = '99:99:99'
arTimeString = '99:99:99'
jakTimeString = '99:99:99'
kapaTimeString = '99:99:99'
warmTimeString = '99:99:99'
deathTimeString = '99:99:99'
curchTimeString = '99:99:99'
greenTimeString = '99:99:99'
redTimeString = '99:99:99'
sanduTimeString = '99:99:99'

tmp_gigamTimeString = ''
tmp_gudeTimeString = ''
tmp_ifTimeString = ''
tmp_mayoTimeString = ''
tmp_pinyxTimeString = ''
tmp_dehugTimeString = ''
tmp_sedeTimeString = ''
tmp_sede2TimeString = ''
tmp_jungdeTimeString = ''
tmp_dongdeTimeString = ''
tmp_arTimeString = ''
tmp_jakTimeString = ''
tmp_kapaTimeString = ''
tmp_warmTimeString = ''
tmp_deathTimeString = ''
tmp_curchTimeString = ''
tmp_greenTimeString = ''
tmp_redTimeString = ''
tmp_sanduTimeString = ''

gigamFlag = False
gudeFlag = False
ifFlag = False
mayoFlag = False
pinyxFlag = False
dehugFlag = False
sedeFlag = False
sede2Flag = False
jungdeFlag = False
dongdeFlag = False
arFlag = False
jakFlag = False
kapaFlag = False
warmFlag = False
deathFlag = False
curchFlag = False
greenFlag = False
redFlag = False
sanduFlag = False

nowTimeString = '1'

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "여기에 입력 하세요."

async def my_background_task():
    await client.wait_until_ready()

    global channel
    global nowTimeString

    global gigamTime
    global gudeTIme
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time
    global jungdeTime
    global dongdeTime
    global arTime
    global jakTime
    global kapaTime
    global warmTime
    global deathTime
    global curchTime
    global greenTime
    global redTime
    global sanduTime
    
    global gigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString
    global jungdeTimeString
    global dongdeTimeString
    global arTimeString
    global jakTimeString
    global kapaTimeString
    global warmTimeString
    global deathTimeString
    global curchTimeString
    global greenTimeString
    global redTimeString
    global sanduTimeString

    global tmp_gigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString
    global tmp_jungdeTimeString
    global tmp_dongdeTimeString
    global tmp_arTimeString
    global tmp_jakTimeString
    global tmp_kapaTimeString
    global tmp_warmTimeString
    global tmp_deathTimeString
    global tmp_curchTimeString
    global tmp_greenTimeString
    global tmp_redTimeString
    global tmp_sanduTimeString

    global gigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag
    global jungdeFlag
    global dongdeFlag
    global arFlag
    global jakFlag
    global kapaFlag
    global warmFlag
    global deathFlag
    global curchFlag
    global greenFlag
    global redFlag
    global sanduFlag

    
    while not client.is_closed:
        now = datetime.datetime.now()
        priv = now+datetime.timedelta(minutes=1)
        privTimeString = priv.strftime('%H:%M:%S')
        nowTimeString = now.strftime('%H:%M:%S')
        #print('loop check ' + gigamTime.strftime('%H:%M:%S') + ' ' + nowTimeString + ' ' + privTimeString)

        if channel != '':


            
            if gigamTime <= now:
                gigamFlag = False
                tmp_gigamTime = gigamTime
                gigamTimeString = '99:99:99'
                gigamTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '기감 탐 입니다.')
                
            if gudeTIme <= now:
                gudeFlag = False
                tmp_gudeTime = gudeTime
                gudeTimeString = '99:99:99'
                gudeTIme = now+datetime.timedelta(days=365)
                await client.send_message(channel, '거드 탐 입니다.')

            if ifTime <= now:
                ifFlag = False
                tmp_ifTime = ifTime
                ifTimeString = '99:99:99'
                ifTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '이프 탐 입니다.')

            if mayoTime <= now:
                mayoFlag = False
                tmp_mayoTime = mayoTime
                mayoTimeString = '99:99:99'
                mayoTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '마요 탐 입니다.')

            if pinyxTime <= now:
                pinyxFlag = False
                tmp_pinyxTime = pinyxTime
                pinyxTimeString = '99:99:99'
                pinyxTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '피닉 탐 입니다.')

            if dehugTime <= now:
                dehugFlag = False
                tmp_dehugTime = dehugTime
                dehugTimeString = '99:99:99'
                dehugTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '대흑 탐 입니다.')

            if sedeTime <= now:
                sedeFlag = False
                tmp_sedeTime = sedeTime
                sedeTimeString = '99:99:99'
                sedeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '서드1 탐 입니다.')

            if sede2Time <= now:
                sede2Flag = False
                tmp_sede2Time = sede2Time
                sede2TimeString = '99:99:99'
                sede2Time = now+datetime.timedelta(days=365)
                await client.send_message(channel, '서드2 탐 입니다.')

            if jungdeTime <= now:
                jungdeFlag = False
                tmp_jungdeTime = jungdeTime
                jungdeTimeString = '99:99:99'
                jungdeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '중드 탐 입니다.')

            if dongdeTime <= now:
                dongdeFlag = False
                tmp_dongdeTime = dongdeTime
                dongdeTimeString = '99:99:99'
                dongdeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '동드 탐 입니다.')

            if arTime <= now:
                arFlag = False
                tmp_arTime = arTime
                arTimeString = '99:99:99'
                arTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '아르 탐 입니다.')

            if jakTime <= now:
                jakFlag = False
                tmp_jakTime = jakTime
                jakTimeString = '99:99:99'
                jakTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '자크 탐 입니다.')

            if kapaTime <= now:
                kapaFlag = False
                tmp_kapaTime = kapaTime
                kapaTimeString = '99:99:99'
                kapaTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '카파 탐 입니다.')

            if warmTime <= now:
                warmFlag = False
                tmp_warmTime = warmTime
                warmTimeString = '99:99:99'
                warmTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '웜 탐 입니다.')

            if deathTime <= now:
                deathFlag = False
                tmp_deathTime = deathTime
                deathTimeString = '99:99:99'
                deathTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '데스 탐 입니다.')

            if curchTime <= now:
                curchFlag = False
                tmp_curchTime = curchTime
                curchTimeString = '99:99:99'
                curchTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '커츠 탐 입니다.')

            if greenTime <= now:
                greenFlag = False
                tmp_greenTime = greenTime
                greenTimeString = '99:99:99'
                greenTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '질풍 탐 입니다.')

            if redTime <= now:
                redFlag = False
                tmp_redTime = redTime
                redTimeString = '99:99:99'
                redTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '광풍 탐 입니다.')

            if sanduTime <= now:
                sanduFlag = False
                tmp_sanduTime = redTime
                sanduTimeString = '99:99:99'
                sanduTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '산두 탐 입니다.')



            if gigamTime <= priv:
                if gigamFlag == False:
                    gigamFlag = True
                    await client.send_message(channel, '기감 1분 전 입니다.')
                
            if gudeTIme <= priv:
                if gudeFlag == False:
                    gudeFlag = True
                    await client.send_message(channel, '거드 1분 전 입니다.')

            if ifTime <= priv:
                if ifFlag == False:
                    ifFlag = True
                    await client.send_message(channel, '이프 1분 전 입니다.')

            if mayoTime <= priv:
                if mayoFlag == False:
                    mayoFlag = True
                    await client.send_message(channel, '마요 1분 전 입니다.')

            if pinyxTime <= priv:
                if pinyxFlag == False:
                    pinyxFlag = True
                    await client.send_message(channel, '피닉 1분 전 입니다.')

            if dehugTime <= priv:
                if dehugFlag == False:
                    dehugFlag = True
                    await client.send_message(channel, '대흑 1분 전 입니다.')

            if sedeTime <= priv:
                if sedeFlag == False:
                    sedeFlag = True
                    await client.send_message(channel, '서드1 1분 전 입니다.')

            if sede2Time <= priv:
                if sede2Flag == False:
                    sede2Flag = True
                    await client.send_message(channel, '서드2 1분 전 입니다.')

            if jungdeTime <= priv:
                if jungdeFlag == False:
                    jungdeFlag = True
                    await client.send_message(channel, '중드 1분 전 입니다.')

            if dongdeTime <= priv:
                if dongdeFlag == False:
                    dongdeFlag = True
                    await client.send_message(channel, '동드 1분 전 입니다.')

            if arTime <= priv:
                if arFlag == False:
                    arFlag = True
                    await client.send_message(channel, '아르 1분 전 입니다.')

            if jakTime <= priv:
                if jakFlag == False:
                    jakFlag = True
                    await client.send_message(channel, '자크 1분 전 입니다.')

            if kapaTime <= priv:
                if kapaFlag == False:
                    kapaFlag = True
                    await client.send_message(channel, '카파 1분 전 입니다.')

            if warmTime <= priv:
                if warmFlag == False:
                    warmFlag = True
                    await client.send_message(channel, '웜 1분 전 입니다.')

            if deathTime <= priv:
                if deathFlag == False:
                    deathFlag = True
                    await client.send_message(channel, '데스 1분 전 입니다.')

            if curchTime <= priv:
                if curchFlag == False:
                    curchFlag = True
                    await client.send_message(channel, '커츠 1분 전 입니다.')

            if greenTime <= priv:
                if greenFlag == False:
                    greenFlag = True
                    await client.send_message(channel, '질풍 1분 전 입니다.')

            if redTime <= priv:
                if redFlag == False:
                    redFlag = True
                    await client.send_message(channel, '광풍 1분 전 입니다.')

            if sanduTime <= priv:
                if sanduFlag == False:
                    sanduFlag = True
                    await client.send_message(channel, '광풍 1분 전 입니다.')
   
            
        await asyncio.sleep(1) # task runs every 60 seconds
        


async def joinVoiceChannel():
    channel = client.get_channel("일반")
    await client.join_voice_channel(channel)
    

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")

    #await joinVoiceChannel()
    
    client.loop.create_task(my_background_task())
    
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))

    

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    global channel
    global nowTimeString

    global gigamTime
    global gudeTime
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time
    global jungdeTime
    global dongdeTime
    global arTime
    global jakTime
    global kapaTime
    global warmTime
    global deathTime
    global curchTime
    global greenTime
    global redTime
    global sanduTime
    
    global gigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString
    global jungdeTimeString
    global dongdeTimeString
    global arTimeString
    global jakTimeString
    global kapaTimeString
    global warmTimeString
    global deathTimeString
    global curchTimeString
    global greenTimeString
    global redTimeString
    global sanduTimeString

    global tmp_gigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString
    global tmp_jungdeTimeString
    global tmp_dongdeTimeString
    global tmp_arTimeString
    global tmp_jakTimeString
    global tmp_kapaTimeString
    global tmp_warmTimeString
    global tmp_deathTimeString
    global tmp_curchTimeString
    global tmp_greenTimeString
    global tmp_redTimeString
    global tmp_sanduTimeString

    global gigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag
    global jungdeFlag
    global dongdeFlag
    global arFlag
    global jakFlag
    global kapaFlag
    global warmFlag
    global deathFlag
    global curchFlag
    global greenFlag
    global redFlag
    global sanduFlag

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    
    modify = ''
    try:
        hello = message.content
        length = len(hello)     # UTF-8로 인코딩 했을 때 바이트 수를 구함
        print(hello)
        print(length)
    
        if length == 11:
            hours = hello[6:8]
            minutes = hello[9:11]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 12:
            hours = hello[7:9]
            minutes = hello[10:12]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 10:
            hours = hello[5:7]
            minutes = hello[8:10]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        else :
            now = datetime.datetime.now()
            nowTimeString = now.strftime('%H:%M:%S')
    except:
        print('exception');
        now = datetime.datetime.now()
        nowTimeString = now.strftime('%H:%M:%S')


    if message.content.startswith('!기감 컷'):
        gigamFlag = False
        gigamTime = nextTime = now+datetime.timedelta(hours=1)
        tmp_gigamTimeString = gigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 기감 ' + gigamTimeString)
        
    if message.content.startswith('!거드 컷'):
        gudeFlag = False
        gudeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 거드 ' + gudeTimeString)

    if message.content.startswith('!이프 컷'):
        ifFlag = False
        ifTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 이프 ' + ifTimeString)

    if message.content.startswith('!마요 컷'):
        mayoFlag = False
        mayoTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 마요 ' + mayoTimeString)

    if message.content.startswith('!피닉 컷'):
        pinyxFlag = False
        pinyxTime = nextTime = now+datetime.timedelta(hours=7)
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

    if message.content.startswith('!대흑 컷'):
        dehugFlag = False
        dehugTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 대흑 ' + dehugTimeString)

    if message.content.startswith('!서드1 컷'):
        sedeFlag = False
        sedeTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드1 ' + sedeTimeString)

    if message.content.startswith('!서드2 컷'):
        sede2Flag = False
        sede2Time = nextTime = now+datetime.timedelta(hours=2)
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드2 ' + sede2TimeString)

    if message.content.startswith('!중드 컷'):
        jungdeFlag = False
        jungdeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_jungdeTimeString = jungdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 중드 ' + jungdeTimeString)

    if message.content.startswith('!동드 컷'):
        dongdeFlag = False
        dongdeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_dongdeTimeString = dongdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 동드 ' + dongdeTimeString)

    if message.content.startswith('!아르 컷'):
        arFlag = False
        arTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_arTimeString = arTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 아르 ' + arTimeString)

    if message.content.startswith('!자크 컷'):
        jakFlag = False
        nextTime = now+datetime.timedelta(hours=3)
        tmp_jakTimeString = jakTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 자크 ' + jakTimeString)

    if message.content.startswith('!카파 컷'):
        kapaFlag = False
        kapaTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_kapaTimeString = kapaTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 카파 ' + kapaTimeString)

    if message.content.startswith('!웜 컷'):
        warmFlag = False
        warmTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_warmTimeString = warmTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 웜 ' + warmTimeString)

    if message.content.startswith('!데스 컷'):
        deathFlag = False
        deathTime = nextTime = now+datetime.timedelta(hours=7)
        tmp_deathTimeString = deathTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 데스 ' + deathTimeString)

    if message.content.startswith('!커츠 컷'):
        curchFlag = False
        curchTime = nextTime = now+datetime.timedelta(hours=10)
        tmp_curchTimeString = curchTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 커츠 ' + curchTimeString)

    if message.content.startswith('!질풍 컷'):
        greenFlag = False
        greenTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_greenTimeString = greenTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 질풍 ' + greenTimeString)

    if message.content.startswith('!광풍 컷'):
        redFlag = False
        redTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_redTimeString = redTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 광풍 ' + redTimeString)

    if message.content.startswith('!산두 컷'):
        sanduFlag = False
        sanduTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_sanduTimeString = sanduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 산두 ' + sanduTimeString)
        


    if message.content.startswith('!기감 젠'):
        gigamFlag = False
        gigamTime = nextTime = now
        tmp_gigamTimeString = gigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 기감 ' + gigamTimeString)
        
    if message.content.startswith('!거드 젠'):
        gudeFlag = False
        gudeTIme = nextTime = now
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 거드 ' + gudeTimeString)

    if message.content.startswith('!이프 젠'):
        ifFlag = False
        ifTime = nextTime = now
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 이프 ' + ifTimeString)

    if message.content.startswith('!마요 젠'):
        mayoFlag = False
        mayoTime = nextTime = now
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 마요 ' + mayoTimeString)

    if message.content.startswith('!피닉 젠'):
        pinyxFlag = False
        pinyxTime = nextTime = now
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

    if message.content.startswith('!대흑 젠'):
        dehugFlag = False
        dehugTime = nextTime = now
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 대흑 ' + dehugTimeString)

    if message.content.startswith('!서드1 젠'):
        sedeFlag = False
        sedeTime = nextTime = now
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드1 ' + sedeTimeString)

    if message.content.startswith('!서드2 젠'):
        sede2Flag = False
        sede2Time = nextTime = now
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드2 ' + sede2TimeString)

    if message.content.startswith('!중드 젠'):
        jungdeFlag = False
        jungdeTime = nextTime = now
        tmp_jungdeTimeString = jungdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 중드 ' + jungdeTimeString)

    if message.content.startswith('!동드 젠'):
        dongdeFlag = False
        dongdeTime = nextTime = now
        tmp_dongdeTimeString = dongdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 동드 ' + dongdeTimeString)

    if message.content.startswith('!아르 젠'):
        arFlag = False
        arTime = nextTime = now
        tmp_arTimeString = arTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 아르 ' + arTimeString)

    if message.content.startswith('!자크 젠'):
        jakFlag = False
        jakTime = nextTime = now
        tmp_jakTimeString = jakTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 자크 ' + jakTimeString)

    if message.content.startswith('!카파 젠'):
        kapaFlag = False
        kapaTime = nextTime = now
        tmp_kapaTimeString = kapaTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 카파 ' + kapaTimeString)

    if message.content.startswith('!웜 젠'):
        warmFlag = False
        warmTime = nextTime = now
        tmp_warmTimeString = warmTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 웜 ' + warmTimeString)

    if message.content.startswith('!데스 젠'):
        deathFlag = False
        deathTime = nextTime = now
        tmp_deathTimeString = deathTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 데스 ' + deathTimeString)

    if message.content.startswith('!커츠 젠'):
        curchFlag = False
        curchTime = nextTime = now
        tmp_curchTimeString = curchTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 커츠 ' + curchTimeString)

    if message.content.startswith('!질풍 젠'):
        greenFlag = False
        greenTime = nextTime = now
        tmp_greenTimeString = greenTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 질풍 ' + greenTimeString)

    if message.content.startswith('!광풍 젠'):
        redFlag = False
        redTime = nextTime = now
        tmp_redTimeString = redTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 광풍 ' + redTimeString)
    
    if message.content.startswith('!산두 젠'):
        sanduFlag = False
        sanduTime = nextTime = now
        tmp_sanduTimeString = sanduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 산두 ' + sanduTimeString)




    try:
        if message.content.startswith('!거드 멍'):
            gudeFlag = False
            now = tmp_gudeTime
            gudeTIme = nextTime = now+datetime.timedelta(hours=3)
            gudeTimeString = gudeTIme.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 거드 ' + gudeTimeString)

        if message.content.startswith('!이프 멍'):
            ifFlag = False
            now = tmp_ifTime
            ifTime = nextTime = now+datetime.timedelta(hours=2)
            ifTimeString = ifTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 이프 ' + ifTimeString)

        if message.content.startswith('!마요 멍'):
            mayoFlag = False
            now = tmp_mayoTime
            mayoTime = nextTime = now+datetime.timedelta(hours=3)
            mayoTimeString = mayoTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 마요 ' + mayoTimeString)

        if message.content.startswith('!피닉 멍'):
            pinyxFlag = False
            now = tmp_pinyxTime
            pinyxTime = nextTime = now+datetime.timedelta(hours=7)
            pinyxTimeString = pinyxTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

        if message.content.startswith('!웜 멍'):
            warmFlag = False
            now = tmp_warmTime
            warmTime = nextTime = now+datetime.timedelta(hours=2)
            warmTimeString = warmTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 웜 ' + warmTimeString)

        if message.content.startswith('!데스 멍'):
            deathFlag = False
            now = tmp_deathTime
            deathTime = nextTime = now+datetime.timedelta(hours=2)
            deathTimeString = deathTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 데스 ' + deathTimeString)

        if message.content.startswith('!커츠 멍'):
            curchFlag = False
            now = tmp_curchTime
            curchTime = nextTime = now+datetime.timedelta(hours=2)
            curchTimeString = curchTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 커츠 ' + curchTimeString)

        if message.content.startswith('!질풍 멍'):
            greenFlag = False
            now = tmp_greenTime
            greenTime = nextTime = now+datetime.timedelta(hours=2)
            greenTimeString = greenTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 질풍 ' + greenTimeString)

        if message.content.startswith('!광풍 멍'):
            redFlag = False
            now = tmp_redTime
            redTime = nextTime = now+datetime.timedelta(hours=2)
            redTimeString = redTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 광풍 ' + redTimeString)
    except:
        await client.send_message(channel, '입력 오류 ')


        

    if message.content.startswith('!불러오기'):
        file = open("D:\my_bot.db", 'r')
        
        while True:
            line = file.readline();
            
            if not line: break
            
            #await client.send_message(channel, line)
            
            if (line.startswith(' - 기감 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gigamTime = now2
                gigamTimeString = gigamTime.strftime('%H:%M:%S')

            if (line.startswith(' - 거드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gudeTime = now2
                gudeTimeString = gudeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 이프 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                ifTime = now2
                ifTimeString = ifTime.strftime('%H:%M:%S')

            if (line.startswith(' - 마요 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                mayoTime = now2
                mayoTimeString = mayoTime.strftime('%H:%M:%S')

            if (line.startswith(' - 피닉 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                pinyxTime = now2
                pinyxTimeString = pinyxTime.strftime('%H:%M:%S')

            if (line.startswith(' - 대흑 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                dehugTime = now2
                dehugTimeString = dehugTime.strftime('%H:%M:%S')

            if (line.startswith(' - 서드1 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sedeTime = now2
                sedeTimeString = sedeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 서드2 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sede2Time = now2
                sede2TimeString = sede2Time.strftime('%H:%M:%S')

            if (line.startswith(' - 중드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jungdeTime = now2
                jungdeTimeString = jungdeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 동드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                dongdeTime = now2
                dongdeTimeString = dongdeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 아르 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                arTime = now2
                arTimeString = arTime.strftime('%H:%M:%S')

            if (line.startswith(' - 자크 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jakTime = now2
                jakTimeString = jakTime.strftime('%H:%M:%S')

            if (line.startswith(' - 카파 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                kapaTime = now2
                kapaTimeString = kapaTime.strftime('%H:%M:%S')

            if (line.startswith(' - 웜 : ')):
                hours = line[7:9]
                minutes = line[10:12]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                warmTime = now2
                warmTimeString = warmTime.strftime('%H:%M:%S')

            if (line.startswith(' - 데스 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                deathTime = now2
                deathTimeString = deathTime.strftime('%H:%M:%S')

            if (line.startswith(' - 커츠 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                curchTime = now2
                curchTimeString = curchTime.strftime('%H:%M:%S')

            if (line.startswith(' - 질풍 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                greenTime = now2
                greenTimeString = greenTime.strftime('%H:%M:%S')

            if (line.startswith(' - 광풍 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                redTime = now2
                redTimeString = redTime.strftime('%H:%M:%S')

            if (line.startswith(' - 산두 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sanduTime = now2
                sanduTimeString = sanduTime.strftime('%H:%M:%S')
                
        file.close()
        await client.send_message(channel, '불러오기 완료')
    

        

    if message.content.startswith('!보스탐'):

        datelist=[gigamTimeString, gudeTimeString, ifTimeString, mayoTimeString, pinyxTimeString, dehugTimeString,
                  sedeTimeString, sede2TimeString, jungdeTimeString, dongdeTimeString, arTimeString, jakTimeString,
                  kapaTimeString, warmTimeString, deathTimeString, curchTimeString, redTimeString, greenTimeString, sanduTimeString]

        information = '----- 보스탐 정보 -----\n'
        
        for timestring in sorted(datelist):
            #print(timestring)
        
            if timestring == gigamTimeString:
                if gigamTimeString != '99:99:99':
                    information += ' - 기감 : ' + gigamTimeString + '\n'

            elif timestring == gudeTimeString:
                if gudeTimeString != '99:99:99':
                    information += ' - 거드 : ' + gudeTimeString + '\n'

            elif timestring == ifTimeString:     
                if ifTimeString != '99:99:99':
                    information += ' - 이프 : ' + ifTimeString + '\n'

            elif timestring == mayoTimeString:        
                if mayoTimeString != '99:99:99':
                    information += ' - 마요 : ' + mayoTimeString + '\n'

            elif timestring == pinyxTimeString:        
                if pinyxTimeString != '99:99:99':
                    information += ' - 피닉 : ' + pinyxTimeString + '\n'

            elif timestring == dehugTimeString:       
                if dehugTimeString != '99:99:99':
                    information += ' - 대흑 : ' + dehugTimeString + '\n'

            elif timestring == sedeTimeString:       
                if sedeTimeString != '99:99:99':
                    information += ' - 서드1 : ' + sedeTimeString + '\n'
                    
            elif timestring == sede2TimeString:        
                if sede2TimeString != '99:99:99':
                    information += ' - 서드2 : ' + sede2TimeString + '\n'

            elif timestring == jungdeTimeString:     
                if jungdeTimeString != '99:99:99':
                    information += ' - 중드 : ' + jungdeTimeString + '\n'

            elif timestring == dongdeTimeString: 
                if dongdeTimeString != '99:99:99':
                    information += ' - 동드 : ' + dongdeTimeString + '\n'

            elif timestring == arTimeString: 
                if arTimeString != '99:99:99':
                    information += ' - 아르 : ' + arTimeString + '\n'

            elif timestring == jakTimeString:     
                if jakTimeString != '99:99:99':
                    information += ' - 자크 : ' + jakTimeString + '\n'

            elif timestring == kapaTimeString:     
                if kapaTimeString != '99:99:99':
                    information += ' - 카파 : ' + kapaTimeString + '\n'

            elif timestring == warmTimeString:     
                if warmTimeString != '99:99:99':
                    information += ' - 웜 : ' + warmTimeString + '\n'

            elif timestring == deathTimeString: 
                if deathTimeString != '99:99:99':
                    information += ' - 데스 : ' + deathTimeString + '\n'

            elif timestring == curchTimeString:    
                if curchTimeString != '99:99:99':
                    information += ' - 커츠 : ' + curchTimeString + '\n'

            elif timestring == redTimeString:     
                if redTimeString != '99:99:99':
                    information += ' - 광풍 : ' + redTimeString + '\n'

            elif timestring == greenTimeString:     
                if greenTimeString != '99:99:99':
                    information += ' - 질풍 : ' + greenTimeString + '\n'
                    
            elif timestring == sanduTimeString: 
                if sanduTimeString != '99:99:99':
                    information += ' - 산두 : ' + sanduTimeString + '\n'
        



        if gigamTimeString == '99:99:99':
            information += ' - 기감 입력 안됨\n'
        if gudeTimeString == '99:99:99':
            information += ' - 거드 입력 안됨\n'
        if ifTimeString == '99:99:99':
            information += ' - 이프 입력 안됨\n'
        if mayoTimeString == '99:99:99':
            information += ' - 마요 입력 안됨\n'
        if pinyxTimeString == '99:99:99':
            information += ' - 피닉 입력 안됨\n'
        if dehugTimeString == '99:99:99':
            information += ' - 대흑 입력 안됨\n'
        if sedeTimeString == '99:99:99':
            information += ' - 서드1 입력 안됨\n'        
        if sede2TimeString == '99:99:99':
            information += ' - 서드2 입력 안됨\n'
        if jungdeTimeString == '99:99:99':
            information += ' - 중드 입력 안됨\n'
        if dongdeTimeString == '99:99:99':
            information += ' - 동드 입력 안됨\n'
        if arTimeString == '99:99:99':
            information += ' - 아르 입력 안됨\n'    
        if jakTimeString == '99:99:99':
            information += ' - 자크 입력 안됨\n'
        if kapaTimeString == '99:99:99':
            information += ' - 카파 입력 안됨\n'
        if warmTimeString == '99:99:99':
            information += ' - 웜 입력 안됨\n'
        if deathTimeString == '99:99:99':
            information += ' - 데스 입력 안됨\n'
        if curchTimeString == '99:99:99':
            information += ' - 커츠 입력 안됨\n'
        if redTimeString == '99:99:99':
            information += ' - 광풍 입력 안됨\n'
        if greenTimeString == '99:99:99':
            information += ' - 질풍 입력 안됨\n'
        if sanduTimeString == '99:99:99':
            information += ' - 산두 입력 안됨\n'

        await client.send_message(channel, information)

        file = open("D:\my_bot.db", 'w')
        file.write(information);
        file.close()



    if message.content.startswith('!현재시간'):
        await client.send_message(channel, datetime.datetime.now().strftime('%H:%M:%S'))

client.run(token)


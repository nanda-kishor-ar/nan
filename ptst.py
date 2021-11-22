import requests , json

token = ' '

url = f'https://api.telegram.org/bot{token}/getUpdates'
url1 = 'https://pokeapi.co/api/v2/pokemon?limit=9999'
a = requests.get(url1)
a3= a.json()
a4 = a3['results']
pk =[]

for dic in range(len(a4)):
    pk.append(a4[dic]['name'])

    

uid1 =0
def getupdate(offset , limit=50 , timeout=0 , a_w =[]):
    params1 = {'offset': offset,
                'limit' : limit,
                'timeout' : timeout,
                'allowed_updates' :a_w}
    r=requests.get(url , params = params1)
    r1 = r.json()
    return r1

def pokepic(name):
    if name in pk:
        pic = requests.get(f'https://img.pokemondb.net/artwork/large/{name}.jpg')
        return pic
    else:
        pass
    return None
def sendmess(mssg , cid)   :     
    r= requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={cid}'+f'&photo=https://img.pokemondb.net/artwork/large/{mssg}.jpg'+f'&caption={mssg}')
    print(r)

def main():
    global uid1
    u=getupdate(offset = -2 , a_w=["message"])
    #print(u)
    uid = u['result'][-1]['update_id']
    if uid == uid1:
        pass
    else:
        if 'text' in u['result'][-1]['message'] :
            p = u['result'][-1]['message']['text']
            cid = cid = u['result'][-1]['message']['chat']['id']
            p1 = pokepic(p)
            try :
                if p1.status_code == 200:
                    sendmess(p , cid)
            except:
                pass
        uid1 = uid
    
while True:  
   main()
   

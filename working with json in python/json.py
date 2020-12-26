"""
orders of json

json.dump(name1 , name2) =>  ساخت فایل جیسونی به اسم نام۲ و ریخت اطلاعات پایتونی فایل با نام۱

json.dumps(name1 , name2) => اگر اطلاعات در فایل۱ به صورت استرینگ بود از این متود استفاده میشود

data = json.load(name) =>اطلاعات جیسونی در فایل را تبدیل به اطلاعات پایتونی میکند و در متغیر دیتا ذخیره میکند

data = json.loads(name) => اگر بخواهیم اطلاعات به صورت استرینگ باشد

json.dump(name1 , name2 , indent=2) => مقدار ایندنت میزان تو رفتگی را نشان میدهد

"""


from urllib.request import urlopen
from json import dumps , loads


url = 'https://api.exchangeratesapi.io/latest'

with urlopen(url) as f :
    data = f.read()

pdata = loads(data)

with open('curency.json' 'w') as c :
    dump(pdata , c , indent=2)

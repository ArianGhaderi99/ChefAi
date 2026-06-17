# 🍳 Chef AI

یک دستیار هوشمند آشپزی که با استفاده از هوش مصنوعی و مواد اولیه موجود در خانه، غذاهای قابل تهیه را پیشنهاد می‌دهد.

---

## ✨ امکانات

* 🥘 پیشنهاد غذا بر اساس مواد اولیه
* 📖 نمایش دستور پخت کامل
* ⏱ نمایش زمان تقریبی آماده‌سازی
* 📊 نمایش درجه سختی هر غذا
* 🎨 رابط کاربری مدرن و کاملاً ریسپانسیو
* 🤖 اتصال به مدل‌های هوش مصنوعی از طریق OpenRouter

---

## 📸 تصاویر پروژه

### صفحه اصلی

![Home Page](https://github.com/ArianGhaderi99/ChefAi/blob/main/Screenhome.png)

---

### بخش Chef AI

![Chef AI](https://github.com/ArianGhaderi99/ChefAi/blob/main/Screenchefai.png)

---

## 🛠 تکنولوژی‌های استفاده شده

* Python
* Django
* HTML5
* CSS3
* JavaScript
* OpenRouter API

---

## 🚀 نصب و اجرا

ابتدا پروژه را Clone کنید:

```bash
git clone YOUR_REPOSITORY_URL
```

وارد پوشه پروژه شوید:

```bash
cd ChefAI
```

ساخت محیط مجازی:

```bash
python -m venv .venv
```

فعال‌سازی محیط مجازی:

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

اجرای مایگریشن‌ها:

```bash
python manage.py migrate
```

اجرای پروژه:

```bash
python manage.py runserver
```

---

## 🔑 تنظیم API

به دلایل امنیتی کلید API داخل ریپازیتوری قرار نگرفته است.

برای دریافت API Key:

1. وارد OpenRouter شوید.
2. یک API Key جدید بسازید.
3. مقدار کلید را داخل فایل تنظیمات پروژه قرار دهید.

نمونه:

```python
OPENROUTER_API_KEY = "YOUR_API_KEY"
```

همچنین مدل مورد استفاده:

```python
OPENROUTER_MODEL = "deepseek/deepseek-chat-v3-0324:free"
```

---

## 📂 ساختار پروژه

```text
chef/
├── services/
│   └── ai_service.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── chef-ai.html
│
├── static/
│   ├── css/
│   └── js/
│
├── views.py
├── urls.py
└── models.py
```

---

## 🤝 مشارکت

اگر ایده یا پیشنهادی برای بهبود پروژه دارید خوشحال می‌شوم Pull Request ارسال کنید.

---

## ⭐ حمایت

اگر این پروژه برای شما مفید بود، فراموش نکنید به آن Star بدهید.


# دليل نشر تطبيق A+Academy مجانًا

## الطرق المجانية لنشر التطبيق

### 1. نشر على Vercel (الأسهل والأفضل)

**الخطوات:**

1. **إنشاء حساب على Vercel:**
   - اذهب إلى https://vercel.com
   - سجل دخول باستخدام GitHub أو Google

2. **رفع الملفات:**
   - اضغط على "New Project"
   - اختر "Import Git Repository" أو ارفع الملفات مباشرة
   - ارفع مجلد `aplus_academy` كاملاً

3. **إعدادات النشر:**
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: `src/static`
   - Install Command: `pip install -r requirements.txt`

4. **متغيرات البيئة:**
   - أضف `FLASK_ENV=production`
   - أضف `SECRET_KEY=your_secret_key_here`

### 2. نشر على Railway

**الخطوات:**

1. **إنشاء حساب على Railway:**
   - اذهب إلى https://railway.app
   - سجل دخول باستخدام GitHub

2. **إنشاء مشروع جديد:**
   - اضغط على "New Project"
   - اختر "Deploy from GitHub repo"
   - ارفع الكود إلى GitHub أولاً

3. **إعدادات النشر:**
   - Railway سيكتشف Flask تلقائيًا
   - سيقوم بتثبيت المتطلبات من `requirements.txt`

### 3. نشر على Render

**الخطوات:**

1. **إنشاء حساب على Render:**
   - اذهب إلى https://render.com
   - سجل دخول باستخدام GitHub

2. **إنشاء Web Service:**
   - اضغط على "New +"
   - اختر "Web Service"
   - اربط مع GitHub repository

3. **إعدادات النشر:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python src/main.py`

## إعداد GitHub Repository

**لنشر التطبيق، ستحتاج أولاً لرفعه على GitHub:**

1. **إنشاء repository جديد على GitHub:**
   - اذهب إلى https://github.com
   - اضغط على "New repository"
   - اختر اسم للمشروع (مثل: aplus-academy)

2. **رفع الملفات:**
   ```bash
   cd aplus_academy
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/aplus-academy.git
   git push -u origin main
   ```

## ملفات مطلوبة للنشر

تأكد من وجود هذه الملفات في مجلد المشروع:

1. **requirements.txt** - قائمة المكتبات المطلوبة
2. **runtime.txt** - إصدار Python (اختياري)
3. **Procfile** - لبعض المنصات (اختياري)

## إزالة أي إشارات خارجية

تم تصميم التطبيق ليكون ملكيتك الخاصة بالكامل:
- لا توجد أي إشارات لمطور خارجي
- جميع الحقوق محفوظة لك
- يمكنك تعديل أي شيء في الكود
- لا توجد علامات مائية أو روابط خارجية

## نصائح مهمة

1. **احتفظ بنسخة احتياطية من الكود**
2. **قم بتغيير SECRET_KEY في الإنتاج**
3. **تأكد من أن جميع المتطلبات في requirements.txt**
4. **اختبر التطبيق محليًا قبل النشر**

## الدعم الفني

إذا واجهت أي مشاكل في النشر:
1. تحقق من logs المنصة
2. تأكد من أن جميع الملفات موجودة
3. تحقق من إعدادات البيئة

## رابط التطبيق بعد النشر

بعد النشر الناجح، ستحصل على رابط مثل:
- Vercel: `https://your-app-name.vercel.app`
- Railway: `https://your-app-name.up.railway.app`
- Render: `https://your-app-name.onrender.com`

هذا الرابط سيكون ملكك بالكامل ويمكنك مشاركته مع أي شخص.


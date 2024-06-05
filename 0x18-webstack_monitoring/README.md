0x18-webstack_monitoring
الخطوة الأولى: التسجيل في Datadog
افتح المتصفح وروح للموقع ده: https://app.datadoghq.com
اعمل حساب جديد لو معندكش واحد. لو عندك، سجل الدخول بحسابك.
الخطوة الثانية: تحميل وتثبيت الـ Datadog Agent على السيرفر web-01
افتح التيرمنال على السيرفر web-01.

نفذ الأوامر دي لتحميل وتثبيت الـ Datadog Agent:

bash
Copy code
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=YOUR_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
استبدل YOUR_API_KEY بمفتاح الـ API الخاص بيك اللي حناخده بعد شوية.

الخطوة الثالثة: إنشاء مفتاح API ومفتاح تطبيق
ارجع لموقع Datadog اللي فاتحته.
روح لـ API Keys تحت Integration.
انشئ مفتاح API جديد واعمله نسخ.
روح لـ Application Keys تحت Integration.
انشئ مفتاح تطبيق جديد واعمله نسخ برضو.
الخطوة الرابعة: نسخ ولصق مفاتيح Datadog في بروفايل المستخدم على Intranet
افتح الـ Intranet بتاعك.
ادخل على بروفايل المستخدم بتاعك.
الصق مفاتيح Datadog اللي انت نسختها (API Key و Application Key).
الخطوة الخامسة: التحقق من ظهور السيرفر web-01 في Datadog
افتح التيرمنال تاني على السيرفر web-01.

نفذ الأمر ده لتحديث اسم السيرفر (استبدل XX-web-01 بالاسم اللي عايزه):

bash
Copy code
hostnamectl set-hostname XX-web-01
أعد تشغيل الـ Datadog Agent بالأمر ده:

bash
Copy code
sudo systemctl restart datadog-agent
ارجع لموقع Datadog وشوف السيرفر تحت Infrastructure > Hosts. لازم تلاقي السيرفر web-01 بالاسم اللي انت حددته.

الخطوة السادسة: التحقق باستخدام الـ API
افتح التيرمنال على جهازك.

نفذ الأمر ده عشان تتأكد إن السيرفر ظاهر:

bash
Copy code
curl -X GET "https://api.datadoghq.com/api/v1/hosts" -H "Content-Type: application/json" -H "DD-API-KEY: YOUR_API_KEY" -H "DD-APPLICATION-KEY: YOUR_APP_KEY"
استبدل YOUR_API_KEY و YOUR_APP_KEY بالقيم اللي عندك.

لو ظهر السيرفر في الناتج، كده احنا تمام.

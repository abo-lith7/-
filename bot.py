import tweepy
import random
import os

# جلب المفاتيح من GitHub Secrets
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# التأكد من وجود المفاتيح
for key_name, key_value in [("API_KEY", API_KEY), ("API_SECRET", API_SECRET),
                            ("ACCESS_TOKEN", ACCESS_TOKEN), ("ACCESS_TOKEN_SECRET", ACCESS_TOKEN_SECRET)]:
    if not key_value:
        print(f"❌ {key_name} غير موجود")
        exit(1)

# المصادقة مع تويتر
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# قائمة التغريدات
tweets = [
    "🔮 تبحث عن مفسر أحلام موثوق وذو خبرة؟ الشيخ أبو ليان يقدم لك تحليلاً شرعياً ودقيقاً لرؤاك وأحلامك ✨\n📲 للتواصل مباشرة عبر واتساب: wa.me/+966536329403",
    "🌙 مفسر أحلام شرعي ومعروف بخبرته الطويلة. تواصل مع الشيخ أبو ليان ✅\n📲 wa.me/+966536329403",
    "✨ كثير يسألون عن مفسر أحلام موثوق، الشيخ أبو ليان يساعدك على فهم رؤاك بدقة وبطريقة شرعية 🌟\n📲 wa.me/+966536329403",
    "🔮 هل رأيت رؤيا وتريد تفسيرها؟ الشيخ أبو ليان، مفسر أحلام بخبرة سنين طويلة، يفسر لك بدقة ووضوح ✅\n📲 wa.me/+966536329403",
    "🌟 تبحث عن تفسير شرعي لرؤاك؟ مفسر الأحلام الشيخ أبو ليان يقدم لك أجوبة واضحة وموثوقة ✨\n📲 wa.me/+966536329403",
    "💫 كثير من الناس يثقون بمفسر الأحلام الشيخ أبو ليان لأنه يفسر الرؤى بالشرع والخبرة 🌙\n📲 wa.me/+966536329403",
    "🌙 عندك رؤيا محيرة؟ مفسر الأحلام الشيخ أبو ليان يفسرها لك بسهولة ووضوح ✨\n📲 wa.me/+966536329403",
    "🔮 لا تبحث كثيراً، مفسر الأحلام الموثوق أبو ليان يشرح لك رموز رؤاك بدقة عالية وشرعية ✅\n📲 wa.me/+966536329403",
    "🌟 إذا أردت تفسير رؤياك بطريقة شرعية صحيحة، مفسر الأحلام الشيخ أبو ليان هو الخيار الأفضل ✨\n📲 wa.me/+966536329403",
    "✨ آلاف الأشخاص يسألون عن مفسر أحلام موثوق، الشيخ أبو ليان يقدم التفسير بخبرة وصدق 🌙\n📲 wa.me/+966536329403"
]

# اختيار تغريدة عشوائية للنشر
tweet = random.choice(tweets)

# محاولة النشر
try:
    api.update_status(tweet)
    print("✅ تم نشر التغريدة بنجاح:", tweet)
except Exception as e:
    print("❌ خطأ في النشر:", e)

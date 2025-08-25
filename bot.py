import tweepy
import random
import os

# المفاتيح
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# قائمة التغريدات
tweets = [
    "🔮 تبحث عن مفسر أحلام موثوق وذو خبرة؟ الشيخ أبو ليان يقدم لك تفسيرًا شرعيًا دقيقًا لكل رؤاك وأحلامك ✨\n📲 تواصل مباشرة: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام #رؤى",
    
    "🌙 هل حلمت برؤيا محيرة وتريد فهمها بطريقة شرعية؟ مفسر الأحلام الشيخ أبو ليان يساعدك على التحليل الصحيح والواضح ✅\n📲 تواصل الآن: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام",
    
    "✨ كثير من الناس يسألون عن مفسر أحلام موثوق، الشيخ أبو ليان يقدم شرحًا واضحًا لكل الرموز والأحلام بطريقة شرعية 🌟\n📲 رقم مباشر: wa.me/+966536329403\n#رؤى #مفسر_أحلام",
    
    "🔮 لديك حلم تريد تفسيره بدقة وصدق؟ الشيخ أبو ليان مفسر أحلام ذو خبرة طويلة يقدم لك التحليل الشرعي الصحيح ✅\n📲 تواصل عبر واتساب: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام",
    
    "🌟 تبحث عن تفسير شرعي لرؤاك؟ مفسر الأحلام الشيخ أبو ليان يقدم لك الإجابة الموثوقة لكل الأحلام ✨\n📲 للتواصل: wa.me/+966536329403\n#رؤى #مفسر_أحلام",
    
    "💫 آلاف الأشخاص يثقون بمفسر الأحلام الشيخ أبو ليان لأنه يفسر الرؤى بالشرع والخبرة 🌙\n📲 تواصل الآن: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام #رؤى",
    
    "🌙 هل رأيت رؤيا محيرة؟ مفسر الأحلام الشيخ أبو ليان يفسرها بسهولة ووضوح مع توضيح الرموز بدقة شرعية ✨\n📲 رقم مباشر: wa.me/+966536329403\n#مفسر_أحلام #رؤى",
    
    "🔮 لا تبحث كثيرًا، مفسر الأحلام أبو ليان يشرح لك كل رموز رؤاك بدقة عالية وطريقة شرعية ✅\n📲 تواصل عبر واتساب: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام",
    
    "🌟 إذا أردت تفسير رؤياك بطريقة شرعية صحيحة، مفسر الأحلام الشيخ أبو ليان هو الخيار الأمثل ✨\n📲 للتواصل: wa.me/+966536329403\n#رؤى #مفسر_أحلام",
    
    "✨ آلاف الأشخاص يسألون عن مفسر أحلام موثوق، هذا هو الشيخ أبو ليان، يقدم لك التحليل الشرعي بدقة وصدق 🌙\n📲 تواصل عبر واتساب: wa.me/+966536329403\n#تفسير_الأحلام #مفسر_أحلام"
]
# سجل التغريدات المنشورة
log_file = "log.txt"
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        posted = [line.strip() for line in f.readlines()]
else:
    posted = []

# التغريدات المتاحة للنشر
available = [t for t in tweets if t not in posted]

if not available:
    posted = []
    available = tweets.copy()

tweet = random.choice(available)

try:
    response = client.create_tweet(text=tweet)
    print("✅ تم النشر:", response.data["id"])
    
    # تحديث السجل
    posted.append(tweet)
    with open(log_file, "w", encoding="utf-8") as f:
        for t in posted:
            f.write(t + "\n")
except Exception as e:
    print("❌ خطأ في النشر:", e)

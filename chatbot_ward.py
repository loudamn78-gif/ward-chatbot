import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk
from tkinter import simpledialog

# دالة إصلاح العرض (تضمن إن الكلام يطلع مشبوك ومن اليمين لليسار)
def fix_text(text):
    if not text: return ""
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def ورد_بوت():
    # إخفاء نافذة tkinter الرئيسية الكبيرة
    root = tk.Tk()
    root.withdraw()

    # ترحيب البداية في الترمنال
    print(fix_text("--- مرحبا بك في ورد | WARD ---"))
    print(fix_text("هلا والله حياك! أنا مساعدك الذكي من براند ورد."))
    print("-" * 30)
    
    while True:
        # تفتح لك نافذة صغيرة تكتب فيها، وتدعم العربي 100% بدون قلب حروف
        user_input = simpledialog.askstring("ورد بوت", "اكتب سؤالك هنا:")
        
        # إذا قفلت النافذة أو ضغطت Cancel يخرج علطول وفوراً
        if user_input is None: 
            print(fix_text("في أمان الله"))
            break 

        # تنظيف النص من المساحات الزائدة
        user_input = user_input.strip()

        # طباعة الكلام اللي أنت كتبته في الترمنال بشكل مرتب
        print(fix_text(f"أنت: {user_input}"))

        # 1. شرط الخروج والوداع (يرد "في أمان الله" ويقفل علطول)
        if 'باي' in user_input or 'مع السلامة' in user_input or 'خروج' in user_input:
            print(fix_text("ورد: في أمان الله"))
            break

        # 2. شرط السلام والتحية
        elif 'السلام عليكم' in user_input or 'سلام' in user_input:
            print(fix_text("ورد: وعليكم السلام ورحمة الله وبركاته، هلا بك!"))
        
        # 3. شرط أنواع الورد
        elif 'انواع الورد' in user_input or 'أنواع الورد' in user_input:
            print(fix_text("ورد: عندنا ورود متنوعة وجميلة تناسب كل أذواقكم ومناسباتكم."))
        
        # 4. شرط التوصيل
        elif 'توصيل' in user_input or 'فيه توصيل' in user_input:
            print(fix_text("ورد: نعم نوصل لجميع مناطق المملكة، والرياض خلال 24 ساعة!"))
        
        # 5. شرط الأسعار
        elif 'الاسعار' in user_input or 'الأسعار' in user_input or 'كم السعر' in user_input or 'بكم' in user_input:
            print(fix_text("ورد: أسعارنا في المتناول وأبشر باللي يرضيك!"))
            
        # 6. شرط العطور
        elif 'عطور' in user_input or 'عندكم عطور' in user_input:
            print(fix_text("ورد: إي نعم، عندنا تشكيلة فخمة من العطور اللي تليق بمناسباتكم وجاذبيتكم."))
        
        # رد احتياطي إذا كتب شيء خارج الشروط
        else:
            print(fix_text("ورد: تسلم، بس ما فهمت عليك زين.. تقدر تسألني عن الورد، العطور، الأسعار أو التوصيل؟"))

        print("-" * 20)

if __name__ == "__main__":
    ورد_بوت()
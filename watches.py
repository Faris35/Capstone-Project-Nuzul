# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd

# Inject CSS for RTL
rtl_css = """
<style>
body {
    direction: rtl;
    text-align: right;
}
</style>
"""
st.markdown(rtl_css, unsafe_allow_html=True)

# Load data
df = pd.read_csv('Final_version4_all_watches.csv')

# Title
st.title('ساعتك مو للزينة بس تقدر تستثمر فيها، خلها زينة وخزينة!')

# Introduction
st.markdown("""
في الوقت الحالي، الساعات الفاخرة ما صارت مجرد أداة نعرف فيها الوقت، لكنها صارت استثمار ذكي يحتفظ بقيمته ويزيد مع الوقت، مثل الذهب والعقارات.
الكثير صاروا يشوفونها كأصول ثمينة، خاصة إذا كانت نادرة أو من ماركات عالمية معروفة، وهذا يخليها خيار مثالي لأي شخص يفكر في الاستثمار.
**وهنا دورنا**، بنساعدك تعرف أهم الجوانب وتكتشف السوق عشان تدخل بثقة سواء كنت هاوي ساعات أو مستثمر.
""")

# User Segmentation
st.markdown("""
**أنت وش تفضل؟**
- إذا كنت **هاوي** تحب تجمع الساعات عشان شكلها وجمالها.
- أو كنت **مستثمر** تبحث عن عوائد مالية واستثمار ذكي.
""")

user_type = st.radio("اختر هدفك", ("هاوي", "مستثمر"))

# Collector Flow
if user_type == "هاوي":
    st.subheader("للهواة: اكتشف أفضل الخيارات الجمالية!")
    
    st.markdown("""
    للهواة، أهم شيء أنك تختار الساعة اللي تعكس شخصيتك وتناسب ذوقك. هنا بنقدم لك:
    - توزيع المواد (ذهب، فولاذ، بلاتين) وكيف تؤثر على شكل الساعة.
    - تحليل الأحجام والأنماط المناسبة (صغيرة أو كبيرة) لكل مناسبة.
    """)
    
    # Material Distribution
    material_counts = df['case_material'].value_counts()
    st.markdown("### توزيع المواد الأكثر استخداماً:")
    st.bar_chart(material_counts)

    # Size Analysis
    st.markdown("### توزيع الأحجام (مم):")
    st.bar_chart(df['size_mm'].value_counts())

# Investor Flow
elif user_type == "مستثمر":
    st.subheader("للمستثمرين: اعرف أكثر عن السوق!")
    
    st.markdown("""
    للمستثمرين، نركز على العوائد المالية وكيف تختار الساعة المناسبة للاستثمار. 
    - تعرف على الماركات اللي تحافظ على قيمتها أو تزيد مع الوقت.
    - تابع الأسعار حسب حالة الساعة (جديدة أو مستعملة).
    """)
    
    # Condition Filter
    condition = st.selectbox('اختر حالة الساعة', df['condition'].unique())
    filtered_df = df[df['condition'] == condition]

    # Average Prices by Brand
    top_brands = filtered_df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(5)
    st.markdown("### متوسط الأسعار لأغلى خمس ماركات:")
    st.bar_chart(top_brands)

    # Yearly Trends
    st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
    yearly_prices = df.groupby('year_of_production')['price_usd'].mean()
    st.line_chart(yearly_prices)

# Additional Insights
st.subheader("نقاط إضافية مهمة")
st.markdown("""
بغض النظر إذا كنت هاوي أو مستثمر، هنا بعض النقاط اللي لازم تعرفها:
- متوسط الأسعار يختلف بين الساعات الرجالية والنسائية بشكل ملحوظ.
- مادة السوار (جلد، معدن، سيراميك) ممكن تؤثر على السعر.
- حالة الساعة (جديدة، مستعملة) لها تأثير مباشر على قيمتها.
""")

# Gender and Price
st.markdown("### متوسط الأسعار حسب الجنس:")
gender_prices = df.groupby('sex')['price_usd'].mean()
st.bar_chart(gender_prices)

# Bracelet Material Impact
st.markdown("### تأثير مادة السوار على الأسعار:")
bracelet_prices = df.groupby('bracelet_material')['price_usd'].mean()
st.bar_chart(bracelet_prices)

# Case Material Impact
st.markdown("### تأثير مادة الساعة على الأسعار:")
case_material_prices = df.groupby('case_material')['price_usd'].mean()
st.bar_chart(case_material_prices)

# Conclusion and Recommendations
st.subheader("توصياتنا")
st.markdown("""
بناءً على تحليلنا، هذه أهم النصائح:
1. إذا كنت هاوي، ركز على الساعات النادرة وذات التصاميم المميزة.
2. إذا كنت مستثمر، اختار الماركات اللي تحافظ على قيمتها مثل Patek Philippe وRichard Mille.
3. اهتم بحالة الساعة، الجديدة غالباً تحتفظ بقيمتها بشكل أفضل.
4. تابع السوق باستمرار وتعلم من الموديلات اللي نجحت.
""")

# Final Interactive Section
st.subheader("نبي نسمع منك!")
st.markdown("""
وش رأيك في تحليلنا؟ هل فيه شيء إضافي تحب نستكشفه؟ اكتب لنا اقتراحاتك أو استفساراتك.
""")
user_feedback = st.text_area("اكتب تعليقك هنا:")
if st.button("إرسال"):
    st.success("شكراً لك! بنراجع تعليقك وناخذ اقتراحاتك بعين الاعتبار.")
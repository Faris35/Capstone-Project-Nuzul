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
# TODO - rewrite the introduction
st.markdown("""
في الوقت الحالي، الساعات الفاخرة ما صارت مجرد أداة نعرف فيها الوقت، لكنها صارت استثمار ذكي يحتفظ بقيمته ويزيد مع الوقت، مثل الذهب والعقارات.
الكثير صاروا يشوفونها كأصول ثمينة، خاصة إذا كانت نادرة أو من ماركات عالمية معروفة، وهذا يخليها خيار مثالي لأي شخص يفكر في الاستثمار.
**وهنا دورنا**، بنساعدك تعرف أهم الجوانب وتكتشف السوق عشان تدخل بثقة سواء كنت هاوي ساعات أو مستثمر.
""")

# User Segmentation
# st.markdown("""
# **أنت وش تفضل؟**
# - إذا كنت **هاوي** تحب تجمع الساعات عشان شكلها وجمالها.
# - أو كنت **مستثمر** تبحث عن عوائد مالية واستثمار ذكي.
# """)

# user_type = st.radio("اختر هدفك", ("هاوي", "مستثمر"))

# Collector Flow
# if user_type == "هاوي":
#     st.subheader("للهواة: اكتشف أفضل الخيارات الجمالية!")
    
#     st.markdown("""
#     للهواة، أهم شيء أنك تختار الساعة اللي تعكس شخصيتك وتناسب ذوقك. هنا بنقدم لك:
#     - توزيع المواد (ذهب، فولاذ، بلاتين) وكيف تؤثر على شكل الساعة.
#     - تحليل الأحجام والأنماط المناسبة (صغيرة أو كبيرة) لكل مناسبة.
#     """)
    
#     # Material Distribution
#     material_counts = df['case_material'].value_counts()
#     st.markdown("### توزيع المواد الأكثر استخداماً:")
#     st.bar_chart(material_counts)

#     # Size Analysis
#     st.markdown("### توزيع الأحجام (مم):")
#     st.bar_chart(df['size_mm'].value_counts())

# Investor Flow
# elif user_type == "مستثمر":
# st.subheader("للمستثمرين: اعرف أكثر عن السوق!")

st.markdown("""
للمستثمرين، نركز على العوائد المالية وكيف تختار الساعة المناسبة للاستثمار. 
- تعرف على الماركات اللي تحافظ على قيمتها أو تزيد مع الوقت.
- تابع الأسعار حسب حالة الساعة (جديدة أو مستعملة).
""")

# # Condition Filter
# condition = st.selectbox('اختر حالة الساعة', df['condition'].unique())
# filtered_df = df[df['condition'] == condition]

# Average Prices by Brand
# TODO - Map it to Arabic
# top_brands = filtered_df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)
top_brands_all = df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)
# st.markdown("### متوسط الأسعار لأغلى عشر ماركات:")
# st.bar_chart(top_brands)
st.markdown("### متوسط الأسعار لأغلى عشر ماركات :")
st.bar_chart(top_brands_all)

# Correlation between Price and rest of the features and put a drop down menu to select the brand
st.markdown("### تحليل العلاقة بين الأسعار والمواصفات:")
features = ['model','movement','case_material','bracelet_material','year_of_production','condition','sex','size_mm']

# Yearly Trends
st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
yearly_prices = df.groupby('year_of_production')['price_usd'].mean()
st.line_chart(yearly_prices)

# Additional Insights
# TODO - Add more insights and visualizations 
st.subheader("نقاط إضافية مهمة")
st.markdown("""
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
# TODO - Rewrite the recommendations
st.subheader("توصياتنا")
st.markdown("""
بناءً على تحليلنا، هذه أهم النصائح:
1. إذا كنت هاوي، ركز على الساعات النادرة وذات التصاميم المميزة.
2. إذا كنت مستثمر، اختار الماركات اللي تحافظ على قيمتها مثل Patek Philippe وRichard Mille.
3. اهتم بحالة الساعة، الجديدة غالباً تحتفظ بقيمتها بشكل أفضل.
4. تابع السوق باستمرار وتعلم من الموديلات اللي نجحت.
""")
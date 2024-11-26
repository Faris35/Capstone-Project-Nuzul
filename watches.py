# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

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

# # Correlation between Price and rest of the features and put a drop down menu to select the brand
# # Features to analyze
# features = [
#     'model', 'movement', 'case_material', 
#     'bracelet_material', 'year_of_production', 
#     'condition', 'sex', 'size_mm'
# ]

# # Streamlit header
# st.markdown("### تحليل العلاقة بين الأسعار والمواصفات:")

# # Select the brand
# selected_brand = st.selectbox("اختر الماركة", df['brand'].unique())

# # Filter the DataFrame based on the selected brand
# brand_df = df[df['brand'] == selected_brand].copy()

# # Encode non-numeric columns to numeric using LabelEncoder
# label_encoders = {}
# for feature in features:
#     if brand_df[feature].dtype == 'object':
#         le = LabelEncoder()
#         brand_df[feature] = le.fit_transform(brand_df[feature].astype(str))
#         label_encoders[feature] = le

# # Select the numeric features
# numeric_features = ['price_usd'] + features

# # Compute the correlation matrix
# correlation_matrix = brand_df[numeric_features].corr()

# # Extracting just the first column (correlations with 'price_usd')
# first_column_corr = correlation_matrix['price_usd'].to_frame()

# # Plot the heatmap
# fig, ax = plt.subplots()
# sns.heatmap(first_column_corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
# ax.set_title(f"Correlation Heatmap for {selected_brand}", fontsize=14)
# st.pyplot(fig)

####################

# size Trends
st.markdown("### تحليل الأسعار حسب حجم الساعة:")
size_prices = df.groupby('size_mm')['price_usd'].median()
st.line_chart(size_prices)

# Yearly Trends
st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
yearly_prices = df.groupby('year_of_production')['price_usd'].median()
st.line_chart(yearly_prices)

# Model Analysis
st.markdown("### تحليل الأسعار حسب الموديل:")
model_prices = df.groupby('model')['price_usd'].median().sort_values(ascending=False).head(10)
st.bar_chart(model_prices)

# Movement Analysis
st.markdown("### تحليل الأسعار حسب نوع الحركة:")
movement_prices = df.groupby('movement')['price_usd'].median().sort_values(ascending=False)
st.bar_chart(movement_prices)

# Case Material Analysis
st.markdown("### تحليل الأسعار حسب مادة الساعة:")
case_material_prices = df.groupby('case_material')['price_usd'].median().sort_values(ascending=False)
st.bar_chart(case_material_prices)

# Bracelet Material Analysis
st.markdown("### تحليل الأسعار حسب مادة السوار:")
bracelet_material_prices = df.groupby('bracelet_material')['price_usd'].median().sort_values(ascending=False)
st.bar_chart(bracelet_material_prices)

# Condition Analysis
st.markdown("### تحليل الأسعار حسب حالة الساعة:")
condition_prices = df.groupby('condition')['price_usd'].median().sort_values(ascending=False)
st.bar_chart(condition_prices)

# Gender and Price
st.markdown("### متوسط الأسعار حسب الجنس:")
gender_prices = df.groupby('sex')['price_usd'].median()
st.bar_chart(gender_prices)

# Additional Insights
# TODO - Add more insights and visualizations 
st.subheader("نقاط إضافية مهمة")
st.markdown("""
- متوسط الأسعار يختلف بين الساعات الرجالية والنسائية بشكل ملحوظ.
- مادة السوار (جلد، معدن، سيراميك) ممكن تؤثر على السعر.
- حالة الساعة (جديدة، مستعملة) لها تأثير مباشر على قيمتها.
""")

# TODO - Add section for the user to input features and get the df of the watches that match the features
# we will show him the models that match his features and the price of each model
# User Input
st.header("اختر مواصفات الساعة:")
brand = st.selectbox("البراند", df['brand'].unique())
movement = st.selectbox("نوع الحركة", df[df['brand'] == brand]['movement'].unique())
case_material = st.selectbox("مادة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement)]['case_material'].unique())
bracelet_material = st.selectbox("مادة السوار", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material)]['bracelet_material'].unique())
year_of_production = st.selectbox("سنة التصنيع", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material)]['year_of_production'].unique())
condition = st.selectbox("حالة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material) & (df['year_of_production'] == year_of_production)]['condition'].unique())

# Filter the DataFrame
filtered_data = df[
    (df['brand'] == brand) &
    (df['movement'] == movement) &
    (df['case_material'] == case_material) &
    (df['bracelet_material'] == bracelet_material) &
    (df['year_of_production'] == year_of_production) &
    (df['condition'] == condition)
]

# Show the filtered DataFrame
st.subheader("الساعات المتوفرة:")
#st.write(filtered_data.drop(columns=['brand', 'movement', 'case_material', 'bracelet_material', 'year_of_production', 'condition']))
# Add a column for price range for each model within the filtered DataFrame
filtered_data['price_range'] = filtered_data.groupby('model')['price_usd'].transform(lambda x: f"${x.min()} - ${x.max()}")
filtered_data = filtered_data.drop_duplicates(subset=['model'])
st.write(filtered_data[['model', 'price_range']])

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
# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

st.image("zeina.png", width=120)


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
**وهنا دورنا**، بنساعدك تعرف أهم الجوانب وتكتشف السوق عشان تدخل بثقة.
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

# st.markdown("""
# للمستثمرين، نركز على العوائد المالية وكيف تختار الساعة المناسبة للاستثمار. 
# - تعرف على الماركات اللي تحافظ على قيمتها أو تزيد مع الوقت.
# - تابع الأسعار حسب حالة الساعة (جديدة أو مستعملة).
# """)

# # Condition Filter
# condition = st.selectbox('اختر حالة الساعة', df['condition'].unique())
# filtered_df = df[df['condition'] == condition]

# Average Prices by Brand
# TODO - Map it to Arabic
# top_brands = filtered_df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)
top_brands_all = df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)
# st.markdown("### متوسط الأسعار لأغلى عشر ماركات:")
# st.bar_chart(top_brands)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### تدري وش الماركات اللي تتصدر أغلى الساعات بالعالم؟
    **ريتشارد ميل** متربعة على القمة بأسعارها العالية واللي تعكس ندرتها وفخامتها، تليها **باتيك فيليب** و**أوديمار بيغيه** كخيارات راقية ومميزة.  
    أما **رولكس**، فهي تقدم جودة عالية بفخامة وسعر أقل شوي مقارنة بالباقي.
    """)
    st.markdown("### متوسط الأسعار لأغلى عشر ماركات :")
    st.bar_chart(top_brands_all)

with col2:
    top_brands_distribution = df['brand'].value_counts().head(10).index
    # Filter data for only the top 10 brands
    top_brands_distribution = df[df['brand'].isin(top_brands_distribution)]
    st.markdown("### توزيع الأسعار لأغلى عشر ماركات:")
    st.bar_chart(top_brands_distribution['price_usd'])

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

st.markdown("""
بعد دراسة البيانات وخصائص الساعات، وصلنا لاستنتاج بأن أغلب الساعات تتأثر بالتالي:
1. الحجم
2. سنة التصنيع
3. الموديل
4. نوع الحركة
5. مادة السوار

سنعرض الآن الرسوم البيانية للخصائص المذكورة ومدى تأثيرها على قيمة الساعات.
""")

st.markdown("### تحليل الأسعار حسب حجم الساعة:")
size_prices = df.groupby('size_mm')['price_usd'].median()
st.line_chart(size_prices)

# Yearly Trends
st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
yearly_prices = df.groupby('year_of_production')['price_usd'].median()
st.line_chart(yearly_prices)

# Model Analysis
selected_brand = st.selectbox("اختر الماركة لتحليل الأسعار حسب الموديل:", df['brand'].unique())
model_prices = df[df['brand'] == selected_brand].groupby('model')['price_usd'].median().sort_values(ascending=False).head(10)
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



st.markdown("""
الآن بعد ما وضحت لك الصورة أكثر وشفت الماركات اللي لها احتمالية عالية إنك تستفيد منها، صار عندك الخيار تتصفح الماركات وتشوف تفاصيل أكثر عن تأثير الخصائص عليها.
""")

column_names_mapping = {
    'model': 'الموديل',
    'movement': 'نوع الحركة',
    'case_material': 'مادة الساعة',
    'bracelet_material': 'مادة السوار',
    'year_of_production': 'سنة الإنتاج',
    'condition': 'الحالة',
    'sex': 'الجنس',
    'size_mm': 'الحجم (مم)',
    'price_usd': 'السعر بالدولار'
}

st.markdown("""
بعد دراسة البيانات وخصائص الساعات، وصلنا لاستنتاج بأن أغلب الساعات تتأثر بالتالي:
1. الحجم
2. سنة التصنيع
3. الموديل
4. نوع الحركة
5. مادة السوار

سنعرض الآن الرسوم البيانية للخصائص المذكورة ومدى تأثيرها على قيمة الساعات.
""")
brand_options = ['All'] + top_brands_all.index.tolist()

# Create a dropdown menu for brand selection
brand_filter = st.selectbox('اختر البراند', brand_options)

# Filter the dataframe based on the selected brand or 'All'
if brand_filter != "All":
    filtered_df = df[df['brand'] == brand_filter]
else:
    filtered_df = df

# 1. الحجم (Size) 
st.markdown("##### تحليل تأثير الحجم على السعر:")
st.markdown("""
في هذا الرسم البياني، نلاحظ العلاقة بين حجم الساعة وسعرها. 
هل هناك علاقة بين الحجم والسعر؟ هل الساعات الأكبر حجمًا أغلى عادة؟
خلنا نكتشف من خلال الرسم البياني.
""")
fig_size_price_bubble = px.scatter(filtered_df, x='size_mm', y='price_usd', size='price_usd',
                                   color='brand', hover_name='model',
                                   title=f'الحجم والسعر للبراند {brand_filter}', 
                                   labels={'size_mm': 'الحجم (mm)', 'price_usd': 'السعر (دولار أمريكي)'})
st.plotly_chart(fig_size_price_bubble)
st.markdown("""
كما يظهر في الرسم البياني، في أغلب الحالات، يزداد السعر مع زيادة الحجم. 
هذا يعني أن هناك علاقة طردية بين حجم الساعة وسعرها.
""")

# 2. سنة التصنيع (Year of Production) - Line chart
st.markdown("#### تحليل تأثير سنة التصنيع على السعر:")
st.markdown("""
هنا راح نشوف إذا كان سنة التصنيع لها تأثير على السعر. 
هل الساعات القديمة أغلى؟ ولا الساعات الحديثة هي الأغلى؟ خلونا نكتشف.
""")
yearly_prices = filtered_df.groupby('year_of_production')['price_usd'].mean()
st.markdown(f"تحليل اختلاف الاسعار على حسب سنة الصنع {brand_filter}")
st.line_chart(yearly_prices)

st.markdown("""
من الرسم البياني نقدر نشوف أن الساعات الحديثة عمومًا أغلى، لكن في بعض الساعات القديمة لها قيمة عالية جدا.
""")

# 3. الموديل (Model) - Best model regarding the highest price

st.markdown("#### تحليل الموديلات الأفضل من حيث السعر:")
st.markdown("""
في هذا التحليل، بنشوف أفضل الموديلات اللي تحقق أعلى أسعار.
نتعرف على الموديلات اللي تستحق استثمارك.
""")
top_models = filtered_df.groupby('model')['price_usd'].mean().sort_values(ascending=False).head(10)
fig_model = px.bar(top_models, x=top_models.index, y=top_models.values, 
                   title=f'أفضل موديلات حسب السعر للبراند {brand_filter}', 
                   labels={'x': 'الموديل', 'y': 'متوسط السعر (دولار أمريكي)'})
st.plotly_chart(fig_model)
st.markdown("""
من خلال الرسم البياني، نلاحظ أن بعض الموديلات تحقق أسعار أعلى بكثير من غيرها. 
الموديلات النادرة هي اللي تسجل أعلى الأسعار.
""")

# 4. نوع الحركة (Movement Type) - Best movement type regarding the highest price
st.markdown("#### تحليل نوع الحركة وتأثيره على السعر:")
st.markdown("""
هنا بنحلل تأثير نوع الحركة على سعر الساعة. 
هل الساعات ذات الحركة المعقدة أغلى؟ دعونا نكتشف مع الرسم البياني.
""")
top_movements = filtered_df.groupby('movement')['price_usd'].mean().sort_values(ascending=False).head(10)
fig_movement = px.bar(top_movements, x=top_movements.index, y=top_movements.values, 
                      title=f'أفضل أنواع الحركة حسب السعر للبراند {brand_filter}', 
                      labels={'x': 'نوع الحركة', 'y': 'متوسط السعر (دولار أمريكي)'})
st.plotly_chart(fig_movement)
st.markdown("""
من الرسم البياني نلاحظ أن الحركة المعقدة أو المتطورة عمومًا تؤدي إلى رفع السعر.
إذا كنت تدور على ساعة فاخرة، فكر في الحركة اللي تحتها!
""")

# 5. مادة السوار (Bracelet Material) - Best bracelet material regarding the highest price
st.markdown("##### تحليل مادة السوار وتأثيرها على السعر:")
st.markdown("""
في هذا التحليل، راح نشوف إذا كان نوع السوار له تأثير على السعر. 
هل الساعات المصنوعة من مواد مثل الذهب أغلى؟ خلونا نكتشف.
""")
top_bracelet_materials = filtered_df.groupby('bracelet_material')['price_usd'].mean().sort_values(ascending=False).head(10)
fig_bracelet_material = px.bar(top_bracelet_materials, x=top_bracelet_materials.index, y=top_bracelet_materials.values, 
                               title=f'أفضل مواد السوار حسب السعر للبراند {brand_filter}', 
                               labels={'x': 'مادة السوار', 'y': 'متوسط السعر (دولار أمريكي)'})
st.plotly_chart(fig_bracelet_material)
st.markdown("""
من خلال الرسم البياني نقدر نلاحظ أن بعض المواد مثل الذهب والفولاذ هي اللي ترفع الأسعار.
إذا كنت تبغى استثمار حقيقي، يمكن المواد هذه تكون اختيارك.
""")


st.markdown("#### توصيات أخيرة:")
st.markdown("""
بعد ما استعرضنا تأثير الخصائص المختلفة على سعر الساعات، نحب نشارك معك بعض التوصيات التي يمكن أن تساعدك في اتخاذ القرار الأفضل للاستثمار:
""")
st.markdown("""
1. **اختيار الماركات الشهيرة:**
   - إذا كنت تبحث عن استثمار طويل الأمد، اختيار الماركات العالمية المعروفة هو الخيار الأفضل، حيث أن هذه الماركات تحافظ على قيمتها أو تزيد بمرور الوقت. وأيضًا، **Richard Mille** تعد من أعلى الماركات من حيث الأسعار، حيث أن الساعات منها تعتبر من الاستثمارات المربحة نظرًا لندرتها وتفرد تصاميمها.

2. **الحجم مهم:** 
   - بشكل عام، الساعات الأكبر حجمًا قد تكون أغلى، لكن هذا ليس قاعدة ثابتة. راجع الموديلات بحذر وركز على سمعة الماركة.

3. **سنة التصنيع:** 
   - الساعات الحديثة تكون غالبًا أغلى، لكنها أيضًا تحافظ على قيمتها بمرور الوقت. بعض الساعات القديمة قد تملك قيمة كبيرة إذا كانت نادرة أو مشهورة.

4. **الموديلات النادرة:** 
   - بعض الموديلات تكون أكثر قيمة من غيرها بسبب ندرتها أو خصوصيتها. إذا كنت مهتمًا بالاستثمار، حاول دائمًا البحث عن الموديلات المميزة التي تتمتع بشعبية.
            
5. **نوع الحركة والمادة:** 
   - كلما كانت الحركة معقدة وأكثر تطورًا، كلما ارتفع السعر. أيضًا، المواد الفاخرة مثل **الذهب الوردي**، **البلاتين**، **الذهب الأبيض**، و **السيراميك** تساهم في رفع السعر بشكل كبير. هذه المواد تضيف قيمة كبيرة للساعة بسبب ندرتها وجودتها العالية.
""")

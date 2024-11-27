# Import necessary libraries
import streamlit as st  # Streamlit for building the interactive web app
from PIL import Image  # To handle image loading and manipulation
import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For plotting charts
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
import plotly.express as px  # For interactive visualizations

# Displaying a logo or an image on the app
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("zeina.png", width= 200)  # Display an image with a specific width

with col3:
    st.write(' ')



# Adding RTL (Right-to-Left) styling for Arabic content
rtl_css = """
<style>
body {
    direction: rtl;
    text-align: right;
}
</style>
"""
st.markdown(rtl_css, unsafe_allow_html=True)  # Applying RTL style for Arabic alignment

# Loading the dataset
df = pd.read_csv('Final_version4_all_watches.csv')  # Load watch data; ensure file exists in the correct location

# Adding a catchy title to the app
st.title('ساعتك مو للزينة بس تقدر تستثمر فيها، خلها زينة وخزينة!')

# Adding a description and context for the app
st.markdown("""
            فكرت تشتري ساعة غالية؟ يقولون الساعات الفخمة مو بس زينة، لكنها استثمار يرفع قيمتها مع الوقت. والمؤثرين يتكلمون عنها كأنها الذهب الجديد، لكن هل كلامهم صحيح؟

في "زينة وخزينة"، حللنا سوق الساعات عشان نفهم وش يفرق بين الماركات ونترك الحكم لك. جمعنا البيانات من موقع "Chrono24"، المتخصص في بيع الساعات الجديدة والمستعملة، لتقديم صورة واضحة تساعدك في معرفة إذا كانت الساعات الفاخرة مجرد زينة أم استثمار حقيقي
""")

url = "https://www.chrono24.com/"

# Display the image
st.image("./logo-positive-reduced.svg", width=150)

# Add a clickable caption using markdown
st.markdown(f"[Click Here For More Information]({url})", unsafe_allow_html=True)

st.markdown("#### هل سوق الساعات في نمو مستمر؟")

st.markdown(""" تم تقييم حجم سوق الساعات الفاخرة بحوالي 42.9 مليار دولار أمريكي في عام 2022. ومن المتوقع أن ينمو سوق الساعات الفاخرة من 45.1 مليار دولار أمريكي في عام 2023 إلى 68.2 مليار دولار أمريكي بحلول عام 2032، مع معدل نمو سنوي مركب قدره 5.30% خلال فترة التوقعات (2023 - 2032). ومن العوامل الرئيسية التي تدفع السوق هي الزيادة في اتجاه ارتداء البالغين للساعات الفاخرة كرمز للمكانة الاجتماعية.
المصدر: [Market Research Future](https://www.marketresearchfuture.com/reports/luxury-watch-market-10897) """)

st.image("./Global_Luxury_Watch_Market.jpg",width=500)




# Calculate median price for top 10 watch brands
top_brands_all = df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)

# Split the layout into two columns for better data presentation

st.markdown(""" 
            ## قل نبدأ في تحليل السوق وش أول شي يجي في بالك اول ماتسمع ساعة فاخرة؟ 
            #### في هذا الرسم البياني راح نستعرض لكم متوسط الأسعار لأغلى 5 براندات
        
             """)
col1, col2 = st.columns(2)

with col1:
    # Add a description of the top brands
    st.markdown("""
    ### تدري وش الماركات اللي تتصدر أغلى الساعات بالعالم؟
    **ريتشارد ميل** متربعة على القمة بأسعارها العالية واللي تعكس ندرتها وفخامتها، تليها **باتيك فيليب** و**أوديمار بيغيه** كخيارات راقية ومميزة.  
    أما **رولكس**، فهي تقدم جودة عالية بفخامة وسعر أقل شوي مقارنة بالباقي.
    """)
    # Display a bar chart for the median price of the top brands
    st.markdown("### متوسط الأسعار لأغلى عشر ماركات :")
    st.bar_chart(top_brands_all)

with col2:
    # Add insights about brand popularity
    st.markdown("""
    ### شفنا أغلى الماركات، لكن هنا الصورة تختلف:
    **رولكس** جمعت بين السعر المعقول والانتشار الأكبر.  
    **باتيك فيليب**، رغم أنها من الأغلى، إلا أنها برضو من الأكثر انتشاراً.  
    بينما **أوميغا** و**تاغ هوير** ركزت على الشعبية والجودة بسعر أقل.
    """)
    # Display a bar chart for the most popular brands
    popular_brands = df['brand'].value_counts().head(10)
    st.markdown("### أكثر عشر ماركات انتشاراً:")
    st.bar_chart(popular_brands)

# Add a detailed markdown for data insights and analysis
st.markdown("""
بعد دراسة البيانات وخصائص الساعات، وصلنا لاستنتاج بأن أغلب الساعات تتأثر بالتالي:
1. الحالة
2. الحجم
3. سنة التصنيع
4. الموديل
5. نوع الحركة
6. مادة السوار

سنعرض الآن الرسوم البيانية للخصائص المذكورة ومدى تأثيرها على قيمة الساعات.
""")

# Median price based on watch condition
condition_prices = df.groupby('condition')['price_usd'].median().sort_values(ascending=False)
st.markdown("### تحليل الأسعار حسب حالة الساعة:")
st.bar_chart(condition_prices)  # Display a bar chart

# Median price based on size
size_prices = df.groupby('size_mm')['price_usd'].median()
st.markdown("### تحليل الأسعار حسب حجم الساعة:")
st.line_chart(size_prices)  # Display a line chart

# Median price over the years
yearly_prices = df.groupby('year_of_production')['price_usd'].median()
st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
st.line_chart(yearly_prices)  # Display a line chart

# Allow users to select a brand for further analysis
selected_brand = st.selectbox("اختر الماركة لتحليل الأسعار حسب الموديل:", df['brand'].unique())
model_prices = df[df['brand'] == selected_brand].groupby('model')['price_usd'].median().sort_values(ascending=False).head(10)
st.bar_chart(model_prices)  # Display a bar chart for models of the selected brand

# Filter data for the selected brand
filtered_df = df[df['brand'] == selected_brand]

# Median price based on movement type
movement_prices = filtered_df.groupby('movement')['price_usd'].median().sort_values(ascending=False)
st.markdown("### تحليل الأسعار حسب نوع الحركة:")
st.bar_chart(movement_prices)

## Trend of Case Metarial ###
st.markdown("##### في الرسم البياني التالي راح يظهر لنا عدد الساعات بناءً على نوع الهيكل المصنع منه الساعة على الى مر العقود الماضية. هذا الرسم البياني مع الرسم البياني في (تحليل الأسعار حسب مادة الساعة) راح يفيدك في اختيار المادة الاكثر طلباً والاكثر سعراً")
st.markdown("### ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)")

# Filter dataset for specific year range and add a decade column
start_year = 1900
end_year = 2023
filtered_df = filtered_df[(filtered_df['year_of_production'] >= start_year) & (filtered_df['year_of_production'] <= end_year)]
filtered_df['decade'] = (filtered_df['year_of_production'] // 10) * 10  # Group by decade

# Analyze the number of watches based on case material per decade
case_material_count = filtered_df.groupby(['decade', 'case_material']).size().reset_index(name='count')
fig = px.line(
    case_material_count,
    x='decade',
    y='count',
    color='case_material',
    markers=True,
    labels={'count': 'عدد الساعات بحسب نوع الهيكل', 'decade': 'عقد'}
)
st.plotly_chart(fig)  # Interactive line chart for decade-wise data

# Allow users to select a year and analyze case materials
selected_year = st.selectbox("اختر السنة لتحليل الأسعار حسب مادة الساعة:", filtered_df['decade'].unique())
year_filtered_df = filtered_df[filtered_df['year_of_production'] == selected_year]
case_material_prices = year_filtered_df.groupby('case_material')['price_usd'].median().sort_values(ascending=False)
st.markdown("### تحليل الأسعار حسب مادة الساعة:")
st.bar_chart(case_material_prices)

# Median price based on bracelet material
bracelet_material_prices = filtered_df.groupby('bracelet_material')['price_usd'].median().sort_values(ascending=False)
st.markdown("### تحليل الأسعار حسب مادة السوار:")
st.bar_chart(bracelet_material_prices)

# Median price based on gender
gender_prices = filtered_df.groupby('sex')['price_usd'].median()
st.markdown("### متوسط الأسعار حسب الجنس:")
st.bar_chart(gender_prices)

# Additional insights section
st.subheader("نقاط إضافية مهمة")
st.markdown("""
- متوسط الأسعار يختلف بين الساعات الرجالية والنسائية بشكل ملحوظ.
- مادة السوار (جلد، معدن، سيراميك) ممكن تؤثر على السعر.
- حالة الساعة (جديدة، مستعملة) لها تأثير مباشر على قيمتها.
""")

# Interactive filters for watch specifications
st.header("اختر مواصفات الساعة:")
brand = st.selectbox("البراند", df['brand'].unique())
movement = st.selectbox("نوع الحركة", df[df['brand'] == brand]['movement'].unique())
case_material = st.selectbox("مادة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement)]['case_material'].unique())
bracelet_material = st.selectbox("مادة السوار", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material)]['bracelet_material'].unique())
year_of_production = st.selectbox("سنة التصنيع", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material)]['year_of_production'].unique())
condition = st.selectbox("حالة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material) & (df['year_of_production'] == year_of_production)]['condition'].unique())

# Filter data based on selected criteria
filtered_data = df[
    (df['brand'] == brand) &
    (df['movement'] == movement) &
    (df['case_material'] == case_material) &
    (df['bracelet_material'] == bracelet_material) &
    (df['year_of_production'] == year_of_production) &
    (df['condition'] == condition)
]



# Display available watches based on the selected filters
st.subheader("الساعات المتوفرة:")
filtered_data['price_range'] = filtered_data.groupby('model')['price_usd'].transform(lambda x: f"${x.min()} - ${x.max()}")
filtered_data = filtered_data.drop_duplicates(subset=['model'])
st.write(filtered_data[['model', 'price_range']])  # Display filtered watch details

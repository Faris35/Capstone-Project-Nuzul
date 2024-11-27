# Import necessary libraries
import streamlit as st  # Streamlit for building the interactive web app
from PIL import Image  # To handle image loading and manipulation
import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For plotting charts
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
import plotly.express as px  # For interactive visualizations
import numpy as np  # For numerical computing

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

# URL and logo details
url = "https://www.chrono24.com/"
logo_path = "./logo-positive-reduced.svg"

# Custom CSS for subtle-colored widgets in a 3x3 grid
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; /* Three columns */
        gap: 10px; /* Spacing between grid items */
    }
    .widget {
        padding: 10px;
        border-radius: 8px;
        font-size: 14px;
        color: black;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
    }
    .widget1 { background-color: #D9F2E6; }  /* Soft Green */
    .widget2 { background-color: #D9EAFB; }  /* Soft Blue */
    .widget3 { background-color: #FFF4CC; }  /* Soft Yellow */
    .widget4 { background-color: #FFDAD5; }  /* Soft Orange */
    .widget5 { background-color: #E8D9F2; }  /* Soft Purple */
    .widget6 { background-color: #EAE4D9; }  /* Soft Brown */
    .widget7 { background-color: #F2D9D9; }  /* Soft Pink */
    .widget8 { background-color: #D9F2F0; }  /* Soft Teal */
    .widget9 { background-color: #F2E6D9; }  /* Soft Beige */
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# Column 1: Logo with title
with col1:
    st.markdown("<h3 style='text-align: center; font-weight: bold;'>المصدر</h3>", unsafe_allow_html=True)
    st.image(logo_path, width=150)
    st.markdown(f"[للإطلاع]({url})", unsafe_allow_html=True)

# Column 2: Watches text with title
with col2:
    st.markdown("<h3 style='text-align: center; font-weight: bold;'>حجم البيانات</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>40,000+<br>ساعة</h4>", unsafe_allow_html=True)

# Column 3: Widgets in a 3x3 grid with title
with col3:
    st.markdown("<h3 style='text-align: center; font-weight: bold;'>شكل البيانات</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="grid-container">
            <div class="widget widget1">الحالة</div>
            <div class="widget widget2">الحجم</div>
            <div class="widget widget3">سنة التصنيع</div>
            <div class="widget widget4">الموديل</div>
            <div class="widget widget5">نوع الحركة</div>
            <div class="widget widget6">مادة السوار</div>
            <div class="widget widget7">السعر</div>
            <div class="widget widget8">رجالي/نسائي</div>
            <div class="widget widget9">الرقم المرجعي</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("#### هل سوق الساعات في نمو مستمر؟")

st.markdown("""قُدّر حجم سوق الساعات الفاخرة بحوالي 42.9 مليار دولار أمريكي في عام 2022، ومن المتوقع أن ينمو من 45.1 مليار دولار أمريكي في عام 2023 إلى 68.2 مليار دولار أمريكي بحلول عام 2032، بمعدل نمو سنوي مركب (CAGR) يبلغ 5.30% خلال فترة التوقعات (2024 - 2032). يُعدّ الاتجاه المتزايد بين البالغين لارتداء الساعات الفاخرة كرمز للمكانة الاجتماعية أحد أبرز العوامل التي تُحفّز نمو هذا السوق.
المصدر: [Market Research Future](https://www.marketresearchfuture.com/reports/luxury-watch-market-10897) """)

# Corrected data for the chart
years = np.arange(2018, 2032 + 1)  # 15 years from 2018 to 2032
market_sizes = [20, 25, 30, 35, 42.9, 45.1, 50, 52, 55, 60, 62, 64, 66, 68, 68.2]  # 15 values to match the years

# Create the chart
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(years, market_sizes, color='red', edgecolor='black')

# Add labels to bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}', ha='center', fontsize=8)

# Customize the chart
ax.set_title('Luxury Watch Market', fontsize=16, fontweight='bold')
ax.set_ylabel('Market Size in USD Bn', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_ylim(0, 75)  # Adjust y-axis limit for better visibility

# Add a horizontal line and arrow for title emphasis
ax.annotate('', xy=(2018, 73), xytext=(2032, 73),
            arrowprops=dict(arrowstyle='<|-', color='black', lw=1.5))
# Display the chart in Streamlit
st.pyplot(fig)



# Split the layout into two columns for better data presentation

st.markdown(""" ### بعد ما أخذنا فكرة عن سوق الساعات ونموه، خلونا نركز على التفاصيل أكثر ونشوف وش الماركات اللي تسيطر على قائمة الأغلى، وهل دايم السعر يعكس الانتشار والشعبية؟""")

st.markdown("""
### تدري وش الماركات اللي تتصدر أغلى الساعات بالعالم؟
تتوقع **رولكس** الأولى؟
المفاجأة إنها حتى مو ضمن اغلى خمس ماركات!
مثلًا، **Richard Mille** و **Patek Philippe** متصدرين القائمة بأسعار عالية جدًا.
لكن إذا جينا للساعات اللي تشوفها بشكل أكبر أو تنتشر بين عشاق الساعات، الوضع يختلف!
""")

top_brands_all = df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10).reset_index()

top_brands_all['color'] = top_brands_all['brand'].apply(lambda x: 'red' if x == 'Rolex' else 'blue')

fig1 = px.bar(
    top_brands_all,
    x='brand',
    y='price_usd',
    color='color',
    color_discrete_map={'red': 'red', 'blue': 'blue'},
    # title="أغلى الماركات حسب السعر المتوسط",
    # labels={'brand': 'العلامة التجارية', 'price_usd': 'السعر بالدولار'}
)
fig1.update_traces(marker=dict(line=dict(width=1, color='black')))
st.plotly_chart(fig1)

st.markdown("""
### شفنا أغلى الماركات، بس وش الأكثر انتشاراً؟:
رولكس هنا تتصدر المشهد.
رغم إنها مو الأغلى، إلا إنها الأكثر شعبية وتواجد بين عشاق الساعات.
ليش؟ لأنها جمعت بين الفخامة والجودة بسعر يعتبر معقول نسبيًا مقارنة بالباقين.
""")

popular_brands = df['brand'].value_counts().head(10).reset_index()
popular_brands.columns = ['brand', 'count']

popular_brands['color'] = popular_brands['brand'].apply(lambda x: 'red' if x == 'Rolex' else 'blue')

fig2 = px.bar(
    popular_brands,
    x='brand',
    y='count',
    color='color',
    color_discrete_map={'red': 'red', 'blue': 'blue'},
    # title="أكثر العلامات انتشاراً",
    # labels={'brand': 'العلامة التجارية', 'count': 'عدد الساعات'}
)
fig2.update_traces(marker=dict(line=dict(width=1, color='black')))
st.plotly_chart(fig2)


st.image("feature.png",  use_column_width=True)  


# Create a dropdown menu for selecting the chart to display
selected_brand = st.selectbox("اختر الماركة:", ["All Brands"] + list(df['brand'].unique()))

# Filter the dataframe based on the selected brand
if selected_brand != "All Brands":
    df = df[df['brand'] == selected_brand]

# Create a dropdown menu for selecting the chart to display
chart_option = st.selectbox(
    "اختر الرسم البياني لعرضه:",
    [
        "تحليل الأسعار حسب حالة الساعة",
        "تحليل الأسعار حسب حجم الساعة",
        "تحليل الأسعار حسب سنوات التصنيع",
        "تحليل الأسعار حسب الموديل",
        "تحليل الأسعار حسب نوع الحركة",
        "ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)",
        # "تحليل الأسعار حسب مادة الساعة",
        "تحليل الأسعار حسب مادة السوار",
        "متوسط الأسعار حسب الجنس"
    ]
)

# Display the selected chart
if chart_option == "تحليل الأسعار حسب حالة الساعة":
    condition_prices = df.groupby('condition')['price_usd'].median().sort_values(ascending=False)
    st.markdown("### تحليل الأسعار حسب حالة الساعة:")
    st.bar_chart(condition_prices)
    fig_condition_prices = px.bar(
        condition_prices,
        x=condition_prices.index,
        y=condition_prices.values,
        labels={'x': 'حالة الساعة', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب حالة الساعة'
    )
    st.plotly_chart(fig_condition_prices)

elif chart_option == "تحليل الأسعار حسب حجم الساعة":
    size_prices = df.groupby('size_mm')['price_usd'].median()

    distinct_color_map = {
    "A. Lange & Söhne": "#e6194b",  # Bright Red
    "Audemars Piguet": "#3cb44b",  # Bright Green
    "Breitling": "#ffe119",        # Bright Yellow
    "Cartier": "#4363d8",          # Bright Blue
    "Hublot": "#f58231",           # Bright Orange
    "IWC": "#911eb4",              # Bright Purple
    "Jaeger-LeCoultre": "#42d4f4", # Cyan
    "Longines": "#f032e6",         # Magenta
    "Omega": "#bfef45",            # Lime
    "Oris": "#fabebe",             # Light Pink
    "Panerai": "#469990",          # Teal
    "Patek Philippe": "#e6beff",   # Lavender
    "Rado": "#9a6324",             # Brown
    "Richard Mille": "#fffac8",    # Light Yellow
    "Rolex": "#800000",            # Maroon
    "Seiko": "#aaffc3",            # Mint Green
    "Sinn": "#808000",             # Olive
    "TAG Heuer": "#ffd8b1",        # Peach
    "Tudor": "#000075",            # Navy
    "Vacheron Constantin": "#808080", # Gray
    "Zenith": "#000000"            # Black
    }

# Create the scatter plot
    fig_size_price_bubble = px.scatter(
    df,
    x='size_mm',
    y='price_usd',
    size='price_usd',
    color='brand',
    hover_name='model',
    color_discrete_map=distinct_color_map,  # Apply the distinct color map
    )

    fig_size_price_bubble.update_layout(
    #title="الحجم والسعر حسب البراند",
    xaxis_title="الحجم (mm)",
    yaxis_title="السعر (دولار أمريكي)",
    legend_title="البراند",
    legend=dict(orientation="v", x=1.05, y=1)  # Adjust legend position
)

    st.plotly_chart(fig_size_price_bubble)

elif chart_option == "تحليل الأسعار حسب سنوات التصنيع":
    yearly_prices = df.groupby('year_of_production')['price_usd'].median()
    st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")
    fig_yearly_prices = px.line(
        yearly_prices,
        x=yearly_prices.index,
        y=yearly_prices.values,
        labels={'x': 'سنة التصنيع', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب سنوات التصنيع'
    )
    st.plotly_chart(fig_yearly_prices)

elif chart_option == "تحليل الأسعار حسب الموديل":
    model_prices = df.groupby('model')['price_usd'].median().sort_values(ascending=False).head(10)
    st.markdown("### تحليل الأسعار حسب الموديل:")
    fig_model_prices = px.bar(
        model_prices,
        x=model_prices.index,
        y=model_prices.values,
        labels={'x': 'الموديل', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب الموديل'
    )
    st.plotly_chart(fig_model_prices)

elif chart_option == "تحليل الأسعار حسب نوع الحركة":
    movement_prices = df.groupby('movement')['price_usd'].median().sort_values(ascending=False)
    st.markdown("### تحليل الأسعار حسب نوع الحركة:")
    fig_movement_prices = px.bar(
        movement_prices,
        x=movement_prices.index,
        y=movement_prices.values,
        labels={'x': 'نوع الحركة', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب نوع الحركة'
    )
    st.plotly_chart(fig_movement_prices)

elif chart_option == "ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)":
    st.markdown("##### في هذا الرسم البياني راح يظهر لنا عدد الساعات بناءً على نوع الهيكل المصنع منه الساعة على مر العقود الماضية.")
    st.markdown("### ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)")
    start_year = 1900
    end_year = 2023
    filtered_df = df[(df['year_of_production'] >= start_year) & (df['year_of_production'] <= end_year)]
    filtered_df['decade'] = (filtered_df['year_of_production'] // 10) * 10
    case_material_count = filtered_df.groupby(['decade', 'case_material']).size().reset_index(name='count')
    fig = px.line(
        case_material_count,
        x='decade',
        y='count',
        color='case_material',
        markers=True,
        labels={'count': 'عدد الساعات بحسب نوع الهيكل', 'decade': 'عقد'}
    )
    st.plotly_chart(fig)

elif chart_option == "تحليل الأسعار حسب مادة السوار":
    bracelet_material_prices = df.groupby('bracelet_material')['price_usd'].median().sort_values(ascending=False)
    st.markdown("### تحليل الأسعار حسب مادة السوار:")
    fig_bracelet_material_prices = px.bar(
        bracelet_material_prices,
        x=bracelet_material_prices.index,
        y=bracelet_material_prices.values,
        labels={'x': 'مادة السوار', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب مادة السوار'
    )
    st.plotly_chart(fig_bracelet_material_prices)

elif chart_option == "متوسط الأسعار حسب الجنس":
    # Calculate the median price grouped by gender
    gender_prices = df.groupby('sex')['price_usd'].median().reset_index()
    gender_prices.rename(columns={'price_usd': 'median_price'}, inplace=True)

    # Calculate the count of watches by gender
    gender_counts = df['sex'].value_counts().reset_index()
    gender_counts.columns = ['sex', 'count']

    # Merge the median price and count data into a single DataFrame
    gender_data = pd.merge(gender_counts, gender_prices, on='sex', how='left')

    # Calculate the percentage distribution
    gender_data['percentage'] = (gender_data['count'] / gender_data['count'].sum()) * 100

    # Create the pie chart
    fig = px.pie(
        gender_data,
        names='sex',
        values='count',
        title="توزيع الساعات حسب الجنس ومتوسط الأسعار",
        hover_data={'median_price': True, 'percentage': ':.2f'},
        labels={'sex': 'الجنس', 'count': 'عدد الساعات'}
    )

    # Customize the hover template
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>عدد الساعات: %{value}<br>متوسط السعر: %{customdata[0]:,.0f}$<br>النسبة: %{customdata[1]:.2f}%"
    )

    # Display the pie chart in Streamlit
    st.plotly_chart(fig)




# Additional insights section
st.subheader("نقاط إضافية مهمة")
st.markdown("""
- متوسط الأسعار يختلف بين الساعات الرجالية والنسائية بشكل ملحوظ.
- مادة السوار (جلد، معدن، سيراميك) ممكن تؤثر على السعر.
- حالة الساعة (جديدة، مستعملة) لها تأثير مباشر على قيمتها.
""")














########## OLD CODE ##########

    ## Case material prices analysis It was with the same code as the bracelet material prices analysis
    # selected_year = st.selectbox("اختر السنة لتحليل الأسعار حسب مادة الساعة:", df['year_of_production'].unique())
    # year_filtered_df = df[df['year_of_production'] == selected_year]
    # case_material_prices = year_filtered_df.groupby('case_material')['price_usd'].median().sort_values(ascending=False)
    # st.markdown("### تحليل الأسعار حسب مادة الساعة:")
    # st.bar_chart(case_material_prices)

# Interactive filters for watch specifications
# st.header("اختر مواصفات الساعة:")
# brand = st.selectbox("البراند", df['brand'].unique())
# movement = st.selectbox("نوع الحركة", df[df['brand'] == brand]['movement'].unique())
# case_material = st.selectbox("مادة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement)]['case_material'].unique())
# bracelet_material = st.selectbox("مادة السوار", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material)]['bracelet_material'].unique())
# year_of_production = st.selectbox("سنة التصنيع", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material)]['year_of_production'].unique())
# condition = st.selectbox("حالة الساعة", df[(df['brand'] == brand) & (df['movement'] == movement) & (df['case_material'] == case_material) & (df['bracelet_material'] == bracelet_material) & (df['year_of_production'] == year_of_production)]['condition'].unique())

# # Filter data based on selected criteria
# filtered_data = df[
#     (df['brand'] == brand) &
#     (df['movement'] == movement) &
#     (df['case_material'] == case_material) &
#     (df['bracelet_material'] == bracelet_material) &
#     (df['year_of_production'] == year_of_production) &
#     (df['condition'] == condition)
# ]

# # Display available watches based on the selected filters
# st.subheader("الساعات المتوفرة:")
# filtered_data['price_range'] = filtered_data.groupby('model')['price_usd'].transform(lambda x: f"${x.min()} - ${x.max()}")
# filtered_data = filtered_data.drop_duplicates(subset=['model'])
# st.write(filtered_data[['model', 'price_range']])  # Display filtered watch details

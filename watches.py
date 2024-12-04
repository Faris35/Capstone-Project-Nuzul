# Import necessary libraries
import streamlit as st  # Streamlit for building the interactive web app
from PIL import Image  # To handle image loading and manipulation
import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For plotting charts
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
import plotly.express as px  # For interactive visualizations
import plotly.graph_objects as go  # For creating detailed plotly graphs
from plotly.subplots import make_subplots  # For creating subplots
import numpy as np  # For numerical computing
import requests  # For making HTTP requests

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
st.markdown("""
    <style>
        .main-title {
            font-family: 'Georgia', sans-serif;
            font-size: 30px;
            font-weight: bold;
            color: #3b1277; /* Smooth blue color for the title */
            #text-align: center;
            margin-top: 50px; /* Space above the title */
            line-height: 1.4;
        }
    </style>
    <div class="main-title">
        ساعتك مو للزينة بس تقدر تستثمر فيها، خلها زينة وخزينة!
    </div>
""", unsafe_allow_html=True)

# Adding a description and context for the app


st.markdown("""
        <style>
        .custom-text {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: 400; /* Regular weight for better readability */
            color: #444444; /* Neutral dark gray for both light and dark modes */
            text-align: justify;
            line-height: 1.8; /* Comfortable line spacing */
            margin-bottom: 20px; /* Space below the text */
        }
        .highlight {
            color: #6D9DC5; /* Gold color to emphasize certain phrases */
            font-weight: bold;
        }
        </style>
        <div class="custom-text">
            فكرت تشتري ساعة غالية؟ يقولون الساعات الفخمة مو بس زينة، لكنها استثمار يرفع قيمتها مع الوقت. والمؤثرين يتكلمون عنها كأنها الذهب الجديد، لكن هل كلامهم صحيح؟

        في "زينة وخزينة"، حللنا سوق الساعات عشان نفهم وش يفرق بين الماركات ونترك الحكم لك. جمعنا البيانات من موقع "Chrono24"، المتخصص في بيع الساعات الجديدة والمستعملة، لتقديم صورة واضحة تساعدك في معرفة إذا كانت الساعات الفاخرة مجرد زينة أم استثمار حقيقي

        </div>
        """, unsafe_allow_html=True)

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


st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown("#### هل سوق الساعات في نمو مستمر؟")

st.markdown("""قُدّر حجم سوق الساعات الفاخرة بحوالي 42.9 مليار دولار أمريكي في عام 2022، ومن المتوقع أن ينمو من 45.1 مليار دولار أمريكي في عام 2023 إلى 68.2 مليار دولار أمريكي بحلول عام 2032، بمعدل نمو سنوي مركب (CAGR) يبلغ 5.30% خلال فترة التوقعات (2024 - 2032). يُعدّ الاتجاه المتزايد بين البالغين لارتداء الساعات الفاخرة كرمز للمكانة الاجتماعية أحد أبرز العوامل التي تُحفّز نمو هذا السوق.
المصدر: [Market Research Future](https://www.marketresearchfuture.com/reports/luxury-watch-market-10897) """)

# Corrected data for the chart
years = np.arange(2018, 2032 + 1)  # 15 years from 2018 to 2032
market_sizes = [20, 25, 30, 35, 42.9, 45.1, 50, 52, 55, 60, 62, 64, 66, 68, 68.2]  # 15 values to match the years

# Create the line chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, market_sizes, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)

# Add labels to points
for i, txt in enumerate(market_sizes):
    ax.annotate(f'{txt}', (years[i], market_sizes[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

# Customize the chart
ax.set_title('Luxury Watch Market', fontsize=16, fontweight='bold')
ax.set_ylabel('Market Size in USD Bn', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_ylim(0, 75)  # Adjust y-axis limit for better visibility

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


st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
### بعد دراسة البيانات وخصائص الساعات، تبين أن قيمة الساعة تختلف بناءً على العوامل التالية:
""")

st.image("feature.png", use_column_width=True)



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
    
    # Add a description for the chart
    st.markdown("""
        يعكس هذا الرسم البياني توزيع أسعار الساعات حسب حالتها والعلامة التجارية. 
        يساعدنا هذا التحليل في فهم تأثير حالة الساعة (مثل جديدة، غير مستخدمة، بحالة جيدة) 
        على قيمتها السوقية، مع تسليط الضوء على العلامات التجارية التي تقود السوق في الفئات ذات الأسعار العالية.
    """)
    
    if selected_brand != "All Brands":
        # Filter the data for the selected brand
        filtered_data = df[df['brand'] == selected_brand].copy()

        # Add year_of_production to model for display
        filtered_data['model_with_year'] = filtered_data['model'] + " (" + filtered_data['year_of_production'].astype(str) + ")"

        # Group by 'condition' and 'model_with_year'
        condition_model_prices = filtered_data.groupby(['condition', 'model_with_year'])['price_usd'].median().reset_index()

        # Limit to top 20 models by median price
        top_models = (
            condition_model_prices
            .groupby('model_with_year')['price_usd']
            .median()
            .sort_values(ascending=False)
            .head(20)
            .index
        )
        condition_model_prices = condition_model_prices[condition_model_prices['model_with_year'].isin(top_models)]

        # Create a Sunburst chart with 'condition' and 'model_with_year' as hierarchical levels
        fig = px.sunburst(
            condition_model_prices,
            path=['condition', 'model_with_year'],  # Hierarchical levels: Condition > Model (with year)
            values='price_usd',                     # Size of the segments
            color='price_usd',                      # Color based on price
            color_continuous_scale='viridis',
            title=f"تحليل الأسعار حسب حالة الساعة والموديلات (مع سنة التصنيع) للماركة: {selected_brand}",
        )
    else:
        # Group by 'condition' and 'brand' for all data
        condition_brand_prices = df.groupby(['condition', 'brand'])['price_usd'].median().reset_index()

        # Create a Sunburst chart with 'condition' and 'brand' as hierarchical levels
        fig = px.sunburst(
            condition_brand_prices,
            path=['condition', 'brand'],  # Hierarchical levels: Condition > Brand
            values='price_usd',          # Size of the segments
            color='price_usd',           # Color based on price
            color_continuous_scale='viridis',
            title="تحليل الأسعار حسب حالة الساعة والماركة",
        )

    # Render the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


elif chart_option == "تحليل الأسعار حسب حجم الساعة":
    # Add a description for the chart
    st.markdown("""
        يعكس هذا الرسم البياني العلاقة بين حجم الساعة (بالمليمتر) وقيمتها السوقية بالدولار الأمريكي، 
        مع توزيع النقاط حسب العلامة التجارية. يساعد هذا التحليل في فهم تأثير حجم الساعة على السعر 
        واستكشاف العلامات التجارية التي تركز على أحجام محددة وتستهدف فئات سعرية معينة.
    """)

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
    st.markdown("الساعات زي ريتشارد ميل تتميز بموادها الفريدة وتصاميمها المبتكرة اللي تجمع بين الخفة والمتانة، عشان كذا أسعارها مرتفعة.")
    st.markdown("بالذات موديلات مثل RM 055 وRM 035 غالية لأنها مصنوعة من كربون TPT، وتعاونهم مع رياضيين كبار زي نادال يرفع قيمتها أكثر.")

    st.plotly_chart(fig_model_prices)
   
elif chart_option == "تحليل الأسعار حسب نوع الحركة":
    movement_prices = df.groupby('movement')['price_usd'].median().sort_values(ascending=False)
    
    st.markdown("""
        <style>
        .custom-text {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: 400; /* Regular weight for better readability */
            color: #444444; /* Neutral dark gray for both light and dark modes */
            text-align: justify;
            line-height: 1.8; /* Comfortable line spacing */
            margin-bottom: 20px; /* Space below the text */
        }
        
        </style>
        <div class="custom-text">
        تلعب حركة الساعة (نوع الميكانيكية التي تديرها) دورًا كبيرًا في تحديد قيمتها. في عالم الساعات الفاخرة، تختلف الأسعار بناءً على نوع الحركة، حيث يعكس ذلك تعقيد التصميم ومستوى الحرفية. يوضح الرسم البياني التالي متوسط أسعار الساعات حسب نوع الحركة:
        </div>
        """, unsafe_allow_html=True)

    fig_movement_prices = px.bar(
        movement_prices,
        x=movement_prices.index,
        y=movement_prices.values,
        labels={'x': 'نوع الحركة', 'y': 'السعر بالدولار'},
        title='تحليل الأسعار حسب نوع الحركة'
    )
    fig_movement_prices.update_layout(
    xaxis_title="<b>نوع الحركة</b>",
    yaxis_title="<b>السعر بالدولار</b>",
    title_font=dict(size=18, family="Arial"),
    xaxis=dict(
        tickfont=dict(size=12, family="Arial", weight="bold",color="black")
    ),
    yaxis=dict(
        tickfont=dict(size=12, family="Arial", weight="bold")
    ))
    st.plotly_chart(fig_movement_prices)
    st.markdown('من الرسم البياني يوضح لك إن الساعات اللي بحركة يدوية (manual winding) وأوتوماتيكية (automatic) هي الأغلى، لأنها تعكس الحرفية العالية والجودة في التصميم.')

 


elif chart_option == "ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)":
    st.markdown("""
        <style>
        .custom-text {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: 400; /* Regular weight for better readability */
            color: #444444; /* Neutral dark gray for both light and dark modes */
            text-align: justify;
            line-height: 1.8; /* Comfortable line spacing */
            margin-bottom: 20px; /* Space below the text */
        }
        .highlight {
            color: #6D9DC5; /* Gold color to emphasize certain phrases */
            font-weight: bold;
        }
        </style>
        <div class="custom-text">
        يعكس هذا الرسم البياني توزيع عدد الساعات حسب المادة المستخدمة في تصنيع هيكلها عبر العقود 
        <span class="highlight">(1900-2023)</span>. يساعدنا هذا التحليل في تتبع التغيرات في تفضيلات مواد التصنيع بمرور الزمن 
        وفهم الاتجاهات السائدة في سوق الساعات الفاخرة.
        </div>
        """, unsafe_allow_html=True)

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
        #title='تحليل الأسعار حسب مادة السوار'
    )

    st.write("""
    بناءً على البيانات، المواد زي **البلاتين** والذهب (الوردي والأبيض) تستهدف اللي يدورون الفخامة والقيمة العالية، 
    بينما مواد زي **الستانلس ستيل** أو السيراميك تناسب الناس اللي يبغون ساعات عملية وقوية للاستخدام اليومي.
    """)

    st.write("""
    المثير للاهتمام إن مواد نادرة زي **جلد القرش** و**جلد الثعبان**، وعلى الرغم من التوقعات بأنها بتكون غالية، 
    إلا إنها طلعت بأسعار أقل بكثير، مما يعكس إنها موجهة لمحبي التميز بأسعار معقولة بدل ما تكون رمز فخامة بحت.
    """)

    st.plotly_chart(fig_bracelet_material_prices)

elif chart_option == "متوسط الأسعار حسب الجنس":
    gender_stats = df.groupby('sex').agg({'price_usd': 'median', 'model': 'count'}).reset_index()
    gender_stats.columns = ['sex', 'median_price', 'count']

    # Create the dual-axis bar and line chart
    fig_dual_axis = make_subplots(specs=[[{"secondary_y": True}]])

    # Add bar chart for the number of watches
    fig_dual_axis.add_trace(
        go.Bar(x=gender_stats['sex'], y=gender_stats['count'], name='عدد الساعات', marker_color='blue'),
        secondary_y=False,
    )

    # Add line chart for the median price
    fig_dual_axis.add_trace(
        go.Scatter(x=gender_stats['sex'], y=gender_stats['median_price'], name='متوسط السعر', marker_color='red', mode='lines+markers'),
        secondary_y=True,
    )

    # Update layout
    fig_dual_axis.update_layout(
        title_text="عدد الساعات ومتوسط السعر حسب الجنس",
        xaxis_title="الجنس",
        yaxis_title="عدد الساعات",
        yaxis2_title="متوسط السعر بالدولار",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.write('بناءً على البيانات، يظهر إن عدد الساعات الرجالية أكبر من النسائية، ومتوسط أسعارها أعلى. هذي الأرقام تعكس طبيعة السوق بدون أي تحيز، لكنها توضح الفروقات في المعروض والأسعار بين الفئتين.')

    # Render the dual-axis chart in Streamlit
    st.plotly_chart(fig_dual_axis)


# Additional insights section
st.write("""
""")

# List of Factors
st.markdown("""
### ختامًا، إذا كنت تفكر تشتري ساعة، فيه كم نقطة مهمة لازم تحطها ببالك:
- متوسط الأسعار يفرق بين الساعات الرجالية والنسائية.  
- حالة الساعة، إذا هي جديدة أو مستعملة، ومادة السوار لها تأثير كبير على قيمتها.  
- الماركات العالمية زي **Richard Mille** تحافظ على قيمتها وتعتبر استثمار مربح.  
- المواد الفخمة زي الذهب الوردي والبلاتين تضيف قيمة عالية للساعة.  
""")

# Conclusion
st.write("""
هالنقاط بتساعدك تختار الساعة اللي تناسبك سواء كشكل أو كاستثمار ذكي.
""")

# Load the dataset
df = pd.read_csv('Final_version4_all_watches.csv')  # Ensure the file exists in the correct location

# Dropdown for Brand Selection
selected_brand = st.selectbox("اختر العلامة التجارية:", sorted(df['brand'].unique()))

# Filter the models based on the selected brand
filtered_models = df[df['brand'] == selected_brand]

# Dropdown for Model Selection
selected_model = st.selectbox("اختر الموديل:", sorted(filtered_models['model'].unique()))

# Filter the years based on the selected brand and model
filtered_years = filtered_models[filtered_models['model'] == selected_model]

# Dropdown for Year Selection
selected_year = st.selectbox("اختر سنة التصنيع:", sorted(filtered_years['year_of_production'].unique()))

if st.button("عرض معلومات الساعة"):
    # Extract the reference for the selected row
    selected_row = filtered_years[
        (filtered_years['model'] == selected_model) & 
        (filtered_years['year_of_production'] == selected_year)
    ]

    # Check if the reference exists
    if not selected_row.empty and 'ref' in selected_row.columns:
        reference = selected_row.iloc[0]['ref']
        st.write(f"تم استخراج الرقم المرجعي: {reference}")

        # Use the extracted reference as input for the API
        api_key = "Q54K647We9a6QAitZA9Wn5rn9l3I2P9i3O53VuZ8"
        search_url = f'https://api.watchcharts.com/v3/search/watch?brand_name={selected_brand}&reference={reference}'

        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }

        response = requests.get(search_url, headers=headers)

        # Display the API response
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'results' in data:
                results = data['results']
                if len(results) > 0:
                    uuid = results[0].get('uuid', None)
                    st.success(f"تم استخراج UUID: {uuid}")
                    
                    # Step 2: Use the UUID to make the second request
                    info_url = f'https://api.watchcharts.com/v3/watch/info?uuid={uuid}'
                    info_response = requests.get(info_url, headers=headers)

                    if info_response.status_code == 200:
                        info_data = info_response.json()

                        # Extract data with proper handling for missing values
                        market_price = info_data.get('market_price')
                        dealer_price = info_data.get('dealer_price')
                        market_price_formatted = f"${market_price:,.2f}" if market_price else "N/A"
                        dealer_price_formatted = f"${dealer_price:,.2f}" if dealer_price else "N/A"

                        st.subheader("تفاصيل الساعة")
                        st.write("فيما يلي المعلومات التفصيلية عن الساعة:")
                        st.markdown(f"""
                            - **العلامة التجارية**: {info_data.get('brand', 'N/A')}
                            - **المجموعة**: {info_data.get('collection', 'N/A')}
                            - **الموديل**: {info_data.get('model', 'N/A')}
                            - **السعر في السوق**: {market_price_formatted}
                            - **سعر التاجر**: {dealer_price_formatted}
                            - **التقلب**: {info_data.get('volatility', 'N/A') * 100 if info_data.get('volatility') else 'N/A'}%
                            - **آخر تحديث**: {info_data.get('updated', 'N/A')}
                        """)
                    else:
                        st.error(f"خطأ أثناء جلب تفاصيل الساعة: {info_response.status_code}")
                else:
                    st.warning("لم يتم العثور على نتائج.")
            else:
                st.error("لم يتم استرجاع البيانات بشكل صحيح.")
        else:
            st.error(f"خطأ في طلب API: {response.status_code}")

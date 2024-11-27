# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

st.set_page_config(page_title="زينة وخزينة", page_icon=":watch:", layout="wide")

rtl_css = """
<style>
body {
    direction: rtl;
    text-align: center;
}
</style>
"""



st.markdown(rtl_css, unsafe_allow_html=True)

st.image("logo.png", width=700)
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 70px; 
        font-weight: bold;
        text-align: right; 
        color: #fff;
    }

    .stMarkdown p {
        font-size: 30px;
        font-weight: normal;
        text-align: right;
        color: #333;
        line-height: 1.6 !important;
    }

    div.stSelectbox > label {
        font-size: 60px !important;  /* Adjust label font size */
    }
        div.stSelectbox select {
        font-size: 50px !important; /* Adjust select options font size */
        height: 50px !important; /* Adjust height */
        width: 300px !important; /* Adjust width for better visibility */
    }

    /* Style for checkbox label */
    div.stCheckbox label {
        font-size: 60px !important; /* Adjust checkbox label font size */
    }
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; /* Three columns */
        gap: 10px; /* Spacing between grid items */
        text-align: center;
        
        
    }
    .widget {
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        font-size: 30px;
        text-align: right;
        color: #333;
        line-height: 1.6 !important;
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
    """,
    unsafe_allow_html=True
)
#---------------------------------------------------------------------------------------------------------
# Load data
df = pd.read_csv('Final_version4_all_watches.csv')
#----------------------------------------------------------------------------------------------------------
# Title
# Introduction with a rectangle background
st.markdown(
    """
    <style>
        .custom-container {
            background-color: #9e9085; 
            border: 2px solid #ccc;     
            border-radius: 10px;       
            padding: 70px;              
            margin: 20px 0;            
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
            font-size: 50px;           
            line-height: 1.8;          
            text-align: right;         
            color: #000;                
          
        }
    </style>
    <div class="custom-container">
        فكرت تشتري ساعة غالية؟ يقولون الساعات الفخمة مو بس زينة،
        لكنها استثمار يرفع قيمتها مع الوقت.
        <br>
        والمؤثرين يتكلمون عنها كأنها الذهب الجديد،
        لكن هل كلامهم صحيح؟
        في "زينة وخزينة" حللنا سوق الساعات عشان نفهم وش يفرق بين الماركات ونترك الحكم لك.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------------------------
url = "https://www.chrono24.com/"
logo_path = "./logo-positive-reduced.svg"
col1, col2, col3 = st.columns(3)

# Column 1: Logo with title
with col1:
    st.markdown("<h3 style='text-align: center; font-weight: bold; color: #5C4D4D;'>المصدر</h3>", unsafe_allow_html=True)
    st.image(logo_path, width=150)
    st.markdown(f"[للإطلاع]({url})", unsafe_allow_html=True)

# Column 2: Watches text with title
with col2:
    st.markdown("<h3 style='text-align: center; font-weight: bold; color: #5C4D4D;'>حجم البيانات</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-weight: normal; color: #2C2A2A;'>40,000+<br>ساعة</h4>", unsafe_allow_html=True)

# Column 3: Widgets in a 3x3 grid with title
with col3:
    st.markdown("<h3 style='text-align: center; font-weight: bold; color: #5C4D4D;'>شكل البيانات</h3>", unsafe_allow_html=True)
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

# Adjusted styling for the rest of the content
st.markdown("#### هل سوق الساعات في نمو مستمر؟", unsafe_allow_html=True)


#---------------------------------------------------------------------------------------------------------------
col1, col2 = st.columns([1, 2]) 
with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
         هل سوق الساعات في نمو مستمر؟

        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("""<p style="font-size: 16px; color: #2C2A2A; line-height: 1.5;">قُدّر حجم سوق الساعات الفاخرة بحوالي 42.9 مليار دولار أمريكي في عام 2022، ومن المتوقع أن ينمو من 45.1 مليار دولار أمريكي في عام 2023 إلى 68.2 مليار دولار أمريكي بحلول عام 2032، بمعدل نمو سنوي مركب (CAGR) يبلغ 5.30% خلال فترة التوقعات (2024 - 2032). يُعدّ الاتجاه المتزايد بين البالغين لارتداء الساعات الفاخرة كرمز للمكانة الاجتماعية أحد أبرز العوامل التي تُحفّز نمو هذا السوق.</p>""", unsafe_allow_html=True)
    st.markdown("المصدر: [Market Research Future](https://www.marketresearchfuture.com/reports/luxury-watch-market-10897)", unsafe_allow_html=True)


with col2:
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
#-----------------------------
st.markdown(""" ### بعد ما أخذنا فكرة عن سوق الساعات ونموه، خلونا نركز على التفاصيل أكثر ونشوف وش الماركات اللي تسيطر على قائمة الأغلى، وهل دايم السعر يعكس الانتشار والشعبية؟""")

#------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
col1, col2 = st.columns([1, 2]) 
with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
             تدري وش الماركات اللي تتصدر أغلى الساعات بالعالم؟
             تتوقع **رولكس** الأولى؟ 
             المفاجأة إنها حتى مو ضمن اغلى خمس ماركات!
             مثلًا، **Richard Mille** و **Patek Philippe** متصدرين القائمة بأسعار عالية جدًا.
             لكن إذا جينا للساعات اللي تشوفها بشكل أكبر أو تنتشر بين عشاق الساعات، الوضع يختلف!
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    top_brands_all = df.groupby('brand')['price_usd'].median().sort_values(ascending=False).head(10)

    fig = px.bar(top_brands_all, 
                 x=top_brands_all.index, 
                 y=top_brands_all.values, 
                 labels={'x': 'العلامات التجارية', 'y': 'السعر المتوسط بالـ USD'},
                 title="متوسط الأسعار لأغلى عشر ماركات:")

    fig.update_layout(
        width=1000,  
        height=900,  
        title_font_size=35,  
        xaxis_title_font_size=35,  
        yaxis_title_font_size=35, 
        xaxis_tickfont_size=20,  
        yaxis_tickfont_size=20
    )
    st.plotly_chart(fig)
#-----------------------------------------------

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
             شفنا أغلى الماركات، بس وش الأكثر انتشاراً؟:
             رولكس هنا تتصدر المشهد.
             رغم إنها مو الأغلى، إلا إنها الأكثر شعبية وتواجد بين عشاق الساعات.
             ليش؟ لأنها جمعت بين الفخامة والجودة بسعر يعتبر معقول نسبيًا مقارنة بالباقين.
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    popular_brands = df['brand'].value_counts().head(10).reset_index()
    popular_brands.columns = ['brand', 'count']

# Assigning a color based on brand
    popular_brands['color'] = popular_brands['brand'].apply(lambda x: 'red' if x == 'Rolex' else 'blue')

# Creating a bar chart using plotly express
    fig2 = px.bar(
         popular_brands,
         x='brand',
         y='count',
         color='color',
         color_discrete_map={'red': 'red', 'blue': 'blue'},
         title="أكثر العلامات انتشاراً",
         labels={'brand': 'العلامة التجارية', 'count': 'عدد الساعات'}
    )
    fig.update_layout(
        width=1000,  
        height=900,  
        title_font_size=35,  
        xaxis_title_font_size=35,  
        yaxis_title_font_size=35, 
        xaxis_tickfont_size=20,  
        yaxis_tickfont_size=20
    )

# Adding black edges to the bars
fig2.update_traces(marker=dict(line=dict(width=1, color='black')))

# Displaying the chart in Streamlit
st.plotly_chart(fig2)
#----------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.image("feature.png", use_column_width=True)


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
        "تحليل الأسعار حسب مادة السوار",
        "متوسط الأسعار حسب الجنس"
    ]
)

# Display the selected chart
if chart_option == "تحليل الأسعار حسب حالة الساعة":
    condition_prices = df.groupby('condition')['price_usd'].median().sort_values(ascending=False)

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب حالة الساعة:")

    with col2:
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
        # ... other brands
    }

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب حجم الساعة:")

    with col2:
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
            xaxis_title="الحجم (mm)",
            yaxis_title="السعر (دولار أمريكي)",
            legend_title="البراند",
            legend=dict(orientation="v", x=1.05, y=1)  # Adjust legend position
        )

        st.plotly_chart(fig_size_price_bubble)

elif chart_option == "تحليل الأسعار حسب سنوات التصنيع":
    yearly_prices = df.groupby('year_of_production')['price_usd'].median()

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب سنوات التصنيع:")

    with col2:
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

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب الموديل:")
        st.markdown("الساعات زي ريتشارد ميل تتميز بموادها الفريدة وتصاميمها المبتكرة اللي تجمع بين الخفة والمتانة، عشان كذا أسعارها مرتفعة.")
        st.markdown("بالذات موديلات مثل RM 055 وRM 035 غالية لأنها مصنوعة من كربون TPT، وتعاونهم مع رياضيين كبار زي نادال يرفع قيمتها أكثر.")

    with col2:
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

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب نوع الحركة:")
        st.markdown('من الرسم البياني يوضح لك إن الساعات اللي بحركة يدوية (manual winding) وأوتوماتيكية (automatic) هي الأغلى، لأنها تعكس الحرفية العالية والجودة في التصميم.')


    with col2:
        fig_movement_prices = px.bar(
            movement_prices,
            x=movement_prices.index,
            y=movement_prices.values,
            labels={'x': 'نوع الحركة', 'y': 'السعر بالدولار'},
            title='تحليل الأسعار حسب نوع الحركة'
        )
        st.plotly_chart(fig_movement_prices)

elif chart_option == "ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)":
    st.markdown("### ترند مواد تصنيع الهياكل حسب العِقد (1900-2023)")

    # Processing data
    filtered_df = df[(df['year_of_production'] >= 1900) & (df['year_of_production'] <= 2023)]
    filtered_df['decade'] = (filtered_df['year_of_production'] // 10) * 10
    case_material_count = filtered_df.groupby(['decade', 'case_material']).size().reset_index(name='count')

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### تحليل المواد على مر العقود:")

    with col2:
        fig_case_material = px.line(
            case_material_count,
            x='decade',
            y='count',
            color='case_material',
            markers=True,
            labels={'count': 'عدد الساعات بحسب نوع الهيكل', 'decade': 'عقد'}
        )
        st.plotly_chart(fig_case_material)

elif chart_option == "تحليل الأسعار حسب مادة السوار":
    bracelet_material_prices = df.groupby('bracelet_material')['price_usd'].median().sort_values(ascending=False)

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### تحليل الأسعار حسب مادة السوار:")

    with col2:
        fig_bracelet_material_prices = px.bar(
            bracelet_material_prices,
            x=bracelet_material_prices.index,
            y=bracelet_material_prices.values,
            labels={'x': 'مادة السوار', 'y': 'السعر بالدولار'},
            title='تحليل الأسعار حسب مادة السوار'
        )
        st.plotly_chart(fig_bracelet_material_prices)

elif chart_option == "متوسط الأسعار حسب الجنس":
    gender_prices = df.groupby('sex')['price_usd'].median().reset_index()
    gender_prices.rename(columns={'price_usd': 'median_price'}, inplace=True)
    
    gender_counts = df['sex'].value_counts().reset_index()
    gender_counts.columns = ['sex', 'count']

    gender_data = pd.merge(gender_counts, gender_prices, on='sex', how='left')
    gender_data['percentage'] = (gender_data['count'] / gender_data['count'].sum()) * 100

    # Create two columns: one for markdown and one for the chart
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### توزيع الساعات حسب الجنس ومتوسط الأسعار:")

    with col2:
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

        st.plotly_chart(fig)


#---------------------------------------------------------------------------------------------------------------

st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# Conclusion and Recommendations
# TODO - Rewrite the recommendations
st.markdown(
    """
    <h1 style="font-size: 40px; text-align: center; color: #333;">توصيات أخيرة:</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("""
بعد ما استعرضنا تأثير الخصائص المختلفة على سعر الساعات، نحب نشارك معك بعض التوصيات التي يمكن أن تساعدك في اتخاذ القرار الأفضل للاستثمار:
""")
st.markdown("""
1. **اختيار الماركات الشهيرة:**

2. **الحجم مهم:** 

3. **سنة التصنيع:** 

4. **الموديلات النادرة:** 
            
5. **نوع الحركة والمادة:** 
""")

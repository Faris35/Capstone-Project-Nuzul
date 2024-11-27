# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(page_title="زينة وخزينة", page_icon=":watch:", layout="wide")

rtl_css = """
<style>
body {
    direction: rtl;
    text-align: right;
}
</style>
"""


st.markdown(rtl_css, unsafe_allow_html=True)

st.image("logo.png", width=600)

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





#----------------------------------------------------------------------------------------------------------------
col1, col2 = st.columns([1, 2]) 
with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            أفضل عشر ماركات فاخرة من ناحية
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
#------------------------------------------------------------------------------------------------------------------------------

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            أكثر عشر ماركات انتشاراً:
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    popular_brands = df['brand'].value_counts().head(10)

    # Create the bar chart using Plotly Express
    fig = px.bar(popular_brands, 
                 x=popular_brands.index, 
                 y=popular_brands.values, 
                 labels={'x': 'العلامات التجارية', 'y': 'عدد المرات'},
                 title="أكثر عشر ماركات انتشاراً:")

    # Update layout for the rectangular shape and axis sizes
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
#----------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.image("feature.png", use_column_width=True)


with st.container():
    brand_options = ['All'] + top_brands_all.index.tolist()
    brand_filter = st.selectbox('اختر البراند', brand_options)

# Filter the dataframe based on the selected brand
if brand_filter != "All":
    filtered_df = df[df['brand'] == brand_filter]
else:
    filtered_df = df
#-------------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 1. الحجم (Size) 
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            تحليل تأثير الحجم على السعر:
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    fig_size_price_bubble = px.scatter(
        filtered_df,
        x='size_mm',
        y='price_usd',
        size='price_usd',
        color='brand',
        hover_name='model',
        title=f'الحجم والسعر للبراند {brand_filter}',
        labels={'size_mm': 'الحجم (mm)', 'price_usd': 'السعر (دولار أمريكي)'}
    )

    # Update layout for improved appearance
    fig_size_price_bubble.update_layout(
        width=1500,
        height=900,
        title_font_size=35,
        xaxis_title_font_size=35,
        yaxis_title_font_size=35,
        xaxis_tickfont_size=20,
        yaxis_tickfont_size=20,
        legend_title_font_size=20
    )

    st.plotly_chart(fig_size_price_bubble)
#------------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 2. سنة التصنيع (Year of Production) - Line chart
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
         <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            تحليل تأثير السنة على السعر:
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    yearly_prices = filtered_df.groupby('year_of_production')['price_usd'].mean()
    fig_yearly_prices = px.line(
        x=yearly_prices.index,
        y=yearly_prices.values,
        labels={'x': 'سنة الصنع', 'y': 'متوسط السعر (دولار أمريكي)'},
        title=f"تحليل اختلاف الأسعار على حسب سنة الصنع - {brand_filter}"
    )
    fig_yearly_prices.update_layout(
        width=900,
        height=600,  
        title_font_size=35,
        xaxis_title_font_size=30,
        yaxis_title_font_size=30,
        xaxis_tickfont_size=20,
        yaxis_tickfont_size=20,
        legend_title_font_size=20,
        margin=dict(t=50, l=50, b=50, r=50) 
    )

    st.plotly_chart(fig_yearly_prices, use_container_width=True)


#--------------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 3. الموديل (Model) - Best model regarding the highest price

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            تحليل الموديلات الأفضل من حيث السعر:
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    top_models = filtered_df.groupby('model')['price_usd'].mean().sort_values(ascending=False).head(10)

    fig_model = px.bar(
        top_models, 
        x=top_models.index, 
        y=top_models.values, 
        title=f'أفضل موديلات حسب السعر للبراند {brand_filter}', 
        labels={'x': 'الموديل', 'y': 'متوسط السعر (دولار أمريكي)'}
    )

    fig_model.update_layout(
        width=1000,
        height=900,
        title_font_size=30,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont_size=15,
        yaxis_tickfont_size=15,
        legend_title_font_size=18
    )
    st.plotly_chart(fig_model)

#-----------------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 4. نوع الحركة (Movement Type) - Best movement type regarding the highest price
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            تحليل نوع الحركة وتأثيره على السعر:
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    top_movements = filtered_df.groupby('movement')['price_usd'].mean().sort_values(ascending=False).head(10)

    fig_movement = px.bar(
        top_movements, 
        x=top_movements.index, 
        y=top_movements.values, 
        title=f'أفضل أنواع الحركة حسب السعر للبراند {brand_filter}', 
        labels={'x': 'نوع الحركة', 'y': 'متوسط السعر (دولار أمريكي)'}
    )
    fig_movement.update_layout(
        width=1000,
        height=900,
        title_font_size=30,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont_size=15,
        yaxis_tickfont_size=15,
        legend_title_font_size=18
    )
    st.plotly_chart(fig_movement)

#----------------------------------------------------------------------------------------------------------
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 5. مادة السوار (Bracelet Material) - Best bracelet material regarding the highest price
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; 
        align-items: right; height: 100%; font-size: 35px; text-align: right; margin-top: 400px; margin-bottom: 100px;">
            تحليل مادة السوار وتأثيرها على السعر:
        </div>
        """, unsafe_allow_html=True
    )    
with col2:
    top_bracelet_materials = filtered_df.groupby('bracelet_material')['price_usd'].mean().sort_values(ascending=False).head(10)

    fig_bracelet_material = px.bar(
        top_bracelet_materials, 
        x=top_bracelet_materials.index, 
        y=top_bracelet_materials.values, 
        title=f'أفضل مواد السوار حسب السعر للبراند {brand_filter}', 
        labels={'x': 'مادة السوار', 'y': 'متوسط السعر (دولار أمريكي)'}
    )
    fig_bracelet_material.update_layout(
        width=1000,
        height=900,
        title_font_size=30,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont_size=15,
        yaxis_tickfont_size=15,
        legend_title_font_size=18
    )
    st.plotly_chart(fig_bracelet_material)


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
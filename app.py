import streamlit as st
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline

cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

st.title('PRICE OF THE DIAMONDS ')
col1, col2, col3 ,col4= st.columns(4)
with col1:
    carat=st.number_input("CARAT VALUE",step=1.,format="%.5f")
    depth = st.number_input("DEPTH VALUE",step=1.,format="%.5f")
    table = st.number_input("TABLE VALUE",step=1.,format="%.5f")
with col2:
    x = st.number_input("X VALUE",step=1.,format="%.5f")
    y = st.number_input("Y VALUE",step=1.,format="%.5f")
    z = st.number_input("Z Value",step=1.,format="%.5f")
with col3:
    cut = st.selectbox("CUT CATEGORIES",cut_categories)
    color= st.selectbox("COLOR CATEGORIES",color_categories)
    clarity = st.selectbox("CLARITY CATEGORIES",clarity_categories)

data=CustomData(carat,depth,table,x,y,z,cut,color,clarity)

def predict():
    final_new_data=data.get_data_as_dataframe()
    predict_pipeline=PredictPipeline()
    pred=predict_pipeline.predict(final_new_data)
    results=round(pred[0],2)
    finall = 'Diamond Price = $'+str(results)
    st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{finall}</h1>', unsafe_allow_html=True)

button = st.button("PREDICT",on_click=predict)

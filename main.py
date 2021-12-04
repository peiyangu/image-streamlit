import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('Streamlit 超入門')

st.write('Interactive Widgets')

let_column, right_column = st.beta_columns(2)

button=let_column.button('右からむに文字を表示　')

if button:
    right_column.write('ここに文字を表示')
# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text,'です'

# 'コンディション:', condition


# if st.checkbox('Show Image'):
#     img = Image.open('sample.JPG')
#     st.image(img, caption='Kohei Imanishi', use_column_width=True)




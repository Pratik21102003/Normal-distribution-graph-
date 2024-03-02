import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
np.random.seed(42)
data=np.random.normal(loc=0, scale=1,size=1000)
sns.histplot(data,kde=True,stat="density")
st.sidebar.write('Normal Distribution')
def func():
   mean=st.sidebar.select_slider('Mean',options=list(range(-5,5)))
   std=st.sidebar.select_slider('std',options=list(range(1, 11)))
   return mean,std
mean,std=func()
data1=np.random.normal(loc=mean,scale=std,size=1000)
sns.histplot(data1,kde=True,stat="density")
plt.xlim(-8,8)
st.pyplot()
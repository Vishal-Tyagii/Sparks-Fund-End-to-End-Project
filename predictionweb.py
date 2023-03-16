# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 23:00:14 2023

@author: LENOVO
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model=pickle.load(open('D:/NIIT/Grooming Session/Ishan Sir 20th Feb-2023/27-Feb assignment/assignment/deploy/trained_model.sav','rb'))

def Price_prediction(input_data):
    
    prediction=loaded_model.predict([input_data])
    return prediction.astype('int64')
    

def main():  
    
    st.title('Spark Funds')
    st.title('Predict the investment')
    
    a=st.number_input('a')
    b=st.number_input('b')
    c=st.number_input('c')
    d=st.number_input('d')
    e=st.number_input('e')
    f=st.number_input('f')
    g=st.number_input('g')
    h=st.number_input('h')
    i=st.number_input('i')
    j=st.number_input('j')
    k=st.number_input('k')
    l=st.number_input('l')
    m=st.number_input('m')
    n=st.number_input('n')
    o=st.number_input('o')
    p=st.number_input('p')
    q=st.number_input('q')
    
    
    
    
    #code for prediction
    
    Investment = ''
    
    if st.button('Investment Price'):
        Investment=Price_prediction([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]) 
    
    
    st.success(Investment)

if __name__ == '__main__':
    main()
    
    
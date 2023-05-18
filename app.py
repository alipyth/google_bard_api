#pip install streamlit bardapi deep_translator
#برای مشاهده آموزش این پروژه و پیدا کردن توکن ویدیو زیر رو ببینید 
#
import streamlit as st
from bardapi import Bard
from deep_translator import GoogleTranslator

with st.form('pr'):
    inp = st.text_input('Type Anythiung')
    sub = st.form_submit_button('submit')
    if inp is not None and sub:
        token ="توکن خودتون رو اینجا قزار بدید "
        bard = Bard(token=token)
        translated = GoogleTranslator(source='fa', target='en').translate("آیا دیوید بکهام را میشناسی")
        x = bard.get_answer(translated)['content']
        en_to_fa = GoogleTranslator(source='en',target='fa').translate(x)
        st.write(en_to_fa)
        

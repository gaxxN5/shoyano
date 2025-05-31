import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon=":shark:")

#top_page = st.Page(page="pages/top_page.py", title="Top", icon=":material/home:")
#my_profile = st.Page(page="pages/myprofile.py", title="自己紹介ぺージ", icon=":material/open_with:")
#about = st.Page(page="pages/about.py", title="About", icon=":material/apps:")
#config = st.Page(page="pages/config.py", title="Config", icon=":material/settings_applications:")


#with st.sidebar:

#	st.page_link("main.py", label="Top", icon=":material/home:")
#	st.page_link("pages/2_myprofile.py", label="自己紹介ぺージ", icon=":material/open_with:")
#	st.page_link("pages/3_about.py",label="About", icon=":material/apps:")
#	st.page_link("pages/4_Visitor_main2.py", label="入館者属性", icon=":material/apps:")

st.title("multi page app")
st.image("images/osiro.png")
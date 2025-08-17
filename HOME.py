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

st.title("DATA Miningについて")
st.markdown("""#データマイニング（data mining）とは、大量のデータの中から未知の知識やパターンを発見すること、またそのための技術。膨大なデータの中から人間では見つけにくい傾向や関係性を明らかにする。ビジネスなどそれぞれの目的に役立てられる情報を抽出できる。具体的には、統計学、機械学習、人工知能などの技術を用いて、データの分析、分類、予測、パターン抽出などを行う。
""")
st.image("images/main-pict.jpg")
st.write("あなたのビジネス、もっと深く理解しませんか？— データマイニングで新たな価値を創造！")
st.markdown(
'''<div style='background-color:#f0f8ff; padding:10px; border:2px solid #add8e6;
border-radius: 8px; '>
		🌟 【ご提案】<BR>
	ビッグデータから重要な情報やパターンを抽出し、競争力を高める【データマイニングサービス】を提供します。<P>
		🔍 こんな課題にお悩みではありませんか？ <br>
		顧客の購買傾向を把握したい<br>
		効率的な販売戦略を立てたい<BR>
		経営の意思決定をデータドリブンにしたい<BR>
		商品・サービスの改善ポイントを見つけたい<p>
		🚀 【データマイニングの強み】<BR>
		大量のデータから隠れたパターンや関係性を発見<BR>
		未来予測やリスク分析が可能に<BR>
		顧客満足度や売上アップに直結する施策の立案支援<p>
#		🎁 今だけの特典！<BR>
#		無料のデモやコンサルテーション実施中！<BR>
#		まずはお気軽にご相談ください。<P>
#		📞 お問い合わせはコチラ<BR>
#		電話：〇〇〇-〇〇〇-〇〇〇〇<BR>
#		メール：〇〇〇@〇〇〇.com<BR>
</div>''',
unsafe_allow_html=True

)



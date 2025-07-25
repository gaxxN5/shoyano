import streamlit as st
#from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from streamlit.column_config import Column
import pydeck as pdk
import plotly.express as px
import matplotlib.pyplot as plt

#①読み込まれたデータ
st.write('参照した入館者数データ(5月5日)')
df = pd.read_csv('訪問客属性3.csv')
st.write("①参照データ")
st.dataframe(df)


#②都道府県別表＆グラフ（df2,df3,df_grouped,df4 )
df_grouped = df.groupby('都道府県').sum()

df2 = df_grouped
df3 = df2.drop(labels=['作成日時','時間','分','lat','long','性別','年代','車種','用途名'],axis=1)

column_config = {
    "都道府県": Column(
        label="都道府県名",
        width=90,
        help="都道府県の名前を表示します。"
    ),
    "No.": Column(
        label="訪問者数",
        width=70,
        help="数の並べ替えができます",
        required=True
    ),
    
}

#＊日本地図

# 都道府県ごとの中心座標を定義
prefecture_coordinates = {
	"福岡県":(33.599679,130.682867),
	"佐賀県" :(33.279436,130.118294),
	"長崎県" :(32.955619,129.715641),
	"山口県":(34.226281,131.430559),
	"大分県" :(33.203809,131.411655),
	"鹿児島県" :(31.355836,130.410976),
	"島根県":(34.975087,132.423277),
	"香川県" :(34.219680,133.979044),
	"北海道" :(43.420962,142.781281),
	"愛知県":(35.002511,137.208724),
	"大阪府" :(34.598366,135.545261),
	"千葉県" :(35.473969,140.222304),
	"宮崎県":(32.200128,131.353483),
	"広島県" :(34.588492,132.792091),
	"東京都" :(35.686991,139.539242),
	"熊本県":(32.587230,130.807836)
}

#各都市のデータを定義
sales_data = {

	"福岡県":359,
	"佐賀県":172,
	"長崎県":72,
	"山口県":21,
	"大分県":34,
	"鹿児島県":13,
	"島根県":26,
	"香川県":22,
	"北海道":21,
	"愛知県":20,
	"大阪府":14,
	"千葉県":13,
	"宮崎県":11,
	"広島県":11,
	"東京都":10,
	"熊本県":33
}


#データフレームを作成
df4 = pd.DataFrame ({

	'prefecture': list (prefecture_coordinates. keys() ),

	'lat': [prefecture_coordinates [p] [0] for p in prefecture_coordinates],
	'lon': [prefecture_coordinates [p] [1] for p in prefecture_coordinates],
	'sales': list (sales_data. values())

})

#日本地図の描画
# Pydeck の Deck オブジェクトを作成
deck = pdk.Deck(
	map_style="mapbox://styles/mapbox/light-v9",
	initial_view_state=pdk.ViewState(
	latitude=34.598366, # 大阪府の緯度
	longitude=135.545261, # 大阪府の経度
	zoom=4.5,
	pitch=55,
	use_container_width=False,width=None, height=None,
),
layers=[
	pdk.Layer(
	#'ArcLayer',
	'ColumnLayer',
	data=df4,
	get_position='[lon, lat]',
	get_elevation='sales',
	elevation_scale=400, #売上データのスケーリング
	radius=10000,#円柱の底面の半径
	get_fill_color='[200, 30, 0, 160]',
	pickable=True,
	auto_highlight=True,
	),

],
height=50
)

#コラム分け
col1,col2 = st.columns([1,3])


#③データの表示
with col1:
	st.write('②都道府県別合計')
	st.dataframe(df3, column_config=column_config,width=160)



with col2:
	# Streamlit アプリのタイトルを設定
	st.write("------------------------------------------------")
	# Pydeck チャートを Streamlit アプリに表示
	#st.pydeck_chart (deck, unsafe_allow_html=True)
	st.pydeck_chart (deck, use_container_width=True)
	
	


#車用途別（df5,df6,df_grouped2 )
df_grouped2 = df.groupby('用途名').sum()

df5 = df_grouped2
df6 = df5.drop(labels=['作成日時','時間','分','都道府県','lat','long','性別','年代','車種'],axis=1)

st.write('③駐車場での車の用途別台数割合')

#データの合計
column_sums = df6.sum()

kei = (column_sums.at['計'])

df6['%'] = df6.round(2)['計'] / kei * 100


wariai = df6.filter(items=['用途','%'])
column_config_form = {
    "用途名": Column(
        label="	車の用途",
        width=150,
        help="事業用はバスを含む"
    ),
    "計": Column(
        label="%",
        width=50,
        help=""
    )
}
 
st.dataframe( wariai.round(),width=200,column_config=column_config_form)


#年代別のグラフ
col1,col2 = st.columns([1,3])


with col1:

	st.write('④年代別訪問者')
	df_grouped3 = df.groupby('年代').sum()

	df7 = df_grouped3

	df8 = df7.drop(labels=['作成日時','時間','分','都道府県','lat','long','性別','車種','用途名'],axis=1)

	column_config3 = {
    	"年代": Column(
        	label="年代～",
        	width=80,
        	help="おおよその年代"
    	),
    		"計": Column(
        	label="訪問者数",
        	width=65,
       	help="数の並べ替えができます",
        	required=True
    	),
	}

	st.dataframe(df8, column_config=column_config3)


with col2:
	#st.write('年代別訪問者計')
	month_group_df = df.groupby(["年代", "性別"]).sum()
	fig = px.bar(month_group_df.reset_index(), x="年代", y="計", color="性別",title="",color_discrete_sequence=["red", "green", "blue"])
	st.plotly_chart(fig, use_container_width=True)

# ④折れ線グラフの表示
st.write('⑤時間帯別訪問者')
col1,col2 = st.columns([4,1])

with col1:
	
	time_group_df = df.groupby(["時間","性別"]).sum()
	fig = px.line(time_group_df.reset_index(), x="時間", y="計", color="性別",title="",markers=True,color_discrete_sequence=["green", "red", "blue"])
	st.plotly_chart(fig, use_container_width=True)

with col2:
	
	df10 = df.drop(labels=['作成日時','分','都道府県','lat','long','性別','年代','車種','用途名'],axis=1)
	time_group_df = df10.groupby(["時間"]).sum()
	st.dataframe(time_group_df)


st.write("***********")

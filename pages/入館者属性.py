import streamlit as st
#from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from streamlit.column_config import Column
import pydeck as pdk
import plotly.express as px
import matplotlib.pyplot as plt

#①読み込まれたデータ
st.write('参照した入館者属性データ(5月5日)')
df = pd.read_csv('data/訪問客属性3.csv')
st.write("①参照データ")
st.dataframe(df)


#②都道府県別表＆グラフ
ken_total = df.groupby(['都道府県','long','lat']).sum(numeric_only=True).sort_values(by="計", ascending=False).reset_index()

st.write("***********")
st.write('②都道府県別合計')
#st.dataframe(ken_total,width=360)


# PyDeckを使用して地図を描画します
#st.dataframe(ken_total)

# 高さ倍率スライダー
elevation_scale = st.slider("棒の高さ倍率", 10, 500, 100, step=10)

# Pydeckで3D棒グラフ作成
layer = pdk.Layer(
	"ColumnLayer",
	data=ken_total,
	get_position=["long", "lat"],
	get_elevation="計",
	elevation_scale=elevation_scale,  # 高さ倍率
	radius=20000,         # 棒の半径（m）
	get_fill_color=[0, 100, 200, 200],  # RGBA
	pickable=True,
	auto_highlight=True,
	)

# 初期表示位置（日本の中心付近）
view_state = pdk.ViewState(
	latitude=37.5,
	longitude=137.0,
	zoom=4.5,
	pitch=40
 )

r = pdk.Deck(
	layers=[layer],
	initial_view_state=view_state,
	tooltip={"text": "{都道府県}\n計: {計}"},
	map_style="mapbox://styles/mapbox/light-v10"
	)

st.pydeck_chart(r)

#車用途別（df5,df6,df_grouped2 )
df_grouped2 = df.groupby('用途名').sum()

df5 = df_grouped2
df6 = df5.drop(labels=['作成日時','時','分','都道府県','lat','long','性別','年代','車種'],axis=1)
st.write("***********")
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

st.write("***********")
#年代別のグラフ
col1,col2 = st.columns([1,3])


with col1:

	st.write('④年代別訪問者')
	df_grouped3 = df.groupby('年代').sum()

	df7 = df_grouped3

	df8 = df7.drop(labels=['作成日時','時','分','都道府県','lat','long','性別','車種','用途名'],axis=1)

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
st.write("***********")
# ④折れ線グラフの表示
st.write('⑤時間帯別訪問者')
col1,col2 = st.columns([4,1])

with col1:
	
	time_group_df = df.groupby(["時","性別"]).sum()
	fig = px.line(time_group_df.reset_index(), x="時", y="計", color="性別",title="",markers=True,color_discrete_sequence=["green", "red", "blue"])
	st.plotly_chart(fig, use_container_width=True)

with col2:
	
	df10 = df.drop(labels=['作成日時','分','都道府県','lat','long','性別','年代','車種','用途名'],axis=1)
	time_group_df = df10.groupby(["時"]).sum()
	st.dataframe(time_group_df)


st.write("***********")


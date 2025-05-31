import streamlit as st
import pandas as pd
from streamlit.column_config import Column
import pydeck as pdk


df = pd.read_csv('訪問客属性2.csv')

    
st.write(df)

df_grouped = df.groupby('都道府県').sum()

df2 = df_grouped
df3 = df2.drop(labels=['作成日時','性別','年代','車種','用途名'],axis=1)

column_config = {
    "都道府県": Column(
        label="都道府県名",
        width=80,
        help="都道府県の名前を表示します。"
    ),
    "No.": Column(
        label="訪問者数",
        width=75,
        help="数の並べ替えができます",
        required=True
    ),
    
}

#df_grouped = df.groupby('用途名').sum()

#df5 = df_grouped
#df6 = df5.drop(labels=['作成日時','性別','年代','車種','用途名'],axis=1)

#column_config = {
#    "都道府県": Column(
#        label="都道府県名",
#        width=80,
#        help="都道府県の名前を表示します。"
#    ),
#    "No.": Column(
#        label="訪問者数",
#        width=75,
#        help="数の並べ替えができます",
#        required=True
#    ),
    
#}




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

	"福岡県":398,
	"佐賀県":223,
	"長崎県":65,
	"山口県":32,
	"大分県":31,
	"鹿児島県":29,
	"島根県":26,
	"香川県":22,
	"北海道":21,
	"愛知県":16,
	"大阪府":14,
	"千葉県":13,
	"宮崎県":11,
	"広島県":11,
	"東京都":10,
	"熊本県":48
}
# データフレームを作成
df4 = pd. DataFrame ({

	'prefecture': list (prefecture_coordinates. keys() ),

	'lat': [prefecture_coordinates [p] [0] for p in prefecture_coordinates],
	'lon': [prefecture_coordinates [p] [1] for p in prefecture_coordinates],
	'sales': list (sales_data. values())

})


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

col1,col2 = st.columns([1,3])


with col1:
	st.write('都道府県別合計')
	st.dataframe(df3, column_config=column_config)



with col2:
	# Streamlit アプリのタイトルを設定
	st.write("")
	# Pydeck チャートを Streamlit アプリに表示
	#st.pydeck_chart (deck, unsafe_allow_html=True)
	st.pydeck_chart (deck, use_container_width=True)
	
	



import datetime
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from streamlit.column_config import Column

#コラム名：日付,品名コード,品名,数量,単価,金額,分類コード,分類名,備考

st.title("売店の売上")
data = []
# 日付を選ぶカレンダーを表示
selected_date = st.date_input("下記の欄をクリックしてカレンダーから日付を選んでください")

# 選んだ日付を表示
#st.write("あなたが選んだ日付は：", selected_date)

search_date = selected_date.strftime('%Y%m%d')

# ファイルの読み込み
df = pd.read_csv('data/20250501-05お土産売上2.csv',low_memory=False)


df2 = df.query(f'日付 == {search_date}')
#df2から始める
df3 = df2.drop(labels=['No.','日付','品名コード','分類コード'],axis=1)
df3.columns = ['品名','個数','単価','金額','区分','備考']

searched_datas = (df3.shape[0])

st.write(f"販売件数：",('{:,}'.format(searched_datas)),"件")
k_金額 =(df3['金額'].sum())
st.write("合計金額は:",('{:,}'.format(k_金額)),"円")
st.subheader("売上金額TOP10")
st.dataframe(df3.sort_values('金額',ascending=False).head(10))
#d3はOK
st.text("-----------------------------------------------------------------------")

#分類別円グラフ
st.subheader("お土産品分類別売上")
st.text("")
st.text("")
df4_grouped = df2.groupby('分類名').sum()
df5 = df4_grouped.drop(labels=['No.','日付','品名コード','品名','単価','金額','分類コード','備考'],axis=1)
col1, col2 = st.columns([3,2])

#グラフを描くときの土台となるオブジェクト
fig = go.Figure(
    data=[
        go.Pie(
            labels=df['分類名'], # ラベルの設定
            values=df['金額'] # 値の設定
            )])
fig.update_layout(
    showlegend=True, #凡例表示
    height=290, # グラフの高さの設定
    margin={'l': 20, 'r': 60, 't': 0, 'b': 0}, #余白の設定 left, right, top, bottom
    )
fig.update_traces(textposition='inside', textinfo='label+percent') 

col1.plotly_chart(fig, use_container_width=True) 

#col2.subheader("購入数TOP10")
many_df = df2.groupby("分類名").sum(numeric_only=True).sort_values(by="金額", ascending=False).reset_index()


#検索
filtered_df = df2[df['分類名']==("雑貨類")]


col2.text("雑貨類売上--TOP10")
#st.dataframe(filtered_df).ascending=False
col2.dataframe(filtered_df[["品名", "金額"]].sort_values(by="金額", ascending=False).head(10))
#col2.dataframe(filtered_df.style.format("{:,.0f}"))

col1, col2  = st.columns([1,1])
#検索(和菓子)
filtered_df = df2[df['分類名']==("和菓子")]

col1.text("和菓子売上--TOP10")
col1.table(filtered_df[["品名", "金額"]].sort_values(by="金額", ascending=False).head(10))
#検索(洋菓子)
filtered_df2 = df2[df['分類名']==("洋菓子")]

col2.text("洋菓子売上--TOP10")
col2.table(filtered_df2[["品名", "金額"]].sort_values(by="金額", ascending=False).head(10))
#検索(洋菓子)

#検索(食品)
#filtered_df3 = df2[df['分類名']==("食品")]

#col3.text("食品売上--TOP10")
#col3.table(filtered_df3[["品名", "金額"]].iloc[:10].sort_values(by="金額", ascending=False))



#-------------------------------------------------------------------------------------
st.text("-------------------------------------------------------------------")
st.subheader("価格帯別売上個数")
df_sorted = df.sort_values(by='単価', ascending=True)
#st.dataframe(df_sorted.head(10))
df_grouped2 = df.groupby('単価').sum()
df5 = df_grouped2.drop(labels=['No.','日付','品名コード','品名','金額','分類コード','分類名','備考'],axis=1)

col1, col2 = st.columns([2,5])


column_config3 = {
    	"単価": Column(
        	label="単価(円)",
			width=35

    	),
    		"数量": Column(
        	label="売上(個)",
        	width=40,
       	help="数の並べ替えができます",
        	required=True
    	),
	}





col1.dataframe(df5.head(10).reset_index(),column_config=column_config3)
col2.text('**散布図**')
col2.scatter_chart(df5)


st.text("-------------------------------------------------------------------")

#st.title('散布図')

# ダミーデータの作成
#dates = pd.date_range(start='2024-01-01', periods=100)
#values1 = np.random.randn(100).cumsum()
#values2 = np.random.randn(100).cumsum()

# データフレームの作成
#data = pd.DataFrame({
#    'date': dates,
#    'column 1': values1,
#    'column 2': values2
#})
#st.dataframe(data)

# スキャッターチャートの表示
#st.scatter_chart(data.set_index('date'))
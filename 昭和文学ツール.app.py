import streamlit as st
import pandas as pd

# アプリ設定
st.set_page_config(page_title="昭和文学統計ツール", layout="wide")

# 統計データベース
showa_db = {
    "昭和初期 (1930頃)": {
        "year": 1930,
        "pop": {"年少": 36.6, "生産": 58.7, "老年": 4.7},
        "rice": 2.1, "salary": 73, "infant_death": 124.1,
        "urban": 24.0, "death": "結核・肺炎",
        "context": "多喜二『蟹工船』の時代。若者が多く、死が身近なプロレタリア文学全盛期。",
        "mult": 3000
    },
    "戦後復興期 (1950頃)": {
        "year": 1950,
        "pop": {"年少": 35.4, "生産": 59.7, "老年": 4.9},
        "rice": 635.0, "salary": 3000, "infant_death": 60.1,
        "urban": 37.3, "death": "脳血管疾患",
        "context": "戦後文学・無頼派。混乱期からベビーブーム、復興への転換点。",
        "mult": 100
    },
    "高度成長期 (1965頃)": {
        "year": 1965,
        "pop": {"年少": 25.6, "生産": 68.1, "老年": 6.3},
        "rice": 1105.0, "salary": 24000, "infant_death": 18.5,
        "urban": 67.9, "death": "ガン・心疾患",
        "context": "都市化が進行。団地生活やサラリーマンの孤独が描かれた時代。",
        "mult": 5
    }
}

# 画面表示
st.title("📚 昭和文学 × 社会統計分析ツール")
selected_era = st.sidebar.selectbox("時代を選択", list(showa_db.keys()))
data = showa_db[selected_era]

col1, col2 = st.columns(2)
with col1:
    st.subheader("🖋 作品テキスト入力")
    text = st.text_area("文章を入力", height=200)
    if st.button("分析照合"):
        st.info(f"**歴史的背景:** {data['context']}")
        money = st.number_input("作中の金額(円)", value=1.0)
        st.write(f"現代価値：約 **{int(money * data['mult']):,}円**")

with col2:
    st.subheader("📊 当時の指標")
    st.metric("乳児死亡率", data['infant_death'])
    st.bar_chart(pd.DataFrame(list(data['pop'].items()), columns=['層', '比']).set_index('層'))

st.divider()
st.caption("出典：総務省統計局『日本長期統計総覧』、日銀消費者物価指数 他")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="昭和文学・社会情勢分析アーカイブ", layout="wide")

# 詳細データベース
showa_details = {
    "昭和初期 (1926-1935)": {
        "context": "大正デモクラシーの終焉と昭和恐慌。エログロナンセンスとプロレタリア文学の対立。",
        "keywords": ["治安維持法", "欠食児童", "モダンガール", "円本"],
        "stats": "乳児死亡率は現代の約60倍。結核は『亡国病』と呼ばれ、文学における悲劇の定番でした。",
        "mult": 3000, "death_rate": 120
    },
    "戦中・戦後直後 (1936-1950)": {
        "context": "軍国主義の台頭から敗戦、そして虚脱。闇市文学と無頼派の流行。",
        "keywords": ["贅沢は敵だ", "疎開", "カストリ雑誌", "新円切替"],
        "stats": "インフレが数千倍規模で進行。戦後直後の作品における『1円』の重みは日々変動していました。",
        "mult": 100, "death_rate": 60
    },
    "高度成長期 (1955-1970)": {
        "year_range": "1955-1970",
        "context": "『もはや戦後ではない』。都市への人口集中と中間層の誕生。",
        "keywords": ["三種の神器", "団地", "安保闘争", "サラリーマン"],
        "stats": "都市化率が急上昇し、故郷を喪失した孤独な都市居住者が文学の主役になりました。",
        "mult": 5, "death_rate": 20
    }
}

st.title("📚 昭和文学 時代考証・社会統計ツール")

selected_era = st.sidebar.radio("考察したい年代を選択してください", list(showa_details.keys()))
data = showa_details[selected_era]

# メインレイアウト
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🖋 文学テキスト解析")
    user_text = st.text_area("解析したい一節を入力", placeholder="（例）小林多喜二、太宰治、三島由紀夫など", height=250)
    
    if st.button("時代背景を抽出"):
        st.markdown(f"### 【{selected_era}】の社会考察")
        st.write(data['context'])
        st.info(f"**当時の重要語彙:** {', '.join(data['keywords'])}")
        
        st.subheader("💰 経済的背景")
        money = st.number_input("作中の金額（円）", value=1.0)
        st.success(f"現代価値換算: 約 **{int(money * data['mult']):,}円**")

with col2:
    st.subheader("📊 統計データによる裏付け")
    st.write(data['stats'])
    
    # 比較グラフ：死亡率の推移
    st.write("**乳児死亡率（1000人対）の比較**")
    death_df = pd.DataFrame({
        "時代": list(showa_details.keys()) + ["現代"],
        "死亡率": [v['death_rate'] for v in showa_details.values()] + [1.8]
    }).set_index("時代")
    st.bar_chart(death_df)

st.divider()
st.write("※このツールは文学研究の補助を目的としています。数値は概数であり、当時の物価・社会情勢を理解するための指標です。")

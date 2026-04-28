{\rtf1\ansi\ansicpg932\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
\
# \uc0\u12450 \u12503 \u12522 \u35373 \u23450 \
st.set_page_config(page_title="\uc0\u26157 \u21644 \u25991 \u23398 \u32113 \u35336 \u12484 \u12540 \u12523 ", layout="wide")\
\
# \uc0\u32113 \u35336 \u12487 \u12540 \u12479 \u12505 \u12540 \u12473 \
showa_db = \{\
    "\uc0\u26157 \u21644 \u21021 \u26399  (1930\u38915 )": \{\
        "year": 1930,\
        "pop": \{"\uc0\u24180 \u23569 ": 36.6, "\u29983 \u29987 ": 58.7, "\u32769 \u24180 ": 4.7\},\
        "rice": 2.1, "salary": 73, "infant_death": 124.1,\
        "urban": 24.0, "death": "\uc0\u32080 \u26680 \u12539 \u32954 \u28814 ",\
        "context": "\uc0\u22810 \u21916 \u20108 \u12302 \u34809 \u24037 \u33337 \u12303 \u12398 \u26178 \u20195 \u12290 \u33509 \u32773 \u12364 \u22810 \u12367 \u12289 \u27515 \u12364 \u36523 \u36817 \u12394 \u12503 \u12525 \u12524 \u12479 \u12522 \u12450 \u25991 \u23398 \u20840 \u30427 \u26399 \u12290 ",\
        "mult": 3000\
    \},\
    "\uc0\u25126 \u24460 \u24489 \u33288 \u26399  (1950\u38915 )": \{\
        "year": 1950,\
        "pop": \{"\uc0\u24180 \u23569 ": 35.4, "\u29983 \u29987 ": 59.7, "\u32769 \u24180 ": 4.9\},\
        "rice": 635.0, "salary": 3000, "infant_death": 60.1,\
        "urban": 37.3, "death": "\uc0\u33075 \u34880 \u31649 \u30142 \u24739 ",\
        "context": "\uc0\u25126 \u24460 \u25991 \u23398 \u12539 \u28961 \u38972 \u27966 \u12290 \u28151 \u20081 \u26399 \u12363 \u12425 \u12505 \u12499 \u12540 \u12502 \u12540 \u12512 \u12289 \u24489 \u33288 \u12408 \u12398 \u36578 \u25563 \u28857 \u12290 ",\
        "mult": 100\
    \},\
    "\uc0\u39640 \u24230 \u25104 \u38263 \u26399  (1965\u38915 )": \{\
        "year": 1965,\
        "pop": \{"\uc0\u24180 \u23569 ": 25.6, "\u29983 \u29987 ": 68.1, "\u32769 \u24180 ": 6.3\},\
        "rice": 1105.0, "salary": 24000, "infant_death": 18.5,\
        "urban": 67.9, "death": "\uc0\u12460 \u12531 \u12539 \u24515 \u30142 \u24739 ",\
        "context": "\uc0\u37117 \u24066 \u21270 \u12364 \u36914 \u34892 \u12290 \u22243 \u22320 \u29983 \u27963 \u12420 \u12469 \u12521 \u12522 \u12540 \u12510 \u12531 \u12398 \u23396 \u29420 \u12364 \u25551 \u12363 \u12428 \u12383 \u26178 \u20195 \u12290 ",\
        "mult": 5\
    \}\
\}\
\
# \uc0\u30011 \u38754 \u34920 \u31034 \
st.title("\uc0\u55357 \u56538  \u26157 \u21644 \u25991 \u23398  \'d7 \u31038 \u20250 \u32113 \u35336 \u20998 \u26512 \u12484 \u12540 \u12523 ")\
selected_era = st.sidebar.selectbox("\uc0\u26178 \u20195 \u12434 \u36984 \u25246 ", list(showa_db.keys()))\
data = showa_db[selected_era]\
\
col1, col2 = st.columns(2)\
with col1:\
    st.subheader("\uc0\u55357 \u56715  \u20316 \u21697 \u12486 \u12461 \u12473 \u12488 \u20837 \u21147 ")\
    text = st.text_area("\uc0\u25991 \u31456 \u12434 \u20837 \u21147 ", height=200)\
    if st.button("\uc0\u20998 \u26512 \u29031 \u21512 "):\
        st.info(f"**\uc0\u27508 \u21490 \u30340 \u32972 \u26223 :** \{data['context']\}")\
        money = st.number_input("\uc0\u20316 \u20013 \u12398 \u37329 \u38989 (\u20870 )", value=1.0)\
        st.write(f"\uc0\u29694 \u20195 \u20385 \u20516 \u65306 \u32004  **\{int(money * data['mult']):,\}\u20870 **")\
\
with col2:\
    st.subheader("\uc0\u55357 \u56522  \u24403 \u26178 \u12398 \u25351 \u27161 ")\
    st.metric("\uc0\u20083 \u20816 \u27515 \u20129 \u29575 ", data['infant_death'])\
    st.bar_chart(pd.DataFrame(list(data['pop'].items()), columns=['\uc0\u23652 ', '\u27604 ']).set_index('\u23652 '))\
\
st.divider()\
st.caption("\uc0\u20986 \u20856 \u65306 \u32207 \u21209 \u30465 \u32113 \u35336 \u23616 \u12302 \u26085 \u26412 \u38263 \u26399 \u32113 \u35336 \u32207 \u35239 \u12303 \u12289 \u26085 \u37504 \u28040 \u36027 \u32773 \u29289 \u20385 \u25351 \u25968  \u20182 ")\
\
}

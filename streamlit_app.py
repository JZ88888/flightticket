import streamlit as st
from flight_scraper import get_mock_flights
from utils import filter_flights

st.set_page_config(page_title="FlightAgent ✈️", layout="centered")
st.title("🛫 FlightAgent v1.0 – AI订票助手")

st.markdown("请输入以下信息，我们将为你推荐最佳航班：")

with st.form("flight_form"):
    from_city = st.text_input("出发城市", placeholder="北京")
    to_city = st.text_input("目的地", placeholder="马尼拉")
    depart_date = st.date_input("出发日期")
    max_price = st.number_input("最高预算（元）", min_value=100, value=1500)
    direct_only = st.checkbox("只看直飞航班", value=True)
    submitted = st.form_submit_button("搜索航班")

if submitted:
    st.info("正在搜索，请稍候...")
    flights = get_mock_flights(from_city, to_city, str(depart_date))
    results = filter_flights(flights, max_price, direct_only)

    if results:
        st.success(f"共找到 {len(results)} 条符合条件的航班：")
        for f in results:
            st.markdown(f"""
                **{f['airline']} {f['flight_no']}**
                - 🕒 时间：{f['depart_time']} → {f['arrive_time']}
                - 💰 票价：¥{f['price']}
                - ✈️ {'直飞' if f['direct'] else '经停'}
                - 🔗 [模拟预订链接](https://kayak.com)
                ---
            """)
    else:
        st.warning("未找到符合条件的航班，请尝试放宽限制或更换日期。")

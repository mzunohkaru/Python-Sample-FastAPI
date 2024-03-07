import streamlit as st
import datetime
import requests
import random
import json
import pandas as pd

page = st.sidebar.selectbox("APIテスト", ["ユーザー", "ルーム", "予約"])

if page == "ユーザー":
    st.title("ユーザー登録")
    with st.form(key="user"):
        username = st.text_input("名前", max_chars=12)
        data = {"username": username}
        submit_button = st.form_submit_button("登録")

    if submit_button:
        st.write("### レスポンス結果")
        url = "http://127.0.0.1:8000/users"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success("ユーザー登録完了")
        else:
            st.error("ユーザー登録失敗")
        st.write(response.status_code)
        st.write(response.json())

elif page == "ルーム":
    st.title("会議室登録")

    with st.form(key="room"):
        room_name = st.text_input("会議室名", max_chars=12)
        capacity = st.number_input("定員", min_value=1, max_value=5, step=1)
        data = {"room_name": room_name, "capacity": capacity}
        submit_button = st.form_submit_button("送信")

    if submit_button:
        st.write("### レスポンス結果")
        url = "http://127.0.0.1:8000/rooms"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success("会議室登録完了")
        else:
            st.error("会議室登録失敗")
        st.write(response.status_code)
        st.write(response.json())

elif page == "予約":
    st.title("会議室予約")
    # ユーザー一覧を取得
    url_users = "http://127.0.0.1:8000/users"
    response = requests.get(url_users)
    users = response.json()
    users_name = {}
    for user in users:
        users_name[user["username"]] = user["user_id"]

    # 会議室一覧を取得
    url_rooms = "http://127.0.0.1:8000/rooms"
    response = requests.get(url_rooms)
    rooms = response.json()
    rooms_name = {}
    for room in rooms:
        rooms_name[room["room_name"]] = {
            "room_id": room["room_id"],
            "capacity": room["capacity"],
        }

    # 予約一覧を取得
    url_bookings = "http://127.0.0.1:8000/bookings"
    response = requests.get(url_bookings)
    bookings = response.json()
    df_bookings = pd.DataFrame(bookings)

    st.write("### 会議室一覧")
    df_rooms = pd.DataFrame(rooms)
    if not df_rooms.empty:
        df_rooms.columns = ["会議室名", "定員", "会議室 ID"]
        st.table(df_rooms)
    else:
        st.write('会議室はありません')

    users_id = {}
    for user in users:
        users_id[user["user_id"]] = user["username"]

    rooms_id = {}
    for room in rooms:
        rooms_id[room["room_id"]] = {
            "room_name": room["room_name"],
            "capacity": room["capacity"],
        }

    st.write("### 予約一覧")
    if not df_bookings.empty:

        # IDを各値に変更
        # lambda : users_idに格納されている要素全てに変更を適用するのに最適
        # xにuser_idが格納される->users_id[x]でusernameに変換
        to_username = lambda x: users_id[x]
        to_room_name = lambda x: rooms_id[x]["room_name"]
        to_datetime = lambda x: datetime.datetime.fromisoformat(x).strftime(
            "%Y/%m/%d %H:%M"
        )

        # 特定の列に適用
        df_bookings["user_id"] = df_bookings["user_id"].map(to_username)
        df_bookings["room_id"] = df_bookings["room_id"].map(to_room_name)
        df_bookings["start_datetime"] = df_bookings["start_datetime"].map(to_datetime)
        df_bookings["end_datetime"] = df_bookings["end_datetime"].map(to_datetime)

        df_bookings = df_bookings.rename(
            columns={
                "user_id": "予約者名",
                "room_id": "会議室名",
                "booked_num": "予約人数",
                "start_datetime": "開始時刻",
                "end_datetime": "終了時刻",
                "booking_id": "予約番号",
            }
        )
        st.table(df_bookings)
    else:
        st.write("予約はありません")

    with st.form(key="booking"):
        username: str = st.selectbox("予約者名", users_name.keys())
        room_name: str = st.selectbox("会議室名", rooms_name.keys())
        booked_num = st.number_input("予約人数", min_value=1, step=1)
        date = st.date_input("予約日", min_value=datetime.date.today())
        start_time = st.time_input("開始時間", value=datetime.time(hour=9, minute=0))
        end_time = st.time_input("終了時間", value=datetime.time(hour=18, minute=0))

        submit_button = st.form_submit_button("予約する")

    if submit_button:
        user_id: int = users_name[username]
        room_id: int = rooms_name[room_name]["room_id"]
        capacity: int = rooms_name[room_name]["capacity"]

        data = {
            "user_id": user_id,
            "room_id": room_id,
            "booked_num": booked_num,
            "start_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute,
            ).isoformat(),
            "end_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute,
            ).isoformat(),
        }

        # 定員より多い予約人数の場合
        if booked_num > capacity:
            st.error(
                f"{room_name}の定員は、{capacity}名です。{capacity}名以下の予約人数のみ受け付けております。"
            )
        # 開始時刻 >= 終了時刻
        elif start_time >= end_time:
            st.error("開始時刻が終了時刻を越えています")
        elif start_time < datetime.time(
            hour=9, minute=0, second=0
        ) or end_time > datetime.time(hour=18, minute=0, second=0):
            st.error("利用時間は9:00~18:00になります。")
        else:
            # 会議室予約
            url = "http://127.0.0.1:8000/bookings"
            res = requests.post(url, data=json.dumps(data))
            if res.status_code == 200:
                st.success("予約完了しました")
                st.experimental_rerun()
            elif res.status_code == 404 and res.json()["detail"] == "予約済みです":
                st.error("指定の時間にはすでに予約が入っています。")

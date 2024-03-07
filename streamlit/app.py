import streamlit as st

# サイドバーのメニュー
menu = ["ホーム", "商品管理", "受注管理", "会員管理", "コンテンツ管理", "設定"]
productMenu = ["商品登録", "カテゴリ管理", "タグ管理"]
orderMenu = ["受注登録", "カテゴリ管理", "タグ管理"]
memberMenu = ["会員登録", "カテゴリ管理", "タグ管理"]
contentMenu = ["コンテンツ登録", "カテゴリ管理", "タグ管理"]
settingMenu = ["基本設定", "カテゴリ管理", "タグ管理"]

st.sidebar.title("メニュー")
choice = st.sidebar.selectbox("メニューを選択してください", menu)

if choice == "商品管理":
    st.sidebar.subheader("商品管理メニュー")
    submenu_choice = st.sidebar.selectbox("", productMenu)
elif choice == "受注管理":
    st.sidebar.subheader("受注管理メニュー")
    submenu_choice = st.sidebar.selectbox("", orderMenu)
elif choice == "会員管理":
    st.sidebar.subheader("会員管理メニュー")
    submenu_choice = st.sidebar.selectbox("", memberMenu)
elif choice == "コンテンツ管理":
    st.sidebar.subheader("コンテンツ管理メニュー")
    submenu_choice = st.sidebar.selectbox("", contentMenu)
elif choice == "設定":
    st.sidebar.subheader("設定メニュー")
    submenu_choice = st.sidebar.selectbox("", settingMenu)

# メインコンテンツエリア
if choice == "ホーム":
    st.title("ホーム")
elif choice == "商品管理":
    if submenu_choice == "商品登録":
        st.title("商品登録")
    elif submenu_choice == "カテゴリ管理":
        st.title("カテゴリ管理")
    elif submenu_choice == "タグ管理":
        st.title("タグ管理")
elif choice == "受注管理":
    st.title("受注管理")
elif choice == "会員管理":
    st.title("会員管理")
elif choice == "コンテンツ管理":
    st.title("コンテンツ管理")
elif choice == "設定":
    st.title("設定")

if choice == "商品管理" and submenu_choice == "商品登録":
    # 商品一覧ページ
    st.text_input("商品名を検索")
    st.button("検索")
    st.write("ここに表を表示")
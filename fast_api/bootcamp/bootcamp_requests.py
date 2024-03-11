import requests
import json

def main():
    url = 'http://127.0.0.1:8000/item/'
    # Dict型のデータ
    body = {
        "name": "PC",
        "description": "This is a Hyper Spec PC",
        "price": 23500,
        "tax": 1.1
    }
    # Dict型のデータをJSONに変換
    data = json.dumps(body)
    # JSONデータをPOST
    res = requests.post(url, data)
    print(res.json())

# import しただけで、その読み込んだライブラリの処理が実行されたくないので、 
# if __name__ == “__main__“: と書いておくと、特定のライブラリをインポートした時にその内部のプログラムが動かないようにする
if __name__ == '__main__':
    print(__name__)
    main()


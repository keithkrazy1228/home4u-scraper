from flask import Flask, request, jsonify

app = Flask(__name__)

# テスト用ルート
@app.route('/')
def hello():
    return "HOME4U Scraper is running!"

# GASからPOSTされたデータを受け取る場所
@app.route('/api/parse', methods=['POST'])
def parse_home4u():
    try:
        # 受け取ったデータを取得
        data = request.json
        if not data:  # データがない場合にエラーメッセージを表示
            raise ValueError("No data received")

        # 受け取ったデータを取得
        property_id = data.get("propertyId")
        contact_date = data.get("contactDate")
        detail_url = data.get("detailUrl")
        login_id = data.get("loginId")
        password = data.get("password")

        # ログに出力
        print("▼ログインID：", login_id)
        print("▼パスワード：", password)
        print("査定ナンバー:", property_id)
        print("ご依頼日:", contact_date)
        print("詳細URL:", detail_url)

        # 正常に受け取った場合、レスポンスを返す
        return jsonify({"status": "received", "propertyId": property_id})

    except Exception as e:
        # エラーが発生した場合にエラーメッセージを表示
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

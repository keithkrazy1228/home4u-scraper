from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# テスト用ルート
@app.route('/')
def hello():
    return "HOME4U Scraper is running!"

# GASからPOSTされたデータを受け取る場所
@app.route('/api/parse', methods=['POST'])
def parse_home4u():
   data = request.json

property_id = data.get("propertyId")
contact_date = data.get("contactDate")
detail_url = data.get("detailUrl")
login_id = data.get("loginId")
password = data.get("password")

print("▼ログインID：", login_id)
print("▼パスワード：", password)

print("査定ナンバー:", property_id)
print("ご依頼日:", contact_date)
print("詳細URL:", detail_url)

    # ここから先にスクレイピング＆スプレッドシート登録処理を追加していく
return jsonify({"status": "received", "propertyId": property_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

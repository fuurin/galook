# ぎゃルック！ API

## ゲーム情報 API

- エンドポイント: /games/:game_id
- メソッド: GET
- パラメータ
    - なし

## ゲーム情報検索 API

- エンドポイント: /games?title=:title
- メソッド: GET
- パラメータ
    - title: ゲームのタイトルの一部 or 全部
- 例: /games?title=大学
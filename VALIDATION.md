# v2.1.0 検証記録

対象：Victoria 3 1.13.11。確認日：2026年10月22日。

- 静的検査：スクリプト構文、定義重複、SGUI参照、建物参照、GUI式の括弧、翻訳キーの整合を確認。検出エラー0。
- SGUI 64定義、GUI側のSGUI参照191件を照合。
- 8言語各547キー。キー集合の差と重複は0。
- 企業設立の6選択肢すべてで対象scopeを引き継ぐことを検査。
- 支払増減は、対象Vanilla実定義との差分が全額免除との相互排他のみであることを検査。
- 本体を隔離userdir・本MODのみで起動し、スクリプトのPostValidateまで実施。MOD由来のparser/unknown trigger/effect/重複action等の読み込みエラーは0。
- MOD由来の変数参照警告は22件。GUI・localizationで読む変数が検査の参照集計に含まれない警告と、旧対象フラグのcleanup用参照です。警告を隠すためのダミー処理は追加していません。
- MODなしの本体も別userdirで初期化し、残る他ファイルのログ3件を再現。Vanillaの`custom_tooltip.gui`の表示キー、`30_transfer_subject.txt`の`TRANSFER_SUBJECT_OTHER_THAN_RECIPIENT`キーに関するものです。本体には修正を加えていません。
- パッケージのCRCと全収録ファイルのSHA-256を検査。

これは初期読み込みと静的検査の結果です。テスト用ゲームのウィンドウは操作APIに現れず、プレイ中のボタン操作、移譲・支払額、関係変更時の実行、JE/event、AI・経済、セーブロード、MP、DLC未所有環境は未検証です。

次の確認：新規ゲームでNVGMだけを有効化し、送金条約→追加融資→助成→3資源の追加/再適用/解除→独立→再ロードを試してください。error.logは最初の新しいparser/script errorから確認してください。

# v2.2.0 — 2026-10-23

- Add schema-3 contract generations and recorded recipient/issuer identity.
- Rebuild donor resource burdens from authoritative recipient amounts; retain 15 recipients per resource.
- Import valid v2.1.1 records without inferring financial consent.
- Add subsidy batch membership, close/resume controls and a daily relation/lease watchdog.
- Preserve per-building general-aid conditions and spontaneous preexisting subsidies.
- Prevent stale donor indices from closing a new generation.
- Keep exact full-cost reimbursement disabled pending a verified server expenditure API.
- Add Japanese/English strings; other six locales use the new English fallback strings.

# v2.1.1

独立・宗主国変更後の支援残留に対策。移譲の双方向検査・45日期限・翌日再検査、外交支援の固定期間撤去、元契約からの停止、常設の修復/停止決断を追加。新規助成の追跡、人口移動先の消し忘れ、企業イベントの実行前検査・建設企業の誤参照を修正。旧NVGM外交支援は移行時に終了し、再設定が必要。

# Changelog

## 2.1.0 — 2026-10-22

Victoria 3 1.13.11向けに、確認済みv1.7.8から再構築。

- 現行Vanillaの外交画面・HUD・都市タイプを基準に差分移植。
- 現行送金条約と投資権判定、維持費・法制定modifier・DecisionのAI構文へ追従。
- 支払増減の同名定義はVanillaと同じファイルパスで置換し、全額免除と排他化。
- 移譲の誤参照とslot識別を修正し、関係変更時・月次のcleanupを追加。
- ガラス工場SGUI、統計の参照・括弧・旧支出値・list選択指定、企業設立と人口移動のscopeを修正。
- debug consoleによる統計更新をSGUIへ変更。
- 8言語のlocalizationキーを統一。試作・生成ツール・メモは配布領域から分離。

過去会話で案内されたv2.0.0は実体を回収できていないため、この版との直接差分は未確認です。

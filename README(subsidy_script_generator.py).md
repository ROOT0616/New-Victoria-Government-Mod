# NVGM Subsidized Script Generator

## 概要
このスクリプトは、指定された建物（建築産業）に助成スクリプトを自動生成する Python スクリプトです。`input.txt` に建物のリストを記述すると、それに基づいて `output_script.txt` にスクリプトを出力します。

## ファイル構成
- `script_generator.py`: スクリプト生成を行う Python スクリプト
- `input.txt`: 入力データファイル（建物情報を記述）
- `output_script.txt`: 生成されたスクリプトが保存されるファイル

## 使い方
1. `input.txt` に対象の建物を記述します。
2. Python スクリプト `script_generator.py` を実行します。
3. `output_script.txt` に生成されたスクリプトが出力されます。

## `input.txt` のフォーマット
各行に `キー: "値"` の形式で建物情報を記述します。

### 例:
```
building_food_industry: "食品産業"
building_textile_mills: "織物工場"
building_furniture_manufacturies: "家具製造業"
```

## スクリプトの実行
Python 3 がインストールされている環境で、以下のコマンドを実行します。
```
python script_generator.py
```

成功すると `output_script.txt` にスクリプトが出力されます。

## 出力例 (`output_script.txt`)
```plaintext
# 助成 食品産業
nvgm_subsidized_food_industry_scriptedgui = {
  scope = country
  saved_scopes = {}
  is_shown = { always = yes }
  ai_is_valid = { always = no }
  is_valid = { always = yes }
  effect = {
    if = {
      limit = {
        any_scope_building = { is_building_type = building_food_industry }
        OR = {
          overlord = { has_diplomatic_pact = { who = root type = bankroll } }
          overlord = { has_diplomatic_pact = { who = root type = NVGM_decrease_payments } }
        }
      }
      custom_tooltip = "nvgm_subsidized_scriptedgui_tooltip"
      every_scope_building = {
        limit = { is_building_type = building_food_industry }
        set_subsidized = yes
      }
    }
  }
}
```

## ライセンス
このスクリプトは自由に使用・改変できます。

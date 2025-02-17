  import re
  from string import Template

  # 各建物向けのスクリプトテンプレート
  script_template = Template(
    r'''# 助成 $display_name
  nvgm_subsidized_${industry}_scriptedgui = {
    scope = country  # the root scope, i.e. the target of the effects
    saved_scopes = {
    }
    # any additional targets
    # These are scope, it should be added in GUI to effect.
    is_shown = {
      always = yes
    }
    # is it visible on the UI?
    ai_is_valid = {
      always = no
    }
    # is the AI allowed to use it? Disabled by default.
    is_valid = {
      always = yes
    }
    # can the player use it?
    # Three trigger context, you can use them as you like whatever it used for valid or shown
    effect = {
      if = {
        limit = {
          any_scope_building = {
            is_building_type = building_${industry}
          }
          OR = {
            overlord = {
              has_diplomatic_pact = {
                who = root
                type = bankroll
              }
            }
            overlord = {
              has_diplomatic_pact = {
                who = root
                type = NVGM_decrease_payments
              }
            }
          }
        }
        custom_tooltip = "nvgm_subsidized_scriptedgui_tooltip"
        every_scope_building = {
          limit = {
            is_building_type = building_${industry}
          }
          set_subsidized = yes
        }
      }
      else_if = {
        limit = {
          any_scope_building = {
            is_building_type = building_${industry}
          }
          liberty_desire <= 90
        }
        custom_tooltip = "nvgm_subsidized_scriptedgui_tooltip"
        add_liberty_desire = 10
        every_scope_building = {
          limit = {
            is_building_type = building_${industry}
          }
          set_subsidized = yes
        }
      }
      else = {
        custom_tooltip = "nvgm_not_subsidized_scriptedgui_tooltip"
      }
    }
  }
  '''
  )

  def generate_script(industry, display_name):
    """
    industry: テンプレート中で使用する内部コード（例: food_industry, textile_mills など）
    display_name: 表示名（例: 食品産業, 織物工場 など）
    """
    return script_template.substitute(industry=industry, display_name=display_name)

  def main():
    input_filename = "input.txt"  # テキストファイルのファイル名
    data = {}
    # 各行が「キー: "値"」の形式になっている前提で正規表現を利用してパースする
    pattern = re.compile(r'([^:]+):\s*"(.*)"')
    
    with open(input_filename, "r", encoding="utf-8") as f:
      for line in f:
        line = line.strip()
        if not line:
          continue  # 空行はスキップ
        m = pattern.match(line)
        if m:
          key = m.group(1).strip()
          value = m.group(2).strip()
          data[key] = value
    
    output_scripts = []
    for key, value in data.items():
      # _lens_option のエントリは生成対象から除外
      if key.endswith("_lens_option"):
        continue
      
      # キーが "building_" で始まる場合、内部コードとして "building_" 以降を利用
      if key.startswith("building_"):
        industry = key[len("building_"):]
      else:
        industry = key
      
      display_name = value  # テキストファイルの値を表示名として利用
      script = generate_script(industry, display_name)
      output_scripts.append(script)
    
    # 生成した全てのスクリプトをまとめる
    full_script = "\n".join(output_scripts)
    
    output_filename = "output_script.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
      f.write(full_script)
    
    print(f"スクリプトが {output_filename} に生成されました。")

  if __name__ == "__main__":
    main()

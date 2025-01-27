	scripted_gui_key = {
		scope = < string >			# この SGUI が使用できるスコープタイプ
		is_shown = { trigger }		# SGUI が表示されるかどうかを決定します。
		is_valid = { trigger }		# SGUI をプレーヤーが使用できるかどうかを決定します。
		effect = { effect }			# SGUI 要素がアクティブになったときの動作を決定します。
		saved_scopes = { scopes }	# トリガー/エフェクトでイベントターゲットとしたいスコープに対応する文字列のリスト
		notification_key = < key >	# この SGUI がアクティブになったときの通知キー (デフォルト jomini_scripted_gui_confirm)
		confirm_title = {}			# この SGUI の確認ウィンドウのタイトル
		confirm_text = {}			# この SGUI の確認ウィンドウのテキスト
		ai_is_valid = { trigger }	# この SGUI を AI が利用できるかどうか（デフォルト false）
		ai_chance = { }				# AIがこのSGUIを起動する確率（1～100のスクリプト値）
		ai_frequency = {}			# AIがこのSGUIを評価する頻度を決定する名前付き値（月単位）
	}

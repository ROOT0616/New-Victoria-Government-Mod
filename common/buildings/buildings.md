building_key = {
    building_group = bg_key                             # *building groupへの参照。building groupは類似した建物の共通プロパティを定義します*
    icon = "path/to/texture"                            # 建物のアイコン
    buildable = yes/no                                  # この建物は建築可能ですか？（可能であれば、履歴、スクリプト、または自動配置によって作成できます）デフォルトは「はい」
    expandable = yes/no                                 # この建物を拡張できますか？ デフォルトは「はい
    downsizeable = yes/no                               # この建物を縮小できますか？ デフォルトは「はい
    unique = yes/no                                     # もし「はい」の場合、この建物のタイプは世界で1つのレベルのみ建設可能で、個人投資家による建設は不可。デフォルトは「いいえ
    has_max_level = yes/no                              # もし「はい」なら、最大レベルを決定するために動的な国別修飾子が作成されます。デフォルトは「いいえ」です
    ignore_stateregion_max_level = yes                  # ビルのビルディンググループに stateregion_max_level = yes が設定されている場合、このビルディングタイプではそれを上書きします
    enable_air_connection = yes/no                      # もし「はい」なら、そのビルが建設された地域は航空便の利用を考慮したものと見なされます。デフォルトは「いいえ」です
    port = yes/no                                       # ビルが異なる市場地域を接続できる場合は「はい」、デフォルトは「いいえ」
    company_headquarter = yes/no                        # ビルが企業の本社である場合は「はい」、デフォルトは「いいえ」
    unlocking_technologies = {                          # このビルを建設するために必要なテクノロジーのオプションリスト
        # テクノロジーキーのリスト
    }
    
    # オプションのカスタムトリガー（州単位） その州がこの建物タイプに適している場合、すなわち、将来的に建設が可能である場合、デフォルトは「はい」
    potential = {
        # トリガー定義
    }
    
    # オプションのカスタムトリガー（州単位） その州で現在、建物の建設が可能である場合、デフォルトは「はい」
    possible = {
        # トリガー定義
    }

    can_build = {                                       # オプションのカスタムトリガー（州スコープ） 建築要件用
        # トリガー定義
    }
    
    construction_points = int32                         # 建築に必要な建設ポイント数
    construction_modifier = {                           # (オプション) 建設キャンプに適用される。週単位の建設出力/construction_pointsのスケールで
        # 修飾子の定義                                   # 建設期間中に消費される追加の建設コストを追加するために一般的に使用される
    }
    
    owners = pop_type_key                               # 設定されていない場合、配当および投資プールはビルディンググループによって決定される
    economic_contribution = 0.0-1.0                     # このビルディングからの税金/GDPに対する乗数、税金/GDPなしの場合は0.0、デフォルトは1.0
    min_raise_to_hire = fixed_point                     # 従業員がこの職場に転職するために必要な最低給与額、デフォルトはNEconomy.MIN_RAISE_TO_HIRE
 
    naval = yes/no                                      # 海軍または陸軍、デフォルトはno、軍事用建物のみに適用可能、建物グループによって決定される
    canal = canal_type_key                              # 運河の種類への参照。設定されている場合、そのビルを運河としてマークする
 
    # 基本AI値。デフォルトはNAI.BUILDING_BASE_VALUEまたはNAI.GOVERNMENT_BUILDING_BASE_VALUE
    # スコープは、そのビルが位置する州
    # これを使用する際には注意してください。複雑なトリガーを適用すると、パフォーマンスに重大な悪影響を及ぼす可能性があります。
    ai_value = スクリプト値 
    
    # その建物についてAIが国有化/私有化を望む度合い。ai_strategiesのnationalization_desire値に追加
    # スコープは建物の位置する国
    ai_privatization_deisre = スクリプト値              
    
    slaves_role = pop_type_key                          # スレーブがどのポップタイプとして働くかを定義します。デフォルトはDEFAULT_POP_TYPEです。
 
    production_methods = {                              # ビルの動作は生産方法によって変更できます
        # 生産方法グループのリスト
    }
    
    should_auto_expand = trigger                        # 自動拡張が有効になっている場合、どの条件で自動拡張を行うか (ビルディンググループが存在する場合はそれを上書きします)
                                                        # このトリガーに何か内容がある場合、ゲームはそのビルディングが自動拡張の可能性があると見なします。したがって、ここで絶対に true と評価されないトリガーを記述しないでください
    
    category_building_type = other_building_key         # この建物をどのカテゴリーに分類するか：平均収益/生産性、建物登録など。デフォルトはそれ自身

    city_type = none/city/farm/mine/port/wood           # この建物がどのタイプのハブに生成されるか、デフォルトはnone
    generates_residences = yes/no                       # 建物が都市に居住区を追加する場合、デフォルトはyes
    terrain_manipulator = terrain_manipulator_key       # 地形マニピュレーターは建物によって更新される
    levels_per_mesh = int32                             # マップ上に建物1つを追加するために必要なレベル数、デフォルトは1
    residence_points_per_level                          # このビルがハブに追加する「住宅ポイント」の合計数。住宅ビルが作成されるかどうかを決定する。デフォルトは1
 
    override_centerpiece_mesh = yes                     # ビルがセンターピースメッシュを置き換えるかどうか。ビルを上書きする優先度の高いエンティティまたはメッシュを決定するにはcenterpiece_mesh_weightが必要
    statue = yes                                        # パワーブロックスの像のための特別な建物タイプ。override_centerpiece_meshとは排他的で、パワーブロックのセンターピース要素を使用します。 
                                                        # センターピースを上書きする際に優先されるエンティティまたはメッシュを決定するために、centerpiece_mesh_weightが必要です
    centerpiece_mesh_weight = 1                         # 対応するセンターピースメッシュを置き換える際の優先度
    
    meshes = {                                          # ダイナミックな地形配置用に配置する建物
        # メッシュのリスト
    }
    entity_not_constructed = {                          # 建設中ではないエンティティを表示できる特別な建物
        # エンティティのリスト
    }
    entity_under_construction = {                       # 特別な建物用の建設中エンティティのオーバーロード
        # エンティティのリスト
    }
    entity_constructed = {                              # 特殊建築物に建設済みエンティティを使用するためのオーバーロード
        # エンティティのリスト
    }
    locator = locator_type                              # 特殊建築物のロケータタイプ
    
    lens = infrastructure                               # 建築物のタイプをどのレンズで表示するかを上書き指定、指定がない場合は建築物グループで指定
    
    ownership_type = no_ownership/self/other            # 建物の所有形態、no_ownership - 他の建物を所有できない。配当がある場合は国に支払われる。self - 自身のみ所有でき、所有する建物に配当を支払う。other - 他の建物を所有でき、所有する建物にのみ配当を支払う。
    
    background = 「gfx/interface/icons/building_icons/backgrounds/building_panel_wheat_farms_bg.dds」 # 建物登録項目の背景テクスチャ
}
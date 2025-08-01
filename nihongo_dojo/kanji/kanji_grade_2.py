#!/usr/bin/env python
"""
常用漢字データ - 小学2年生
Total: 160 characters
"""

GRADE_2_KANJI = [
    ("引", ['イン'], ['ひ'], ['pull'], 2, 4),
    ("羽", ['ウ'], ['は', 'はね'], ['feather'], 2, 6),
    ("雲", ['ウン'], ['くも'], ['cloud'], 2, 12),
    ("園", ['エン'], ['その'], ['garden'], 2, 13),
    ("遠", ['エン', 'オン'], ['とお'], ['far'], 2, 13),
    ("科", ['カ'], [], ['subject'], 2, 9),
    ("夏", ['カ', 'ゲ'], ['なつ'], ['summer'], 2, 10),
    ("家", ['カ', 'ケ'], ['いえ', 'や'], ['house'], 2, 10),
    ("歌", ['カ'], ['うた'], ['song'], 2, 14),
    ("画", ['ガ', 'カク'], [], ['picture'], 2, 8),
    ("回", ['カイ', 'エ'], ['まわ'], ['rotate'], 2, 6),
    ("会", ['カイ', 'エ'], ['あ'], ['meet'], 2, 6),
    ("海", ['カイ'], ['うみ'], ['sea'], 2, 9),
    ("絵", ['カイ', 'エ'], [], ['picture'], 2, 12),
    ("外", ['ガイ', 'ゲ'], ['そと', 'ほか', 'はず'], ['outside'], 2, 5),
    ("角", ['カク'], ['かど', 'つの'], ['corner'], 2, 7),
    ("楽", ['ガク', 'ラク'], ['たの'], ['fun', 'music'], 2, 13),
    ("活", ['カツ'], [], ['active'], 2, 9),
    ("間", ['カン', 'ケン'], ['あいだ', 'ま'], ['between'], 2, 12),
    ("丸", ['ガン'], ['まる'], ['round'], 2, 3),
    ("岩", ['ガン'], ['いわ'], ['rock'], 2, 8),
    ("顔", ['ガン'], ['かお'], ['face'], 2, 18),
    ("汽", ['キ'], [], ['steam'], 2, 7),
    ("記", ['キ'], [], ['record'], 2, 10),
    ("帰", ['キ'], ['かえ'], ['return'], 2, 10),
    ("弓", ['キュウ'], ['ゆみ'], ['bow'], 2, 3),
    ("牛", ['ギュウ'], ['うし'], ['cow'], 2, 4),
    ("魚", ['ギョ'], ['うお', 'さかな'], ['fish'], 2, 11),
    ("京", ['キョウ', 'ケイ'], [], ['capital'], 2, 8),
    ("強", ['キョウ', 'ゴウ'], ['つよ'], ['strong'], 2, 11),
    ("教", ['キョウ'], ['おし', 'おそ'], ['teach'], 2, 11),
    ("近", ['キン', 'コン'], ['ちか'], ['near'], 2, 7),
    ("兄", ['ケイ', 'キョウ'], ['あに'], ['older brother'], 2, 5),
    ("形", ['ケイ', 'ギョウ'], ['かたち', 'かた'], ['shape'], 2, 7),
    ("計", ['ケイ'], ['はか'], ['measure'], 2, 9),
    ("元", ['ゲン', 'ガン'], ['もと'], ['origin'], 2, 4),
    ("言", ['ゲン', 'ゴン'], ['い', 'こと'], ['say'], 2, 7),
    ("原", ['ゲン'], ['はら'], ['field'], 2, 10),
    ("戸", ['コ'], ['と'], ['door'], 2, 4),
    ("古", ['コ'], ['ふる'], ['old'], 2, 5),
    ("午", ['ゴ'], [], ['noon'], 2, 4),
    ("後", ['ゴ', 'コウ'], ['あと', 'うし', 'のち'], ['after'], 2, 9),
    ("語", ['ゴ'], ['かた'], ['language'], 2, 14),
    ("工", ['コウ', 'ク'], [], ['craft'], 2, 3),
    ("公", ['コウ'], ['おおやけ'], ['public'], 2, 4),
    ("広", ['コウ'], ['ひろ'], ['wide'], 2, 5),
    ("交", ['コウ'], ['まじ', 'か'], ['exchange'], 2, 6),
    ("光", ['コウ'], ['ひかり', 'ひか'], ['light'], 2, 6),
    ("考", ['コウ'], ['かんが'], ['think'], 2, 6),
    ("行", ['コウ', 'ギョウ', 'アン'], ['い', 'ゆ', 'おこな'], ['go'], 2, 6),
    ("高", ['コウ'], ['たか'], ['high'], 2, 10),
    ("黄", ['オウ', 'コウ'], ['き'], ['yellow'], 2, 11),
    ("合", ['ゴウ', 'ガッ', 'カッ'], ['あ'], ['fit'], 2, 6),
    ("谷", ['コク'], ['たに'], ['valley'], 2, 7),
    ("国", ['コク'], ['くに'], ['country'], 2, 8),
    ("黒", ['コク'], ['くろ'], ['black'], 2, 11),
    ("今", ['コン', 'キン'], ['いま'], ['now'], 2, 4),
    ("才", ['サイ'], [], ['talent'], 2, 3),
    ("細", ['サイ'], ['ほそ', 'こま'], ['thin'], 2, 11),
    ("作", ['サク', 'サ'], ['つく'], ['make'], 2, 7),
    ("算", ['サン'], [], ['calculate'], 2, 14),
    ("止", ['シ'], ['と'], ['stop'], 2, 4),
    ("市", ['シ'], ['いち'], ['city'], 2, 5),
    ("矢", ['シ'], ['や'], ['arrow'], 2, 5),
    ("姉", ['シ'], ['あね'], ['older sister'], 2, 8),
    ("思", ['シ'], ['おも'], ['think'], 2, 9),
    ("紙", ['シ'], ['かみ'], ['paper'], 2, 10),
    ("寺", ['ジ'], ['てら'], ['temple'], 2, 6),
    ("自", ['ジ', 'シ'], ['みずか'], ['self'], 2, 6),
    ("時", ['ジ'], ['とき'], ['time'], 2, 10),
    ("室", ['シツ'], ['むろ'], ['room'], 2, 9),
    ("社", ['シャ'], ['やしろ'], ['company'], 2, 7),
    ("弱", ['ジャク'], ['よわ'], ['weak'], 2, 10),
    ("首", ['シュ'], ['くび'], ['neck'], 2, 9),
    ("秋", ['シュウ'], ['あき'], ['autumn'], 2, 9),
    ("週", ['シュウ'], [], ['week'], 2, 11),
    ("春", ['シュン'], ['はる'], ['spring'], 2, 9),
    ("書", ['ショ'], ['か'], ['write'], 2, 10),
    ("少", ['ショウ'], ['すく', 'すこ'], ['few'], 2, 4),
    ("場", ['ジョウ'], ['ば'], ['place'], 2, 12),
    ("色", ['ショク', 'シキ'], ['いろ'], ['color'], 2, 6),
    ("食", ['ショク', 'ジキ'], ['た', 'く'], ['eat'], 2, 9),
    ("心", ['シン'], ['こころ'], ['heart'], 2, 4),
    ("新", ['シン'], ['あたら', 'あら', 'にい'], ['new'], 2, 13),
    ("親", ['シン'], ['おや', 'した'], ['parent'], 2, 16),
    ("図", ['ズ', 'ト'], ['はか'], ['diagram'], 2, 7),
    ("数", ['スウ', 'ス', 'サク'], ['かず', 'かぞ'], ['number'], 2, 13),
    ("西", ['セイ', 'サイ'], ['にし'], ['west'], 2, 6),
    ("声", ['セイ', 'ショウ'], ['こえ'], ['voice'], 2, 7),
    ("星", ['セイ', 'ショウ'], ['ほし'], ['star'], 2, 9),
    ("晴", ['セイ'], ['は'], ['clear'], 2, 12),
    ("切", ['セツ', 'サイ'], ['き'], ['cut'], 2, 4),
    ("雪", ['セツ'], ['ゆき'], ['snow'], 2, 11),
    ("船", ['セン'], ['ふね', 'ふな'], ['ship'], 2, 11),
    ("線", ['セン'], [], ['line'], 2, 15),
    ("前", ['ゼン'], ['まえ'], ['before'], 2, 9),
    ("組", ['ソ'], ['く'], ['group'], 2, 11),
    ("走", ['ソウ'], ['はし'], ['run'], 2, 7),
    ("多", ['タ'], ['おお'], ['many'], 2, 6),
    ("太", ['タイ', 'タ'], ['ふと'], ['thick'], 2, 4),
    ("体", ['タイ', 'テイ'], ['からだ'], ['body'], 2, 7),
    ("台", ['ダイ', 'タイ'], [], ['platform'], 2, 5),
    ("地", ['チ', 'ジ'], [], ['ground'], 2, 6),
    ("池", ['チ'], ['いけ'], ['pond'], 2, 6),
    ("知", ['チ'], ['し'], ['know'], 2, 8),
    ("茶", ['チャ', 'サ'], [], ['tea'], 2, 9),
    ("昼", ['チュウ'], ['ひる'], ['noon'], 2, 9),
    ("長", ['チョウ'], ['なが'], ['long'], 2, 8),
    ("鳥", ['チョウ'], ['とり'], ['bird'], 2, 11),
    ("朝", ['チョウ'], ['あさ'], ['morning'], 2, 12),
    ("直", ['チョク', 'ジキ'], ['ただ', 'なお'], ['straight'], 2, 8),
    ("通", ['ツウ', 'ツ'], ['とお', 'かよ'], ['pass'], 2, 10),
    ("弟", ['テイ', 'ダイ', 'デ'], ['おとうと'], ['younger brother'], 2, 7),
    ("店", ['テン'], ['みせ'], ['shop'], 2, 8),
    ("点", ['テン'], [], ['point'], 2, 9),
    ("電", ['デン'], [], ['electricity'], 2, 13),
    ("刀", ['トウ'], ['かたな'], ['sword'], 2, 2),
    ("冬", ['トウ'], ['ふゆ'], ['winter'], 2, 5),
    ("当", ['トウ'], ['あ'], ['hit'], 2, 6),
    ("東", ['トウ'], ['ひがし'], ['east'], 2, 8),
    ("答", ['トウ'], ['こた'], ['answer'], 2, 12),
    ("頭", ['トウ', 'ズ', 'ト'], ['あたま', 'かしら'], ['head'], 2, 16),
    ("同", ['ドウ'], ['おな'], ['same'], 2, 6),
    ("道", ['ドウ', 'トウ'], ['みち'], ['road'], 2, 12),
    ("読", ['ドク', 'トク', 'トウ'], ['よ'], ['read'], 2, 14),
    ("内", ['ナイ', 'ダイ'], ['うち'], ['inside'], 2, 4),
    ("南", ['ナン', 'ナ'], ['みなみ'], ['south'], 2, 9),
    ("肉", ['ニク'], [], ['meat'], 2, 6),
    ("馬", ['バ'], ['うま', 'ま'], ['horse'], 2, 10),
    ("売", ['バイ'], ['う'], ['sell'], 2, 7),
    ("買", ['バイ'], ['か'], ['buy'], 2, 12),
    ("麦", ['バク'], ['むぎ'], ['wheat'], 2, 7),
    ("半", ['ハン'], ['なか'], ['half'], 2, 5),
    ("番", ['バン'], [], ['number'], 2, 12),
    ("父", ['フ'], ['ちち'], ['father'], 2, 4),
    ("風", ['フウ', 'フ'], ['かぜ', 'かざ'], ['wind'], 2, 9),
    ("分", ['ブン', 'フン', 'ブ'], ['わ'], ['part'], 2, 4),
    ("聞", ['ブン', 'モン'], ['き'], ['hear'], 2, 14),
    ("米", ['ベイ', 'マイ'], ['こめ'], ['rice'], 2, 6),
    ("歩", ['ホ', 'ブ', 'フ'], ['ある', 'あゆ'], ['walk'], 2, 8),
    ("母", ['ボ'], ['はは'], ['mother'], 2, 5),
    ("方", ['ホウ'], ['かた'], ['direction'], 2, 4),
    ("北", ['ホク'], ['きた'], ['north'], 2, 5),
    ("毎", ['マイ'], [], ['every'], 2, 6),
    ("妹", ['マイ'], ['いもうと'], ['younger sister'], 2, 8),
    ("万", ['マン', 'バン'], [], ['ten thousand'], 2, 3),
    ("明", ['メイ', 'ミョウ'], ['あか', 'あき', 'あ'], ['bright'], 2, 8),
    ("鳴", ['メイ'], ['な'], ['sound'], 2, 14),
    ("毛", ['モウ'], ['け'], ['hair'], 2, 4),
    ("門", ['モン'], ['かど'], ['gate'], 2, 8),
    ("夜", ['ヤ'], ['よ', 'よる'], ['night'], 2, 8),
    ("野", ['ヤ'], ['の'], ['field'], 2, 11),
    ("友", ['ユウ'], ['とも'], ['friend'], 2, 4),
    ("用", ['ヨウ'], ['もち'], ['use'], 2, 5),
    ("曜", ['ヨウ'], [], ['day of week'], 2, 18),
    ("来", ['ライ'], ['く', 'き', 'こ'], ['come'], 2, 7),
    ("里", ['リ'], ['さと'], ['village'], 2, 7),
    ("理", ['リ'], [], ['reason'], 2, 11),
    ("話", ['ワ'], ['はな', 'はなし'], ['talk'], 2, 13),
    ("何", ['カ'], ['なに', 'なん'], ['what'], 2, 7),
]

if __name__ == "__main__":
    print(f"小学2年生: {len(GRADE_2_KANJI)}字")
    # サンプル表示
    for kanji, on_yomi, kun_yomi, meanings, grade, strokes in GRADE_2_KANJI[:5]:
        print(f"{kanji} - 音読み: {on_yomi}, 訓読み: {kun_yomi}, 意味: {meanings}")

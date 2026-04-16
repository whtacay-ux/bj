import localeInfo

IMG_DIR = "d:/ymir work/ui/game/black_jack/"

window = {
	"name" : "BlackjackWindow",
	"style" : ("movable", "float",),

	"x" : 0, "y" : 0,

	"width" : 420,
	"height" : 380,

	"children" :
	(
				{
					"name" : "board",
					"type" : "board",
					"style" : ("attach",),

					"x" : 0, "y" : 0,

					"width" : 420,
					"height" : 380,

					"children" :
					(
						## Title Bar
						{
							"name" : "TitleBar",
							"type" : "titlebar",
							"style" : ("attach",),

							"x" : 8, "y" : 7,
							"width" : 404,

							"children" :
							(
								{ "name":"TitleName", "type":"text", "x":202, "y":3, "text":"Blackjack", "text_horizontal_align":"center" },
							),
						},

						## Background Image
						{
							"name" : "BlackjackBG",
							"type" : "image",
							"x" : 13, "y" : 35,
							"image" : IMG_DIR + "bg.tga",
						},

				## Scores
				{ "name":"DealerScoreLabel", "type":"text", "x":210, "y":50, "text":"Krupiye Skoru:", "text_horizontal_align":"center" },
				{ "name":"DealerScoreValue", "type":"text", "x":210, "y":70, "text":"0", "text_horizontal_align":"center" },

				{ "name":"PlayerScoreLabel", "type":"text", "x":210, "y":240, "text":"Senin Skorun:", "text_horizontal_align":"center" },
				{ "name":"PlayerScoreValue", "type":"text", "x":210, "y":260, "text":"0", "text_horizontal_align":"center" },

				## Bet Input
				{
					"name" : "BetInputSlot",
					"type" : "image",
					"x" : 160, "y" : 290,
					"image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"children" :
					(
						{
							"name" : "BetInput",
							"type" : "editline",
							"x" : 3, "y" : 3,
							"width" : 94, "height" : 18,
							"input_limit" : 12,
							"text" : "1000",
						},
					),
				},

				## Main Buttons
				{
					"name" : "BetButton",
					"type" : "button",
					"x" : 260, "y" : 287,
					"text" : "Bahis Yap",
					"default_image" : IMG_DIR + "play_btn_0.tga",
					"over_image" : IMG_DIR + "play_btn_1.tga",
					"down_image" : IMG_DIR + "play_btn_2.tga",
				},
				{
					"name" : "ClearBetButton",
					"type" : "button",
					"x" : 80, "y" : 287,
					"text" : "Temizle",
					"default_image" : IMG_DIR + "stand_btn_0.tga",
					"over_image" : IMG_DIR + "stand_btn_1.tga",
					"down_image" : IMG_DIR + "stand_btn_2.tga",
				},
				{
					"name" : "NewGameButton",
					"type" : "button",
					"x" : 160, "y" : 325,
					"text" : "Yeni Oyun",
					"default_image" : IMG_DIR + "play_btn_0.tga",
					"over_image" : IMG_DIR + "play_btn_1.tga",
					"down_image" : IMG_DIR + "play_btn_2.tga",
				},

				## Action Buttons
				{
					"name" : "HitButton",
					"type" : "button",
					"x" : 30, "y" : 325,
					"text" : "Hit",
					"default_image" : IMG_DIR + "new_card_btn_0.tga",
					"over_image" : IMG_DIR + "new_card_btn_1.tga",
					"down_image" : IMG_DIR + "new_card_btn_2.tga",
				},
				{
					"name" : "StandButton",
					"type" : "button",
					"x" : 95, "y" : 325,
					"text" : "Stand",
					"default_image" : IMG_DIR + "stand_btn_0.tga",
					"over_image" : IMG_DIR + "stand_btn_1.tga",
					"down_image" : IMG_DIR + "stand_btn_2.tga",
				},
				{
					"name" : "DoubleButton",
					"type" : "button",
					"x" : 160, "y" : 325,
					"text" : "Double",
					"default_image" : IMG_DIR + "increase_btn_0.tga",
					"over_image" : IMG_DIR + "increase_btn_1.tga",
					"down_image" : IMG_DIR + "increase_btn_2.tga",
				},
				{
					"name" : "SplitButton",
					"type" : "button",
					"x" : 225, "y" : 325,
					"text" : "Split",
					"default_image" : IMG_DIR + "increase_btn_0.tga",
					"over_image" : IMG_DIR + "increase_btn_1.tga",
					"down_image" : IMG_DIR + "increase_btn_2.tga",
				},
				{
					"name" : "InsuranceButton",
					"type" : "button",
					"x" : 290, "y" : 325,
					"text" : "Sigorta",
					"default_image" : IMG_DIR + "increase_btn_0.tga",
					"over_image" : IMG_DIR + "increase_btn_1.tga",
					"down_image" : IMG_DIR + "increase_btn_2.tga",
				},
				{
					"name" : "SurrenderButton",
					"type" : "button",
					"x" : 355, "y" : 325,
					"text" : "Teslim Ol",
					"default_image" : IMG_DIR + "stand_btn_0.tga",
					"over_image" : IMG_DIR + "stand_btn_1.tga",
					"down_image" : IMG_DIR + "stand_btn_2.tga",
				},
			),
		},
	),
}

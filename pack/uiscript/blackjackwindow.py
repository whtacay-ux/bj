import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "BlackjackWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 400,
	"height" : 350,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 400,
			"height" : 350,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 384,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":192, "y":3, "text":"Blackjack", "text_horizontal_align":"center" },
					),
				},

				## Dealer Cards
				{
					"name" : "DealerArea",
					"type" : "window",
					"x" : 10, "y" : 40, "width" : 380, "height" : 100,
					"children" : (
						{"name":"DealerText", "type":"text", "x":0, "y":0, "text":"Krupiye", "all_align":"center"},
						{"name":"DealerScoreValue", "type":"text", "x":0, "y":20, "text":"0", "all_align":"center"},
						{"name":"DealerCardSlot_0", "type":"image", "x":50, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"DealerCardValue_0", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"DealerCardSlot_1", "type":"image", "x":80, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"DealerCardValue_1", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"DealerCardSlot_2", "type":"image", "x":110, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"DealerCardValue_2", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"DealerCardSlot_3", "type":"image", "x":140, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"DealerCardValue_3", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"DealerCardSlot_4", "type":"image", "x":170, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"DealerCardValue_4", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
					),
				},

				## Player Cards
				{
					"name" : "PlayerArea",
					"type" : "window",
					"x" : 10, "y" : 130, "width" : 380, "height" : 100,
					"children" : (
						{"name":"PlayerText", "type":"text", "x":0, "y":0, "text":"Siz", "all_align":"center"},
						{"name":"PlayerScoreValue", "type":"text", "x":0, "y":20, "text":"0", "all_align":"center"},
						{"name":"PlayerCardSlot_0", "type":"image", "x":50, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"PlayerCardValue_0", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"PlayerCardSlot_1", "type":"image", "x":80, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"PlayerCardValue_1", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"PlayerCardSlot_2", "type":"image", "x":110, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"PlayerCardValue_2", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"PlayerCardSlot_3", "type":"image", "x":140, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"PlayerCardValue_3", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
						{"name":"PlayerCardSlot_4", "type":"image", "x":170, "y":40, "image":"d:/ymir work/ui/public/parameter_slot_01.sub", "children":({"name":"PlayerCardValue_4", "type":"text", "x":0, "y":0, "text":"", "all_align":"center"},)},
					),
				},

				## Controls
				{
					"name" : "ControlArea",
					"type" : "window",
					"x" : 10, "y" : 240, "width" : 380, "height" : 100,
					"children" : (
						{
							"name" : "BetInputSlot",
							"type" : "image",
							"x" : 50, "y" : 10,
							"default_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
							"children" : (
								{
									"name" : "BetInput",
									"type" : "editline",
									"x" : 3, "y" : 3,
									"width" : 100, "height" : 20,
									"input_limit" : 12,
									"text" : "1000",
								},
							),
						},
						{
							"name" : "ClearBetButton",
							"type" : "button",
							"x" : 160, "y" : 10,
							"text" : "Temizle",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "BetButton",
							"type" : "button",
							"x" : 220, "y" : 10,
							"text" : "Bahis Yap",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "NewGameButton",
							"type" : "button",
							"x" : 280, "y" : 10,
							"text" : "Yeni Oyun",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "HitButton",
							"type" : "button",
							"x" : 20, "y" : 40,
							"text" : "Hit",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "StandButton",
							"type" : "button",
							"x" : 80, "y" : 40,
							"text" : "Stand",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "DoubleButton",
							"type" : "button",
							"x" : 140, "y" : 40,
							"text" : "Double",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "SplitButton",
							"type" : "button",
							"x" : 200, "y" : 40,
							"text" : "Split",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "InsuranceButton",
							"type" : "button",
							"x" : 260, "y" : 40,
							"text" : "Sigorta",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
						{
							"name" : "SurrenderButton",
							"type" : "button",
							"x" : 320, "y" : 40,
							"text" : "Teslim Ol",
							"default_image" : ROOT + "middle_button_01.sub",
							"over_image" : ROOT + "middle_button_02.sub",
							"down_image" : ROOT + "middle_button_03.sub",
						},
					),
				},
			),
		},
	),
}

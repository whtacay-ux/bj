import localeInfo

IMG_DIR = "black_jack/"

BG_IMAGE = (394, 294)

WINDOW_WIDTH = 13+BG_IMAGE[0]+13
WINDOW_HEIGHT = 35+BG_IMAGE[1]+13


window = {
	"name" : "BlackJackGame",
	"x" : 0, "y" : 0,
	"style" : ("movable", "float", "animate",),
	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,
	"children" :
	(
		{
			"name" : "Window",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"x" : 0, "y" : 0,
			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGHT,
			"title":"BlackJack",
			"children" :
			(
				{
					"name":"board",
					"type":"image",
					"x":13,"y":35,
					"image":IMG_DIR+"bg.tga",
					"children" :
					(
						{"name":"dealer_text","type":"text","style" : ("not_pick",),"x":200,"y":15,"text_horizontal_align":"center","text": localeInfo.BLACKJACK_DEALER,},
						{"name":"me_text","type":"text","style" : ("not_pick",),"x":200,"y":BG_IMAGE[1]-88,"text_horizontal_align":"center","text": localeInfo.BLACKJACK_ME,},
						{"name":"reward_text","type":"text","style" : ("not_pick",),"x":30,"y":BG_IMAGE[1]-63,"text_horizontal_align":"center","text": localeInfo.BLACKJACK_REWARD,},
						{"name":"reward_item","type":"image","x":15,"y":BG_IMAGE[1]-40,"image": "icon/item/50011.tga",},
						{"name":"deal_text","type":"text","style" : ("not_pick",),"x":121,"y":BG_IMAGE[1]-45,"text_horizontal_align":"center","text": localeInfo.BLACKJACK_DEAL,},
						{"name":"deal","type":"text","style" : ("not_pick",),"x":121,"y":BG_IMAGE[1]-25,"text_horizontal_align":"center","text": "0",},
						{
							"name" : "decreaseDealBtn",
							"type" : "button",
							"x" : 67,
							"y" : BG_IMAGE[1]-33,
							"default_image" : IMG_DIR+"decrease_btn_0.tga",
							"over_image" : IMG_DIR+"decrease_btn_1.tga",
							"down_image" : IMG_DIR+"decrease_btn_2.tga",
							"disable_image" : IMG_DIR+"decrease_btn_2.tga",
						},
						{
							"name" : "increaseDealBtn",
							"type" : "button",
							"x" : 147,
							"y" : BG_IMAGE[1]-33,
							"default_image" : IMG_DIR+"increase_btn_0.tga",
							"over_image" : IMG_DIR+"increase_btn_1.tga",
							"down_image" : IMG_DIR+"increase_btn_2.tga",
							"disable_image" : IMG_DIR+"increase_btn_2.tga",
						},
						{
							"name" : "startBtn",
							"type" : "button",
							"x" : 227,
							"y" : BG_IMAGE[1]-37,
							"text":localeInfo.BLACKJACK_STARTGAME,
							"default_image" : IMG_DIR+"play_btn_0.tga",
							"over_image" : IMG_DIR+"play_btn_1.tga",
							"down_image" : IMG_DIR+"play_btn_2.tga",
							"disable_image" : IMG_DIR+"play_btn_2.tga",
						},
						{
							"name" : "standBtn",
							"type" : "button",
							"x" : 200,
							"y" : BG_IMAGE[1]-37,
							"text":localeInfo.BLACKJACK_STAND,
							"default_image" : IMG_DIR+"stand_btn_0.tga",
							"over_image" : IMG_DIR+"stand_btn_1.tga",
							"down_image" : IMG_DIR+"stand_btn_2.tga",
							"disable_image" : IMG_DIR+"stand_btn_2.tga",
						},
						{
							"name" : "newCardBtn",
							"type" : "button",
							"x" : 200+85,
							"y" : BG_IMAGE[1]-37,
							"text":localeInfo.BLACKJACK_NEWCARD,
							"default_image" : IMG_DIR+"new_card_btn_0.tga",
							"over_image" : IMG_DIR+"new_card_btn_1.tga",
							"down_image" : IMG_DIR+"new_card_btn_2.tga",
							"disable_image" : IMG_DIR+"new_card_btn_2.tga",
						},
					),
				},
			),
		},
	),
}

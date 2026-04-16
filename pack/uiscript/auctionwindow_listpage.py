SEARCHING_AREA_X_POS = 15
SEARCHING_AREA_Y_POS = 235

window = {
	"name" : "AuctionWindow_RegisterPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		{
			"name" : "NumberPrint",
			"type" : "text",
			"x" : 18,
			"y" : 7,
			"text" : "��ȣ",
		},
		{
			"name" : "NamePrint",
			"type" : "text",
			"x" : 79,
			"y" : 7,
			"text" : "������ �̸�",
		},
		{
			"name" : "NamePrint",
			"type" : "text",
			"x" : 228,
			"y" : 7,
			"text" : "����",
		},

		{
			"name" : "ItemSearchAreaBar",
			"type" : "horizontalbar",

			"x" : 0,
			"y" : 235,
			"width" : 330,
			"horizontal_align" : "center",
			"children" :
			(

				{
					"name" : "ItemSearchAreaBarPrint",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"text" : "������ �˻��ϱ�",
					"all_align" : "center",
				},

			),
		},

		{
			"name" : "SearchingNamePrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 5,
			"y" : SEARCHING_AREA_Y_POS + 24,
			"text" : "�������̸�",
		},
		{
			"name" : "SearchingNameSlot",
			"type" : "image",
			"x" : SEARCHING_AREA_X_POS + 68,
			"y" : SEARCHING_AREA_Y_POS + 22,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",
		},

		{
			"name" : "SearchingIDPrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 5,
			"y" : SEARCHING_AREA_Y_POS + 44,
			"text" : "��ȣ��ã��",
		},
		{
			"name" : "SearchingIDSlot",
			"type" : "image",
			"x" : SEARCHING_AREA_X_POS + 68,
			"y" : SEARCHING_AREA_Y_POS + 42,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",
		},

		{
			"name" : "SearchingIDPrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 205,
			"y" : SEARCHING_AREA_Y_POS + 24,
			"text" : "���Ͽ���",
		},

		{
			"name" : "SearchingButtonByName",
			"type" : "button",
			"x" : SEARCHING_AREA_X_POS + 295,
			"y" : SEARCHING_AREA_Y_POS + 20,
			"text" : "ã��",
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "SearchingButtonByID",
			"type" : "button",
			"x" : SEARCHING_AREA_X_POS + 295,
			"y" : SEARCHING_AREA_Y_POS + 40,
			"text" : "ã��",
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

	),
}

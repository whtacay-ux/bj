import uiScriptLocale

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
#Big-List
#SERVER_BOARD_HEIGHT = 180 + 390
#SERVER_LIST_HEIGHT = 171 + 350
#Small list like german
import localeInfo
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180
SERVER_BOARD_WEIGHT = 375 
window = {
	"name" : "LoginWindow",
	"style" : ("movable",),
	
	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	[

		## Board

		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : "d:/ymir work/ui/login.sub",
		},


		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "window",

			"x" : 0,
			"y" : 0,
			
			"horizontal_align" : "center",
			"vertical_align" : "center",
			
			"width" : 800,
			"height" : 550,

			"image" : "d:/ymir work/ui/tunga/login/dialogbg.dds",

			"children" :
			(
				{
					"name" : "RegisterBoard",
					"type" : "window",
					"x" : 515,
					"y" : 87,
					"width" : 240,
					"height" : 260,
					"children" :
					(
						{
							"name" : "registerButton1",
							"type" : "button",

							"x" : 0,
							"y" : 0,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton1",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",

								},
							),
						},
						
						{
							"name" : "registerButton2",
							"type" : "button",

							"x" : 0,
							"y" : 38,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton2",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",
								},
							),
						},
						
						{
							"name" : "registerButton3",
							"type" : "button",

							"x" : 0,
							"y" : 38*2,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton3",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",

								},
							),
						},
						
						{
							"name" : "registerButton4",
							"type" : "button",

							"x" : 0,
							"y" : 38*3,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton4",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",

								},
							),
						},
						{
							"name" : "registerButton5",
							"type" : "button",

							"x" : 0,
							"y" : 38*4,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton5",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",
								},
							),
						},
						{
							"name" : "registerButton6",
							"type" : "button",

							"x" : 0,
							"y" : 38*5,

							"default_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/accounts_button2.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/accounts_button.tga",

							"text" : uiScriptLocale.FREE,
							"children":
							(
								{
									"name" : "deleteButton6",
									"type" : "button",

									"x" : 115,
									"y" : 7,

									"default_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"over_image" : "d:/ymir work/ui/tunga/login/delete.tga",
									"down_image" : "d:/ymir work/ui/tunga/login/delete.tga",
								},
							),
						},
					)
				},
				{
					"name" : "Login_back",
					"type" : "image",
					
					"x" : 0,
					"y" : 87,
					
					"image" : "d:/ymir work/ui/tunga/login/dialogbg.dds",
					"children":
					(
						{
							"name" : "Metin2_Board_Logo",
							"type" : "image",
							"image" : "d:/ymir work/ui/tunga/login/logo.tga",
							"x" : -55,
							"y" : -125,
						},
						{
							"name" : "ID_BACKGROUND",
							"type" : "image",
							"x" : 16,
							"y" : 65,
							"image" : "d:/ymir work/ui/tunga/login/user_input.dds",
							"children" : 
							(
								{
									"name" : "ID_EditLine",
									"type" : "editline",

									"x" : 50,
									"y" : 8,

									"width" : 194,
									"height" : 22,

									"input_limit" : 19,
									"enable_codepage" : 0,

									"fontsize" : "LARGE",
									"color" : 0xff8d5e51,

								},
							),
						},
						{
							"name" : "PW_BACKGROUND",
							"type" : "image",
							"x" : 16,
							"y" : 105,
							"image" : "d:/ymir work/ui/tunga/login/pw_input.dds",
							"children" : 
							(
								{
									"name" : "Password_EditLine",
									"type" : "editline",

									"x" : 50,
									"y" : 8,

									"width" : 194,
									"height" : 22,

									"input_limit" : 16,
									"secret_flag" : 1,
									"enable_codepage" : 0,

									"fontsize" : "LARGE",

									"color" : 0xff8d5e51,
								},
							),
						},


						{
							"name" : "LoginButton",
							"type" : "button",

							"x" : 17,
							"y" : 147,

							"default_image" : "d:/ymir work/ui/tunga/login/login_btn_default.dds",
							"over_image" : "d:/ymir work/ui/tunga/login/login_btn_over.dds",
							"down_image" : "d:/ymir work/ui/tunga/login/login_btn_down.dds",

						#	"text" : uiScriptLocale.LOGIN_CONNECT,
						},
						{
							"name" : "passwordresetbutton",
							"type" : "button",
							
							"x" : 100,
							"y" : 190,
							"width" : 93,
							"height" : 19,
							
							"children" : 
							(
								{ "name" : "ForgotPwText", "type" : "text", "x" : 0, "y" : 0, "text" :  uiScriptLocale.PASSWORD_RESTART, "color" : 0xff905f53, "all_align" : "center","fontsize" : "LARGE", },
							),
						},

						{
							"name" : "ChannelButton1",
							"type" : "radio_button",
					
							"x" : 271,
							"y" : 65,
					
					
							"default_image" : "d:/ymir work/ui/tunga/login/ch_btn_default.dds",
							"over_image" : "d:/ymir work/ui/tunga/login/ch_btn_over.dds",
							"down_image" : "d:/ymir work/ui/tunga/login/ch_btn_down.dds",

							"children":
							(
								{
									"name" : "ChannelButton1_Name",
									"type" : "text",
									"x" : 0,
									"y" : 4,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "CH1",
									
									"fontsize" : "LARGE",
									"color" : 0xffa8602c,
								},
								{
									"name" : "ChannelButtonTooltip1",
									"type" : "text",
					
									"x" : 0,
									"y" : 23,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "OFF",
									"color" : 0xffb77643,			
								},
							),						
						},
						{
							"name" : "ChannelButton2",
							"type" : "radio_button",
					
							"x" : 386,
							"y" : 65,

							"default_image" : "d:/ymir work/ui/tunga/login/ch_btn_default.dds",
							"over_image" : "d:/ymir work/ui/tunga/login/ch_btn_over.dds",
							"down_image" : "d:/ymir work/ui/tunga/login/ch_btn_down.dds",	
							"children":
							(
								{
									"name" : "ChannelButton2_Name",
									"type" : "text",
									"x" : 0,
									"y" : 4,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "CH2",
									
									"fontsize" : "LARGE",
									"color" : 0xffa8602c,
								},
								{
									"name" : "ChannelButtonTooltip2",
									"type" : "text",
					
									"x" : 0,
									"y" : 23,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "OFF",
									"color" : 0xffb77643,					
								},
							),								
						},

						{
							"name" : "ChannelButton3",
							"type" : "radio_button",
					
							"x" : 271,
							"y" : 116,
					
							"default_image" : "d:/ymir work/ui/tunga/login/ch_btn_default.dds",
							"over_image" : "d:/ymir work/ui/tunga/login/ch_btn_over.dds",
							"down_image" : "d:/ymir work/ui/tunga/login/ch_btn_down.dds",	
							"children":
							(
								{
									"name" : "ChannelButton3_Name",
									"type" : "text",
									"x" : 0,
									"y" : 4,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "CH3",
									
									"fontsize" : "LARGE",
									"color" : 0xffa8602c,
								},
								{
									"name" : "ChannelButtonTooltip3",
									"type" : "text",
					
									"x" : 0,
									"y" : 23,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "OFF",
									"color" : 0xffb77643,					
								},
							),				
						},
				
						{
							"name" : "ChannelButton4",
							"type" : "radio_button",
					
							"x" : 386,
							"y" : 116,
					
							"default_image" : "d:/ymir work/ui/tunga/login/ch_btn_default.dds",
							"over_image" : "d:/ymir work/ui/tunga/login/ch_btn_over.dds",
							"down_image" : "d:/ymir work/ui/tunga/login/ch_btn_down.dds",	
							"children":
							(
								{
									"name" : "ChannelButton4_Name",
									"type" : "text",
									"x" : 0,
									"y" : 4,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "CH4",
									
									"fontsize" : "LARGE",
									"color" : 0xffa8602c,
								},
								{
									"name" : "ChannelButtonTooltip4",
									"type" : "text",
					
									"x" : 0,
									"y" : 23,
									
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",
									
									"text" : "OFF",
									"color" : 0xffb77643,			
								},
							),				
						},
						{
							"name" : "facebook",
							"type" : "button",

							"x" : 320,
							"y" : 200,

							"default_image" : "d:/ymir work/ui/tunga/login/facebook_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/facebook_button.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/facebook_button.tga",
						},
						{
							"name" : "instagram",
							"type" : "button",

							"x" : 320+42,
							"y" : 200,

							"default_image" : "d:/ymir work/ui/tunga/login/instagram_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/instagram_button.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/instagram_button.tga",
						},
						{
							"name" : "youtube",
							"type" : "button",

							"x" : 320+84,
							"y" : 200,

							"default_image" : "d:/ymir work/ui/tunga/login/youtube_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/youtube_button.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/youtube_button.tga",
						},
						{
							"name" : "discord",
							"type" : "button",

							"x" : 320+42*3,
							"y" : 200,

							"default_image" : "d:/ymir work/ui/tunga/login/discord_button.tga",
							"over_image" : "d:/ymir work/ui/tunga/login/discord_button.tga",
							"down_image" : "d:/ymir work/ui/tunga/login/discord_button.tga",
						},
						{
							"name" : "ServerList",
							"type" : "listbox",

							"x" : 30,
							"y" : 210,
							#"width" : 100,
							#"height" : SERVER_LIST_HEIGHT,
							"row_count" : 15,
							"item_align" : 0,
						},
					),
				},
				{
					"name" : "LanguageBoard",
					"type" : "window",
					"x" : 30,
					"y" : 310,
					"width" : 340,
					"height" : 50,
					"children" :
					(
						{
							"name" : "ChangeLanguageTr",
							"type" : "radio_button",

							"x": 0,
							"y": 0,
							"default_image": "d:/ymir work/ui/tunga/login/language/flag_tr_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_tr_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_tr_norm.tga",
						},
						{
							"name" : "ChangeLanguageEn",
							"type" : "radio_button",

							"x": 40,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_en_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_en_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_en_norm.tga",
						},
						{
							"name" : "ChangeLanguagePt",
							"type" : "radio_button",

							"x": 40*2,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_pt_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_pt_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_pt_norm.tga",
						},
						{
							"name" : "ChangeLanguageDe",
							"type" : "radio_button",

							"x": 40*3,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_de_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_de_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_de_norm.tga",
						},
						{
							"name" : "ChangeLanguageRo",
							"type" : "radio_button",

							"x": 40*4,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_ro_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_ro_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_ro_norm.tga",
						},
						{
							"name" : "ChangeLanguageEs",
							"type" : "radio_button",

							"x": 40*5,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_es_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_es_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_es_norm.tga",
						},
						{
							"name" : "ChangeLanguageHu",
							"type" : "radio_button",

							"x": 40*6,
							"y": 0,

							"default_image": "d:/ymir work/ui/tunga/login/language/flag_hu_norm.tga",
							"over_image": "d:/ymir work/ui/tunga/login/language/flag_hu_over.tga",
							"down_image": "d:/ymir work/ui/tunga/login/language/flag_hu_norm.tga",
						},
					)
				},

				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 360,
					"y" : 360,
					"default_image" : "d:/ymir work/ui/tunga/login/exit_btn_default.dds",
					"over_image" : "d:/ymir work/ui/tunga/login/exit_btn_over.dds",
					"down_image" : "d:/ymir work/ui/tunga/login/exit_btn_down.dds",

				},
			),
		},




	],
}
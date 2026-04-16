import uiScriptLocale

ROOT_DIR = "d:/ymir work/ui/game/guild/guildmemberpage/"
window = {
	"name" : "GuildWindow_MemberPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(
		## ScrollBar
		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 341,
			"y" : 20,
			"scrollbar_type" : "normal",
			"size" : 270,
		},

		## Grade
		{
			"name" : "IndexName", "type" : "image", "x" : 43, "y" : 8, "image" : ROOT_DIR+"IndexName.sub",
		},
		{
			"name" : "IndexGrade", "type" : "image", "x" : 119, "y" : 8, "image" : ROOT_DIR+"IndexGrade.sub",
		},
		{
			"name" : "IndexJob", "type" : "image", "x" : 177, "y" : 8, "image" : ROOT_DIR+"IndexJob.sub",
		},
		{
			"name" : "IndexLevel", "type" : "image", "x" : 217, "y" : 8, "image" : ROOT_DIR+"IndexLevel.sub",
		},
		{
			"name" : "IndexOffer", "type" : "image", "x" : 251, "y" : 8, "image" : ROOT_DIR+"IndexOffer.sub",
		},
		{
			"name" : "IndexGeneral", "type" : "image", "x" : 304, "y" : 8, "image" : ROOT_DIR+"IndexGeneral.sub",
		},

	),
}

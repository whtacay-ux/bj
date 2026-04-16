import app
import localeInfo
app.ServerName = None

SRV1 = {
	"name":"Metin2Korsan",
	"host":"192.168.1.20",
	"auth1":30001,
	"ch1":30003,
	"ch2":30009,
	"ch3":30015,
	"ch4":30021,
}



STATE_NONE = "|cFFdadada" + localeInfo.CHANNEL_STATUS_OFFLINE

STATE_DICT = {
	0 : "|cFFffffff" + localeInfo.CHANNEL_STATUS_OFFLINE,
	1 : "|cFF00ff00" + localeInfo.CHANNEL_STATUS_RECOMMENDED,
	2 : "|cFFffc000" + localeInfo.CHANNEL_STATUS_BUSY,
	3 : "|cFFff0000" + localeInfo.CHANNEL_STATUS_FULL,
}

SERVER1_CHANNEL_DICT = {
	1:{"key":11,"name":"CH1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"CH2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"CH3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"CH4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}


REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
	}
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SERVER1_CHANNEL_DICT, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}


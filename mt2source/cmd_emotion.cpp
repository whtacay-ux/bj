#include "stdafx.h"
#include "utils.h"
#include "char.h"
#include "char_manager.h"
#include "motion.h"
#include "packet.h"
#include "buffer_manager.h"
#include "unique_item.h"
#include "wedding.h"

#define NEED_TARGET	(1 << 0)
#define NEED_PC		(1 << 1)
#define WOMAN_ONLY	(1 << 2)
#define OTHER_SEX_ONLY	(1 << 3)
#define SELF_DISARM	(1 << 4)
#define TARGET_DISARM	(1 << 5)
#define BOTH_DISARM	(SELF_DISARM | TARGET_DISARM)

struct emotion_type_s
{
	const char* command;
	const char* command_to_client;
	long	flag;
	float	extra_delay;
} emotion_types[] = {
	{ "Ű��",	"french_kiss",	NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		2.0f },
	{ "�ǻ�",	"kiss",		NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		1.5f },
	{ "����",	"slap",		NEED_PC | SELF_DISARM,				1.5f },
	{ "�ڼ�",	"clap",		0,						1.0f },
	{ "��",		"cheer1",	0,						1.0f },
	{ "����",	"cheer2",	0,						1.0f },

	// DANCE
	{ "��1",	"dance1",	0,						1.0f },
	{ "��2",	"dance2",	0,						1.0f },
	{ "��3",	"dance3",	0,						1.0f },
	{ "��4",	"dance4",	0,						1.0f },
	{ "��5",	"dance5",	0,						1.0f },
	{ "��6",	"dance6",	0,						1.0f },
	// END_OF_DANCE
	{ "����",	"congratulation",	0,				1.0f	},
	{ "�뼭",	"forgive",			0,				1.0f	},
	{ "ȭ��",	"angry",			0,				1.0f	},
	{ "��Ȥ",	"attractive",		0,				1.0f	},
	{ "����",	"sad",				0,				1.0f	},
	{ "���",	"shy",				0,				1.0f	},
	{ "����",	"cheerup",			0,				1.0f	},
	{ "����",	"banter",			0,				1.0f	},
	{ "���",	"joy",				0,				1.0f	},
#ifdef ENABLE_EMOJI_UPDATE
	{ "��ī",	"selfie",				0,				1.0f	},
	{ "��7",	"dance7",				0,				1.0f	},
	{ "����",	"doze",				0,				1.0f	},
	{ "�",	"exercise",				0,				1.0f	},
	{ "Ǫ�� ��",	"pushup",				0,				1.0f	},
#endif
	{ "\n",	"\n",		0,						0.0f },
	/*
	//{ "Ű��",		NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		MOTION_ACTION_FRENCH_KISS,	 1.0f },
	{ "�ǻ�",		NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		MOTION_ACTION_KISS,		 1.0f },
	{ "���ȱ�",		NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		MOTION_ACTION_SHORT_HUG,	 1.0f },
	{ "����",		NEED_PC | OTHER_SEX_ONLY | BOTH_DISARM,		MOTION_ACTION_LONG_HUG,		 1.0f },
	{ "�������",	NEED_PC | SELF_DISARM,				MOTION_ACTION_PUT_ARMS_SHOULDER, 0.0f },
	{ "��¯",		NEED_PC	| WOMAN_ONLY | SELF_DISARM,		MOTION_ACTION_FOLD_ARM,		 0.0f },
	{ "����",		NEED_PC | SELF_DISARM,				MOTION_ACTION_SLAP,		 1.5f },

	{ "���Ķ�",		0,						MOTION_ACTION_CHEER_01,		 0.0f },
	{ "����",		0,						MOTION_ACTION_CHEER_02,		 0.0f },
	{ "�ڼ�",		0,						MOTION_ACTION_CHEER_03,		 0.0f },

	{ "ȣȣ",		0,						MOTION_ACTION_LAUGH_01,		 0.0f },
	{ "űű",		0,						MOTION_ACTION_LAUGH_02,		 0.0f },
	{ "������",		0,						MOTION_ACTION_LAUGH_03,		 0.0f },

	{ "����",		0,						MOTION_ACTION_CRY_01,		 0.0f },
	{ "����",		0,						MOTION_ACTION_CRY_02,		 0.0f },

	{ "�λ�",		0,						MOTION_ACTION_GREETING_01,	0.0f },
	{ "����",		0,						MOTION_ACTION_GREETING_02,	0.0f },
	{ "�����λ�",	0,						MOTION_ACTION_GREETING_03,	0.0f },

	{ "��",		0,						MOTION_ACTION_INSULT_01,	0.0f },
	{ "���",		SELF_DISARM,					MOTION_ACTION_INSULT_02,	0.0f },
	{ "����",		0,						MOTION_ACTION_INSULT_03,	0.0f },

	{ "�����",		0,						MOTION_ACTION_ETC_01,		0.0f },
	{ "��������",	0,						MOTION_ACTION_ETC_02,		0.0f },
	{ "��������",	0,						MOTION_ACTION_ETC_03,		0.0f },
	{ "��������",	0,						MOTION_ACTION_ETC_04,		0.0f },
	{ "ơ",		0,						MOTION_ACTION_ETC_05,		0.0f },
	{ "��",		0,						MOTION_ACTION_ETC_06,		0.0f },
	 */
};

std::set<std::pair<DWORD, DWORD> > s_emotion_set;

ACMD(do_emotion_allow)
{
	if (!ch) return;//@Turkmmo62
	if (ch->GetArena())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("����忡�� ����Ͻ� �� �����ϴ�."));
		return;
	}

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
		return;

	DWORD	val = 0; str_to_number(val, arg1);
	s_emotion_set.insert(std::make_pair(ch->GetVID(), val));
}

#ifdef ENABLE_NEWSTUFF
#include "config.h"
#endif

bool CHARACTER_CanEmotion(CHARACTER& rch)
{
#ifdef ENABLE_NEWSTUFF
	if (g_bDisableEmotionMask)
		return true;
#endif

	if (marriage::WeddingManager::instance().IsWeddingMap(rch.GetMapIndex()))
		return true;

	if (rch.IsEquipUniqueItem(UNIQUE_ITEM_EMOTION_MASK))
		return true;

	if (rch.IsEquipUniqueItem(UNIQUE_ITEM_EMOTION_MASK2))
		return true;

	return false;
}

ACMD(do_emotion)
{
	int i;
	{
		if (ch->IsRiding())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���� ź ���¿��� ����ǥ���� �� �� �����ϴ�."));
			return;
		}
	}

	for (i = 0; *emotion_types[i].command != '\n'; ++i)
	{
		if (!strcmp(cmd_info[cmd].command, emotion_types[i].command))
			break;

		if (!strcmp(cmd_info[cmd].command, emotion_types[i].command_to_client))
			break;
	}

	if (*emotion_types[i].command == '\n')
	{
		sys_err("cannot find emotion");
		return;
	}

	if (!CHARACTER_CanEmotion(*ch))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("������ ������ ����ÿ��� �� �� �ֽ��ϴ�."));
		return;
	}

	if (IS_SET(emotion_types[i].flag, WOMAN_ONLY) && SEX_MALE == GET_SEX(ch))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڸ� �� �� �ֽ��ϴ�."));
		return;
	}

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	LPCHARACTER victim = NULL;

	if (*arg1)
		victim = ch->FindCharacterInView(arg1, IS_SET(emotion_types[i].flag, NEED_PC));

	if (IS_SET(emotion_types[i].flag, NEED_TARGET | NEED_PC))
	{
		if (!victim)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�׷� ����� �����ϴ�."));
			return;
		}
	}

	if (victim)
	{
		if (!victim->IsPC() || victim == ch)
			return;

		if (victim->IsRiding())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���� ź ���� ����ǥ���� �� �� �����ϴ�."));
			return;
		}

		long distance = DISTANCE_APPROX(ch->GetX() - victim->GetX(), ch->GetY() - victim->GetY());

		if (distance < 10)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�ʹ� ������ �ֽ��ϴ�."));
			return;
		}

		if (distance > 500)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�ʹ� �ָ� �ֽ��ϴ�"));
			return;
		}

		if (IS_SET(emotion_types[i].flag, OTHER_SEX_ONLY))
		{
			if (GET_SEX(ch) == GET_SEX(victim))
			{
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�̼������� �� �� �ֽ��ϴ�."));
				return;
			}
		}

		if (IS_SET(emotion_types[i].flag, NEED_PC))
		{
			if (s_emotion_set.find(std::make_pair(victim->GetVID(), ch->GetVID())) == s_emotion_set.end())
			{
				if (true == marriage::CManager::instance().IsMarried(ch->GetPlayerID()))
				{
					const marriage::TMarriage* marriageInfo = marriage::CManager::instance().Get(ch->GetPlayerID());

					const DWORD other = marriageInfo->GetOther(ch->GetPlayerID());

					if (0 == other || other != victim->GetPlayerID())
					{
						ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� �ൿ�� ��ȣ���� �Ͽ� ���� �մϴ�."));
						return;
					}
				}
				else
				{
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� �ൿ�� ��ȣ���� �Ͽ� ���� �մϴ�."));
					return;
				}
			}

			s_emotion_set.insert(std::make_pair(ch->GetVID(), victim->GetVID()));
		}
	}

	char chatbuf[256 + 1];
	int len = snprintf(chatbuf, sizeof(chatbuf), "%s %u %u",
		emotion_types[i].command_to_client,
		(DWORD)ch->GetVID(), victim ? (DWORD)victim->GetVID() : 0);

	if (len < 0 || len >= (int)sizeof(chatbuf))
		len = sizeof(chatbuf) - 1;

	++len;

	TPacketGCChat pack_chat;
	pack_chat.header = HEADER_GC_CHAT;
	pack_chat.size = sizeof(TPacketGCChat) + len;
	pack_chat.type = CHAT_TYPE_COMMAND;
	pack_chat.id = 0;
	TEMP_BUFFER buf;
	buf.write(&pack_chat, sizeof(TPacketGCChat));
	buf.write(chatbuf, len);

	ch->PacketAround(buf.read_peek(), buf.size());

	if (victim)
		sys_log(1, "ACTION: %s TO %s", emotion_types[i].command, victim->GetName());
	else
		sys_log(1, "ACTION: %s", emotion_types[i].command);
}
#ifndef __PRIV_MANAGER_H
#define __PRIV_MANAGER_H

/**
 * @version 05/06/08	Bang2ni - Guild privilege ���� �Լ� ���� �ð� �߰�
 * 			          RequestGiveGuildPriv, GiveGuildPriv �Լ� ������Ÿ�� ����
 * 			          m_aPrivGuild Ÿ�� ����
 * 			          ����ü SPrivGuildData, ��� �Լ� GetPrivByGuildEx �߰�
 */
class CPrivManager : public singleton<CPrivManager>
{
public:
	CPrivManager();

	void RequestGiveGuildPriv(DWORD guild_id, BYTE type, int value, time_t dur_time_sec);
	void RequestGiveEmpirePriv(BYTE empire, BYTE type, int value, time_t dur_time_sec);
	void RequestGiveCharacterPriv(DWORD pid, BYTE type, int value);

	void GiveGuildPriv(DWORD guild_id, BYTE type, int value, BYTE bLog, time_t end_time_sec);
	void GiveEmpirePriv(BYTE empire, BYTE type, int value, BYTE bLog, time_t end_time_sec);
	void GiveCharacterPriv(DWORD pid, BYTE type, int value, BYTE bLog);

	void RemoveGuildPriv(DWORD guild_id, BYTE type);
	void RemoveEmpirePriv(BYTE empire, BYTE type);
	void RemoveCharacterPriv(DWORD pid, BYTE type);

	int GetPriv(LPCHARACTER ch, BYTE type);
	int GetPrivByEmpire(BYTE bEmpire, BYTE type);
	int GetPrivByGuild(DWORD guild_id, BYTE type);
	int GetPrivByCharacter(DWORD pid, BYTE type);

public:
	struct SPrivEmpireData
	{
		int m_value;
		time_t m_end_time_sec;
	};

	SPrivEmpireData* GetPrivByEmpireEx(BYTE bEmpire, BYTE type);

	struct SPrivGuildData
	{
		int		value;
		time_t	end_time_sec;
	};

	/**
	 * @param [in]	dwGuildID ���� ����� ID
	 * @param [in]	byType ���ʽ� Ÿ��
	 * @return	��� ����� ��� ���ʽ� �������� ������, �ش��ϴ� ���ʽ� Ÿ�ٰ� ����� ID �� ���� ���ʽ� �����Ͱ� ���� ��� NULL
	 */
	const SPrivGuildData* GetPrivByGuildEx(DWORD dwGuildID, BYTE byType) const;

private:
	SPrivEmpireData m_aakPrivEmpireData[MAX_PRIV_NUM][EMPIRE_MAX_NUM];
	std::map<DWORD, SPrivGuildData> m_aPrivGuild[MAX_PRIV_NUM];
	std::map<DWORD, int> m_aPrivChar[MAX_PRIV_NUM];
};
#endif

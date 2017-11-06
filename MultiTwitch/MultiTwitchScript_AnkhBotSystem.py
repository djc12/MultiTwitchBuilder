#---------------------------------------
# Import Libraries
#---------------------------------------
import sys
import clr
import json
import logging
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import datetime


#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "MultiTwitchBuilder"
Website = "https://www.valhallasmostwanted.com"
Description = "!MT will post a multiwitch of all currently online Valhalla Streamers"
Creator = "Derek Cody (SkrubDaNub)"
Version = "1.0.0.0"


#---------------------------------------
# Set Variables
#---------------------------------------
m_Response = "https://beta.multitwitch.net/"
m_Command = "!mt"
m_CooldownSeconds = 10
m_CommandPermission = "everyone"
m_CommandInfo = ""
m_URL = "https://api.twitch.tv/helix/streams?community_id=5f34aa5c-1551-4480-bb0f-926ef093d4cf"
m_getUserUrl = "https://api.twitch.tv/helix/users?"
m_Headers = {'Client-ID' : 'jctfwago0490knwjg2kyrdqdq8e7wm' }
m_streamers = ["SkrubDaNub","Grey_Wolves_Gaming","Outlawviking","Undead_duende","StealingFirst","PlatinumTrophyWife"]
m_User_ids = []

def Init():
 return

#---------------------------------------
# [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):
    if data.IsChatMessage():
        if data.GetParam(0).lower() == m_Command and not \
            Parent.IsOnCooldown(ScriptName, m_Command) and \
                Parent.HasPermission(data.User, m_CommandPermission,
                                     m_CommandInfo):
                global m_Response
                global m_User_ids
                global m_getUserUrl
                data = Parent.GetRequest(m_URL, m_Headers)
                parsed_json = json.loads(data);
                parsed_json = json.loads(parsed_json['response'])
                for stream in parsed_json['data']:
                    Parent.Log(ScriptName,str(stream))
                    m_User_ids.append(stream['user_id'])
                for user in m_User_ids:
                    m_getUserUrl += "id=" + user
                    m_getUserUrl += "&"
                display_names = Parent.GetRequest(m_getUserUrl,m_Headers)
                parsed_names = json.loads(display_names)
                parsed_names = json.loads(parsed_names['response'])
                for username in parsed_names['data']:
                    m_Response += username['display_name'] +'/'
                Parent.SendTwitchMessage(m_Response)
                m_Response = "https://beta.multitwitch.net/";
                m_User_ids = []
                m_getUserUrl = "https://api.twitch.tv/helix/users"
    return
#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
 return

from typing import Literal
from .Updates import getUpdates
from .Methods import (
  getMe,
  sendMessage,
  approveChatJoinRequest,
  declineChatJoinRequest,
  deleteMessage
)
from .bot_command import BotCommands
from .events import EventWatcher


class Bot:
  def __init__(self):
    self.Updates = self._Updates()
    self.Methods = self._Methods()
  
  # Updates
  class _Updates:
    def __init__(self):
      pass
    
    # updates: getUpdates
    async def getUpdates(self, offset: None):
      """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects.
  
      Args:
          offset (int): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.
      """
      return await getUpdates().Initialize(offset)
    
  # Methods
  class _Methods:
    def __init__(self):
      pass
    
    # methods: getMe
    async def getMe(self):
      """Use this method to get information about the bot. Returns a User object on success."""
      return await getMe().Initialize()
    
    # methods: sendMessage
    async def sendMessage(self,
      chat_id: int | str,
      text: int | str,
      parse_mode: Literal["MarkdownV2", "HTML", "Markdown"] = "MarkdownV2",
      disable_notification: bool | None = None,
      protect_content: bool | None = None,
      reply_markup: str | None = None,
      reply_message: int | str | None = None,
    ):
      """Use this method to send text messages. On success, the sent Message is returned.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          text (str): Text of the message to be sent.
          parse_mode (str): Send MarkdownV2, HTML or Markdown style for parsing entities in the message text.
          disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
          protect_content (bool): Protects the contents of the sent message from forwarding and saving.
          reply_markup (str): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
          reply_message (int): If the message is a reply, ID of the original message.
      """
      return await sendMessage().Initialize(
        chat_id=chat_id,
        text=text,
        parse_mode=parse_mode,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_markup=reply_markup,
        reply_message=reply_message
      )
      
    # methods: approveChatJoinRequest
    async def approveChatJoinRequest(self,
      chat_id: int | str,
      user_id: int | str
    ):
      """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          user_id (int): Unique identifier of the target user.
      """
      return await approveChatJoinRequest().Initialize(
        chat_id,
        user_id
      )
    # methods: declineChatJoinRequest
    async def declineChatJoinRequest(self,
      chat_id: int | str,
      user_id: int | str
    ):
      """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          user_id (int): Unique identifier of the target user.
      """
      return await declineChatJoinRequest().Initialize(
        chat_id,
        user_id
      )
      
    # methods: deleteMessage
    async def deleteMessage(self,
      chat_id: int | str,
      message_id: int | str
    ):
      """Use this method to delete a message, including service messages, with the following limitations:
          - A message can only be deleted if it was sent less than 48 hours ago.
          - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
          - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
          - Bots can delete outgoing messages in private chats, groups, and supergroups.
          - Bots can delete incoming messages in private chats.
          - Bots granted can_post_messages permissions can delete outgoing messages in channels.
          - If the bot is an administrator of a group, it can delete any message there.
          - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
          Returns True on success.
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          message_id (int): Identifier of the message to delete.
      """
      return await deleteMessage().Initialize(
        chat_id,
        message_id
      )

  # Bot Commands
  def command(self, command: str):
    return BotCommands(command)
  
  # Bot  Event
  def EventWatchers(self, event_list: Literal["UserRequest"]):
    return EventWatcher(event_list)
bot = Bot()
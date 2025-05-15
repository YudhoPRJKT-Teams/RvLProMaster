from typing import Literal
from .Updates import getUpdates
from .Methods import (
  getMe,
  sendMessage,
  approveChatJoinRequest,
  declineChatJoinRequest,
  deleteMessage,
  sendPhoto,
  logOut,
  sendVideo,
  close,
  forwardMessage,
  sendDocument,
  copyMessage
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
      
    # methods: sendPhoto
    async def sendPhoto(self,
      chat_id: int | str,
      photo: str,
      caption: str | None = None,
      parse_mode: Literal["MarkdownV2", "HTML", "Markdown"] = "MarkdownV2",
      has_spoiler: bool = False,
      disable_notification: bool = False,
      protect_content: bool = False,
      reply_markup: str | None = None,
      reply_message: int | str | None = None
    ):
      """Use this method to send photos. On success, the sent Message is returned.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          photo (str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data.
          caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing.
          parse_mode (str): Send MarkdownV2, HTML or Markdown style for parsing entities in the message text.
          has_spoiler (bool): Disables link previews for links in this message.
          disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
          protect_content (bool): Protects the contents of the sent message from forwarding and saving.
          reply_markup (str): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
          reply_message (int): If the message is a reply, ID of the original message.
      """
      return await sendPhoto().Initialize(
        chat_id,
        photo,
        caption,
        parse_mode,
        has_spoiler,
        disable_notification,
        protect_content,
        reply_markup,
        reply_message
      )
      
    # methods: logOut
    async def logOut(self):
      """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it in local mode. The method will return True on success.
  
      Note:
          You must log out the bot before running it in local mode.
      """
      return await logOut().Initialize()
    # methods: sendVideo
    async def sendVideo(self,
      chat_id: int | str,
      video: str,
      caption: str | None = None,
      parse_mode: Literal["MarkdownV2", "HTML", "Markdown"] = "MarkdownV2",
      has_spoiler: bool = False,
      disable_notification: bool = False,
      protect_content: bool = False,
      reply_markup: str | None = None,
      reply_message: int | str | None = None,
    ):
      """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

      Args:
          chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
          video (str): Video from url or path/to/video.mp4 to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
          caption (str | None, optional): _description_. Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
          parse_mode (Literal[&quot;MarkdownV2&quot;, &quot;HTML&quot;, &quot;Markdown&quot;], optional): Mode for parsing entities in the video caption. See formatting options for more details. Defaults to "MarkdownV2".
          has_spoiler (bool): Disables link previews for links in this message.
          disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
          protect_content (bool): Protects the contents of the sent message from forwarding and saving.
          reply_markup (str): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
          reply_message (int): If the message is a reply, ID of the original message.

      Returns:
          _type_: _description_
      """
      return await sendVideo().Initialize(
        chat_id,
        video,
        caption,
        parse_mode,
        has_spoiler,
        disable_notification,
        protect_content,
        reply_markup,
        reply_message
      )
    
    # methods: close
    async def close(self):
      """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
      return await close().Initialize()
    # methods: forwardMessage
    async def forwardMessage(self,
      chat_id: int | str,
      from_chat_id: int | str,
      message_id: int | str,
      protect_content: bool = False,
      disable_notification: bool = False
    ):
      """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent Message is returned.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          from_chat_id (int): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).
          message_id (int): Identifier of the original message.
          protect_content (bool): Protects the contents of the sent message from forwarding and saving.
          disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
      """
      return await forwardMessage().Initialize(
        chat_id,
        from_chat_id,
        message_id,
        protect_content,
        disable_notification
      )
    # methods: sendDocument
    async def sendDocument(self,
      chat_id: int | str,
      document: str,
      caption: str | None = None,
      parse_mode: Literal["MarkdownV2", "HTML", "Markdown"] = "MarkdownV2",
      disable_notification: bool = False,
      protect_content: bool = False,
      reply_markup: str | None = None,
      reply_message: int | str | None = None,
    ):
      """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

      Args:
          chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
          document (str): document from url or path/to/file to send	File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »
          caption (str | None, optional): _description_. Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
          parse_mode (Literal[&quot;MarkdownV2&quot;, &quot;HTML&quot;, &quot;Markdown&quot;], optional): Mode for parsing entities in the video caption. See formatting options for more details. Defaults to "MarkdownV2".
          disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
          protect_content (bool): Protects the contents of the sent message from forwarding and saving.
          reply_markup (str): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
          reply_message (int): If the message is a reply, ID of the original message.
      """
      return await sendDocument().Initialize(
        chat_id,
        document,
        caption,
        parse_mode,
        disable_notification,
        protect_content,
        reply_markup,
        reply_message
      )
    # methods: copyMessage
    async def copyMessage(self,
      chat_id: int | str,
      from_chat_id: int | str,
      message_id: int | str,
      caption: str | None = None,
      parse_mode: str | None = None,
      reply_markup: str | None = None,
      reply_message: int | str | None = None
    ):
      """Use this method to copy messages of any kind. Service messages and messages with protected content can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
  
      Args:
          chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
          from_chat_id (int): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).
          message_id (int): Identifier of the original message.
          caption (str): New caption for media, 0-1024 characters after entities parsing.
          parse_mode (str): Send MarkdownV2, HTML or Markdown style for parsing entities in the message text.
      """
      return await copyMessage().Initialize(
        chat_id,
        from_chat_id,
        message_id,
        caption,
        parse_mode
      )
  # Bot Commands
  def command(self, command: str):
    return BotCommands(command)
  
  # Bot  Event
  def EventWatchers(self, event_list: Literal["UserRequest", "UserJoined", "UserLeft"]):
    return EventWatcher(event_list)
bot = Bot()
from telethon import TelegramClient, events, sync
import pickle

# User(id=1979909536, is_self=True, contact=False, mutual_contact=False, deleted=False, bot=False, bot_chat_history=False, bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False, support=False, scam=False, apply_min_photo=True, fake=False, access_hash=2118236008595820803, first_name='vei', last_name='tsi', username='vetsinen', phone='380631741784', photo=UserProfilePhoto(photo_id=5188527073361246249, dc_id=2, has_video=False, stripped_thumb=b'\x01\x08\x08\x8d/\x01\x93\x9cu\xe2\x8a(\xa5a\x9f'), status=UserStatusOffline(was_online=datetime.datetime(2021, 11, 9, 9, 40, 13, tzinfo=datetime.timezone.utc)), bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None, lang_code=None)

async def main():
    # print(client.get_me().stringify())
    # entity = await client.get_entity('helvetian')
    # print(entity)
    # await client.send_message('helvetian', 'Hello, not myself!')

    chatid = (await client.get_peer_id('CK_talk'))
    users = []
    async for user in client.iter_participants(chatid):
        users.append({"id":user.id,"first_name": user.first_name,  "username": user.username, "phone": user.phone})

    print(users)
    print(len(users))
    with open('CK_talk-users.pickle', 'wb') as f:
        pickle.dump(users, f)

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 9777306
api_hash = 'c894e7a0d82773cae554a85e32a55620'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

with client:
    client.loop.run_until_complete(main())








# messages = client.get_messages('vetsinen')

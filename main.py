import aiohttp, asyncio
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.icq.net/bot/v1/messages/sendText?chatId=752738404&text=%D1%85%D1%83%D0%B9&token=001.0756150291.3568131232:756656077') as r$
            print(resp.status)
            print(await resp.text())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

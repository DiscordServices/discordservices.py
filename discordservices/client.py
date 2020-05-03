import asyncio
import aiohttp

from .errors import *

class DSClient:
	def __init__(self, bot, token, autopost=False):
		self.token = token
		self.bot = bot
		self.bot_id = None
		self.loop = asyncio.get_event_loop()
		self.session = aiohttp.ClientSession()
		self.autopost = autopost
		
		if self.autopost:
			self.loop.create_task(self._auto_post())
			
	async def _ensure_bot(self):
		await self.bot.wait_until_ready()
		if self.bot_id is None:
			self.bot_id = self.bot.user.id
			
	async def _auto_post(self):
		await self._ensure_bot()
		await self.post_count()
		await asyncio.sleep(900)
		
	async def post_count(self, shards: int=None):
		base = "https://api.discordservices.net/"
		if not self.token:
			raise TokenNotProvided("No Token Given")
		else:
			if shards:
				payload = {"servers": len(self.bot.guilds), "shards": shards}
			else:
				payload = {"servers": len(self.bot.guilds)}
				
			async with self.session.request('POST', base + f"bot/{self.bot_id}/stats", headers={"Authorization": self.token, "Content-Type": "application/json"}, json=payload) as resp:
				data = await resp.text()
				
				if resp.status == 200:
					return data
					
				if resp.status == 400:
					raise BadRequest(resp, data)
				elif resp.status == 401:
					raise Unauthotized(resp, data)
				elif resp.status == 404:
					raise NotFound(resp, data)
					
	async def post_news(self, title, *, content):
		base = "https://api.discordservices.net/"
		
		if not self.token:
			raise TokenNotProvided("No token given")
		else:
			if not title:
				print("title is required argument")
			elif not content:
				print("content is a required argument")
			else:
				payload = {"title": title, "content": content}
				async with self.session.request('POST', base + f'bot/{self.bot_id}/news', headers={"Authorization": self.token, "Content-Type": "application/json"}, json=payload) as resp:
					if resp.status == 200:
						return resp
						
					if resp.status == 400:
						raise BadRequest(resp, data)
					elif resp.status == 401:
						raise Unauthotized(resp, data)
					elif resp.status == 404:
						raise NotFound(resp, data)
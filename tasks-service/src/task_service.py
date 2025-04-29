import aiohttp
from aiohttp import web

async def create_task(request):
	user_id = request.match_info.get('user_id')
	task_data = await request.json()
	
	async with aiohttp.ClientSession() as session:
		url = f'http://user_service:5002/user/{user_id}'
		async with session.get(url) as resp:
			user_info = await resp.json()
			print("User info:", user_info)
	# Здесь можно использовать информацию о пользователе для создания задачи
	return web.json_response({'message': 'Task created successfully' })

app = web.Application()
app.router.add_post('/task/{user_id}', create_task)
web.run_app(app, port=5001, host='0.0.0.0')

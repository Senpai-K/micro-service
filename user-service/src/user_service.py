from aiohttp import web

async def handle_user(request):
	user_id = request.match_info.get('user_id')
	user_info = {'user_id': user_id, 'user_name': 'test_user'}
	return web.json_response(user_info)

app = web.Application()
app.router.add_get('/user/{user_id}', handle_user)
web.run_app(app, port=5002, host='0.0.0.0')

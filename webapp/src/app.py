from aiohttp import web
import aiohttp_jinja2
import jinja2

# Инициализируем приложение aiohttp
app = web.Application()
# Настраиваем Jinja2 для использования шаблонов из папки Templates
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('src/templates'))
# URL адрес сервиса "user"
USER_SERVICE_URL = 'http://user_service:5002'

# Обработчик главной страницы
@aiohttp_jinja2.template('index.html')
async def handle_index(request):
    return {}

# Обработчик страницы задач
@aiohttp_jinja2.template('tasks.html')
async def handle_tasks(request):
    if request.method == 'GET':
        # Обработка GET запроса для страницы задач
        return {}

# Обработчик страницы регистрации
@aiohttp_jinja2.template('register.html')
async def handle_register(request):
    if request.method == 'GET':
        # Обработка GET запроса для страницы регистрации
        return {}

# Обработчик создания задачи
async def create_task(request):
    user_id = request.match_info.get('user_id')
    task_data = await request.json()

    async with aiohttp.ClientSession() as session:
        url = f'http://user_service:5002/user/{user_id}'
        async with session.get(url) as resp:
            user_info = await resp.json()
            print("User info:", user_info)
    # Здесь можно использовать информацию о пользователе для создания задачи
    return web.json_response({'message': 'Task created successfully'})

# Обработчик пользователя
async def handle_user(request):
    user_id = request.match_info.get('user_id')
    user_info = {'user_id': user_id, 'username': 'test_user'}
    return web.json_response(user_info)

# Регистрируем обработчики для соответствующих страниц
app.router.add_get('/', handle_index)
app.router.add_get('/tasks', handle_tasks)
app.router.add_get('/register', handle_register)
app.router.add_post('/task/{user_id}', create_task)
app.router.add_get('/user/{user_id}', handle_user)

# Запускаем веб-сервер
if __name__ == "__main__":
    web.run_app(app, port=5000, host='0.0.0.0')

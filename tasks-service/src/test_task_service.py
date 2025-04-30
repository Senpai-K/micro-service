import pytest
import aiohttp
from aiohttp import web
from unittest.mock import patch
from task_service import create_task

# Фикстура для создания тестового приложения
@pytest.fixture
async def test_app():
	app = web.Application()
	app.router.add_post('/task/{user_id}', create_task)
	return app

# Фикстура для создания тестового клиента
@pytest.fixture
async def cli(test_app, aiohttp_client):
	return await aiohttp_client(test_app)

@pytest.mark.asyncio
async def test_create_task(cli):
	# Мокаем запрос к user_service
	with patch('aiohttp.ClientSession.get') as mock_get:
		mock_response = type('MockResponse', (), {
			'json': lambda self: {'user_id': '1', 'username': 'test_user'},
			'__aenter__': lambda self: self,
			'__aexit__': lambda self, exc_type, exc, tb: None,
			'__await__': lambda self: self.__aenter__().__await__()
		})()
		mock_get.return_value = mock_response

		# Делаем тестовый POST-запрос
		response = await cli.post('/task/1', json={'description': 'Test task'})

		# Проверяем, что ответ корректный
		assert response.status == 200
		data = await response.json()
		assert data == {'message': 'Task created successfully'}

		# Проверяем, что запрос к user_service был выполнен
		mock_get.assert_called_once()
		print("Unit test 'test_create_task' passed successfully")

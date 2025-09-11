## Запуск тестов

Для запуска тестов и генерации результатов Allure выполните:

pytest tests/ --alluredir=./allure-results -v


- Флаг `--alluredir` указывает, где сохранить результаты тестов Allure.
- Результаты сохраняются в папке `allure-results`.

## Просмотр отчета Allure

Для создания и просмотра отчета Allure:
1. Сгенерируйте отчет из результатов:
   
   allure generate ./allure-results -o ./allure-report --clean
   
   - Флаг `--clean` удаляет существующий отчет в папке `allure-report`.
2. Откройте отчет:
   
   allure open ./allure-report
   
   - Команда запускает локальный веб-сервер и открывает отчет в браузере по умолчанию.


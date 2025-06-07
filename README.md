Скачать архив с кодом, распаковать, в папке с кодом запустить powershell (на пустом месте правой кнопкой мыши + Shift).
Тестовые данные можно скачать по адресу: https://drive.google.com/file/d/1qJduj_-_nWCNhfTdICReepAbUs8OHC_Y/view

Выполнить команды:
1. `python -m venv ./venv` (в PowerShell в папке с проектом)
2. `.\venv\Scripts\Activate.ps1` (если скрипт не сработает "выполнение сценариев отключено в этой системе",
открыть PowerSell от администратора и выполнить команду `Set-ExecutionPolicy RemoteSigned` и подтвердить `A`)
Должны появиться в начале строки круглые скобки и `venv` - можно продолжать.
3. `pip install -r .\requirements.txt`
4. `uvicorn app:app --reload --port 8000` - должно появиться `Application startup complete` (запуск сервера в первом окне PowerShell)
5. Открыть второй терминал PowerShell и там запускается команда п.7.
6. Поместить тестовые данные в файле csv в папку с программой.
7. `curl.exe -X POST "http://localhost:8000/predict" \  
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@heart_test.csv"`

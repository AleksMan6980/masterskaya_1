Скачать архив с кодом, распаковать, в папке с кодом запустить powershell (на пустом месте правой кновкой мыши + Shift).
Выполнить команды:
1. `python -m venv ./venv`
2. `.\venv\Scripts\Activate.ps1` (если скрипт не сработает "выполнение сценариев отключено в этой системе",
открыть PowerSell от администратора и выполнить команду `Set-ExecutionPolicy RemoteSigned` и подтвердить `A`)
Должны появиться в начале строки круглые скобки и `venv` - можно продолжать.
3. `pip install -r .\requirements.txt`
4. `uvicorn app:app --reload --port 8000` - должно появиться `Application startup complete`
5. Поместить csv в папку с программой.
6. `curl.exe -X POST "http://localhost:8000/predict" \  
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@heart_test.csv"`

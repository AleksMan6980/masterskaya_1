Чтобы запустить приложение нужны модули fastapi, python-multipart, uvicorn.

Запускается командой uvicorn app:app --reload --port 8000 в папке с app.py

Взаимодействие осуществляется командой

curl -X POST "http://localhost:8000/predict" \  
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@/path/to/csv/heart_test.csv"
если, например, через curl

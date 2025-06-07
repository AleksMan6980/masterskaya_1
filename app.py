from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
import io

app = FastAPI()

# получаем из ноутбука с моделью ()
# import joblib
# joblib.dump(model.best_estimator_, './final_model.pkl')
model = joblib.load('final_model.pkl')

# конечная точка маршрута запроса curl (программы, формирующей запрос)
@app.post("/predict")

# функция, в которую передается запрос
async def predict(file: UploadFile = File(...)): # запрос содержит файл с данными
    content = await file.read() # чтение байт строки
    df = pd.read_csv(io.StringIO(content.decode('utf-8'))) # создание датасета с декодирование строки в csv файл из потока декодированных данных
    df = df.drop(['Unnamed: 0', 'Family History'], axis = 1)
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.replace('(', '')
    df.columns = df.columns.str.replace(')', '')
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('-', '_')
    df.columns = df.columns.str.replace('_binary', '')

    proba = model.predict_proba(df.drop(columns=['id']))[:,1]
    proba = df[['id']].join(pd.DataFrame(proba))
    proba.columns = ['id', 'pred_proba']
    proba['prediction'] = proba['pred_proba'].apply(lambda x: .0 if x>=0.42 else 1.)

    return {
        "probabilities": proba.values.tolist()
    }

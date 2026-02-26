from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import models

feedbacks=[]
validated_feedbacks=[]

app=FastAPI()

#№1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

#№1.2
@app.get("/page",response_class=HTMLResponse)
async def get_page():
    path= r"/index.html"  #я не знаю правильно так или нет, но у меня по другому не рабоает
    return FileResponse(path, media_type="text/html")

#№1.3
@app.post("/calculate")
async def calculate(num1:float,num2:float):
    return {"result":num1+num2}

#№1.4
users= models.User(id=1, name='Маслов Алексей')
@app.get("/users")
async def get_users():
    return users

#№1.5
@app.post("/user")
async def get_user(user: models.UserAge):
    user_data=user.dict()
    user_data["is_adult"]=user.age>=18
    return user_data

#№2.1
@app.post("/feedback")
async def give_feedback(feedback: models.Feedback):
    feedback_data=feedback.dict()
    feedbacks.append(feedback_data)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

#№2.2
@app.post("/feedback/v2")
async def create_feedback_validated(feedback: models.FeedbackValidated):
    validated_feedbacks.append(feedback.model_dump())
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён.",
        "feedback": feedback.model_dump()
    }
@app.get("/feedbacks")
async def get_all_feedbacks():
    return {
        "feedbacks": feedbacks,
    }
@app.get("/feedbacks/v2")
async def get_validated_feedbacks():
    return {
        "feedbacks": validated_feedbacks,
    }
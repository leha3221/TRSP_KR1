from pydantic import*

class User(BaseModel):
    id: int
    name: str

class UserAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message:str

class FeedbackValidated(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_bad_words(cls, v: str) -> str:
        bad_words = ['Александр', 'Серегин', 'Евгеньевич']
        message_lower = v.lower()
        for word in bad_words:
            if word in message_lower:
                raise ValueError(f'Использование недопустимых слов: "{word}"')
        return v




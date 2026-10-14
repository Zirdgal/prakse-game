from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")      # GET uz /hello
def hello():
    return {"message": "Sveiki!"}


# palaiž terminālī (projekta mapē):
# uvicorn api.main:app --reload

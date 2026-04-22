from fastapi import Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import	FastAPI
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


		@app.get("/", response_class=HTMLResponse)
		def read_index(request: Request, db: Session = Depends(get_db)):
			dogs = crud.get_dogs(db)
		return templatesResponse("index.html", {"request": request, "dogs": dogs})

		@app.post("/dogs")
		def create_dog(
			name: str = Form(...),
			age: int = Form(...),
			breed: str = Form(...),
			gender: str = Form(...),
			size: str = Form(...),
			vaccinated: bool = Form(False),
			adopted: bool = Form(False),
			notes: str = Form(""),
			db: Session = Depends(get_db)

		):

			dog = schemas.DogCreate(
			name = name,
			age = age,
			breed = breed,
			gender = gender,
			size = size,
			vaccinated = vaccinated,
			adopted = adopted,
			notes = notes,

		)
		crud.create_dog(db, dog)
		return RedirectResponse(url="/", status_code=303)

		@app.post("dogs/delete/{dog_id}")
		def delete_dog(dog_id: int, db: Session = Depends(get_db)):
			deleted = crud.delete_dog(db, dog_id)
		if not deleted:
			raise HTTPException(status_code=404, detail="Dog not found")
			return RedirectResponse(url="/", status_code=303)
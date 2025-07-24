from  fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import session_local, engine, Base
from models import User
from auth_utils import create_access_token, verify_password, hash_password, decode_access_token
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

Base.metadata.create_all(bind=engine)
app = FastAPI()
security = HTTPBearer()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "id": new_user.id, "message": "User created successfully"}

@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user or not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # sub is used to encrypt the data inside of the arguments
    access_token = create_access_token(data={"sub": existing_user.username})
    return {"access_token": access_token, "token_type": "bearer", "username": existing_user}

@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials or not credentials.credentials:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Missing credentials")
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or expired token")
    return {"message": "Protected route accessed", "user": payload["sub"]}

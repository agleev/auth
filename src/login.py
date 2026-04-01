from fastapi import FastAPI, Response, Request
import string
import random
from typing import Optional

app = FastAPI()


async def auth_session_validate(session_id: str):
  pass

async def check_user_app_connection(callback_url: str, auth_session_id: str):
  pass

async def auth_user_login(
  login: str,
  password: str
):
  pass

@app.get("/login")
async def check_login_session(
  request: Request,
  response: Response,
  auth_session_id: Optional[str] = None,
  callback_url: str = None
):
  
  session_valid = await auth_session_validate(auth_session_id)
  if not session_valid:
    response.delete_cookie('auth_session_id')
    return {
      'status_code': 404, 
      'message': 'Unauthorized'
    }
  
  conn_valid = await check_user_app_connection(callback_url, auth_session_id)
  if not conn_valid:
    response.set_cookie(key='auth_session_id', value=auth_session_id)
    return {
      'status_code': 403,
      'message': 'Forbidden'
      }
  session_token = geterate_token()

def geterate_token(length=256):
  characters = string.ascii_letters + string.digits
  random_string = ''.join(random.choice(characters) for _ in range(length))
  return random_string
  

@app.post("/login")
async def authenticate_user(
  # request: Request,
  response: Response,
  login: str,
  password: str,
  auth_session_id: str,
  callback_url: str):
  
  auth_valid = auth_user_login(login, password)
  if not auth_valid:
    response.delete_cookie("auth_session_id")
    return {
      'status_code': 401, 
      'message': 'Unauthorized'
    }
    
  conn_valid = await check_user_app_connection(callback_url, auth_session_id)
  if not conn_valid:
    response.set_cookie(key='auth_session_id', value=auth_session_id)
    return {
      'status_code': 403,
      'message': 'Forbidden'
      }
    

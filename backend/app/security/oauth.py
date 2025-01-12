from fastapi.security.oauth2 import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")


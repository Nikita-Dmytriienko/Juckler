
from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db



app = FastAPI(title="Juckler - Personal Finance Tracker")




# GET
@app.get("/")
def root():
    return {"message": "First start"}

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute("SELECT 1")
        return {"status": "ok", "detail": "Service is healthy"}
    except Exception as e:
        return {"status": "error", "database": "disconnected", "detail": str(e)}



# POST
# @app.post()



# PUT
# @app.put()



# DELETE
# @app.delete()
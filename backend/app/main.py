from fastapi import FastAPI




app = FastAPI(title="Juckler - Personal Finance Tracker")




# GET
@app.get("/")
def root():
    return {"message": "First start"}

@app.get("/health")
def health():
    return {"status": "ok", "detail": "Service is healthy"}



# POST
# @app.post()



# PUT
# @app.put()



# DELETE
# @app.delete()
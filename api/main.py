from fastapi import HTTPException
import traceback, sys

@app.post("/recommend")
def recommend(body: dict):
    try:
        run_id = trigger_dag(body)
        data   = wait_xcom(run_id)
        return {"recommendations": data}
    except Exception as e:
        traceback.print_exc(file=sys.stderr)   # <-- fuerza la traza
        raise HTTPException(500, f"Error interno: {e}")

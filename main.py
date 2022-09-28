from fastapi import FastAPI
from pydantic import BaseModel

class TheStudent(BaseModel):
    name: str

data_mahasiswa = {
    18220999: {
        "Nama" : "NIM"
    }
}

app = FastAPI()
@app.get("/mahasiswa/{nim}")
def get_mahasiswa(nim: int):
    if nim in data_mahasiswa:
        return data_mahasiswa[nim]
    else:
        return {"Mahasiswa tidak ditemukan"}

@app.post("/mahasiswa")
def post_mahasiswa(nim: int, item: TheStudent):
    if nim in data_mahasiswa:
        return {"Error: Mahasiswa sudah terdaftar"}

    data_mahasiswa[nim] = {"nama": item.name}
    return data_mahasiswa[nim]
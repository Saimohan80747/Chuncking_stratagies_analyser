
class ChunkRequest(BaseModel):
    text: str
    strategy: str
    chunk_size: int = 100
    overlap_size: int = 20

class TokenRequest(BaseModel):
    text: str

class PipeLine:
  def _init_(self,steps=[]):
    self.steps=steps

  def run(data):
    for step in self.steps:
        data=step(data)
    return data

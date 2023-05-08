import uvicorn
from fastapi import FastAPI, Request
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

model = "bigcode/santacoder"
device = "cpu"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model, trust_remote_code=True).to(device)

@app.post("/")
async def predict(request: Request):
    return generateCode(await request.json())

def generateCode(request):
    print(request)
    input = request['inputs']
    args = request['parameters']
    if "stop" in args:
        del(args['stop'])
    inputs = tokenizer.encode(input, return_tensors="pt").to(device)
    outputs = model.generate(inputs, **args)
    decoded_outputs = tokenizer.decode(outputs[0])
    print(decoded_outputs)
    return {"generated_text": decoded_outputs}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

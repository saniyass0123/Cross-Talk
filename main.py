
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# app = FastAPI()

# # Load pre-trained model and tokenizer
# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
# model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

# class TranslationRequest(BaseModel):
#     text: str

# @app.post("/translate/")
# async def translate(request: TranslationRequest):
#     try:
#         # Tokenize input text
#         inputs = tokenizer(request.text, return_tensors="pt")

#         # Generate the translation using the model
#         translated_outputs = model.generate(**inputs)

#         # Decode the translation
#         translated_text = tokenizer.decode(translated_outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
        
#         return {"translated_text": translated_text}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

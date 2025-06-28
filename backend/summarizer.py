from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from functools import lru_cache

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

@lru_cache(maxsize=1)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return tokenizer, model

def generate_summary_with_llama(claim_text, claimant_name, policy_number, date_of_incident, claim_amount, claim_reason):
    """
    Generate a formal, paragraph-style summary of the insurance claim using TinyLlama.
    Avoid field name repetition or bullet points.
    """
    prompt = f"""
You are a professional insurance assistant AI. Given the claim information below, write a human-friendly summary in one formal paragraph. Do not repeat field names. Do not use bullet points. Use proper grammar.

Details:
Claimant Name: {claimant_name}
Policy Number: {policy_number}
Date of Incident: {date_of_incident}
Claim Amount: ₹{claim_amount}
Claim Reason: {claim_reason}

Summary:
"""
    tokenizer, model = load_model()
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=250,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "Summary:" in generated_text:
        return generated_text.split("Summary:")[-1].strip()

    return generated_text.strip()

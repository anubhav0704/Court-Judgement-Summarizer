import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import preprocessing

class LegalSummarizer:
    def __init__(self, model_name="sshleifer/distilbart-cnn-12-6"):
        self.device = "cpu"  # Streamlit Cloud = CPU only
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def summarize(self, text: str, min_length=120, max_length=250) -> str:
        text = preprocessing.clean_text(text)

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(self.device)

        summary_ids = self.model.generate(
            inputs["input_ids"],
            num_beams=4,
            min_length=min_length,
            max_length=max_length,
            no_repeat_ngram_size=3
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

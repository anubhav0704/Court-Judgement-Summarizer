Novelty and Contributions
1. Integration of Long-Range Context (LED Architecture)
Traditional Transformer models (like BERT or BART) are limited by a "Self-Attention" bottleneck, restricting them to ~1,024 tokens.

Novelty: This project implements the Longformer Encoder-Decoder (LED), which utilizes a specialized Global-Local Attention mechanism.

Contribution: By expanding the input window to 16,384 tokens, the system can process an entire Indian High Court or Supreme Court judgement in a single pass, ensuring that critical final decisions located at the end of long documents are not truncated or lost.

2. Abstractive Synthesis of Legal Pillars
Most legal tools are "Extractive," merely highlighting existing sentences which can lead to fragmented results.

Novelty: The project employs Abstractive Summarization, which mimics human cognitive behavior by paraphrasing and synthesizing new sentences.

Contribution: The model is designed to intelligently extract and condense the four essential pillars of a judgement: Facts, Legal Issues, Judicial Reasoning, and the Final Decision, making complex law accessible to non-experts.

3. Domain-Specific Indian Legal Preprocessing
Generic text cleaners fail to handle the unique formatting and archaic abbreviations prevalent in the Indian Judiciary.

Novelty: A custom preprocessing.py module was developed to handle Citation Normalization (e.g., AIR, SC, SCC) and noisy text artifacts.

Contribution: This ensures the model receives "clean" semantic data, reducing hallucination risks and improving the ROUGE score (accuracy) of the generated summaries.

4. Real-Time Deployment Pipeline
High-end legal NLP research often lacks a practical user interface for practitioners.

Novelty: The project features an end-to-end integration of a heavy Transformer model with a Streamlit web interface hosted via a cloud-based GPU tunnel.

Contribution: It provides a no-code solution for legal professionals, allowing them to upload raw documents and receive professional summaries in under two minutes, bridging the gap between academic AI and industrial application.

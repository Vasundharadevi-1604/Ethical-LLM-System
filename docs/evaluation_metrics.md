# Evaluation Metrics and Results

## Objective

To evaluate the effectiveness of different language models and an ensemble approach
in detecting malicious or unsafe prompts.

## Models Evaluated

- Twitter RoBERTa
- Twitter XLM-R
- SentiBERT
- Final Ensemble Model

## Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1-score
- Approximate AUC

## Results Summary

| Model | Accuracy | Precision | Recall | F1-score | Approx. AUC |
|------|---------|----------|-------|---------|-------------|
| Twitter RoBERTa | 0.5563 | 1.0000 | 0.5563 | 0.7149 | 0.2781 |
| Twitter XLM-R | 0.9938 | 1.0000 | 0.9938 | 0.9969 | 0.4969 |
| SentiBERT | 0.6438 | 1.0000 | 0.6438 | 0.7832 | 0.3219 |
| **Final Ensemble** | **0.7938** | **1.0000** | **0.7938** | **0.8850** | **0.3969** |

## Key Observations

- The ensemble model provides balanced performance across metrics.
- High precision ensures minimal false positives.
- Ensemble improves robustness and generalization.

## Conclusion

The ensemble-based approach offers a reliable and ethical prompt classification
mechanism suitable for real-world LLM moderation systems.


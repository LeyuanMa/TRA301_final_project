Directory Guide
- code
    - clean_data.py:
        code for removing excess characters in the results of the literal and fluent translations
    - gpt_translation.ipynb:
        code for translating tweets using the GPT-4o api and for finetuning the English RoBERTa model on the translated data

- results
    - gpt_4o_results:
        results of the fine-tuned English RoBERTa model on gpt-4o translated tweets (performance metrics and confusion matrices)
    - xlm_predictions:
        results of the multilingual XLM-RoBERTa model on untranslated tweets (predicted labels and confidence scores)

- translations
    - gpt_4o_translations:
        translations of tweets obtained using the GPT-4o api
    - literal_and_fluent_translations:
        literal and fluent translations of tweets obtained using the Marian/Helsinki translation model
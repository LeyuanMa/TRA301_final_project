# Directory guide

## code
- clean_data.py  
  code for removing excess characters in the results of the literal and fluent translations

- gpt_translation.ipynb  
  code for translating tweets using the GPT-4o api and for finetuning the English RoBERTa model on the translated data

- finetuning_literal_fluent_translations/  
  directory with code for finetuning English RoBERTa model on literal/fluent translated tweets

- literal_and_fluent_translations.ipynb  
  code for obtaining literal and fluent translation of tweets

## results
- gpt_4o_results/  
  results of the fine-tuned English RoBERTa model on gpt-4o translated tweets (performance metrics and confusion matrices)

- xlm_predictions/  
  results of the multilingual XLM-RoBERTa model on untranslated tweets (predicted labels and confidence scores)

- finetuning_literal_fluent_results/  
  directory with detailed metrics and confusion matrices for results of finetuning English RoBERTa model on literal/fluent translated tweets:

## translations
- gpt_4o_translations/  
  translations of tweets obtained using the GPT-4o api

- literal_and_fluent_translations/  
  literal and fluent translations of tweets obtained using the Marian/Helsinki translation model

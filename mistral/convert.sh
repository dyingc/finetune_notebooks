cat harmful-examples-choosing.jsonl | jq -c '. | {"input": .messages | map(select(.role=="user"))[].content, "output": .messages | map(select(.role=="assistant"))[].content}' > harmful-examples-mistral.jsonl

python prepare_train_and_eval_data.py

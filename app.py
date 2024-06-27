from transformers import pipeline
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

sentences = input()

model_outputs = classifier([sentences])[0]
print(model_outputs)

top_5 = sorted(model_outputs, key=lambda x: x['score'], reverse=True)[:5]
top_5_labels = [item['label'] for item in top_5]
print(top_5_labels)
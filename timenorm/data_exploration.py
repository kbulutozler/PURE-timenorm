from shared.data_structures import Dataset
from entity.utils import convert_dataset_to_samples
from shared.const import task_ner_labels, get_labelmap
from relation.utils import generate_relation_data, decode_sample_id
import os

data_path = "/xdisk/bethard/kbozler/timenorm/PURE-timenorm-datasets/scierc_data/processed_data/json/"
train_data_path = os.path.join(data_path, 'train.json')
train_data = Dataset(train_data_path)
max_span_length=8
context_window=0
ner_label2id, ner_id2label = get_labelmap(task_ner_labels['scierc'])
print(ner_label2id)
train_samples, train_ner = convert_dataset_to_samples(train_data, max_span_length, ner_label2id=ner_label2id, context_window=context_window)
print(train_samples[1])
train_dataset, train_examples, train_nrel = generate_relation_data(train_data_path, use_gold=True, context_window=context_window)

for train_example in train_examples:
    if train_example['relation'] != 'no_relation':
        print(train_example)

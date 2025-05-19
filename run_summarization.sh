git clone https://github.com/huggingface/transformers.git
cd transformers

conda create -n transformers python=3.10 -y
conda activate transformers
pip install -e .
pip install torch torchvision torchaudio
pip install datasets evaluate rouge_score nltk

cd examples/pytorch/summarization

pip install 'accelerate>=0.26.0'

python run_summarization.py \
    --model_name_or_path t5-base \
    --train_file ./train.csv \
    --validation_file ./val.csv \
    --text_column text \
    --summary_column summary \
    --do_train \
    --do_eval \
    --output_dir ./t5_summarization_output \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --num_train_epochs 3 \
    --predict_with_generate \
    --overwrite_output_dir


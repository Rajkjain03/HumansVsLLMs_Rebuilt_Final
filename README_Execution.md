# README - HumansVsLLMs_Rebuilt_Final

## Setup
unzip HumansVsLLMs_Rebuilt_Final.zip
cd HumansVsLLMs_Rebuilt_Final
python3 -m venv venv
source venv/bin/activate
pip install pytest hypothesis nbclient nbformat jupyter

## Run per-question tests (example)
cd chinese_zodiac
pytest test_chinese_zodiac_llm.py -v
pytest test_chinese_zodiac_human.py -v

## Execute all notebooks (optional)
cd ..
python execute_all_notebooks.py

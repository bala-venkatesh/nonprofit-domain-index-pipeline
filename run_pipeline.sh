#!/bin/bash

echo "Running Nonprofit Crawl Pipeline..."

source venv/bin/activate

python classifier/nonprofit_classifier.py
python processing/deduplicate_domains.py
python processing/export_to_csv.py

echo "Pipeline Completed"

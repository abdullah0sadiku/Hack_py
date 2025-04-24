#!/bin/bash
echo "Running FHIR Data Harmonizer Pipeline..."
python scripts/map_patient.py
echo "✅ Pipeline complete."

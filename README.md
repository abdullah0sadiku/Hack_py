# 🏥 FHIR Data Harmonizer

This project converts messy healthcare CSV data (e.g., from [Synthea](https://synthetichealth.github.io/synthea/)) into clean, structured [FHIR](https://hl7.org/fhir/) JSON bundles for use with healthcare systems like DBIgnite.

## 🔧 Features
- 🧹 ETL pipeline to map patient records to valid FHIR resources
- ✅ JSON Schema validation ready
- 📦 Exports `Bundle` type FHIR JSON
- 📊 Optional logging & validation reports

## 📁 Project Structure

```bash
fhir-data-harmonizer/
├── data/               # Raw Synthea CSVs
├── fhir_schemas/       # JSON schemas (optional)
├── output/             # Exported FHIR bundles
├── scripts/            # ETL logic
├── validation/         # Logs and reports
```

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Place your Synthea CSVs in `/data`

```bash
# For example
data/patients.csv
```

### 3. Run the patient mapping script

```bash
python scripts/map_patient.py
```

### 4. Output

Check the generated FHIR bundle here:

```
output/patient_bundle.json
```

## 📋 To-Do
- [ ] Add `Condition`, `Encounter`, `Observation` mappers
- [ ] Add validation via JSONSchema or fhir.resources
- [ ] Add CLI or web UI (optional)

---

Built for the 💻 Hackathon 2025!

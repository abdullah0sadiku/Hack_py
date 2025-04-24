import pandas as pd
import json
from pathlib import Path

def map_patient(row):
    return {
        "resourceType": "Patient",
        "id": row["Id"],
        "name": [{
            "use": "official",
            "family": row["LAST"],
            "given": [row["FIRST"]]
        }],
        "gender": row["GENDER"].lower(),
        "birthDate": row["BIRTHDATE"],
        "address": [{
            "city": row["CITY"],
            "state": row["STATE"],
            "postalCode": row["ZIP"],
            "country": "US"
        }]
    }

def main():
    df = pd.read_csv("csv/patients.csv")
    bundle = {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": []
    }

    for _, row in df.iterrows():
        resource = map_patient(row)
        bundle["entry"].append({"resource": resource})

    Path("output").mkdir(exist_ok=True)
    with open("output/patient_bundle.json", "w") as f:
        json.dump(bundle, f, indent=2)

    print("✅ Patient bundle generated at output/patient_bundle.json")

if __name__ == "__main__":
    main()

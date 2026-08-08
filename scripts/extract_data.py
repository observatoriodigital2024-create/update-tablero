import csv
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

from openpyxl import load_workbook

SOURCE = Path(sys.argv[1])
OUTPUT = Path(sys.argv[2])

def text(value):
    if value is None:
        return ""
    if isinstance(value, (datetime, date)):
        return value.strftime("%Y-%m-%d")
    return re.sub(r"\s+", " ", str(value).replace("\xa0", " ")).strip()

def clean_status(value):
    value = text(value)
    aliases = {
        "no inicido": "No iniciado",
        "no iniciado": "No iniciado",
        "en curso": "En curso",
        "terminado": "Terminado",
        "rechazado": "Rechazado",
    }
    return aliases.get(value.strip().lower(), value.strip() or "Sin estado")

def split_people(value):
    value = text(value)
    if not value or value.lower() in {"todos", "por definir"}:
        return [value] if value else []
    value = re.sub(r"\s+y\s+", ",", value, flags=re.I)
    people = [p.strip() for p in value.split(",") if p.strip()]
    people = [{"Martin": "Martín"}.get(person, person) for person in people]
    return list(dict.fromkeys(people))

wb = load_workbook(SOURCE, data_only=True, read_only=True)
projects = []
people_rows = []

for sheet in wb.worksheets:
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row[0]:
            continue
        values = list(row[:7]) + [None] * max(0, 7 - len(row))
        project_id = f"P{len(projects)+1:03d}"
        people = split_people(values[1])
        record = {
            "id": project_id,
            "categoria": sheet.title,
            "proyecto": text(values[0]),
            "responsables": text(values[1]),
            "lista_responsables": "|".join(people),
            "fecha_inicio": text(values[2]),
            "fecha_fin": text(values[3]),
            "estado": clean_status(values[4]),
            "observaciones": text(values[5]),
            "por_hacer": text(values[6]),
        }
        projects.append(record)
        people_rows.extend({"id": project_id, "responsable": person} for person in people)

OUTPUT.mkdir(parents=True, exist_ok=True)
with (OUTPUT / "proyectos.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=projects[0].keys())
    writer.writeheader(); writer.writerows(projects)
with (OUTPUT / "responsables.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "responsable"])
    writer.writeheader(); writer.writerows(people_rows)

print(f"{len(projects)} proyectos y {len(people_rows)} asignaciones exportadas")

import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("analytics/upload_logs.jsonl")

def log_upload_event(user_id: str, document_type: str, filename: str, text_length: int, notes: str = ""):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "document_type": document_type,
        "filename": filename,
        "text_length": text_length,
        "notes": notes
    }

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
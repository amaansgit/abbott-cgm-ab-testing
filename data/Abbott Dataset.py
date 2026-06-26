import numpy as np
import pandas as pd
import os

# ----------------------------
# Reproducibility
# ----------------------------
np.random.seed(42)

N = 100000

# ----------------------------
# Patient Demographics
# ----------------------------

patient_id = [f"P{100000+i}" for i in range(N)]

age = np.random.choice(
    np.arange(18, 81),
    size=N,
    p=np.concatenate(
        [
            np.repeat(0.20 / 13, 13),  # 18-30
            np.repeat(0.35 / 15, 15),  # 31-45
            np.repeat(0.30 / 15, 15),  # 46-60
            np.repeat(0.15 / 20, 20),  # 61-80
        ]
    ),
)

gender = np.random.choice(["Male", "Female"], size=N, p=[0.52, 0.48])

diabetes_type = np.random.choice(["Type 1", "Type 2"], size=N, p=[0.35, 0.65])

states = [
    "California",
    "Texas",
    "Florida",
    "New York",
    "Illinois",
    "Ohio",
    "Pennsylvania",
    "Georgia",
    "North Carolina",
    "Michigan",
]

state = np.random.choice(states, size=N)

device = np.random.choice(["Libre 2", "Libre 3"], size=N, p=[0.60, 0.40])

days_since_signup = np.random.randint(30, 731, size=N)

# ----------------------------
# Campaign Groups
# ----------------------------

campaign_group = np.random.choice(["A", "B", "C", "D"], size=N)

# ----------------------------
# Campaign Parameters
# ----------------------------

campaign_params = {
    "A": {
        "open_rate": 0.42,
        "sessions_mean": 4.8,
        "scan_mean": 8,
        "retention": 0.70,
        "refill": 0.58,
    },
    "B": {
        "open_rate": 0.56,
        "sessions_mean": 6.5,
        "scan_mean": 10,
        "retention": 0.79,
        "refill": 0.67,
    },
    "C": {
        "open_rate": 0.52,
        "sessions_mean": 7.0,
        "scan_mean": 12,
        "retention": 0.75,
        "refill": 0.63,
    },
    "D": {
        "open_rate": 0.48,
        "sessions_mean": 5.7,
        "scan_mean": 9,
        "retention": 0.74,
        "refill": 0.69,
    },
}

# ----------------------------
# Generate Metrics
# ----------------------------

notification_open = []
weekly_sessions = []
weekly_scan_count = []
avg_session_time = []
retained_30_days = []
prescription_refill = []
revenue = []

for grp in campaign_group:

    p = campaign_params[grp]

    # Notification Open
    opened = np.random.binomial(1, p["open_rate"])

    # Weekly Sessions
    sessions = np.random.normal(p["sessions_mean"] + opened * 0.8, 1.3)
    sessions = np.clip(round(sessions, 1), 1, 15)

    # Weekly Scan Count
    scans = np.random.normal(p["scan_mean"] + sessions * 0.25, 2)
    scans = max(2, round(scans))

    # Average Session Time
    session_time = np.random.normal(8 + sessions * 0.4, 2)
    session_time = round(max(2, session_time), 1)

    # Retention
    retention_prob = p["retention"]

    if sessions > 6:
        retention_prob += 0.05

    if scans > 10:
        retention_prob += 0.03

    retention_prob = min(retention_prob, 0.95)

    retained = np.random.binomial(1, retention_prob)

    # Prescription Refill
    refill_prob = p["refill"]

    if retained:
        refill_prob += 0.08

    if sessions > 6:
        refill_prob += 0.03

    refill_prob = min(refill_prob, 0.97)

    refill = np.random.binomial(1, refill_prob)

    # Revenue
    if refill:
        rev = round(np.random.uniform(140, 170), 2)
    else:
        rev = 0

    notification_open.append(opened)
    weekly_sessions.append(sessions)
    weekly_scan_count.append(scans)
    avg_session_time.append(session_time)
    retained_30_days.append(retained)
    prescription_refill.append(refill)
    revenue.append(rev)

# ----------------------------
# Create DataFrame
# ----------------------------

df = pd.DataFrame(
    {
        "patient_id": patient_id,
        "age": age,
        "gender": gender,
        "diabetes_type": diabetes_type,
        "state": state,
        "device": device,
        "days_since_signup": days_since_signup,
        "campaign_group": campaign_group,
        "notification_open": notification_open,
        "weekly_sessions": weekly_sessions,
        "weekly_scan_count": weekly_scan_count,
        "avg_session_time": avg_session_time,
        "retained_30_days": retained_30_days,
        "prescription_refill": prescription_refill,
        "revenue": revenue,
    }
)

# ----------------------------
# Save CSV
# ----------------------------

output_folder = r"C:\Users\AmaanAlam\OneDrive - ProcDNA Analytics Pvt. Ltd\Desktop\Abbott AB Testing"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "abbott_cgm_ab_testing_dataset.csv")

df.to_csv(output_file, index=False)

print("=" * 60)
print("Dataset Generated Successfully!")
print(f"Shape: {df.shape}")
print(f"Saved to: {output_file}")
print("=" * 60)

# Preview
print(df.head())

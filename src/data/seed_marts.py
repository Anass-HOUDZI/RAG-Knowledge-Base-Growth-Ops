"""Seed script — Génère les données fictives des 5 marts dbt dans DuckDB.

Exécuter une seule fois pour créer/recréer la base :
    python src/data/seed_marts.py
"""
import duckdb
import random
import os
from datetime import date, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "marts.duckdb")

random.seed(42)

# ── Helpers ──────────────────────────────────────────────────────────────────

def random_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))


def seed_database():
    """Crée et peuple les 5 marts avec données fictionnalisées."""
    # Supprimer l'ancien fichier s'il existe
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    con = duckdb.connect(DB_PATH)

    # ── 1. mart_partner_360 ─────────────────────────────────────────────────
    con.execute("""
        CREATE TABLE mart_partner_360 (
            partner_id VARCHAR,
            region VARCHAR,
            status VARCHAR,
            signup_date DATE,
            total_orders INTEGER,
            total_revenue DECIMAL(12,2)
        )
    """)

    regions = ["Europe West", "Europe East", "North America", "APAC", "LATAM"]
    statuses = ["active", "active", "active", "churned", "trial"]  # weighted

    for i in range(200):
        partner_id = f"P-{1000 + i}"
        region = random.choice(regions)
        status = random.choice(statuses)
        signup = random_date(date(2023, 1, 1), date(2026, 5, 1))
        orders = random.randint(0, 500) if status == "active" else random.randint(0, 50)
        revenue = round(orders * random.uniform(80, 350), 2)

        con.execute(
            "INSERT INTO mart_partner_360 VALUES (?, ?, ?, ?, ?, ?)",
            [partner_id, region, status, signup, orders, revenue],
        )

    # ── 2. mart_funnel_daily ────────────────────────────────────────────────
    con.execute("""
        CREATE TABLE mart_funnel_daily (
            date DATE,
            step VARCHAR,
            count_users INTEGER,
            conversion_rate DECIMAL(5,4)
        )
    """)

    steps = ["visit", "signup", "activation", "purchase"]
    base_counts = {"visit": 5000, "signup": 800, "activation": 400, "purchase": 120}
    base_rates = {"visit": 1.0, "signup": 0.16, "activation": 0.50, "purchase": 0.30}

    current = date(2025, 1, 1)
    while current <= date(2026, 6, 1):
        for step in steps:
            noise = random.uniform(0.85, 1.15)
            count = int(base_counts[step] * noise)
            rate = round(base_rates[step] * random.uniform(0.90, 1.10), 4)
            con.execute(
                "INSERT INTO mart_funnel_daily VALUES (?, ?, ?, ?)",
                [current, step, count, rate],
            )
        current += timedelta(days=1)

    # ── 3. mart_revenue_monthly ─────────────────────────────────────────────
    con.execute("""
        CREATE TABLE mart_revenue_monthly (
            month DATE,
            channel VARCHAR,
            revenue DECIMAL(12,2),
            new_customers INTEGER
        )
    """)

    channels = ["organic", "paid", "referral", "partner"]
    channel_revenue = {"organic": 45000, "paid": 65000, "referral": 22000, "partner": 38000}
    channel_custs = {"organic": 45, "paid": 80, "referral": 25, "partner": 35}

    for year in [2024, 2025, 2026]:
        max_month = 6 if year == 2026 else 12
        for m in range(1, max_month + 1):
            month_date = date(year, m, 1)
            # Growth trend
            growth_factor = 1 + (year - 2024) * 0.15 + m * 0.01
            for ch in channels:
                rev = round(channel_revenue[ch] * growth_factor * random.uniform(0.8, 1.2), 2)
                custs = int(channel_custs[ch] * growth_factor * random.uniform(0.7, 1.3))
                con.execute(
                    "INSERT INTO mart_revenue_monthly VALUES (?, ?, ?, ?)",
                    [month_date, ch, rev, custs],
                )

    # ── 4. mart_cohort_retention ────────────────────────────────────────────
    con.execute("""
        CREATE TABLE mart_cohort_retention (
            cohort_month DATE,
            period_number INTEGER,
            retention_pct DECIMAL(5,2)
        )
    """)

    for year in [2024, 2025, 2026]:
        max_month = 6 if year == 2026 else 12
        for m in range(1, max_month + 1):
            cohort = date(year, m, 1)
            retention = 100.0
            for period in range(0, 13):
                if period == 0:
                    retention = 100.0
                elif period == 1:
                    retention = round(random.uniform(55, 75), 2)
                else:
                    decay = random.uniform(0.88, 0.96)
                    retention = round(retention * decay, 2)
                    retention = max(retention, 5.0)

                # Limit period based on how old the cohort is
                months_since = (date(2026, 6, 1).year - cohort.year) * 12 + (6 - cohort.month)
                if period <= months_since:
                    con.execute(
                        "INSERT INTO mart_cohort_retention VALUES (?, ?, ?)",
                        [cohort, period, retention],
                    )

    # ── 5. mart_growth_accounting ───────────────────────────────────────────
    con.execute("""
        CREATE TABLE mart_growth_accounting (
            month DATE,
            status VARCHAR,
            n_users INTEGER
        )
    """)

    ga_statuses = ["new", "retained", "resurrected", "churned"]
    ga_base = {"new": 120, "retained": 800, "resurrected": 35, "churned": 60}

    for year in [2024, 2025, 2026]:
        max_month = 6 if year == 2026 else 12
        for m in range(1, max_month + 1):
            month_date = date(year, m, 1)
            growth_factor = 1 + (year - 2024) * 0.12 + m * 0.008
            for status in ga_statuses:
                n = int(ga_base[status] * growth_factor * random.uniform(0.8, 1.2))
                con.execute(
                    "INSERT INTO mart_growth_accounting VALUES (?, ?, ?)",
                    [month_date, status, n],
                )

    con.close()
    print(f"✅ Database seeded: {DB_PATH}")

    # Verify
    con = duckdb.connect(DB_PATH, read_only=True)
    for table in [
        "mart_partner_360",
        "mart_funnel_daily",
        "mart_revenue_monthly",
        "mart_cohort_retention",
        "mart_growth_accounting",
    ]:
        count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"   {table}: {count} rows")
    con.close()


if __name__ == "__main__":
    seed_database()

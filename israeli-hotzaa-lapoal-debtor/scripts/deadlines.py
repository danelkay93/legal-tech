#!/usr/bin/env python3
"""Prepare calendar-day planning dates for Hotzaa LaPoal debtor notices.

The four azhara clocks run from service (hamtzaa), not from the date printed on the azhara and not
from the day the debtor noticed the file. This does not validate service, determine a
legal last day, or adjust holidays, recesses, emergencies or registrar orders.
Payment-order and examination dates must be copied from the actual applicable notice;
they are not inferred solely from file type. See references/forms-and-clocks.md.

Usage:
  python3 deadlines.py 2026-08-01 --type shtar
  python3 deadlines.py 2026-08-01 --type katzuv
  python3 deadlines.py 2026-08-01 --type psak-din
"""
import argparse
from datetime import date, timedelta

TYPES = {
    "shtar":    ("Bill or check (shtar / hamchaa)", True),
    "katzuv":   ("Fixed-sum claim (sechum katzuv)", True),
    "psak-din": ("Money judgment (psak din kaspi)", False),
    "mezonot":  ("Maintenance (mezonot)",           False),
}

def iso_date(value):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() != value:
            raise ValueError
        return parsed
    except ValueError:
        raise argparse.ArgumentTypeError("Use a real calendar date in YYYY-MM-DD format") from None

def main():
    p = argparse.ArgumentParser(description="Hotzaa LaPoal provisional calendar planner")
    p.add_argument("served", type=iso_date, help="verified service date of the azhara, YYYY-MM-DD")
    p.add_argument("--type", required=True, choices=sorted(TYPES), help="file type")
    p.add_argument("--payment-order-date", type=iso_date, help="applicable payment-order date from the azhara")
    p.add_argument("--examination-date", type=iso_date, help="applicable ability-examination date from the azhara")
    a = p.parse_args()

    served = a.served
    label, can_object = TYPES[a.type]
    if a.type == "mezonot" and (a.payment_order_date or a.examination_date):
        p.error("Maintenance requires its separate procedure; ordinary notice dates are not accepted here")
    for notice_date in (a.payment_order_date, a.examination_date):
        if notice_date and notice_date < served:
            p.error("Notice date precedes service; reconcile the notice/service record before calculation")

    print(f"File type   : {label}")
    print(f"Azhara served: {served.isoformat()}")
    print("PLANNING ONLY: service day excluded; no holiday/recess/emergency adjustment or service validation.")
    print()

    rows = []
    if can_object:
        rows.append(("Objection (form 218)", served + timedelta(days=30),
                     "30 calendar days from supplied service. Check valid service and applicable counting rules. "
                     "A late objection needs extension and separate stay requests; filing alone does not grant them."))
    else:
        rows.append(("Objection", None,
                     "NOT AVAILABLE on this file type. Consider paraati (form 236) or setting aside the judgment."))
    if a.type != "mezonot":
        rows.append(("Payment order (form 233)", a.payment_order_date,
                     "Supplied azhara date, not calculated. If absent, read the notice: s.7A allows its date "
                     "to differ from the ordinary 20-day rule. Do not assume 30 days from fixed-sum file type."))
    if a.type == "mezonot":
        rows.append(("Maintenance warning", None,
                     "No ordinary payment order (form 233). Arrest and past-arrears applications use separate "
                     "rules and warnings; this planner does not calculate them."))
    else:
        rows.append(("Ability examination", a.examination_date,
                     "Supplied notice date, not calculated. Check s.67(a1), the notice and any pending objection/"
                     "paraati proceedings or rejection; the ordinary 21-day period is not universal."))

    for name, when, note in rows:
        when_s = when.isoformat() if when else "not calculated — check applicable notice/procedure"
        left = f"({(when - date.today()).days:+d} days from today)" if when else ""
        print(f"  {name}")
        print(f"    planning/notice date: {when_s} {left}")
        print(f"    {note}")
        print()

    print("Paraati (form 236, relief 119) has NO deadline and stays open at any stage.")
    print("Reminder: a payment order does NOT lift existing restrictions or attachments.")
    print("A restriction takes effect only 30 days after its own warning is served: pay, or ask for an")
    print("ability examination on form 400 (code 159), inside that window. Count it from the warning, not the azhara.")
    print("If the restriction was imposed in your presence, no warning is sent and the 30 days run from imposition.")

if __name__ == "__main__":
    main()

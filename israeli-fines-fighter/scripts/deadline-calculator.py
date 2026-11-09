#!/usr/bin/env python3
"""
Israeli Fine Appeal Deadline Calculator

Calculates 30/90-day arithmetic milestones from a supplied service date.
These are not verified legal deadlines or a determination of remedy eligibility.

Usage:
    python deadline-calculator.py --date 2026-03-15 --type parking
    python deadline-calculator.py --date 2026-03-15 --type traffic
    python deadline-calculator.py --help
"""

import argparse
from datetime import datetime, timedelta
import sys

# Baseline arithmetic only. Service/deemed service, the applicable offence-date
# regime, statutory counting, rest days and later decisions can change the
# legal deadline. The administrative non-driver and post-decision paths are
# not calculated here. Collection by the Fines Collection Center is not an
# Execution Office objection route; read the actual collection notice.
PARKING_CANCEL_DAYS = 30
TRAFFIC_CANCEL_DAYS = 30
COURT_HEARING_DAYS = 90
SURCHARGE_STARTS_DAYS = 90  # legacy arithmetic milestone, NOT an accrual determination

# Verify the specific notice and current rules before advising on any track.


def calculate_deadline(receipt_date: str, fine_type: str) -> dict:
    """Return arithmetic milestones only; legacy key names are not legal findings."""
    try:
        date = datetime.strptime(receipt_date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{receipt_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    cancel_window = PARKING_CANCEL_DAYS if fine_type == "parking" else TRAFFIC_CANCEL_DAYS
    # Baseline 30/90 arithmetic; exceptions and legal counting are not modelled.
    appeal_deadline = date + timedelta(days=cancel_window)
    court_deadline = date + timedelta(days=COURT_HEARING_DAYS)
    surcharge_deadline = date + timedelta(days=SURCHARGE_STARTS_DAYS)

    days_to_appeal = (appeal_deadline - today).days
    days_to_court = (court_deadline - today).days
    days_to_surcharge = (surcharge_deadline - today).days

    return {
        "calculation_only": True,
        "receipt_date": date.strftime("%Y-%m-%d"),
        "fine_type": fine_type,
        "appeal_deadline": appeal_deadline.strftime("%Y-%m-%d"),
        "days_remaining_appeal": max(days_to_appeal, 0),
        # Legacy flag means only that the calculated 30-day date has not passed.
        "can_appeal": days_to_appeal >= 0,
        "on_appeal_date": days_to_appeal == 0,
        "on_court_date": days_to_court == 0,
        # Kept for backwards compatibility with earlier CLI consumers.
        "late_payment_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_late": max(days_to_court, 0),
        "court_hearing_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_court": max(days_to_court, 0),
        "surcharge_deadline": surcharge_deadline.strftime("%Y-%m-%d"),
        "days_until_surcharge": max(days_to_surcharge, 0),
        # Legacy flag means after the arithmetic 90-day date, not actual accrual.
        "surcharge_started": days_to_surcharge < 0,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate Israeli fine 30/90-day milestones (not legal deadlines)"
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Supplied service date (YYYY-MM-DD); verify receipt/deemed service separately",
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["parking", "traffic", "administrative"],
        help=(
            "parking or traffic: use only for a notice on the criminal track; baseline "
            "30-day bakasha le-bitul, 90-day bakasha le-hishafet. administrative = Administrative "
            "Traffic Violations Law track: 30-day hasagah (90 if you were not the driver), "
            "90-day arar to the traffic tribunal, and NO request to be tried. Which track "
            "applies must be checked against the OFFENCE date and current rules. "
            "This helper does not calculate exceptions or statutory counting rules."
        ),
    )

    args = parser.parse_args()
    result = calculate_deadline(args.date, args.type)

    fine_label = {
        "parking": "Parking fine",
        "traffic": "Traffic fine",
        "administrative": "Administrative traffic violation",
    }[result["fine_type"]]
    admin = result["fine_type"] == "administrative"

    print(f"\n{'='*50}")
    print(f"  {fine_label} Arithmetic Milestones")
    print(f"{'='*50}")
    print(f"  Receipt date:           {result['receipt_date']}")
    if admin:
        print(f"  Hasagah window:         30 days (90 if you were not the driver, s.8(a))")
        print(f"  30-day arithmetic date: {result['appeal_deadline']}")
        print(f"  90-day arithmetic date: {result['court_hearing_deadline']}")
        print(f"  Not calculated:         non-driver or post-hasagah-decision deadlines")
        print(f"  Note:                   there is NO bakasha le-hishafet on this track")
    else:
        print(f"  Cancellation window:    30 days (bakasha le-bitul)")
        print(f"  30-day arithmetic date: {result['appeal_deadline']}")
        print(f"  90-day arithmetic date: {result['court_hearing_deadline']}")

    if result["on_appeal_date"]:
        print("  Status:                 CALCULATED 30-DAY DATE IS TODAY; CHECK URGENTLY")
    elif result["can_appeal"]:
        print(f"  Days to calculated 30-day date: {result['days_remaining_appeal']}")
    elif result["on_court_date"]:
        print("  Status:                 CALCULATED 90-DAY DATE IS TODAY; CHECK URGENTLY")
    elif not result["surcharge_started"]:
        print("  Status:                 AFTER CALCULATED 30-DAY DATE, BEFORE 90-DAY DATE")
        print(f"  Days to calculated 90-day date: {result['days_remaining_court']}")
    else:
        print("  Status:                 AFTER CALCULATED 90-DAY DATE; CHECK AVAILABLE REMEDIES")

    print("  Verify: service/deemed service, offence-date regime, counting and rest-day")
    print("          rules, later decisions and possible extensions before relying on a date.")
    print("  Arithmetic does not establish the statutory last day or surcharge accrual.")
    print("  Check the payment date and balance with the authority named on the notice.")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

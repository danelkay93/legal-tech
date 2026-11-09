# Forms, codes and clocks (debtor side)

The azhara clocks below run from **service of the azhara** (hamtzaat ha-azhara), not from the
date printed on it and not from the day the debtor noticed the file; the restriction and arrest
clocks run from their own warnings. Section numbers are to the Execution Law, 5727-1967, as shown
in the National Insurance Institute's consolidated text (amendment notes to 2025, not a certified
current text), checked on 28 October 2026.

How to count: every date is a provisional planning calculation. The general rule is that the
service day is not counted, and rest days, recess days and statutory holidays count unless they are
the last days of the period (Interpretation Law, 5741-1981, s.10(א), (ג)). Then check valid
service, any recess or emergency rule for that particular procedure, and the calendar. Filing any
request in the file counts as full service on that day unless the registrar orders otherwise
(s.7(ג1)). A date printed on the azhara governs only where the statute lets the azhara set it (the
payment-order request, s.7א(א); the ability examination, s.67(א1)); it does not change the 30-day
objection period. `scripts/deadlines.py` is excluded from this documents-only deployment and is
unvalidated.

## Forms

| Form | Purpose | Notes |
|---|---|---|
| 218 | Objection to execution of a bill, or to a fixed-sum claim | Same form for both routes. 3 copies. Needs a witnessed affidavit |
| 236 | Paraati claim (debt already discharged) | Mark relief number 119. 2 copies |
| 214 | Cancel, stay or renew proceedings and restrictions | Online code 311. Per file, not per debtor |
| 233 | Payment order, or change of an existing one | Attach form 529. Not for maintenance debt |
| 400 | Request to be summoned to an ability examination | Code 159, inside the 30 days after a restriction warning |
| 529 | Questionnaire and confidentiality waiver | Signed by the debtor, attached to form 233 |

## Clocks

| Days | What | Applies to | Source |
|---|---|---|---|
| 30 | Objection deadline | Bill files and fixed-sum files ONLY | s.81א(ג1); s.81א1(ד)(1) |
| 20, or the date set in the azhara | Payment-order request | All money files by default. A fixed-sum azhara may set 30, and Kol Zchut gives 30 for these files; the statute changes only their objection period (s.81א1(ה)(1)), so read the azhara | s.7א(א) |
| 21, or the date set in the azhara | Ability examination | Suspended while a paraati claim or bill objection is pending; counted again from a rejection | s.67(א1) |
| 14 | Creditor delivers the court decision back to the office | After the court rules on an objection | Kol Zchut |
| none | Paraati claim | Any stage; payment or other discharge only, not the original debt | s.19 |
| 30 | Restriction takes effect after its warning is served | Runs from the restriction warning, not the azhara; from imposition if imposed in the debtor's presence | s.66ג |
| 7 | Arrest order carried out after its warning is served | Maintenance files only | s.74(ג) |

## Challenge route by file type

| File type | Objection? | Notes |
|---|---|---|
| Bill or check | Yes, form 218 | Grounds include failure of consideration, forgery, theft, no signature, defective endorsement, security check |
| Fixed-sum claim | Yes, form 218 | Adds technical grounds: over the 75,000 NIS ceiling, not calculable by simple arithmetic, or filed without the statutory prior warning and the 30-day (and at most one-year) wait (s.81א1(א), (ב1), (ג)(1)) |
| Money judgment | No | Paraati, set-aside of a default judgment, appeal, or stay of execution |
| Maintenance | Separate track | Wage protection does not apply. Arrest up to 21 days without an ability examination. No ordinary payment order; past arrears can be spread |
| Performance of an act | Separate track | Out of scope for this skill |

## The five restrictions (Enforcement Law s.66א)

Exit from the country; passport or travel document; special restricted customer under the
Checks Without Cover Law (no checks; whether an account without checks stays available is a
banking-rules question not verified here, so check current Bank of Israel guidance); charge cards (not an immediate-debit card usable only against a credit balance, or a card loaded only with a protected benefit); founding or holding an interest
in a corporation. Passport and exit restrictions are not imposed where travel is needed for the
health of the debtor or a dependent family member.

There is no driving-licence restriction. A restriction takes effect only 30 days after its
warning is served, or 30 days after imposition if imposed in the debtor's presence (no warning then).
It needs a statutory ground first (s.66ב): evader with debts over 500 NIS after appearing, a maintenance
debt, or presumed evader plus 6 months and over 2,500 NIS, or 1 year and over 500 NIS. Cancellation is on form 214 and is granted where the debt is paid, a payment
order is being complied with, or an approved agreement with the creditor is being complied with.

## Two traps worth restating

1. A payment order, once granted, does **not** lift existing restrictions or attachments.
   Each needs its own request.
2. A restriction can be re-imposed immediately and with no warning if compliance lapses.
3. Paraati is not the late-objection route. Grounds against the original debt need a late
   objection, an extension request with an affidavit, and a separate stay request.

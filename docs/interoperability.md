# Interoperability Notes

AAIO is intentionally narrower than global taxonomies but keeps fields that make later mapping possible.

## AI Incident Database (AIID)

Where a case is already indexed by AIID, AAIO stores `aiid_id` and `aiid_url`. AAIO does not copy AIID taxonomy labels wholesale; it preserves a small set of human-readable harm descriptors and source links.

## OECD AI Incidents and Hazards Monitor (AIM)

AAIO's `country`, `sector`, `affected_parties`, `incident_date`, `summary`, `harm_types` and source fields are designed to support later mapping to AIM-style incident metadata. AAIO's core dataset intentionally focuses on realised incidents; a future hazard collection should be clearly separated.

## NIST AI RMF

The repository supports practical risk-management activities by documenting incidents, response, evidence and lessons in a repeatable structure. It is not a NIST conformity assessment.

## EU AI Act Article 73

The project is not a regulatory reporting mechanism. However, its structured fields can help researchers study the type of information serious-incident regimes need: affected system/context, event date, harm, response, evidence and corrective action.

## Design principle

Interoperability should not erase local context. AAIO therefore keeps narrative fields and source-calibrated notes alongside machine-readable columns.

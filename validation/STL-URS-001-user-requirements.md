# STL-URS-001 — SampleTrack Lite User Requirements Specification

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-URS-001 |
| Title | SampleTrack Lite User Requirements Specification |
| System | SampleTrack Lite |
| Document status | Draft |
| Requirement count | 35 |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This User Requirements Specification defines the required behavior of SampleTrack Lite for the bounded fictional GMP warehouse/distribution scenario described by STL-SD-001.

The requirements express regulated-user and process needs rather than implementation design.

They are intended to become traceable to:

- STL-RSK-001 risk/failure modes;
- STL-OQ-001 verification;
- execution evidence;
- STL-DL-001 deviations where applicable;
- STL-VSR-001 final disposition.

No risk score is assigned in this document. Risk scoring belongs in STL-RSK-001.

## 2. Requirement-writing conventions

Each requirement:

- has one stable ID;
- uses "shall" for required system behavior;
- is intended to be objectively verifiable;
- names its principal GxP rationale;
- maps to the regulatory/guidance source that motivates the requirement.

A regulatory reference does not mean that every cited source is legally applicable in every jurisdiction.

The 21 CFR Part 11 references are the conditional exercise overlay defined in STL-RA-001.

## 3. Source abbreviations

| Abbreviation | Source |
|---|---|
| HC-0001 | Health Canada GUI-0001 — Good manufacturing practices guide for drug products |
| HC-0050 | Health Canada GUI-0050 — Annex 11: Computerized Systems |
| HC-0069 | Health Canada GUI-0069 — Environmental control during storage and transportation |
| P11 | 21 CFR Part 11, used as a conditional exercise overlay |
| GAMP | GAMP 5 Second Edition, used as industry lifecycle guidance |

## 4. Receiving and core record control

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-001 | The system shall assign a unique, persistent identifier to each SampleTrack inventory/receiving record. | Prevents ambiguous identity and supports traceability. | HC-0001; HC-0050 4.5/4.7 | OQ |
| URS-002 | The system shall require product/material identifier, lot or batch number, receipt date, required storage condition, received quantity or sample count where applicable, and receiving user before a receiving record can be completed. | Prevents incomplete regulated receiving records. | HC-0001; HC-0069 5.4 | OQ |
| URS-003 | The system shall automatically record the identity of the user creating a receiving record and the date/time of creation. | Supports attributable, contemporaneous records. | HC-0050 4.12(4); P11 11.10(e) overlay | OQ |
| URS-004 | For critical manually entered receiving data identified by risk assessment, the system shall require an independent verification step or a validated electronic accuracy check before the record can enter a Released state. | Reduces risk from erroneous critical manual data. | HC-0050 4.6 | OQ / configuration review |
| URS-005 | The system shall preserve previously recorded GxP information when a permitted correction is made rather than overwriting the prior value without history. | Protects data integrity and reconstructability. | HC-0050 4.9; P11 11.10(e) overlay | OQ |
| URS-006 | The system shall prevent standard Warehouse Operator and QA Reviewer users from permanently deleting a completed GxP receiving/inventory record. | Protects required records from loss. | HC-0050 4.7/4.9; P11 11.10(c) overlay | OQ |
| URS-007 | Authorized users shall be able to retrieve a receiving/inventory record by its unique SampleTrack record ID and by lot/batch identifier and generate an accurate, complete human-readable copy of the retrieved regulated record. | Supports investigation, recall, inspection-like review, and accurate record copying. | HC-0001; HC-0050 4.7/4.8; P11 11.10(b) overlay | OQ |
| URS-008 | The system shall retain the relationship between the current record state and its associated receiving, status, custody, excursion, disposition, audit-trail, and signature information. | Prevents fragmented evidence and supports inspection/reconstruction. | HC-0001; HC-0050 4.7/4.9 | OQ |

## 5. Storage location and material status

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-009 | The system shall require each active inventory record to have a configured required storage condition. | Supports appropriate environmental control. | HC-0069 4.1; HC-0001 | OQ |
| URS-010 | The system shall allow storage location assignment only from active configured storage locations authorized for the record's required storage condition. | Reduces inappropriate storage-location assignment. | HC-0069; HC-0001 | OQ |
| URS-011 | A newly completed receiving record shall enter the configured initial controlled status of Quarantine unless an explicitly validated alternate workflow applies. | Prevents unreviewed material from appearing available. | HC-0001 material-status control | OQ |
| URS-012 | The system shall use controlled configured material-status values, including at minimum Quarantine, Released, On Hold, Rejected, Returned, and Recalled. | Supports segregation, inventory control, and recall. | HC-0001 | OQ / configuration review |
| URS-013 | The system shall enforce permitted status-transition sequences and shall prevent a user from bypassing a required quality-review step. | Prevents invalid workflow sequencing. | HC-0050 4.4(7); P11 11.10(f) overlay | OQ |
| URS-014 | Only a user with the configured QA authority shall be able to perform a quality disposition that places material into Released or Rejected status after a quality hold/review. | Protects quality decisions from unauthorized execution. | HC-0001; HC-0050 4.12; P11 11.10(g) overlay | OQ |
| URS-015 | A GMP-relevant material-status change shall record the user, date/time, prior status, new status, and required reason or disposition rationale. | Supports attributable status history and investigation. | HC-0050 4.9/4.12 | OQ |

## 6. Temperature-excursion control

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-016 | The system shall identify a temperature excursion when an entered or received temperature condition is outside the configured allowable range for the affected material. | Supports timely identification of potentially affected stock. | HC-0069 4.1/5.4; HC-0001 | OQ boundary testing |
| URS-017 | The system shall apply the configured excursion rule consistently at the lower and upper temperature boundaries, including values immediately inside, at, and outside each limit. | Demonstrates correct limit handling at the failure boundary. | HC-0050 4.4(7); HC-0069 | OQ boundary testing |
| URS-018 | An excursion record shall capture the affected SampleTrack record, observed temperature or condition, event date/time, source or reporter, and available duration/details required by the configured process. | Preserves information needed for investigation. | HC-0069; HC-0001 | OQ |
| URS-019 | When a record is subject to an unresolved temperature excursion, the system shall place or maintain the affected material in a restricted On Hold state and shall prevent a Warehouse Operator from returning it to Released status. | Prevents potentially affected product from uncontrolled use/distribution. | HC-0069; HC-0001; P11 11.10(f)/(g) overlay | OQ negative/authority testing |
| URS-020 | A QA excursion disposition shall require a documented rationale and shall preserve the resulting disposition/status with the excursion history. | Supports evidence-based accept/reject decisions and traceability. | HC-0069 4.1/5.4; HC-0050 4.9 | OQ |

## 7. Chain of custody

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-021 | The system shall record each in-scope custody or responsibility transfer against the affected SampleTrack record. | Supports handling traceability. | HC-0001 | OQ |
| URS-022 | Each custody event shall identify the acting user, event date/time, and the relevant prior/new custody or location information defined by the workflow. | Supports attribution and reconstruction. | HC-0050 4.12(4); HC-0001 | OQ |
| URS-023 | Recording a new custody event shall not overwrite or remove prior custody-history events. | Preserves complete handling history. | HC-0050 4.7/4.9 | OQ |

## 8. Security and authority controls

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-024 | The system shall assign each user a unique user identity and shall not permit a single active user identity to be shared by multiple named users. | Supports attributable actions and signature identity. | HC-0050 4.12; P11 11.100/11.300 overlay | OQ / configuration review |
| URS-025 | The system shall require successful authentication before a user can access GxP functions. | Restricts system access to authorized users. | HC-0050 4.12(1); P11 11.10(d) overlay | OQ |
| URS-026 | The system shall restrict functions and data-changing actions according to the user's configured role and authority. | Prevents unauthorized operations. | HC-0050 4.12; P11 11.10(g) overlay | OQ |
| URS-027 | A disabled or cancelled user account shall be prevented from authenticating to the system. | Ensures revoked access is effective. | HC-0050 4.12(3); P11 11.300 overlay | OQ |
| URS-028 | The creation, change, and cancellation of user access authorizations shall be recorded with sufficient information to determine what access changed and when. | Supports review of access administration. | HC-0050 4.12(3) | OQ / admin record review |

## 9. Audit trail and data-integrity controls

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-029 | The system shall generate an audit-trail record for GMP-relevant creation, modification, deletion attempt where supported, material-status change, excursion disposition, and electronic approval/signature actions identified by risk. | Preserves history of critical GxP actions. | HC-0050 4.9; P11 11.10(e) overlay | OQ |
| URS-030 | For a GMP-relevant change, the audit trail shall identify the acting user, date/time, affected record, action/change, prior and new values where applicable, and reason for change where required by the workflow. | Makes change history intelligible and attributable. | HC-0050 4.9/4.12(4); P11 11.10(e) overlay | OQ |
| URS-031 | Authorized ordinary users shall not be able to alter or delete audit-trail entries, and record changes shall not obscure previously recorded GxP information. | Protects audit evidence from ordinary manipulation. | HC-0050 4.9; P11 11.10(e) overlay | OQ negative testing |
| URS-032 | Authorized QA users shall be able to retrieve and review the GMP-relevant audit trail in a generally intelligible form associated with the applicable record. | Supports routine review and investigation. | HC-0050 4.9 | OQ |

## 10. Electronic-signature controls

| ID | User requirement | GxP rationale | Source mapping | Planned verification |
|---|---|---|---|---|
| URS-033 | A required electronic signature shall display or retain the signer's name, date/time of signing, and meaning of the signature such as review or approval. | Establishes who signed, when, and for what purpose. | HC-0050 4.14; P11 11.50 overlay | OQ |
| URS-034 | An electronic signature shall remain permanently linked to the specific electronic record/action it signs and shall be included with the signature information in human-readable record output. | Prevents detached or misleading signatures. | HC-0050 4.14; P11 11.50/11.70 overlay | OQ |
| URS-035 | Each electronic signature shall be associated with one unique user identity and, for this non-biometric exercise, the signing action shall require the configured identification code and password controls so that another user cannot ordinarily apply that signature. | Supports signature authenticity and non-repudiation controls. | P11 11.100/11.200/11.300 overlay; HC-0050 4.12/4.14 | OQ negative/authentication testing |

## 11. Record-copy and retention expectations

The 35 requirements above deliberately keep the core URS small.

The following lifecycle expectations remain required real-world controls but are not represented as separate application-functional URS rows in this revision because the mock exercise does not include real production infrastructure or long-term operation:

- regular backup of relevant data;
- verified restoration of backup data;
- long-term archival accessibility/readability/integrity;
- tested business-continuity arrangements;
- periodic review of the validated state.

Those expectations are retained in STL-VP-001 as production dependencies and revalidation/lifecycle controls rather than being falsely marked as fully verified application functions.

If the exercise later implements a real backup/restore or archive mechanism in the demonstration environment, a controlled URS revision may add bounded requirements and verification.

## 12. Requirement-quality review

Before this URS is treated as the OQ design authority, review each requirement for:

- necessity for the stated intended use;
- one clear primary behavior;
- objective verifiability;
- absence of hidden implementation design;
- absence of vague adjectives such as "secure", "robust", or "user-friendly" without a testable property;
- consistency with STL-SD-001;
- consistency with STL-RA-001;
- correct treatment of Part 11 as a conditional overlay.

## 13. Planned traceability

STL-RTM-001 will add, at minimum:

```text
URS ID
  -> risk ID / risk level
  -> OQ test ID
  -> execution result
  -> evidence ID
  -> deviation ID where applicable
  -> final status
```

This URS intentionally does not predeclare risk rankings before STL-RSK-001 is authored.

## 14. References

- Health Canada GUI-0001  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/gmp-guidelines-0001/document.html
- Health Canada GUI-0050  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/annex-11-guide-computerized-systems-gui-0050.html
- Health Canada GUI-0069  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/guidelines-temperature-control-drug-products-storage-transportation-0069.html
- FDA Part 11 Scope and Application guidance  
  https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application
- 21 CFR Part 11  
  https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- ISPE GAMP 5 Second Edition — industry guidance; copyrighted guide text is not reproduced here.

## 15. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft | Initial set of 35 testable user requirements. |

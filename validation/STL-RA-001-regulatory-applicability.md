# STL-RA-001 — Regulatory Applicability Statement

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-RA-001 |
| Title | Regulatory Applicability Statement |
| System | SampleTrack Lite |
| Document status | Draft |
| Jurisdictional scenario | Canadian GMP warehouse/distribution operation |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This statement defines the regulatory and guidance framework used to design the SampleTrack Lite mock validation package.

Its purpose is to prevent three common errors:

1. treating guidance as though it were legislation;
2. treating an international or U.S. requirement as automatically legally applicable to a Canadian scenario;
3. citing a control without explaining which regulated use or record makes the control relevant.

This is an educational applicability assessment, not legal advice or a real establishment's regulatory determination.

## 2. Applicability decision summary

The package uses the following hierarchy:

| Source | Use in this mock package | Applicability posture |
|---|---|---|
| Food and Drugs Act / Food and Drug Regulations, Part C Division 2 | Underlying Canadian GMP framework for the fictional drug warehouse/distribution setting | Primary regulatory basis |
| Health Canada GUI-0001 | Interpretation of Canadian GMP expectations, including wholesaler computerized systems, records, inventory/status, storage, excursions, and recalls | Primary Canadian guidance |
| Health Canada GUI-0050, Annex 11 to the GMP Guide: Computerized Systems | Computerized-system lifecycle, risk, validation, system description, URS, traceability, audit trail, security, e-signatures, backup/restore and related controls | Primary computerized-systems guidance |
| Health Canada GUI-0069 | Receiving, storage/environmental controls, temperature monitoring, excursion investigation and distribution-chain records | Primary process-specific guidance |
| GAMP 5 Second Edition | Risk-based lifecycle and configured-product validation approach | Industry guidance; not law |
| EU/PIC/S Annex 11 concepts | Harmonized computerized-system reference; principally represented here through Health Canada's GUI-0050 | Supporting reference |
| 21 CFR Part 11 | Selected electronic-record/e-signature control set included to demonstrate awareness of U.S. expectations | Conditional exercise overlay; U.S. legal applicability is not asserted |

## 3. Canadian GMP basis

### 3.1 Health Canada GUI-0001

Health Canada's **Good manufacturing practices guide for drug products (GUI-0001)** interprets Part C, Division 2 of the Food and Drug Regulations.

For the fictional warehouse/distribution scenario, the guide is particularly relevant because Health Canada's published interpretation states that wholesalers need to validate computerized systems used for GMP activities and identifies quality-system functions including:

- tracking customer orders and distribution to support recall;
- material status control;
- stock/inventory accountability;
- expiry-date control;
- storage/environmental control;
- temperature excursions, alarms, and notifications;
- returned-drug processing;
- complaint handling.

The same interpretation explains that, when computerized or automated systems control and maintain quality-system functions, the system must provide and maintain data integrity so regulatory record requirements can be met.

**Package consequence:** SampleTrack Lite is treated as GxP-relevant because it controls or records inventory status, storage/location, excursion handling, chain of custody, disposition, and related electronic records.

Reference: Health Canada, GUI-0001:
https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/gmp-guidelines-0001/document.html

### 3.2 Health Canada GUI-0050 / computerized systems

Health Canada's **Annex 11 to the good manufacturing practices guide: Computerized Systems (GUI-0050)** applies to computerized systems used as part of GMP-regulated activities.

The guide states that the application should be validated and IT infrastructure should be qualified.

Relevant controls for this package include:

- lifecycle risk management based on patient safety, data integrity, and product quality;
- defined responsibilities among process owner, system owner, IT, suppliers, and service providers;
- validation documentation covering relevant lifecycle steps;
- deviation reporting;
- a system description for critical systems;
- URS based on GMP impact and documented risk;
- lifecycle traceability;
- supplier assessment;
- test scenarios including parameter limits, data limits, and error handling;
- secure data storage and tested backup/restore;
- risk-based GMP audit trails;
- controlled configuration/change management;
- security and access control;
- incident management;
- electronic signatures;
- business continuity and archiving.

**Package consequence:** GUI-0050 is the primary computerized-system guidance used to structure the validation plan, system description, URS, risk assessment, OQ, deviation handling, traceability, and final report.

Reference:
https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/annex-11-guide-computerized-systems-gui-0050.html

### 3.3 Health Canada GUI-0069 / storage and transportation

Health Canada's **Guidelines for environmental control of drugs during storage and transportation (GUI-0069)** apply to parties involved in drug storage and transportation, including wholesalers.

The guide addresses:

- labelled storage conditions;
- environmental monitoring;
- temperature alarms and excursion notification;
- receiving checks;
- controlled transfer to appropriate storage;
- investigation of excursions or damaged shipments;
- evidence-based decisions on affected stock;
- storage and transportation records;
- quality-risk management proportional to product risk.

**Package consequence:** SampleTrack Lite's excursion, hold/status, receiving, location, record-retention, and disposition requirements will be designed to support the controlled process. The application will not be portrayed as replacing scientific stability assessment or environmental qualification.

Reference:
https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/guidelines-temperature-control-drug-products-storage-transportation-0069.html

## 4. GAMP 5 Second Edition

GAMP 5 is used as industry guidance for a scalable, risk-based computerized-system lifecycle.

The exercise uses GAMP concepts to:

- define intended use before test design;
- scale validation effort according to risk;
- distinguish configured product from custom development;
- leverage supplier activity where justified rather than mechanically repeating it;
- maintain traceability between requirements, risk, verification, and final disposition;
- treat configuration as a controlled lifecycle object.

The fictional product is treated as a **Category 4 configured product** for scenario design because regulated-company behavior is assumed to be achieved through configuration of a supplier-maintained base product rather than modification of supplier source code.

This categorization does not itself establish compliance, criticality, or validation depth.

Reference: ISPE, *GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems, Second Edition*.

## 5. EU / PIC/S Annex 11 posture

The repository owner is studying EU Annex 11. For this Canadian mock package, direct European legal applicability is not asserted.

Health Canada's GUI-0050 provides the principal Annex 11-style computerized-system framework used here. Where EU/PIC/S Annex 11 concepts are discussed separately, they are treated as harmonization/background references rather than an additional Canadian legal basis.

## 6. 21 CFR Part 11 applicability posture

### 6.1 Why Part 11 is not labelled automatically applicable

FDA's current Part 11 scope guidance ties Part 11 to electronic records and signatures that are required by FDA predicate rules, or that are submitted to FDA under relevant laws and regulations.

Whether a particular record is a Part 11 record therefore depends on the underlying FDA-regulated activity and the organization's actual reliance on the electronic record.

The fictional operating context for SampleTrack Lite is Canadian. The mock package does not establish an FDA predicate-rule obligation for the fictional records.

Accordingly, the package must not state simply:

> "SampleTrack Lite is subject to 21 CFR Part 11."

or:

> "SampleTrack Lite is Part 11 compliant."

### 6.2 How Part 11 is used in the exercise

Part 11 is included as a **conditional design and test overlay** so that the URS and OQ can exercise controls commonly expected when regulated electronic records and electronic signatures are relied upon.

The package will draw from relevant controls including:

- validation / intended performance for closed systems;
- accurate and complete record copies;
- record protection and retrieval;
- access limited to authorized individuals;
- computer-generated, time-stamped audit trails where appropriate;
- operational and authority checks;
- signature manifestations;
- permanent signature/record linkage;
- unique electronic signatures;
- electronic-signature components and controls;
- identification-code/password controls.

The exercise will treat the relevant SampleTrack electronic records as authoritative application records **for test design purposes**. That does not convert the fictional Canadian operation into an FDA-regulated operation.

Primary references:

FDA, *Part 11, Electronic Records; Electronic Signatures — Scope and Application*:
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application

Electronic Code of Federal Regulations, 21 CFR Part 11:
https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11

## 7. Record-level applicability for the mock exercise

| Electronic record / action | Canadian GMP relevance | Part 11 exercise overlay |
|---|---|---|
| Receiving record | Yes; supports receipt, traceability, storage and inventory control | Apply electronic-record controls for demonstration |
| Inventory status | Yes; supports quarantine/release/reject/recall control | Apply access, authority, audit-trail and record-integrity controls |
| Storage location | Yes; supports inventory accountability and controlled storage | Apply record-integrity and auditability controls where changed |
| Chain-of-custody event | Yes; supports traceability and accountability | Apply attribution, timestamp, access and auditability controls |
| Temperature-excursion record | Yes; supports investigation and affected-stock control | Apply record-integrity, auditability and retrieval controls |
| QA disposition | Yes; affects controlled material status | Apply authority and signature controls |
| Audit-trail event | Yes; supports reconstruction of GMP-relevant changes | Apply selected Part 11 audit-trail expectations |
| Electronic approval/signature | Yes where used as a regulated approval record | Apply signature manifestation, uniqueness and record-linkage controls |

## 8. Infrastructure and supplier boundary

GUI-0050 distinguishes application validation from IT infrastructure qualification and expects supplier/service-provider responsibilities to be controlled.

The initial mock package validates neither a real infrastructure stack nor a real supplier.

Instead:

- infrastructure qualification is recorded as a real-world prerequisite/out-of-scope dependency;
- supplier assessment is described in the Validation Plan as required in a real implementation;
- the fictional supplier/product assumption is sufficient only for this demonstration package;
- no supplier-quality claim will be made from invented evidence.

## 9. Regulatory design decisions carried into later documents

The following decisions govern the next deliverables unless later evidence justifies a controlled change:

1. **Canadian GMP is primary.**
2. **GUI-0050 is the primary computerized-system guidance.**
3. **GUI-0069 drives the receiving/storage/excursion process controls.**
4. **GAMP 5 drives the risk-based lifecycle method, not legal applicability.**
5. **Part 11 controls are intentionally included, but FDA jurisdiction is not asserted.**
6. **The system is treated as configured-product Category 4 for the exercise only.**
7. **Electronic records in the defined SampleTrack workflow are treated as authoritative for test design.**
8. **Actual infrastructure qualification, supplier audit, environmental qualification, and scientific excursion assessment are outside the initial application-validation claim.**

## 10. Reassessment triggers

Regulatory applicability should be reconsidered if the scenario changes materially, including if:

- the fictional business process is expanded into U.S. FDA-regulated operations;
- a specific FDA predicate rule is introduced;
- the authoritative record changes from electronic to paper or to a hybrid model;
- an EU establishment or EU regulatory use is added;
- automated interfaces are introduced;
- the system begins performing actual batch certification/release;
- controlled-substance functionality is added;
- the demonstration surrogate is incorrectly substituted for the fictional configured product.

## 11. Non-claims

This statement does not establish legal compliance with Canadian, U.S., or EU requirements.

It does not establish that the complete set of requirements for any actual McKesson system or site has been identified.

Its function is to define a defensible regulatory basis for the mock validation exercise and to keep later requirements and test claims within that boundary.

## 12. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft | Initial regulatory-applicability assessment for Canadian warehouse/distribution mock scenario. |

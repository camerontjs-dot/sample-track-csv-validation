# STL-SD-001 — SampleTrack Lite System Description and Intended Use

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-SD-001 |
| Title | SampleTrack Lite System Description and Intended Use |
| System | SampleTrack Lite |
| Document status | Draft |
| Validation scenario | Fictional configured product |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This document defines the intended use, GxP context, system boundary, principal functions, users, regulated records, interfaces, assumptions, and explicit exclusions for the fictional **SampleTrack Lite** computerized system.

It establishes the system object that the remaining mock validation package will evaluate. It does not establish that the system is validated.

## 2. Intended use

SampleTrack Lite is intended to support controlled receipt, identification, storage-location assignment, status control, chain-of-custody recording, temperature-excursion handling, and quality disposition of pharmaceutical samples or inventory in a GMP warehouse/distribution setting.

Within the mock scenario, authorized users rely on SampleTrack Lite to:

- create and maintain receiving records for incoming material;
- identify material by a unique system record and relevant lot/batch information;
- assign and update approved storage locations;
- maintain controlled inventory status such as **Quarantine**, **Released**, **On Hold**, **Rejected**, **Returned**, or **Recalled**;
- record custody transfers and the responsible user;
- record or receive temperature-excursion information and place affected material into an appropriate restricted status pending assessment;
- document quality review and disposition decisions;
- maintain an audit trail of GMP-relevant record changes;
- associate defined approval actions with an electronic signature;
- retrieve human-readable regulated records and their associated history.

SampleTrack Lite is intended to support these activities. It does not replace the regulated organization's responsibility to define storage conditions, assess product impact, approve dispositions, maintain procedures, train personnel, or operate an appropriate pharmaceutical quality system.

## 3. Business and GxP context

The mock operating context is a Canadian pharmaceutical warehouse or distribution operation that receives and stores drug products or samples under defined environmental conditions.

The system supports functions that can affect:

- the ability to locate and account for regulated inventory;
- the segregation and status control of material;
- the ability to identify material affected by an excursion or other quality event;
- traceability of custody and handling;
- the integrity and retrievability of regulated records;
- the evidence available to support investigation, disposition, complaint, return, and recall activities.

Failure of these functions could affect product quality decisions, record integrity, or the ability to execute an effective recall. The system is therefore treated as GxP-relevant within this mock scenario.

## 4. System classification assumption

For this exercise, SampleTrack Lite is treated as a **configured commercial product** consistent with a GAMP 5 Category 4 scenario.

The exercise assumes that:

- a supplier develops and maintains the base application;
- the regulated company does not modify supplier source code;
- the regulated company configures defined application behavior such as user roles, workflow/status values, storage locations, excursion thresholds, and approval settings;
- supplier documentation and supplier quality information would be assessed in a real implementation.

This classification is an exercise assumption used to select an appropriate validation approach. GAMP software categories are industry guidance concepts rather than regulatory classifications.

If a custom Python implementation is later added to this repository, it will be treated as a **demonstration surrogate** for test execution and not as the Category 4 product described here.

## 5. System boundary

### 5.1 In scope

The validation scenario includes the application behavior needed to:

1. authenticate a user;
2. apply configured role-based permissions;
3. create and modify receiving/inventory records;
4. maintain unique record identity;
5. assign storage location;
6. manage controlled material status;
7. record chain-of-custody events;
8. record temperature-excursion information;
9. place affected material into a controlled hold/review state;
10. document quality assessment and disposition;
11. generate and retain GMP-relevant audit-trail events;
12. apply electronic approval/signature controls to defined quality actions;
13. retrieve and export human-readable records and associated history.

### 5.2 Outside the application-validation scope

The following are not established by this mock package unless a later deliverable explicitly adds bounded evidence:

- qualification of real server, network, cloud, workstation, or database infrastructure;
- supplier quality-system audit;
- source-code review of a commercial product;
- cybersecurity certification or penetration testing;
- validation of temperature sensors, data loggers, refrigerators, freezers, or warehouse HVAC;
- temperature mapping of a real storage area;
- scientific determination of product stability during an excursion;
- ERP, WMS, transport-management, laboratory, regulatory, or financial-system integration;
- real production backup, disaster-recovery, or business-continuity infrastructure;
- real organizational training or SOP effectiveness;
- legal certification of electronic signatures to a regulator;
- use for controlled substances;
- actual batch release by an Authorized Person;
- production deployment.

These exclusions do not imply that the functions are unimportant in a real implementation. They define what this exercise does and does not claim.

## 6. Conceptual process flow

```text
Receive material
      |
      v
Create receiving / inventory record
      |
      v
Verify identity, lot and required storage condition
      |
      v
Assign controlled storage location and status
      |
      +------------------------------+
      |                              |
      v                              v
Normal handling                Temperature excursion
      |                              |
      v                              v
Custody / location update       Flag affected material
      |                              |
      v                              v
Continue controlled state       Place on Hold / review
                                     |
                                     v
                              Quality assessment
                                     |
                       +-------------+-------------+
                       |                           |
                       v                           v
                    Release                    Reject / other
                       |                           |
                       +-------------+-------------+
                                     |
                                     v
                          Retain record + audit history
```

## 7. User roles

### 7.1 Warehouse Operator

Typical authorized activities:

- create receiving records;
- enter lot/batch and storage information;
- assign or update permitted storage locations;
- perform permitted custody transfers;
- enter excursion observations or acknowledge an externally provided excursion event;
- view material status and applicable handling restrictions.

The Warehouse Operator is not authorized to perform quality disposition or administer user access.

### 7.2 QA Reviewer

Typical authorized activities:

- review inventory and excursion records;
- assess records supporting a quality decision;
- apply or approve defined status/disposition transitions;
- enter required rationale;
- apply an electronic approval/signature where configured;
- review relevant audit-trail information.

### 7.3 System Administrator

Typical authorized activities:

- create, disable, or administer user accounts;
- assign configured roles;
- maintain permitted application configuration within controlled procedures.

The System Administrator is not assumed to have authority to make QA disposition decisions merely because the role has technical administrative privileges. Segregation between technical administration and quality decision authority will be considered in the URS and risk assessment.

## 8. Principal functions

### 8.1 Receiving and record creation

The application creates a unique electronic record for received material and captures the minimum data required by the configured process.

Expected data may include:

- SampleTrack record ID;
- product/material identifier;
- lot or batch number;
- quantity or sample count where applicable;
- receipt date/time;
- received-by user;
- required storage condition;
- initial material status;
- assigned storage location;
- shipment or source reference where applicable.

### 8.2 Storage location and inventory status

The application maintains the current configured storage location and controlled status of each in-scope record.

Status transitions should be constrained so that users cannot bypass required quality review or place affected material into an unrestricted state without appropriate authority.

### 8.3 Chain of custody

The system records custody or responsibility transfers relevant to the warehouse process.

A custody event should preserve sufficient information to determine what record was affected, the prior and new responsible state where applicable, who performed the action, and when it occurred.

### 8.4 Temperature excursions

The application supports identification and management of material potentially exposed outside a defined storage condition.

The system does not determine pharmaceutical stability. Its intended role is to:

- identify that an excursion condition exists;
- associate the condition with affected material;
- preserve relevant event information;
- prevent inappropriate unrestricted disposition while assessment is pending;
- record the resulting quality decision.

### 8.5 Audit trail

The system maintains a system-generated history for GMP-relevant creation, modification, status, custody, and approval events as defined by risk.

The validation package will distinguish between proving that an audit-trail mechanism exists and proving that it captures the specific information required for the intended use.

### 8.6 Electronic approvals/signatures

Defined quality-review or disposition actions may require an electronic signature.

Where used in the mock scenario, the signature is intended to remain linked to the associated electronic record and to identify the signer, signing date/time, and meaning of the signing action.

### 8.7 Retrieval and human-readable output

Authorized users can retrieve records needed for review, investigation, traceability, and inspection-like examination.

The exercise will verify bounded human-readable retrieval/export behavior. It will not claim long-term archive performance beyond the tested demonstration conditions.

## 9. Regulated data and electronic records

The following record types are treated as GxP-relevant within the exercise:

| Record / data object | GxP relevance |
|---|---|
| Receiving record | Establishes receipt, identity, and initial controlled state. |
| Inventory status | Prevents inappropriate use/distribution and supports recall/segregation. |
| Storage location | Supports retrieval, segregation, and inventory accountability. |
| Chain-of-custody event | Establishes handling history and responsibility. |
| Temperature-excursion record | Supports investigation and identification of potentially affected material. |
| Quality assessment/disposition | Records the decision affecting material availability or rejection. |
| Audit-trail event | Preserves history of GMP-relevant changes. |
| Electronic signature/approval record | Attributes defined review/approval actions to an identified user. |

These electronic records are treated as the authoritative application records for the mock workflow.

## 10. Conceptual architecture and data flow

The package does not depend on a particular commercial technology stack.

For validation purposes, the conceptual system consists of:

```text
Authorized user
    |
    v
SampleTrack Lite application
    |
    +--> authentication / authorization controls
    |
    +--> configured workflow and status rules
    |
    +--> regulated application records
    |
    +--> audit-trail records
    |
    +--> electronic approval/signature records
    |
    +--> human-readable retrieval/export
```

No external production interface is assumed for the initial package.

A later demonstration surrogate may implement these behaviors locally for execution evidence, but that implementation will not alter the fictional product boundary.

## 11. Interfaces

### 11.1 Initial validation package

The initial scenario assumes manual entry of required receiving and excursion information and no automated upstream/downstream integrations.

This keeps the first validation claim focused on application behavior rather than data-interface validation.

### 11.2 Future optional interfaces

Potential interfaces such as temperature-monitoring systems, ERP/WMS platforms, barcode scanners, or identity providers are outside the initial scope.

Adding any such interface would require review of data ownership, transfer controls, failure modes, and traceability.

## 12. Security and access-control boundary

SampleTrack Lite is treated as a controlled-access system.

The validation package is expected to address:

- unique user identity;
- authentication;
- role-based authorization;
- restriction of quality decisions to authorized roles;
- restriction of user/role administration;
- attribution of GMP-relevant actions to an identified user;
- auditability of relevant changes.

The package does not establish a broad cybersecurity claim.

## 13. Data integrity considerations

The system is expected to preserve the content and meaning of its regulated electronic records across normal creation, modification, review, and retrieval.

Risk assessment and URS development will consider at least:

- unauthorized modification;
- loss of prior values/history;
- missing or misleading timestamps;
- incorrect user attribution;
- incomplete excursion or disposition records;
- inability to retrieve required information;
- inappropriate status transition;
- broken linkage between approval/signature and the associated record.

## 14. Assumptions and dependencies

This initial system description assumes:

1. the mock organization has approved procedures defining receiving, storage, excursion assessment, status control, and disposition;
2. storage conditions and excursion limits are scientifically established outside SampleTrack Lite;
3. users receive appropriate procedural training;
4. infrastructure services required by a real deployment would be separately qualified or otherwise controlled;
5. system configuration is managed through change control in a real implementation;
6. supplier assessment would be performed before regulated reliance on a real configured product;
7. the application clock/time source is appropriately controlled in a real deployment;
8. backup and restore controls would be established for a real production environment.

Where an assumption materially affects a later verification claim, it should either be tested, made a prerequisite, or retained as an explicit limitation.

## 15. Intended-use limitations and non-claims

This document does **not** claim that:

- SampleTrack Lite exists as a commercial product;
- the application is validated;
- the mock package satisfies every requirement applicable to a real McKesson or other pharmaceutical operation;
- Category 4 classification alone determines validation effort;
- compliance with 21 CFR Part 11 has been established;
- Health Canada, FDA, the European Commission, ISPE, or any employer has reviewed or endorsed the package;
- the repository owner has previously authored or owned a production computerized-system validation program.

The intended claim is narrower: this repository defines and will exercise a fictional, risk-based CSV scenario using recognizable pharmaceutical validation practices and explicitly bounded evidence.

## 16. Related package documents

- STL-RA-001 — Regulatory Applicability Statement
- SampleTrack Lite Mock CSV Package Plan
- Future: STL-VP-001 Validation Plan
- Future: STL-URS-001 User Requirements Specification
- Future: STL-RSK-001 Risk Assessment
- Future: STL-RTM-001 Requirements Traceability Matrix
- Future: STL-OQ-001 Operational Qualification
- Future: STL-DL-001 Validation Deviation Log
- Future: STL-VSR-001 Validation Summary Report

## 17. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft | Initial mock system description and intended-use boundary. |

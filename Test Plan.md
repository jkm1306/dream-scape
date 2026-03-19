# Test Plan Document
## DreamScape — Study Abroad & Travel Platform

| Field | Detail |
|---|---|
| **Document Title** | Software Quality Assurance Test Plan |
| **Project Name** | DreamScape |
| **Version** | 1.0 |
| **Prepared By** | Student 1 |
| **Date** | 19 March 2026 |
| **Status** | Draft |

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Scope and Objectives](#2-scope-and-objectives)
3. [Testing Strategy](#3-testing-strategy)
4. [Testing Techniques](#4-testing-techniques)
5. [Test Environment](#5-test-environment)
6. [Entry and Exit Criteria](#6-entry-and-exit-criteria)
7. [Roles and Responsibilities](#7-roles-and-responsibilities)
8. [Risks and Mitigations](#8-risks-and-mitigations)

---

## 1. Introduction

### 1.1 Purpose

This document defines the Test Plan for the **DreamScape** web application. It provides a structured approach for verifying that the system meets its functional, non-functional, and security requirements before release.

### 1.2 Project Overview

DreamScape is a full-stack Django 5.2 web application that:
- Connects aspiring students with international **scholarship and study-abroad** opportunities in Poland, Northern Cyprus, and Denmark.
- Helps travelers discover **tourist destinations** across Zambia, Ghana, Eswatini, Zimbabwe, China, Dubai, and Nigeria.
- Provides **user account management** (email-based authentication, user profiles).
- Allows community **testimonials** with admin moderation.
- Features a **dynamic content system** (admin-managed carousel, media uploads).

### 1.3 References

| Reference | Document |
|---|---|
| IEEE 829 | Standard for Software Test Documentation |
| Project README | [dream-scape/README.md](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/README.md) |
| Django Documentation | https://docs.djangoproject.com/en/5.2/ |
| Project Requirements | [requirements.txt](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/requirements.txt) |

---

## 2. Scope and Objectives

### 2.1 Objectives

The primary objectives of testing the DreamScape application are:

1. **Verify Functional Correctness** — Confirm that all features (user registration, login/logout, scholarship applications, travel inquiries, testimonials, and content browsing) work as specified.
2. **Ensure Data Integrity** — Validate that data submitted through forms is correctly stored, retrieved, and displayed from the SQLite database.
3. **Validate Security** — Confirm that protected pages enforce authentication, that unauthorized actions are prevented, and that form inputs are sanitised against injection attacks.
4. **Assess Usability** — Verify that the user interface is intuitive, forms auto-populate correctly, and navigation flows are logical.
5. **Evaluate Performance** — Ensure pages load within acceptable time limits under expected user loads.

### 2.2 In Scope

The following modules and features are within the scope of this test plan:

#### 2.2.1 User Management Module (`users` app)
| Feature | Description |
|---|---|
| User Registration | New users can sign up using email and password |
| User Login | Authenticated access using email-based login |
| User Logout | Session termination and redirect to homepage |
| Profile Dashboard | Logged-in users can view their submitted applications, inquiries, and testimonials |

#### 2.2.2 Student Services Module (`student_travel` app — Student Features)
| Feature | Description |
|---|---|
| Student Destinations Listing | Browse all study-abroad destinations with images, tuition fees, and scholarship info |
| Student Destination Detail | View a specific country detail page including partner schools and galleries |
| Scholarship Application Form | Submit an application with personal details, study level, country preference, and course of interest |
| Application Pre-fill | Authenticated users have form fields pre-populated with their profile data |
| Country Pre-selection | Form pre-selects the country when navigated from a destination page |

#### 2.2.3 Tourist Services Module (`student_travel` app — Tourist Features)
| Feature | Description |
|---|---|
| Tourist Destinations Listing | Browse tourist destinations with rich descriptions and image galleries |
| Tourist Destination Detail | View an individual destination with attraction sites |
| Travel Inquiry Form | Submit a travel inquiry with dates, group size, and destination preferences |
| Smart Pre-filling | Forms auto-populate destination and attraction info from browsing context |

#### 2.2.4 Services & Content Module (`services` app)
| Feature | Description |
|---|---|
| Homepage | Display hero carousel, service highlights, and navigation |
| Testimonials List | Read community-approved testimonials with ratings |
| Submit Testimonial | Logged-in users can submit testimonials for admin moderation |
| Admin Panel | Admin users can manage all content (destinations, schools, carousel, testimonials) |

#### 2.2.5 Non-Functional Requirements
| Area | Scope |
|---|---|
| Security | CSRF protection, login-required views, input validation |
| Performance | Page response times under standard load |
| Responsiveness | UI renders correctly on desktop and mobile viewports |
| Database | Data persistence across sessions and page reloads |

### 2.3 Out of Scope

The following are **not** covered by this test plan:

- Third-party payment integrations (not present in this application).
- Email delivery/SMTP functionality.
- Penetration testing and advanced security audits.
- Load/stress testing at enterprise scale.
- Browser compatibility testing beyond Chrome and Firefox.
- iOS/Android native mobile application testing.

---

## 3. Testing Strategy

### 3.1 Overall Approach

Testing will follow a **layered strategy**, moving from isolated unit tests upward to full end-to-end validation. The sequence ensures that lower-level defects are resolved before higher-level testing begins, reducing the cost of bug detection.

```
  ┌─────────────────────────────────┐
  │      System / E2E Testing       │  ← Full user flows
  ├─────────────────────────────────┤
  │      Integration Testing        │  ← Module interactions
  ├─────────────────────────────────┤
  │        Unit Testing             │  ← Models, forms, views
  └─────────────────────────────────┘
```

### 3.2 Test Levels

#### Level 1 — Unit Testing

**Goal:** Verify individual components (models, forms, helper methods) in isolation.

| Target | What to Test |
|---|---|
| `users.models.User` | Custom UserManager creates users and superusers correctly; email uniqueness enforced |
| `users.forms.SignUpForm` | Validates required fields, rejects duplicate emails, enforces password rules |
| `student_travel.models.StudentApplication` | [full_name](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#70-73) property returns correct concatenation; [__str__](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#67-69) method |
| `student_travel.models.TouristInquiry` | [full_name](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#70-73) property; [__str__](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#67-69) method |
| `student_travel.forms.StudentApplicationForm` | Pre-population of fields from user object; country pre-selection |
| `student_travel.forms.TouristInquiryForm` | Destination pre-selection; attraction pre-fill; readonly field behaviour |
| `services.models.Testimonial` | Star rating validations; `submitted_by` FK relationship |

**Framework:** Django's built-in test framework (`django.test.TestCase`) using `TestCase` classes.

#### Level 2 — Integration Testing

**Goal:** Verify that modules interact correctly — form submissions reach the database, authenticated sessions pass through views, and redirects work as expected.

| Interaction | What to Verify |
|---|---|
| User Registration → Login | Registered user can immediately log in |
| Login → Profile Dashboard | Profile page correctly filters and displays the logged-in user's data |
| Application Form → Database | Valid submission creates a [StudentApplication](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#7-41) record linked to the submitting user |
| Inquiry Form → Database | Valid submission creates a [TouristInquiry](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/models.py#43-73) record |
| Testimonial Submit → Admin Queue | Submitted testimonial has `is_approved=False` until admin acts |
| URL Query Params → Form Pre-fill | `?country=poland` passed in URL correctly pre-selects the form field |

**Framework:** Django `TestCase` with `Client` for HTTP-level requests.

#### Level 3 — System / End-to-End (E2E) Testing

**Goal:** Validate complete user journeys from the browser's perspective, across all pages and modules.

Key E2E scenarios:

| Scenario ID | Scenario |
|---|---|
| E2E-01 | New visitor registers, logs in, submits a scholarship application, and views it on the profile page |
| E2E-02 | Guest user browses tourist destinations, clicks an attraction, and submits a travel inquiry |
| E2E-03 | Logged-in user submits a testimonial; admin approves it; it appears on the testimonials page |
| E2E-04 | Admin logs into `/admin/`, adds a new student destination with images, and it appears on the destinations page |
| E2E-05 | Unauthenticated user attempts to access the profile page and is redirected to login |

**Framework:** Browser-based manual testing and/or Selenium WebDriver for automated E2E tests.

### 3.3 Types of Testing

| Type | Description | When Applied |
|---|---|---|
| **Functional Testing** | Verify every feature works as per requirements | All test levels |
| **Regression Testing** | Re-run existing tests after any code change to confirm nothing is broken | After every bug fix or feature addition |
| **Boundary Testing** | Test edge cases and limits (e.g., age limits 16–60, group size 1–20) | Unit & Integration |
| **Negative Testing** | Submit invalid, empty, or malicious inputs to confirm proper rejection | Unit & Integration |
| **Security Testing** | Verify CSRF tokens, login-required decorators, and input sanitisation | Integration & System |
| **Usability Testing** | Manually evaluate navigation, form clarity, and responsiveness | System level |
| **Performance Testing** | Measure page load times using Django's DEBUG toolbar or `ab` (Apache Benchmark) | System level |

### 3.4 Test Management

- **Test Cases** will be documented in a separate Test Cases spreadsheet (maintained by the group).
- **Bug Reports** will use a standardised format: Bug ID, Description, Steps to Reproduce, Expected vs. Actual Result, Severity, Status.
- **Severity Levels:** Critical → High → Medium → Low.
- **Tools:** Django Test Runner, SQLite browser for DB verification, browser DevTools.

---

## 4. Testing Techniques

### 4.1 Black-Box Testing Techniques

These techniques focus on the application's **external behaviour** without knowledge of internal code. They are applied primarily at the system and integration levels.

#### 4.1.1 Equivalence Partitioning (EP)

Input data is divided into valid and invalid partitions. One representative value from each partition is tested, reducing the number of test cases while maintaining coverage.

**Example — Scholarship Application: Age Field** (`min=16`, `max=60`)

| Partition | Range | Representative Value | Expected Result |
|---|---|---|---|
| Below minimum (invalid) | < 16 | 10 | Form rejected with validation error |
| Valid range | 16 – 60 | 25 | Form accepted |
| Above maximum (invalid) | > 60 | 75 | Form rejected with validation error |

**Example — User Registration: Email Field**

| Partition | Example | Expected Result |
|---|---|---|
| Valid email | `user@example.com` | Accepted |
| Missing @ symbol | `userexample.com` | Rejected |
| Empty field | `` | Rejected ("This field is required") |
| Already registered email | `existing@user.com` | Rejected ("Email already in use") |

#### 4.1.2 Boundary Value Analysis (BVA)

Tests are designed at the boundary of valid and invalid partitions, where defects are most commonly found.

**Example — Scholarship Application: Age Field**

| Boundary | Value | Expected Result |
|---|---|---|
| Just below minimum | 15 | Rejected |
| At minimum | 16 | Accepted |
| Just above minimum | 17 | Accepted |
| Just below maximum | 59 | Accepted |
| At maximum | 60 | Accepted |
| Just above maximum | 61 | Rejected |

**Example — Tourist Inquiry: Number of People Field** (`min=1`, `max=20`)

| Boundary | Value | Expected Result |
|---|---|---|
| 0 | 0 | Rejected |
| 1 | 1 | Accepted |
| 20 | 20 | Accepted |
| 21 | 21 | Rejected |

#### 4.1.3 Decision Table Testing

Used to test combinations of inputs and conditions that produce different outcomes — especially relevant for form submission logic.

**Example — Student Application Submission Logic**

| Condition | Case 1 | Case 2 | Case 3 | Case 4 |
|---|---|---|---|---|
| User is authenticated | Yes | Yes | No | No |
| Form data is valid | Yes | No | Yes | No |
| **Action: Save application** | ✅ | ❌ | ✅ | ❌ |
| **Action: Link to user account** | ✅ | — | ❌ | — |
| **Action: Show success message** | ✅ | ❌ | ✅ | ❌ |
| **Action: Show validation errors** | ❌ | ✅ | ❌ | ✅ |

#### 4.1.4 State Transition Testing

Models user sessions as a state machine. Used to verify authentication flows and navigation states.

```
[Anonymous] ──register──► [Registered + Logged In]
[Registered] ──login──────► [Logged In]
[Logged In] ──logout──────► [Anonymous]
[Logged In] ──access profile──► [Profile Page]
[Anonymous] ──access profile──► [Redirected to Login]
```

**Test Cases to Derive:**
- TC-ST-01: Anonymous user accesses `/users/profile/` → redirected to `/users/login/`
- TC-ST-02: Logged-in user accesses `/users/profile/` → profile page rendered
- TC-ST-03: User logs out → redirected to homepage; subsequent access to profile redirects to login

#### 4.1.5 Use Case / Scenario-Based Testing

Tests complete user scenarios from start to finish as an end user would experience them.

**Scenario: SC-01 — First-Time Student Applicant**
1. User visits the homepage.
2. User navigates to "Student" section and selects Poland.
3. User clicks "Apply Now" on the Poland destination page.
4. User is redirected to the application form with "Poland" pre-selected.
5. Guest fills out all required fields.
6. User submits the form.
7. **Expected:** Success message displayed; application saved to DB.

**Scenario: SC-02 — Returning Authenticated User**
1. User logs in with registered credentials.
2. User navigates to tourist destinations and selects Zambia.
3. User clicks on Victoria Falls attraction and then "Plan My Trip".
4. Inquiry form opens with "Zambia" as destination and "Victoria Falls" pre-filled.
5. User reviews pre-filled form, adds travel date and group size.
6. User submits the inquiry.
7. **Expected:** Success message; inquiry saved; viewable on profile.

---

### 4.2 White-Box Testing Techniques

These techniques examine the **internal structure and logic** of the source code. Applied primarily at the unit testing level.

#### 4.2.1 Statement Coverage

Ensures every executable statement in a function is executed at least once.

**Target:** [users/views.py](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/users/views.py) — [login_view](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/users/views.py#21-35)
- TC: Valid credentials → `authenticate()` returns user → [login()](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/users/views.py#21-35) called → redirect to home.
- TC: Invalid credentials → `authenticate()` returns `None` → error message added → redirect to login.

**Target:** [student_travel/views.py](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/views.py) — [tourist_inquiry_view](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/views.py#45-81)
- TC: GET request with `attraction` param → `destination_details` pre-filled.
- TC: GET request without params → empty form rendered.
- TC: POST with valid data → object saved → redirect.
- TC: POST with invalid data → form re-rendered with errors.

#### 4.2.2 Branch Coverage

Ensures every decision point (if/else) is evaluated for both `True` and `False` outcomes.

**Target:** [student_travel/forms.py](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/forms.py) — `StudentApplicationForm.__init__`

| Branch | Condition | Test Scenario |
|---|---|---|
| Branch 1a | `user and user.is_authenticated` → True | Logged-in user; expect fields pre-populated |
| Branch 1b | `user and user.is_authenticated` → False | Anonymous user; expect empty fields |
| Branch 2a | `country` is not None | `?country=poland` passed; expect pre-selected |
| Branch 2b | `country` is None | No `country` param; expect no pre-selection |

#### 4.2.3 Path Testing

Tests independent paths through a function to achieve a higher level of structural coverage.

**Target:** [student_travel/views.py](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/views.py) — [student_application_view](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/student_travel/views.py#16-43)

| Path | Conditions | Expected Outcome |
|---|---|---|
| Path 1 | GET request, `country` param present | Form rendered with country pre-selected |
| Path 2 | GET request, no `country` param | Empty form rendered |
| Path 3 | POST, valid form, user authenticated | Application saved with `submitted_by`; redirect |
| Path 4 | POST, valid form, user anonymous | Application saved without user link; redirect |
| Path 5 | POST, invalid form | Form re-rendered with validation errors |

---

### 4.3 Experience-Based Testing

#### 4.3.1 Exploratory Testing

Testers interact with the application freely — without a predefined script — to discover unexpected defects. Especially useful for testing edge cases not considered during formal test design.

**Chartered Exploratory Sessions:**
- Session 1: Try submitting forms with SQL injection strings (e.g., `'; DROP TABLE users; --`) in text fields.
- Session 2: Navigate all pages as an unauthenticated user and verify no protected data is exposed.
- Session 3: Rapidly submit the scholarship application multiple times and verify duplicate passport/NRC numbers are rejected (the `unique=True` constraint).
- Session 4: Test the application on a mobile viewport (375px width) for UI issues.

#### 4.3.2 Error Guessing

Based on experience and knowledge of common web application failure modes, testers deliberately try inputs known to cause issues.

| Suspected Error | Test Input | Module |
|---|---|---|
| Empty required fields | Submit forms with blank mandatory fields | All forms |
| Duplicate unique fields | Submit 2 applications with same `passport_or_nrc` | Student Application |
| Past date submission | Enter a travel date in the past | Tourist Inquiry |
| XSS injection | `<script>alert('xss')</script>` in text fields | All text inputs |
| CSRF attack simulation | Submit a form without a CSRF token | All POST forms |
| Long string overflow | Enter a 1000-character string in a `max_length=150` field | All CharField inputs |

---

## 5. Test Environment

| Component | Detail |
|---|---|
| **Operating System** | Windows 11 |
| **Python Version** | 3.10+ |
| **Django Version** | 5.2.5 |
| **Database** | SQLite 3 ([db.sqlite3](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/db.sqlite3)) |
| **Web Server** | Django Development Server (`runserver`) |
| **Browser** | Google Chrome (latest), Mozilla Firefox (latest) |
| **Test Framework** | `django.test.TestCase` |
| **Base URL** | `http://127.0.0.1:8000/` |
| **Admin URL** | `http://127.0.0.1:8000/admin/` |

---

## 6. Entry and Exit Criteria

### 6.1 Entry Criteria (Testing may begin when:)

- [ ] The application is cloned and runs successfully on the local environment.
- [ ] All database migrations have been applied (`python manage.py migrate`).
- [ ] A superuser account has been created for admin testing.
- [ ] All required dependencies are installed from [requirements.txt](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/requirements.txt).
- [ ] The test plan has been reviewed and approved by the group.

### 6.2 Exit Criteria (Testing is complete when:)

- [ ] All planned test cases have been executed.
- [ ] 100% of critical and high-severity defects have been fixed and re-tested.
- [ ] Minimum **80% test pass rate** has been achieved across all test levels.
- [ ] The test summary report has been completed and signed off.

---

## 7. Roles and Responsibilities

| Role | Responsibility | Assigned To |
|---|---|---|
| **Test Lead (Student 1)** | Develop and maintain this test plan; define scope and strategy | Student 1 |
| **Test Designer** | Write detailed test cases based on this plan | Group Member |
| **Tester** | Execute test cases, log defects, and report results | Group Member |
| **Developer** | Fix reported defects and provide builds for re-testing | Group Member |
| **Review & Approval** | Review test plan and test results | All Group Members |

---

## 8. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| SQLite database file gets corrupted or deleted during testing | Low | High | Keep a backup of [db.sqlite3](file:///c:/Users/Jerome/Documents/School/ZCAS/Courses/Year%203/Sem%202/Software%20Quality%20Assurance%20Testing/Assignment/dream-scape/dream-scape/db.sqlite3) before each test run; use a dedicated test database |
| Changes to models break existing tests | Medium | Medium | Run the full test suite after every code change (regression testing) |
| Forms do not validate all edge cases on the server side | Medium | High | Supplement browser-level tests with direct HTTP POST requests using Django's test `Client` |
| Time constraints limit test coverage | High | Medium | Prioritise critical paths (authentication, form submission) before less critical features |
| Unanticipated UI breakage on mobile viewports | Medium | Medium | Test on multiple viewport sizes using browser DevTools device emulation |

---

*End of Test Plan Document — Version 1.0*

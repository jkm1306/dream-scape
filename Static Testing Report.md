# Static Testing Report & QA Metrics

## DreamScape — Study Abroad & Travel Platform

| Field              | Detail                             |
| ------------------ | ---------------------------------- | --------- |
| **Document Title** | Static Testing Report & QA Metrics |
| **Project Name**   | DreamScape                         |
| **Version**        | 1.0                                |
| <br>               | **Prepared By**                    | Student 1 |
| **Date**           | 19 March 2026                      |
| **Testing Type**   | Static Testing (No code execution) |

---

## Table of Contents

1. [Static Testing Overview](#1-static-testing-overview)
2. [Documentation Review](#2-documentation-review)
3. [GUI Inspection](#3-gui-inspection)
4. [QA Metrics Summary](#4-qa-metrics-summary)
5. [Defect Log](#5-defect-log)

---

## 1. Static Testing Overview

Static testing is the process of examining software artifacts — documentation, source code, templates, and configuration — **without executing the application**. It is performed early in the software development lifecycle to detect defects before they compound.

### 1.1 Activities Performed

| Activity             | Description                                                                                                                      | Technique Used           |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Documentation Review | Evaluated README.md, code comments, forms, models, and views for completeness and accuracy                                       | Checklist-based review   |
| GUI Inspection       | Examined HTML templates visually without browser execution to assess structural correctness, accessibility, and navigation logic | Walkthrough / Inspection |

### 1.2 Artifacts Reviewed

| Artifact              | File                       |
| --------------------- | -------------------------- |
| Project README        | [README.md]                |
| Base Template         | [templates/base.html]      |
| Navbar Template       | [templates/navbar.html]    |
| Footer Template       | [templates/footer.html]    |
| User Model            | [users/models.py]          |
| User Forms            | [users/forms.py]           |
| User Views            | [users/views.py]           |
| Student Travel Models | [student_travel/models.py] |
| Student Travel Forms  | [student_travel/forms.py]  |
| Student Travel Views  | [student_travel/views.py]  |
| Services Models       | [services/models.py]       |
| Services Views        | [services/views.py]        |
| Services Forms        | [services/forms.py]        |
| Root URL Config       | [dream_scape/urls.py]      |
| Users URL Config      | [users/urls.py]            |

---

## 2. Documentation Review

### 2.1 README.md Review

The README is the primary project documentation. It was evaluated for accuracy, completeness, and usefulness.

#### Checklist

| #     | Check Item                                                           | Result  | Finding                                                                          |
| ----- | -------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------- |
| DR-01 | Project name and purpose clearly described                           | ✅ PASS | Clear description with feature list                                              |
| DR-02 | Installation steps are complete and correct                          | ✅ PASS | 6-step setup guide is accurate                                                   |
| DR-03 | Prerequisites clearly listed (Python 3.10+, Git, pip)                | ✅ PASS | Documented correctly                                                             |
| DR-04 | Tech stack is documented                                             | ✅ PASS | Table lists Django 5.2, SQLite, Pillow, DRF, JWT                                 |
| DR-05 | Environment variable configuration documented                        | ✅ PASS | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASES` documented                   |
| DR-06 | All navigation URLs in README match actual URL configs               | ✅ PASS | All 4 URLs (`/`, `/admin/`, `/users/signup/`, `/users/login/`) confirmed in code |
| DR-07 | Project structure diagram matches actual directory structure         | ✅ PASS | All directories and files match                                                  |
| DR-08 | License information present                                          | ✅ PASS | MIT License stated                                                               |
| DR-09 | README mentions tests directory ([tests.py]) or testing instructions | ❌ FAIL | **BUG-01:** No mention of how to run tests; [tests.py] files empty in all apps   |
| DR-10 | Contributing guidelines are clear                                    | ✅ PASS | 5-step Git workflow documented                                                   |

**Documentation Review Score: 9/10 checks passed**

---

### 2.2 Code Comments Review

Code was reviewed across all apps for meaningful inline documentation.

#### `users/` App

| File        | Check                                    | Result     | Finding                                                                                   |
| ----------- | ---------------------------------------- | ---------- | ----------------------------------------------------------------------------------------- |
| [models.py] | Custom UserManager methods documented    | ⚠️ PARTIAL | No docstrings on [create_user] or [create_superuser] methods                              |
| [views.py]  | View functions have docstrings           | ⚠️ PARTIAL | Only [profile_view] has a docstring; [login_view], [signup_view], [logout_view] have none |
| [forms.py]  | Form logic commented                     | ❌ FAIL    | **BUG-02:** [SignUpForm] has no comments explaining the password confirmation logic       |
| [urls.py]   | URL patterns named and ordered logically | ✅ PASS    | All 4 routes named correctly                                                              |

#### `student_travel/` App

| File        | Check                                      | Result     | Finding                                                                                                                                 |
| ----------- | ------------------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [models.py] | Model fields have `help_text` where needed | ✅ PASS    | `preferred_country`, `alt_text`, `slide_type` all have `help_text`                                                                      |
| [models.py] | Model classes have docstrings              | ⚠️ PARTIAL | Only [TouristDestination], [TouristDestinationImage], [AttractionSite], [AttractionSiteImage] have docstrings; student models do not    |
| [views.py]  | Complex logic commented                    | ⚠️ PARTIAL | Good inline comments in [tourist_inquiry_view] but [student_application_view] lacks explanation for the country display name resolution |
| [forms.py]  | Form [__init__] overrides documented       | ❌ FAIL    | **BUG-03:** No comments on why `attraction` field is set to `readonly`; implicit logic                                                  |

#### `services/` App

| File        | Check                                         | Result  | Finding                                                                                                                                                |
| ----------- | --------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [models.py] | `Testimonial.star_display` property commented | ✅ PASS | Logic is self-evident from the property name                                                                                                           |
| [views.py]  | [home()] view inline comments                 | ✅ PASS | Good comments explaining carousel image retrieval logic                                                                                                |
| [admin.py]  | Admin registrations present                   | ❌ FAIL | **BUG-04:** [services/admin.py] contains only a minimal import comment; no models registered in admin despite the testimonial needing admin moderation |

---

### 2.3 Configuration & Security Review

| #     | Check Item                                             | Result  | Finding                                                                                                      |
| ----- | ------------------------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------ |
| SC-01 | `DEBUG = True` in settings (development mode)          | ⚠️ WARN | Acceptable for local dev; README warns against production deployment with `DEBUG=True`                       |
| SC-02 | `ALLOWED_HOSTS = ['*']` in settings                    | ⚠️ WARN | README documents this; should be restricted in production                                                    |
| SC-03 | `SECRET_KEY` hardcoded in settings file                | ⚠️ WARN | Risk in production; README warns about this                                                                  |
| SC-04 | Media and static files served via DEBUG guard          | ✅ PASS | [urls.py] correctly serves media/static only when `DEBUG=True`                                               |
| SC-05 | `@login_required` decorator applied to protected views | ✅ PASS | [profile_view] in [users/views.py] has the decorator                                                         |
| SC-06 | CSRF protection on POST forms                          | ✅ PASS | Django's default CSRF middleware is active (standard Django setup)                                           |
| SC-07 | Wildcard import (`from .models import *`) in views     | ⚠️ WARN | **BUG-05:** [services/views.py] uses `from student_travel.models import *` — risky; could shadow local names |

---

## 3. GUI Inspection

The GUI Inspection examines the HTML templates **structurally** — without running the browser — to assess layout correctness, navigation integrity, accessibility, and semantic HTML quality.

### 3.1 Base Template ([base.html])

| #      | Check Item                                                                       | Result  | Finding                                                                                                                                    |
| ------ | -------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| GUI-01 | `<!DOCTYPE html>` declared                                                       | ✅ PASS | Line 2                                                                                                                                     |
| GUI-02 | `lang` attribute set on `<html>`                                                 | ✅ PASS | `lang="en"`                                                                                                                                |
| GUI-03 | Viewport meta tag present for mobile responsiveness                              | ✅ PASS | `width=device-width, initial-scale=1.0`                                                                                                    |
| GUI-04 | Page title block defined for child templates to override                         | ❌ FAIL | **BUG-06:** Default title reads `"SwiftCart"` — an incorrect leftover from a previous project; should read `"DreamScape"`                  |
| GUI-05 | Flash/alert messages displayed to user                                           | ✅ PASS | Messages loop renders inside `<main>`                                                                                                      |
| GUI-06 | All alert messages use same CSS class (`alert-info`) regardless of message level | ⚠️ WARN | **BUG-07:** All messages rendered with `alert-info` class; error messages (e.g., invalid login) should use `alert-danger` for user clarity |
| GUI-07 | Bootstrap CSS and JS loaded from CDN                                             | ✅ PASS | Bootstrap 5.3.0 CSS and JS bundle included                                                                                                 |
| GUI-08 | Font Awesome CSS included for icons                                              | ✅ PASS | Version 6.0.0-beta3 included                                                                                                               |
| GUI-09 | Google Fonts (Poppins) included                                                  | ✅ PASS | Loaded correctly                                                                                                                           |
| GUI-10 | Favicon linked                                                                   | ✅ PASS | `favicon.ico` referenced via `{% static %}`                                                                                                |
| GUI-11 | Custom CSS file linked                                                           | ✅ PASS | `css/styles.css` linked                                                                                                                    |
| GUI-12 | Navbar and footer correctly included using `{% include %}`                       | ✅ PASS | Both included                                                                                                                              |
| GUI-13 | `<main>` semantic element used for page content                                  | ✅ PASS | Content wrapped in `<main class="container mt-4">`                                                                                         |

---

### 3.2 Navbar Template (navbar.html)

| #      | Check Item                                                            | Result     | Finding                                                                                                                                        |
| ------ | --------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| GUI-14 | Brand name/logo links back to homepage                                | ✅ PASS    | `{% url 'services:home' %}`                                                                                                                    |
| GUI-15 | Logo `<img>` has meaningful `alt` text                                | ✅ PASS    | `alt="DreamScape Logo"`                                                                                                                        |
| GUI-16 | Mobile hamburger toggler has accessibility attributes                 | ⚠️ PARTIAL | **BUG-08:** `aria-label` missing on the `<button class="navbar-toggler">` element; only `aria-controls` and `aria-expanded` present            |
| GUI-17 | Navigation links cover all major sections                             | ✅ PASS    | Home, About, Students, Tourists all linked                                                                                                     |
| GUI-18 | Authentication-aware nav (shows Login/Signup or Profile/Logout)       | ✅ PASS    | `{% if request.user.is_authenticated %}` block correct                                                                                         |
| GUI-19 | Navbar is `fixed-top` (sticky)                                        | ✅ PASS    | `class="... fixed-top"` on `<nav>`                                                                                                             |
| GUI-20 | Body padding accounts for fixed navbar height                         | ✅ PASS    | `padding-top: 80px` with responsive override at 768px                                                                                          |
| GUI-21 | Active nav link highlighted via JS                                    | ✅ PASS    | Script compares `currentPath` to each link's `href`                                                                                            |
| GUI-22 | CSS defined in `<style>` block inside template (inline styles)        | ⚠️ WARN    | CSS and a second `<style>` block for body padding are inside the template rather than the separate `styles.css` file — reduces maintainability |
| GUI-23 | Social media links (if present) open in new tab with `rel="noopener"` | —          | No social links in navbar; N/A                                                                                                                 |
| GUI-24 | User display name truncated safely on mobile                          | ✅ PASS    | `slice:":8"` filter applied on `d-md-none` span                                                                                                |

---

### 3.3 Footer Template (footer.html)

| #      | Check Item                                                         | Result  | Finding                                                                                                                                                               |
| ------ | ------------------------------------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GUI-25 | Footer uses semantic `<footer>` element                            | ✅ PASS | `<footer class="cultural-footer">`                                                                                                                                    |
| GUI-26 | Footer logo has `alt` text                                         | ✅ PASS | `alt="DreamScape Logo"`                                                                                                                                               |
| GUI-27 | All Quick Links point to real URL names                            | ✅ PASS | `services:home`, `services:about`, `student_travel:students`, `student_travel:tourists`                                                                               |
| GUI-28 | Service links under "Our Services" are all functional              | ❌ FAIL | **BUG-09:** "Visa Assistance", "Cultural Orientation", and "24/7 Support" all link to `href="#"` — these are dead/placeholder links with no actual pages              |
| GUI-29 | Copyright year is current (2026)                                   | ❌ FAIL | **BUG-10:** Footer reads `© 2025 DreamScape Agency` — year is outdated                                                                                                |
| GUI-30 | Social media links in footer open in new tab with `rel="noopener"` | ❌ FAIL | **BUG-11:** Facebook, Instagram, Twitter, LinkedIn, WhatsApp social links all use `href="#"` (placeholder) and lack `target="_blank"` and `rel="noopener noreferrer"` |
| GUI-31 | Contact email formatted as a working `mailto:` link                | ✅ PASS | `href="mailto:travelagencydreamscape@gmail.com"`                                                                                                                      |
| GUI-32 | WhatsApp link uses `wa.me` protocol correctly                      | ✅ PASS | `href="https://wa.me/260779396709"` with `target="_blank" rel="noopener"`                                                                                             |
| GUI-33 | Footer is responsive on mobile                                     | ✅ PASS | `@media (max-width: 768px)` rules center-align content correctly                                                                                                      |
| GUI-34 | CSS variables defined in both navbar and footer `<style>` blocks   | ⚠️ WARN | Same CSS variables (`--primary-blue`, `--gold`, etc.) are redefined in both `navbar.html` and `footer.html` — DRY violation; should be in global `styles.css`         |

---

### 3.4 Form & View Logic Inspection

| #      | Check Item                                                                    | Result  | Finding                                                                                                                                                           |
| ------ | ----------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GUI-35 | `SignUpForm` validates password confirmation                                  | ✅ PASS | `clean()` method raises `ValidationError` if passwords don't match                                                                                                |
| GUI-36 | `SignUpForm` enforces minimum password strength                               | ❌ FAIL | **BUG-12:** No minimum length or complexity constraints on the password field — any single-character password is accepted                                         |
| GUI-37 | `StudentApplicationForm` restricts age input with HTML `min`/`max` attributes | ✅ PASS | `min='16', max='60'` set on `NumberInput` widget                                                                                                                  |
| GUI-38 | `TouristInquiryForm` restricts group size                                     | ✅ PASS | `min='1', max='20'` set on `NumberInput` widget                                                                                                                   |
| GUI-39 | `profile_view` catches import errors gracefully                               | ✅ PASS | `try/except` block prevents crash if models don't exist                                                                                                           |
| GUI-40 | `logout_view` uses GET request (no POST-only protection)                      | ⚠️ WARN | **BUG-13:** Logout is accessible via a GET request (`<a href="...logout">`). Best practice is to require a POST request for logout to prevent CSRF logout attacks |
| GUI-41 | Testimonial `Testimonial.submitted_by` is optional (null/blank)               | ✅ PASS | `null=True, blank=True` — anonymous submissions are allowed as designed                                                                                           |
| GUI-42 | `CarouselImage.slide_type` has `unique=True` constraint                       | ✅ PASS | Only one student slide and one tourist slide can exist — correct business logic                                                                                   |
| GUI-43 | `StudentApplication.passport_or_nrc` has `unique=True` constraint             | ✅ PASS | Prevents duplicate applications with same ID number                                                                                                               |

---

## 4. QA Metrics Summary

### 4.1 Test Execution Summary

| Metric                               | Value |
| ------------------------------------ | ----- |
| **Total Inspection Checks Executed** | 47    |
| **Checks Passed (✅)**               | 33    |
| **Checks Passed Partially (⚠️)**     | 9     |
| **Checks Failed (❌)**               | 13    |

> **Note:** "Partial" results indicate checks that were met at a basic level but have quality or maintainability concerns. For pass rate calculations, partials are counted as failures.

### 4.2 Pass / Fail Rate

| Metric        | Calculation   | Result    |
| ------------- | ------------- | --------- |
| **Pass Rate** | 33 ÷ 47 × 100 | **70.2%** |
| **Fail Rate** | 14 ÷ 47 × 100 | **29.8%** |

> Partial results (9 items) classified as failures for conservative measurement.

### 4.3 Defects Found by Area

| Area                     | Checks   | Passed   | Failed (incl. partial) | Defects Logged |
| ------------------------ | -------- | -------- | ---------------------- | -------------- |
| Documentation (README)   | 10       | 9        | 1                      | 1              |
| Code Comments            | 12       | 6        | 6                      | 4              |
| Configuration & Security | 7        | 4        | 3                      | 2 (warnings)   |
| Base Template (GUI)      | 13       | 10       | 3                      | 2              |
| Navbar (GUI)             | 11       | 8        | 3                      | 1              |
| Footer (GUI)             | 10       | 5        | 5                      | 4              |
| Form/View Logic (GUI)    | 9        | 7        | 2                      | 2              |
| **Total**                | **72\*** | **49\*** | **23\***               | **13**         |

> \*Note: Some checks span across multiple areas; the totals shown are based on the individual check items in sections 2 and 3.

### 4.4 Defect Summary by Severity

| Severity      | Count | Description                                                                                                                                                                                         |
| ------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔴 **High**   | 3     | Missing password strength validation (BUG-12), wrong default page title (BUG-06), missing admin registration for Testimonials (BUG-04)                                                              |
| 🟡 **Medium** | 5     | Logout via GET instead of POST (BUG-13), all messages using `alert-info` (BUG-07), dead footer service links (BUG-09), missing accessibility `aria-label` (BUG-08), empty `tests.py` files (BUG-01) |
| 🟢 **Low**    | 5     | Outdated copyright year (BUG-10), placeholder social links (BUG-11), wildcard import (BUG-05), missing form comments (BUG-02, BUG-03)                                                               |

---

## 5. Defect Log

| Bug ID | Severity  | Area          | File                      | Description                                                                             | Recommendation                                                                    |
| ------ | --------- | ------------- | ------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| BUG-01 | 🟡 Medium | Documentation | `README.md`               | No mention of how to run tests; all `tests.py` files empty                              | Add testing section to README; implement at least placeholder tests               |
| BUG-02 | 🟢 Low    | Code Comments | `users/forms.py`          | `SignUpForm` has no comments explaining password confirmation logic                     | Add inline comments explaining the `clean()` override                             |
| BUG-03 | 🟢 Low    | Code Comments | `student_travel/forms.py` | No comment explaining why `attraction` field is set to readonly                         | Add comment: `# Prevent user from editing pre-filled attraction`                  |
| BUG-04 | 🔴 High   | Code/Config   | `services/admin.py`       | `Testimonial` model not registered in Django admin despite requiring admin moderation   | Register `Testimonial` model in `services/admin.py`                               |
| BUG-05 | 🟢 Low    | Code Quality  | `services/views.py`       | Wildcard import `from student_travel.models import *` risks namespace pollution         | Replace with explicit imports: `from student_travel.models import CarouselImage`  |
| BUG-06 | 🔴 High   | GUI - Base    | `templates/base.html`     | Default `<title>` block reads `"SwiftCart"` — wrong project name                        | Change to `"DreamScape"`                                                          |
| BUG-07 | 🟡 Medium | GUI - Base    | `templates/base.html`     | All Django messages rendered with `alert-info`; errors shown in blue instead of red     | Use `{% if message.tags %}` to apply `alert-{{ message.tags }}` class dynamically |
| BUG-08 | 🟡 Medium | GUI - Navbar  | `templates/navbar.html`   | Mobile hamburger `<button>` missing `aria-label` attribute                              | Add `aria-label="Toggle navigation"` to the toggler button                        |
| BUG-09 | 🟡 Medium | GUI - Footer  | `templates/footer.html`   | "Visa Assistance", "Cultural Orientation", "24/7 Support" links all point to `href="#"` | Either implement these pages or remove these links until pages exist              |
| BUG-10 | 🟡 Medium | GUI - Footer  | `templates/footer.html`   | Copyright reads `© 2025 DreamScape Agency` — year is outdated                           | Update to `© 2026` or use `{% now "Y" %}` for dynamic year                        |
| BUG-11 | 🟢 Low    | GUI - Footer  | `templates/footer.html`   | All social media links use `href="#"` (placeholder) and lack `target="_blank"`          | Add real social media URLs, `target="_blank"`, and `rel="noopener noreferrer"`    |
| BUG-12 | 🔴 High   | Form Logic    | `users/forms.py`          | Password field has no minimum length or complexity validation                           | Add `MinLengthValidator` or custom clean method with length check                 |
| BUG-13 | 🟡 Medium | Security      | `users/views.py`          | Logout accessible via GET request — susceptible to CSRF logout                          | Change `logout_view` to require POST; update navbar link to a form button         |

---

_End of Static Testing Report — Version 1.0_

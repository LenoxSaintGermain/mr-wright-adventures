# Mr. Wright Adventures - Resource Management Plan

**Version:** 1.0  
**Last Updated:** October 2025  
**Owner:** Operations Manager

---

## 1. Resource Management Overview

This document outlines the key resources—technology, physical assets, and financial—required to operate Mr. Wright Adventures effectively. The goal is to ensure that our team has the tools and infrastructure needed to deliver a world-class service while maintaining operational efficiency and financial discipline.

---

## 2. Technology Stack

Our technology stack is designed to be scalable, reliable, and integrated, providing a seamless experience for both clients and our internal team. All systems are cloud-based to enable remote access and real-time collaboration.

| System Category | Platform/Tool | Purpose | Access & Credentials | Annual Cost |
|---|---|---|---|---|
| **Core Platform** | **Custom Web App (Flask + React)** | Serves as the primary interface for bookings, client management, and operational dashboards. | **URL:** `[mrwrightadventures.com]`<br>**Admin:** `[admin.mrwrightadventures.com]`<br>**Credentials:** Stored in 1Password | `$1,200 (Hosting)` |
| **Communication** | **WhatsApp Business API** | The central nervous system for all client and team communication, including automated notifications and 24/7 support. | **Dashboard:** `[twilio.com/console]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$600 (Usage-based)` |
| **CRM** | **HubSpot (Starter Plan)** | Manages the entire customer lifecycle, from initial inquiry to post-trip follow-up and re-engagement campaigns. | **URL:** `[app.hubspot.com]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$360` |
| **Payment Gateway** | **Stripe** | Processes all online payments securely, including credit cards and digital wallets. | **Dashboard:** `[dashboard.stripe.com]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `2.9% + $0.30 per transaction` |
| **Flight Tracking** | **FlightAware API** | Provides real-time flight data to automatically track arrivals and proactively manage delays. | **Dashboard:** `[flightaware.com/commercial/aeroapi]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$300` |
| **GPS Tracking** | **Trakm8** | Monitors the real-time location of all transfer vehicles for safety and operational coordination. | **URL:** `[trakm8.com/portal]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$240 per vehicle` |
| **Collaboration** | **Google Workspace** | Provides email (`@mrwrightadventures.com`), shared calendars, and document storage (Google Drive). | **URL:** `[workspace.google.com]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$144 per user` |
| **Knowledge Base** | **Notion** | Central repository for all SOPs, training materials, and this operational manual. Serves as the knowledge base for the future AI assistant. | **URL:** `[notion.so/mrwright]`<br>**Account:** `[EMAIL]`<br>**Credentials:** Stored in 1Password | `$96 per user` |

---

## 3. Physical Resources

Physical assets are essential for maintaining our brand presence and ensuring our team can operate effectively in the field.

#### A. Office & Staging Areas
- **Primary Office (Optional):** A small, centrally located office in San José (e.g., Escazú, Santa Ana) can serve as a hub for management and administrative staff. For a lean start, a fully remote operation is feasible.
- **Airport Staging Areas:** We will not maintain a physical office at SJO or LIR airports. Instead, our Airport Coordinators will operate from designated public areas (e.g., nearby cafes with Wi-Fi) and meet clients at the official arrivals hall meeting points.

#### B. Field Equipment

| Item | Quantity | Assigned To | Purpose | Maintenance Schedule |
|---|---|---|---|---|
| **Company Mobile Phones** | `[#]` | All client-facing staff (Coordinators, Agents) | Provides a dedicated WhatsApp Business line and ensures reliable communication. | Replace every 2 years. |
| **Tablets with Data Plan** | `[#]` | All drivers (owned or partnered) | Used for GPS navigation, receiving job details, and capturing digital signatures for service confirmation. | Replace every 3 years. |
| **Branded Airport Signage** | 4 (2 per airport) | Airport Coordinators | Professional, high-quality signs with the Mr. Wright Adventures logo and a slot for the client's name. | Inspect weekly for wear and tear. Replace as needed. |
| **Driver Welcome Kits** | 1 per vehicle | All drivers | A small kit containing branded water bottles, local snacks, and business cards. | Restock monthly. |
| **Branded Uniforms** | `[#]` | All client-facing staff | Professional polo shirts with the Mr. Wright Adventures logo to ensure easy identification and a polished look. | Replace annually or as needed. |

#### C. Vehicle Fleet (Partner-Operated)
Since we operate an asset-light model, we do not own our vehicle fleet. All vehicles are provided by our vetted transportation partners. However, we enforce strict standards for all partner vehicles.

| Vehicle Type | Minimum Year | Required Features | Capacity | Partner Responsibility |
|---|---|---|---|---|
| **Luxury SUV** | 2022+ | Leather seats, A/C, Wi-Fi, bottled water | 3-4 passengers | Maintain vehicle in immaculate condition; adhere to all maintenance schedules. |
| **Executive Van** | 2022+ | Comfortable seating, A/C, Wi-Fi | 6-12 passengers | Ensure vehicle is clean and commercially insured. |
| **Executive Sedan** | 2023+ | Premium model (e.g., Mercedes E-Class), A/C, Wi-Fi | 2-3 passengers | Driver must be bilingual and have professional driving certification. |

---

## 4. Financial Resources

Prudent financial management is critical for sustainable growth. This section outlines our banking setup, budgeting, and financial controls.

#### A. Banking & Accounts

| Account Type | Institution | Purpose | Authorized Users |
|---|---|---|---|
| **Business Checking** | `[e.g., Banco Nacional de Costa Rica]` | Handles all operational cash flow, including payroll, partner payments, and expenses. | Mr. Wright, Operations Manager |
| **USD Domiciliary Account** | `[e.g., Scotiabank Costa Rica]` | Holds USD funds received from international clients via Stripe to minimize currency conversion fees. | Mr. Wright, Operations Manager |
| **Merchant Account** | **Stripe** | Processes all incoming client payments and manages payouts to our business bank accounts. | Mr. Wright, Technology Lead |
| **Corporate Credit Card** | `[e.g., American Express]` | Used for recurring software subscriptions and approved operational purchases. | Mr. Wright, Operations Manager |

#### B. Budgeting & Financial Controls

- **Annual Budget:** An annual budget will be created and approved by Mr. Wright. The Operations Manager is responsible for tracking monthly spending against this budget.
- **Expense Approval:** All non-recurring expenses over $250 require written approval from Mr. Wright.
- **Monthly Financial Review:** The Operations Manager will conduct a monthly review of all income and expenses, preparing a summary report for Mr. Wright. This includes:
  - Revenue by service type
  - Partner commission payouts
  - Operational costs (payroll, tech, marketing)
  - Profitability analysis
- **Contingency Fund:** 10% of all profits will be allocated to a contingency fund to cover unexpected expenses or business interruptions.

#### C. 90-Day Launch Budget (Example)

| Category | Estimated Cost | Notes |
|---|---|---|
| **Legal & Registration** | $1,500 | Business formation, legal counsel, ICT license application. |
| **Technology Setup** | $1,000 | Initial setup fees, first 3 months of subscriptions. |
| **Branding & Marketing** | $2,500 | Logo design, website content, initial ad spend. |
| **Field Equipment** | $2,000 | Phones, tablets, uniforms, signage. |
| **Initial Payroll** | $9,000 | Salaries for core team for the first 3 months. |
| **Contingency** | $4,000 | 20% of initial budget for unforeseen costs. |
| **Total Launch Budget** | **$20,000** | |

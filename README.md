<div align="center">

# Microsoft 365 Copilot for Excel

[![Course](https://img.shields.io/badge/Course-C34-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html)
[![Duration](https://img.shields.io/badge/Duration-1_day_7_5_instructional_hours-5E5E5E?style=for-the-badge)](#course-toolkit)
[![Labs](https://img.shields.io/badge/Labs-6-34d399?style=for-the-badge)](labs/README.md)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**A connected, hands-on course in Microsoft 365 Copilot for Excel — progress through 6 practical labs from Prepare the Workbook and Create the Copilot Control Trail to Run Advanced Analysis and Write the Verified Decision Summary.**

[📘 Course Page](https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-Microsoft 365 Copilot for Excel.md>) · [🐛 Report Bug](https://github.com/tertiarycourses/C34---Microsoft-365-Copilot-for-Excel/issues) · [💡 Request Feature](https://github.com/tertiarycourses/C34---Microsoft-365-Copilot-for-Excel/issues)

</div>

> [!NOTE]
> **These are the official hands-on lab materials for the commercial course:**
> ### 🎓 Microsoft 365 Copilot for Excel
> **Course Code:** `C34` · by Tertiary Courses / Tertiary Infotech<br>
> **Duration:** 1 day · 7.5 instructional hours<br>
> **Course page:** https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html

---

## Lab Activities

The 6 labs form one connected practical journey. Complete them in order so each verified output can support the activities that follow.

### Topic 1 — Getting Started with Copilot in Excel

| # | Activity | Outcome |
|---:|----------|---------|
| **1** | [Prepare the Workbook and Create the Copilot Control Trail](labs/lab-01-prepare-the-workbook-and-create-the-copilot-control-trail.md) | work-c34/C34-HarbourLight-Copilot-Analysis.xlsx with Raw_Orders, Control and Prompt_Log sheets, a tblOrdersRaw table, baseline counts and a recorded Copilot access note |
| **2** | [Apply Reproducible Highlights, Sorts and Filters](labs/lab-02-apply-reproducible-highlights-sorts-and-filters.md) | An Orders_Working sheet with tblOrdersWorking, reversible highlighting, an explicit multi-level sort, a returned-order filter and Prompt_Log evidence for every applied change |
| **3** | [Generate and Reconcile Formula Columns](labs/lab-03-generate-and-reconcile-formula-columns.md) | Six calculated columns in tblOrdersWorking - Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount, Gross_Profit and Margin_Rate - plus formula checks and reconciled totals on Control |

### Topic 2 — AI-Powered Data Analysis and Insights

| # | Activity | Outcome |
|---:|----------|---------|
| **4** | [Clean and Enrich the Analysis Table](labs/lab-04-clean-and-enrich-the-analysis-table.md) | An Orders_Clean sheet with tblOrdersClean, canonical categories, Month, Return_Flag and Note_Theme fields, plus a cleaning log and before/after control checks |
| **5** | [Build Reconciled PivotTables and Charts](labs/lab-05-build-reconciled-pivottables-and-charts.md) | A Pivot_Analysis sheet with two PivotTables, a monthly regional net-sales line chart, a channel return-rate chart, tie-out cells and a Prompt_Log record for each object |
| **6** | [Run Advanced Analysis and Write the Verified Decision Summary](labs/lab-06-run-advanced-analysis-and-write-the-verified-decision-summary.md) | An Advanced_Analysis sheet with prompt, method, generated output and reconciliation; plus an Executive_Summary sheet with three verified findings, limitations, actions and a final decision |

---

## About

This repository contains the complete lab and courseware package for **Microsoft 365 Copilot for Excel** (**C34**) by Tertiary Courses / Tertiary Infotech. The practical activities build progressively from **Prepare the Workbook and Create the Copilot Control Trail** to **Run Advanced Analysis and Write the Verified Decision Summary**, with explicit checks that help learners verify each result before moving on.

### What you'll learn

- Complete **6 connected hands-on activities** and carry their outputs through one coherent learning journey.
- Practise with **Microsoft 365 Copilot · Microsoft Excel** and the supporting resources supplied in the repository.
- Begin with **Prepare the Workbook and Create the Copilot Control Trail** and finish with **Run Advanced Analysis and Write the Verified Decision Summary**.
- Apply safe data handling, evidence checks and named human review before using AI-generated or automated outputs.

> 📖 **Full walkthrough:** see the [Learner Guide](<LG-Microsoft 365 Copilot for Excel.md>) for the complete course narrative, and [labs/README.md](labs/README.md) for the lab index. Slides, the Learner Guide and the Lesson Plan are in [courseware/](courseware/).

---

## Course Toolkit

| Category | Details |
|----------|---------|
| **Duration** | 1 day · 7.5 instructional hours |
| **Delivery** | Instructor-led, hands-on practical labs |
| **Core tools** | Microsoft 365 Copilot · Microsoft Excel |
| **Practical work** | 6 connected labs with verification steps |
| **Courseware** | PowerPoint and PDF slides, Word and PDF guides, Markdown lab instructions |

---

## Learning Journey

```text
START
  Lab 1    Prepare the Workbook and Create the Copilot Control Trail
     │
     ▼
  Topic 1 — Getting Started with Copilot in Excel
  Labs 1–3
     │
     ▼
  Topic 2 — AI-Powered Data Analysis and Insights
  Labs 4–6
     │
     ▼
FINISH
  Lab 6   Run Advanced Analysis and Write the Verified Decision Summary
```

---

## Project Structure

```text
C34---Microsoft-365-Copilot-for-Excel/
├── README.md
├── LG-Microsoft 365 Copilot for Excel.md
│
├── labs/
│   ├── README.md                 # Start here: complete lab index
│   └── lab-*.md                    # 6 connected practical activities
│
└── courseware/
    ├── *.pptx / *.pdf             # Trainer and learner slides
    ├── LG-*.docx / LG-*.pdf       # Learner Guide
    └── LP-*.docx / LP-*.pdf       # Lesson Plan
```

---

## Getting Started

### Prerequisites

- The accounts and software required for **Microsoft 365 Copilot · Microsoft Excel**. Follow the setup and access notes in each lab.
- A modern web browser and Git for cloning the materials.
- Synthetic or authorised data only. Do not place secrets, personal data or confidential material into an unapproved service.
- A named human reviewer for facts, calculations, decisions and any externally released output.

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C34---Microsoft-365-Copilot-for-Excel.git
cd C34---Microsoft-365-Copilot-for-Excel
```

### 2. Open the lab index

Start with [labs/README.md](labs/README.md), then complete Labs 1–6 in order. Each lab provides the activity context, practical steps and a way to verify the result.

### 3. Keep your connected outputs

Store each lab output in the suggested working folder and retain the evidence or review notes requested by the lab. Later activities depend on these approved outputs.

---

## Contributing

Contributions, corrections and improvements are welcome:

1. **Fork** the repository.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Commit your changes: `git commit -m "Add my improvement"`.
4. Push the branch: `git push origin feature/my-improvement`.
5. Open a **Pull Request**.

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C34---Microsoft-365-Copilot-for-Excel/issues).

---

## License

This material is provided for **educational use** as part of the commercial course **Microsoft 365 Copilot for Excel (C34)**. © Tertiary Infotech Pte. Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Pte. Ltd.** — [Tertiary Courses](https://www.tertiarycourses.com.sg)<br>
Course: [Microsoft 365 Copilot for Excel (C34)](https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html)

## Acknowledgements

- The teams behind Microsoft 365 Copilot · Microsoft Excel.
- Course trainers and learners of C34.

---

<div align="center">

⭐ **If these materials helped you learn Microsoft 365 Copilot for Excel, star the repository!**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[📘 Course Page](https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-Microsoft 365 Copilot for Excel.md>)

</div>

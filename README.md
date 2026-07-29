# C34---Microsoft-365-Copilot-for-Excel

Aligned non-WSQ courseware for:

- Course: Microsoft 365 Copilot for Excel
- Course code: C34
- Duration: 1 day, 7.5 instructional hours
- Version: v1.0
- Effective date: 29 July 2026
- Course page: https://www.tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html

## Package

The package is generated from one source so the slide deck, Learner Guide, Lesson Plan and six labs share the same:

- course identity and version
- learning outcomes
- two-topic sequence
- lab numbers, titles and order
- one-day schedule
- HarbourLight Retail scenario and control totals

Generated artifacts:

- `courseware/Microsoft 365 Copilot for Excel-v1.0.pptx`
- `courseware/Microsoft 365 Copilot for Excel-v1.0.pdf`
- `courseware/LG-Microsoft 365 Copilot for Excel.docx`
- `courseware/LG-Microsoft 365 Copilot for Excel.pdf`
- `courseware/LP-Microsoft 365 Copilot for Excel.docx`
- `courseware/LP-Microsoft 365 Copilot for Excel.pdf`
- `LG-Microsoft 365 Copilot for Excel.md`
- `labs/README.md` and `labs/lab-01-*.md` through `labs/lab-06-*.md`

## Published course materials

- [Trainer Slides — PPT](https://drive.google.com/file/d/1fFywXnVkQq0cc6yN67ADScKe_CoAJOrp/view?usp=sharing)
- [Learner Slides — PDF](https://drive.google.com/file/d/1SyUIuyU4kyHtE0J41s58PYWO6Xk1oFle/view?usp=sharing)
- [Learner Guide — DOCX](https://drive.google.com/file/d/1CBR9r9DKodxSipasR88m7ShA9oKKa-mC/view?usp=sharing)
- [Learner Guide — PDF](https://drive.google.com/file/d/1x3yMv0qtrFUZIYRVH-uCKYqMjSYaSl33/view?usp=sharing)
- [Lesson Plan — DOCX](https://drive.google.com/file/d/1xcNTywl2J6JJHuMNiC4WWpKWyASnZv9j/view?usp=sharing)
- [Lesson Plan — PDF](https://drive.google.com/file/d/1YOmbGQSKejSydpKv5DyotVuRegS0PNh_/view?usp=sharing)
- [Course materials folder](https://drive.google.com/drive/u/0/folders/1CyHHAm7BEZdE3xOY_z91zD8YpSDQ_mXy)

## Single source

Course metadata and concept teaching:

- `.agents/skills/non-wsq-courseware-build/build/course_data.py`

Connected lab definitions:

- `.agents/skills/non-wsq-courseware-build/build/data_domain1.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain2.py`

The build engine also generates the standalone lab Markdown from the same lab definitions before importing those detailed steps into the Learner Guide.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

## Quality gate

Run the automated learner-facing content scan:

```bash
python ".agents/skills/non-wsq-courseware-qa/scan_prohibited.py" .
```

The release is ready only after the generated PDFs are rendered and visually inspected, all six labs pass their structural checks, and the deck, guide, plan and labs agree on every course and lab identifier.

Release v1.0 passed the final automated and independent QA gates on 29 July 2026.

## Authoritative product references

The concept sections cite current Microsoft Support and Microsoft Learn sources, including:

- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions
- https://support.microsoft.com/en-US/Excel/python/introduction-to-python-in-excel
- https://support.microsoft.com/en-US/Excel/python/data-security-and-python-in-excel

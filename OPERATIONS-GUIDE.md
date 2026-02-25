# HR Analytics Fabric Catalog - Operations Guide

**Last Updated:** 2026-02-25
**Status:** Production
**Document Purpose:** Complete reference for future Claude Cowork sessions

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [GitHub Configuration](#2-github-configuration)
3. [Repository Structure](#3-repository-structure)
4. [Data Architecture](#4-data-architecture)
5. [How the HTML App Works](#5-how-the-html-app-works)
6. [How to Make Updates](#6-how-to-make-updates)
7. [Build Scripts](#7-build-scripts)
8. [Python Environment Notes](#8-python-environment-notes)
9. [Key Design Decisions](#9-key-design-decisions)
10. [Pattern Schema Template](#10-pattern-schema-template)
11. [Blueprint Schema Template](#11-blueprint-schema-template)
12. [Quick Reference Commands](#12-quick-reference-commands)

---

## 1. Project Overview

### What This Project Is

The **HR Analytics Fabric Catalog** is a comprehensive collection of tested patterns, best practices, and implementation guidance for building people analytics solutions on Microsoft Fabric. This catalog is specifically designed for HR analytics teams in regulated financial services organizations.

### Who It's For

- **Primary Audience:** HR Analytics teams at regulated financial services organizations
- **Secondary Users:** Data engineers, data scientists, business intelligence teams building on Microsoft Fabric
- **Use Cases:** Building comprehensive people analytics solutions from basic HR dashboards to advanced ML-driven workforce intelligence

### What It Contains

The catalog includes:

- **73 Patterns** - Tested, documented approaches across 8 domain areas with:
  - Implementation complexity assessments (Low/Medium/High)
  - Maturity levels (GA/Preview/Emerging)
  - Governance and compliance considerations
  - Real-world HR analytics use cases
  - Estimated implementation effort
  - Cost implications
  - Pattern dependencies and compatibility

- **8 Use Case Blueprints** - Complete implementation roadmaps combining multiple patterns into cohesive solutions:
  - Workforce Analytics Dashboard (Foundation)
  - Employee Attrition Risk Prediction Pipeline
  - Succession Planning and Career Development Analytics
  - Compensation and Equity Analytics
  - Learning and Development Impact Measurement
  - Operational HR KPI Dashboard
  - GDPR and Data Residency Compliance Pipeline
  - Real-time HR Metrics and Alerts System

- **Interactive HTML App** (`pattern-builder.html`) - Single-file web application with three tabs:
  - Browse Catalog - Explore all patterns by domain
  - Pattern Builder - Construct custom stacks and detect conflicts
  - Use Case Blueprints - Pre-designed implementation paths

- **Streamlit Application** - Alternative Python-based explorer with pattern relationships and dependency visualization

- **4 Word Documents** - Domain-agnostic reference materials:
  - Data Governance Guide
  - Fabric Components Reference
  - AI Model Governance
  - Usage Guide

- **8 Markdown Domain Files** - Detailed documentation for each domain area:
  - 01-data-organization.md
  - 02-transformation-processing.md
  - 03-governance-security.md
  - 04-business-intelligence.md
  - 05-machine-learning.md
  - 06-generative-ai.md
  - 07-alerting-automation.md
  - 08-data-sharing.md

---

## 2. GitHub Configuration

### Repository Details

```
Repository Name:    hr-analytics-fabric-catalog
GitHub Username:    Barlowtech
Repository URL:     https://github.com/Barlowtech/hr-analytics-fabric-catalog
GitHub Pages URL:   https://barlowtech.github.io/hr-analytics-fabric-catalog/pattern-builder.html
Branch:             main
Local Config:       /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/.git/
```

### Git Configuration

The repository is configured with:

```
user.name=Wes Barlow
user.email=wes.barlow@gmail.com
remote.origin.url=https://Barlowtech:<PASTE_BARLOWTECH_PAT_HERE>@github.com/Barlowtech/hr-analytics-fabric-catalog.git
```

### GitHub Pages

The HTML app is automatically published to GitHub Pages when pushed to main. Access it at:
https://barlowtech.github.io/hr-analytics-fabric-catalog/pattern-builder.html

---

## 3. Repository Structure

```
/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/
│
├── README.md                                    # Project overview and quick start
├── OPERATIONS-GUIDE.md                          # This file
├── COMPLETION-REPORT.md                         # Historical completion record
├── research-notes.md                            # Pattern summary by domain
├── execution-log.md                             # Implementation execution log
│
├── patterns.json                                # MASTER DATA: All 73 patterns (4921 lines)
├── blueprints.json                              # MASTER DATA: All 8 blueprints (506 lines)
│
├── pattern-builder.html                         # MAIN APPLICATION: Single-file interactive app (1840 lines)
│
├── .gitignore                                   # Git ignore rules
├── .git/                                        # Version control directory
│
├── docs/
│   ├── pattern-descriptions/                    # Domain-specific documentation
│   │   ├── 01-data-organization.md              # Data Organization and Structuring patterns
│   │   ├── 02-transformation-processing.md      # Data Transformation and Processing patterns
│   │   ├── 03-governance-security.md            # Data Governance and Security patterns
│   │   ├── 04-business-intelligence.md          # Business Intelligence and Reporting patterns
│   │   ├── 05-machine-learning.md               # Machine Learning and Traditional AI patterns
│   │   ├── 06-generative-ai.md                  # Generative AI and Conversational Interfaces patterns
│   │   ├── 07-alerting-automation.md            # Alerting, Automation, and Operational Intelligence patterns
│   │   └── 08-data-sharing.md                   # Data Sharing and Distribution patterns
│   │
│   ├── governance-guide/
│   │   └── data-governance-guide.docx           # Comprehensive governance and compliance reference
│   │
│   ├── fabric-reference/
│   │   └── fabric-components-reference.docx     # Microsoft Fabric components reference
│   │
│   ├── ai-model-governance/
│   │   └── ai-model-governance.docx             # AI model governance best practices
│   │
│   └── usage-guide/
│       └── usage-guide.docx                     # Implementation guidance and usage instructions
│
└── streamlit/
    ├── app.py                                   # Streamlit application (interactive explorer)
    └── requirements.txt                         # Python dependencies
```

### Build Script Locations

The build scripts used to generate and maintain this project are located in the parent directory:

```
/sessions/zen-practical-faraday/
├── build_html.py                                # Builds pattern-builder.html from JSON
├── gen_patterns.py                              # Generates patterns.json with all 73 patterns
├── gen_blueprints.py                            # Generates blueprints.json with all 8 blueprints
├── gen_markdown.py                              # Generates markdown documentation from patterns.json
├── gen_docs.py                                  # Generates Word documents
├── add_patterns.py                              # Utility to add new patterns
├── add_patterns_final.py                        # Final version of pattern addition utility
│
└── pyfix/
    └── sitecustomize.py                         # Python dataclasses compatibility fix
```

---

## 4. Data Architecture

### 4.1 Patterns Schema

Each pattern in `patterns.json` is a JSON object with the following fields:

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | string | Unique identifier (kebab-case, no spaces) | `"medallion-architecture"` |
| `name` | string | Human-readable pattern name | `"Medallion Architecture (Bronze-Silver-Gold)"` |
| `domain` | string | Domain area this pattern belongs to | `"Data Organization and Structuring"` |
| `domainId` | number | Numeric domain identifier (1-8) | `1` |
| `category` | string | Sub-category within domain | `"Lakehouse Architecture"` |
| `summary` | string | Short one-sentence summary | `"Implements a three-layer medallion architecture..."` |
| `description` | string | Detailed description of the pattern | `"The medallion architecture separates raw data..."` |
| `complexity` | string | Implementation complexity: "Low", "Medium", or "High" | `"High"` |
| `maturity` | string | Feature maturity: "GA", "Preview", or "Emerging" | `"GA"` |

#### Content Fields

| Field | Type | Description |
|-------|------|-------------|
| `fabricComponents` | array[string] | Microsoft Fabric components used (Lakehouse, OneLake, Power BI, etc.) |
| `pros` | array[string] | Advantages/benefits of this pattern |
| `cons` | array[string] | Drawbacks/considerations |
| `usageInstructions` | string | Step-by-step implementation instructions |
| `governanceConsiderations` | string | Governance, security, and compliance notes |
| `peopleAnalyticsUseCases` | array[string] | HR-specific use cases demonstrating the pattern |
| `tags` | array[string] | Searchable tags |
| `estimatedImplementationEffort` | string | Effort estimate (e.g., "3-4 weeks", "1 week") |
| `costImplications` | string | Cost considerations and optimization notes |

#### Relationship Fields

| Field | Type | Description |
|-------|------|-------------|
| `compatibleWith` | array[string] | Array of pattern IDs that work well together |
| `incompatibleWith` | array[string] | Array of pattern IDs that conflict with this one |
| `prerequisites` | array[string] | Array of pattern IDs that should be implemented first |

#### Reference Fields

| Field | Type | Description |
|-------|------|-------------|
| `referenceLinks` | array[object] | External documentation links with `label` and `url` properties |

### 4.2 Blueprints Schema

Each blueprint in `blueprints.json` is a JSON object combining multiple patterns:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique blueprint identifier (kebab-case) |
| `name` | string | Human-readable blueprint name |
| `description` | string | Detailed blueprint description |
| `audience` | string | Target audience for this blueprint |
| `patterns` | array[string] | Array of pattern IDs included in blueprint |
| `patternFlow` | array[object] | Recommended sequence with `from`, `to`, and `description` |
| `editableNotes` | string | Customization instructions for organizations |
| `estimatedTotalEffort` | string | Total implementation effort estimate |
| `keyGovernanceRequirements` | array[string] | Governance requirements for this blueprint |
| `tags` | array[string] | Searchable tags |

### 4.3 Domain List with IDs and Colors

The 8 domain areas are assigned numeric IDs and visual colors:

| ID | Domain Name | Color (Hex) | Purpose |
|----|-------------|-----------|---------|
| 1 | Data Organization and Structuring | #3B82F6 (Blue) | Data modeling, lakehouse architecture, storage design |
| 2 | Data Transformation and Processing | #8B5CF6 (Purple) | ETL, data pipelines, transformation logic |
| 3 | Data Governance and Security | #EF4444 (Red) | Access control, compliance, audit trails |
| 4 | Business Intelligence and Reporting | #10B981 (Green) | Dashboards, reports, analytics interfaces |
| 5 | Machine Learning and Traditional AI | #F59E0B (Amber) | Predictive models, ML pipelines, AI integration |
| 6 | Generative AI and Conversational Interfaces | #EC4899 (Pink) | LLMs, RAG, conversational AI, copilots |
| 7 | Alerting, Automation, and Operational Intelligence | #06B6D4 (Cyan) | Monitoring, alerts, automated actions |
| 8 | Data Sharing and Distribution | #14B8A6 (Teal) | Data distribution, APIs, collaboration |

### 4.4 How Patterns Reference Each Other

Patterns can declare relationships using three fields:

#### `compatibleWith` Array

Patterns that work well together and should be combined:

```json
"compatibleWith": [
  "delta-lake-partitioning",
  "onelake-shortcuts",
  "spark-notebook-etl",
  "dataflow-gen2"
]
```

The HTML app will highlight these patterns when you're building a stack.

#### `incompatibleWith` Array

Patterns that conflict or are mutually exclusive:

```json
"incompatibleWith": []
```

The HTML app will warn you if you try to add conflicting patterns.

#### `prerequisites` Array

Patterns that must be implemented first:

```json
"prerequisites": ["medallion-architecture"]
```

The HTML app will suggest prerequisites when building a stack.

---

## 5. How the HTML App Works

### 5.1 Overview

The `pattern-builder.html` is a **single-file, self-contained web application** that:

- Requires no server
- Works offline completely
- Embeds all pattern and blueprint data as JavaScript constants
- Uses vanilla JavaScript (no frameworks like React)
- Renders a modern dark-themed UI with Tailwind CSS-inspired styling
- Exports patterns and stacks as HTML documents and JSON

### 5.2 Three Main Tabs

#### Tab 1: Browse Catalog

- **Purpose:** Explore all 73 patterns with search and filtering
- **Features:**
  - Search by pattern name, description, or summary
  - Filter by domain
  - Filter by complexity (Low/Medium/High)
  - Filter by maturity (GA/Preview/Emerging)
  - Click any pattern to see full details in a modal
  - View compatible/incompatible patterns
  - Export individual pattern as HTML
- **Key Function:** `setupBrowseTab()` initializes filters; `filterPatterns()` applies search/filters; `renderCatalog()` displays results

#### Tab 2: Pattern Builder

- **Purpose:** Construct custom implementation stacks
- **Features:**
  - Drag-and-drop (or click to add) patterns to a working stack
  - Real-time conflict detection (incompatible patterns)
  - Prerequisite suggestions
  - Summary table showing all selected patterns
  - Export as JSON for programmatic use
  - Generate a brief text summary of the stack
  - Print-friendly view of the stack
- **Key Function:** `setupBuilderTab()` initializes interface; `addPatternToStack()` adds pattern; `checkIncompatible()` validates; `exportStackJSON()` exports data

#### Tab 3: Use Case Blueprints

- **Purpose:** View pre-designed implementation paths
- **Features:**
  - Browse all 8 use case blueprints
  - View pattern flow diagram with descriptions
  - See governance requirements
  - Load a blueprint into Pattern Builder to modify
  - Export blueprint as HTML document
  - Jump to individual patterns from blueprint
- **Key Function:** `setupBlueprintsTab()` initializes; `renderBlueprintsGrid()` displays blueprints; `loadBlueprintToBuilder()` populates builder

### 5.3 How Data is Embedded

The build process works as follows:

1. **Python script reads JSON files:**
   ```python
   with open('patterns.json') as f:
       patterns = json.load(f)['patterns']
   with open('blueprints.json') as f:
       blueprints = json.load(f)['blueprints']
   ```

2. **HTML template embeds as JavaScript constants:**
   ```html
   <script>
       const PATTERNS_DATA = [...all 73 patterns...];
       const BLUEPRINTS_DATA = [...all 8 blueprints...];
   </script>
   ```

3. **JavaScript functions access this data directly:**
   ```javascript
   function filterPatterns() {
       return PATTERNS_DATA.filter(p => p.complexity === 'High');
   }
   ```

4. **HTML is generated to `/pattern-builder.html`**

### 5.4 Key JavaScript Functions

Core functions in `pattern-builder.html`:

| Function | Purpose |
|----------|---------|
| `initApp()` | Initializes the application on page load |
| `setupTabs()` | Sets up tab switching functionality |
| `switchTab(tabName)` | Switches between Browse, Builder, and Blueprints tabs |
| `setupBrowseTab()` | Initializes the catalog browser tab |
| `setupFilters()` | Creates domain, complexity, and maturity filter dropdowns |
| `filterPatterns()` | Applies all active filters to pattern list |
| `renderCatalog()` | Renders filtered patterns as clickable cards |
| `showPatternModal(pattern)` | Opens detailed modal for a pattern |
| `exportPatternHTML(pattern)` | Exports pattern as standalone HTML document |
| `setupBuilderTab()` | Initializes the pattern builder tab |
| `renderBuilderPatternList()` | Lists available patterns for builder |
| `addPatternToStack(patternId)` | Adds pattern to current stack |
| `removePatternFromStack(patternId)` | Removes pattern from stack |
| `checkIncompatible(pattern)` | Validates pattern against current stack |
| `updateBuilderStack()` | Updates UI after adding/removing patterns |
| `updateSummaryTable()` | Refreshes summary table in builder |
| `checkWarnings()` | Checks for compatibility warnings |
| `exportStackJSON()` | Exports builder stack as JSON file |
| `generateBrief()` | Creates text summary of stack |
| `printStack()` | Generates print-friendly view |
| `setupBlueprintsTab()` | Initializes blueprints tab |
| `renderBlueprintsGrid()` | Displays blueprint grid |
| `showBlueprintDetail(blueprintId)` | Shows full blueprint details |
| `loadBlueprintToBuilder(blueprintId)` | Loads blueprint patterns into builder |
| `exportBlueprintHTML(blueprintId)` | Exports blueprint as HTML |

### 5.5 Design System

#### Color Palette

```css
/* Background */
--bg-dark: #0F172A;
--bg-darker: #0A0F1E;
--bg-card: #1E293B;

/* Text */
--text-primary: #F8FAFC;
--text-secondary: #94A3B8;
--text-muted: #64748B;

/* Accent */
--accent-blue: #0EA5E9;
--accent-green: #10B981;
--accent-red: #EF4444;
```

#### Typography

- **Font Family:** Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica Neue
- **Heading Font Size:** 1.5rem (h1), 1.25rem (h2)
- **Body Font Size:** 0.95rem, line-height 1.6

#### Component Styling

- Modal overlays with semi-transparent backdrop
- Card-based UI with subtle shadows
- Hover effects for interactivity
- Responsive grid layout for patterns

### 5.6 Export Features

#### Pattern Export

Exports individual pattern as self-contained HTML with styling:

```
Export Format: HTML document
Filename: {pattern-id}-pattern.html
Content: Full pattern details, pros/cons, use cases, references
```

#### Blueprint Export

Exports use case blueprint with pattern flow and requirements:

```
Export Format: HTML document
Filename: {blueprint-id}-blueprint.html
Content: Blueprint overview, pattern flow, governance requirements, customization notes
```

#### Stack Export

Exports the builder stack as JSON for programmatic use:

```json
{
  "stackId": "custom-stack-1",
  "createdAt": "2026-02-25T10:00:00Z",
  "patterns": [
    "medallion-architecture",
    "delta-lake-partitioning",
    "row-level-security"
  ],
  "notes": "Foundational HR analytics setup"
}
```

#### Brief Generation

Creates a concise text summary of all selected patterns with descriptions.

---

## 6. How to Make Updates

### 6.1 Adding a New Pattern

**Step-by-step process to add a new pattern:**

1. **Edit patterns.json**
   - Open: `/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json`
   - Add your pattern object to the `"patterns"` array (see schema template in section 10)
   - Ensure `id` is unique and kebab-case
   - Assign correct `domainId` (1-8)

2. **Validate JSON**
   ```bash
   jq . /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json > /dev/null
   ```
   If this succeeds, JSON is valid.

3. **Rebuild HTML**
   ```bash
   cd /sessions/zen-practical-faraday
   python3 build_html.py
   ```
   This reads patterns.json and blueprints.json, then generates pattern-builder.html.

4. **Update markdown documentation**
   ```bash
   cd /sessions/zen-practical-faraday
   PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_markdown.py
   ```
   This generates domain-specific markdown files in docs/pattern-descriptions/.

5. **Commit and push to GitHub**
   ```bash
   cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog
   git add patterns.json pattern-builder.html docs/
   git commit -m "Add pattern: {pattern-name}"
   git push origin main
   ```

6. **Verify GitHub Pages update**
   - Wait 1-2 minutes for GitHub Pages to rebuild
   - Check: https://barlowtech.github.io/hr-analytics-fabric-catalog/pattern-builder.html

### 6.2 Adding a New Blueprint

**Step-by-step process to add a new use case blueprint:**

1. **Edit blueprints.json**
   - Open: `/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json`
   - Add blueprint object to `"blueprints"` array (see schema template in section 11)
   - Reference only existing pattern IDs in the `"patterns"` array
   - Define `patternFlow` showing how patterns connect
   - Provide `keyGovernanceRequirements` specific to HR domain

2. **Validate JSON**
   ```bash
   jq . /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json > /dev/null
   ```

3. **Verify pattern references**
   All pattern IDs in blueprint must exist in patterns.json:
   ```bash
   # Extract pattern IDs from the blueprint
   jq '.blueprints[].patterns[]' blueprints.json

   # Check they exist in patterns.json
   jq '.patterns[].id' patterns.json
   ```

4. **Rebuild HTML**
   ```bash
   cd /sessions/zen-practical-faraday
   python3 build_html.py
   ```

5. **Test the blueprint**
   - Open pattern-builder.html in browser
   - Go to "Use Case Blueprints" tab
   - Verify your blueprint appears
   - Test loading it into Pattern Builder

6. **Commit and push**
   ```bash
   cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog
   git add blueprints.json pattern-builder.html
   git commit -m "Add blueprint: {blueprint-name}"
   git push origin main
   ```

### 6.3 Modifying the HTML App

The HTML app is generated from a Python script. **Do not edit pattern-builder.html directly** — edit the build script instead.

**To modify HTML functionality:**

1. **Locate the build script**
   - Path: `/sessions/zen-practical-faraday/build_html.py`

2. **Understand the structure**
   The script has sections:
   - Section 1: DOCTYPE and HEAD (styles)
   - Section 2: HTML body and tab structure
   - Section 3: Embedded data (PATTERNS_DATA, BLUEPRINTS_DATA)
   - Section 4: JavaScript functions

3. **Make your changes**
   - To add CSS: modify the `<style>` section (around line 40-500)
   - To add HTML: modify the body section (around line 500-800)
   - To add JS functions: modify the `<script>` section (around line 1000-end)

4. **Rebuild HTML**
   ```bash
   cd /sessions/zen-practical-faraday
   python3 build_html.py
   ```

5. **Test in browser**
   - Open pattern-builder.html
   - Test your changes

6. **Commit changes to build script**
   ```bash
   cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog
   git add pattern-builder.html
   git commit -m "Update HTML app: {description}"
   git push origin main
   ```

### 6.4 Updating Documentation

The markdown documentation is **automatically generated** from patterns.json.

**To update documentation:**

1. **Edit the patterns.json content fields**
   - Modify `description`, `usageInstructions`, `governanceConsiderations`, etc.

2. **Regenerate markdown**
   ```bash
   cd /sessions/zen-practical-faraday
   PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_markdown.py
   ```

   This creates:
   - `/docs/pattern-descriptions/01-data-organization.md`
   - `/docs/pattern-descriptions/02-transformation-processing.md`
   - (and 6 more for each domain)

3. **Review generated files**
   Each markdown file contains:
   - Domain introduction
   - All patterns for that domain
   - Pattern details formatted as markdown

4. **Commit generated files**
   ```bash
   cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog
   git add docs/pattern-descriptions/
   git commit -m "Regenerate documentation from patterns"
   git push origin main
   ```

### 6.5 Git Workflow for Updates

**Complete workflow to commit and push changes:**

```bash
# Navigate to repository
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog

# Check what changed
git status

# Stage specific files (preferred over git add .)
git add patterns.json
git add blueprints.json
git add pattern-builder.html
git add docs/

# Create commit with descriptive message
git commit -m "Add pattern: Feature Store Implementation

- Pattern ID: feature-store-delta
- Domain: Machine Learning and Traditional AI
- Complexity: Medium
- Includes governance considerations for feature versioning"

# Push to main branch
git push origin main

# Verify push succeeded
git status
```

The remote is configured as:
```
https://Barlowtech:<PASTE_BARLOWTECH_PAT_HERE>@github.com/Barlowtech/hr-analytics-fabric-catalog.git
```

---

## 7. Build Scripts

All build scripts are located in `/sessions/zen-practical-faraday/` (parent of the repo).

### 7.1 build_html.py

**Location:** `/sessions/zen-practical-faraday/build_html.py`
**Purpose:** Generate pattern-builder.html from JSON data sources

**How it works:**

1. Reads patterns.json
2. Reads blueprints.json
3. Embeds both as JavaScript constants
4. Wraps in HTML/CSS/JS template
5. Writes complete HTML to pattern-builder.html

**When to use:**
- After editing patterns.json
- After editing blueprints.json
- After modifying build_html.py itself

**Command:**
```bash
cd /sessions/zen-practical-faraday
python3 build_html.py
```

**Output:**
```
Reading patterns.json...
Reading blueprints.json...
Loaded 73 patterns and 8 blueprints
Writing /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/pattern-builder.html...
HTML generation complete!
```

### 7.2 gen_patterns.py

**Location:** `/sessions/zen-practical-faraday/gen_patterns.py`
**Purpose:** Generate complete patterns.json with all 73 patterns

**How it works:**

1. Defines all 73 patterns as Python dictionaries
2. Organizes by domain (1-8)
3. Includes all required fields
4. Serializes to JSON format
5. Writes to patterns.json

**When to use:**
- When you need to regenerate all patterns from scratch
- After major restructuring

**Command:**
```bash
cd /sessions/zen-practical-faraday
python3 gen_patterns.py
```

**Output:**
Generates: `/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json`

### 7.3 gen_blueprints.py

**Location:** `/sessions/zen-practical-faraday/gen_blueprints.py`
**Purpose:** Generate complete blueprints.json with all 8 use case blueprints

**How it works:**

1. Defines all 8 blueprints as Python dictionaries
2. Maps patterns to blueprints
3. Defines patternFlow showing sequence
4. Includes governance requirements
5. Serializes to JSON

**When to use:**
- When you need to regenerate all blueprints from scratch
- After adding multiple new blueprints

**Command:**
```bash
cd /sessions/zen-practical-faraday
python3 gen_blueprints.py
```

**Output:**
Generates: `/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json`

### 7.4 gen_markdown.py

**Location:** `/sessions/zen-practical-faraday/gen_markdown.py`
**Purpose:** Generate domain-specific markdown documentation from patterns.json

**How it works:**

1. Reads patterns.json
2. Groups patterns by domain
3. Creates markdown file for each domain
4. Generates pattern list table for README.md
5. Creates research-notes.md summary

**When to use:**
- After editing pattern descriptions
- After adding or removing patterns

**Command:**
```bash
cd /sessions/zen-practical-faraday
PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_markdown.py
```

**Note:** PYTHONPATH is set to fix Python dataclasses compatibility

**Output:**
- `/docs/pattern-descriptions/01-data-organization.md`
- `/docs/pattern-descriptions/02-transformation-processing.md`
- (and 6 more files)
- `/README.md` (updated pattern table)
- `/research-notes.md` (updated summary)

### 7.5 gen_docs.py

**Location:** `/sessions/zen-practical-faraday/gen_docs.py`
**Purpose:** Generate Word document reference materials

**How it works:**

1. Creates Word documents using python-docx
2. Generates governance guide
3. Generates fabric components reference
4. Generates AI model governance guide
5. Generates usage guide

**When to use:**
- When updating Word document content
- After adding new patterns that need documentation

**Command:**
```bash
cd /sessions/zen-practical-faraday
PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_docs.py
```

**Output:**
- `/docs/governance-guide/data-governance-guide.docx`
- `/docs/fabric-reference/fabric-components-reference.docx`
- `/docs/ai-model-governance/ai-model-governance.docx`
- `/docs/usage-guide/usage-guide.docx`

### 7.6 add_patterns.py and add_patterns_final.py

**Location:**
- `/sessions/zen-practical-faraday/add_patterns.py`
- `/sessions/zen-practical-faraday/add_patterns_final.py`

**Purpose:** Utility scripts to add new patterns to patterns.json interactively

**When to use:**
- For interactive pattern creation (less common, usually edit JSON directly)
- Use `add_patterns_final.py` as it's the most recent version

**Command:**
```bash
cd /sessions/zen-practical-faraday
python3 add_patterns_final.py
```

---

## 8. Python Environment Notes

### 8.1 Python Version and Path

```
Python: Python 3
Working Directory: /sessions/zen-practical-faraday/
PYTHONPATH: /sessions/zen-practical-faraday/pyfix
```

### 8.2 Dataclasses Compatibility Fix

A custom Python path is required for dataclasses compatibility:

```
PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 <script.py>
```

The fix is located at:
```
/sessions/zen-practical-faraday/pyfix/sitecustomize.py
```

This is required for:
- `gen_markdown.py`
- `gen_docs.py`

### 8.3 Required Python Packages

Install these before running build scripts:

```bash
pip install python-docx requests pandas streamlit
```

**Package purposes:**

| Package | Version | Used By | Purpose |
|---------|---------|---------|---------|
| python-docx | Latest | gen_docs.py | Generate Word documents |
| requests | Latest | (HTTP support) | Make API calls if needed |
| pandas | >=2.0.0 | gen_patterns.py | Data manipulation |
| streamlit | >=1.32.0 | streamlit/app.py | Run interactive Streamlit app |

### 8.4 Streamlit Application Notes

**Location:** `/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/streamlit/app.py`

**Features:**
- Alternative to HTML app (same pattern data)
- Interactive pattern explorer
- Domain-specific views
- Pattern relationships and dependencies
- Implementation checklist generation

**Running the app:**

```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/streamlit
streamlit run app.py
```

**Known Issues:**

- Contextvars compatibility issue in Cowork sandbox
- Works fine on local machine
- Use HTML app as primary interface if Streamlit fails

---

## 9. Key Design Decisions

### 9.1 Single-File HTML (No Server Needed)

**Decision:** Build pattern-builder.html as a completely self-contained single file.

**Rationale:**
- No server deployment required
- Works completely offline
- Can be hosted anywhere (GitHub Pages, email, USB drive)
- Zero external dependencies
- Faster loading (no round-trips to server)
- Easier to share and distribute

**Trade-offs:**
- Data embedded in HTML increases file size (~2MB)
- Can't dynamically fetch new patterns from API
- Search/filtering done in browser (still very fast)

### 9.2 patterns.json as Single Source of Truth

**Decision:** All pattern data lives in patterns.json; generated files derive from it.

**Rationale:**
- One place to edit patterns
- Documentation stays in sync with actual patterns
- HTML app is always current
- Machine-readable for future integrations

**Workflow:**
1. Edit patterns.json
2. Run build_html.py to update HTML app
3. Run gen_markdown.py to update docs
4. Commit all files

This ensures everything is always consistent.

### 9.3 Blueprints as Separate from Patterns

**Decision:** Blueprints are not patterns themselves; they're pattern combinations.

**Rationale:**
- Patterns are reusable building blocks
- Blueprints are pre-configured solutions
- A pattern can appear in multiple blueprints
- Blueprints can change without affecting individual patterns
- Clear separation of concerns

**Example:**
- Pattern: "Medallion Architecture"
- Blueprint: "Workforce Analytics Dashboard Foundation" uses medallion architecture + 5 other patterns

### 9.4 Domain Color Assignments

**Decision:** Each domain gets a distinct color for visual identification.

| Domain | Color | Rationale |
|--------|-------|-----------|
| Data Organization | Blue (#3B82F6) | Foundation (cool, stable) |
| Data Transformation | Purple (#8B5CF6) | Complex work (rich color) |
| Governance & Security | Red (#EF4444) | Critical/sensitive (warning color) |
| Business Intelligence | Green (#10B981) | End results (positive) |
| Machine Learning | Amber (#F59E0B) | Advanced/complex (warm) |
| Generative AI | Pink (#EC4899) | Cutting edge (distinct) |
| Alerting & Automation | Cyan (#06B6D4) | Real-time (bright, active) |
| Data Sharing | Teal (#14B8A6) | Connectivity (connecting color) |

Colors help users visually group patterns by domain in the browse and builder tabs.

### 9.5 Complexity and Maturity Taxonomy

**Complexity Levels:**

- **Low:** Can be implemented in days; basic skills; setup pattern
- **Medium:** 1-3 weeks; requires specialized knowledge; integration pattern
- **High:** 3+ weeks; significant expertise needed; foundational/advanced pattern

**Maturity Levels:**

- **GA (General Availability):** Production-ready; fully supported by Microsoft; recommended for production use
- **Preview:** Available but may change; use with caution; likely to be GA soon
- **Emerging:** Research stage; experimental; evaluate carefully before production

This taxonomy helps users understand implementation scope and feature stability.

---

## 10. Pattern Schema Template

Use this template to add new patterns to patterns.json. Copy this and fill in all fields:

```json
{
  "id": "unique-kebab-case-id",
  "name": "Human-Readable Pattern Name",
  "domain": "One of the 8 domain names",
  "domainId": 1,
  "category": "Sub-category within domain",
  "summary": "Single sentence describing what this pattern does.",
  "description": "Multi-paragraph description explaining the pattern, how it works, why you'd use it, and relevant context for HR analytics. Can be 2-3 sentences or a full paragraph.",
  "fabricComponents": [
    "Lakehouse",
    "OneLake",
    "Power BI",
    "Other Fabric components used in this pattern"
  ],
  "pros": [
    "Benefit or advantage 1",
    "Benefit or advantage 2",
    "Benefit or advantage 3"
  ],
  "cons": [
    "Drawback or consideration 1",
    "Drawback or consideration 2",
    "Drawback or consideration 3"
  ],
  "usageInstructions": "Step-by-step implementation guidance. Start with '1. ', '2. ', etc. Be specific and actionable. Include code examples if helpful. Should be implementable by someone with basic Fabric knowledge.",
  "governanceConsiderations": "Governance, security, compliance, and audit requirements. Include RLS considerations, sensitivity labels, audit trails, and any regulatory requirements relevant to HR data. This is critical for HR analytics.",
  "peopleAnalyticsUseCases": [
    "Specific HR use case 1 (e.g., 'Employee master repository moving through all layers')",
    "Specific HR use case 2",
    "Specific HR use case 3"
  ],
  "complexity": "Low | Medium | High",
  "maturity": "GA | Preview | Emerging",
  "compatibleWith": [
    "pattern-id-1",
    "pattern-id-2",
    "pattern-id-that-works-well-with-this-one"
  ],
  "incompatibleWith": [
    "pattern-id-that-conflicts"
  ],
  "prerequisites": [
    "pattern-that-should-be-done-first"
  ],
  "tags": [
    "searchable-tag-1",
    "searchable-tag-2",
    "architecture"
  ],
  "referenceLinks": [
    {
      "label": "Microsoft Documentation Title",
      "url": "https://docs.microsoft.com/full-url"
    },
    {
      "label": "Another Reference",
      "url": "https://example.com"
    }
  ],
  "estimatedImplementationEffort": "1-2 weeks | 2-3 weeks | 3-4 weeks | etc.",
  "costImplications": "Cost analysis, scaling considerations, optimization suggestions, etc. E.g., 'Storage scales with volume; optimize with VACUUM' or 'Cost depends on query complexity; use Import mode for small dimensions'"
}
```

### Field Guidelines

- **id**: Must be unique, kebab-case, lowercase, no spaces. Examples: `medallion-architecture`, `feature-store-delta`, `workforce-analytics-dashboard`
- **domain**: Must exactly match one of the 8 domain names (case-sensitive)
- **domainId**: 1-8, must match the domain
- **complexity**: Only "Low", "Medium", or "High"
- **maturity**: Only "GA", "Preview", or "Emerging"
- **pros/cons**: 2-4 items each, concise
- **usageInstructions**: Most important field for users; detailed and specific
- **governanceConsiderations**: Focus on HR-specific governance (RLS, sensitivity labels, compliance)
- **peopleAnalyticsUseCases**: 2-3 specific HR examples, not generic
- **compatibleWith**: Pattern IDs that work well together
- **incompatibleWith**: Patterns that conflict (uncommon)
- **prerequisites**: Patterns that must be done first
- **tags**: 3-5 searchable keywords
- **referenceLinks**: 1-3 official Microsoft documentation links

---

## 11. Blueprint Schema Template

Use this template to add new blueprints to blueprints.json:

```json
{
  "id": "unique-blueprint-id",
  "name": "Human-Readable Blueprint Name",
  "description": "Detailed description of what this blueprint accomplishes, who it's for, and what outcomes it enables. 2-3 sentences explaining the value proposition.",
  "audience": "Target audience: 'HR Leadership, CHRO', 'Data Scientists, ML Engineers', etc.",
  "patterns": [
    "pattern-id-1",
    "pattern-id-2",
    "pattern-id-3",
    "pattern-id-4",
    "pattern-id-5",
    "pattern-id-6"
  ],
  "patternFlow": [
    {
      "from": "first-pattern-id",
      "to": "second-pattern-id",
      "description": "How the first pattern feeds into the second. E.g., 'Bronze-Silver-Gold layers provide clean data that feeds into semantic model'"
    },
    {
      "from": "second-pattern-id",
      "to": "third-pattern-id",
      "description": "Connection description"
    },
    {
      "from": "third-pattern-id",
      "to": "fourth-pattern-id",
      "description": "Connection description"
    }
  ],
  "editableNotes": "Customization guidance for organizations. Explain how to tailor this blueprint to specific org needs. E.g., 'Customize by selecting which workforce metrics (headcount by department, turnover trends, diversity breakdowns) are most relevant to your HR leadership KPIs.'",
  "estimatedTotalEffort": "2-3 weeks | 3-4 weeks | 4-6 weeks | etc.",
  "keyGovernanceRequirements": [
    "Governance requirement 1 specific to HR domain",
    "Governance requirement 2",
    "Governance requirement 3",
    "Governance requirement 4"
  ],
  "tags": [
    "use-case-type",
    "hr-specific",
    "foundational",
    "security",
    "domain-specific-tag"
  ]
}
```

### Blueprint Guidelines

- **id**: Unique, kebab-case. Examples: `workforce-dashboard-foundation`, `attrition-risk-scoring`
- **patterns**: Must be actual pattern IDs that exist in patterns.json (required field validation)
- **patternFlow**: Must include all patterns in the `patterns` array. Each pattern should appear as `from` or `to` (typically in a sequence)
- **audience**: Specific role/persona (not generic "developers")
- **keyGovernanceRequirements**: Focus on HR-specific governance (RLS, sensitivity labels, compliance, privacy)
- **estimatedTotalEffort**: Sum of individual pattern efforts plus integration complexity
- **editableNotes**: Should mention specific metrics, roles, or configurations users can customize
- **tags**: Include domain, use-case category, and 3-4 descriptive tags

### Example Blueprint Structure

A complete blueprint would have:

1. 5-8 patterns in sequence
2. Pattern flow connecting all patterns logically
3. Each governance requirement tied to a pattern or HR-specific need
4. Clear customization guidance

---

## 12. Quick Reference Commands

### Validation Commands

**Validate patterns.json:**
```bash
jq . /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json > /dev/null && echo "Valid"
```

**Validate blueprints.json:**
```bash
jq . /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json > /dev/null && echo "Valid"
```

**Count patterns:**
```bash
jq '.patterns | length' /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json
```

**List all pattern IDs:**
```bash
jq -r '.patterns[].id' /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json
```

**List all blueprint IDs:**
```bash
jq -r '.blueprints[].id' /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json
```

### Build Commands

**Rebuild HTML from JSON:**
```bash
cd /sessions/zen-practical-faraday && python3 build_html.py
```

**Regenerate markdown documentation:**
```bash
cd /sessions/zen-practical-faraday && PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_markdown.py
```

**Regenerate Word documents:**
```bash
cd /sessions/zen-practical-faraday && PYTHONPATH=/sessions/zen-practical-faraday/pyfix python3 gen_docs.py
```

**Regenerate all patterns:**
```bash
cd /sessions/zen-practical-faraday && python3 gen_patterns.py && python3 build_html.py
```

**Regenerate all blueprints:**
```bash
cd /sessions/zen-practical-faraday && python3 gen_blueprints.py && python3 build_html.py
```

### Git Workflow Commands

**Check status:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && git status
```

**Stage files:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && \
git add patterns.json blueprints.json pattern-builder.html docs/
```

**Create commit:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && \
git commit -m "Update: Brief description of changes"
```

**Push to GitHub:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && \
git push origin main
```

**View recent commits:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && \
git log --oneline -10
```

**View differences:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog && \
git diff
```

### Data Extraction Commands

**Extract specific pattern:**
```bash
jq '.patterns[] | select(.id == "medallion-architecture")' \
  /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json
```

**List patterns by domain:**
```bash
jq -r '.patterns[] | select(.domainId == 1) | .name' \
  /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json
```

**List high-complexity patterns:**
```bash
jq -r '.patterns[] | select(.complexity == "High") | .name' \
  /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/patterns.json
```

**Extract blueprint pattern list:**
```bash
jq '.blueprints[] | select(.id == "workforce-dashboard-foundation") | .patterns' \
  /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json
```

### Running Applications

**Start Streamlit app:**
```bash
cd /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/streamlit && \
streamlit run app.py
```

**Open HTML app:**
```
Open in browser: /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/pattern-builder.html
Or via GitHub Pages: https://barlowtech.github.io/hr-analytics-fabric-catalog/pattern-builder.html
```

---

## Summary for Future Claude Sessions

When working with this project:

1. **Start here:** Read sections 1-3 for overview and structure
2. **Making changes:** Go to section 6 for step-by-step instructions
3. **Build process:** Section 7 explains all scripts and when to use them
4. **Adding content:** Use templates in sections 10-11
5. **Troubleshooting:** Check section 8 for environment issues
6. **Quick tasks:** Jump to section 12 for one-liner commands

**Key principles:**
- patterns.json is the source of truth
- Always validate JSON after edits
- Always rebuild HTML after JSON changes
- Always push to GitHub to publish changes
- Pattern relationships (compatibleWith, incompatibleWith, prerequisites) are critical for app functionality

**GitHub Pages:**
Changes pushed to main branch appear at:
https://barlowtech.github.io/hr-analytics-fabric-catalog/pattern-builder.html

(2-minute delay for deployment)

---

**End of Operations Guide**

#!/usr/bin/env python3
"""
Update blueprints.json with:
1. Add roleAssignments field to all 8 existing blueprints
2. Update hr-chatbot-secure description and editableNotes
3. Add 4 new blueprints with roleAssignments
"""

import json
from datetime import datetime

# Load existing blueprints
with open('/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json', 'r') as f:
    data = json.load(f)

# Define roleAssignments for each existing blueprint
role_assignments_map = {
    "workforce-dashboard-foundation": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Lakehouse/Warehouse setup and medallion structure",
                "DirectLake semantic model configuration",
                "Row-level security configuration",
                "Encryption with customer-managed keys"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Gold-layer table design and creation",
                "Semantic model development and certification",
                "Power BI dashboard development",
                "Sensitivity label application to fields"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define key HR metrics and KPIs",
                "Validate data accuracy and business logic",
                "Design dashboard layouts and user experience",
                "Acceptance testing and stakeholder feedback"
            ]
        }
    ],
    "attrition-risk-scoring": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Feature store and Delta table infrastructure setup",
                "Batch inference pipeline orchestration",
                "Data Activator alert configuration",
                "Pipeline monitoring and SLA management"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Feature engineering and selection",
                "ML model development and training",
                "Fairness and bias evaluation testing",
                "MLflow model registry management"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define attrition drivers and business context",
                "Validate model predictions against HR intuition",
                "Design escalation workflows for high-risk employees",
                "Champion fairness and bias thresholds"
            ]
        }
    ],
    "compensation-analytics-secure": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "SCD Type 2 implementation for salary history",
                "Dynamic data masking rules configuration",
                "DLP policy enforcement setup",
                "Audit logging and monitoring infrastructure"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Compensation data modeling and cleansing",
                "Semantic model development with masking rules",
                "k-anonymity algorithm implementation",
                "Paginated report template development"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define role-based masking policies",
                "Validate compensation aggregations and trends",
                "Review k-anonymity thresholds with compensation team",
                "Executive report content curation and approval"
            ]
        }
    ],
    "regulatory-compliance-stack": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "CMK encryption and key management setup",
                "Network isolation and private link configuration",
                "Privileged access management (PAM) setup",
                "SIEM integration and audit log export"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Sensitivity label classification and tagging",
                "Purview data catalog configuration",
                "DLP policy rule creation and testing",
                "Audit report automation"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define regulatory classification scheme",
                "Document compliance requirements and policies",
                "Review audit logs and compliance dashboards",
                "Stakeholder communication on compliance status"
            ]
        }
    ],
    "hr-chatbot-secure": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Vector database and RAG infrastructure setup",
                "Row-level security implementation in RAG layer",
                "Audit logging and SIEM integration",
                "Copilot Studio secure connection configuration"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "HR policy document indexing and vectorization",
                "Prompt engineering and guardrail development",
                "RAG retrieval testing and optimization",
                "Content generation template design"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Select and curate HR policy documents",
                "Define guardrails to prevent sensitive answers",
                "Test chatbot responses for accuracy",
                "Design escalation workflows and approve conversations"
            ]
        }
    ],
    "onboarding-offboarding-pipeline": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Change data capture (CDC) infrastructure setup",
                "Data retention and lifecycle management policies",
                "DSR fulfillment automation and workflow",
                "Data quality monitoring and alerting"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "SCD Type 2 pipeline development",
                "Data quality validation rule definition",
                "Lifecycle event schema and transformation design",
                "DSR template and anonymization logic"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define retention policies per jurisdiction",
                "Map lifecycle events to business processes",
                "Validate employee data completeness",
                "Review DSR fulfillment before data deletion"
            ]
        }
    ],
    "cross-border-hr-analytics": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Data residency infrastructure per country",
                "Separate encryption keys per region",
                "Hub-spoke workspace architecture",
                "Cross-border data flow monitoring"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Medallion stack per country setup",
                "k-anonymity threshold tuning per country",
                "RLS rule design for country isolation",
                "Cross-border aggregate model development"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define country-specific compliance requirements",
                "Validate anonymization effectiveness",
                "Review aggregated global metrics",
                "Stakeholder communication on data residency"
            ]
        }
    ],
    "self-service-bi-governed": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Hub-spoke workspace architecture setup",
                "Deployment pipeline infrastructure",
                "Metrics scorecard framework",
                "Performance monitoring and optimization"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Certified semantic model development",
                "Deployment pipeline testing and validation",
                "Metrics scorecard design and governance",
                "Self-service report templates"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define certified metrics and KPIs",
                "Approve metrics for self-service availability",
                "Develop self-service reports",
                "Monitor metric usage and quality"
            ]
        }
    ]
}

# Add roleAssignments to existing blueprints
for blueprint in data['blueprints']:
    blueprint_id = blueprint['id']
    if blueprint_id in role_assignments_map:
        blueprint['roleAssignments'] = role_assignments_map[blueprint_id]

# Update hr-chatbot-secure description and editableNotes
for blueprint in data['blueprints']:
    if blueprint['id'] == 'hr-chatbot-secure':
        blueprint['description'] = "RAG-based conversational AI agent grounded in HR policies and employee data with row-level security enforcement and audit logging. Can be customized as a domain-specific assistant for content generation (policy summaries, FAQs, onboarding guides) or Q&A, enabling both conversational interfaces and automated content creation."
        blueprint['editableNotes'] = "Customize the chatbot for your HR context by selecting which policies, benefits information, and employee data to ground the RAG retriever in. Define guardrails to prevent the chatbot from answering sensitive questions (e.g., compensation, performance reviews). Configure escalation flows for complex questions. Optionally extend for content generation use cases (policy summaries, FAQ creation, onboarding materials) by adjusting LLM prompts and output templates."
        break

# New blueprint 1: conversational-hr-analyst
new_blueprint_1 = {
    "id": "conversational-hr-analyst",
    "name": "Conversational HR Reporting Analyst",
    "description": "A Fabric Data Agent-powered conversational interface that lets HR professionals ask natural language questions and receive reliable, data-driven answers. Uses whitelisted queries, curated semantic models, and a query translation layer that maps business questions to the appropriate metrics, datasets, and pre-validated queries.",
    "audience": "HR Business Partners, People Analytics Consumers, HR Leaders",
    "patterns": [
        "fabric-data-agent-hr",
        "direct-lake-semantic-model",
        "row-level-security",
        "cls-column-level-security",
        "hr-ai-guardrails",
        "audit-siem-integration",
        "medallion-architecture"
    ],
    "patternFlow": [
        {
            "from": "medallion-architecture",
            "to": "direct-lake-semantic-model",
            "description": "Gold-layer HR metrics tables feed directly into DirectLake semantic model"
        },
        {
            "from": "direct-lake-semantic-model",
            "to": "fabric-data-agent-hr",
            "description": "DirectLake semantic model serves as trusted data foundation for Data Agent queries"
        },
        {
            "from": "fabric-data-agent-hr",
            "to": "row-level-security",
            "description": "Data Agent respects row-level security rules to return only data users are authorized to see"
        },
        {
            "from": "row-level-security",
            "to": "cls-column-level-security",
            "description": "Column-level security masks sensitive fields even within authorized rows"
        },
        {
            "from": "cls-column-level-security",
            "to": "hr-ai-guardrails",
            "description": "Data Agent response generation constrained with HR-specific guardrails and query whitelisting"
        },
        {
            "from": "hr-ai-guardrails",
            "to": "audit-siem-integration",
            "description": "All Data Agent queries and responses logged to SIEM for audit and compliance tracking"
        }
    ],
    "editableNotes": "Customize by defining the query translation layer — map common natural language questions (e.g., 'What's our turnover rate?' or 'Show me headcount by department') to specific metrics, semantic model tables, and pre-validated DAX queries. Use few-shot examples in Data Agent instructions (up to 15K chars) to steer the agent toward trusted analytical paths. Define guardrails to prevent cross-boundary queries and sensitive data exploration.",
    "estimatedTotalEffort": "4-6 weeks",
    "keyGovernanceRequirements": [
        "Document whitelisted queries and query translation mappings",
        "Validate example queries in Data Agent instructions with HR stakeholders",
        "Test row-level and column-level security enforcement with sample user queries",
        "Enable audit logging of all Data Agent interactions for compliance tracking"
    ],
    "roleAssignments": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Lakehouse/Warehouse setup with medallion architecture",
                "DirectLake semantic model configuration",
                "Row-level and column-level security setup",
                "Audit log export to SIEM"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Semantic model design with business-friendly names and measures",
                "Data Agent instruction authoring (up to 15K chars)",
                "Example query curation and few-shot learning setup",
                "Query translation layer mapping definition"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define which questions the agent should answer",
                "Validate metric definitions and calculations",
                "Test Data Agent accuracy with sample queries",
                "Acceptance testing and feedback on response quality"
            ]
        }
    ],
    "tags": [
        "generative-ai",
        "data-agent",
        "conversational",
        "semantic-model",
        "self-service"
    ]
}

# New blueprint 2: hr-policy-content-engine
new_blueprint_2 = {
    "id": "hr-policy-content-engine",
    "name": "HR Policy & Domain Knowledge Content Engine",
    "description": "A customizable, domain-specific AI assistant that aids HR teams in understanding complex policies, generating policy summaries, drafting communications, and creating domain-specific content (onboarding guides, policy explainers, FAQ documents). Combines RAG-grounded policy knowledge with LLM generation capabilities and content guardrails.",
    "audience": "HR Service Delivery, Total Rewards, Talent Acquisition, HR Communications",
    "patterns": [
        "rag-fabric-grounded",
        "copilot-studio-grounded",
        "hr-ai-guardrails",
        "llm-powered-analysis",
        "sensitivity-labels",
        "audit-siem-integration",
        "medallion-architecture"
    ],
    "patternFlow": [
        {
            "from": "medallion-architecture",
            "to": "rag-fabric-grounded",
            "description": "Gold-layer HR policy documents and reference materials indexed as vectors in RAG knowledge base"
        },
        {
            "from": "rag-fabric-grounded",
            "to": "copilot-studio-grounded",
            "description": "RAG retriever grounds Copilot Studio with authoritative policy context"
        },
        {
            "from": "copilot-studio-grounded",
            "to": "llm-powered-analysis",
            "description": "LLM layer generates policy summaries, communications drafts, and content from grounded context"
        },
        {
            "from": "llm-powered-analysis",
            "to": "hr-ai-guardrails",
            "description": "Generated content validated against HR guardrails to ensure tone, brand consistency, and accuracy"
        },
        {
            "from": "hr-ai-guardrails",
            "to": "sensitivity-labels",
            "description": "Generated content inherits sensitivity labels from source policy documents"
        },
        {
            "from": "sensitivity-labels",
            "to": "audit-siem-integration",
            "description": "Content generation requests and approvals audited in SIEM for compliance"
        }
    ],
    "editableNotes": "Customize by curating HR policy documents, benefits guides, and company procedures to index in the RAG knowledge base. Define content generation templates for common use cases (policy summaries, FAQ responses, onboarding checklists). Configure LLM prompts to match your organization's tone and communication style. Set guardrails for sensitive topics (compensation, legal disclaimers).",
    "estimatedTotalEffort": "6-10 weeks",
    "keyGovernanceRequirements": [
        "Establish policy document curation and versioning process",
        "Document LLM prompt templates and content generation guidelines",
        "Validate generated content accuracy and brand alignment before publishing",
        "Enable audit logging of all content generation requests and approvals"
    ],
    "roleAssignments": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Policy document ingestion pipeline development",
                "Vector database and RAG infrastructure setup",
                "Audit logging and SIEM integration",
                "Access control and sensitivity label configuration"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Policy document vectorization and indexing",
                "Prompt engineering for content generation",
                "LLM integration and guardrail configuration",
                "Output template design and validation"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Curate and maintain policy document library",
                "Define guardrails and content tone guidelines",
                "Review and approve generated content",
                "Validate accuracy and brand alignment"
            ]
        }
    ],
    "tags": [
        "generative-ai",
        "content-generation",
        "rag",
        "policy",
        "domain-knowledge"
    ]
}

# New blueprint 3: presentation-ready-artifacts
new_blueprint_3 = {
    "id": "presentation-ready-artifacts",
    "name": "Template-Governed Artifact Generation",
    "description": "An automated pipeline for creating presentation-ready Word documents and PowerPoint slides that adhere to strict organizational template standards, visual guidelines, and branding requirements. Uses parameterized notebooks to pull data, apply statistical analysis, and generate formatted outputs that are mostly ready for stakeholder consumption.",
    "audience": "People Analytics Team, HR Leadership Reporting, Executive Briefing Teams",
    "patterns": [
        "adhoc-insight-engine",
        "llm-powered-analysis",
        "direct-lake-semantic-model",
        "medallion-architecture",
        "sensitivity-labels",
        "git-version-control"
    ],
    "patternFlow": [
        {
            "from": "medallion-architecture",
            "to": "direct-lake-semantic-model",
            "description": "Gold-layer HR metrics feed into DirectLake semantic model for parameterized notebook queries"
        },
        {
            "from": "direct-lake-semantic-model",
            "to": "adhoc-insight-engine",
            "description": "Parameterized Spark notebooks query semantic model for fresh data and run statistical analyses"
        },
        {
            "from": "adhoc-insight-engine",
            "to": "llm-powered-analysis",
            "description": "LLM layer generates executive summaries and narrative sections for presentation slides"
        },
        {
            "from": "llm-powered-analysis",
            "to": "sensitivity-labels",
            "description": "Generated artifacts inherit sensitivity labels from source data"
        },
        {
            "from": "sensitivity-labels",
            "to": "git-version-control",
            "description": "Output files and templates stored in Git for version tracking and audit compliance"
        }
    ],
    "editableNotes": "Customize by defining parameterized notebook templates that pull your HR metrics, apply relevant statistical tests, and populate locked Word/PowerPoint templates with branded formatting. Version control all templates in Git to track changes and enforce brand standards. Configure LLM prompts to generate executive narratives matching your organization's voice.",
    "estimatedTotalEffort": "5-8 weeks",
    "keyGovernanceRequirements": [
        "Define and version-control presentation templates with locked formatting sections",
        "Document parameterized notebook logic and statistical methods",
        "Validate generated artifacts for accuracy and brand compliance before distribution",
        "Maintain template change history in Git with approval workflows"
    ],
    "roleAssignments": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Notebook scheduling and orchestration setup",
                "Template repository and Git integration",
                "Output file storage and lifecycle management",
                "Version control and change tracking"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Parameterized Spark notebook development",
                "Statistical analysis code implementation",
                "Template-to-data binding and formatting",
                "LLM narrative generation prompt design"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Design presentation templates and brand standards",
                "Define content requirements and narrative tone",
                "Review and approve generated artifacts",
                "Validate statistical accuracy before stakeholder distribution"
            ]
        }
    ],
    "tags": [
        "automation",
        "reporting",
        "template",
        "artifacts",
        "generative-ai"
    ]
}

# New blueprint 4: sandbox-analytics-environment
new_blueprint_4 = {
    "id": "sandbox-analytics-environment",
    "name": "Governed Sandbox Analytics Environment",
    "description": "A flexible, governed workspace where analysts can manually upload files (CSV, Excel, JSON), combine them with production Lakehouse data via OneLake shortcuts, run ad-hoc statistical testing, and generate insights — all within a controlled environment with time-limited data retention and audit trails. Supports both one-off exploratory analysis and recurring parameterized insight generation.",
    "audience": "People Analytics Team, HR Data Scientists, Business Analysts",
    "patterns": [
        "sandbox-upload-workspace",
        "adhoc-insight-engine",
        "onelake-shortcuts",
        "medallion-architecture",
        "row-level-security",
        "sensitivity-labels",
        "llm-powered-analysis"
    ],
    "patternFlow": [
        {
            "from": "sandbox-upload-workspace",
            "to": "onelake-shortcuts",
            "description": "Sandbox Lakehouse accepts manual file uploads; OneLake shortcuts connect to production Gold-layer data"
        },
        {
            "from": "onelake-shortcuts",
            "to": "medallion-architecture",
            "description": "Shortcuts provide access to production data without copying; sandbox maintains separate Bronze/Silver layers"
        },
        {
            "from": "medallion-architecture",
            "to": "adhoc-insight-engine",
            "description": "Analysts run statistical tests (t-tests, regression, ANOVA) in notebooks on combined sandbox and production data"
        },
        {
            "from": "adhoc-insight-engine",
            "to": "llm-powered-analysis",
            "description": "LLM layer interprets statistical test results and generates plain-language insights"
        },
        {
            "from": "llm-powered-analysis",
            "to": "row-level-security",
            "description": "Output insights respect row-level security rules for sensitive data"
        },
        {
            "from": "row-level-security",
            "to": "sensitivity-labels",
            "description": "Sandbox artifacts inherit and display sensitivity labels from source data"
        }
    ],
    "editableNotes": "Customize by configuring the sandbox Lakehouse with auto-schema detection for uploaded files. Define OneLake shortcuts to your production Gold tables. Configure retention policies (e.g., 90-day auto-deletion) and audit logging. Create statistical testing notebook templates for common analyses (cohort comparisons, trend analysis, correlation studies).",
    "estimatedTotalEffort": "4-6 weeks",
    "keyGovernanceRequirements": [
        "Establish sandbox Lakehouse with time-bound data retention (e.g., 90 days)",
        "Configure OneLake shortcuts to production data without copying",
        "Enable audit logging of all uploads, analysis, and exports",
        "Require approval workflows for exports and sensitive data uploads"
    ],
    "roleAssignments": [
        {
            "role": "Data Engineers/Architects",
            "activities": [
                "Sandbox Lakehouse provisioning and configuration",
                "OneLake shortcut setup to production data",
                "Retention policies and auto-cleanup scheduling",
                "Audit logging and access control configuration"
            ]
        },
        {
            "role": "Analytics Engineers",
            "activities": [
                "Statistical testing notebook templates",
                "Data quality checks on uploaded files",
                "Output formatting and visualization",
                "LLM integration for result interpretation"
            ]
        },
        {
            "role": "Business SMEs / HR Analysts",
            "activities": [
                "Define analysis requirements and hypotheses",
                "Upload source files and validate data quality",
                "Perform statistical tests and interpret results",
                "Approve insights before distribution to stakeholders"
            ]
        }
    ],
    "tags": [
        "sandbox",
        "analytics",
        "governed",
        "adhoc",
        "statistical-analysis"
    ]
}

# Add new blueprints to the list
data['blueprints'].extend([new_blueprint_1, new_blueprint_2, new_blueprint_3, new_blueprint_4])

# Update metadata
data['metadata']['totalBlueprints'] = 12
data['metadata']['lastUpdated'] = datetime.now().isoformat()

# Write updated data back to file
with open('/sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify and print summary
print(f"✓ Successfully updated blueprints.json")
print(f"✓ Total blueprints: {data['metadata']['totalBlueprints']}")
print(f"\nExisting blueprints with roleAssignments added:")
for bp in data['blueprints'][:8]:
    print(f"  - {bp['name']}")

print(f"\nNew blueprints added:")
for bp in data['blueprints'][8:]:
    print(f"  - {bp['name']}")

print(f"\nUpdated blueprint:")
for bp in data['blueprints']:
    if bp['id'] == 'hr-chatbot-secure':
        print(f"  - {bp['name']} (description and editableNotes expanded for content generation)")
        break

print(f"\n✓ All 12 blueprints now include roleAssignments field")
print(f"✓ File saved: /sessions/zen-practical-faraday/mnt/WesBarlow/hr-analytics-fabric-catalog/blueprints.json")

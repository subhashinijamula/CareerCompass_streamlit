
"""
CareerCompass - Career Skill Requirements and Learning Roadmaps

This module contains:
1. Career-wise skill requirements
2. Skill gap calculations
3. Detailed learning topics
4. Practice exercises
5. Mini-projects
6. Capstone projects

The skill levels are illustrative guidance for this prototype.
"""

# ==========================================================
# 1. CAREER-WISE REQUIRED SKILLS
# ==========================================================

CAREER_SKILLS = {

    "Data Analyst": {
        "Python": ("python", 3),
        "SQL": ("sql", 4),
        "Excel": ("data_visualization", 3),
        "Statistics": ("statistics", 4),
        "Data Visualization": ("data_visualization", 4),
    },

    "Data Scientist": {
        "Python": ("python", 4),
        "Statistics": ("statistics", 4),
        "SQL": ("sql", 3),
        "Machine Learning": ("machine_learning", 5),
        "Data Visualization": ("data_visualization", 3),
    },

    "Machine Learning Engineer": {
        "Python": ("python", 5),
        "Mathematics & Statistics": ("statistics", 4),
        "Machine Learning": ("machine_learning", 5),
        "Software Engineering": ("java", 3),
        "Cloud & Deployment": ("cloud", 4),
    },

    "Software Developer": {
        "Programming": ("java", 4),
        "Python": ("python", 3),
        "Data Structures & Algorithms": ("problem_solving", 4),
        "Database & SQL": ("sql", 4),
        "Web Development": ("web_development", 4),
    },

    "Cybersecurity Analyst": {
        "Networking": ("cybersecurity", 3),
        "Linux & Operating Systems": ("cybersecurity", 3),
        "Security Fundamentals": ("cybersecurity", 5),
        "Python Scripting": ("python", 3),
        "Log Analysis": ("analytical_thinking", 4),
    },

    "Cloud Engineer": {
        "Linux": ("cloud", 3),
        "Networking": ("cloud", 4),
        "Cloud Platform": ("cloud", 5),
        "Containers & DevOps": ("cloud", 4),
        "Scripting": ("python", 3),
    },

    "Business Analyst": {
        "Excel": ("data_visualization", 4),
        "SQL": ("sql", 3),
        "Statistics": ("statistics", 3),
        "Business Analysis": ("business_interest", 4),
        "Communication": ("communication", 5),
    },

    "UI/UX Designer": {
        "Design Principles": ("design", 5),
        "Figma & Design Tools": ("design", 4),
        "UX Research": ("design_interest", 4),
        "Prototyping": ("creativity", 4),
        "Communication": ("communication", 3),
    },
}


# ==========================================================
# 2. SKILL GAP CALCULATION
# ==========================================================

def get_skill_gaps(career, profile):
    """
    Compare a student's current skill ratings with
    the target skill ratings for the selected career.
    """

    if career not in CAREER_SKILLS:
        raise ValueError(f"Unknown career: {career}")

    requirements = CAREER_SKILLS[career]

    results = []

    for skill, (profile_key, required) in requirements.items():

        current = int(profile.get(profile_key, 1))

        gap = max(0, required - current)

        results.append({
            "skill": skill,
            "current": current,
            "required": required,
            "gap": gap
        })

    return results


# ==========================================================
# 3. GENERAL ROADMAP FUNCTION
# ==========================================================

def get_roadmap(career, gaps):
    """
    Return a simple three-stage roadmap.

    Kept available for compatibility with code that uses
    the older get_roadmap function.
    """

    focus = [
        item["skill"]
        for item in gaps
        if item["gap"] > 0
    ]

    return [
        {
            "stage": "01",
            "title": "Build Foundations",
            "description": (
                "Learn the fundamentals of "
                + (
                    ", ".join(focus[:3])
                    if focus
                    else "the core skills required for this career"
                )
                + "."
            )
        },
        {
            "stage": "02",
            "title": "Develop Practical Skills",
            "description": (
                "Study intermediate topics, complete exercises "
                "and build small practical applications."
            )
        },
        {
            "stage": "03",
            "title": "Build Your Portfolio",
            "description": (
                "Complete a career-related project, document "
                "your work and showcase your skills."
            )
        }
    ]


# ==========================================================
# 4. HELPER FUNCTION TO CREATE LEARNING LEVELS
# ==========================================================

def create_levels(
    foundation,
    intermediate,
    advanced,
    foundation_practice,
    intermediate_practice,
    advanced_practice,
    foundation_project="",
    intermediate_project="",
    advanced_project=""
):

    return [

        {
            "name": "Level 1 - Foundations",
            "goal": "Understand the basic concepts and terminology.",
            "topics": foundation,
            "practice": foundation_practice,
            "mini_project": foundation_project
        },

        {
            "name": "Level 2 - Intermediate",
            "goal": "Apply concepts to practical problems.",
            "topics": intermediate,
            "practice": intermediate_practice,
            "mini_project": intermediate_project
        },

        {
            "name": "Level 3 - Advanced Application",
            "goal": "Use the skill in a complete real-world workflow.",
            "topics": advanced,
            "practice": advanced_practice,
            "mini_project": advanced_project
        }

    ]


def create_skill(name, purpose, levels, capstone_title, capstone):

    return {
        "name": name,
        "purpose": purpose,
        "levels": levels,
        "capstone_title": capstone_title,
        "capstone": capstone
    }


# ==========================================================
# 5. DATA SCIENTIST ROADMAP
# ==========================================================

DATA_SCIENTIST = [

    create_skill(
        "Python",
        "Use Python for data processing and scientific programming.",
        create_levels(
            [
                "Variables and data types",
                "Operators",
                "Conditional statements",
                "Loops",
                "Functions",
                "Lists, tuples, sets and dictionaries"
            ],
            [
                "Object-oriented programming",
                "Exception handling",
                "File handling",
                "NumPy arrays",
                "Pandas Series and DataFrames",
                "Data cleaning and transformation"
            ],
            [
                "Lambda functions",
                "List comprehensions",
                "Iterators and generators",
                "Modules and packages",
                "Vectorization",
                "Reusable data pipelines"
            ],
            "Write Python programs using variables, loops and functions.",
            "Load a CSV file and clean missing values using Pandas.",
            "Create a reusable data preprocessing pipeline.",
            "Student marks analysis",
            "Sales data cleaning",
            "Automated data analysis"
        ),
        "End-to-End Data Science Project",
        "Use Python, Pandas and NumPy to clean, analyze and prepare a real dataset."
    ),

    create_skill(
        "Statistics",
        "Understand data distributions, probability and statistical reasoning.",
        create_levels(
            [
                "Population and sample",
                "Mean, median and mode",
                "Range and variance",
                "Standard deviation",
                "Probability basics",
                "Types of data"
            ],
            [
                "Conditional probability",
                "Bayes theorem",
                "Normal distribution",
                "Binomial distribution",
                "Correlation and covariance",
                "Sampling distributions"
            ],
            [
                "Hypothesis testing",
                "Null and alternative hypotheses",
                "p-values",
                "Confidence intervals",
                "Type I and Type II errors",
                "A/B testing"
            ],
            "Calculate mean, median and standard deviation manually.",
            "Solve probability problems and visualize distributions.",
            "Perform a hypothesis test and explain the result.",
            "Student performance statistics",
            "Probability simulation",
            "A/B testing analysis"
        ),
        "Statistical Analysis Project",
        "Analyze a dataset using descriptive statistics, probability and hypothesis testing."
    ),

    create_skill(
        "SQL",
        "Retrieve, combine and analyze structured database information.",
        create_levels(
            [
                "Database fundamentals",
                "Tables, rows and columns",
                "SELECT",
                "WHERE",
                "ORDER BY",
                "DISTINCT"
            ],
            [
                "Aggregate functions",
                "GROUP BY",
                "HAVING",
                "INNER JOIN",
                "LEFT JOIN",
                "CASE statements"
            ],
            [
                "Subqueries",
                "Common Table Expressions",
                "Window functions",
                "ROW_NUMBER and RANK",
                "Date functions",
                "Query optimization basics"
            ],
            "Retrieve records from a database using SELECT.",
            "Join customer and order tables and calculate total sales.",
            "Use CTEs and window functions to analyze customer activity.",
            "Student database queries",
            "Retail sales analysis",
            "Customer cohort analysis"
        ),
        "Customer Data Analysis",
        "Use SQL joins, aggregations and window functions to analyze customer purchasing behavior."
    ),

    create_skill(
        "Machine Learning",
        "Build predictive models using supervised and unsupervised learning.",
        create_levels(
            [
                "Introduction to Machine Learning",
                "Supervised learning",
                "Unsupervised learning",
                "Linear regression",
                "Logistic regression",
                "Decision trees"
            ],
            [
                "Random forest",
                "Gradient boosting basics",
                "K-means clustering",
                "Feature scaling",
                "Encoding categorical data",
                "Train-test split",
                "Cross-validation"
            ],
            [
                "Hyperparameter tuning",
                "Handling imbalanced datasets",
                "Feature selection",
                "Model interpretability",
                "SHAP and LIME concepts",
                "ML pipelines",
                "Model evaluation"
            ],
            "Train a basic classification model using Scikit-learn.",
            "Compare multiple ML algorithms using evaluation metrics.",
            "Build an end-to-end ML pipeline and analyze model errors.",
            "Iris classification",
            "Customer segmentation",
            "End-to-end prediction system"
        ),
        "Machine Learning Prediction System",
        "Develop a complete ML application that performs data preprocessing, model training, evaluation and prediction."
    ),

    create_skill(
        "Data Visualization",
        "Communicate patterns and insights through meaningful visualizations.",
        create_levels(
            [
                "Introduction to data visualization",
                "Matplotlib",
                "Line charts",
                "Bar charts",
                "Histograms",
                "Scatter plots"
            ],
            [
                "Seaborn",
                "Box plots",
                "Correlation heatmaps",
                "Pair plots",
                "Plotly",
                "Interactive charts"
            ],
            [
                "Dashboard development",
                "KPI design",
                "Dashboard storytelling",
                "Model evaluation plots",
                "ROC curves",
                "Precision-recall curves"
            ],
            "Create basic charts from a CSV dataset.",
            "Create an exploratory data analysis report.",
            "Build an interactive dashboard with important insights.",
            "Basic chart collection",
            "Exploratory data analysis dashboard",
            "Model performance dashboard"
        ),
        "Interactive Data Science Dashboard",
        "Create an interactive dashboard showing dataset insights and machine learning model performance."
    )

]


# ==========================================================
# 6. DATA ANALYST ROADMAP
# ==========================================================

DATA_ANALYST = [

    create_skill(
        "Excel",
        "Use spreadsheets for data cleaning, calculations and reporting.",
        create_levels(
            [
                "Workbook and worksheet basics",
                "Rows, columns and cells",
                "Cell references",
                "SUM and AVERAGE",
                "MIN and MAX",
                "Sorting and filtering"
            ],
            [
                "IF and nested IF",
                "COUNTIF and SUMIF",
                "VLOOKUP and XLOOKUP",
                "PivotTables",
                "Conditional formatting",
                "Data validation"
            ],
            [
                "Power Query",
                "Advanced PivotTables",
                "Dashboard creation",
                "KPI tracking",
                "What-if analysis",
                "Data automation"
            ],
            "Create an expense sheet using basic formulas.",
            "Clean a sales dataset and create PivotTables.",
            "Build an interactive business dashboard.",
            "Monthly expense tracker",
            "Sales summary report",
            "Business KPI dashboard"
        ),
        "Excel Business Dashboard",
        "Create a sales dashboard with KPIs, charts, filters and PivotTables."
    ),

    create_skill(
        "SQL",
        "Extract and analyze business data from relational databases.",
        create_levels(
            [
                "Database fundamentals",
                "SELECT",
                "WHERE",
                "ORDER BY",
                "DISTINCT",
                "LIMIT"
            ],
            [
                "COUNT, SUM and AVG",
                "GROUP BY",
                "HAVING",
                "INNER JOIN",
                "LEFT JOIN",
                "CASE statements"
            ],
            [
                "Subqueries",
                "CTEs",
                "Window functions",
                "Date functions",
                "Data quality checks",
                "Query optimization"
            ],
            "Write basic SELECT queries.",
            "Join customer and order tables.",
            "Analyze customer trends using window functions.",
            "Basic database queries",
            "Sales analysis",
            "Customer behavior analysis"
        ),
        "SQL Business Analysis",
        "Analyze sales, customers and product performance using SQL."
    ),

    create_skill(
        "Statistics",
        "Interpret data and support decisions using statistical methods.",
        create_levels(
            [
                "Mean",
                "Median",
                "Mode",
                "Range",
                "Variance",
                "Standard deviation"
            ],
            [
                "Probability",
                "Normal distribution",
                "Sampling",
                "Correlation",
                "Percentage calculations",
                "Data distributions"
            ],
            [
                "Hypothesis testing",
                "Confidence intervals",
                "p-values",
                "A/B testing",
                "Statistical interpretation"
            ],
            "Calculate descriptive statistics manually.",
            "Compare two business groups using statistics.",
            "Interpret an A/B test and explain the findings.",
            "Student statistics report",
            "Business segment comparison",
            "A/B testing report"
        ),
        "Business Statistical Analysis",
        "Analyze business performance using descriptive and inferential statistics."
    ),

    create_skill(
        "Python",
        "Automate data analysis and perform data preparation.",
        create_levels(
            [
                "Python fundamentals",
                "Variables and data types",
                "Loops and conditions",
                "Functions",
                "Lists and dictionaries"
            ],
            [
                "NumPy",
                "Pandas",
                "Reading CSV and Excel",
                "Missing value handling",
                "Removing duplicates",
                "Data filtering"
            ],
            [
                "GroupBy operations",
                "Merging datasets",
                "Datetime operations",
                "Exploratory data analysis",
                "Reusable scripts"
            ],
            "Write a program that reads a CSV file.",
            "Clean and summarize data using Pandas.",
            "Automate a complete exploratory data analysis workflow.",
            "CSV summary script",
            "Data cleaning notebook",
            "Automated EDA report"
        ),
        "Python Data Analysis Project",
        "Use Python to clean, analyze and summarize a business dataset."
    ),

    create_skill(
        "Data Visualization",
        "Present findings using charts, reports and dashboards.",
        create_levels(
            [
                "Chart types",
                "Bar charts",
                "Line charts",
                "Pie charts",
                "Histograms",
                "Chart formatting"
            ],
            [
                "Power BI fundamentals",
                "Data import",
                "Data relationships",
                "Calculated columns",
                "Measures",
                "Filters and slicers"
            ],
            [
                "Dashboard storytelling",
                "KPI development",
                "Interactive dashboards",
                "Drill-down analysis",
                "Report publishing"
            ],
            "Create charts from a small dataset.",
            "Build a Power BI dashboard with filters.",
            "Create an interactive business performance report.",
            "Basic chart report",
            "Sales dashboard",
            "Executive business dashboard"
        ),
        "Business Intelligence Dashboard",
        "Develop a Power BI dashboard that communicates important business insights."
    )

]


# ==========================================================
# 7. MACHINE LEARNING ENGINEER ROADMAP
# ==========================================================

ML_ENGINEER = [

    create_skill(
        "Python",
        "Develop reliable and reusable Python applications.",
        create_levels(
            [
                "Python syntax",
                "Variables and data types",
                "Conditions and loops",
                "Functions",
                "Lists and dictionaries"
            ],
            [
                "Object-oriented programming",
                "Modules and packages",
                "Exception handling",
                "NumPy and Pandas",
                "Unit testing"
            ],
            [
                "Type hints",
                "Code optimization",
                "Logging",
                "Project architecture",
                "Reusable components"
            ],
            "Build a command-line Python application.",
            "Organize code into reusable modules.",
            "Create a tested Python package.",
            "Python utility script",
            "Reusable preprocessing module",
            "Python package"
        ),
        "Reusable ML Utility Package",
        "Build a reusable Python package for machine learning data preprocessing."
    ),

    create_skill(
        "Mathematics & Statistics",
        "Understand the mathematical foundations behind ML algorithms.",
        create_levels(
            [
                "Vectors",
                "Matrices",
                "Mean and variance",
                "Probability",
                "Functions"
            ],
            [
                "Matrix multiplication",
                "Derivatives",
                "Gradients",
                "Probability distributions",
                "Sampling"
            ],
            [
                "Gradient descent",
                "Loss functions",
                "Regularization",
                "Bias-variance trade-off",
                "Optimization"
            ],
            "Perform basic vector and matrix calculations.",
            "Visualize a loss function and its gradient.",
            "Implement gradient descent manually.",
            "Linear algebra exercises",
            "Loss function visualization",
            "Gradient descent implementation"
        ),
        "Gradient Descent Implementation",
        "Implement a simple optimization algorithm and visualize its convergence."
    ),

    create_skill(
        "Machine Learning",
        "Develop and optimize machine learning models.",
        create_levels(
            [
                "Supervised learning",
                "Unsupervised learning",
                "Linear regression",
                "Logistic regression",
                "Decision trees"
            ],
            [
                "Random forest",
                "Gradient boosting",
                "K-means clustering",
                "Feature engineering",
                "Cross-validation",
                "Model evaluation"
            ],
            [
                "Hyperparameter optimization",
                "Model calibration",
                "Feature importance",
                "SHAP concepts",
                "Model pipelines",
                "Data drift concepts"
            ],
            "Train a basic classification model.",
            "Compare multiple algorithms using cross-validation.",
            "Develop an optimized ML pipeline.",
            "Basic classifier",
            "Model comparison project",
            "Optimized prediction pipeline"
        ),
        "End-to-End ML Pipeline",
        "Build a reusable machine learning pipeline from preprocessing to model evaluation."
    ),

    create_skill(
        "Software Engineering",
        "Convert machine learning experiments into reliable software.",
        create_levels(
            [
                "Git fundamentals",
                "Command-line basics",
                "Python modules",
                "Project structure",
                "Code readability"
            ],
            [
                "REST API concepts",
                "Flask",
                "FastAPI",
                "Input validation",
                "Unit testing"
            ],
            [
                "Docker",
                "CI/CD fundamentals",
                "Logging",
                "Model versioning",
                "API monitoring"
            ],
            "Create a Git repository for a Python project.",
            "Build an API that returns ML predictions.",
            "Containerize and test the prediction API.",
            "Version-controlled script",
            "ML prediction API",
            "Dockerized ML service"
        ),
        "Machine Learning REST API",
        "Develop and test an API that accepts user input and returns model predictions."
    ),

    create_skill(
        "Cloud & Deployment",
        "Deploy machine learning applications and manage cloud resources.",
        create_levels(
            [
                "Cloud computing concepts",
                "Virtual machines",
                "Cloud storage",
                "Regions and availability zones",
                "Basic hosting"
            ],
            [
                "IAM fundamentals",
                "Object storage",
                "Cloud databases",
                "Application deployment",
                "Environment variables"
            ],
            [
                "Container registries",
                "Managed model serving",
                "Monitoring",
                "Logging",
                "Cost optimization"
            ],
            "Understand cloud compute and storage services.",
            "Deploy a simple application to a cloud environment.",
            "Deploy and monitor an ML prediction service.",
            "Cloud service overview",
            "Hosted application",
            "Deployed ML application"
        ),
        "Cloud-Hosted ML Application",
        "Deploy a machine learning API and make it accessible through a web application."
    )

]


# ==========================================================
# 8. SOFTWARE DEVELOPER ROADMAP
# ==========================================================

SOFTWARE_DEVELOPER = [

    create_skill(
        "Programming",
        "Develop strong programming fundamentals.",
        create_levels(
            [
                "Variables and data types",
                "Operators",
                "Conditional statements",
                "Loops",
                "Functions"
            ],
            [
                "Arrays and strings",
                "Collections",
                "Object-oriented programming",
                "Classes and objects",
                "Exception handling"
            ],
            [
                "Inheritance",
                "Polymorphism",
                "Abstraction",
                "Interfaces",
                "Debugging",
                "Unit testing"
            ],
            "Write programs using loops and conditions.",
            "Build an application using classes and objects.",
            "Create a tested application using OOP concepts.",
            "Number utility program",
            "Library management system",
            "Student management application"
        ),
        "Student Management Application",
        "Develop an application that manages student records using OOP and database concepts."
    ),

    create_skill(
        "Data Structures & Algorithms",
        "Solve programming problems efficiently.",
        create_levels(
            [
                "Time complexity",
                "Space complexity",
                "Arrays",
                "Strings",
                "Searching",
                "Sorting"
            ],
            [
                "Linked lists",
                "Stacks",
                "Queues",
                "Hash maps",
                "Binary trees",
                "Recursion"
            ],
            [
                "Graphs",
                "Graph traversal",
                "Heaps",
                "Dynamic programming",
                "Greedy algorithms"
            ],
            "Solve basic array and string problems.",
            "Implement stacks, queues and binary trees.",
            "Solve graph and dynamic programming problems.",
            "Array problem collection",
            "Data structure implementation",
            "Algorithm problem portfolio"
        ),
        "DSA Problem Portfolio",
        "Build a collection of well-documented algorithm solutions with time and space complexity."
    ),

    create_skill(
        "Database & SQL",
        "Store and retrieve application data efficiently.",
        create_levels(
            [
                "Database concepts",
                "Tables and records",
                "Primary keys",
                "Foreign keys",
                "SELECT queries"
            ],
            [
                "Joins",
                "GROUP BY",
                "Normalization",
                "Indexes",
                "Transactions"
            ],
            [
                "Database design",
                "Query optimization",
                "Constraints",
                "Stored procedures",
                "Database migrations"
            ],
            "Create a database with related tables.",
            "Write queries involving multiple tables.",
            "Design a normalized application database.",
            "Student database",
            "Inventory database",
            "Application database design"
        ),
        "Database-Driven Application",
        "Build a database-backed application with CRUD operations and well-designed tables."
    ),

    create_skill(
        "Web Development",
        "Develop responsive frontend and backend applications.",
        create_levels(
            [
                "HTML",
                "CSS",
                "JavaScript fundamentals",
                "Forms",
                "HTML elements"
            ],
            [
                "Flexbox",
                "CSS Grid",
                "DOM manipulation",
                "JavaScript events",
                "REST APIs",
                "Form validation"
            ],
            [
                "Frontend and backend integration",
                "Authentication concepts",
                "Responsive design",
                "Accessibility",
                "Application testing"
            ],
            "Build a personal portfolio webpage.",
            "Develop a responsive form-based application.",
            "Connect a frontend to a backend API.",
            "Personal profile webpage",
            "Responsive registration page",
            "Full-stack CRUD application"
        ),
        "Full-Stack Web Application",
        "Develop a complete web application with frontend, backend and database integration."
    ),

    create_skill(
        "Version Control & Testing",
        "Manage code changes and maintain software quality.",
        create_levels(
            [
                "Git installation",
                "git init",
                "git add",
                "git commit",
                "GitHub basics"
            ],
            [
                "Branches",
                "Merge",
                "Conflict resolution",
                "Pull requests",
                "Unit testing"
            ],
            [
                "Integration testing",
                "Code reviews",
                "Release tags",
                "Continuous integration",
                "Automated testing"
            ],
            "Create a Git repository and commit code.",
            "Practise branches and pull requests.",
            "Create an automated test workflow.",
            "Git practice repository",
            "Collaborative coding exercise",
            "Tested software release"
        ),
        "Tested Software Project",
        "Create a version-controlled application with automated tests and clear documentation."
    )

]


# ==========================================================
# 9. CYBERSECURITY ANALYST ROADMAP
# ==========================================================

CYBERSECURITY_ANALYST = [

    create_skill(
        "Networking",
        "Understand network communication and protocols.",
        create_levels(
            [
                "OSI model",
                "TCP/IP model",
                "IP addressing",
                "Subnet basics",
                "DNS and DHCP"
            ],
            [
                "HTTP and HTTPS",
                "Common ports",
                "Routing",
                "Switching",
                "Firewalls"
            ],
            [
                "VPN concepts",
                "Network segmentation",
                "TLS fundamentals",
                "Packet analysis",
                "Network troubleshooting"
            ],
            "Identify common network protocols and ports.",
            "Inspect sample network packet captures.",
            "Document a small network's security boundaries.",
            "Protocol reference sheet",
            "Packet analysis exercise",
            "Network security diagram"
        ),
        "Network Security Analysis",
        "Analyze a sample network and document its important security controls."
    ),

    create_skill(
        "Linux & Operating Systems",
        "Use Linux tools to inspect systems and understand security.",
        create_levels(
            [
                "Linux installation",
                "Directory navigation",
                "File management",
                "Users and groups",
                "File permissions"
            ],
            [
                "Process management",
                "Package management",
                "SSH concepts",
                "Shell commands",
                "System logs"
            ],
            [
                "Bash scripting",
                "System hardening",
                "Scheduled tasks",
                "Audit logs",
                "Access control"
            ],
            "Practise basic Linux terminal commands.",
            "Inspect system logs and permissions.",
            "Create a script to summarize selected system events.",
            "Linux command notes",
            "Log inspection exercise",
            "System audit script"
        ),
        "Linux Security Audit",
        "Create a report describing permissions, users and selected system events in a test environment."
    ),

    create_skill(
        "Security Fundamentals",
        "Understand defensive security principles and common threats.",
        create_levels(
            [
                "CIA triad",
                "Threats and vulnerabilities",
                "Risk concepts",
                "Authentication",
                "Authorization"
            ],
            [
                "Malware concepts",
                "Phishing awareness",
                "Encryption",
                "Hashing",
                "Multi-factor authentication",
                "Vulnerability management"
            ],
            [
                "Incident response",
                "Security policies",
                "Risk assessment",
                "Security frameworks",
                "Backup and recovery"
            ],
            "Identify common security risks in example scenarios.",
            "Create a basic asset and vulnerability register.",
            "Prepare an incident response checklist for a simulated incident.",
            "Security awareness guide",
            "Risk register",
            "Incident response playbook"
        ),
        "Security Risk Assessment",
        "Prepare a defensive security assessment for a fictional organization's assets and risks."
    ),

    create_skill(
        "Python Scripting",
        "Automate safe defensive security analysis tasks.",
        create_levels(
            [
                "Python basics",
                "Variables and strings",
                "Lists and dictionaries",
                "Loops",
                "Functions"
            ],
            [
                "File handling",
                "Regular expressions",
                "CSV parsing",
                "JSON parsing",
                "Exception handling"
            ],
            [
                "Log parsing",
                "API usage",
                "Automation reports",
                "Logging",
                "Testing scripts"
            ],
            "Read a text file and count selected patterns.",
            "Parse a sample CSV log and summarize events.",
            "Generate a report from sanitized sample security logs.",
            "Text parser",
            "Log summarizer",
            "Security report generator"
        ),
        "Security Log Automation",
        "Develop a Python tool that analyzes sample security logs and generates a summary report."
    ),

    create_skill(
        "Log Analysis",
        "Understand system events and identify suspicious patterns.",
        create_levels(
            [
                "Log formats",
                "Timestamps",
                "Event severity",
                "Authentication events",
                "Normal activity patterns"
            ],
            [
                "Filtering and grouping",
                "Failed login patterns",
                "Time-window analysis",
                "Basic alert rules",
                "Event classification"
            ],
            [
                "Correlation across logs",
                "False positives",
                "SIEM concepts",
                "Incident documentation",
                "Detection rule evaluation"
            ],
            "Classify sample log entries.",
            "Identify repeated failed logins in sample logs.",
            "Create a basic detection rule and document its limitations.",
            "Log classification exercise",
            "Login anomaly analysis",
            "Mini detection report"
        ),
        "Security Event Analysis",
        "Analyze sample system logs and produce a report describing suspicious events."
    )

]


# ==========================================================
# 10. CLOUD ENGINEER ROADMAP
# ==========================================================

CLOUD_ENGINEER = [

    create_skill(
        "Linux",
        "Administer and troubleshoot Linux-based systems.",
        create_levels(
            [
                "Linux commands",
                "Filesystem navigation",
                "File permissions",
                "Users and groups",
                "Processes"
            ],
            [
                "Package managers",
                "SSH",
                "Disk usage",
                "System logs",
                "Bash scripting"
            ],
            [
                "Systemd services",
                "Resource monitoring",
                "System hardening",
                "Backup and recovery",
                "Troubleshooting"
            ],
            "Practise common terminal commands.",
            "Configure and inspect a service in a test VM.",
            "Create a server health-check script.",
            "Linux command worksheet",
            "Service configuration",
            "Server monitoring script"
        ),
        "Linux Server Administration",
        "Configure and monitor a test Linux server."
    ),

    create_skill(
        "Networking",
        "Understand cloud networking and connectivity.",
        create_levels(
            [
                "IP addressing",
                "Subnet basics",
                "DNS",
                "Ports",
                "Protocols"
            ],
            [
                "Routing",
                "NAT",
                "Gateways",
                "Firewalls",
                "Load balancing"
            ],
            [
                "VPC and VNet concepts",
                "Public and private subnets",
                "VPN concepts",
                "Network peering",
                "Troubleshooting"
            ],
            "Calculate simple subnet ranges.",
            "Draw a public and private network layout.",
            "Design a secure multi-tier network.",
            "Subnet exercises",
            "Network diagram",
            "Cloud network architecture"
        ),
        "Cloud Network Architecture",
        "Design a cloud network with secure public and private subnets."
    ),

    create_skill(
        "Cloud Platform",
        "Work with cloud compute, storage and identity services.",
        create_levels(
            [
                "Cloud computing concepts",
                "IaaS, PaaS and SaaS",
                "Regions",
                "Availability zones",
                "Virtual machines"
            ],
            [
                "Object storage",
                "IAM",
                "Cloud databases",
                "Cloud CLI",
                "Application deployment"
            ],
            [
                "Autoscaling",
                "High availability",
                "Backup and recovery",
                "Monitoring",
                "Cost optimization"
            ],
            "Explore basic cloud compute and storage services.",
            "Configure storage access using permissions.",
            "Design a resilient cloud application architecture.",
            "Cloud services overview",
            "Secure storage demonstration",
            "Cloud architecture diagram"
        ),
        "Cloud Application Architecture",
        "Design and deploy a small application using cloud compute and storage."
    ),

    create_skill(
        "Containers & DevOps",
        "Package applications and understand deployment workflows.",
        create_levels(
            [
                "Containers vs virtual machines",
                "Docker images",
                "Docker containers",
                "Dockerfile basics",
                "Ports and volumes"
            ],
            [
                "Docker Compose",
                "Environment variables",
                "Git branching",
                "CI/CD concepts",
                "Container networking"
            ],
            [
                "Kubernetes concepts",
                "Deployments",
                "Services",
                "Secrets and configuration",
                "Monitoring and rollback"
            ],
            "Containerize a simple Python application.",
            "Run an application and database using Compose.",
            "Deploy a sample service in a local Kubernetes environment.",
            "Single-container application",
            "Multi-container application",
            "Kubernetes deployment"
        ),
        "Containerized Application",
        "Build and deploy a multi-container application using Docker."
    ),

    create_skill(
        "Scripting",
        "Automate repeatable cloud and infrastructure tasks.",
        create_levels(
            [
                "Python or Bash basics",
                "Variables",
                "Loops",
                "Functions",
                "File handling"
            ],
            [
                "JSON",
                "REST APIs",
                "Cloud CLI",
                "Error handling",
                "Logging"
            ],
            [
                "Automation scripts",
                "Configuration management",
                "Idempotency",
                "Testing",
                "Documentation"
            ],
            "Write a script that checks local disk usage.",
            "Call an API and save its JSON response.",
            "Automate a deployment validation check.",
            "System checker",
            "API data collector",
            "Deployment validation script"
        ),
        "Cloud Automation Project",
        "Create a Python or Bash tool that performs a repeatable infrastructure check."
    )

]


# ==========================================================
# 11. BUSINESS ANALYST ROADMAP
# ==========================================================

BUSINESS_ANALYST = [

    create_skill(
        "Excel",
        "Prepare and analyze business information.",
        create_levels(
            [
                "Cell references",
                "Formatting",
                "SUM and AVERAGE",
                "COUNT",
                "Sorting and filtering"
            ],
            [
                "IF",
                "SUMIF and COUNTIF",
                "Lookup functions",
                "PivotTables",
                "Conditional formatting"
            ],
            [
                "Power Query",
                "Dashboard creation",
                "KPI tracking",
                "Scenario analysis",
                "Business reporting"
            ],
            "Create a simple expense tracker.",
            "Summarize sales data using PivotTables.",
            "Create an interactive business dashboard.",
            "Expense tracker",
            "Sales summary",
            "Business KPI dashboard"
        ),
        "Business Performance Dashboard",
        "Create an Excel dashboard that summarizes sales, revenue and business performance."
    ),

    create_skill(
        "SQL",
        "Answer business questions using structured data.",
        create_levels(
            [
                "SELECT",
                "WHERE",
                "ORDER BY",
                "DISTINCT",
                "Aggregate functions"
            ],
            [
                "GROUP BY",
                "HAVING",
                "JOINs",
                "CASE statements",
                "Subqueries"
            ],
            [
                "CTEs",
                "Window functions",
                "Date functions",
                "Data quality checks",
                "Query documentation"
            ],
            "Retrieve and filter database records.",
            "Calculate sales using joins and aggregation.",
            "Analyze repeat customers using window functions.",
            "Basic reporting queries",
            "Sales by customer report",
            "Customer retention report"
        ),
        "Business SQL Analysis",
        "Use SQL to investigate business performance and customer trends."
    ),

    create_skill(
        "Statistics",
        "Interpret business trends and support decisions.",
        create_levels(
            [
                "Mean, median and mode",
                "Percentages",
                "Ratios",
                "Range",
                "Standard deviation"
            ],
            [
                "Probability",
                "Sampling",
                "Correlation",
                "Trend analysis",
                "Seasonality"
            ],
            [
                "Confidence intervals",
                "Hypothesis testing",
                "A/B testing",
                "Statistical interpretation",
                "Avoiding misleading conclusions"
            ],
            "Calculate averages and percentage changes.",
            "Compare two business segments using statistics.",
            "Interpret an experiment and recommend an action.",
            "KPI calculation sheet",
            "Segment comparison",
            "Experiment analysis"
        ),
        "Business Statistics Report",
        "Analyze a business dataset and present statistical findings."
    ),

    create_skill(
        "Business Analysis",
        "Understand business problems and translate requirements into solutions.",
        create_levels(
            [
                "Stakeholder identification",
                "Problem statements",
                "Business requirements",
                "As-is processes",
                "To-be processes"
            ],
            [
                "User stories",
                "Acceptance criteria",
                "Process flowcharts",
                "Requirement gathering",
                "Prioritization"
            ],
            [
                "Gap analysis",
                "Root-cause analysis",
                "Use-case modelling",
                "Change impact analysis",
                "Requirements documentation"
            ],
            "Write a problem statement for a sample business process.",
            "Create user stories and a process flowchart.",
            "Prepare a requirements document with acceptance criteria.",
            "Problem brief",
            "Business process map",
            "Requirements specification"
        ),
        "Business Process Improvement",
        "Analyze an existing business process and propose an improved workflow."
    ),

    create_skill(
        "Communication",
        "Explain findings to technical and non-technical stakeholders.",
        create_levels(
            [
                "Professional communication",
                "Active listening",
                "Meeting notes",
                "Clear writing",
                "Asking questions"
            ],
            [
                "Presentation structure",
                "Explaining KPIs",
                "Executive summaries",
                "Stakeholder discussions",
                "Report writing"
            ],
            [
                "Data storytelling",
                "Recommendation framing",
                "Handling feedback",
                "Workshop facilitation",
                "Decision support"
            ],
            "Summarize a finding in five sentences.",
            "Present a dashboard in a short walkthrough.",
            "Deliver a recommendation supported by evidence.",
            "Insight summary",
            "Dashboard presentation",
            "Stakeholder recommendation"
        ),
        "Business Recommendation Presentation",
        "Present an evidence-based business recommendation using charts and analysis."
    )

]


# ==========================================================
# 12. UI/UX DESIGNER ROADMAP
# ==========================================================

UI_UX_DESIGNER = [

    create_skill(
        "Design Principles",
        "Create visually clear, consistent and accessible interfaces.",
        create_levels(
            [
                "Visual hierarchy",
                "Alignment",
                "Spacing",
                "Typography",
                "Colour theory"
            ],
            [
                "Layout grids",
                "Contrast",
                "Accessibility",
                "Responsive design",
                "Design systems"
            ],
            [
                "Information architecture",
                "Design critique",
                "Visual consistency",
                "Accessibility review",
                "Advanced layouts"
            ],
            "Redesign a simple information card.",
            "Create a consistent three-screen layout.",
            "Audit a page for hierarchy and accessibility.",
            "Card redesign",
            "Three-screen interface",
            "UI design audit"
        ),
        "Responsive UI Design",
        "Design a consistent, responsive interface for a small application."
    ),

    create_skill(
        "Figma & Design Tools",
        "Use design software to create reusable interface components.",
        create_levels(
            [
                "Frames and layers",
                "Shapes and text",
                "Images and assets",
                "Basic components",
                "Auto layout"
            ],
            [
                "Components and variants",
                "Constraints",
                "Responsive resizing",
                "Styles and variables",
                "Libraries"
            ],
            [
                "Advanced component systems",
                "Team collaboration",
                "Developer handoff",
                "Design documentation",
                "Reusable design systems"
            ],
            "Recreate a simple mobile screen.",
            "Build reusable buttons, inputs and cards.",
            "Prepare a component library for developer handoff.",
            "Mobile screen design",
            "UI component set",
            "Mini design system"
        ),
        "Figma Design System",
        "Build a small design system with reusable components and consistent styles."
    ),

    create_skill(
        "UX Research",
        "Understand user needs and validate design decisions.",
        create_levels(
            [
                "User-centred design",
                "Personas",
                "User interviews",
                "Observation",
                "User needs"
            ],
            [
                "Survey design",
                "User journeys",
                "Pain-point analysis",
                "Competitor analysis",
                "Research synthesis"
            ],
            [
                "Usability testing",
                "Task success measures",
                "Affinity mapping",
                "Research reporting",
                "Design validation"
            ],
            "Write interview questions for a sample application.",
            "Map a user journey and identify pain points.",
            "Conduct a small usability test and summarize findings.",
            "Interview guide",
            "User journey map",
            "Usability testing report"
        ),
        "UX Research Case Study",
        "Research a user problem and document findings, user journeys and design recommendations."
    ),

    create_skill(
        "Prototyping",
        "Create interactive prototypes to test user experiences.",
        create_levels(
            [
                "Sketching",
                "Wireframes",
                "Low-fidelity screens",
                "Navigation flows",
                "Screen states"
            ],
            [
                "Interactive links",
                "Forms and feedback states",
                "High-fidelity mockups",
                "Responsive variants",
                "Prototype interactions"
            ],
            [
                "Micro-interactions",
                "Prototype testing",
                "Feedback iteration",
                "Handoff specifications",
                "Interaction documentation"
            ],
            "Sketch a three-step user flow.",
            "Create a clickable prototype.",
            "Test and improve a prototype using user feedback.",
            "Wireframe collection",
            "Clickable prototype",
            "Tested interactive flow"
        ),
        "Interactive Application Prototype",
        "Design and test an interactive prototype for a real-world application."
    ),

    create_skill(
        "Communication",
        "Explain design decisions and collaborate with product teams.",
        create_levels(
            [
                "Presenting design ideas",
                "Organizing design files",
                "Receiving feedback",
                "Design annotations",
                "Clear explanations"
            ],
            [
                "Design rationale",
                "Developer collaboration",
                "Feedback prioritization",
                "Meeting facilitation",
                "Documentation"
            ],
            [
                "Portfolio storytelling",
                "Case study writing",
                "Trade-off explanation",
                "Cross-functional collaboration",
                "Design presentations"
            ],
            "Explain why you selected a particular layout.",
            "Prepare design annotations for developers.",
            "Create a portfolio case study explaining your design decisions.",
            "Design walkthrough",
            "Annotated design handoff",
            "UX portfolio case study"
        ),
        "UI/UX Portfolio Case Study",
        "Present a complete design project with research, wireframes, prototypes and final design decisions."
    )

]


# ==========================================================
# 13. COMPLETE CAREER SKILL TREE
# ==========================================================

CAREER_SYLLABI = {

    "Data Analyst": DATA_ANALYST,

    "Data Scientist": DATA_SCIENTIST,

    "Machine Learning Engineer": ML_ENGINEER,

    "Software Developer": SOFTWARE_DEVELOPER,

    "Cybersecurity Analyst": CYBERSECURITY_ANALYST,

    "Cloud Engineer": CLOUD_ENGINEER,

    "Business Analyst": BUSINESS_ANALYST,

    "UI/UX Designer": UI_UX_DESIGNER

}


# ==========================================================
# 14. GET CAREER SKILL TREE
# ==========================================================

def get_career_skill_tree(career):
    """
    Return all skill branches, levels, topics,
    exercises and projects for the selected career.
    """

    if career not in CAREER_SYLLABI:
        raise ValueError(
            f"No learning roadmap found for {career}"
        )

    return CAREER_SYLLABI[career]


# ==========================================================
# 15. GET AVAILABLE CAREERS
# ==========================================================

def get_available_careers():
    """
    Return the list of careers supported by the roadmap.
    """

    return list(CAREER_SYLLABI.keys())

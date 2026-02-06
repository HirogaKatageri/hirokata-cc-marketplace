# Develop Plugin

A Claude Code plugin for automated requirements-to-implementation workflows using a phase-based clean architecture approach.

## Overview

The **develop** plugin transforms requirements documents into working code through a structured, automated workflow. It analyzes requirements, creates implementation plans, organizes work into architectural phases, and spawns developer agents to implement features in parallel.

### Key Features

- **Automated Planning**: Converts requirements into comprehensive master plans
- **Phase-Based Architecture**: Organizes implementation into 7 sequential clean architecture phases
- **Feature Tracking**: Groups related tasks into feature tracks across phases
- **Complexity Scoring**: Analyzes task complexity for better estimation
- **Adaptive Parallelism**: Spawns 1-8 developer agents based on task complexity
- **Progress Tracking**: Integrates with tracker system for real-time visibility
- **Resume Capability**: Continue work from any point if interrupted

## Architecture

This plugin implements a **7-phase clean architecture** workflow:

```
Foundational → Models → Services → Data → Rules → State Management → UI
```

### The 7 Phases

1. **Foundational** - Base abstractions, utilities, infrastructure, and tooling setup
2. **Models** - Data entities, model classes, DTOs, and value objects
3. **Services** - External APIs, service integrations, and network layer
4. **Data** - Repositories, DAOs, data access layer, and local storage
5. **Rules** - Business logic, use cases, validation, and domain rules
6. **State Management** - View models, presenters, state handlers, and controllers
7. **UI** - Screens, components, views, and user interface

**Why This Order?**

Phases must be executed sequentially because each phase builds on the previous ones, following clean architecture dependency flow: UI depends on State Management, which depends on Rules, which depends on Data, and so on.

### Feature Tracks

**Tracks** represent complete features that span multiple phases:

- **authentication**: Login, signup, session management across all layers
- **profile**: User profile management from models to UI
- **products**: Product catalog from data to display
- **cart**: Shopping cart functionality end-to-end

Within each phase, tasks are organized by track. For example, Phase 2 (Models) might have:
- Track: authentication (User model, Token model)
- Track: products (Product model, Category model)
- Track: cart (CartItem model)

## Commands

### `/develop:develop-project`

Complete requirements-to-implementation workflow with 7-phase architecture.

**Usage:**
```
/develop:develop-project [file-path-or-query] [options]
```

**Arguments:**
- `[file-path-or-query]` - Path to requirements document (markdown) or search query (optional)
- `--max-parallel=N` - Override max parallel agents (1-8, default: adaptive)
- `--sequential` - Force sequential execution (1 agent at a time)
- `--aggressive` - Increase parallelism (1.5x multiplier)

**Examples:**
```bash
# Start with requirements file
/develop:develop-project requirements.md

# Search for requirements file
/develop:develop-project app-requirements

# Start with custom parallelism
/develop:develop-project requirements.md --max-parallel=4

# Start in sequential mode
/develop:develop-project requirements.md --sequential

# Start in aggressive mode (more parallel agents)
/develop:develop-project requirements.md --aggressive
```

**Workflow:**

1. **Parse arguments** and resolve requirements file path
2. **Plan Agent** creates comprehensive master plan from requirements
3. **User Reviews** and approves the master plan
4. **develop:development-planner Agent** analyzes master plan using `develop:split-plan` skill and organizes tasks into:
   - 7 sequential phases (Foundational → Models → Services → Data → Rules → State Management → UI)
   - Feature-based tracks (authentication, products, etc.)
   - Complexity scores for each task (1-3)
5. **tracker:tracker Agent** creates and populates tracker from phase plans
6. **Present analysis and select phases** - user reviews structure and chooses which phases to execute
7. **develop:senior-developer Agents** execute selected phases adaptively based on task complexity:
   - Phases run sequentially (1→2→3→4→5→6→7)
   - Within each phase, 1-8 agents run in parallel based on task complexity
   - Tracker updates in real-time
8. **Generate final summary report** with progress and next steps

**Files Generated:**
```
.trackers/{BASE_NAME}/
├── TRACKER.md                        # Progress tracker
└── plans/
    ├── {BASE_NAME}-master-plan.md         # Comprehensive master plan
    ├── {BASE_NAME}-DEPENDENCIES.md        # Dependency analysis
    ├── {BASE_NAME}-01-foundational.md     # Phase 1 plan
    ├── {BASE_NAME}-02-models.md           # Phase 2 plan
    ├── {BASE_NAME}-03-services.md         # Phase 3 plan
    ├── {BASE_NAME}-04-data.md             # Phase 4 plan
    ├── {BASE_NAME}-05-rules.md            # Phase 5 plan
    ├── {BASE_NAME}-06-state-management.md # Phase 6 plan
    ├── {BASE_NAME}-07-ui.md               # Phase 7 plan
    └── {BASE_NAME}-SUMMARY.md             # Summary report
```

## Skills

The plugin includes internal skills used by agents (not directly invokable by users):

### `develop:split-plan`

Analyzes a master plan file and splits it into 7 phase-specific implementation plans organized by feature tracks.

**Responsibilities:**
- Automatically identifies feature tracks
- Classifies tasks by phase
- Scores task complexity (1-3)
- Generates detailed phase plan files following clean architecture principles

### `develop:estimate-task`

Reference guide for scoring task complexity using a 3-level system (1=Low, 2=Medium, 3=High).

**Scoring System:**
- **Score 1 (Low)**: Simple, straightforward tasks (constants, simple models, documentation)
  - Examples: Add API constant, create basic model, update README
  - Estimated effort: Minutes to 1-2 hours
- **Score 2 (Medium)**: Implementation tasks requiring moderate effort (features, services, UI components)
  - Examples: Implement login service, create form with validation, build state management
  - Estimated effort: Half-day to 2 days
- **Score 3 (High)**: Complex architectural tasks (authentication systems, payment integration, real-time features)
  - Examples: Implement full auth system, integrate payment gateway, set up state framework
  - Estimated effort: 2+ days

**Used by:** development-planner agent during task complexity analysis

### `develop:categorize-task`

Reference guide for classifying development tasks into the 7-phase clean architecture structure.

**Classification System:**
- **Phase 1 (Foundational)**: Infrastructure, utilities, abstract classes, base setup
- **Phase 2 (Models)**: Entities, DTOs, data structures, value objects
- **Phase 3 (Services)**: External APIs, third-party integrations, network layer
- **Phase 4 (Data)**: Repositories, DAOs, data access, local storage
- **Phase 5 (Rules)**: Business logic, use cases, validation, domain rules
- **Phase 6 (State Management)**: View models, presenters, state handlers, controllers
- **Phase 7 (UI)**: Screens, components, views, user interface

**Used by:** development-planner agent during task organization

## Agents

### `develop:product-owner`

Transforms ambiguous ideas into well-structured requirements, user stories, and clear project scope.

**Responsibilities:**
- Translate feature requests into structured requirements
- Create comprehensive user stories with acceptance criteria
- Identify edge cases, dependencies, and constraints
- Define success metrics and KPIs
- Validate requirements against project patterns (CLAUDE.md)
- Bridge communication between business and technical stakeholders
- Ensure requirements are testable and complete

**Color:** Pink

**Model:** Haiku (fast, efficient for requirements gathering)

**Tools:** TaskCreate, TaskGet, TaskUpdate, TaskList, Glob, Grep, Read, WebFetch, WebSearch, ListMcpResourcesTool, ReadMcpResourceTool, Edit, Write, NotebookEdit, Bash

**Triggers:**
- When users describe new features without clear requirements
- When existing features need improvement or clarification
- When starting new project phases that need scope definition
- Can be invoked manually for requirements gathering

**Output Formats:**
- User Stories (primary): As a [role], I want [action], so that [value]
- Use Cases (secondary): Detailed workflow documentation for complex scenarios

### `develop:development-planner`

Analyzes master plans and organizes tasks into the 7-phase architecture with feature tracks using the `develop:split-plan` skill.

**Responsibilities:**
- Parse master plan files
- Identify feature tracks (authentication, products, etc.)
- Map tasks to appropriate phases using `develop:split-plan` skill
- Create phase-specific plan files (01-07)
- Add complexity scores to tasks (1-3)
- Generate dependency analysis
- Create tracker structure
- Present analysis for user review

**Color:** Orange

**Model:** Sonnet (comprehensive analysis and planning)

**Tools:** Read, Write, Edit, Glob, Grep, Bash, Skill, AskUserQuestion

**Skills:** develop:split-plan

**Triggers:**
- Called by `/develop:develop-project` command after master plan creation
- Can be invoked manually to analyze and split master plans

### `develop:senior-developer`

Implements features and writes production-ready code following project patterns.

**Responsibilities:**
- Review documentation and codebase patterns
- Implement tasks from phase plans
- Follow existing architectural decisions
- Write clean, maintainable code
- Handle errors appropriately
- Integrate with existing code
- Update tracker status as tasks complete

**Color:** Blue

**Model:** Sonnet (advanced code generation and reasoning)

**Tools:** TaskCreate, TaskGet, TaskUpdate, TaskList, Glob, Grep, Read, Write, Edit, NotebookEdit, Bash, Skill, AskUserQuestion

**Triggers:**
- Spawned by `/develop:develop-project` command during phase execution
- 1-8 agents run in parallel per phase based on task complexity
- Can be invoked manually for specific implementation tasks

## Complexity Scoring

Tasks are assigned complexity scores to determine optimal parallelism:

### Low Complexity (Score: 1)
Simple, straightforward tasks:
- Add constants or configuration
- Create simple model classes
- Add utility functions
- Update documentation

**Parallelism:** Up to 10 agents

### Medium Complexity (Score: 2)
Implementation tasks requiring moderate effort:
- Implement new features
- Create services with multiple methods
- Build UI components
- Implement repository patterns
- Add validation logic

**Parallelism:** Up to 5 agents

### High Complexity (Score: 3)
Complex or architectural tasks:
- Implement authentication systems
- Set up state management frameworks
- Integrate payment gateways
- Implement real-time features
- Complex business logic

**Parallelism:** Up to 3 agents

## Adaptive Parallelism

The plugin automatically calculates optimal parallel agent count based on task complexity:

```
BASE_PARALLEL = floor(10.0 / AVG_COMPLEXITY)
```

**Modes:**

1. **Normal Mode** (default)
   - Adaptive based on complexity
   - Example: Avg complexity 2.0 → 5 agents

2. **Sequential Mode** (`--sequential`)
   - Forces 1 agent at a time
   - Best for debugging or limited resources

3. **Aggressive Mode** (`--aggressive`)
   - 1.5x parallelism multiplier
   - Example: Base 5 agents → 7 agents
   - Best for powerful machines

4. **Override Mode** (`--max-parallel=N`)
   - User-specified parallelism (1-8)
   - Respects task count and complexity constraints

## Example Usage

### Complete Workflow

```bash
# 1. Start with requirements
/develop:develop-project requirements/my-app.md

# The plugin will:
# - Create master plan using Plan agent
# - Wait for your review and approval
# - Analyze with develop:development-planner agent using develop:split-plan skill
# - Show you the phase/track structure
# - Ask for phase selection
# - Begin implementation phase by phase with develop:senior-developer agents

# 2. Monitor progress
# Tracker updates show in terminal as work progresses

# 3. View tracker status anytime
/tracker:review-tracker my-app

# 4. If needed, rerun with different parallelism
/develop:develop-project requirements/my-app.md --max-parallel=2
```

### Starting with Options

```bash
# Conservative approach (sequential)
/develop:develop-project requirements.md --sequential

# Aggressive approach (more parallelism)
/develop:develop-project requirements.md --aggressive

# Controlled parallelism
/develop:develop-project requirements.md --max-parallel=3

# Interactive mode (prompts for file)
/develop:develop-project
```

## Installation

### Local Development

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd cc-develop-plugin
   ```

2. Use the plugin with Claude Code:
   ```bash
   cc --plugin-dir /path/to/cc-develop-plugin
   ```

### Project-Specific

1. Copy plugin to your project:
   ```bash
   cp -r cc-develop-plugin /path/to/your-project/.claude-plugin/develop
   ```

2. The plugin will be automatically loaded by Claude Code

## Requirements

- **Claude Code**: Latest version
- **Tracker System**: Plugin integrates with tracker commands (create-tracker, add-task, mark-status, review-tracker)
- **Plan Agent**: Claude Code's built-in Plan agent for master plan creation
- **Requirements Format**: Markdown files with clear feature descriptions

## Best Practices

### Requirements Documents

Structure your requirements for best results:

```markdown
# Project Requirements

## Overview
Brief description of the project

## Features

### Feature 1: User Authentication
- User can sign up with email/password
- User can log in
- Sessions are maintained
- Passwords are securely hashed

### Feature 2: Product Catalog
- Display list of products
- Filter by category
- Search by name
- View product details

## Technical Requirements
- Use JWT for authentication
- RESTful API architecture
- PostgreSQL database
- React frontend
```

### Resuming Work

- The plugin tracks progress automatically
- You can pause at any time (Ctrl+C)
- Resume picks up exactly where you left off
- Blocked tasks can be retried or skipped

### Reviewing Plans

Always review the master plan and phase structure before execution:
- Verify feature groupings make sense
- Check task assignments to phases
- Confirm complexity scores are reasonable
- Adjust if needed before proceeding

## File Structure

```
cc-develop-plugin/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   ├── product-owner.md         # Product owner agent (NEW in 0.1.1)
│   ├── development-planner.md   # Development planner agent
│   └── senior-developer.md      # Senior developer agent
├── commands/
│   └── develop-project.md       # Main workflow command
├── skills/
│   ├── split-plan/              # Split master plan into phases
│   ├── estimate-task/           # Task estimation
│   └── categorize-task/         # Task categorization
├── .gitignore
├── LICENSE                      # MIT License
└── README.md                   # This file
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Claude Code
5. Submit a pull request

## License

MIT License - See LICENSE file for details.

## Author

**Gian Patrick Quintana**
- Email: gian.quintana@hirokata.dev
- GitHub: [@hirogakatageri](https://github.com/hirogakatageri)

## Support

For issues, questions, or feature requests:
1. Open an issue on the repository
2. Provide details about your use case
3. Include relevant error messages or logs

## Changelog

### 0.1.1
- **New Agent: product-owner** - Expert requirements engineering agent for translating ideas into structured user stories
  - Proactive engagement when users describe new features
  - Comprehensive requirements gathering with edge cases and acceptance criteria
  - Integration with project context (CLAUDE.md) for pattern alignment
  - Support for both User Stories and Use Cases formats
  - Quality gates for testable, measurable requirements
- Enhanced agent ecosystem with specialized roles (product-owner, development-planner, senior-developer)

### 0.1.0 (Initial Release)
- Phase-based requirements-to-implementation workflow
- Development planner agent for plan analysis and task organization
- Senior developer agent for implementation
- Start and resume commands
- Adaptive parallelism based on complexity
- Tracker integration for progress management

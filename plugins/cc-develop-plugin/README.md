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

## Skills

### `/develop:start`

Start a new requirements-to-implementation workflow.

**Usage:**
```
/develop:start <requirements-file> [options]
```

**Arguments:**
- `<requirements-file>` - Path to requirements document (markdown) or search query
- `--max-parallel=N` - Override max parallel agents (1-8, default: adaptive)
- `--sequential` - Force sequential execution (1 agent at a time)
- `--aggressive` - Increase parallelism (1.5x multiplier)

**Examples:**
```bash
# Start with requirements file
/develop:start requirements.md

# Search for requirements file
/develop:start app-requirements

# Start with custom parallelism
/develop:start requirements.md --max-parallel=4

# Start in sequential mode
/develop:start requirements.md --sequential

# Start in aggressive mode (more parallel agents)
/develop:start requirements.md --aggressive
```

**Workflow:**

1. **Plan Agent** creates comprehensive master plan from requirements
2. **User Reviews** and approves the master plan
3. **Phase-Architect Agent** analyzes master plan and organizes tasks into:
   - 7 sequential phases (Foundational → Models → Services → Data → Rules → State Management → UI)
   - Feature-based tracks (authentication, products, etc.)
   - Complexity scores for each task (1-3)
4. **Tracker Agent** initializes progress tracking
5. **User Confirms** phase/track structure
6. **Senior-Developer Agents** execute implementation:
   - Phases run sequentially (1→2→3→4→5→6→7)
   - Within each phase, 1-8 agents run in parallel based on task complexity
   - Tracker updates in real-time
7. **Summary Report** generated on completion

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

### `/develop:resume`

Resume implementation from an existing tracker.

**Usage:**
```
/develop:resume <tracker-name> [options]
```

**Arguments:**
- `<tracker-name>` - Name of existing tracker (BASE_NAME)
- `--max-parallel=N` - Override max parallel agents (1-8, default: adaptive)
- `--sequential` - Force sequential execution (1 agent at a time)
- `--aggressive` - Increase parallelism (1.5x multiplier)

**Examples:**
```bash
# Resume from tracker
/develop:resume app-v1

# Resume with custom parallelism
/develop:resume app-v1 --max-parallel=4

# Resume in sequential mode
/develop:resume app-v1 --sequential
```

**Workflow:**

1. **Reads tracker** state to identify incomplete work
2. **Presents status** to user (completed, pending, blocked tasks)
3. **User selects** which phases to resume
4. **Senior-Developer Agents** continue implementation from incomplete phases
5. **Tracker updates** in real-time
6. **Progress report** generated on completion or pause

## Agents

### `phase-architect`

Analyzes master plans and organizes tasks into the 7-phase architecture with feature tracks.

**Responsibilities:**
- Parse master plan files
- Identify feature tracks (authentication, products, etc.)
- Map tasks to appropriate phases
- Create phase-specific plan files (01-07)
- Add complexity scores to tasks (1-3)
- Generate dependency analysis
- Create summary reports

**Color:** Purple

**Triggers:**
- Called by `/develop:start` skill after master plan creation
- Can be invoked manually to re-analyze a master plan

### `senior-developer`

Implements features and writes production-ready code following project patterns.

**Responsibilities:**
- Review documentation and codebase patterns
- Implement tasks from phase plans
- Follow existing architectural decisions
- Write clean, maintainable code
- Handle errors appropriately
- Integrate with existing code

**Color:** Blue

**Triggers:**
- Spawned by `/develop:start` and `/develop:resume` skills
- 1-8 agents run in parallel per phase based on complexity
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
/develop:start requirements/my-app.md

# The plugin will:
# - Create master plan using Plan agent
# - Wait for your review and approval
# - Analyze with phase-architect agent
# - Show you the phase/track structure
# - Ask for confirmation
# - Begin implementation phase by phase

# 2. Monitor progress
# Tracker updates show in terminal as work progresses

# 3. If interrupted, resume later
/develop:resume my-app

# 4. Continue from incomplete phases
# Select which phases to resume
```

### Starting with Options

```bash
# Conservative approach (sequential)
/develop:start requirements.md --sequential

# Aggressive approach (more parallelism)
/develop:start requirements.md --aggressive

# Controlled parallelism
/develop:start requirements.md --max-parallel=3
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
│   └── plugin.json          # Plugin manifest
├── agents/
│   ├── phase-architect.md   # Phase architect agent
│   └── senior-developer.md  # Senior developer agent
├── commands/
│   ├── start.md            # Start command
│   └── resume.md           # Resume command
├── .gitignore
├── LICENSE                  # MIT License
└── README.md               # This file
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Author

**hirogakatageri**
- Email: gian.quintana@hirokata.dev

## Support

For issues, questions, or feature requests:
1. Open an issue on the repository
2. Provide details about your use case
3. Include relevant error messages or logs

## Changelog

### 0.1.0 (Initial Release)
- Phase-based requirements-to-implementation workflow
- Product owner agent for plan analysis
- Senior developer agent for implementation
- Start and resume commands
- Adaptive parallelism based on complexity
- Tracker integration for progress management

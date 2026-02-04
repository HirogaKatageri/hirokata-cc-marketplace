---
name: develop-project
description: Full requirements-to-implementation workflow with 7-phase architecture, automated planning, complexity analysis, and adaptive parallel execution
arguments:
  - name: file-path-or-query
    description: Path to requirements markdown file, or search query to find file
    required: false
    type: string
  - name: max-parallel
    description: Override max parallel agents (1-8)
    required: false
    type: number
  - name: sequential
    description: Force sequential execution (parallel=1)
    required: false
    flag: true
  - name: aggressive
    description: Increase parallelism (1.5x multiplier)
    required: false
    flag: true
examples:
  - "/develop-project requirements.md"
  - "/develop-project app-requirements --sequential"
  - "/develop-project requirements.md --max-parallel=4"
  - "/develop-project requirements.md --aggressive"
---

# Develop Project Workflow Command

You are automating a complete requirements-to-implementation workflow with a structured phase-based architecture. This command takes a requirements document, creates a master plan using a planning agent, analyzes the master plan with a split-plan skill to organize tasks into phases and tracks, creates implementation plans, executes those plans, and tracks progress using the tracker agent.

## Your Task

Process a requirements document through this 8-step workflow:
1. **Parse arguments** and resolve requirements file path
2. **Plan agent** creates a comprehensive master plan
3. **User reviews** and approves the master plan
4. **develop:development-planner agent** analyzes master plan using split-plan skill and organizes tasks into **predefined phases** (Foundational → Models → Services → Data → Rules → State Management → UI) and **feature-based tracks** (authentication, profile, products, etc.)
5. **Tracker agent** creates and populates tracker from phase plans
6. **Present analysis and select phases** - user reviews structure and chooses which phases to execute
7. **develop:senior-developer agents** execute selected phases adaptively based on task complexity
8. **Generate final summary report** with progress and next steps

## Phase Architecture

The start command uses a **fixed, sequential phase structure** that represents a clean architecture approach:

1. **Foundational Phase** - Abstract classes, toolings, utilities, base setup
2. **Models Phase** - Entities, models, JSON classes, data structures
3. **Services Phase** - APIs, external services, network layer
4. **Data Phase** - Repositories, DAOs, data access layer
5. **Rules Phase** - Use cases, business rules, domain logic
6. **State Management Phase** - View models, presenters, state handlers
7. **UI Phase** - Widgets, components, screens, views

**Tracks** within each phase represent **features** being built:
- Example tracks: "authentication", "profile", "products", "cart", "notifications", etc.
- Tasks within a track across different phases build the complete feature

**File Naming Convention**: Use zero-padded short format: `{BASE_NAME}-{NN}-{name}.md` where NN is 01-07.

## Progress Tracking

**CRITICAL**: Before starting Step 1, create all workflow tasks using the **TaskCreate** tool to provide visual progress indicators to the user.

Create these tasks at the start of execution:

1. **Task 1**: "Parse arguments and resolve requirements file"
   - subject: "Parse arguments and resolve requirements file"
   - description: "Parse command-line arguments, extract file path and options, resolve requirements file path"
   - activeForm: "Parsing arguments and resolving requirements file"

2. **Task 2**: "Generate master plan from requirements"
   - subject: "Generate master plan from requirements"
   - description: "Spawn Plan agent to analyze requirements and create comprehensive master implementation plan"
   - activeForm: "Generating master plan from requirements"

3. **Task 3**: "Review master plan with user"
   - subject: "Review master plan with user"
   - description: "Present master plan to user for review, approval, or edits before proceeding"
   - activeForm: "Reviewing master plan with user"

4. **Task 4**: "Split master plan into phase plans"
   - subject: "Split master plan into phase plans"
   - description: "Use develop:development-planner agent to organize tasks into 7 phase-specific plans with tracks and complexity scores"
   - activeForm: "Splitting master plan into phase plans"

5. **Task 5**: "Create and populate tracker"
   - subject: "Create and populate tracker"
   - description: "Create tracker and populate with all phases, tracks, and tasks from phase plans"
   - activeForm: "Creating and populating tracker"

6. **Task 6**: "Present analysis and select phases"
   - subject: "Present analysis and select phases"
   - description: "Present phase/track structure, get confirmation on organization, and select phases for execution"
   - activeForm: "Presenting analysis and selecting phases"

7. **Task 7**: "Execute selected phases"
   - subject: "Execute selected phases"
   - description: "Execute implementation for selected phases using develop:senior-developer agents"
   - activeForm: "Executing selected phases"

8. **Task 8**: "Generate final summary report"
   - subject: "Generate final summary report"
   - description: "Create comprehensive summary report with progress, files, and next steps"
   - activeForm: "Generating final summary report"

**At the start of each step**: Use **TaskUpdate** to mark the corresponding task as `in_progress`.

**At the end of each step**: Use **TaskUpdate** to mark the task as `completed`.

This gives users real-time visibility into workflow progress.

## Process Flow

### Step 1: Parse Arguments and Resolve Requirements File Path

**Before starting**: Use **TaskUpdate** to set Task 1 status to `in_progress`

**CRITICAL**: Parse $ARGUMENTS to extract file path and execution options, then resolve the file path to an actual file.

1. **Parse $ARGUMENTS format**:
   ```
   Format: <file-path-or-search-query> [options]

   The first argument can be:
   - An exact file path (e.g., "requirements/app-requirements.md")
   - A search query to find markdown files (e.g., "app", "requirements")

   Options:
   --max-parallel=N      Override max parallel agents (default: adaptive, range: 1-8)
   --sequential          Force sequential execution (parallel=1)
   --aggressive          Increase parallelism (1.5x multiplier on calculated value)

   Examples:
   /develop-project requirements.md
   /develop-project app-requirements
   /develop-project requirements/app.md --max-parallel=4
   /develop-project requirements.md --sequential
   /develop-project requirements.md --aggressive
   ```

2. **Extract configuration from arguments**:
   - Parse the file path or search query (first argument) → `FILE_PATH_OR_QUERY`
   - Parse optional flags:
     * `MAX_PARALLEL_OVERRIDE` = value from --max-parallel=N flag (or null if not provided)
     * `FORCE_SEQUENTIAL` = true if --sequential flag present
     * `AGGRESSIVE_MODE` = true if --aggressive flag present

3. **Validate flags**:
   - If MAX_PARALLEL_OVERRIDE is set, ensure it's between 1 and 8
   - If FORCE_SEQUENTIAL and MAX_PARALLEL_OVERRIDE both set, FORCE_SEQUENTIAL takes precedence
   - Warn about unrecognized flags (continue with valid flags only)

4. **Handle missing file path**:
   - If `FILE_PATH_OR_QUERY` is empty or not provided:
     * Ask the user: "Please provide the name or path to your requirements file."
     * Wait for the user's response
     * Use the provided response as `FILE_PATH_OR_QUERY`

5. **Resolve the file path**:

   a. **Try as exact file path first**:
      - Use the Read tool to try reading the file at `FILE_PATH_OR_QUERY`
      - If the file exists and can be read:
        * Set `RESOLVED_FILE_PATH = FILE_PATH_OR_QUERY`
        * Skip to step 6

   b. **If exact path fails, treat as search query**:
      - Use the Glob tool to search for markdown files:
        * Pattern 1: `**/*{FILE_PATH_OR_QUERY}*.md` (fuzzy match)
        * Pattern 2: `**/{FILE_PATH_OR_QUERY}` (exact filename)
      - Combine and deduplicate the results

   c. **Handle search results**:
      - If **no files found**:
        * Inform the user: "No markdown files found matching '{FILE_PATH_OR_QUERY}'"
        * Ask the user: "Please provide a different file name or path."
        * Wait for user's response, set as new `FILE_PATH_OR_QUERY`
        * Repeat from step 5a

      - If **exactly one file found**:
        * Set `RESOLVED_FILE_PATH` to the found file path
        * Inform the user: "Found file: {RESOLVED_FILE_PATH}"
        * Continue to step 6

      - If **multiple files found**:
        * Present the list to the user (limit to first 20 if > 20 results):
          ```
          Multiple markdown files found matching '{FILE_PATH_OR_QUERY}':

          1. {file_path_1}
          2. {file_path_2}
          3. {file_path_3}
          ...

          Which file would you like to use? (Enter the number or provide a more specific search query)
          ```
        * Wait for user's response
        * If user enters a number:
          - Validate number is between 1 and file_count
          - Set `RESOLVED_FILE_PATH` to the corresponding file
          - Continue to step 6
        * If user provides text:
          - Set `FILE_PATH_OR_QUERY` to the new text
          - Repeat from step 5a

6. **Validate resolved file**:
   - Verify file is markdown (.md extension)
   - Check file has content (not empty)
   - If validation fails, ask user for different file and repeat from step 5a

7. **Configuration complete**:
   Store final configuration:
   - `RESOLVED_FILE_PATH`: The validated requirements file path
   - `MAX_PARALLEL_OVERRIDE`: User's override value (1-8, or null)
   - `FORCE_SEQUENTIAL`: Boolean
   - `AGGRESSIVE_MODE`: Boolean

**After completing Step 1**: Use **TaskUpdate** to set Task 1 status to `completed`

8. Continue to Step 2 (Generate Master Plan)

### Step 2: Generate Master Plan from Requirements

**Before starting**: Use **TaskUpdate** to set Task 2 status to `in_progress`

**CRITICAL**: Use a planning agent to analyze requirements and create a comprehensive master plan, then write it directly to a file.

1. Read the input file from `RESOLVED_FILE_PATH` (the file path resolved in Step 1)

2. **Extract base name for unique naming**:
   - Get the filename from the path (e.g., `requirements/app-v1.md` → `app-v1.md`)
   - Remove the extension (e.g., `app-v1.md` → `app-v1`)
   - Store this as `BASE_NAME` to use for:
     * Tracker name
     * Plan file prefixes
     * Master plan filename
     * All generated filenames
   - This ensures different requirements don't overwrite each other's files

3. **Create directory structure**:
   ```bash
   mkdir -p .trackers/{BASE_NAME}/plans
   ```

4. **Spawn a Plan agent to create implementation strategy**:

   ```
   <Task tool call>
     subagent_type: "Plan"
     description: "Create master implementation plan"
     prompt: "Analyze the requirements document and create a comprehensive master implementation plan.

     ## Requirements File
     Read and analyze: {RESOLVED_FILE_PATH}

     ## Your Task
     Create a detailed master plan that:

     1. **Analyzes all requirements** and extracts:
        - Feature descriptions
        - User stories
        - Acceptance criteria
        - Functional requirements
        - Non-functional requirements
        - Technical constraints

     2. **Identifies discrete tasks** for implementation:
        - Break down features into actionable tasks
        - Include task titles and descriptions
        - Specify acceptance criteria for each task
        - Note any dependencies between tasks
        - Consider technical architecture implications

     3. **Provides implementation guidance**:
        - Suggest architectural patterns
        - Identify technical challenges
        - Recommend technology/framework choices
        - Note security and performance considerations

     4. **Organizes logically**:
        - Group related tasks together
        - Show clear progression from foundation to UI
        - Highlight critical paths and dependencies

     **CRITICAL**: Return the COMPLETE master plan content in your response as a well-structured markdown document. DO NOT save the file yourself (you don't have Write access).

     Format your response as a comprehensive master plan ready to be saved to:
     `.trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md`"
   </Task>
   ```

5. Wait for the Plan agent to complete and return the master plan content

6. **Extract the master plan content** from the Plan agent's response

7. **Write the master plan to file directly**:
   - Use the Write tool to save the master plan content to:
     `.trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md`

8. Inform user:
   ```
   Master plan created and saved!

   **File**: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md
   **Source Requirements**: {RESOLVED_FILE_PATH}

   The master plan analyzes your requirements and provides a comprehensive implementation strategy.
   ```

**After completing Step 2**: Use **TaskUpdate** to set Task 2 status to `completed`

9. Continue to Step 3

### Step 3: Review Master Plan

**Before starting**: Use **TaskUpdate** to set Task 3 status to `in_progress`

**CRITICAL**: Before proceeding with split-plan analysis, ALWAYS present the master plan to the user for review and get confirmation.

1. **Read the master plan file**:
   - File: `.trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md`

2. **Present master plan summary to user**:
   ```
   Master plan created! Before organizing into phases, let's review the plan.

   **File**: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md
   **Source Requirements**: {RESOLVED_FILE_PATH}

   **Master Plan Summary**:
   [Show a brief overview of:
    - Key features identified
    - Major task groups
    - Suggested architecture
    - Total estimated tasks
   ]

   Questions:
   1. Would you like to review the full master plan before I organize it into phases?
   2. Are there any changes or adjustments needed to the plan?
   3. Should I proceed with the split-plan workflow to organize this into the 7-phase architecture?

   Options:
   - Type "proceed" to continue with split-plan workflow
   - Type "review" to see the full master plan details
   - Type "edit" to make changes to the master plan
   ```

3. **Wait for user response**:

   - If **"proceed"**: Continue to Step 4 (Split Plan Analysis)

   - If **"review"**:
     * Read and display the full master plan file content to the user
     * Ask again: "Would you like to proceed with split-plan workflow, or edit the master plan?"
     * Wait for response (proceed/edit)

   - If **"edit"**:
     * Inform user: "Please edit the master plan file at: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md"
     * Wait for user to confirm edits are complete
     * Re-read the updated master plan file
     * Ask: "Master plan updated. Would you like to proceed with split-plan workflow?"
     * Wait for response (proceed)

4. Once user confirms "proceed", continue to Step 4

**After completing Step 3**: Use **TaskUpdate** to set Task 3 status to `completed`

**IMPORTANT**: This step ensures user has reviewed and approved the master plan before the split-plan skill organizes it into phases.

### Step 4: Split Master Plan into Phase Plans

**Before starting**: Use **TaskUpdate** to set Task 4 status to `in_progress`

**CRITICAL**: Use the develop:development-planner agent to analyze the master plan and organize it into the 7-phase architecture with feature tracks.

1. **Spawn the develop:development-planner agent** using the Task tool:

   ```
   <Task tool call>
     subagent_type: "develop:development-planner"
     description: "Create phase plans from master plan"
     prompt: "Analyze the master plan and split it into 7 phase-specific implementation plans.

     ## Master Plan Location
     File: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md

     ## Base Name
     Use base name: {BASE_NAME}

     ## Your Task

     Use the split-plan skill to:
     1. Read and analyze the entire master plan
     2. Identify feature tracks that span multiple phases
     3. Map tasks to appropriate phases using phase classification
     4. Score task complexity (1-3)
     5. Generate all 7 phase plan files with detailed task descriptions
     6. Verify all files were created successfully
     7. Report completion status with statistics

     Execute the split-plan skill with:
     - master-plan-path: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md
     - base-name: {BASE_NAME}

     After the split-plan skill completes, provide a comprehensive summary of:
     - All 7 phase plan files created
     - Feature tracks identified
     - Task distribution across phases
     - Complexity distribution

     Report the complete analysis so we can proceed to tracker creation."
   </Task>
   ```

2. Wait for the develop:development-planner agent to complete. The agent will:
   - Use the split-plan skill to analyze the master plan
   - Generate all 7 phase plan files in `.trackers/{BASE_NAME}/plans/`
   - Identify feature tracks and classify tasks by phase
   - Score task complexity (1-3)
   - Verify all files were created successfully
   - Provide a comprehensive summary report

3. **After the develop:development-planner agent completes**, the following files will exist:
   ```
   .trackers/{BASE_NAME}/plans/
   ├── {BASE_NAME}-master-plan.md           # From Step 2
   ├── {BASE_NAME}-01-foundational.md       # Phase 1 plan
   ├── {BASE_NAME}-02-models.md             # Phase 2 plan
   ├── {BASE_NAME}-03-services.md           # Phase 3 plan
   ├── {BASE_NAME}-04-data.md               # Phase 4 plan
   ├── {BASE_NAME}-05-rules.md              # Phase 5 plan
   ├── {BASE_NAME}-06-state-management.md   # Phase 6 plan
   └── {BASE_NAME}-07-ui.md                 # Phase 7 plan
   ```

4. **Review the agent's output** and summarize for the user:
   ```
   Phase plans created by develop:development-planner agent!

   **Master Plan**: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md
   **Phase Plans**: {BASE_NAME}-01 through {BASE_NAME}-07

   The develop:development-planner agent has analyzed your master plan and organized all tasks into the 7-phase architecture with feature tracks and complexity scores.

   [Include summary from agent's output showing:
    - Feature tracks identified
    - Tasks per phase
    - Complexity distribution
    - Any important notes or considerations]

   All 7 phase plan files have been generated:
   - Phase 1 (Foundational): {BASE_NAME}-01-foundational.md
   - Phase 2 (Models): {BASE_NAME}-02-models.md
   - Phase 3 (Services): {BASE_NAME}-03-services.md
   - Phase 4 (Data): {BASE_NAME}-04-data.md
   - Phase 5 (Rules): {BASE_NAME}-05-rules.md
   - Phase 6 (State Management): {BASE_NAME}-06-state-management.md
   - Phase 7 (UI): {BASE_NAME}-07-ui.md

   Questions:
   1. Would you like to review any of the phase plan files?
   2. Are there any adjustments needed to the task organization?
   3. Should I proceed to create the tracker from these phase plans?

   Options:
   - Type "proceed" to continue with tracker creation
   - Type "review [phase-number]" to see a specific phase plan (e.g., "review 1" or "review 5")
   - Type "review all" to see summary of all phases
   ```

5. **Wait for user response**:

   - If **"proceed"**: Continue to Step 5 (Create Tracker)

   - If **"review [phase-number]"**:
     * Read and display the requested phase plan file
     * Ask again: "Would you like to review another phase, or proceed with tracker creation?"
     * Wait for response (proceed/review)

   - If **"review all"**:
     * Read all 7 phase plan files and provide a summary showing:
       - Tasks per phase
       - Tracks identified
       - Complexity distribution
     * Ask: "Would you like to proceed with tracker creation?"
     * Wait for response (proceed)

**After completing Step 4**: Use **TaskUpdate** to set Task 4 status to `completed`

6. Once user confirms "proceed", continue to Step 5

### Step 5: Create Tracker and Populate from Phase Plans

**Before starting**: Use **TaskUpdate** to set Task 5 status to `in_progress`

**CRITICAL**: Use the tracker agent to create a new tracker and populate it with all phases, tracks, and tasks from the phase plan files using ONLY tracker skills.

1. **Create empty tracker**:

   ```
   Use Skill tool with:
     skill: "tracker:create-tracker"
     args: "{BASE_NAME}"
   ```

   This creates a new empty tracker with name `{BASE_NAME}`.

2. **Read the phase plan files** to understand the overall structure:
   - Read through the 7 phase plan files to extract:
     * List of tracks identified
     * Phase distribution of tasks
     * Task counts per phase

3. **For each phase plan file (01 through 07)**, sequentially:

   a. **Read the phase plan file**:
      - File: `.trackers/{BASE_NAME}/plans/{BASE_NAME}-{NN}-{phase-name}.md`
      - Parse the file to extract:
        * Phase name and description
        * All tracks in this phase
        * All tasks with their details (title, description, complexity, priority, track assignment)

   b. **Add the phase to tracker** (if not already added):
      ```
      Use Skill tool with:
        skill: "tracker:add-phase"
        args: "{BASE_NAME} --name='{Phase Name}' --description='{Phase description from plan}'"
      ```

   c. **For each track mentioned in this phase plan**:

      i. **Check if track exists** (track may span multiple phases):
         - Keep a list of tracks already added to avoid duplicates
         - If track already added, skip to step ii
         - If new track, add it:
           ```
           Use Skill tool with:
             skill: "tracker:add-track"
             args: "{BASE_NAME} --name='{track-name}' --description='{track description}' --phase='{Phase Name}'"
           ```

      ii. **For each task in this track within this phase**:
          ```
          Use Skill tool with:
            skill: "tracker:add-task"
            args: "{BASE_NAME} --phase='{Phase Name}' --track='{track-name}' --title='{task-title}' --description='{task-description}' --complexity={1|2|3} --priority={high|medium|low}"
          ```

   d. **After adding all tasks from the phase plan**, inform user:
      ```
      Phase {N} added to tracker:
      - Phase: {Phase Name}
      - Tracks: {count}
      - Tasks: {count}
      ```

4. **After all phase plans are processed**, verify tracker completion:

   ```
   Use Skill tool with:
     skill: "tracker:review-tracker"
     args: "{BASE_NAME} --detailed"
   ```

5. Inform user:
   ```
   Tracker creation complete!

   **Tracker**: {BASE_NAME}
   **Location**: .trackers/{BASE_NAME}/TRACKER.md

   **Summary**:
   - Total Phases: 7
   - Total Tracks: {count}
   - Total Tasks: {count}

   All tasks from phase plans have been added to the tracker with:
   - Phase assignments
   - Track assignments
   - Complexity scores
   - Priority levels
   - Plan file references
   ```

**After completing Step 5**: Use **TaskUpdate** to set Task 5 status to `completed`

6. Continue to Step 6

**IMPORTANT**: This step uses ONLY tracker agent skills to build the tracker structure. The tracker agent handles all data persistence and validation.

### Step 6: Present Analysis and Select Phases for Execution

**Before starting**: Use **TaskUpdate** to set Task 6 status to `in_progress`

**CRITICAL**: Present the phase/track structure, get user confirmation on the organization, and select which phases to execute.

1. **Review the phase plan files** created by develop:development-planner agent:
   - Read through the phase plan files to extract:
     * Feature tracks identified
     * Phase breakdown
     * Task counts per phase and track

2. **Use tracker agent to generate progress report**:
   ```
   Use Skill tool with:
     skill: "tracker:review-tracker"
     args: "{BASE_NAME} --detailed"
   ```

3. **Present the structure and planning status to the user**:
   ```
   Analysis complete! The develop:development-planner agent has organized your requirements.

   **Source Requirements**: {RESOLVED_FILE_PATH}
   **Master Plan**: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md
   **Phase Plans**: {BASE_NAME}-01 through {BASE_NAME}-07
   **Tracker**: {BASE_NAME}

   **Feature Tracks Identified**:
   [List tracks from phase plan files with brief descriptions]

   **Phase Structure** (Sequential execution):

   **Phase 1: Foundational**
   - Track: core ([X] tasks)
   - Purpose: Set up base abstractions and toolings
   - Status: Not started

   **Phase 2: Models**
   - Track: authentication ([X] tasks)
   - Track: products ([X] tasks)
   - Purpose: Define data entities
   - Depends on: Phase 1
   - Status: Not started

   **Phase 3: Services**
   - Track: authentication ([X] tasks)
   - Track: products ([X] tasks)
   - Purpose: Implement API services
   - Depends on: Phase 2
   - Status: Not started

   [... continue for phases 4-7 ...]

   **Summary**:
   - Total Tasks: {count}
   - Total Tracks: {count}
   - Average Complexity: {score}

   **Files Created**:
   - Master Plan: {BASE_NAME}-master-plan.md
   - Phase Plans: {BASE_NAME}-01 through {BASE_NAME}-07
   - Tracker: {BASE_NAME}

   Questions:
   1. Does this phase/track grouping make sense for your architecture?
   2. Should any tasks be moved to different phases or tracks?
   3. Would you like to review any of the generated plan files?
   4. Which phases would you like to execute?
      - "All" - Execute all incomplete phases
      - "Phase [N]" - Execute specific phase(s)
      - "Phase [N] to [M]" - Execute range of phases
      - "Review first" - Skip execution and generate summary only
   ```

4. **Wait for user response**:

   a. **If user wants to adjust organization**:
      - "Move Task [X] to Phase [Y]" - adjust the grouping (requires editing phase plans)
      - "Review plans" - show specific plan files
      - Handle adjustments, then ask again for phase selection

   b. **If user wants to review first**:
      - "Review first" → Skip to Step 8 (final summary) without execution
      - Mark Task 6 as completed
      - End workflow with summary generation

   c. **If user selects phases to execute**:
      - Parse user's selection and record which phases to execute
      - Examples:
        * "All" → Execute all incomplete phases
        * "Phase 3" → Execute only Phase 3
        * "Phase 3 to 7" → Execute Phase 3, 4, 5, 6, 7
      - Continue to Step 7 with selected phases

5. **After user confirms phases to execute**, continue to Step 7

**After completing Step 6**: Use **TaskUpdate** to set Task 6 status to `completed`

**IMPORTANT**: NEVER proceed without explicit user confirmation on both the structure AND which phases to execute. This combined step ensures the user reviews the organization and makes an informed decision about execution scope.

### Step 7: Execute Implementations (Sequential Phases, Adaptive Parallel Within Phase)

**Before starting**: Use **TaskUpdate** to set Task 7 status to `in_progress`

After user selects phases to execute (from Step 6):

**CRITICAL**: Implement phases SEQUENTIALLY (in order 1→2→3→4→5→6→7), but spawn 1-8 developer agents ADAPTIVELY IN PARALLEL for tasks within each phase based on complexity analysis. Update task status via tracker.

**Process each selected phase sequentially:**

1. For each selected phase in order:

   a. Read the phase plan file: `.trackers/{BASE_NAME}/plans/{BASE_NAME}-{NN}-{name}.md`

   b. **Get pending tasks from tracker**:
      ```
      Use Skill tool with:
        skill: "tracker:review-tracker"
        args: "{BASE_NAME} --phase={N} --status=pending"
      ```

   c. **Extract pending tasks and complexity scores**:
      - From the tracker output, extract:
        * Task ID, name, description
        * Track assignment
        * Complexity score (1, 2, or 3)
        * Status (should be Pending)
        * Plan file reference
      - If no pending tasks, skip this phase

   d. **Calculate Optimal Parallel Agent Count** (only for pending tasks):

      i. **Handle Force Sequential Mode**:
         - If `FORCE_SEQUENTIAL = true` (from --sequential flag):
           * Set `PARALLEL_COUNT = 1`
           * Log: "Sequential mode enabled by user - running 1 task at a time"
           * Skip to step e

      ii. **Calculate Average Complexity**:
         - Get complexity scores for all pending tasks in this phase
         - Calculate: `AVG_COMPLEXITY = sum(task_scores) / pending_task_count`
         - Example: Pending tasks with scores [2, 3, 2, 1] → AVG_COMPLEXITY = 2.0

      iii. **Apply Base Formula**:
         ```
         MAX_CAPACITY = 10.0          # Total "capacity units" available
         BASE_PARALLEL = floor(MAX_CAPACITY / AVG_COMPLEXITY)

         Examples:
         - AVG_COMPLEXITY = 1.0 (low) → BASE_PARALLEL = 10
         - AVG_COMPLEXITY = 2.0 (medium) → BASE_PARALLEL = 5
         - AVG_COMPLEXITY = 3.0 (high) → BASE_PARALLEL = 3
         ```

      iv. **Apply Aggressive Mode Multiplier**:
         - If `AGGRESSIVE_MODE = true`:
           * Multiply by 1.5x: `BASE_PARALLEL = floor(BASE_PARALLEL * 1.5)`
           * Example: BASE_PARALLEL = 5 → 7 (with aggressive)

      v. **Apply Constraints**:
         ```
         PENDING_TASK_COUNT = number of pending tasks in this phase
         PARALLEL_COUNT = BASE_PARALLEL

         # Don't spawn more agents than pending tasks
         PARALLEL_COUNT = min(PARALLEL_COUNT, PENDING_TASK_COUNT)

         # Respect hard limits (1 minimum, 8 maximum)
         PARALLEL_COUNT = max(PARALLEL_COUNT, 1)
         PARALLEL_COUNT = min(PARALLEL_COUNT, 8)
         ```

      vi. **Apply User Override**:
         - If `MAX_PARALLEL_OVERRIDE` is set:
           * `PARALLEL_COUNT = min(MAX_PARALLEL_OVERRIDE, PENDING_TASK_COUNT)`
           * `PARALLEL_COUNT = min(PARALLEL_COUNT, 8)`  # Hard cap

      vii. **Log Decision**:
         ```
         Log to user:
         "Phase {number} Analysis:
          - Pending Tasks: {PENDING_TASK_COUNT}
          - Average Complexity: {AVG_COMPLEXITY} ({low|medium|high})
          - Calculated Parallel Count: {PARALLEL_COUNT}
          - Mode: {Normal|Aggressive|Sequential|User Override}

          Spawning {PARALLEL_COUNT} developer agent(s) in parallel..."
         ```

   e. **Mark phase tasks as "In Progress" in tracker**:
      For each pending task in this phase:
      ```
      Use Skill tool with:
        skill: "tracker:mark-status"
        args: "{BASE_NAME} --task={task-id} --status=in-progress"
      ```

   f. **Split pending tasks into batches** of size = `PARALLEL_COUNT`

   g. **For each batch**:

      i. Spawn developer agents IN PARALLEL (one message with multiple Task calls):

      Example:
      ```
      <message>
      <Task tool call 1>
        subagent_type: "develop:senior-developer"
        description: "Implement Task {id}"
        prompt: "Implement Task {id} from Phase {number}: {name}

        ## Task Details
        [Full task description from tracker]
        **Complexity**: {score} ({Low|Medium|High})
        **Track**: {track-name}

        ## Context
        - This is part of Phase {number}: {name}
        - Detailed plan: .trackers/{BASE_NAME}/plans/{plan-file-reference}
        - Read the phase plan for full architectural context

        ## Implementation
        Read the detailed phase plan, then implement this specific task.
        Follow the project's existing patterns and architecture."
      </Task>

      <Task tool call 2>
        [... similar structure for next task ...]
      </Task>

      [... continue for PARALLEL_COUNT tasks ...]
      </message>
      ```

      ii. Wait for batch to complete

      iii. **Update tracker with batch results**:
         For each task in the batch:
         - Analyze agent output to determine success/failure
         - If successful:
           ```
           Use Skill tool with:
             skill: "tracker:mark-status"
             args: "{BASE_NAME} --task={task-id} --status=complete"
           ```
         - If failed:
           ```
           Use Skill tool with:
             skill: "tracker:mark-status"
             args: "{BASE_NAME} --task={task-id} --status=blocked"
           ```

   h. **After all batches in phase complete**:

      i. **Check phase completion using tracker**:
         ```
         Use Skill tool with:
           skill: "tracker:review-tracker"
           args: "{BASE_NAME} --phase={N}"
         ```

      ii. **Ask user before continuing**:
         ```
         Phase {number}: {name} has been completed!

         Tracker: {BASE_NAME} (updated)
         Plan file: .trackers/{BASE_NAME}/plans/{BASE_NAME}-{NN}-{name}.md

         [Show completion summary from tracker]

         [If there are more selected phases]
         **Next Phase**: Phase {next-number}: {next-phase-name}

         Questions:
         1. Would you like to continue with Phase {next-number}?
         2. Or would you like to pause here and resume later?

         Type "continue" to proceed, or "pause" to stop here.
         ```

      iii. **Wait for user response**:
         - If "continue": Continue to next selected phase in Step 7
         - If "pause": Skip remaining phases, go to Step 8

2. Continue until all selected phases are implemented or user pauses

**After completing Step 7**: Use **TaskUpdate** to set Task 7 status to `completed`

**IMPORTANT**:
- Task status is tracked via tracker agent
- Tracker provides real-time visibility in terminal
- Plan files contain detailed implementation plans
- Tracker links to plan files via task metadata

### Step 8: Generate Final Summary Report

**Before starting**: Use **TaskUpdate** to set Task 8 status to `in_progress`

After all implementations complete (or when user chooses to pause):

1. **Generate comprehensive progress report using tracker**:
   ```
   Use Skill tool with:
     skill: "tracker:review-tracker"
     args: "{BASE_NAME} --detailed"
   ```

2. **Create summary report** at `.trackers/{BASE_NAME}/plans/{BASE_NAME}-SUMMARY.md`:
   ```markdown
   # Build Summary - {BASE_NAME}

   **Requirements File**: {RESOLVED_FILE_PATH}
   **Date**: {timestamp}
   **Status**: {Completed|Paused}

   ## Overview

   - **Total Phases**: 7
   - **Phases Completed**: {count}
   - **Phases Remaining**: {count}
   - **Total Tasks**: {count}
   - **Tasks Complete**: {count}
   - **Tasks Remaining**: {count}
   - **Total Feature Tracks**: {count}

   ## Phase Architecture

   This project follows clean architecture with 7 sequential phases:
   1. Foundational → 2. Models → 3. Services → 4. Data → 5. Rules → 6. State Management → 7. UI

   ## Tracker

   All progress is tracked in the tracker system:
   - **Tracker**: `.trackers/{BASE_NAME}/TRACKER.md`
   - **Plans**: `.trackers/{BASE_NAME}/plans/`
   - Use `/tracker:review-tracker {BASE_NAME}` to view current status

   ## Phase Status

   [Include tracker summary for each phase showing completion status]

   ## Feature Tracks

   The following features were built:
   [List tracks with completion status from tracker]

   ## Files Generated

   ### Tracker
   - Tracker: `.trackers/{BASE_NAME}/TRACKER.md`

   ### Plans (All in .trackers/{BASE_NAME}/plans/)
   - Master Plan: {BASE_NAME}-master-plan.md
   - Phase 1 Plan: {BASE_NAME}-01-foundational.md
   - Phase 2 Plan: {BASE_NAME}-02-models.md
   - Phase 3 Plan: {BASE_NAME}-03-services.md
   - Phase 4 Plan: {BASE_NAME}-04-data.md
   - Phase 5 Plan: {BASE_NAME}-05-rules.md
   - Phase 6 Plan: {BASE_NAME}-06-state-management.md
   - Phase 7 Plan: {BASE_NAME}-07-ui.md
   - Summary: {BASE_NAME}-SUMMARY.md (this file)

   ## How to Resume

   To resume this build workflow:

   1. Run the /develop-project command again with the same requirements file:
      ```
      /develop-project {RESOLVED_FILE_PATH}
      ```

   2. The command will:
      - Read the tracker for completion status
      - Skip completed phases automatically
      - Resume from incomplete phases
      - Only execute pending tasks within each phase

   3. To check progress at any time:
      ```
      /tracker:review-tracker {BASE_NAME}
      ```

   ## Next Steps

   [If paused]
   - Continue with Phase {next-number}: {name}
   - Review tracker for current progress
   - Verify implementation before proceeding

   [If completed]
   - All phases complete!
   - Review code quality
   - Proceed to integration testing
   - Deploy to staging environment
   ```

3. Present summary to user:
   ```
   Build workflow complete!

   Summary saved to: .trackers/{BASE_NAME}/plans/{BASE_NAME}-SUMMARY.md
   Tracker: .trackers/{BASE_NAME}/TRACKER.md

   **Completed**: {count} phases, {count} tasks
   **Remaining**: {count} phases, {count} tasks

   To view detailed progress:
   /tracker:review-tracker {BASE_NAME}

   You can resume at any time by running /develop-project again.
   ```

**After completing Step 8**: Use **TaskUpdate** to set Task 8 status to `completed`

## Important Notes

- **Progress Tracking**: Creates 8 workflow tasks at start for real-time visibility
- **Task Status Updates**: Each step marks its task as in_progress (start) and completed (end)
- **Master Plan First**: Planning agent creates comprehensive master plan from requirements
- **Master Plan Review**: User reviews and approves master plan before split-plan workflow
- **Development Planner Agent**: Step 4 uses develop:development-planner agent to analyze master plan and create phase plans
- **Split Plan Analysis**: develop:development-planner agent uses split-plan skill to organize master plan into 7 phases
- **Separate Tracker Creation**: Step 5 creates tracker and populates it from phase plans using ONLY tracker skills
- **Fixed Phase Architecture**: Always use the 7 predefined phases in order
- **Feature-Based Tracks**: Tracks represent features, not arbitrary groupings
- **Tracker Integration**: All task management goes through tracker agent skills
- **Plan Files**: Master plan + 7 phase-specific plans + summary (generated at end)
- **Terminal Visibility**: Both workflow tasks and tracker updates visible throughout
- **Complexity Scoring**: split-plan skill adds complexity scores to all tasks
- **User Confirmation**: Required at multiple checkpoints:
  - After master plan creation (Step 3)
  - After phase plans creation (Step 4)
  - After phase/track structure presentation and phase selection (Step 6)
  - After each phase execution (Step 7)
- **Sequential Phases**: Phases execute in strict order (1→2→3→4→5→6→7)
- **Adaptive Parallel**: Within each phase, 1-8 agents run in parallel based on complexity
- **Resume Support**: Can resume from any incomplete phase using tracker status
- **File Naming**: Uses `{BASE_NAME}-{NN}-{name}.md` format (zero-padded, 01-07)
- **Workflow Steps**: Plan → Review → Development Planner Agent → Tracker Creation → Senior Developers
- **Senior Developer Agent**: All implementation tasks use the develop:senior-developer agent

## Agent Selection

For implementation tasks:
- Use `subagent_type: "develop:senior-developer"` for all projects

## Output to User

Keep the user informed at each step:

**Before Step 1: Create Workflow Tasks**
- Create all 8 workflow tasks using TaskCreate for progress visibility
- Tasks show in terminal as the workflow progresses
- Each task transitions: pending → in_progress → completed

**Step 1: Parse Arguments and Configuration**
- Mark Task 1 as in_progress
- Parse command-line arguments
- Validate configuration
- Mark Task 1 as completed

**Step 2: Master Plan Creation**
- Mark Task 2 as in_progress
- "Processing requirements file: {BASE_NAME}"
- "Spawning Plan agent to create master plan..."
- "Master plan created and saved!"
- "File: .trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md"
- Mark Task 2 as completed

**Step 3: Master Plan Review**
- Mark Task 3 as in_progress
- **[Present master plan summary to user]**
- **[Wait for proceed/review/edit]**
- Mark Task 3 as completed

**Step 4: Split Plan Analysis**
- Mark Task 4 as in_progress
- "Spawning develop:development-planner agent to analyze master plan..."
- "develop:development-planner agent analyzing and organizing tasks into phases..."
- "Phase plans created by develop:development-planner agent!"
- **[Present summary from agent including tracks, tasks, complexity]**
- **[Present list of all 7 phase plan files]**
- **[Ask user: Review phase plans or proceed to tracker creation?]**
- **[Wait for proceed/review confirmation]**
- Mark Task 4 as completed

**Step 5: Tracker Creation**
- Mark Task 5 as in_progress
- "Creating tracker: {BASE_NAME}"
- "Processing phase plan: {BASE_NAME}-01-foundational.md"
- "Phase 1 added to tracker: X tracks, Y tasks"
- [... repeat for each phase ...]
- "Processing phase plan: {BASE_NAME}-07-ui.md"
- "Phase 7 added to tracker: X tracks, Y tasks"
- "Tracker creation complete!"
- Mark Task 5 as completed

**Step 6: Present Analysis and Select Phases**
- Mark Task 6 as in_progress
- **[Present complete phase/track structure from develop:development-planner output]**
- **[Show statistics: total tasks, tracks, phases, complexity]**
- **[Present progress report from tracker]**
- **[Wait for user confirmation on structure]**
- **[Ask which phases to execute: All, specific phase(s), range, or review first]**
- **[Wait for user to select phases or choose to review]**
- Mark Task 6 as completed

**Step 7: Execute Implementation**
- Mark Task 7 as in_progress
- "Phase {N} Analysis: {count} pending tasks, AVG complexity: {score}, spawning {count} agents..."
- "Updating tracker with task status..."
- "Phase {N} completed! Tracker updated."
- **[Ask user: Continue or pause?]**
- **[Wait for response]**
- Mark Task 7 as completed (when all phases done or user pauses)

**Step 8: Final Summary**
- Mark Task 8 as in_progress
- "Final summary generated"
- "Build complete! Check tracker for full status."
- Mark Task 8 as completed

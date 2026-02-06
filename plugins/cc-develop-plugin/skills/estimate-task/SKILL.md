---
name: estimate-task
description: Reference guide for scoring task complexity using a 3-level system (1=Low, 2=Medium, 3=High). Use when you need to estimate development effort, plan sprints, or assess task difficulty.
user-invocable: false
---

# Estimate Task

Use this skill to score task complexity using a 3-level scoring system. This helps with planning, estimation, and resource allocation.

## Complexity Scoring System

Tasks are scored on a scale of 1-3:
- **1 = Low Complexity** (Simple)
- **2 = Medium Complexity** (Moderate)
- **3 = High Complexity** (Complex)

---

## Score 1: Low Complexity

**Definition**: Simple, straightforward tasks that require minimal decision-making and have clear implementation paths.

**Characteristics**:
- Well-defined, single-purpose changes
- Little to no architectural decision required
- Minimal testing complexity
- Low risk of side effects
- Can be completed quickly
- Requires basic technical knowledge

**Task Types**:
- Add a constant or configuration value
- Create a simple model class with basic fields
- Add a simple utility function
- Update documentation
- Rename variables or refactor names
- Format code or fix styling
- Add comments or docstrings
- Simple UI text changes
- Add an enum or constant list
- Copy-paste similar existing code

**Examples**:
- "Create User model with name, email, id fields"
- "Add API_BASE_URL constant"
- "Create UserRole enum with Admin, User, Guest"
- "Add docstring to calculateTotal function"
- "Rename getUserData to fetchUserProfile"
- "Fix indentation in config file"
- "Update README with installation steps"
- "Add success message constant"

**Estimated Effort**: Small (minutes to 1-2 hours)

---

## Score 2: Medium Complexity

**Definition**: Implementation tasks requiring moderate effort, some decision-making, and integration with existing code.

**Characteristics**:
- Requires understanding of existing codebase
- Involves multiple files or components
- Some architectural decisions needed
- Moderate testing requirements
- May have some edge cases
- Requires solid technical skills
- Integration with existing systems

**Task Types**:
- Implement a new feature
- Create a service with multiple methods
- Build a new UI component with logic
- Implement repository pattern
- Add validation logic with multiple rules
- Create state management for a feature
- Implement API integration with endpoints
- Add form with validation
- Create reusable component
- Refactor existing code structure

**Examples**:
- "Implement authentication service with login/logout"
- "Create login screen with form validation"
- "Implement product repository with CRUD operations"
- "Add password validation with strength checker"
- "Build shopping cart state management"
- "Create user profile page with edit functionality"
- "Implement API client for product endpoints"
- "Add image upload component with preview"
- "Create responsive navigation menu"
- "Implement local cache with expiration"

**Estimated Effort**: Medium (half-day to 2 days)

---

## Score 3: High Complexity

**Definition**: Complex or architectural tasks that require significant planning, multiple integrations, or critical system changes.

**Characteristics**:
- Significant architectural decisions
- Affects multiple systems or modules
- Complex business logic or algorithms
- Extensive testing required
- High risk or security-critical
- Performance considerations
- Third-party integrations
- Requires advanced technical expertise
- May need research or spike work

**Task Types**:
- Implement authentication/authorization system
- Set up state management framework
- Integrate payment gateway
- Implement real-time features (websockets, notifications)
- Database migration or schema changes
- Complex business logic with multiple rules
- Security-critical implementations
- Performance optimization requiring refactoring
- Complex algorithm implementations
- Multi-service orchestration

**Examples**:
- "Implement JWT authentication with refresh tokens and role-based access"
- "Set up real-time chat using websockets with presence"
- "Integrate Stripe payment processing with webhooks"
- "Implement search with full-text indexing and filters"
- "Add offline sync with conflict resolution"
- "Create complex form wizard with validation across steps"
- "Implement OAuth2 flow with multiple providers"
- "Add real-time collaborative editing"
- "Implement video streaming with adaptive bitrate"
- "Create complex reporting system with aggregations"

**Estimated Effort**: Large (multiple days to weeks)

---

## Scoring Decision Tree

Use this flowchart to determine complexity:

```
START: What is the task?
  |
  ├─> Creates/modifies 1-2 files with simple logic?
  |   └─> Does it require research or architectural decisions?
  |       ├─> No → Score: 1 (Low)
  |       └─> Yes → Continue to next question
  |
  ├─> Involves multiple components/integrations?
  |   └─> Does it involve critical systems (auth, payments, security)?
  |       ├─> No → Score: 2 (Medium)
  |       └─> Yes → Score: 3 (High)
  |
  └─> Requires framework setup or major architecture change?
      └─> Score: 3 (High)
```

## Scoring Factors

Consider these factors when scoring:

### Increase Complexity If:
- ✓ Requires integration with multiple systems
- ✓ Involves security or authentication
- ✓ Handles sensitive data (payments, PII)
- ✓ Requires real-time functionality
- ✓ Needs complex error handling
- ✓ Involves database migrations
- ✓ Affects critical user flows
- ✓ Requires performance optimization
- ✓ Needs extensive testing
- ✓ Involves third-party services
- ✓ Has unclear requirements

### Decrease Complexity If:
- ✓ Similar code already exists (copy-paste)
- ✓ Well-defined, single responsibility
- ✓ Isolated from other systems
- ✓ Simple CRUD operations
- ✓ Clear requirements
- ✓ No external dependencies
- ✓ Minimal testing needed
- ✓ Uses standard patterns

## Complexity by Phase

Different phases tend toward different complexity levels:

| Phase | Common Complexity | Reasoning |
|-------|------------------|-----------|
| 1 - Foundational | 2-3 (Medium-High) | Architecture decisions, affects all layers |
| 2 - Models | 1-2 (Low-Medium) | Usually straightforward data structures |
| 3 - Services | 2-3 (Medium-High) | External integrations, error handling |
| 4 - Data | 2 (Medium) | Repository patterns, persistence logic |
| 5 - Rules | 2-3 (Medium-High) | Business logic complexity varies |
| 6 - State Management | 2 (Medium) | State patterns, reactivity |
| 7 - UI | 1-3 (All levels) | Varies widely from simple text to complex flows |

**Note**: These are guidelines, not rules. Always evaluate each task individually.

## Common Patterns

### Low Complexity (1) Patterns:
- "Add X field to Y model"
- "Create Z enum"
- "Update text/copy"
- "Add constant"
- "Simple getter/setter"

### Medium Complexity (2) Patterns:
- "Implement X feature"
- "Create Y screen with Z"
- "Add A to B with C"
- "Build X component"
- "Integrate Y API"

### High Complexity (3) Patterns:
- "Implement X system"
- "Set up Y framework"
- "Integrate Z with A and B"
- "Add real-time X"
- "Migrate Y to Z"
- "Implement X with security"

## Edge Cases

### Multi-Part Tasks
If a task description contains multiple complexity levels, consider:
1. **Break it down** into separate tasks with appropriate scores
2. **Score the highest** if it must be done as one task
3. **Average up** if components are tightly coupled

**Example**: "Create login screen with email validation and password strength indicator"
- Could be split: Screen (1) + Validation (2) + Strength indicator (2)
- Or scored as one: Score 2 (Medium) - multiple features, moderate integration

### Research Tasks
Tasks requiring investigation or spike work should be scored based on:
- **Known unknowns**: Score 2-3 depending on scope
- **Unknown unknowns**: Score 3 (High) - research adds complexity

### Maintenance vs New Features
- **Bug fixes**: Usually score 1-2 depending on root cause complexity
- **Refactoring**: Score based on scope (1-3)
- **New features**: Usually score 2-3

## Scoring Template

When estimating, use this format:

```markdown
**Task**: {task description}

**Complexity Analysis**:
- Files affected: {count}
- External dependencies: {Yes/No}
- Integration points: {count}
- Business logic complexity: {Low/Medium/High}
- Testing requirements: {Low/Medium/High}
- Risk level: {Low/Medium/High}

**Score**: {1|2|3} ({Low|Medium|High})
**Estimated Effort**: {Small|Medium|Large}

**Rationale**: {Brief explanation of why this score}
```

## Examples with Rationale

### Example 1: Score 1 (Low)
**Task**: "Add createdAt timestamp to User model"

**Rationale**:
- Single file modification
- Simple field addition
- No business logic
- Minimal testing needed
- Standard pattern

**Score**: 1 (Low)

---

### Example 2: Score 2 (Medium)
**Task**: "Implement product search with filters"

**Rationale**:
- Multiple components (search bar, filter UI, results)
- Backend API integration
- State management for filters
- Some UX considerations
- Moderate testing needed

**Score**: 2 (Medium)

---

### Example 3: Score 3 (High)
**Task**: "Add two-factor authentication"

**Rationale**:
- Security-critical feature
- Multiple integrations (SMS/email provider)
- Complex state management (enrollment, verification)
- Extensive testing required (security scenarios)
- Affects authentication flow
- Requires QR code generation
- Session management changes

**Score**: 3 (High)

---

## Calibration Tips

To maintain consistency:

1. **Compare to reference tasks** - Keep examples handy
2. **Consider team skill level** - Adjust for expertise
3. **Review past estimates** - Learn from accuracy
4. **Be consistent** - Similar tasks should have similar scores
5. **When in doubt** - Round up for safety

## Red Flags for High Complexity (3)

If any of these apply, consider scoring 3:
- Task description uses words: "system", "framework", "migration", "integration"
- Involves money, security, or privacy
- Requires coordination across teams
- Has vague or unclear requirements
- Affects critical user flows
- Needs research or proof-of-concept first
- Changes core architecture
- Involves real-time or distributed systems

## Usage

Simply provide a task description, and this skill will help you score it from 1-3 based on the criteria above.

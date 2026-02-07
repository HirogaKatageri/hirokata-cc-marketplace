# Changelog

All notable changes to the Develop Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] - 2026-02-08

### Added
- **software-architect agent** - New dedicated agent for master plan creation
  - Analyzes requirements documents to understand scope and constraints
  - Investigates existing codebase to understand architecture and patterns
  - Designs comprehensive implementation strategies
  - Creates single, well-structured master plan documents
  - Has Write capabilities to save plans directly without returning content

### Changed
- **develop-project command** - Updated Step 2 to use software-architect agent
  - Uses `develop:software-architect` subagent_type
  - Agent writes master plan directly to `.trackers/{BASE_NAME}/plans/{BASE_NAME}-master-plan.md`
  - Streamlined workflow proceeds directly to Step 3 after plan creation
  - No need to return plan content to main agent

### Improved
- Master plan creation workflow efficiency
- Separation of concerns: software-architect for planning, development-planner for organization
- Documentation clarity about agent roles and responsibilities

## [0.2.1] - 2026-02-07

### Added
- **generate-requirements skill** - Comprehensive requirements documentation generator
  - Launches product-owner agent for structured requirements gathering
  - Single file output: `requirements/[FEATURE_NAME]_REQUIREMENTS.md`
  - Complete requirements template with all sections
  - User story patterns and best practices
  - Full biometric authentication requirements example
  - References for requirements engineering and user story writing

### Changed
- **product-owner agent** - Enhanced with strict file output policy
  - Now creates only ONE requirements file (no auxiliary files)
  - Added File Output Policy section with explicit constraints
  - Added File Creation Policy section as critical constraint
  - Consolidated all content (summaries, checklists) into single file

### Improved
- Product-owner agent output consistency
- Requirements documentation workflow
- Single-file requirements approach eliminates clutter

## [0.2.0] - 2026-02-07

### Added
- Critical concepts section to develop-project command frontmatter
- Purpose sections to all reference skills (categorize-task, estimate-task, split-plan)
- Enhanced workflow documentation with 8-step process clarity

### Changed
- Improved skill descriptions to be more action-oriented and concise
- Enhanced conventional-commit skill documentation for better clarity
- Made all documentation more direct and user-focused
- Updated skill descriptions from passive to active voice

### Improved
- Documentation consistency across all skills
- Command frontmatter with critical workflow concepts
- User guidance in all skill files

## [0.1.2] - 2026-02-07

### Added
- Conventional commit skill for intelligent commit message generation
- Automated change grouping and commit strategy selection

### Changed
- Enhanced develop-project command documentation
- Improved README with conventional commit feature

## [0.1.1] - 2026-02-07

### Added
- Product owner agent for requirements gathering
- Enhanced documentation structure

### Changed
- Improved agent descriptions and triggering conditions

## [0.1.0] - 2026-01-27

### Added
- Initial release
- 7-phase clean architecture workflow
- Adaptive parallel execution (1-8 agents)
- Master plan and phase plan generation
- Tracker integration
- Development planning and execution agents
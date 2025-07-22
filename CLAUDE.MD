# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Test Principles
- Never test internals, only test functions which are exported and exposed/part of the application logic
- Test a "system" e.g. first define what the system is supposed to achieve (in the simplest case some kind of transform) and validate inputs and outputs only
- If state consistency is an important feature, also test this

# Type System
- We use dataclasses a lot
- Please always use the unvalidated or validated dataclasses imported from common 
- Validated is using Pydantic under the hood, and has defaults we want (frozen no extra attrs etc)
- Never use BaseModel or dataclass directly!!!
- All types go in the `types_/` folder
- Annotate every function with return types
- Strict typing enforced (Pyright strict mode)
- Always include return type annotations
- Always try to think about extra validations that could be applied to our classes! And all validation logic should live on the types

# Type Checking and Linting
- **Type checking**: Using Pyright in strict mode (configured in `pyrightconfig.json`)
- **Linting/Formatting**: Ruff (configured in `ruff.toml`)

# Code Style 
- We prefer a functional but pragmatic style, e.g. try to avoid mutating states, but use pythonic patterns and don't be religious about it
- We use a pattern where local only functions are leading with an underscore e.g. def _my_local_fun():
- Use Match Statements a lot, please never add a default _ case but match each case exhaustively.
- Using Python 3.13 - use modern Python features (e.g., `match` statements, `list` instead of `List` in typing)

# Infrastructure
- Postgres/Supabase for Auth + Production Use-Cases
- SQLite for Dev/Local Setups
- We use a Docker Container and always deploy some kind of docker Runtime through github actions.
- We run part of our Infra on cloud platforms (AWS/GCP/Azure)

# Running Scripts
- Please add all scripts to src/scripts/ 
- Make sure to also type annotate scripts as best as possible

# Import Style
- Use absolute imports from project root (e.g., `from types_.ai import ...`)
- Never use relative imports
- Don't prefix with `src.` (e.g., use `types_.ai` not `src.types_.ai`)

# Code Comments
- Do not add code comments unless explicitly requested
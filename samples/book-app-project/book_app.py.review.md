
Code Quality

 - [FAIL] Functions lack type hints (show_books, handle_*, main).
 - [PASS] No bare except clauses (only except ValueError).
 - [PASS] No mutable default arguments.
 - [PASS] No file I/O here, so context manager usage is not applicable.
 - [PASS] All functions are under 50 lines.
 - [PASS] Naming follows PEP 8 (snake_case).
 - [FAIL] Global mutable state (collection = BookCollection()) hurts testability and reuse.

Input Validation

 - [FAIL] title/author inputs are not validated for empty values before add/remove/find.
 - [FAIL] year accepts 0/negative/unrealistic values; no range validation.
 - [PASS] Error output for invalid year is clear (Error: ...).

Testing

 - [FAIL] No pytest tests found for book_app.py.
 - [FAIL] CLI edge cases (missing args, empty fields, invalid year, unknown command) are not covered.
 - [FAIL] No test names exist to assess descriptiveness.

Summary

6 items need attention before merge.

Suggested improvements: add type hints throughout, inject BookCollection into handlers (or main) instead of using a global, validate non-empty text inputs,
enforce a sane year range (e.g., 1450..current_year), and add pytest coverage for CLI command paths and input-validation failures.
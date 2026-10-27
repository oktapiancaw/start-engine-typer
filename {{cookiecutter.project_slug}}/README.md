# {{ cookiecutter.project_name }}

{{ cookiecutter.package_description }}

Long-running engine with a **thin** Typer CLI. The CLI parses flags and
hands off to runners in `src/core/`. CLI rarely changes — engine does.

## Quick start

```bash
uv sync
uv run {{ cookiecutter.cli_command }} --help
uv run {{ cookiecutter.cli_command }} stream --source default
uv run {{ cookiecutter.cli_command }} batch  --window 1h
uv run {{ cookiecutter.cli_command }} schedule --cron "*/5 * * * *"
```

## Project structure

```
src/
  main.py              # Typer entrypoint — all CLI commands live here
  configs/
    __init__.py        # logger setup + config/project_meta singletons
    env.py             # ApplicationConfig (Pydantic settings from .env)
  connections/         # clients/adapters (Kafka, Redis, DB, HTTP, ...)
  core/                # engine code — streaming, batching, scheduling runners
  models/              # pydantic data models
public/                # input/ output/ cache/ data/ working dirs
logs/                  # rotating log files (prod_debug.log)
```

**No `commands/` package.** This template assumes the CLI surface is small
and stable (a handful of top-level verbs). If commands start multiplying,
either reach for `start-cli-typer` instead, or add `src/commands/` yourself.

## CLI shape

Three verbs ship by default — rename, remove, or extend in `src/main.py`:

- `stream` — long-running consumer loop
- `batch`  — one pass over a window
- `schedule` — scheduler loop (blocks)

Each is a stub that logs and prints. Wire real work via
`from src.core.<module> import run`.

### Adding a command

Add a `@app.command()` function in `src/main.py`:

```python
@app.command()
def backfill(
    since: Annotated[str, typer.Option(help="ISO date")] = "2024-01-01",
):
    """One-off backfill run."""
    from src.core.backfill import run
    run(since)
```

```bash
uv run {{ cookiecutter.cli_command }} backfill --since 2024-06-01
```

## Configuration

Copy `.env.example` to `.env`. Settings load via `ApplicationConfig` (nested
keys use `__`):

| Var          | Default            | Purpose            |
| ------------ | ------------------ | ------------------ |
| `OUTPUT_DIR` | `./public/output`  | Default output dir |

Access anywhere via `from src.configs import config` → `config.output_dir`.

## Development

```bash
uv run ruff check .        # lint (F/E/W/I/N/UP/B/S rule sets)
uv run ruff format .       # format
```

Requires Python >= {{ cookiecutter.python_version }}.

# start-engine-typer

Cookiecutter template for a long-running Python **engine** (streaming,
batching, scheduling) with a thin Typer CLI. The CLI lives in `src/main.py`
and rarely changes — real work lives in `src/core/`.

## When to use this vs `start-cli-typer`

| Use `start-cli-typer`                    | Use `start-engine-typer`                       |
| ---------------------------------------- | ---------------------------------------------- |
| CLI *is* the product (many subcommands)  | CLI is a thin entry (`stream` / `batch` / `schedule`) |
| Commands evolve often                    | CLI rarely changes; engine evolves             |
| Needs a `commands/` package              | Flat `main.py` — no `commands/`                |

## Generate a project

```bash
uvx cookiecutter gh:oktapiancaw/start-engine-typer
# or from a local clone:
uvx cookiecutter path/to/start-engine-typer
```

Prompts collected:

| Variable              | Default                                         |
| --------------------- | ----------------------------------------------- |
| `project_name`        | `My Engine`                                     |
| `project_slug`        | derived from name                               |
| `cli_command`         | same as `project_slug`                          |
| `package_description` | engine description                              |
| `author_name`         | `Your Name`                                     |
| `author_email`        | `you@example.com`                               |
| `python_version`      | `3.12`                                          |

The post-gen hook runs `git init` and prints the next commands.

## Layout shipped to the generated project

```
<project_slug>/
  pyproject.toml
  .env.example
  .python-version
  README.md
  src/
    main.py              Typer CLI — stream / batch / schedule entrypoints
    configs/             logger + pydantic-settings
    connections/         clients / adapters (Kafka, DB, HTTP, ...)
    core/                engine code (streaming / batching / scheduling)
    models/              pydantic data models
  public/{cache,data,input,output}/
  tests/
  logs/
```

See the generated project's own `README.md` for day-to-day commands.

"""Flat Typer CLI for a long-running engine (streaming / batching / scheduling).

Commands live here, not under a `commands/` subpackage. The CLI is thin: it
parses flags and hands off to runners in `src/core/`.
"""

from typing import Annotated

import typer

from src.configs import CustomLogLevel, logging, project_meta

app = typer.Typer(pretty_exceptions_show_locals=False)

LOGGER = logging.getLogger(project_meta.name)


@app.callback()
def main(
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Enable verbose logging")
    ] = False,
):
    if verbose:
        logging.getLogger().setLevel(CustomLogLevel.INFO)
        LOGGER.debug("Verbose mode enabled")
    else:
        logging.getLogger().setLevel(CustomLogLevel.NOTSET)


@app.command()
def stream(
    source: Annotated[str, typer.Option(help="Input stream identifier")] = "default",
):
    """Run the streaming engine (long-running consumer loop)."""
    LOGGER.info("stream start source=%s", source)
    # from src.core.streaming import run; run(source)
    typer.echo(f"[stream] source={source}")


@app.command()
def batch(
    window: Annotated[str, typer.Option(help="Batch window, e.g. 1h / 1d")] = "1h",
):
    """Run one batch pass over the window."""
    LOGGER.info("batch start window=%s", window)
    # from src.core.batching import run; run(window)
    typer.echo(f"[batch] window={window}")


@app.command()
def schedule(
    cron: Annotated[str, typer.Option(help="Cron expression")] = "*/5 * * * *",
):
    """Start the scheduler loop (blocks)."""
    LOGGER.info("schedule start cron=%s", cron)
    # from src.core.scheduling import run; run(cron)
    typer.echo(f"[schedule] cron={cron}")


if __name__ == "__main__":
    app()

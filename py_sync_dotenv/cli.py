import glob
import logging
import os
import re
import time

import click
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


def just_variable_formatting(lines_list):
    computed_list = [re.sub(r"=.*", "=", line) for line in lines_list]
    return computed_list


def sync_dot_env(
    source,
    destination_env,
    destination_envs=None,
    just_variables=False,
):
    computed_list = []
    lines_list = []

    with open(f"{source}", "r") as f:
        lines_list = f.readlines()
        computed_list = just_variable_formatting(lines_list)

    if destination_envs is not None:
        for filename in glob.glob(
            os.path.join(destination_envs, ".env*"), recursive=False
        ):
            with open(f"{filename}", "w") as f:
                if just_variables:
                    f.writelines(computed_list)
                else:
                    f.writelines(lines_list)

    if destination_env is not None:
        with open(f"{destination_env}", "w") as f:
            if just_variables:
                f.writelines(computed_list)
            else:
                f.writelines(lines_list)


@click.group(invoke_without_command=True)
@click.option(
    "-s",
    "--source",
    default=".env",
    show_default=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
    help="source .env file to use in populating other .env files",
)
@click.option(
    "-d",
    "--destination-env",
    required=False,
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, readable=True, writable=True
    ),
    help=".env file for destination stage",
)
@click.option(
    "-ds",
    "--destination-envs",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    help="directory path to .env files for destination stage",
)
@click.option(
    "--just-variables",
    is_flag=True,
    help="indicates to the engine to synchronize just the variables",
)
@click.pass_context
def main(
    context,
    source,
    destination_env,
    destination_envs,
    just_variables,
    *args,
    **kwargs,
):
    """This script synchronizes .env files."""

    if context.invoked_subcommand is None:
        click.echo("Synchronizing your .env file(s) 🍰")
        sync_dot_env(
            source=source,
            destination_env=destination_env,
            destination_envs=destination_envs,
            just_variables=just_variables,
        )
        click.echo("✨ Synchronizing Complete ✨")
        
    else:
        click.echo("Watching for source .env file changes 🍰")
        click.echo("Quit the watch with CONTROL-C.")
        context.ensure_object(dict)
        context.obj["source"] = source
        context.obj["destination_env"] = destination_env
        context.obj["destination_envs"] = destination_envs
        context.obj["just_variables"] = just_variables


def watch_sync_dot_env(**kwargs):
    sync_dot_env(**kwargs)
    click.echo("✨ .env file(s) updated ✨")


@main.command()
@click.option(
    "--show-logs",
    is_flag=True,
    help="indicates logging of file changes events",
)
@click.pass_context
def watch(context, show_logs):
    """This command watches the source .env file for changes & synchronize on change."""
    if show_logs:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    src_path = os.getcwd()
    event_handler = PatternMatchingEventHandler(
        patterns=[f"{context.obj['source']}"],
        ignore_directories=True,
        case_sensitive=False,
        ignore_patterns=None,
    )
    event_handler.on_modified = lambda _: watch_sync_dot_env(**context.obj)
    observer = Observer()
    observer.schedule(event_handler, src_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()

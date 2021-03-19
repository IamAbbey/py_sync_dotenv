import glob
import os

import emoji
import pytest
from click.testing import CliRunner

from py_sync_dotenv.cli import formatting_engine, main

test_env = """
PRODUCTION=1
DEBUG=0
SECRET_KEY=iu0^cv$mghjfa_vp8vk)e(c_5^cfo7staccjs4+!f#=1a_22-h2
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
"""


@pytest.mark.parametrize(
    "source, dev_env, dev_envs, just_variables",
    [
        ("", "", "", ""),
        ("-s .env", "", "", ""),
        ("-s .env", "-d .env.dev", "", ""),
        ("-s .env", "-d .env.dev", "-ds dev_envs/", ""),
        ("-s .env", "-d .env.dev", "-ds dev_envs/", "--just-variables"),
    ],
)
def test_standard_sync(source, dev_env, dev_envs, just_variables):
    runner = CliRunner()
    with runner.isolated_filesystem():
        s_source = source.split(" ")[1] if source else ".env"
        with open(f"{s_source}", "w") as f:
            f.write(test_env)

        if dev_env:
            with open(f"{dev_env.split(' ')[1]}", "a") as f:
                pass

        if dev_envs:
            if not os.path.exists(dev_envs.split(" ")[1]):
                os.makedirs(dev_envs.split(" ")[1])
                with open(f"{dev_envs.split(' ')[1]}/.env.dev", "a") as f:
                    pass
                with open(f"{dev_envs.split(' ')[1]}/.env1.dev", "a") as f:
                    pass

        args = f"{source} {dev_env} {dev_envs} {just_variables}"
        result = runner.invoke(main, args=args)
        assert not result.exception
        assert result.output == (
            f"{emoji.emojize(':loudspeaker: Synchronizing your .env file(s) :loudspeaker:')}"
            + f"\n{emoji.emojize(':fire: Synchronizing Complete :fire:', use_aliases=True)}\n"
        )

        if dev_env:
            with open(f"{dev_env.split(' ')[1]}", "r") as f:
                output = f.read()
                if just_variables:
                    assert output == "\n".join(formatting_engine(test_env.split("\n")))
                else:
                    assert output == test_env

        if dev_envs:
            for filename in glob.glob(
                os.path.join(dev_envs.split(" ")[1], ".env*"), recursive=False
            ):
                with open(f"{filename}", "r") as f:
                    output = f.read()
                    if just_variables:
                        assert output == "\n".join(
                            formatting_engine(test_env.split("\n"))
                        )
                    else:
                        assert output == test_env


@pytest.mark.parametrize(
    "source, dev_env, dev_envs, just_variables",
    [
        ("", "", "", ""),
        ("-s .env", "", "", ""),
        ("-s .env", "-d .env.dev", "", ""),
        ("-s .env", "-d .env.dev", "-ds dev_envs/", ""),
        ("-s .env", "-d .env.dev", "-ds dev_envs/", "--just-variables"),
    ],
)
def test_standard_sync_invalid_path(source, dev_env, dev_envs, just_variables):
    runner = CliRunner()
    with runner.isolated_filesystem():
        args = f"{source} {dev_env} {dev_envs} {just_variables}"
        result = runner.invoke(main, args=args)
        assert result.exception
        assert result.exit_code == 2


def test_standard_sync_invlaid_source_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, "-s .env")
        assert result.exception
        assert result.exit_code == 2


def test_standard_sync_invlaid_dev_envs_dir():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, "-ds dev_envs/")
        assert result.exception
        assert result.exit_code == 2


def test_standard_sync_invlaid_prod_envs_dir():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, "-ps prod_envs/")
        assert result.exception
        assert result.exit_code == 2

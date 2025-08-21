from fastshell.cli.cli import CLI
import pytest


cli = CLI()


@cli.command("add", multitypes=True)
def add(fn: int, sn: int) -> int:
    """
    :param fn:
    :param sn:
    :return int:

    Simple function that adds two numbers.
    """
    return fn + sn


@cli.command("echo")
def echo(msg: str) -> str:
    """
    :param msg:
    :return str:

    Simple function that prints some text.
    """
    return f"ECHO: {msg}"


def test_add_command(capfd):
    cli.main(
        debugging=True,
        fake_args=["add", "/:", "fn=4", "sn=8", ":/"]
    )
    out, err = capfd.readouterr()
    assert "12" in out
    assert err == ""


def test_echo_command(capfd):
    cli.main(
        debugging=True,
        fake_args=["echo", "/:", "msg=Hello", ":/"]
    )
    out, err = capfd.readouterr()
    print(out)
    assert "ECHO: Hello" in out
    assert err == ""

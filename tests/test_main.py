from unittest.mock import patch, MagicMock
from project_x.main import main


def test_main_exists():
    assert callable(main)


def test_main_exits_on_quit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "quit")
    with patch("project_x.main.chat"):
        main()


def test_main_handles_chat_error(monkeypatch):
    inputs = iter(["hello", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with patch("project_x.main.chat", side_effect=Exception("Ollama not running")):
        main()  # should not raise


def test_main_streams_response(monkeypatch, capsys):
    inputs = iter(["hello", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    chunk = MagicMock()
    chunk.get = lambda key, default=None: {"message": {"content": "hi"}}.get(key, default)

    with patch("project_x.main.chat", return_value=[chunk]):
        main()

    captured = capsys.readouterr()
    assert "hi" in captured.out

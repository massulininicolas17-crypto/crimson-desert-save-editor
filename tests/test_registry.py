"""Registry collision + dispatch tests for the plugin host."""
import pytest

from crimson_desert_host.registry import ExtensionRegistry


class _Fake:
    name = "fake"
    commands = ["fake.ping"]

    def handle(self, payload):
        return {"pong": payload}


def test_dispatch():
    reg = ExtensionRegistry()
    reg.activate(_Fake())
    assert reg.resolve("fake.ping").module.handle({"x": 1}) == {"pong": {"x": 1}}


def test_collision():
    reg = ExtensionRegistry()
    reg.activate(_Fake())
    with pytest.raises(RuntimeError):
        reg.activate(_Fake())
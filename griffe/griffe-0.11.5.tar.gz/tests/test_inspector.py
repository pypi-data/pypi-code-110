"""Test inspection mechanisms."""


from griffe.expressions import Name
from tests.helpers import temporary_inspected_module


def test_annotations_from_builtin_types():
    """Assert builtin types are correctly transformed to annotations."""
    with temporary_inspected_module("def func(a: int) -> str: pass") as module:
        func = module["func"]
        assert func.parameters[0].name == "a"
        assert func.parameters[0].annotation == Name("int", full="int")
        assert func.returns == Name("str", full="str")


def test_annotations_from_classes():
    """Assert custom classes are correctly transformed to annotations."""
    with temporary_inspected_module("class A: pass\ndef func(a: A) -> A: pass") as module:
        func = module["func"]
        assert func.parameters[0].name == "a"
        assert func.parameters[0].annotation == Name("A", full=f"{module.name}.A")
        assert func.returns == Name("A", full=f"{module.name}.A")


def test_class_level_imports():
    """Assert annotations using class-level imports are resolved."""
    with temporary_inspected_module(
        """
        class A:
            from io import StringIO
            def method(self, p: StringIO):
                pass
        """
    ) as module:
        method = module["A.method"]
        assert method.parameters["p"].annotation == Name("StringIO", full="io.StringIO")

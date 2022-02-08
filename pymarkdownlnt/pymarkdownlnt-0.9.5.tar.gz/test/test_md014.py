"""
Module to provide tests related to the MD014 rule.
"""
from test.markdown_scanner import MarkdownScanner

import pytest


@pytest.mark.rules
def test_md014_good_shell_example():
    """
    Test to make sure this rule does not trigger with a document that
    contains a fenced block with a `shell` tag and no leading $.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md014/good_shell_example.md",
    ]

    expected_return_code = 0
    expected_output = ""
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md014_good_shell_example_some_output():
    """
    Test to make sure this rule does not trigger with a document that
    contains a fenced block with a `shell` tag and mixed lines with leading $
    and no leading $.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md014/good_shell_example_some_output.md",
    ]

    expected_return_code = 0
    expected_output = ""
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md014_bad_shell_example():
    """
    Test to make sure this rule does trigger with a document that
    contains a fenced block with a `shell` tag and only leading $.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md014/bad_shell_example.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md014/bad_shell_example.md:2:1: "
        + "MD014: Dollar signs used before commands without showing output (commands-show-output)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md014_bad_shell_example_with_leading_space():
    """
    Test to make sure this rule not trigger with a document that
    contains a fenced block with a `shell` tag and only leading $
    with leading space before that.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md014/bad_shell_example_with_leading_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md014/bad_shell_example_with_leading_space.md:2:2: "
        + "MD014: Dollar signs used before commands without showing output (commands-show-output)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md014_bad_shell_example_indented():
    """
    Test to make sure this rule not trigger with a document that
    contains an indented block with leading $ that looks like shell output.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md014/bad_shell_example_indented.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md014/bad_shell_example_indented.md:3:5: "
        + "MD014: Dollar signs used before commands without showing output (commands-show-output)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )

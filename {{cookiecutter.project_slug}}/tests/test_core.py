{% if cookiecutter.include_sample_code == "yes" %}from {{ cookiecutter.package_name }}.core import sample_function


def test_sample_function() -> None:
    # Test with default multiplier
    assert sample_function([1, 2, 3]) == [1.0, 2.0, 3.0]
    # Test with custom multiplier
    assert sample_function([1, 2, 3], 2.0) == [2.0, 4.0, 6.0]
{% endif %}
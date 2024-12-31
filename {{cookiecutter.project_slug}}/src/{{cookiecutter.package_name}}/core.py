{% if cookiecutter.include_sample_code == "yes" %}from typing import Optional


def sample_function(input_list: list[int], multiplier: Optional[float] = None) -> list[float]:
    """Sample function with type hints.

    :param input_list: List of integers to process
    :param multiplier: Optional multiplier to apply to each element
    :return: List of processed numbers
    """
    if multiplier is None:
        multiplier = 1.0
    return [x * multiplier for x in input_list]


if __name__ == "__main__":
    print(sample_function([32, 12], 1))
{% endif %}
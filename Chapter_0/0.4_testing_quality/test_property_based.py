"""
Property-Based Testing with Hypothesis

Hypothesis generates test cases automatically to find edge cases.

Run tests with:
    uv add --dev hypothesis
    uv run pytest test_property_based.py -v
"""

import pytest
from hypothesis import given, strategies as st, assume, settings
from hypothesis import HealthCheck


# ============================================================================
# 1. BASIC PROPERTY-BASED TESTS
# ============================================================================

def add(a, b):
    """Simple addition"""
    return a + b


@given(st.integers(), st.integers())
def test_add_is_commutative(a, b):
    """Test that addition is commutative: a + b == b + a"""
    assert add(a, b) == add(b, a)


@given(st.integers(), st.integers())
def test_add_is_associative(a, b):
    """Test that (a + b) + 0 == a + b"""
    c = 0
    assert add(add(a, b), c) == add(a, add(b, c))


# ============================================================================
# 2. TESTING WITH STRINGS
# ============================================================================

def reverse_string(s: str) -> str:
    """Reverse a string"""
    return s[::-1]


@given(st.text())
def test_reverse_is_idempotent(s):
    """Reversing twice gives original string"""
    assert reverse_string(reverse_string(s)) == s


@given(st.text(), st.text())
def test_reverse_concatenation(s1, s2):
    """Reverse of concatenation equals reversed parts reversed"""
    assert reverse_string(s1 + s2) == reverse_string(s2) + reverse_string(s1)


# ============================================================================
# 3. TESTING WITH LISTS
# ============================================================================

def sum_list(lst):
    """Sum a list of numbers"""
    return sum(lst)


@given(st.lists(st.integers()))
def test_sum_is_additive(lst):
    """Sum of list plus empty list equals original sum"""
    assert sum_list(lst) + sum_list([]) == sum_list(lst)


@given(st.lists(st.integers(min_value=0, max_value=100)))
def test_sum_is_positive(lst):
    """Sum of positive numbers is positive or zero"""
    assert sum_list(lst) >= 0


# ============================================================================
# 4. FILTERING TEST CASES WITH ASSUME
# ============================================================================

@given(st.integers(), st.integers())
def test_divide_property(a, b):
    """Test division (skip when b == 0)"""
    assume(b != 0)  # Skip if b is zero
    
    quotient = a / b
    product = quotient * b
    
    # Check that (a / b) * b ≈ a (with floating point tolerance)
    assert abs(product - a) < 0.0001


# ============================================================================
# 5. COMPLEX STRATEGIES
# ============================================================================

@given(
    st.lists(
        st.integers(min_value=0, max_value=1000),
        min_size=0,
        max_size=100
    )
)
def test_sorted_list_is_sorted(lst):
    """Test that sorted list is actually sorted"""
    sorted_lst = sorted(lst)
    
    for i in range(len(sorted_lst) - 1):
        assert sorted_lst[i] <= sorted_lst[i + 1]


@given(st.dictionaries(st.text(), st.integers()))
def test_dict_keys_exist(d):
    """Test that all keys in a dict can be accessed"""
    for key in d.keys():
        # Should not raise KeyError
        _ = d[key]


# ============================================================================
# 6. STATEFUL TESTING (ADVANCED)
# ============================================================================

class Counter:
    """Simple counter for testing"""
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1
    
    def decrement(self):
        self.value -= 1
    
    def get(self):
        return self.value


@given(st.lists(st.sampled_from(["increment", "decrement"])))
def test_counter_operations(operations):
    """Test counter with sequence of operations"""
    counter = Counter()
    
    for op in operations:
        if op == "increment":
            counter.increment()
        else:
            counter.decrement()
    
    # Count increments and decrements
    increments = operations.count("increment")
    decrements = operations.count("decrement")
    
    assert counter.get() == increments - decrements


# ============================================================================
# 7. BOUNDED TESTING
# ============================================================================

@given(
    st.lists(
        st.integers(),
        min_size=1,
        max_size=1000
    )
)
def test_max_is_max(lst):
    """Test that max() returns the maximum element"""
    assert max(lst) >= all(x for x in lst)


# ============================================================================
# 8. HYPOTHESIS SETTINGS
# ============================================================================

@settings(max_examples=1000)  # Run 1000 examples instead of default 100
@given(st.integers(min_value=0, max_value=100))
def test_with_custom_settings(n):
    """Test with custom Hypothesis settings"""
    assert n >= 0 and n <= 100


@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.too_slow]  # Suppress slow test warnings
)
@given(st.lists(st.integers(), min_size=0, max_size=100))
def test_slow_operation(lst):
    """Test slow operation without health check warnings"""
    # Some potentially slow operation
    result = sum(x * x for x in lst)
    assert isinstance(result, int)


# ============================================================================
# 9. CUSTOM STRATEGIES
# ============================================================================

# Strategy for positive integers
positive_integers = st.integers(min_value=1)


# Strategy for email-like strings
email_strategy = st.emails()


@given(positive_integers)
def test_with_custom_strategy(n):
    """Test using custom strategy"""
    assert n > 0


@given(email_strategy)
def test_email_format(email):
    """Test email-like strings"""
    assert "@" in email


# ============================================================================
# 10. TESTING PARSING/VALIDATION
# ============================================================================

def parse_json_string(s: str) -> dict:
    """Parse simple JSON (hypothetical)"""
    import json
    return json.loads(s)


@given(st.dictionaries(st.text(), st.integers()))
def test_parse_json_roundtrip(d):
    """Test that dict -> JSON -> dict works"""
    import json
    
    json_str = json.dumps(d)
    parsed = parse_json_string(json_str)
    
    assert parsed == d


# ============================================================================
# COMBINING STRATEGIES
# ============================================================================

@given(
    st.lists(st.integers()),
    st.lists(st.integers())
)
def test_concatenation_length(lst1, lst2):
    """Test that concatenated list has correct length"""
    combined = lst1 + lst2
    assert len(combined) == len(lst1) + len(lst2)


@given(
    st.tuples(
        st.integers(min_value=0, max_value=100),
        st.integers(min_value=0, max_value=100),
    )
)
def test_coordinate_validity(coords):
    """Test coordinate validation"""
    x, y = coords
    assert 0 <= x <= 100
    assert 0 <= y <= 100
    assert x * y >= 0  # Both non-negative

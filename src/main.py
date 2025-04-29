from tests.my_test import MyTest
from base.test_result import TestResult
from tests.test_case_test import TestCaseTest

# ------- Questão 3 -------

# result = TestResult()

# test = MyTest('test_a')
# test.run(result)

# test = MyTest('test_b')
# test.run(result)

# test = MyTest('test_c')
# test.run(result)

# print(result.summary())

# ------- Questão 4 -------

result = TestResult()

test = TestCaseTest('test_result_success_run')
test.run(result)

test = TestCaseTest('test_result_failure_run')
test.run(result)

test = TestCaseTest('test_result_error_run')
test.run(result)

test = TestCaseTest('test_result_multiple_run')
test.run(result)

test = TestCaseTest('test_was_set_up')
test.run(result)

test = TestCaseTest('test_was_run')
test.run(result)

test = TestCaseTest('test_was_tear_down')
test.run(result)

test = TestCaseTest('test_template_method')
test.run(result)

print(result.summary())
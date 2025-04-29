from tests.my_test import MyTest
from base.test_result import TestResult
from tests.test_case_test import TestCaseTest
from base.test_suite import TestSuite
from tests.test_suite_test import TestSuiteTest

# ------- Questão 2 -------

# test = MyTest('test_a')
# test.run()

# test = MyTest('test_b')
# test.run()

# test = MyTest('test_c')
# test.run()

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

# result = TestResult()

# test = TestCaseTest('test_result_success_run')
# test.run(result)

# test = TestCaseTest('test_result_failure_run')
# test.run(result)

# test = TestCaseTest('test_result_error_run')
# test.run(result)

# test = TestCaseTest('test_result_multiple_run')
# test.run(result)

# test = TestCaseTest('test_was_set_up')
# test.run(result)

# test = TestCaseTest('test_was_run')
# test.run(result)

# test = TestCaseTest('test_was_tear_down')
# test.run(result)

# test = TestCaseTest('test_template_method')
# test.run(result)

# print(result.summary())

# ------- Questão 5 -------

result = TestResult()
suite = TestSuite()

suite.add_test(TestCaseTest('test_result_success_run'))
suite.add_test(TestCaseTest('test_result_failure_run'))
suite.add_test(TestCaseTest('test_result_error_run'))
suite.add_test(TestCaseTest('test_result_multiple_run'))
suite.add_test(TestCaseTest('test_was_set_up'))
suite.add_test(TestCaseTest('test_was_run'))
suite.add_test(TestCaseTest('test_was_tear_down'))
suite.add_test(TestCaseTest('test_template_method'))

suite.add_test(TestSuiteTest('test_suite_size'))
suite.add_test(TestSuiteTest('test_suite_success_run'))
suite.add_test(TestSuiteTest('test_suite_multiple_run'))

suite.run(result)
print(result.summary())
from common import log_util
import pytest


log = log_util.Log(__file__)
logger = log.Logger


def assert_equal(expected, actual):
    try:
        assert expected == actual
    except AssertionError:
        logger.error('预期结果为: {0}, 实际结果为: {1}'.format(expected, actual))


def assert_not_equal(expected, actual):
    try:
        assert expected != actual
    except AssertionError:
        logger.error('{0} 等于 {1}'.format(expected, actual))


def assert_in(expected, actual):
    try:
        assert expected in actual
    except AssertionError:
        logger.warning('{0} 不包含于 {1}'.format(expected, actual))


def assert_not_in(expected, actual):
    try:
        assert expected not in actual
    except AssertionError:
        logger.error('{0} 包含于 {1}'.format(expected, actual))


def assert_true(value):
    try:
        assert value is True
    except AssertionError:
        logger.error('{0} 为假'.format(value))


if __name__ == '__main__':
    assert_equal(1, 2)
    assert_not_equal(1, 1)
    assert_in(1, (5, 6))
    assert_true(0)
# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools.timeintervaltools import *


def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_01():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 0
    expected_payloads = ('a',)
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks

def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_02():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 9
    expected_payloads = ('b', 'c', 'd',)
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks

def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_03():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 14
    expected_payloads = ()
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks

def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_04():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 19
    expected_payloads = ('e', 'f', 'g', 'h',)
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks

def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_05():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 26
    expected_payloads = ('i', 'j',)
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks

def test_timeintervaltools_TimeIntervalTree_find_intervals_intersecting_or_tangent_to_offset_06():
    blocks = timeintervaltools.make_test_intervals()
    target_offset = 30
    expected_payloads = ('i',)
    expected_blocks = TimeIntervalTree([x for x in blocks if x['name'] in expected_payloads])
    for i in range(len(blocks)):
        blocks.append(blocks.pop(0)) # rotate to permute tree construction
        tree = TimeIntervalTree(blocks)
        actual_blocks = tree.find_intervals_intersecting_or_tangent_to_offset(target_offset)
        assert expected_blocks == actual_blocks
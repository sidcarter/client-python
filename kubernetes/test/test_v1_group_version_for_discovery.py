# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_group_version_for_discovery import V1GroupVersionForDiscovery


class TestV1GroupVersionForDiscovery(unittest.TestCase):
    """ V1GroupVersionForDiscovery unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1GroupVersionForDiscovery(self):
        """
        Test V1GroupVersionForDiscovery
        """
        model = kubernetes.client.models.v1_group_version_for_discovery.V1GroupVersionForDiscovery()


if __name__ == '__main__':
    unittest.main()

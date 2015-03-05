#!/usr/bin/python
# coding=utf-8
################################################################################

from test import CollectorTestCase
from test import get_collector_config
from test import unittest
from mock import patch

from diamond.collector import Collector
from example import PsutilCollector

################################################################################


class TestPsutilCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('PsutilCollector', {
            'interval': 10
        })

        self.collector = PsutilCollector(config, None)

    def test_import(self):
        self.assertTrue(PsutilCollector)

    @patch.object(Collector, 'publish')
    def test(self, publish_mock):
        self.collector.collect()

        metrics = {
            'my.example.metric':  42
        }

        self.setDocExample(collector=self.collector.__class__.__name__,
                           metrics=metrics,
                           defaultpath=self.collector.config['path'])
        self.assertPublishedMany(publish_mock, metrics)

################################################################################
if __name__ == "__main__":
    unittest.main()

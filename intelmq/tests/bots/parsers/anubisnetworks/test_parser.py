# -*- coding: utf-8 -*-
import os.path
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils
from intelmq.bots.parsers.anubisnetworks.parser import AnubisNetworksParserBot

with open(os.path.join(os.path.dirname(__file__), 'example_report.json')) as handle:
    EXAMPLE_RAW = handle.read()
with open(os.path.join(os.path.dirname(__file__), 'example_report2.json')) as handle:
    EXAMPLE2_RAW = handle.read()
with open(os.path.join(os.path.dirname(__file__), 'example_report3.json')) as handle:
    EXAMPLE3_RAW = handle.read()
with open(os.path.join(os.path.dirname(__file__), 'example_report_dns.json')) as handle:
    EXAMPLE_DNS_RAW = handle.read()

EXAMPLE_REPORT = {"feed.url": "https://prod.cyberfeed.net/stream?key=7b7cd29c7a424b2980ca",
                  "feed.accuracy": 100.0,
                  "__type": "Report",
                  "feed.name": "AnubisNetworks",
                  "raw": utils.base64_encode(EXAMPLE_RAW),
                  "time.observation": "2016-04-19T23:16:08+00:00"
                  }
EXAMPLE_EVENT  = {"classification.type": "malware",
                  "destination.port": 80,
                  "feed.accuracy": 100.0,
                  "malware.name": "nivdort",
                  "event_description.text": "Sinkhole attempted connection",
                  "time.source": "2017-01-10T09:45:30+00:00",
                  "source.ip": "203.0.113.2",
                  "source.network": "203.0.113.0/24",
                  "feed.url": "https://prod.cyberfeed.net/stream",
                  "source.geolocation.country": "Austria",
                  "source.geolocation.cc": "AT",
                  "source.geolocation.region": "Vienna",
                  "source.geolocation.city": "Vienna",
                  "source.geolocation.longitude": 13.,
                  "source.geolocation.latitude": 37.,
                  "source.asn": 65536,
                  "source.as_name": "ExampleAS",
                  "time.observation": "2016-04-19T23:16:08+00:00",
                  "__type": "Event",
                  "feed.name": "AnubisNetworks",
                  "raw": EXAMPLE_REPORT['raw'],
                  'extra._provider': 'spikens',
                  'extra.request_method': 'POST',
                  'extra._origin': 'dnsmalware',
                  'extra.dns_query_type': 'A',
                  }

EXAMPLE_REPORT2 = {"feed.name": "AnubisNetworks",
                   "feed.accuracy": 100.0,
                   "feed.url": "https://prod.cyberfeed.net/stream?key=7b7cd29c7a424b2980ca",
                   "raw": utils.base64_encode(EXAMPLE2_RAW),
                   "__type": "Report",
                   "time.observation":
                   "2016-04-19T23:16:10+00:00"
                   }
EXAMPLE_EVENT2  = {"feed.name": "AnubisNetworks",
                   "malware.name": "spyapp",
                   "destination.fqdn": "example.net",
                   "source.ip": "190.124.67.211",
                   "destination.ip": "190.124.67.212",
                   "__type": "Event",
                   "source.geolocation.country": "Dominican Republic",
                   "time.source": "2016-04-19T23:15:54+00:00",
                   "source.port": 52888,
                   "time.observation": "2016-04-19T23:16:10+00:00",
                   "extra.request_method": "POST",
                   "feed.url": "https://prod.cyberfeed.net/stream",
                   "destination.port": 80,
                   "feed.accuracy": 100.0,
                   "raw": EXAMPLE_REPORT2['raw'],
                   "classification.type": "malware",
                   "event_description.text": "Sinkhole attempted connection"
                   }

EXAMPLE_REPORT3 = {"feed.url": "https://prod.cyberfeed.net/stream?key=7b7cd29c7a424b2980ca",
                   "raw": utils.base64_encode(EXAMPLE3_RAW),
                   "__type": "Report",
                   "time.observation": "2016-04-19T23:16:10+00:00"
                   }
EXAMPLE_EVENT3  = {"malware.name": "malwname",
                   "source.ip": "203.0.113.2",
                   "source.port": 59645,
                   "__type": "Event",
                   "time.source": "2020-04-07T09:45:14+00:00",
                   "time.observation": "2016-04-19T23:16:10+00:00",
                   "feed.url": "https://prod.cyberfeed.net/stream",
                   "destination.ip": "203.0.113.1",
                   "destination.port": 80,
                   "raw": EXAMPLE_REPORT3['raw'],
                   "classification.type": "malware",
                   "classification.identifier": "MalwName",
                   "event_description.text": "Sinkhole attempted connection",
                   "extra.metadata": {
                       "flowbits": [
                           "_mt_s",
                           "_mt_sa",
                           "_mt_a",
                           "_mt_p"
                       ], },
                   "protocol.application": "http",
                   "extra.malware.severity": 2,
                   "extra.malware.categories": [
                       "Adware"
                   ],
                   "extra.request_method": "GET",
                   "destination.fqdn": "example.com",
                   "destination.urlpath": "/path",
                   "destination.url": "http://example.com/path",
                   "extra.user_agent": "Agent",
                   "extra.communication.headers": [
                       "Connection: Keep-Alive"
                   ],
                   "extra.communication.x_forwarded_for": [
        "10.26.116.22"
      ],
                   "extra.communication.type": "sinkhole",
                   "extra._origin": "infections",
                   "source.network": "203.0.113.0/24",
                   "source.geolocation.cc": "AT",
                   "source.geolocation.country": "Austria",
                   "source.geolocation.region": "Wien",
                   "extra.source.geolocation.region_code": "09",
                   "source.geolocation.city": "Vienna",
                   "extra.source.geolocation.postal_code": "1210",
                   "source.geolocation.latitude": 48.2993,
                   "source.geolocation.longitude": 16.3479,
                   "source.asn": 1,
                   "source.as_name": "Example AS Name",
                   'extra.communication.cookies': 'dummy=cookie|foo=bar',
                   "extra.tracking.id": "6b49906822f2431894f295921b3c1647",
                   "extra.tracking.last.ip": "203.0.113.3",
                   "extra.first_seen": 1572960032,
                   "extra.last_seen": 1586318132,
                   "extra.tracking.checkins": 2158,
                   "extra.tracking.changes": 5,
                   "extra.tracking.tr": "bd592af93f1a4deca63ee18e87170374",
                   "extra.days_seen": 154,
                   "extra.tracking.same_ip": "true",
                    'extra.tracking.last.as_name': 'Example AS Name',
  'extra.tracking.last.asn': 1,
  'extra.tracking.last.geolocation.cc': 'AT',
  'extra.tracking.last.geolocation.city': 'Vienna',
  'extra.tracking.last.geolocation.country': 'Austria',
  'extra.tracking.last.geolocation.latitude': 48.2993,
  'extra.tracking.last.geolocation.longitude': 16.3479,
  'extra.tracking.last.geolocation.postal_code': '1210',
  'extra.tracking.last.geolocation.region': 'Wien',
  'extra.tracking.last.geolocation.region_code': '09',
  'extra.tracking.last.network': '203.0.113.3/24',
      "extra.tracking.last.geolocation.dma_code": 528,
    "extra.tracking.last.geolocation.area_code": 305,
    "extra.tracking.last.geolocation.metro_code": 528,
  'extra.communication.unverified_domain': 'true',
    'extra.communication.http.host.as_name': 'Example AS Name',
  'extra.communication.http.host.asn': 29791,
  'extra.communication.http.host.geolocation.cc': 'US',
  'extra.communication.http.host.geolocation.country': 'United States',
  'extra.communication.http.host.geolocation.latitude': 37.751,
  'extra.communication.http.host.geolocation.longitude': -97.822,
  'extra.communication.http.host.network': '203.0.113.4/21',

                   }


EXAMPLE_REPORT_DNS = {"feed.url": "https://prod.cyberfeed.net/stream?key=7b7cd29c7a424b2980ca",
                   "raw": utils.base64_encode(EXAMPLE_DNS_RAW),
                   "__type": "Report",
                   "time.observation": "2016-04-19T23:16:10+00:00"
                   }
EXAMPLE_EVENT_DNS  = {"malware.name": "malware name dns",
                   "source.ip": "203.0.113.2",
                   "source.port": 11138,
                   "__type": "Event",
  'time.source': '2020-04-08T04:25:17+00:00',
                   "time.observation": "2016-04-19T23:16:10+00:00",
                   "feed.url": "https://prod.cyberfeed.net/stream",
                   "destination.ip": "203.0.113.1",
                   "destination.port": 53,
                   "raw": EXAMPLE_REPORT_DNS['raw'],
                   "classification.type": "malware",
                   "classification.identifier": "Malware name DNS",
                   "event_description.text": "Sinkhole attempted connection",
                   "protocol.application": "dns",
                   "extra.malware.severity": 2,
                   "extra.malware.categories": [
      "Adware",
      "Trojan"
                   ],
                   "destination.fqdn": "example.com",
                   "extra.communication.type": "sinkhole",
                   "extra._origin": "infections",
                   "source.network": "203.0.112.0/23",
                   "source.geolocation.cc": "AT",
                   "source.geolocation.country": "Austria",
                   "source.geolocation.region": "Steiermark",
                   "extra.source.geolocation.region_code": "06",
                   "source.geolocation.city": "Graz",
                   "extra.source.geolocation.postal_code": "8000",
                   "source.geolocation.latitude": 47.0832,
                   "source.geolocation.longitude": 15.5666,
                   "source.asn": 1,
                   "source.as_name": "Example AS Name",
                                     'extra.dns_query_type': 'A',
                   }


class TestAnubisNetworksParserBot(test.BotTestCase, unittest.TestCase):

    @classmethod
    def set_bot(cls):
        cls.bot_reference = AnubisNetworksParserBot
        cls.default_input_message = EXAMPLE_REPORT

    def test_event(self):
        """ Test: report without fqdn """
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT)

    def test_with_fqdn(self):
        """ Test: report with fqdn """
        self.input_message = EXAMPLE_REPORT2
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT2)

    def test_third(self):
        """ Test: report from 2020 """
        self.input_message = EXAMPLE_REPORT3
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT3)

    def test_dns(self):
        """ Test: report with DNS data """
        self.input_message = EXAMPLE_REPORT_DNS
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT_DNS)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

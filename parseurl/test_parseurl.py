#### 
import unittest 

def get_protocol(url):
    return "http"

class test_parseurl(unittest.TestCase):
    def test_protocol_http(self):
        protocol = get_protocol("http://www.site.com")
        self.assertEqual("http", protocol)

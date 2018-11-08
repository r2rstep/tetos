from utils.fetchers import fetch_html

from unittest import TestCase
from mock import patch, Mock, call


@patch('utils.fetchers.url_request')
class TestFetchHtml(TestCase):
    def test_fetch_html(self, url_request):
        responses = [Mock(), Mock(), Mock(), Mock()]
        url_request.OpenerDirector.return_value.open.side_effect = responses
        responses[0].read.return_value = '<html>' \
                                         'frame_0' \
                                         '<iframe src="frame_1.0_src"></iframe>' \
                                         '<iframe src="www.example.com/dir1/frame_1.1_src"></iframe>' \
                                         '</html>'
        responses[1].read.return_value = '<html>' \
                                         'frame_1.0' \
                                         '<iframe src="../frame_2.0_src"></iframe>' \
                                         '</html>'
        responses[2].read.return_value = '<html>' \
                                         'frame_2.0' \
                                         '</html>'
        responses[3].read.return_value = '<html>' \
                                         'frame_1.1' \
                                         '</html>'

        expected = [resp.read.return_value for resp in [responses[2], responses[1], responses[3], responses[0]]]
        html = fetch_html('http://www.example.com/dir0/src.html')
        self.assertListEqual(expected, html)

        url_request.OpenerDirector.return_value.open.assert_has_calls([call('http://www.example.com/dir0/src.html'),
                                                                       call('http://www.example.com/dir0/frame_1.0_src'),
                                                                       call('http://www.example.com/frame_2.0_src'),
                                                                       call('www.example.com/dir1/frame_1.1_src')])

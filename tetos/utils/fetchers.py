from bs4 import BeautifulSoup

from urllib import request as url_request, parse as url_parse


def fetch_html(src: str):
    def _get_frames(bs):
        frames = bs.find_all('iframe')
        if not frames:
            frames = bs.find_all('frame')
        return frames

    resp = url_request.urlopen(src)

    bs = BeautifulSoup(resp, 'html.parser')

    parsed_src = url_parse.urlparse(src)
    base_addr = '{uri.netloc}'.format(uri=parsed_src)
    htmls = []
    for frame in _get_frames(bs):
        frame_src = frame['src']
        if base_addr not in frame_src:
            frame_src = url_parse.urljoin(src, frame_src)
        htmls.extend(fetch_html(frame_src))
    htmls.extend([str(bs)])

    return htmls

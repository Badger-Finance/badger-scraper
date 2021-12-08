from scraper.helpers import subsctract_statis_js_files

CONTENT = '<script charset="utf-8" src="/static/js/52.0625a25d.chunk.js"></script><script charset='\
          '"utf-8" src="/static/js/37.5a8c459d.chunk.js"></script><script charset="utf-8" ' \
          'src="/static/js/75.532f8220.chunk.js">'


def test_subsctract_statis_js_files():
    parsed_content = subsctract_statis_js_files(CONTENT)
    # chunk.js and chunk.css should be filtered out
    assert parsed_content == '<script charset="utf-8" ></script><script ' \
                             'charset="utf-8" ></script><script charset="utf-8" >'


def test_subsctract_statis_js_files__no_match():
    content = '<script charset="utf-8" ></script><script ' \
              'charset="utf-8" ></script><script charset="utf-8" >'
    assert subsctract_statis_js_files(content) == content

from playwright.sync_api import expect

def assert_url_contains(page, expected: str):
    expect(page).to_have_url(lambda url: expected in url)

import app


def test_header_present(dash_duo):
    dash_duo.start_server(app.app)
    header = dash_duo.find_element("#app-header")
    assert header is not None


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app.app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app.app)
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None

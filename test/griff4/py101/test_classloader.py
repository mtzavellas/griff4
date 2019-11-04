from pytest_mock import MockFixture


def test_b_package(mocker: MockFixture):
    import griff4.py101.a.mya as mya
    import griff4.py101.a.b.myb as myb
    mock_cls = mocker.patch('griff4.py101.a.b.myb.AClass')
    mock_instance = mock_cls.return_value
    print(mock_instance)
    print(mya.AClass())
    print(myb.b_method())

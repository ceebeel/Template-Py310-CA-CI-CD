from src.main import main


def test_main(capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out == "Hello World!\n"

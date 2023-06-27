import pytest
import importlib
import sys
import io
import builtins

@pytest.mark.parametrize("name,start,end,means,itinerary",
                        [['Christian', 'Aachen', 'Berlin', 'Train', "Christian wants to travel from Aachen to Berlin by Train"],
                        ['Joe', 'Louisville', 'Chicago', 'Plane', "Joe wants to travel from Louisville to Chicago by Plane"],
                        ['Bob', 'Lexington', 'Chattanooga', 'Car', "Bob wants to travel from Lexington to Chattanooga by Car"]
                        ])
def test_itinerary(name, start, end, means, itinerary, monkeypatch):
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        inputs = iter([name, start, end, means])
        m.setattr(builtins, "input", lambda _: next(inputs))
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("travel", None)
        importlib.import_module(name="travel", package="files")
    
    assert mocked_stdout.getvalue().strip() == itinerary
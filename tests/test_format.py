import os
from osmem.memory import output_formatter, get_processes

def test_minimal_format_spec():
    column_lengths = {'pid': 0, 'totalmem': 0, 'procmem': 0, 'procname': 0}

    fmt, header = output_formatter(column_lengths, False, False)

    expected = ("PID  Aggregate  Process\n"
                "---  ---------  -------")

    assert expected == header
    assert '%3s  %9s  %-7s' == fmt


def test_dynamic_format_spec():
    column_lengths = {'pid': 4, 'totalmem': 10, 'procmem': 0, 'procname': 0}

    fmt, header = output_formatter(column_lengths, False, False)

    expected = (" PID   Aggregate  Process\n"
                "----  ----------  -------")

    assert expected == header
    assert '%4s  %10s  %-7s' == fmt


def test_get_processes():
    procs = get_processes()
    assert os.getpid() in procs

def test_get_ppid():
    procs = get_processes()
    proc = procs.get(os.getpid())

    # this python process has no parent pid in github's runner for some odd reason, so skip the test there
    if '/opt/hostedtoolcache' not in proc['exe']:
        assert os.getppid() == procs[os.getpid()].get('ppid')

[![unittest](https://img.shields.io/github/actions/workflow/status/jojje/osmem/push.yml?branch=master)](https://github.com/jojje/osmem/actions/workflows/push.yml)
[![PyPI - latest](https://img.shields.io/pypi/v/osmem?label=latest&logo=pypi)](https://pypi.org/project/osmem)
[![PyPI - Python](https://img.shields.io/pypi/pyversions/osmem?logo=pypi)](https://pypi.org/project/osmem)

# osmem

Shows memory usage information for process trees

## Install

```
pip install osmem
```

## Usage

Find out the top-n types of processes consuming most memory.
```
> osmem top -n 3

  PID  Aggregate  Process
-----  ---------  --------------------
 1516   12582 MB  firefox.exe
 3408    9048 MB  Code.exe
 4432    3627 MB  cmdagent.exe
```
Aggregates all processes with the same name, which makes it a whole lot easier to understand just how 
much memory all those tabs one forgets to close in firefox/chrome actually consume.

Get a break-down of all the processes on the system, how much memory each process consumes, and how the
memory usage aggregates up through the process hierarchy.
```
> osmem tree

  PID  Aggregate   Memory  Process
-----  ---------  -------  --------------------
    0      12 MB     0 MB  System Idle Process
    4      12 MB     0 MB    System
  800                1 MB      smss.exe
 3216               10 MB      MemCompression
  168                0 MB
  276              119 MB  Registry
  688      11 MB     4 MB  cmd.exe
 1500                6 MB    conhost.exe
  920    5496 MB     1 MB  wininit.exe
 1088    5482 MB     7 MB    services.exe
    8                5 MB      svchost.exe
 1144                5 MB      svchost.exe
...
```

Since some processes are spawned several times with the same name, it may be beneficial to see the actual
command line arguments for each process. For instance, "svchost" on windows or "sshd" / "bash" /
"docker-proxy" on linux say very little about the _specific_ nature of such a process.

```
> osmem tree -c

  PID  Aggregate   Memory  Process              Command
-----  ---------  -------  -------------------  --------------------
    0      12 MB     0 MB  System Idle Process
    4      12 MB     0 MB    System
  800                1 MB      smss.exe         \SystemRoot\System32\smss.exe
 3216               10 MB      MemCompression
  168                0 MB
  276              119 MB  Registry
  688      11 MB     4 MB  cmd.exe              C:\Windows\System32\cmd.exe
 1500                6 MB    conhost.exe        \??\C:\Windows\system32\conhost.exe 0x4
  920    5498 MB     1 MB  wininit.exe          wininit.exe
 1088    5484 MB     8 MB    services.exe       C:\Windows\system32\services.exe
    8                5 MB      svchost.exe      C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted -p
 1144                4 MB      svchost.exe      C:\Windows\system32\svchost.exe -k LocalService -p -s nsi
...
```

```
$ osmem tree -c

  PID  Aggregate  Memory  Process              Command
-----  ---------  ------  -------------------  --------------------
    1     941 MB   11 MB  systemd  /sbin/init
  369              46 MB    systemd-journald   /lib/systemd/systemd-journald
  408               7 MB    systemd-udevd      /lib/systemd/systemd-udevd
  501               4 MB    rpcbind            /sbin/rpcbind -f -w
...
```

For *nix users, this is somewhat similar to `ps -wwef` but gets you the memory usage as well, and the memory aggregation.

## Development

To execute the main function of the programs, either of the following options are viable

* `osmem` as a CLI
* `python -m osmem` as a python package

To simplify development, common actions are provided via [Makefile](Makefile) targets:

* test - default targets, runs pytest on the project
* lint - performs flake8 and mypy linting
* build - create a wheel package distribution, ready to be shared with someone else.
* clean - removes temporary files generated as part of the package creation.

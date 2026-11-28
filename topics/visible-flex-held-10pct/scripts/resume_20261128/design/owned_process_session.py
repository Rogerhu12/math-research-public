"""Own a new child session until its leader and surviving descendants are reaped.

The leader is observed using waitid(WNOWAIT), never Popen.poll().  Its unreaped
PID/start-time identity therefore remains an anchor while the session is cleaned.
PID-number signals are used only for the verified leader's original process group;
other groups in this same session are signalled through identity-checked pidfds.
Nothing is signalled after the leader has been reaped or its identity has changed.
"""
import os
from pathlib import Path
import signal
import time


def process_identity(pid):
    directory = Path('/proc')/str(pid)
    try:
        text = (directory/'stat').read_text()
        fields = text[text.rfind(')')+2:].split()
        return dict(pid=int(pid), state=fields[0], ppid=int(fields[1]),
            pgid=int(fields[2]), sid=int(fields[3]), start_ticks=int(fields[19]),
            uid=directory.stat().st_uid)
    except (FileNotFoundError, ProcessLookupError):
        return None


class OwnedProcessSession:
    def __init__(self, process):
        for name in ('waitid', 'WNOWAIT', 'pidfd_open'):
            if not hasattr(os, name):
                raise RuntimeError('The session owner requires Linux '+name)
        if not hasattr(signal, 'pidfd_send_signal'):
            raise RuntimeError('The session owner requires pidfd_send_signal')
        identity = process_identity(process.pid)
        if (identity is None or identity['pid'] != identity['pgid']
                or identity['pid'] != identity['sid'] or identity['uid'] != os.getuid()):
            raise RuntimeError('The new child did not establish its verifiable owned session')
        self.process = process
        self.leader = identity
        self.reaped = False
        self.observed_returncode = None
        self.signals = []

    def _anchor(self):
        if self.reaped:
            raise RuntimeError('The owned leader is already reaped; no group signal is permitted')
        actual = process_identity(self.leader['pid'])
        keys = ('pid', 'pgid', 'sid', 'start_ticks', 'uid')
        if actual is None or any(actual[key] != self.leader[key] for key in keys):
            raise RuntimeError('The unreaped owned leader identity changed; no signal was sent')
        return actual

    def poll_leader(self):
        """Observe terminal status without freeing/reusing the ownership anchor."""
        if self.reaped:
            return self.process.returncode
        self._anchor()
        result = os.waitid(os.P_PID, self.leader['pid'], os.WEXITED|os.WNOHANG|os.WNOWAIT)
        if result is None:
            return None
        if result.si_pid != self.leader['pid']:
            raise RuntimeError('waitid returned an unrelated process')
        code = result.si_status if result.si_code == os.CLD_EXITED else -result.si_status
        self.observed_returncode = code
        return code

    def members(self, live_only=True):
        self._anchor()
        found = []
        for entry in Path('/proc').iterdir():
            if not entry.name.isdigit():
                continue
            value = process_identity(int(entry.name))
            if value is None or value['sid'] != self.leader['sid']:
                continue
            if (value['uid'] != self.leader['uid']
                    or value['start_ticks'] < self.leader['start_ticks']):
                raise RuntimeError('The owned session contains an unexpected process identity')
            if live_only and value['state'] in ('Z', 'X', 'x'):
                continue
            found.append(value)
        return found

    def _pidfd_signal(self, expected, signum):
        self._anchor()
        try:
            descriptor = os.pidfd_open(expected['pid'], 0)
        except ProcessLookupError:
            return False
        try:
            actual = process_identity(expected['pid'])
            keys = ('pid', 'sid', 'start_ticks', 'uid')
            if actual is None or any(actual[key] != expected[key] for key in keys):
                return False
            signal.pidfd_send_signal(descriptor, signum, None, 0)
            return True
        except ProcessLookupError:
            return False
        finally:
            os.close(descriptor)

    def signal_session(self, signum):
        self._anchor()
        before = self.members()
        if not before:
            return 0
        # The unreaped leader identity proves this process-group identifier has
        # not become somebody else's new session.  Covers fork races in its PGID.
        try:
            os.killpg(self.leader['pgid'], signum)
        except ProcessLookupError:
            pass
        other = 0
        for value in before:
            if value['pgid'] != self.leader['pgid']:
                other += int(self._pidfd_signal(value, signum))
        self.signals.append(dict(signal=int(signum), live_members_observed=len(before),
                                 other_group_pidfds_signalled=other))
        return len(before)

    def pause(self):
        self.signal_session(signal.SIGSTOP)
        # A child may have made its own process group or forked during the first
        # snapshot.  Repeat only until all observed same-session members stop.
        for _ in range(10):
            running = [value for value in self.members() if value['state'] not in ('T', 't')]
            if not running:
                return
            for value in running:
                self._pidfd_signal(value, signal.SIGSTOP)
            time.sleep(.01)
        raise RuntimeError('The owned session did not finish pausing')

    def resume(self):
        self.signal_session(signal.SIGCONT)

    def cleanup(self, term_timeout=25., kill_timeout=5.):
        if self.reaped:
            return dict(leader=dict(self.leader), returncode=self.process.returncode,
                        already_cleaned=True, signals=list(self.signals))
        initial = self.members()
        if initial:
            self.signal_session(signal.SIGCONT)
            self.signal_session(signal.SIGTERM)
            deadline = time.monotonic()+term_timeout
            while time.monotonic() < deadline:
                if not self.members() and self.poll_leader() is not None:
                    break
                time.sleep(.02)
        remaining = self.members()
        if remaining:
            self.signal_session(signal.SIGKILL)
            deadline = time.monotonic()+kill_timeout
            while time.monotonic() < deadline:
                if not self.members() and self.poll_leader() is not None:
                    break
                time.sleep(.02)
        remaining = self.members()
        code = self.poll_leader()
        if remaining or code is None:
            raise RuntimeError('Owned session still has live members; leader was not reaped')
        # All surviving same-session computation has ended.  Only now may its
        # original process-group/session number be released and later reused.
        actual = self.process.wait()
        self.reaped = True
        if actual != code:
            raise RuntimeError('Observed and reaped leader returncodes differ')
        return dict(leader=dict(self.leader), returncode=actual,
            initial_live_members=len(initial), remaining_live_members=0,
            signals=list(self.signals), leader_observed_with_WNOWAIT=True,
            leader_reaped_only_after_session_cleanup=True,
            all_signals_bound_to_original_owned_session=True)

# Actual regular-transport failure logs: read-only diagnosis

This public run executes no scientific process, imports no mathematical producer, and requests no Git Trees or blob-size audit.
The two original failures remain failures. Their elapsed time alone proves no scientific status.

Only exact full-log identities and bounded real stacks are retained. Full logs remain temporary.

## Original job 132786394695

- Run: 43705772615/1.
- Workflow commit: fb3a6f2bbfa8d5d72266e709bcccd0ebd1848b18
- Complete log identity: {"body_persisted": false, "bytes": 37679, "complete": true, "download_host": "productionresultssa4.blob.core.windows.net", "sha256": "b7ba79e739a16ee2179e51096dc8bcd58fa9494c30e3a1b87b9f540889734737"}
- Diagnostic error: null
- Complete original stack retained: True

```text
Traceback (most recent call last):
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 292, in <module>
    if __name__=="__main__":main()
                            ^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 115, in main
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com");sync()
                                                                                       ^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 98, in sync
    objects=git("ls-tree","-r","-l","HEAD","--",str(TOPIC)).stdout.splitlines()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 85, in git
    r=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/subprocess.py", line 1209, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/subprocess.py", line 2116, in _communicate
    self._check_timeout(endtime, orig_timeout, stdout, stderr)
  File "/usr/local/lib/python3.12/subprocess.py", line 1253, in _check_timeout
    raise TimeoutExpired(
subprocess.TimeoutExpired: Command '['git', '-c', 'safe.directory=/__w/math-research-public/math-research-public', 'ls-tree', '-r', '-l', 'HEAD', '--', 'topics/visible-flex-exact-nearby']' timed out after 900 seconds
```

## Original job 132791691389

- Run: 43707514815/1.
- Workflow commit: c9c96f3431a0ec6a8213e2359186531fb851f822
- Complete log identity: {"body_persisted": false, "bytes": 36778, "complete": true, "download_host": "productionresultssa14.blob.core.windows.net", "sha256": "a0d95b80fc1e189ebf9185e959b00600dfd3eaaf0fde983a5844de5a3e2c97ed"}
- Diagnostic error: null
- Complete original stack retained: True

```text
Traceback (most recent call last):
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 537, in <module>
    if __name__=="__main__":main()
                            ^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 531, in main
    sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    ^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 290, in sync
    capacity,unused_blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 82, in topic_tree_metadata
    entries=request_tree(tree)
            ^^^^^^^^^^^^^^^^^^
  File "/__w/math-research-public/math-research-public/topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_regular_transport_first_local_vector_public_worker.py", line 68, in request_tree
    raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
RuntimeError: the Git tree metadata request returned HTTP 404
```

The source and scientific17-pin manifest are unchanged. These receipts do not assert the current exact topic size.
Combined publication is bounded by40000bytes; this is not a current topic capacity audit.

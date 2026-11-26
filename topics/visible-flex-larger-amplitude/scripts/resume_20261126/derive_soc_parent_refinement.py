#!/usr/bin/env python3
"""Pure complete-source recovery from immutable originals and exact text edits.

This reads only source text and a small plain JSON edit manifest. Each entire
base SHA and result SHA is fixed. All non-equal spans, including inserted text,
are present in the manifest; no scientific module is imported or evaluated.
The sibling unified diffs are for review, not a different reconstruction rule.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def derive(source, entry):
    text = Path(source).read_text()
    if digest(text) != entry['original_sha256']:
        raise ValueError('Changed whole original source: '+str(source))
    pieces = []
    current = 0
    for change in entry['edits']:
        start, end = change['start'], change['end']
        if (not current <= start <= end <= len(text)
                or text[start:end] != change['original_text']):
            raise ValueError('The exact immutable source edit does not match')
        pieces.extend((text[current:start], change['replacement_text']))
        current = end
    pieces.append(text[current:])
    result = ''.join(pieces)
    if digest(result) != entry['result_sha256']:
        raise ValueError('Recovered complete source differs from the locked result')
    if len(result.encode()) != entry['result_bytes']:
        raise ValueError('Recovered source byte count changed')
    ast.parse(result)
    compile(result, entry['result_file'], 'exec')
    if any(line.rstrip() != line for line in result.splitlines()):
        raise ValueError('No trailing whitespace')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-dir', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--edits', type=Path,
        default=Path(__file__).with_name('soc_parent_refinement_source_edits.json'))
    a = p.parse_args()
    document = json.loads(a.edits.read_text())
    if document.get('schema') != 'complete-SOC-parent-refinement-exact-text-edits-v1':
        raise ValueError('Need the complete exact plain-text recovery manifest')
    a.outdir.mkdir(parents=True, exist_ok=True)
    result = []
    for entry in document['files']:
        text = derive(a.source_dir/entry['original_file'], entry)
        path = a.outdir/entry['result_file']
        if path.exists() and path.read_text() != text:
            raise FileExistsError(path)
        path.write_text(text)
        result.append(dict(file=str(path), sha256=digest(text),
            bytes=len(text.encode()), scientific_execution=False))
    print(json.dumps(result))


if __name__ == '__main__':
    main()

#!/usr/bin/env node
// Complete source-text reconstruction only. Not a scientific admission step.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const PARENTS={
  "observer": {
    "name": "fixed_fejer_complete_geometry_trial_progress.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py",
    "bytes": 39500,
    "sha256": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
    "git_blob_sha": "8173d3576958dc5c476466dd4c5012c5ed81b0c1"
  },
  "followups": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_followups_with_active_progress.py",
    "bytes": 32762,
    "sha256": "046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314",
    "git_blob_sha": "d2c8ef87878d57525cfef04cfc401da7a9f30d6d"
  },
  "controller": {
    "bytes": 19984,
    "sha": "c1d51b6ad5e86e41c2afa826968581b41c2d485c",
    "sha256": "289fa6ad3d93ac4257509e31a79459ef25608379efb0ac67dcce84d76f8e8796",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel24_compact_metadata.py"
  }
};
const EXPECTED={
  "observer": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_location_progress.py",
    "bytes": 42637,
    "sha256": "4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94",
    "sha": "bad0be021443e7fa7a8fbfe4ee473f3e05ccadad",
    "git_blob_sha": "bad0be021443e7fa7a8fbfe4ee473f3e05ccadad"
  },
  "followups": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_followups_with_geometry_location_progress.py",
    "bytes": 32763,
    "sha256": "444f57b28c695fbcd0fbfc03237b8c7a56dedccc97a64873b7dae083de5dbb12",
    "sha": "4b72d0565d3f3fd797dd8bf45e48310cad8226d2",
    "git_blob_sha": "4b72d0565d3f3fd797dd8bf45e48310cad8226d2"
  },
  "controller": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel25_geometry_locations.py",
    "bytes": 19995,
    "sha256": "4bbac0cd1bb116205b4f94b8bc544e102bd522af9abb697327a8eb9b6f984562",
    "sha": "e792c8368fc4e0a4a50d693f9a836b44ae662f34",
    "git_blob_sha": "e792c8368fc4e0a4a50d693f9a836b44ae662f34"
  }
};
const TRANSFORMATIONS={
  "observer": [
    {
      "before": "SCHEMA = 'actual-complete-fejer-geometry-trial-scalar-progress-v1'",
      "after": "SCHEMA = 'actual-complete-fejer-geometry-location-scalar-progress-v1'",
      "count": 1
    },
    {
      "before": "BINDING_SCHEMA = 'actual-complete-fejer-own-point-scalar-observation-v1'",
      "after": "BINDING_SCHEMA = 'actual-complete-fejer-own-point-location-observation-v1'",
      "count": 1
    },
    {
      "before": "COMPLETED_TRIAL_SCHEMA = 'actual-complete-fejer-returned-trial-scalar-observation-v1'",
      "after": "COMPLETED_TRIAL_SCHEMA = 'actual-complete-fejer-returned-trial-location-observation-v1'",
      "count": 1
    },
    {
      "before": "MAX_FILE_BYTES = 16384",
      "after": "MAX_FILE_BYTES = 16384\nPROGRESS_FILE_BYTES = 32768",
      "count": 1
    },
    {
      "before": "        maximum_progress_file_bytes=MAX_FILE_BYTES,",
      "after": "        maximum_progress_file_bytes=PROGRESS_FILE_BYTES,\n        original_normal_capture_maximum_bytes=MAX_FILE_BYTES,\n        returned_locations='original finite worst curvature, farthest surface point and three amplitude maximizers; only cell/u/phi/branch/stage/angle/s words',\n        missing_location_coordinates_remain_null=True,\n        physical_piece_or_flex_time_inferred=False,\n        maximum_location_ties_not_enumerated=True,\n        farthest_surface_point_not_claimed_to_attain_whole_diameter=True,",
      "count": 1
    },
    {
      "before": "\ndef _geometry(value,point,*,source,model,driver,state):",
      "after": "\n\nLOCATION_KEYS = ('cell','u','phi','branch','stage','angle','s')\nLOCATION_FAMILIES = ('body_diameter','distance_plus','distance_minus')\n\n\ndef _returned_location(value):\n    # Only original returned scalar coordinates are copied. Missing s, stage,\n    # angle or branch is not reconstructed from another point or a new field.\n    if not isinstance(value,dict):\n        return None\n    return {key:_number(value.get(key)) for key in LOCATION_KEYS}\n\n\ndef _geometry_locations(value):\n    amplitude=value.get('amplitude')\n    amplitude=amplitude if isinstance(amplitude,dict) else {}\n    families=amplitude.get('worst_by_family')\n    families=families if isinstance(families,dict) else {}\n    result={}\n    for name in LOCATION_FAMILIES:\n        item=families.get(name)\n        item=item if isinstance(item,dict) else {}\n        result[name]=dict(location=_returned_location(item.get('location')),\n            physical_g=_number(item.get('physical_g')))\n    return dict(curvature=_returned_location(value.get('worst')),\n        farthest_surface=_returned_location(value.get('farthest')),amplitude=result)\n\n\ndef _validate_geometry_locations(item,raw=None):\n    locations=item.get('returned_locations')\n    if (not isinstance(locations,dict)\n            or set(locations)!=set(('curvature','farthest_surface','amplitude'))):\n        raise ValueError('Keep the three original returned-location categories')\n    families=locations.get('amplitude')\n    if not isinstance(families,dict) or set(families)!=set(LOCATION_FAMILIES):\n        raise ValueError('Keep each original finite amplitude extremum or null')\n    selected=[locations['curvature'],locations['farthest_surface']]\n    for name in LOCATION_FAMILIES:\n        value=families[name]\n        if (not isinstance(value,dict) or set(value)!=set(('location','physical_g'))\n                or value['physical_g'] is not None and _number(value['physical_g']) is None):\n            raise ValueError('A returned amplitude scalar is finite or explicitly unavailable')\n        selected.append(value['location'])\n    for value in selected:\n        if value is not None and (not isinstance(value,dict)\n                or set(value)!=set(LOCATION_KEYS)\n                or any(v is not None and _number(v) is None for v in value.values())):\n            raise ValueError('Keep only the original finite scalar location words or null')\n    if raw is not None and locations!=_geometry_locations(raw):\n        raise ValueError('Observed locations differ from the original returned geometry object')\n\n\ndef _geometry(value,point,*,source,model,driver,state):",
      "count": 1
    },
    {
      "before": "        raise ValueError('The six physical inequalities differ from their actual returned source')",
      "after": "        raise ValueError('The six physical inequalities differ from their actual returned source')\n    _validate_geometry_locations(item,raw)",
      "count": 1
    },
    {
      "before": "        current_height=_number(value.get('current_height')),\n        continuous_geometry_bound_claimed=False,accepted_or_final_inferred=False)",
      "after": "        current_height=_number(value.get('current_height')),\n        returned_locations=_geometry_locations(value),\n        continuous_geometry_bound_claimed=False,accepted_or_final_inferred=False)",
      "count": 1
    },
    {
      "before": "            if len(raw)>=MAX_FILE_BYTES:",
      "after": "            if len(raw)>=PROGRESS_FILE_BYTES:",
      "count": 2
    },
    {
      "before": "or type(record.get('bytes')) is not int or not 0<record['bytes']<MAX_FILE_BYTES",
      "after": "or type(record.get('bytes')) is not int or not 0<record['bytes']<PROGRESS_FILE_BYTES",
      "count": 1
    }
  ],
  "followups": [
    {
      "before": "PROGRESS_MAX_PUBLIC_BYTES = 8000",
      "after": "PROGRESS_MAX_PUBLIC_BYTES = 16384",
      "count": 1
    },
    {
      "before": "if selector_count > 48:",
      "after": "if selector_count > 64:",
      "count": 1
    },
    {
      "before": "Optional progress is limited to 48 explicit scalar fields",
      "after": "Optional progress is limited to 64 explicit scalar fields",
      "count": 1
    }
  ],
  "controller": [
    {
      "before": "visible-larger-parallel-24:start",
      "after": "visible-larger-parallel-25:start",
      "count": 1
    },
    {
      "before": "visible-larger-parallel-24:end",
      "after": "visible-larger-parallel-25:end",
      "count": 1
    },
    {
      "before": "Actions24：",
      "after": "Actions25：",
      "count": 1
    },
    {
      "before": "并行24规则核查：",
      "after": "并行25规则核查：",
      "count": 1
    },
    {
      "before": "scripts/resume_20261126/public_actions_followups_with_active_progress.py",
      "after": "scripts/resume_20261126/public_actions_followups_with_geometry_location_progress.py",
      "count": 1
    },
    {
      "before": "if len(rendered.encode('utf-8'))>=16000:",
      "after": "if len(rendered.encode('utf-8'))>=32768:",
      "count": 1
    }
  ]
};
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const blob=b=>crypto.createHash("sha1").update(Buffer.concat([Buffer.from("blob "+b.length+"\0"),b])).digest("hex");
function check(ok,message){if(!ok)throw Error(message);}
function identity(b,r){check(b.length===r.bytes&&sha(b)===r.sha256&&blob(b)===(r.git_blob_sha??r.sha),"Whole source identity: "+r.path);}
function apply(body,op){check(body.split(op.before).length-1===op.count,"Literal source count");return body.split(op.before).join(op.after);}
export function reproduce(parentBodies){
 const output={};
 for(const role of Object.keys(PARENTS)){
  const original=parentBodies[role];check(typeof original==="string","Complete parent text required");
  identity(Buffer.from(original,"utf8"),PARENTS[role]);
  let body=original;for(const op of TRANSFORMATIONS[role])body=apply(body,op);
  identity(Buffer.from(body,"utf8"),EXPECTED[role]);
  let inverse=body;for(const op of [...TRANSFORMATIONS[role]].reverse()){
   check(inverse.split(op.after).length-1===op.count,"Literal inverse count");
   inverse=inverse.split(op.after).join(op.before);
  }
  check(inverse===original,"Complete inverse text mismatch");output[role]=body;
 }
 return output;
}
function main(){
 const opts={};const args=process.argv.slice(2);
 for(let i=0;i<args.length;i+=2){check(["--source-root","--output-directory"].includes(args[i])&&typeof args[i+1]==="string"&&!(args[i] in opts),"Use the two complete directories");opts[args[i]]=args[i+1];}
 check(opts["--source-root"]&&opts["--output-directory"],"Both directories are required");
 const root=path.resolve(opts["--source-root"]),out=path.resolve(opts["--output-directory"]);
 check(root!==out,"Use a separate output directory");
 const input=Object.fromEntries(Object.entries(PARENTS).map(([role,r])=>[role,fs.readFileSync(path.join(root,r.path),"utf8")]));
 const output=reproduce(input);const records=[];
 for(const [role,body]of Object.entries(output)){const target=path.join(out,EXPECTED[role].path);fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,body,"utf8");records.push({role,...EXPECTED[role],output_path:target});}
 process.stdout.write(JSON.stringify({source_text_only:true,scientific_execution:false,independent_scientific_gate:false,complete_sources:records},null,2)+"\n");
}
if(process.argv[1]&&path.resolve(process.argv[1])===path.resolve(new URL(import.meta.url).pathname))main();

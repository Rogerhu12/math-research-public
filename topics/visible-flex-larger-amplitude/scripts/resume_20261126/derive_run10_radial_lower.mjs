// Complete literal source derivation only. This module does not import scientific Python.
import crypto from 'node:crypto';
const identity = text => ({bytes:Buffer.byteLength(text,'utf8'),sha256:crypto.createHash('sha256').update(text,'utf8').digest('hex')});
const same = (a,b) => a.bytes===b.bytes && a.sha256===b.sha256;
export const SPECS = [
 {
  "role": "closure_values",
  "parent": {
   "path": "scripts/resume_20261126/same_chain_detached_closure_values.py",
   "bytes": 54143,
   "sha256": "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e",
   "git_blob_sha": "efb44b6f7547129d3c069c46e026e2caf6803203"
  },
  "output": {
   "name": "run10_radial_detached_closure_values.py",
   "bytes": 54138,
   "sha256": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   }
  ]
 },
 {
  "role": "analytic_J3",
  "parent": {
   "path": "scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py",
   "bytes": 25725,
   "sha256": "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa",
   "git_blob_sha": "a5bd0c7e8734c30413dd08538ae20c72d8c37a3b"
  },
  "output": {
   "name": "run10_radial_analytic_stage_jacobian.py",
   "bytes": 25720,
   "sha256": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   },
   {
    "old": "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e",
    "new": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb",
    "count": 1
   }
  ]
 },
 {
  "role": "analytic_frame",
  "parent": {
   "path": "scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py",
   "bytes": 47272,
   "sha256": "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598",
   "git_blob_sha": "c040a321bc4384c2a2ea974eb4fb38c3ddfd6da1"
  },
  "output": {
   "name": "run10_radial_analytic_normal_frame.py",
   "bytes": 47267,
   "sha256": "945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   },
   {
    "old": "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e",
    "new": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb",
    "count": 1
   }
  ]
 },
 {
  "role": "frame_C1",
  "parent": {
   "path": "scripts/resume_20261126/normal_frame_c1_closure_values.py",
   "bytes": 37361,
   "sha256": "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa",
   "git_blob_sha": "8985fdc75ecf023939c2e983e4a057fed8fc86be"
  },
  "output": {
   "name": "run10_radial_normal_frame_c1.py",
   "bytes": 37361,
   "sha256": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e",
    "new": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb",
    "count": 1
   },
   {
    "old": "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa",
    "new": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b",
    "count": 1
   }
  ]
 },
 {
  "role": "stage_matrices",
  "parent": {
   "path": "scripts/resume_20261126/detached_stage_matrices_closure_values.py",
   "bytes": 47791,
   "sha256": "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45",
   "git_blob_sha": "da63d2c4752666fdd8f07e552d0125e972977cd3"
  },
  "output": {
   "name": "run10_radial_detached_stage_matrices.py",
   "bytes": 47791,
   "sha256": "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa",
    "new": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b",
    "count": 1
   },
   {
    "old": "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa",
    "new": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2",
    "count": 1
   }
  ]
 },
 {
  "role": "adjacent_matrices",
  "parent": {
   "path": "scripts/resume_20261126/adjacent_normal_matrices_closure_values.py",
   "bytes": 36766,
   "sha256": "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650",
   "git_blob_sha": "c7227964a254c6f62095b96cc767433ac75ff1f7"
  },
  "output": {
   "name": "run10_radial_adjacent_normal_matrices.py",
   "bytes": 36766,
   "sha256": "7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa",
    "new": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b",
    "count": 1
   },
   {
    "old": "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa",
    "new": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2",
    "count": 1
   },
   {
    "old": "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45",
    "new": "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9",
    "count": 1
   }
  ]
 },
 {
  "role": "reference_calibration",
  "parent": {
   "path": "scripts/resume_20261126/radial_refined_public_reference_calibration.py",
   "bytes": 12760,
   "sha256": "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178",
   "git_blob_sha": "a754b5812d4f9092e94cafe7407f3e0cd3a84246"
  },
  "output": {
   "name": "run10_radial_reference_calibration.py",
   "bytes": 12769,
   "sha256": "cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b"
  },
  "patches": [
   {
    "old": "complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   }
  ]
 },
 {
  "role": "endpoint",
  "parent": {
   "path": "scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py",
   "bytes": 98421,
   "sha256": "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4",
   "git_blob_sha": "93e28f0ef1571d9869519b91a6b051e60d1921ab"
  },
  "output": {
   "name": "so3_run10_radial_refined_closure_normal_lift.py",
   "bytes": 98434,
   "sha256": "ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c"
  },
  "patches": [
   {
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
    "count": 1
   },
   {
    "old": "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   },
   {
    "old": "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e",
    "new": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb",
    "count": 1
   },
   {
    "old": "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa",
    "new": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b",
    "count": 1
   },
   {
    "old": "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598",
    "new": "945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2",
    "count": 1
   },
   {
    "old": "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa",
    "new": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2",
    "count": 1
   },
   {
    "old": "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45",
    "new": "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9",
    "count": 1
   },
   {
    "old": "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650",
    "new": "7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37",
    "count": 1
   },
   {
    "old": "b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f",
    "new": "cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b",
    "count": 1
   },
   {
    "old": "supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1",
    "new": "radial-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1",
    "count": 1
   },
   {
    "old": "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7",
    "new": "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652",
    "count": 1
   },
   {
    "old": "complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1",
    "new": "complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1",
    "count": 1
   }
  ]
 },
 {
  "role": "root_packets",
  "parent": {
   "path": "scripts/resume_20261126/immutable_closure_values_normal_root_packets.py",
   "bytes": 70992,
   "sha256": "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805",
   "git_blob_sha": "598110c9548b29fd25a79d7e2acd6928f228db35"
  },
  "output": {
   "name": "immutable_run10_radial_normal_root_packets.py",
   "bytes": 71652,
   "sha256": "fa9f50d318af9ec268ce391b6ba16d8eb971d88ad519ae79c8ba3c661806f528"
  },
  "patches": [
   {
    "old": "SCHEMA = 'immutable-current-analytic-full-frame-normal-root-packets-v1'",
    "new": "SCHEMA = 'immutable-run10-radial-refined-detached-closure-normal-root-packets-v1'",
    "count": 1
   },
   {
    "old": "NORMALS = {\n",
    "new": "NORMALS = {\n    \"ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c\": {\"schema\":\"complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1\",\"base\":\"130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0\",\"adjacent\":\"7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37\",\"calibration\":\"cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b\",\"analytic\":\"7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b\",\"analytic_frame\":\"945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2\",\"closure_values\":\"61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb\"},\n",
    "count": 1
   }
  ]
 }
];

export function build(read) {
  const output=new Map();
  for(const spec of SPECS) {
    const parent=read(spec.parent.path);
    if(typeof parent!=='string'||!same(identity(parent),spec.parent))throw new Error('Whole construction parent differs: '+spec.parent.path);
    let value=parent;
    for(const patch of spec.patches) {
      const count=value.split(patch.old).length-1;
      if(count!==patch.count)throw new Error('Exact patch count differs: '+spec.output.name+' '+count+' != '+patch.count);
      value=value.split(patch.old).join(patch.new);
    }
    if(!same(identity(value),spec.output))throw new Error('Whole derived source differs: '+spec.output.name);
    if(spec.output.bytes>=100000)throw new Error('Complete source exceeds the integration ceiling');
    output.set(spec.output.name,value);
  }
  return output;
}

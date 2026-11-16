#!/usr/bin/env python3
"""Resume four complete weight-zero self/current contractions.

Read the ten pinned records of the interrupted public run. Its two Q-RHS
applications, current inverse and three self references are reused verbatim;
no Q inverse or member check is repeated. Restore only the still-unrestored
three static and eight response mixed roots. The prior 5.033211666999932
science seconds remain charged inside the same 180-second total ceiling.
Nonlocal/high-jet remainders stay exact; n2 is zero only on the proved mother
class. Only the reviewed public Actions entry may execute this module.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import literature_weight_zero_natural_flux as normal
import literature_complete_response_self_current as base

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
ENTRY = TOPIC + "/scripts/literature_weight_zero_complete_self_currents.py"
DESIGN = TOPIC + "/notes/weight-zero-complete-self-four-column-design-20261116.md"
WORKFLOW = ".github/workflows/visible-weight-zero-complete-self-currents.yml"
SCHEMA = "visible-flex-weight-zero-complete-self-four-currents-v1"
TARGET_ORDER = ("response_old8", "response_old9", "normal_XH", "normal_XY")
LIMITS = {
    "seconds": 180, "memory_mib": 1024, "nodes": 500000, "atoms": 60000,
    "terms": 80000, "word_calls": 500000, "cache_entries": 300000,
    "rational_bits": 8192, "monitored_rational_operations": 5000000,
    "mathematical_stdout_bytes": 2500000, "stdout_final_reserve_bytes": 131072,
    "original_log_read_bytes": 16777216, "network_json_bytes": 2097152,
    "network_timeout_seconds": 40,
}
DOMAIN = {
    "targets": list(TARGET_ORDER), "new_complete_self_currents": 4,
    "new_current_scalar_RHS": 4, "necessary_static_mixed_inputs": 3,
    "necessary_response_mixed_inputs": 8,
    "paid_Q_pivots_replayed": 0, "paid_current_pivot_sequence": 707,
    "prior_completed_Q_RHS_applications_reused": 2,
    "resume_only_after_exact_source_hashes_entry_failure": True,
    "old_member_checks_repeated": 0,
    "old_R316_R329_R443_logs_reread": 0,
    "old_pure_Q_Omega_current_rank_or_development_executions": 0,
    "new_profile_or_root_evaluations": 0, "new_development_suites": 0,
    "all_input_reads_and_restoration_in_one_science_clock": True,
    "whole_target_same_right_anchor": True,
    "XH_left_constant": "published_n2_not_universally_zero",
    "XH_left_constant_zero_domain": "the_same_published_four_constraint_affine_mother_library",
    "actual_joint_or_period_claimed": False,
    "nonzero_remainder_is_fixed_mother_nonmembership": False,
    "automatic_mirror_membership_or_rank_executed": False,
}
FROZEN = json.loads(r'''{
  "topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py": "bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94",
  "topics/visible-flex-new-mechanism/scripts/literature_endpoint_first_layer.py": "cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69",
  "topics/visible-flex-new-mechanism/scripts/literature_character_zero_pure_readout.py": "8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py": "337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4",
  "topics/visible-flex-new-mechanism/scripts/literature_color_priority_words.py": "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9",
  "topics/visible-flex-new-mechanism/scripts/literature_colored_profile_algebra.py": "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f",
  "topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_exact_membership.py": "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70",
  "topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_word_normal_form.py": "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_literal_relations.py": "80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_minus2.py": "fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11",
  "topics/visible-flex-new-mechanism/scripts/literature_range_profile_algebra.py": "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52",
  "topics/visible-flex-new-mechanism/scripts/literature_acceleration_layer_mixed.py": "271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c",
  "topics/visible-flex-new-mechanism/scripts/literature_constrained_static_fourth.py": "814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4",
  "topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py": "331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5",
  "topics/visible-flex-new-mechanism/scripts/literature_local_fourth_derivative_factors.py": "02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf",
  "topics/visible-flex-new-mechanism/scripts/literature_full_m8_tail_response_projection.py": "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345",
  "topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py": "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0",
  "topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py": "0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477",
  "topics/visible-flex-new-mechanism/scripts/literature_c7_transverse_tail_probe.py": "98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b",
  "topics/visible-flex-new-mechanism/scripts/literature_full_phase_rational_dual.py": "bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f",
  "topics/visible-flex-new-mechanism/scripts/literature_total_P1_scaling_blocks.py": "40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa",
  "topics/visible-flex-new-mechanism/scripts/literature_closed_c1_endpoint.py": "b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1",
  "topics/visible-flex-new-mechanism/scripts/literature_full_phase_bridge_exact.py": "d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e",
  "topics/visible-flex-new-mechanism/scripts/literature_local_third_bridge_decompose.py": "08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0",
  "topics/visible-flex-new-mechanism/scripts/literature_G_translation_successor.py": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406",
  "topics/visible-flex-new-mechanism/scripts/literature_h_axis_sharp_coefficient.py": "7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b",
  "topics/visible-flex-new-mechanism/scripts/literature_rational_volterra_polynomial.py": "6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22",
  "topics/visible-flex-new-mechanism/scripts/literature_linear_third_bridge_quotient.py": "0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2",
  "topics/visible-flex-new-mechanism/scripts/literature_full_self_euler_coordinates.py": "95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba",
  "topics/visible-flex-new-mechanism/scripts/literature_weight_zero_complete_self.py": "9347caeb4ff7ed54cc88f6c38183d4773d8e12125a5a9631412674550d42b78f",
  "topics/visible-flex-new-mechanism/scripts/literature_weight_zero_joint_self_completion.py": "1f5d671598ca6fc4a804c6f22a65d145b5ced3743506a2144d507717ff4789d3",
  "topics/visible-flex-new-mechanism/scripts/literature_weight_zero_natural_flux.py": "be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f",
  "topics/visible-flex-new-mechanism/scripts/read_original_actions_log.py": "b7b16d0917bf99e4183421ab6d5c1dd33b9c0fe8009ad59a5141a17d798e5c4a",
  "topics/visible-flex-new-mechanism/scripts/literature_complete_response_self_current.py": "18d5578869860f9da52d31137352f6a503a27610eab5e133b9a1c0f9ca85e8f5"
}''')
NORMALS = {
    2: ((0,2,0,0), "b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f"),
    4: ((0,4,0,0), "1d67672bb734f602675f84768b8afd62363d3742ca203ea01b23c9b1f3f0b592"),
    6: ((1,1,1,0), "5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02"),
}
RESPONSE_LABELS = {
    0: ("p0",7), 2: ("p1",1), 3: ("p1",12), 4: ("p1",16),
    5: ("p1",35), 7: ("p2",6), 8: ("p2",11), 9: ("p2",14),
}
TARGETS = {
    "response_old8": {"normal": {}, "response": {0:"-2",2:"5",3:"-1",8:"1"},
        "mixed_sha256": "61e1f2fa80e31b7605d246da44226cf02c5a82d727284e8e9eba5a185458d351"},
    "response_old9": {"normal": {}, "response": {2:"6",3:"-8/3",9:"1"},
        "mixed_sha256": "cc177b7d2dd879b43ed58fcb8f2810344c58b648003ecb10a91681dcc53adb98"},
    "normal_XH": {"normal": {2:"1",4:"1"},
        "response": {2:"31/32",3:"-3/128",4:"31/64",5:"-39/32",9:"27/128"}},
    "normal_XY": {"normal": {4:"1",6:"-1"},
        "response": {2:"35/256",3:"-3/1024",4:"35/512",5:"-39/256",7:"-1/64",9:"27/1024"}},
}
R316 = {
    "run_id":43735872441, "job_id":132878270740,
    "source_commit":"ca186db057ed753abe565d0c3c2c8305278b5af7",
    "log_bytes":182877, "log_sha256":"4d658489abd694f9f4cde2204aec9d23dc507d9ebae47168e42123cf4ff1288f",
    "report_tag":"COMPLETE_REPORT", "report_bytes":61441,
    "report_sha256":"731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd",
}
R329 = {
    "run_id":43740129876, "job_id":132891272196,
    "source_commit":"a5383f62d353890cc24e927b669dd2d6b67f8c78",
    "log_bytes":136609, "log_sha256":"6808d07a3ed6b20d503691de9c979ab5accd9526f52861906c4196ff53d49758",
    "report_tag":"COMPLETE_REPORT", "report_bytes":37516,
    "report_sha256":"d4c5709c150392118ea0189be0f2114e52e9511df12d90f139836cace3863ca3",
}
R434 = {
    "run_id":43796872698, "job_id":133067569306,
    "source_commit":"563defb46bc785295265c3f48fcad3fc8897c617",
    "log_bytes":1322512, "log_sha256":"1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1",
    "report_tag":"COMPLETE_CURRENT_Q_REPORT", "report_bytes":15639,
    "report_sha256":"c4b4031bddacca0c84050c7efdf8b43f80e7553553305d55dd52637f96af292d",
    "record_tag":"CURRENT_Q_RECORD", "records":1020, "record_file_bytes":1170464,
    "record_file_sha256":"dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7",
    "record_chain_sha256":"673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101",
    "request_path":TOPIC+"/computations/request-complete-response-self-current.json",
    "request_bytes":9269, "request_sha256":"fd6e8526d6f7e9492911848b17a852d64a31654513a267ba61e5bdb9390ffb01",
}
R443 = {
    "run_id":43801705436, "job_id":133083261189,
    "source_commit":"9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac",
    "log_bytes":421834, "log_sha256":"d4a266bb80006a56918f21600ecce75ade0b7522ddbfc45459f89958f5b2c1e8",
    "report_tag":"COMPLETE_SELF_KERNEL_REPORT", "report_bytes":17727,
    "report_sha256":"070de2b03125ef6a3be251919dc99ecc736b47a00261708cea0727e5c7d36dc4",
    "record_tag":"SELF_KERNEL_RECORD", "records":249, "record_file_bytes":299732,
    "record_file_sha256":"1ea691a9cb902e6be7bdbf09b892c3f39d665dbd45174a309be7445686611ca8",
    "record_chain_sha256":"6565a3135f586abdbeda18ae58dae8b156e820d81e1f448e1afa0f5339a190c5",
    "request_path":TOPIC+"/computations/request-joint-kernel-complete-self.json",
    "request_bytes":11809, "request_sha256":"f3523f5ee89d820150e52e22c54afd25d5d7deb79fa8adc0d5cbefc7496f4532",
}
PAID = {"R316":R316, "R329":R329, "R434":R434, "R443":R443}
CURRENT_SHA = "729055c2e1075378e3ac5e771e24a6dd4ca824c8c4aa9fab800dd25eb7614e6b"
SELF_REFERENCE_SHA = {
    108:"2555840e1e7d5dab56751e026984ec5d5ae54dc33db4f6ac542e356f6286bbcd",
    109:"f1421e2361d2c9258b3a873385d5662d5e358f4646f99bb342158de59d5c3475",
    119:"8c5baa6b1a6ab8b6c0c691b8ce1a319d82796d1510a0e69f039a12614f681a0c",
}

RESUME = json.loads(r'''{
  "run_id": 43818340099,
  "job_id": 133135408458,
  "source_commit": "821f98de378edfbbf7f6c2b7eb71b0e0782f3e01",
  "log_bytes": 132117,
  "log_sha256": "122f5e0ec8fbb51b3fefce65f6d357fada8bf34ed96d109497f8025e5cdda0b5",
  "report_tag": "COMPLETE_WEIGHT_ZERO_SELF_REPORT",
  "report_bytes": 13440,
  "report_sha256": "a89823532d7aae5d27cfc017c507ca07eca50e6d0caa76a6ad125539c41c38e8",
  "clock_tag": "FINAL_CLOCK",
  "clock_bytes": 692,
  "clock_sha256": "c49200bfe5414ab0ded0bb13adfa2782d15913296833e96928928446af6d6e0f",
  "record_tag": "WEIGHT_ZERO_SELF_RECORD",
  "records": 10,
  "record_file_bytes": 34703,
  "record_file_sha256": "9b89af9b2667919157db4f194cd7a8203fea667568f0f2fe799353758f6644aa",
  "record_chain_sha256": "26638547061388c9c73e05fb030b926f791a272af38a43305f1a2aae848888db",
  "request_bytes": 20871,
  "request_sha256": "5d4ee23e1e1aea80d2cf8cd6b1061ef0ed55f6023d6e3b3b2491d0dbc0b30fb4",
  "prior_science_seconds": 5.033211666999932,
  "prior_pre_science_entry_seconds": 0.005253693000000226,
  "prior_monitored_rational_operations": 2910,
  "prior_maximum_monitored_rational_bits": 30,
  "prior_limit_check_calls": 4579,
  "prior_peak_RSS_KiB": 52868,
  "prior_network": {
    "bytes": 2149732,
    "redirects": 4,
    "requests": 18
  },
  "prior_mathematical_stdout_bytes": 49120,
  "source_entry_sha256": "7f992c389661d731cbb873e42c7ddab84f37ad3a521b8128cfcfb338a9bdb412",
  "record_identities": [
    {
      "sequence": 1,
      "kind": "science.paid_input_identity",
      "payload_bytes": 8217,
      "payload_sha256": "3729cea09f7b0cfd4c6fe77d0906b6c1ea465adf34cdcfde7571bff8a8eee495"
    },
    {
      "sequence": 2,
      "kind": "science.paid_input_identity",
      "payload_bytes": 8394,
      "payload_sha256": "3e024e19a3da85a73dd5a1a0562485da27cb486e95967945df632dfb7128316c"
    },
    {
      "sequence": 3,
      "kind": "science.paid_input_identity",
      "payload_bytes": 2897,
      "payload_sha256": "828311602a7e73481aa0e2ff4b83537dff9f33036ba78a370772c7aed42585d8"
    },
    {
      "sequence": 4,
      "kind": "science.paid_input_identity",
      "payload_bytes": 3071,
      "payload_sha256": "dabc343078da669eff413fc0c0b788d8ead92c5a95812e69a80586b7fad4067d"
    },
    {
      "sequence": 5,
      "kind": "science.new_RHS_paid_Q_right_inverse",
      "payload_bytes": 1345,
      "payload_sha256": "0e9c85564edf024a0b60832f1f3f02760c497b9f771a76d7e59a22cc3a6c62cc"
    },
    {
      "sequence": 6,
      "kind": "science.new_RHS_paid_Q_right_inverse",
      "payload_bytes": 1426,
      "payload_sha256": "44868dd3f03a87dbf1ade0f95c7760876c9e0cdfbded00f79361fd66d6dc0d41"
    },
    {
      "sequence": 7,
      "kind": "science.paid_unique_current_right_inverse",
      "payload_bytes": 476,
      "payload_sha256": "d77e739f7ee6be31408074eab6dcb1c16334838f5b746e4c0ee6a5879cc73a57"
    },
    {
      "sequence": 8,
      "kind": "science.paid_reference_complete_self",
      "payload_bytes": 3188,
      "payload_sha256": "8d170ce8678d03f8359d7d6e95c2374a832bfe2acde80652ed1cbc6ced3e3ce0"
    },
    {
      "sequence": 9,
      "kind": "science.paid_reference_complete_self",
      "payload_bytes": 3170,
      "payload_sha256": "2c06b36c75b304a7c581845c804e2b2de9b9e9fed0063093656114c728f1be65"
    },
    {
      "sequence": 10,
      "kind": "science.paid_reference_complete_self",
      "payload_bytes": 781,
      "payload_sha256": "e3d29cd3499860ad7d9f88a3d41ffc1f6a24e47defc8f3d70619eaf817d14c43"
    }
  ],
  "R434_operator_records": [
    {
      "sequence": 7,
      "kind": "science.original_operator",
      "payload_bytes": 517,
      "payload_sha256": "9aa5cef71c5ebcb81edc3abe57e44007c9e0f176e311ffbb4338e267d403de3b",
      "label": "H4"
    },
    {
      "sequence": 8,
      "kind": "science.original_operator",
      "payload_bytes": 564,
      "payload_sha256": "62524bd40f2c4089af142e7049a68305bd081365a5e77beb01e4876f3669cba3",
      "label": "H5"
    },
    {
      "sequence": 9,
      "kind": "science.original_operator",
      "payload_bytes": 589,
      "payload_sha256": "12e5be5f26a14e0ea188edd9e2582d89ad3874d80762d8a5650aad74f73113ad",
      "label": "H6"
    },
    {
      "sequence": 12,
      "kind": "science.original_operator",
      "payload_bytes": 323,
      "payload_sha256": "bf37a664a79ece085f3bcef78b4b67800f270ab5c39b079a350d6d0c9866b891",
      "label": "J2"
    },
    {
      "sequence": 17,
      "kind": "science.original_operator",
      "payload_bytes": 440,
      "payload_sha256": "369162dd19f79b72fad5dc02c07f177179170e9e0cfeb4066b05a94df10a9ead",
      "label": "chi40"
    },
    {
      "sequence": 19,
      "kind": "science.original_operator",
      "payload_bytes": 438,
      "payload_sha256": "ed03b0d14f07c58c88757364b04e0c25bc7c22f172750d0cf46986fed7141125",
      "label": "chi104"
    }
  ]
}''')

canonical, sha = base.canonical, base.sha

class InputFailure(Exception):
    pass

def require(test, message):
    if not test:
        raise InputFailure(message)

def freeze(value):
    return tuple(freeze(x) for x in value) if isinstance(value,list) else value

def validate(request, repo):
    require(request.get("schema")==SCHEMA and request.get("repository")==REPOSITORY
            and request.get("entry_point")==ENTRY and request.get("domain")==DOMAIN
            and request.get("limits")==LIMITS and request.get("paid_inputs")==PAID
            and request.get("resume")==RESUME,
            "reviewed four-target request, limits or original identities changed")
    required=set(FROZEN)|{ENTRY,DESIGN,WORKFLOW}
    manifest=request.get("source_manifest",[])
    require(len(manifest)==len(required) and {r.get("path") for r in manifest}==required,
            "complete source manifest changed")
    identities=[]
    for row in sorted(manifest,key=lambda r:r["path"]):
        path=(repo/row["path"]).resolve()
        require(repo in path.parents and path.is_file(),"source path outside checkout or absent")
        raw=path.read_bytes()
        got={"path":row["path"],"bytes":len(raw),"sha256":sha(raw)}
        require(got==row,"bound source bytes/hash changed: "+row["path"])
        require(row["path"] not in FROZEN or row["sha256"]==FROZEN[row["path"]],
                "paid source changed: "+row["path"])
        identities.append(got)
    require(request.get("source_sha256")=={r["path"]:r["sha256"] for r in identities},
            "workflow and entry source binding differ")
    return identities

class Journal:
    def __init__(self,path):
        self.path=path
        self.file=path.open("wb")
        self.file_digest,self.chain=hashlib.sha256(),hashlib.sha256()
        self.sequence=self.file_bytes=self.stdout_bytes=0
        self.inherited_stdout_bytes=RESUME["prior_mathematical_stdout_bytes"]
        self.by_kind={}
        self.last_record=None
        self.unemitted=[]
    def record(self,kind,payload):
        raw=canonical(payload)
        self.sequence+=1
        identity={"sequence":self.sequence,"kind":kind,"payload_bytes":len(raw),"payload_sha256":sha(raw)}
        envelope={**identity,"payload":payload}
        encoded=canonical(envelope)+b"\n"
        self.file.write(encoded); self.file.flush()
        self.file_digest.update(encoded); self.file_bytes+=len(encoded)
        self.chain.update(canonical(identity)+b"\n")
        self.by_kind[kind]=self.by_kind.get(kind,0)+1
        self.last_record=identity
        line=b"WEIGHT_ZERO_SELF_RECORD "+encoded
        if self.inherited_stdout_bytes+self.stdout_bytes+len(line)>LIMITS["mathematical_stdout_bytes"]-LIMITS["stdout_final_reserve_bytes"]:
            self.unemitted.append(identity)
            raise base.OutputBudgetExceeded("completed exact record exceeds remaining stdout allowance")
        self.stdout_bytes+=len(line)
        sys.stdout.buffer.write(line); sys.stdout.buffer.flush()
        return identity
    def receipt(self):
        return {
            "completed_record_count":self.sequence,"record_counts":dict(self.by_kind),
            "record_identity_chain_sha256":self.chain.hexdigest(),
            "temporary_record_file_bytes":self.file_bytes,
            "temporary_record_file_sha256":self.file_digest.hexdigest(),
            "mathematical_record_stdout_bytes":self.stdout_bytes,
            "prior_mathematical_stdout_bytes":self.inherited_stdout_bytes,
            "cumulative_prior_and_current_record_stdout_bytes":self.inherited_stdout_bytes+self.stdout_bytes,
            "reserved_final_stdout_bytes":LIMITS["stdout_final_reserve_bytes"],
            "last_completed_record":self.last_record,
            "completed_but_not_emitted_records":list(self.unemitted),
            "machine_payload_committed_uploaded_or_blobbed":False,
        }

class Reader:
    def __init__(self,budget,deadline):
        self.budget=budget
        self.started=time.perf_counter()
        self.deadline=deadline
        self.redirects=0
        self.requests=0
        self.bytes=0
        self.opener=urllib.request.build_opener(normal.paid.NoRedirect())
        self.token=os.environ.get("GITHUB_TOKEN","")
        require(bool(self.token),"a read-only Actions token is required")
    def get(self,path,cap=None,accept="application/vnd.github+json"):
        self.budget.check()
        require(path.startswith("/repos/"+REPOSITORY+"/"),"unexpected public input API path")
        url="https://api.github.com"+path
        authenticated=True
        cap=cap or LIMITS["network_json_bytes"]
        for attempt in range(4):
            self.budget.check()
            remaining=self.deadline-time.perf_counter()
            if remaining<=0:
                self.budget.check()
                raise base.exact.formal.CompilationBudgetExceeded("one total scientific clock expired")
            parsed=urllib.parse.urlsplit(url)
            require(parsed.scheme=="https" and parsed.hostname and not parsed.username and not parsed.password,
                    "input redirect must be credential-free HTTPS")
            headers={"User-Agent":"visible-four-self-paid-reader","Accept-Encoding":"identity"}
            if authenticated:
                require(parsed.hostname=="api.github.com","API credential host mismatch")
                headers.update({"Accept":accept,"Authorization":"Bearer "+self.token,
                                "X-GitHub-Api-Version":"2022-11-28"})
            request=urllib.request.Request(url,headers=headers,method="GET")
            self.requests+=1
            try:
                response=self.opener.open(request,timeout=min(LIMITS["network_timeout_seconds"],remaining))
            except urllib.error.HTTPError as exc:
                status=exc.code
                location=exc.headers.get("Location")
                exc.close()
                if status not in (301,302,303,307,308) or not location:
                    raise InputFailure("paid public GET failed with HTTP "+str(status)) from None
                self.redirects+=1
                url=urllib.parse.urljoin(url,location)
                authenticated=False
                continue
            except (urllib.error.URLError,TimeoutError):
                raise InputFailure("paid public GET failed; credentials and signed URL omitted") from None
            with response:
                raw=response.read(cap+1)
            self.bytes+=len(raw)
            self.budget.check()
            require(len(raw)<=cap,"paid original input byte cap exceeded")
            return raw
        raise InputFailure("paid original input exceeded finite redirects")
    def json(self,path):
        return normal.paid.decode_json(self.get(path))

def coefficient_rows(values):
    return [[list(key) if isinstance(key,tuple) else key,str(value)]
            for key,value in sorted(values.items()) if value]

def combination(rows):
    return {tuple(label):F(value) for label,value in rows if F(value)}

def add_vector(out, other, coefficient, budget):
    for key,value in other.items():
        base.add(out,key,coefficient*value,budget)

def bound_log(spec, reader, conclusion):
    prefix="/repos/"+REPOSITORY
    run=reader.json(prefix+"/actions/runs/"+str(spec["run_id"]))
    job=reader.json(prefix+"/actions/jobs/"+str(spec["job_id"]))
    require(run.get("id")==spec["run_id"] and job.get("id")==spec["job_id"]
            and job.get("run_id")==spec["run_id"] and run.get("head_sha")==spec["source_commit"]
            and (not job.get("head_sha") or job["head_sha"]==spec["source_commit"])
            and run.get("status")==job.get("status")=="completed"
            and run.get("conclusion")==job.get("conclusion")==conclusion,
            "the bound prior run/job/source/conclusion changed")
    raw=reader.get(prefix+"/actions/jobs/"+str(spec["job_id"])+"/logs",
                   LIMITS["original_log_read_bytes"])
    require((len(raw),sha(raw))==(spec["log_bytes"],spec["log_sha256"]),
            "the bound complete prior log bytes/hash changed")
    return raw,run,job

def resume_paid_interfaces(reader, progress):
    """Decode the ten paid records; do not replay Q or old member checks."""
    spec=RESUME
    raw,run,job=bound_log(spec,reader,"failure")
    records={}; record_hash=hashlib.sha256(); chain=hashlib.sha256(); record_bytes=0
    selected=[]; clocks=[]
    wanted={r["sequence"]:r for r in spec["record_identities"]}
    for raw_line in raw.decode("utf-8-sig").splitlines():
        line=normal.paid.ANSI.sub("",raw_line).lstrip("\ufeff")
        marker=spec["record_tag"]+" "
        if marker in line:
            rec=normal.paid.decode_json(line.split(marker,1)[1])
            require(set(rec)=={"sequence","kind","payload_bytes","payload_sha256","payload"},
                    "paid resume record envelope changed")
            sequence=rec["sequence"]
            require(sequence==len(records)+1 and sequence in wanted,
                    "paid resume record sequence changed")
            identity={k:rec[k] for k in ("sequence","kind","payload_bytes","payload_sha256")}
            require(identity==wanted[sequence],"paid resume record identity changed")
            payload=canonical(rec["payload"])
            require((len(payload),sha(payload))==(rec["payload_bytes"],rec["payload_sha256"]),
                    "paid resume payload bytes/hash changed")
            encoded=canonical(rec)+b"\n"
            record_hash.update(encoded); record_bytes+=len(encoded)
            chain.update(canonical(identity)+b"\n")
            records[sequence]=rec
        for tag,dest,bytekey,hashkey in (
                (spec["report_tag"],selected,"report_bytes","report_sha256"),
                (spec["clock_tag"],clocks,"clock_bytes","clock_sha256")):
            marker=tag+" "
            if marker in line:
                payload=line.split(marker,1)[1].encode("utf-8")+b"\n"
                if (len(payload),sha(payload))==(spec[bytekey],spec[hashkey]):
                    dest.append(normal.paid.decode_json(payload))
        reader.budget.check()
    require(len(records)==spec["records"] and record_bytes==spec["record_file_bytes"]
            and record_hash.hexdigest()==spec["record_file_sha256"]
            and chain.hexdigest()==spec["record_chain_sha256"],
            "paid resume complete record file/chain changed")
    require(len(selected)==len(clocks)==1,"one exact prior main report and final clock required")
    old,clock=selected[0],clocks[0]
    require(old.get("schema")==SCHEMA and old.get("repository")==REPOSITORY
            and str(old.get("run_id"))==str(spec["run_id"])
            and old.get("workflow_source")==spec["source_commit"]
            and old.get("source_binding_complete") is True
            and old.get("entry_outcome")=="entry_error"
            and old.get("entry_error")=={"type":"KeyError","message":"'source_hashes'"}
            and old.get("request")=={"bytes":spec["request_bytes"],"sha256":spec["request_sha256"]},
            "the exact failed entry identity/stopping point changed")
    oldscience=old["science"]
    require(oldscience.get("active_stage")=="restore_only_three_static_and_eight_response_mixed_inputs"
            and oldscience.get("completed_units")==
                {"paid_original_log_reads":4,"new_Q_RHS_paid_inverse_applications":2}
            and oldscience.get("profile_atoms")==0
            and oldscience.get("shared_mapper_usage",{}).get("primitive_calls")==0
            and oldscience.get("shared_mapper_usage",{}).get("cache_entries")==0,
            "resume would skip science not completed at the pinned stopping point")
    require(clock.get("unified_science_started") is True
            and clock.get("workflow_source")==spec["source_commit"]
            and str(clock.get("run_id"))==str(spec["run_id"])
            and clock.get("all_science_and_main_output_elapsed_seconds")==spec["prior_science_seconds"]
            and clock.get("no_further_science") is True,
            "the authoritative prior clock changed")
    for field in ("monitored_rational_operations","maximum_monitored_rational_bits","limit_check_calls"):
        require(oldscience.get(field)==spec["prior_"+field],"prior charged count changed")
    require(oldscience.get("network")==spec["prior_network"]
            and old.get("peak_RSS_KiB")==spec["prior_peak_RSS_KiB"],
            "prior charged network or memory receipt changed")
    manifests={r["path"]:r for r in old["source_manifest"]}
    require(manifests.get(ENTRY,{}).get("sha256")==spec["source_entry_sha256"]
            and all(manifests.get(path,{}).get("sha256")==digest for path,digest in FROZEN.items()),
            "the paid resume ran a different source closure")
    for index,name in enumerate(("R316","R329","R434","R443"),1):
        identity=records[index]["payload"]
        require(identity["name"]==name and identity["original"]==PAID[name]
                and identity["old_science_or_development_executed"]==0,
                "paid ancestral input binding changed")
    progress.data["prior_completed_units"]=oldscience["completed_units"]
    progress.data["prior_science_receipt"]=oldscience
    progress.data["prior_final_clock"]=clock
    progress.data["prior_pre_science_entry_seconds"]=spec["prior_pre_science_entry_seconds"]
    progress.data["resume_entry_failure_repaired_only"]={
        "original_missing_container":"source_hashes.frozen_inputs_and_helpers",
        "replacement":"normal.head.source_identity()",
        "old_bound_source_validation_removed":False,
    }
    progress.record("paid_resume_identity",{
        "run_id":spec["run_id"],"job_id":spec["job_id"],"source_commit":spec["source_commit"],
        "log_bytes":spec["log_bytes"],"log_sha256":spec["log_sha256"],
        "record_identity_chain_sha256":spec["record_chain_sha256"],
        "complete_record_identities":spec["record_identities"],
        "prior_final_clock":clock,"prior_entry_error":old["entry_error"],
        "prior_complete_science_receipt":oldscience,
        "prior_pre_science_entry_seconds":spec["prior_pre_science_entry_seconds"],
        "old_R316_R329_R443_logs_reopened":0,"old_member_receipts_rechecked":0,
        "paid_Q_inverse_reapplied":0,"new_science_skipped":0,
    })
    corrections={"normal_XH":{},"normal_XY":{}}
    for sequence,name in ((5,"response_old8"),(6,"response_old9")):
        payload=records[sequence]["payload"]
        require(payload["target"]==name and payload["complete_Q_residual"]==[],
                "paid Q correction is not complete")
        corrections[name]=combination(payload["subtract_original_Z_cost_combination"])
        progress.record("resumed_paid_Q_correction",{
            "target":name,"original_run_id":spec["run_id"],"original_sequence":sequence,
            "original_payload_sha256":records[sequence]["payload_sha256"],
            "subtract_original_Z_cost_combination":payload["subtract_original_Z_cost_combination"],
            "complete_Q_residual":payload["complete_Q_residual"],
            "paid_Q_inverse_reapplied":0,
        })
    pivot=records[7]["payload"]
    require(pivot["original_sequence"]==707 and pivot["original_payload_sha256"]==CURRENT_SHA
            and pivot["original_complete_current_coordinates"]==[[15,"-2"],[27,"1"]],
            "paid current correction binding changed")
    zc=combination(pivot["original_Z_cost_combination"])
    progress.record("resumed_paid_unique_current_right_inverse",{
        "original_run_id":spec["run_id"],"original_sequence":7,
        "original_payload_sha256":records[7]["payload_sha256"],"original_payload":pivot,
        "old_current_or_Q_executions":0,
    })
    for sequence,reference in ((8,108),(9,109),(10,119)):
        payload=records[sequence]["payload"]
        require(payload["original_sequence"]==reference
                and payload["original_payload_sha256"]==SELF_REFERENCE_SHA[reference],
                "paid self-reference recovery changed")
        progress.record("paid_reference_complete_self",payload)
    needed={label[1] for corr in corrections.values() for label in corr}|{label[1] for label in zc}
    require(needed=={r["label"] for r in spec["R434_operator_records"]},
            "resume has changed its six original operator needs")
    progress.unit("paid_resume_log_reads",spec["job_id"])
    return corrections,zc,needed

def read_paid_operator_rows(reader,progress,needed):
    """Only six original a/b/c records; no old Q/current/membership readback."""
    raw,run,job=bound_log(R434,reader,"success")
    wanted={r["sequence"]:r for r in RESUME["R434_operator_records"]}
    result={}
    marker=R434["record_tag"]+" "
    for raw_line in raw.decode("utf-8-sig").splitlines():
        line=normal.paid.ANSI.sub("",raw_line).lstrip("\ufeff")
        if marker not in line:
            reader.budget.check()
            continue
        rec=normal.paid.decode_json(line.split(marker,1)[1])
        sequence=rec.get("sequence")
        if sequence in wanted:
            pin=wanted[sequence]
            require(rec.get("kind")==pin["kind"] and rec.get("payload_bytes")==pin["payload_bytes"]
                    and rec.get("payload_sha256")==pin["payload_sha256"],
                    "paid operator record identity changed")
            encoded=canonical(rec["payload"])
            require((len(encoded),sha(encoded))==(pin["payload_bytes"],pin["payload_sha256"])
                    and rec["payload"]["label"]==pin["label"]
                    and pin["label"] not in result,
                    "paid operator payload bytes/hash/label changed")
            result[pin["label"]]=rec["payload"]
            progress.record("resumed_original_operator_input",{
                "original_run_id":R434["run_id"],"original_job_id":R434["job_id"],
                "original_record_identity":pin,"original_payload":rec["payload"],
                "original_operator_regenerated":False,
            })
        reader.budget.check()
    require(set(result)==needed,"not all six required paid operator inputs were recovered")
    progress.unit("paid_operator_only_log_reads",R434["job_id"])
    return result

def restore_original_inputs(ring,repository,progress):
    """Restore only the three new-target static inputs and eight old responses."""
    # The original binder compares the producer against this FULL frozen tree.
    # An empty source_hashes mapping would fail at frozen_inputs_and_helpers.
    receipt={"inputs":{},"source_hashes":normal.head.source_identity()}
    labels=normal.zero.read_R0_definition(
        normal.safe_path(repository,TOPIC+"/notes/actions-43649525432-1-g_first_translation"),receipt)
    all_labels=dict(zip(normal.zero.R0_KEEP,labels))
    selected={}
    for old,(quadratic,third) in sorted(RESPONSE_LABELS.items()):
        row=all_labels[old]
        require(row["quadratic_name"]==quadratic and row["third_index"]==third,
                "published R126 old label changed: "+str(old))
        selected[old]=row
    _,data=normal.head.bind_input("static",
        normal.safe_path(repository,TOPIC+"/notes/actions-43645177423-1-local_fourth_quotient"),receipt)
    records=data["local_roots"]
    require(Counter(row["mode"] for row in records)==Counter({-4:197,-2:197}),
            "the paid full static source coverage changed")
    rows=[row for row in records if row["mode"]==-2]
    states=[]
    for row in rows:
        state,jets=normal.head.split_key(row["geometry_key"])
        require(not any(jets),"static original source has unexpected geometry derivatives")
        states.append(state)
    require(len(set(states))==197,"duplicate original static state")
    coordinates,reference=normal.head.constrained.reference_coordinates()
    require(sha(canonical(reference))==normal.GAMMA_SHA,"the original Gamma reference changed")
    weights=normal.pure.combine_normalization_rows(rows,states,coordinates,
        {i:spec[0] for i,spec in NORMALS.items()},normal.head.constrained.BASIS_STATES)
    needed_W=sorted({row["third_index"] for row in selected.values()})
    names=set().union(*(set(row) for row in weights.values()))
    names.update("W"+str(i) for i in needed_W)
    roots=normal.head.subset_decode(ring,data,names)
    del data
    progress.record("original_source_payload_identity",{
        "old_input_binding":receipt,"Gamma_reference_sha256":normal.GAMMA_SHA,
        "decoded_original_root_names":sorted(names),
        "raw_roots_are_existing_paid_original_roots":True,
        "old_forcing_or_pure_recompiled":False,
    })
    grade=normal.prior.blocks.ScalingGrading(ring)
    statics={}
    for index,(state,expected) in sorted(NORMALS.items()):
        progress.data["active_input"]={"kind":"needed_static_mixed_restore","normal_index":index}
        raw=sum((amount*roots[name] for name,amount in sorted(weights[index].items())),ring.number(0))
        value=grade.project(raw,0)
        require(ring.digest(value)==expected,"same-Gamma C%d mixed root differs from the paid source"%index)
        statics[index]=value
        progress.unit("needed_static_mixed_inputs_restored",index)
        progress.record("needed_static_mixed_input",{
            "normal_index":index,"state_h_k_omega_logh":list(state),"mode":-2,"true_weight":0,
            "original_mixed_sha256":ring.digest(value),"terms":len(value.terms),
            "original_static_combination":[[name,str(v)] for name,v in sorted(weights[index].items())],
            "raw_combination_sha256":ring.digest(raw),"complete_N0_and_Gamma_retained":True,
        })
        ring.limits.check()
    quadratics=normal.exact.operator_basis(ring)
    responses={}
    for old,row in sorted(selected.items()):
        progress.data["active_input"]={"kind":"needed_original_response_restore","R126_old_column":old}
        j,a=row["third_index"],row["quadratic_index"]
        require(row["quadratic_name"]==normal.exact.PARAMETERS[a]
                and normal.prior.blocks.THIRD_WEIGHTS[j]+normal.prior.blocks.PARAMETER_WEIGHTS[a]==0
                and ring.digest(roots["W"+str(j)])==row["third_original_sha256"],
                "original W/quadratic source identity changed")
        value=normal.prior.mixed_response(
            ring,normal.colored.ThirdOperator(ring,roots["W"+str(j)]),quadratics[a])
        require(ring.digest(value)==row["original_mode_sha256"]["-2"],
                "restored original R126 mixed SHA differs at "+str(old))
        responses[old]=value
        progress.unit("needed_response_mixed_inputs_restored",old)
        progress.record("needed_response_mixed_input",{
            "R126_old_column":old,"quadratic":row["quadratic_name"],"W_index":j,
            "mixed_sha256":ring.digest(value),"terms":len(value.terms),
            "third_original_sha256":row["third_original_sha256"],
        })
        ring.limits.check()
    return statics,responses

def make_mapper(ring):
    class Guarded(base.priority.PriorityWords):
        def cache_guard(self):
            ring.limits.shared_usage()
            super().cache_guard()
            ring.limits.check()
    owner=Guarded(ring,max_calls=LIMITS["word_calls"],max_terms=LIMITS["terms"],
        max_weight=5,max_shuffle_entries=LIMITS["cache_entries"],
        max_cache_entries=LIMITS["cache_entries"],color_order=("q",))
    ring.limits.monitored_owners.append(owner)
    ring.limits.check()
    return owner

def load_local(ring,rows):
    result=ring.number(0)
    for power,jets,coefficient in rows:
        require(type(power) is int and power>=0 and jets==sorted(jets),"paid local monomial schema changed")
        term=ring.x()**power
        for order in jets:
            require(type(order) is int and order>=0,"invalid paid jet")
            term*=ring.color("q",order)
        result+=F(coefficient)*term
        ring.limits.check()
    return result

class GreenCorrections:
    """Necessary new complete self fields of the SAME paid correction costs."""
    def __init__(self,ring,operator_rows,progress):
        self.ring,self.progress=ring,progress
        self.operators={name:tuple(load_local(ring,row[key]) for key in ("a","b","c"))
                        for name,row in operator_rows.items()}
        self.q,_,_=base.quadratic_operators(ring)
        self.cache={}
    def one(self,label):
        if label not in self.cache:
            e,z=label
            a,b,c=self.operators[z]
            w=self.q[e]
            u,p,r=(self.ring.color("q",j) for j in range(3))
            h=(a*r).D()+b*p
            primitive=(c*w).I()
            second=2*((a*w.D().D()).D()+b*w.D()+primitive)
            sigma=second.I().I()
            current=2*(a*(p*w.D().D()-r*w.D())+w*h+u*primitive)
            self.cache[label]=(sigma,current)
            self.progress.unit("necessary_new_Z_self_components",list(label))
        return self.cache[label]
    def sum(self,coefficients):
        sigma,current=self.ring.number(0),self.ring.number(0)
        for label,amount in sorted(coefficients.items()):
            ss,cc=self.one(label)
            sigma+=amount*ss; current+=amount*cc
            self.ring.limits.check()
        return sigma,current

def word_record(owner,value):
    rows=base.priority.rows(value)
    return {"terms":len(value.terms),"sha256":sha(canonical(rows)),"rows":rows}

def local_quad_integral(power,a,b,budget,cache):
    """Exact compact IBP for integral x^power v^(a)v^(b), not a profile test."""
    if a>b: a,b=b,a
    key=(power,a,b)
    if key in cache:
        return cache[key]
    require(type(power) is int and power>=0 and a>=0,"invalid closed quadratic monomial")
    if a==b:
        result={(power,a):F(1)}
    elif b==a+1:
        result={} if power==0 else {(power-1,a):F(-power,2)}
    else:
        result={}
        if power:
            add_vector(result,local_quad_integral(power-1,a,b-1,budget,cache),F(-power),budget)
        add_vector(result,local_quad_integral(power,a+1,b-1,budget,cache),F(-1),budget)
    cache[key]=result
    budget.check()
    return result

def closed_suffix(word,budget,cache):
    """Return exact closed quadratic symbols, keeping every nonlocal word."""
    require(sum(len(letter[1]) for letter in word)==2,"closed suffix is not quadratic")
    if len(word)==1:
        power,jets=word[0]
        require(len(jets)==2 and all(c=="q" for c,j in jets),"invalid quadratic suffix letter")
        # I is right-to-x: a one-word left value is minus its complete integral.
        values=local_quad_integral(power,jets[0][1],jets[1][1],budget,cache)
        return {("square",p,j):-v for (p,j),v in values.items()}
    require(len(word)==2 and all(len(letter[1])==1 for letter in word),
            "a closed quadratic word has an unexpected length")
    return {("ordered",word):F(1)}

def closed_symbol_rows(symbols):
    result=[]
    for symbol,wordexpr in sorted(symbols.items(),key=lambda kv:repr(kv[0])):
        if not wordexpr.terms:
            continue
        result.append({"closed_right_symbol":symbol,
                       "left_complete_words":base.priority.rows(wordexpr)})
    return result

def ordered_three_moments(whole,owner,degree,progress,target,kind):
    """Exact u-prefix/v-suffix separation of already COMPLETE right words."""
    require(degree in (4,5),"only new self(4) or cumulative(5) is in scope")
    symbolic={}; cache={}
    for (local,word),amount in whole.terms.items():
        require(all(color=="q" for piece in (local,)+word for color,j in piece[1]),
                "the full self is not one-color")
        require(len(local[1])+sum(len(letter[1]) for letter in word)==degree,
                "new ordered input has wrong full profile degree")
        suffix_degree=0
        for cut in range(len(word)-1,-1,-1):
            suffix_degree+=len(word[cut][1])
            if suffix_degree>2:
                break
            if suffix_degree!=2:
                continue
            require(len(local[1])+sum(len(letter[1]) for letter in word[:cut])==degree-2,
                    "ordered split degree inconsistency")
            for symbol,coefficient in closed_suffix(word[cut:],owner.limits,cache).items():
                expr=symbolic.setdefault(symbol,owner.zero())
                symbolic[symbol]=expr+owner.term(local,word[:cut]).scale(amount*coefficient)
            break
        owner.limits.check()
    symbolic={symbol:value for symbol,value in symbolic.items() if value.terms}
    mu0=symbolic.pop(("square",0,2),owner.zero())
    mu1=symbolic.pop(("square",1,2),owner.zero())
    mu2=symbolic.pop(("square",2,2),owner.zero())
    derivative_one=symbolic.pop(("square",0,1),owner.zero())
    mismatch=derivative_one-mu2.scale(2)
    if mismatch.terms:
        symbolic[("mu2_relation_residual",)]=mismatch
    records={
        "target":target,"kind":kind,"full_input_degree":degree,
        "outer_color_is_left_u":"local jets have no mixed-support products",
        "word_color_order":"u_prefix_then_v_suffix",
        "right_suffix_degree":2,"same_original_right_anchor":True,
        "complete_three_left_word_expressions":[base.priority.rows(v) for v in (mu0,mu1,mu2)],
        "exact_non_three_moment_symbols":closed_symbol_rows(symbolic),
        "discarded_words_or_moments":0,
    }
    progress.record("new_exact_ordered_three_moment_read",records)
    if symbolic:
        raise base.InterfaceFailure("new ordered read retains exact non-three-moment terms",records)
    progress.unit("new_ordered_three_moment_reads",target+":"+kind)
    return (mu0,mu1,mu2)

def af_outer(words,budget,expected_degree=5):
    """Only outer t=r^2/(3p). Never change integral letters or differentiate Af."""
    result={}
    for (local,word),amount in words.terms.items():
        power,jets=local
        require(all(color=="q" for color,j in jets),"unexpected outer color")
        orders=tuple(j for color,j in jets)
        require(len(orders)+sum(len(letter[1]) for letter in word)==expected_degree,
                "new self cumulative has wrong total degree")
        n0,n1,n2,n3=(orders.count(j) for j in range(4))
        high=tuple(j for j in orders if j>3)
        base.add(result,(power,n0,n1-n3,n2+2*n3,high,word),amount/F(3)**n3,budget)
    return result

def af_rows(poly):
    return [[power,n0,n1,n2,list(high),list(word),str(amount)]
            for (power,n0,n1,n2,high,word),amount in sorted(poly.items())]

def mirror_rows(poly,budget):
    """Symbolic true jets u=h*r,p=+/-s*r, r>0; x stays physical."""
    if any(high or word for power,n0,n1,n2,high,word in poly):
        return None
    answers=[]
    for sign in (1,-1):
        output={}
        for (power,n0,n1,n2,high,word),amount in poly.items():
            require(n0+n1+n2==5,"mirror normalization needs a complete quintic")
            base.add(output,(power,n0,n1),amount*F(sign)**n1,budget)
        answers.append({
            "sign_p_over_r":sign,"factor_removed":"r^5",
            "variables":["physical_x","h=u/r","s=abs(p/r)"],
            "complete_Laurent_rows":[[power,hpower,spower,str(v)]
                                    for (power,hpower,spower),v in sorted(output.items())],
            "p_denominator_order":max((max(0,-spower) for power,hpower,spower in output),default=0),
            "subsequent_actual_center_substitution":"physical_x=xi+/-b with the same b,h,s",
            "specific_mother_or_root_evaluated":False,
        })
    return answers

def new_current_rhs(current_words,sigma_words,owner,fresh,progress,name):
    current=ordered_three_moments(current_words,owner,5,progress,name,"left_current_3plus2")
    sigma=ordered_three_moments(sigma_words,owner,4,progress,name,"self_field_2plus2")
    flat={}
    for moment in range(3):
        progress.data["active_input"]={"kind":"new_current_moment","target":name,"moment":moment}
        quarter=current[moment].scale(F(1,4))
        # This checks the new two ordered contractions against one another.
        # It does NOT recompute any old Q/current column or rank.
        current_expr=owner.to_old(quarter)
        sigma_expr=owner.to_old(sigma[moment])
        difference=fresh.expression(current_expr.D()-owner.ring.color("q",1)*sigma_expr.D().D()/4)
        progress.record("new_current_derivative_certificate",{
            "target":name,"moment":moment,
            "difference_complete_right_words":base.priority.rows(difference),
            "complete_derivative_zero":not difference.terms,
            "full_left_constant_3plus2":"zero because the only n2 correction is local quintic",
            "old_Q_current_or_rank_executed":0,
        })
        if difference.terms:
            raise base.InterfaceFailure("new ordered current/field derivative mismatch",{
                "target":name,"moment":moment,"complete_difference":base.priority.rows(difference)})
        local=base.plain_local(quarter,"new weight-zero ordered current")
        af=base.af_polynomial(local,"new weight-zero ordered current")
        coordinates=base.decompose_current(af)
        for j,value in enumerate(coordinates):
            if value:
                flat[13*moment+j]=value
        progress.record("new_complete_current_moment",{
            "target":name,"moment":moment,"normalization":"complete partial K/4",
            "complete_quarter_current_before_Af":base.selfmap.local_rows(local),
            "complete_Af_polynomial":[[list(key),str(value)] for key,value in sorted(af.items())],
            "complete_thirteen_coordinates":[[label,str(value)] for label,value in zip(base.PARAMETERS,coordinates)],
            "full_thirteen_coordinate_reconstruction_zero":True,
            "Af_only_outer_relation_no_derivative_or_word_substitution":True,
        })
        progress.unit("new_complete_current_moments",(name,moment))
    value=flat.get(27,F(0))
    residual=dict(flat)
    base.add(residual,27,-value,owner.limits)
    base.add(residual,15,2*value,owner.limits)
    evidence={
        "target":name,"complete_39_coordinates":base.vector_rows(flat),
        "unique_A1_moment2_scalar":str(value),"subtract_current_Zc":str(value),
        "full_one_line_reconstruction_residual":base.vector_rows(residual),
        "old_current_image_or_rank_recomputed":False,
    }
    progress.record("new_unique_current_RHS",evidence)
    if residual:
        raise base.InterfaceFailure("new whole-E-zero current is outside its proved weight-zero line",evidence)
    progress.unit("new_unique_current_RHS",name)
    return value

def new_target(name,statics,responses,correction,zc,green,owner,fresh,progress):
    ring=owner.ring; spec=TARGETS[name]
    progress.stage("new_complete_self_and_current_"+name)
    progress.data["active_input"]={"kind":"new_target","target":name}
    mixed=sum((F(amount)*statics[index] for index,amount in sorted(spec["normal"].items())),ring.number(0))
    mixed+=sum((F(amount)*responses[index] for index,amount in sorted(spec["response"].items())),ring.number(0))
    mixed_sha=ring.digest(mixed)
    if "mixed_sha256" in spec:
        require(mixed_sha==spec["mixed_sha256"],"new target differs from its PAID full mixed source")
    diagonal=ring.substitute(mixed,{"qbar":ring.color("q")})
    require(not(ring.color_degrees(diagonal)-{(("q",4),)}),"complete mixed diagonal is not quartic")
    sigma=-4*diagonal
    u,p,r,t=(ring.color("q",j) for j in range(4))
    current=p*sigma.D()-r*sigma+(t*sigma).I()
    correction_sigma,correction_current=green.sum(correction)
    sigma-=correction_sigma; current-=correction_current
    progress.record("new_same_cost_before_current_correction",{
        "target":name,
        "original_normal_coefficients":coefficient_rows({i:F(v) for i,v in spec["normal"].items()}),
        "original_R126_coefficients":coefficient_rows({i:F(v) for i,v in spec["response"].items()}),
        "original_mixed_sha256":mixed_sha,"original_mixed_terms":len(mixed.terms),
        "global_original_diagonal_sha256":ring.digest(diagonal),"global_diagonal_terms":len(diagonal.terms),
        "subtract_Q_correcting_original_Z_costs":coefficient_rows(correction),
        "self_definition":"Sigma=-4*M_minus2(u,u), including every original N0/Gamma/right tail",
        "true_left_current_equals_right_current_plus_Omega":True,
        "Omega_left_constant":"published_n2" if name=="normal_XH" else "0",
        "Omega_n2_zero_only_on_the_published_four_constraint_affine_mother_library":name=="normal_XH",
        "whole_Q_zero_receipt":"R316 plus the seven recorded Q pivots" if name.startswith("response")
                               else "the original R316/R329 whole-E MEMBER representatives",
        "original_forcing_pure_Q_Omega_or_rank_recomputed":0,
    })
    sigma_words=owner.expression(sigma)
    current_words=owner.expression(current)
    progress.record("new_complete_self_before_current_correction",{
        "target":name,"whole_Sigma":word_record(owner,sigma_words),
        "whole_right_cumulative_current":word_record(owner,current_words),
        "left_constant":"published_n2" if name=="normal_XH" else "0",
        "left_constant_citation":"R406 eq.(9), raw Omega equals n2 for X_H; J4 and responses add zero",
        "known_left_constant_recomputed":False,
    })
    amount=new_current_rhs(current_words,sigma_words,owner,fresh,progress,name)
    zc_sigma,zc_current=green.sum(zc)
    final_sigma=sigma-amount*zc_sigma
    final_current=current-amount*zc_current
    final_words=owner.expression(final_current)
    final_sigma_words=owner.expression(final_sigma)
    final_combo=dict(correction)
    add_vector(final_combo,zc,amount,ring.limits)
    # Full original-source new difference, not a check of stored old coordinates.
    difference=fresh.expression(final_current.D()-p*final_sigma.D().D())
    progress.record("new_final_source_Green_certificate",{
        "target":name,"complete_original_difference":base.priority.rows(difference),
        "new_full_Green_derivative_zero":not difference.terms,
        "proof_scope":"this new full target after its same-cost Q and current corrections",
        "old_certificate_or_rank_executed":0,
    })
    if difference.terms:
        raise base.InterfaceFailure("new full target Green derivative failed",{
            "target":name,"difference":base.priority.rows(difference)})
    # The scalar correction uses the original paid current of Zc. Its full
    # ordered cancellation is nevertheless verified at the NEW target source.
    final_ordered=ordered_three_moments(final_words,owner,5,progress,name,"final_current_3plus2")
    residuals=[]
    for moment,value in enumerate(final_ordered):
        local=base.plain_local(value,"new corrected current")
        af=base.af_polynomial(local,"new corrected current")
        residuals.append([[list(key),str(v)] for key,v in sorted(af.items())])
    progress.record("new_final_whole_current_zero_certificate",{
        "target":name,"three_Af_current_residuals":residuals,
        "complete_current_zero":not any(residuals),
        "right_words_reduced_before_outer_Af":True,
        "no_old_current_map_or_rank":True,
    })
    if any(residuals):
        raise base.InterfaceFailure("new current correction source did not cancel all three moments",{
            "target":name,"three_Af_current_residuals":residuals})
    poly=af_outer(final_words,ring.limits,5)
    local={key:value for key,value in poly.items() if not key[-2] and not key[-1]}
    nonlocal_terms={key:value for key,value in poly.items() if key[-1]}
    high={key:value for key,value in poly.items() if key[-2] and not key[-1]}
    mirrors=mirror_rows(poly,ring.limits)
    result={
        "target":name,"source_normal_coefficients":coefficient_rows({i:F(v) for i,v in spec["normal"].items()}),
        "source_R126_coefficients":coefficient_rows({i:F(v) for i,v in spec["response"].items()}),
        "subtract_total_original_Z_cost_combination":coefficient_rows(final_combo),
        "unique_current_scalar_A1_moment2":str(amount),
        "whole_Sigma":word_record(owner,final_sigma_words),
        "whole_right_cumulative_before_Af":word_record(owner,final_words),
        "true_left_cumulative_equals_shown_plus":"published_n2" if name=="normal_XH" else "0",
        "true_left_constant_definition":"n2(u)=integral of the twelve-term R406 local quintic density",
        "n2_zero_scope":"same four-constraint mother and its complete positive-affine orbit",
        "n2_universal_zero_claimed":False,
        "complete_Af_rows":af_rows(poly),"local_Af_rows":af_rows(local),
        "nonlocal_Af_rows":af_rows(nonlocal_terms),"higher_outer_jet_Af_rows":af_rows(high),
        "complete_local_Laurent_interface":not nonlocal_terms and not high,
        "p_denominator_order":max((max(0,-key[2]) for key in poly),default=0),
        "symbolic_true_mirror_rows":mirrors,
        "whole_current_zero_from_new_source":True,"new_Green_derivative_certificate_zero":True,
        "actual_mother_or_root_evaluation":False,
        "fixed_mother_nonmembership_claimed":False,
        "all_width_or_actual_joint_claimed":False,
        "mirror_rank_or_membership_executed":False,
        "discarded_nonlocal_or_high_jets":0,
    }
    progress.record("new_complete_final_self",result)
    progress.unit("new_complete_final_self_targets",name)
    summary={
        "target":name,"current_scalar":str(amount),"complete_current_zero":True,
        "full_self_observed":True,"complete_local_Laurent_interface":result["complete_local_Laurent_interface"],
        "p_denominator_order":result["p_denominator_order"],
        "complete_self_Af_terms":len(poly),"nonlocal_Af_terms":len(nonlocal_terms),
        "higher_outer_jet_Af_terms":len(high),"mirror_polynomial_published":mirrors is not None,
        "result_payload_sha256":sha(canonical(result)),
        "outcome":"complete_local_self_interface" if result["complete_local_Laurent_interface"]
                  else "complete_exact_self_with_unresolved_nonlocal_or_high_jet_remainder",
        "fixed_mother_nonmembership":None,"old_science_executions":0,
    }
    return summary

def total_clock_budget(started):
    budget=base.make_budget(LIMITS["seconds"])
    inherited=budget.check
    budget.rational_operations+=RESUME["prior_monitored_rational_operations"]
    budget.maximum_monitored_rational_bits=max(budget.maximum_monitored_rational_bits,
        RESUME["prior_maximum_monitored_rational_bits"])
    budget.calls+=RESUME["prior_limit_check_calls"]
    deadline=started+LIMITS["seconds"]-RESUME["prior_science_seconds"]
    def check():
        inherited()
        if time.perf_counter()>deadline:
            raise base.exact.formal.CompilationBudgetExceeded("cumulative scientific clock including the paid failed run expired")
    budget.check=check
    return budget,deadline

def science(repository,progress):
    progress.start()
    progress.stage("initialize_shared_clock_before_resume_reads")
    budget,deadline=total_clock_budget(progress.started_at)
    progress.bind(budget=budget)
    reader=Reader(budget,deadline)
    progress.data["network"]={"requests":0,"bytes":0,"redirects":0}
    progress.data["one_scientific_clock_includes"]=[
        "the prior failed segment and its four paid log reads and two completed Q-RHS applications",
        "this exact ten-record resume read and six original operator records only",
        "necessary three-static/eight-response input restoration",
        "new full self/current symbols and fresh source differences",
        "all failed work, partial observations and main-report output across segments",
    ]
    progress.data["charged_prior_science_seconds"]=RESUME["prior_science_seconds"]
    progress.data["available_resume_seconds_at_start"]=LIMITS["seconds"]-RESUME["prior_science_seconds"]
    progress.data["prior_rational_operation_count"]=RESUME["prior_monitored_rational_operations"]
    progress.data["prior_peak_RSS_KiB"]=RESUME["prior_peak_RSS_KiB"]
    progress.data["scope"]=DOMAIN
    try:
        progress.stage("read_exact_paid_failure_checkpoint")
        corrections,zc,needed=resume_paid_interfaces(reader,progress)
        progress.stage("read_six_paid_R434_operator_records_only")
        operator_rows=read_paid_operator_rows(reader,progress,needed)
        progress.stage("restore_only_three_static_and_eight_response_mixed_inputs")
        ring=normal.colored.ColoredRing(budget)
        progress.bind(ring=ring)
        statics,responses=restore_original_inputs(ring,repository,progress)
        owner,fresh=make_mapper(ring),make_mapper(ring)
        progress.bind(owners=[("new_fullself",owner),("fresh_new_differences",fresh)])
        green=GreenCorrections(ring,operator_rows,progress)
        progress.data["targets"]=[]
        for name in TARGET_ORDER:
            try:
                result=new_target(name,statics,responses,corrections[name],zc,green,owner,fresh,progress)
                progress.data["targets"].append(result)
            except base.InterfaceFailure as exc:
                evidence=exc.evidence or {}
                progress.record("new_target_unresolved_exact_interface",{
                    "target":name,"error":str(exc),"complete_evidence":evidence,
                    "fixed_mother_nonmembership_claimed":False,
                    "not_an_automatic_zero_or_nonmember":True,
                })
                progress.data["targets"].append({
                    "target":name,"outcome":"unresolved_exact_interface",
                    "full_self_observed":False,"error":str(exc),
                    "evidence_sha256":sha(canonical(evidence)),
                    "fixed_mother_nonmembership":None,
                })
                progress.unit("new_target_unresolved_interfaces",name)
            budget.check()
        progress.data["active_input"]=None
        progress.data["all_four_self_targets_observed"]=all(row["full_self_observed"] for row in progress.data["targets"])
        progress.data["all_four_targets_complete_local"]=progress.data["all_four_self_targets_observed"] and all(
            row.get("complete_local_Laurent_interface",False) for row in progress.data["targets"])
        progress.data["zero_executions"]={
            "old_pure_mapping":0,"old_Q_mapping":0,"old_Omega_mapping":0,"old_current_rank":0,
            "old_self_rank":0,"old_development_suites":0,"old_forcing_compilation":0,
            "new_profile_or_root_evaluation":0,"new_development":0,"new_mirror_rank_or_membership":0,
            "already_paid_Q_RHS_reapplications":0,"old_member_checks_repeated":0,
            "old_R316_R329_R443_logs_reread":0,
        }
        progress.data["joint_h_y_quotient_relation_not_replaced_by_two_MEMBER_booleans"]=True
        progress.data["next_mathematical_step"]=(
            "directly continue the two new targets' common quotient/member comparison from these complete formulas; "
            "a nonlocal remainder is not a fixed-mother nonmember certificate")
        progress.finish("complete_four_new_self_interfaces" if progress.data["all_four_self_targets_observed"]
                        else "four_new_targets_attempted_with_exact_unresolved_interfaces")
    finally:
        progress.data["network"]={"requests":reader.requests,"bytes":reader.bytes,"redirects":reader.redirects}
        progress.data["cumulative_network"]={
            key:RESUME["prior_network"][key]+progress.data["network"][key]
            for key in ("requests","bytes","redirects")}
        progress.data["cumulative_science_elapsed_at_stage_exit_seconds"]=(
            RESUME["prior_science_seconds"]+time.perf_counter()-progress.started_at)
        progress.snapshot()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        parser.error("only the reviewed public Actions entry may execute the four new contractions")
    repository=Path(__file__).resolve().parents[3]
    output=args.out.resolve()
    if repository==output or repository in output.parents:
        parser.error("machine outputs must remain outside the Git checkout")
    output.parent.mkdir(parents=True,exist_ok=True)
    journal=Journal(output.with_suffix(".records.jsonl"))
    progress=base.PhaseProgress("science",journal)
    started=time.perf_counter()
    report={
        "schema":SCHEMA,"repository":REPOSITORY,
        "run_id":os.environ.get("GITHUB_RUN_ID"),"run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
        "workflow_source":os.environ.get("GITHUB_SHA"),"domain":DOMAIN,"limits":LIMITS,
        "science":progress.data,"development":{"executed":False,"new_checks":0,"old_checks":0},
        "old_science_executions":0,"actual_joint_period_resolved":False,
        "unabridged_math_emitted_once_as_sequential_records":True,
        "source_binding_complete":False,
        "resume_from":{"run_id":RESUME["run_id"],"job_id":RESUME["job_id"],
            "source_commit":RESUME["source_commit"],
            "charged_prior_science_seconds":RESUME["prior_science_seconds"],
            "prior_pre_science_entry_seconds":RESUME["prior_pre_science_entry_seconds"]},
    }
    exit_code=0;identities=[]
    try:
        request_path=args.request.resolve()
        require(repository in request_path.parents,"request must be inside the bound checkout")
        require(Path(__file__).resolve()==repository/ENTRY,"executed entry path differs from the request")
        request_raw=request_path.read_bytes()
        require(len(request_raw)<100000,"reviewed request must be a small UTF-8 file")
        request=normal.paid.decode_json(request_raw)
        report["request"]={"bytes":len(request_raw),"sha256":sha(request_raw)}
        identities=validate(request,repository)
        report["source_manifest"]=identities
        report["source_binding_complete"]=True
        base.load_algebra()
        # Existing interface limits are identical. No old config/source mutation.
        require(all(base.LIMITS[key]==LIMITS[key] for key in
            ("seconds","memory_mib","nodes","atoms","terms","word_calls","cache_entries",
             "rational_bits","monitored_rational_operations")),"shared paid budget interface changed")
        science(repository,progress)
        report["entry_outcome"]=("complete_new_observation" if progress.data["all_four_self_targets_observed"]
                                 else "unresolved_structural_interface")
        if not progress.data["all_four_self_targets_observed"]:
            exit_code=2
    except Exception as exc:
        if isinstance(exc,base.InterfaceFailure):
            exit_code,outcome=2,"unresolved_structural_interface"
        elif isinstance(exc,base.OutputBudgetExceeded):
            exit_code,outcome=3,"finite_stdout_budget_failure"
        elif hasattr(base,"exact") and isinstance(exc,base.exact.formal.CompilationBudgetExceeded):
            exit_code,outcome=3,"finite_budget_failure"
        elif isinstance(exc,InputFailure):
            exit_code,outcome=4,"original_input_or_source_binding_failure"
        else:
            exit_code,outcome=4,"entry_error"
        report["entry_outcome"]=outcome
        report["entry_error"]={"type":type(exc).__name__,"message":str(exc)}
        if progress.data["started"]:
            try:
                progress.fail(outcome,exc)
            except Exception as second:
                report["secondary_reporting_error"]={"type":type(second).__name__,"message":str(second)}
    finally:
        progress.snapshot()
        journal.file.close()
        report["total_elapsed_seconds"]=time.perf_counter()-started
        report["segment_peak_RSS_KiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report["peak_RSS_KiB"]=max(RESUME["prior_peak_RSS_KiB"],report["segment_peak_RSS_KiB"])
        report["record_journal"]=journal.receipt()
    encoded=canonical(report)+b"\n"
    line=b"COMPLETE_WEIGHT_ZERO_SELF_REPORT "+encoded
    if journal.inherited_stdout_bytes+journal.stdout_bytes+len(line)+2048>LIMITS["mathematical_stdout_bytes"]:
        unabridged=output.with_suffix(".unemitted-summary.json")
        unabridged.write_bytes(encoded)
        report["unabridged_summary_identity"]={"bytes":len(encoded),"sha256":sha(encoded),
                                               "runner_temporary_filename":unabridged.name}
        report.pop("source_manifest",None)
        report["source_manifest_identity"]={"entries":len(identities),"bytes":len(canonical(identities)),
                                            "sha256":sha(canonical(identities))}
        report.pop("domain",None)
        report["domain_identity"]={"bytes":len(canonical(DOMAIN)),"sha256":sha(canonical(DOMAIN))}
        progress.data.pop("scope",None)
        report["entry_outcome"]="finite_stdout_budget_failure"
        report["complete_mathematical_publication"]=False
        encoded=canonical(report)+b"\n"
        line=b"COMPLETE_WEIGHT_ZERO_SELF_REPORT "+encoded
        exit_code=3
    # No charged stage, counter, failure, result fingerprint or earlier record is dropped.
    output.write_bytes(encoded)
    sys.stdout.buffer.write(line);sys.stdout.buffer.flush()
    # Authoritative sample AFTER the complete main report/file/stdout. The old
    # PhaseProgress receipt is deliberately frozen earlier and is not total cost.
    clock_start=progress.started_at
    sampled=time.perf_counter()
    segment_elapsed=None if clock_start is None else sampled-clock_start
    elapsed=RESUME["prior_science_seconds"]+(segment_elapsed or 0.0)
    overrun=max(0.0,elapsed-LIMITS["seconds"])
    exceeded=elapsed>LIMITS["seconds"]
    terminal={
        "schema":SCHEMA+"-final-clock","run_id":os.environ.get("GITHUB_RUN_ID"),
        "workflow_source":os.environ.get("GITHUB_SHA"),
        "unified_science_started":True,
        "resume_segment_science_started":clock_start is not None,
        "prior_charged_science_seconds":RESUME["prior_science_seconds"],
        "resume_segment_science_and_main_output_elapsed_seconds":segment_elapsed,
        "all_science_and_main_output_elapsed_seconds":elapsed,
        "prior_pre_science_entry_seconds":RESUME["prior_pre_science_entry_seconds"],
        "prior_pre_science_entry_seconds_counted_as_science":False,
        "entry_elapsed_seconds":sampled-started,
        "limit_seconds":LIMITS["seconds"],"overrun_seconds":overrun,
        "limit_exceeded":exceeded,"no_further_science":True,
        "supersedes_frozen_PhaseProgress_elapsed_for_total_budget":True,
        "sample_point":"after main report file write and stdout flush; before this terminal clock emission",
        "nonpreemptible_output_overrun_not_clipped":True,
        "main_report_entry_outcome":report.get("entry_outcome"),
        "terminal_exit_code":3 if exceeded else exit_code,
        "peak_RSS_KiB":max(RESUME["prior_peak_RSS_KiB"],resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "total_rational_operations_include_prior_segment":True,
        "mathematical_stdout_cap_includes_prior_segment":True,
    }
    sys.stdout.buffer.write(b"FINAL_CLOCK "+canonical(terminal)+b"\n")
    sys.stdout.buffer.flush()
    return 3 if exceeded else exit_code

if __name__=="__main__":
    raise SystemExit(main())

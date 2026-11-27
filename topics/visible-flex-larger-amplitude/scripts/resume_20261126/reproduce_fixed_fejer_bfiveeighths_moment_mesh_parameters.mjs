#!/usr/bin/env node
/* Complete fixed-parent text/JSON parameter reproducer.
   No scientific imports, numerical field calls, AST, fixture, job or ref operations. */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
const SPEC = {
  "schema": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-construction-spec-v1",
  "repository": "Rogerhu12/math-research-public",
  "topic": "topics/visible-flex-larger-amplitude",
  "prepared_utc": "2026-11-27T23:38:52Z",
  "old_namespace": "fixed-fejer-meridian-batched-bhalf-first",
  "namespace": "fixed-fejer-meridian-batched-bfiveeighths-first",
  "old_short_namespace": "fixed-fejer-bhalf-R723",
  "short_namespace": "fixed-fejer-bfiveeighths-R723",
  "parents": {
    "R716": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 80089,
      "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
      "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db",
      "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
    },
    "R723_R716": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "bytes": 97718,
      "sha256": "11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3",
      "git_blob_sha": "a5111bec896c7a83e598a9ea26f1372b80b309dc"
    },
    "mesh_final": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
      "bytes": 91284,
      "sha256": "04456c30ae931cb8d10e2652c8ef51fcd5e6ad5bfe4141e129b7fb98a04bf9c9",
      "git_blob_sha": "aafad01042d2a1412d070c2e302d762b3d0244c8",
      "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
    },
    "mesh_packet": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
      "bytes": 91233,
      "sha256": "eeb88aede82e6d447472c22d884a91a1dec044d4078b15503e25c956e11ba2f4",
      "git_blob_sha": "bb953c7250373eea6e263e19533282136622d5e3",
      "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
    },
    "sharing_binding20": {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "bytes": 27741,
      "sha256": "fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b",
      "git_blob_sha": "cd97924e283d44b3662083c12e2588aef3c3d306"
    },
    "sharing_delivery20": {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-post-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-post-parameter-delivery.json",
      "bytes": 20363,
      "sha256": "257b75cad290db8c1af0b68f67aa8c93e9c75adf495b6e218eadb3c7e9102698",
      "git_blob_sha": "e8df2b573e3ccb310575a7b31699bc63701623b8"
    },
    "current_binding": {
      "name": "fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
      "bytes": 64060,
      "sha256": "3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1",
      "git_blob_sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5"
    },
    "current_post_delivery": {
      "name": "fixed-fejer-bfiveeighths-complete-normal-closed-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-delivery.json",
      "bytes": 15287,
      "sha256": "ea71cb88d6c8777f3b2a9579197bcc7113eb300d53314037722977378d68b7ca",
      "git_blob_sha": "488d9a9489ec9dca349eb68ed94fe662d75e89c6"
    },
    "current_science": {
      "name": "fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
      "bytes": 97307,
      "sha256": "6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d",
      "git_blob_sha": "6da95445b088f8593ff0f5fb14d76167b26a7a21"
    },
    "current_pure": {
      "name": "fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
      "bytes": 86702,
      "sha256": "b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822",
      "git_blob_sha": "5b2b58e75572b75ce499c8983adf3ba20278211b"
    },
    "current_science_delivery": {
      "name": "fixed-fejer-bfiveeighths-complete-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json",
      "bytes": 52529,
      "sha256": "550ae5ff18b9022bed7ec000c9c63b5958701f632aea100f59f338da249c971e",
      "git_blob_sha": "8125f12b1c6df083945afe30bb412577428b5b32"
    }
  },
  "runtime_sources": [
    {
      "name": "fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
      "bytes": 70554,
      "sha256": "45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8",
      "git_blob_sha": "8f36de4b8a4420e26eb07d4d4bf409d8eac6dda6"
    },
    {
      "name": "fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
      "bytes": 46887,
      "sha256": "d0fe262ba0208562ed5578a17b22847659a5e747b601441b65b2e73d50462e63",
      "git_blob_sha": "03233ce1e49976cb31530df82852ef5154f28462"
    },
    {
      "name": "r716_closed_surface_moment_arithmetic.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r716_closed_surface_moment_arithmetic.py",
      "bytes": 17397,
      "sha256": "f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a",
      "git_blob_sha": "e265b5b25932ac97dc173071e00c60a568e80cc5"
    },
    {
      "name": "fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py",
      "bytes": 73500,
      "sha256": "2ef316b9075f14af66e1deda235c4df9319a0c29cfeddb10a40130712a12d76c",
      "git_blob_sha": "62e4551908e43beb9684db85998a49ff81337d5e"
    },
    {
      "name": "fixed_fejer_complete_phase_mesh_arithmetic.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py",
      "bytes": 39436,
      "sha256": "80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4",
      "git_blob_sha": "57c2c563785dab3a1148645225106ca5860e2e2f"
    },
    {
      "name": "fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py",
      "bytes": 53829,
      "sha256": "b3991da8585b553a6c3133da806fafa4903e2c01087634c18ee168e6718bc4d7",
      "git_blob_sha": "e691ac03f470b3d5477525b8f8c38007741a8747"
    },
    {
      "name": "read_fixed_fejer_meridian_batched_producer_bound_same_field_phase_mesh_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_producer_bound_same_field_phase_mesh_report.py",
      "bytes": 22184,
      "sha256": "8197f77d1372710931ba6882c9fd88f035154a7082310bfdfa645865cde3e5c2",
      "git_blob_sha": "16fb78089178ebd50a925239d179c40588fa90bd"
    },
    {
      "name": "fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
      "bytes": 84576,
      "sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
      "git_blob_sha": "5f3b42618cfab77eaa3297073d71657e8df78dac"
    },
    {
      "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
      "bytes": 87670,
      "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
      "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
    },
    {
      "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
      "bytes": 61706,
      "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
      "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
    }
  ],
  "paths": {
    "binding": "computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
    "R716": "computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "R723_R716": "computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-complete-R716-moment-ready.json",
    "mesh_final": "computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json",
    "mesh_packet": "computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json",
    "reproducer": "scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_moment_mesh_parameters.mjs",
    "note": "notes/2026-11-27-fixed-fejer-bfiveeighths-complete-moment-mesh-parameters.md",
    "manifest": "computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json"
  }
};
const NOTE_TEXT = "# Run21：b/S=5/8 同源完整 R716 / mesh 后处理参数\n\nPrepared UTC: 2026-11-27T23:38:52Z。本件只制作完整参数与恢复说明；没有执行科学计算、AST、编译、数值样例、benchmark、队列写入或 ref 更新。新 namespace 为 fixed-fejer-meridian-batched-bfiveeighths-first。本件不声明实际 run21 已产生完整场、final、packet 或任何费用。\n\n## 1. 当前科学定义与原参数完整性\n\n本参数包消费原完整10fa科学驱动、8027纯读器、f600启动器的同一当前来源家族：137 scientific source roles、18 runtime files。157是科学argv词数，不是来源角色数。原120完整来源路径/SHA对全部保留。完整当前参数把支持种子的相对端层总长度从run19的1/2改为5/8，profile delta仍1/32，metric与restoration初始阻尼都为.01；run20的.001没有带入。其余全部原方向、迭代、线搜索、变量、normal32段、角域、显式点/历史职责和预算不动。\n\n精确预定种子定义：四个端层各长5/32 S，两个中央区间为[3/16,5/16] S与[11/16,13/16] S，各长1/8 S，中央总长1/4 S。这些是预定有理定义，不是实际浮点carrier、mean root或几何返回。maker/reference的全部参数和固定Fejér-R690目标没有因种子width改变；后续实际seed model、完整current field、root branch和输出身份仍必须来自自己的真实报告。same fixed g不等于same field，也不允许从run19/20的可变观察或accepted状态填本任务的实际输入。\n\n当前科学完整投影不是摘要替代：root的完整共享binding逐字保存157个argv词、全部137源记录、全部18运行体记录、原五个支持的pending CLI、八个external peer责任及新19/20已知记录。该binding还绑定完整science/pure文件，因此458/445正式projection和48 live projection全部可恢复。我们再次保存完整157词作为当前矩/mesh归属投影，137/18则精确指向同一whole绑定对象的完整JSON位置。没有把未返回的typed/history改为空，也没有把新external peer塞进不支持的PARENT_FAMILIES。\n\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json — 64060 B; SHA-256 3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1; Git blob 033bc2427bd70d86a639c6c3a38b3314f3ebe5b5.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-delivery.json — 15287 B; SHA-256 ea71cb88d6c8777f3b2a9579197bcc7113eb300d53314037722977378d68b7ca; Git blob 488d9a9489ec9dca349eb68ed94fe662d75e89c6.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json — 97307 B; SHA-256 6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d; Git blob 6da95445b088f8593ff0f5fb14d76167b26a7a21.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json — 86702 B; SHA-256 b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822; Git blob 5b2b58e75572b75ce499c8983adf3ba20278211b.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json — 52529 B; SHA-256 550ae5ff18b9022bed7ec000c9c63b5958701f632aea100f59f338da249c971e; Git blob 8125f12b1c6df083945afe30bb412577428b5b32.\n\n新矩/mesh共享binding：\n\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json — 71214 B; SHA-256 02589f547c2e9cffb3307e1a675f1a3d616925a694844e1ccbdcd9d18c982e99; Git blob fceab004648c04dd5849cf71a125ff6e6db89c55.\n\n## 2. 无损共享历史，而非删除历史字段\n\n每个原19 ready的完整顶层与嵌套对象都保留在其原whole文件中；本包逐件保存路径、字节数、SHA-256和Git blob。当前ready只外置重复的历史metadata，完整可执行step仍直接保留。原field/source/失败/未知责任没有被折叠成短摘要或丢弃。新共享binding明确哪些对象是历史，哪些字段是当前science投影；旧run的actual字段不因字符串换名变成本run实际证据。\n\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json — 80089 B; SHA-256 3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a; Git blob 7d748fcb2ca892ce50c23d0153c198f99fc307db.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json — 97718 B; SHA-256 11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3; Git blob a5111bec896c7a83e598a9ea26f1372b80b309dc.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json — 91284 B; SHA-256 04456c30ae931cb8d10e2652c8ef51fcd5e6ad5bfe4141e129b7fb98a04bf9c9; Git blob aafad01042d2a1412d070c2e302d762b3d0244c8.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json — 91233 B; SHA-256 eeb88aede82e6d447472c22d884a91a1dec044d4078b15503e25c956e11ba2f4; Git blob bb953c7250373eea6e263e19533282136622d5e3.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json — 27741 B; SHA-256 fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b; Git blob cd97924e283d44b3662083c12e2588aef3c3d306.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-post-parameter-delivery.json — 20363 B; SHA-256 257b75cad290db8c1af0b68f67aa8c93e9c75adf495b6e218eadb3c7e9102698; Git blob e8df2b573e3ccb310575a7b31699bc63701623b8.\n\n后两件是已成run20 R723的共享方式来源，不代表继承其.001、run、field或输出。唯一step文本变换是当前完整namespace、R723短ID namespace以及scope中的bhalf-first名称映射。每一个当前step完整反向映射后等于其原19整个step对象，包括script、全部argv位置、parent_bundle、scope、output列表、所有selector键值、retention字段以及原本若有的cleanup字段。不存在按字段白名单重造缩短step。\n\n## 3. 四个完整ready与准确计数\n\n| 完整计划 | argv词数 | 正式selector对 | live对 | 必需实际输入 |\n| --- | ---: | ---: | ---: | --- |\n| 45ca公共矩producer | 10 | 34 | 0 | 完整同点R722 normal/physical-sixjet费用 |\n| d0fe legacy矩consumer | 8 | 60 | 0 | 同矩输出与002eb完整closed主/副链 |\n| 3c0d R723兼容矩consumer | 8 | 65 | 0 | 同矩输出与1782完整R723主/副链 |\n| mesh final / packet，各自原入口 | 32 | 110 | 48 | actual final13或actual完整immutable snapshot |\n| mesh final / packet，各自原纯读 | 6 | 58 | 0 | 自己实际完整mesh报告与完整生成字节 |\n\nR723兼容consumer保原60项并保其五个兼容输出，不把65误裁成60。mesh正式110项是两个完整输出对象的55+55，不只保其中一个。48项live仍是原5个mesh标量加43个normal进度字段；我们不增加selector、不挤掉原项、不据live推断完整返回。\n\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-R716-closed-flux-centred-moments-ready.json — 18849 B; SHA-256 c9d6a4a720a5447fa5b7bd1c0ea5c21a06353674da2fe698b8ba4fa8aa605518; Git blob 94afe89393e0b7d4f6fde3fa453171e55b8c99ab.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-complete-R716-moment-ready.json — 19834 B; SHA-256 470f9f0e328a3aa6d40bad81357f7321edec3b4057ec49ecf31b3082c951be5f; Git blob 655ffdd6468f70edce1eb1c3ddcbe0d9796fc296.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json — 28934 B; SHA-256 4a305e8ae4b90886f88bbcaa18c25645e8145a83bd3def8c2b870e8795852f21; Git blob 6605aa4784b2ac9d32c639d343068ec916b94cbb.\n- topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json — 28936 B; SHA-256 2569954a1496af914a29daa1a1d474e46a34d511b6f121197af0bfe6d410d1da; Git blob f7f83d236437a2f562e5cc17be631bce9bed5342.\n\n两个矩ready的第0项是完全相同的45ca whole step（同ID、script、全部参数、输出及selector）。如果两个consumer都安排，producer只执行一次；若producer已经排队或真实返回，R723计划只取其第1项consumer。不能只按相似名字复用不同point/report的producer。总表把7个唯一step与其完整ready/index列明；本件不创建活动queue，执行先后必须服从真实完整输入。\n\n## 4. R716全域、十二通道与独立闭面解释\n\n矩producer仍用原600秒和maximum-angle-blocks=0，后者表示不另设角块数量上限。完整输入域是phi/pi∈[0,2]、上经线s∈[0,S]，保上游1024闭角胞、原922径向胞、全部准确support/profile/control切点和scalar尾项，保完整33节点/32段normal唯一性、角方向glue、原点/模型/快照/target/六真实input/source闭包。没有用有限采样代替whole cell。\n\n十二原通道逐项保留：V、mx、my、mz、Qxx、Qxy、Qxz、Qyy、Qyz、Qzz、A2_real、A2_imag。下反射、两平帽、精确p4的体积/一次矩/混合矩都沿原算核。一般完整三相位t=0,1/2,1的旋转、总重心及二次中心矩补偿不依赖未付半转；简化B_eff公式仍必须先有真实全32段signed half-turn根包含。原有已完成原子块可保留，但缺任一全域覆盖、mean或branch条件时，whole-domain积分不得补成完整值。\n\n45ca输出首先是准确参数通量及条件矩算术。它本身不证闭面嵌入、外向、有界体或非全等。legacy d0fe分支只消费精确002eb源的final complete主报告及其原记录的R716-unmarked-outward-tube副件，保全原八角色链；R723兼容3c0d增加精确1782/schema派发，并完整保留legacy validator。R723分支保原八角色为false，用自己独立五角色及joint-flow/mixed-pair条件，不能伪装旧R650八角色已付。\n\nR723主报告由root当前参数件提供，完整8词/77 selector已绑定；本包没有重复改写它。两种consumer都要求真实相同完整point/model/snapshot/target、全部主/副输入与输出末次重核，并要求独立unmarked flat-cap outward tube严格超过1/1000。此后仍要正总volume和分离的非零中心不变量，才能解释原R625/R716 E(3)-商下界。R722 mean存在、R718 holding distance、R723标记闭面reach或生成一个副件，都不能单独支付这些R716前提。\n\n## 5. 精确共享的三条矩来源\n\n- topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py — 70554 B; SHA-256 45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8; Git blob 8f36de4b8a4420e26eb07d4d4bf409d8eac6dda6.\n- topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py — 46887 B; SHA-256 d0fe262ba0208562ed5578a17b22847659a5e747b601441b65b2e73d50462e63; Git blob 03233ce1e49976cb31530df82852ef5154f28462.\n- topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py — 61706 B; SHA-256 3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b; Git blob 3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4.\n\n45ca producer、d0fe legacy consumer和3c0d兼容consumer是三个不同whole source，不能只按相似basename混写。没有新运行体；其原body、数学、源guard和失败语义都不变。上游R722四费、002eb与1782闭面源由完整当前root normal/closed总表关联。\n\n## 6. mesh原无附证参数：没有删对模式\n\n本次已实际逐词读原19 final和packet argv：两者都是32词，本来就没有--closed-phase-report。当前21逐词映射后仍为32词；没有为了成功而删除任何参数对，也没有追加R723路径。原2ef3输入源的bind_closed_phase_evidence只在path=None时允许无附证生成；显式给路径后，缺文件、未complete、错误schema/source或不同point都会拒绝。其旧可选分支只认可002eb，不接受1782 R723。\n\n因此本包两mesh计划没有可选准确闭面证据，也不冒称old closed已完成。原optional metadata、精确旧源与将来若显式附证所需完整主报告条件仍在共享binding和完整父件中。geometry另做的R723兼容mesh是另一个显式source family，不能在本2ef3/b399/8197计划里偷偷换源或换报告。无附证模式是原源码公开的数值mesh能力，不减少任何数值域，也不绕过R716必须的闭面证书；连续全局证明仍由独立完整费用链支付。\n\n## 7. 完整同场mesh、物理相位与精化\n\nfinal模式必须读真实complete科学报告及完整13成员final checkpoint；缺final时不能用initial、进度或某trial顶替。packet模式必须读报告真实捕获的完整required-angle immutable snapshot，保存完整点词、全部已录角与32段记录；该点可以是trial/cache点，不能由此推accepted或final。两模式的场身份各自明确，不能把两次选择混称同一输出。\n\n对每个选定完整点，全部mesh和t只使用同一个控制词/高度/固定g。物理相位保持F_t(s,phi)=R_(pi*t/2) U(s,Theta0^(-1)(Theta0(phi)-pi*t/2))，固定material图、全lower reflection和固定Cartesian p4 caps保持；不是只把旧phi网格旋转。H使用该完整当前点自己的原word，全t固定。所有原raw closure lift均保，不能把T偷换成Fs。\n\n| 空间级别 | 每原径向胞细分 | 全角数 | cap rings |\n| --- | ---: | ---: | ---: |\n| 1 | 1 | 512 | 16 |\n| 2 | 2 | 1024 | 32 |\n| 3 | 4 | 2048 | 64 |\n\n每级全做物理t=0,1/4,1/2,3/4,1，共15张完整科学mesh；时间精化保4、8、16的完整分割。fixed-chart iterations=64、working tolerance=2e-12、field-angle-block=8、export-levels=all不动。五个独立预览各保96径向节点、128全角、32帽圈及每文件严格5000000字节上限；此上限只针对完整渲染预览，不截断全科学mesh。全科学坐标64bit，预览32bit的差异与port projection和序列化误差原报告保留。\n\n原M160→M320零嵌入输入说明和三omega路由仍完整保留，但本次mesh不是M320新场求解，不继新solver norm/damping。空间/t实际差值、sampled metric、全raw closure/port/periodic差值必须由真实runner输出。离散mesh拓扑、PL metric或有限差值均不构成连续isometry、embedding、reach或全t误差证书。\n\n## 8. 真输入依赖与执行顺序\n\n- scientific_report: {work}/fixed-fejer-meridian-batched-bfiveeighths-first/report.json\n- scientific_command: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-command.json\n- normal: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-normal-root-and-sixjet-fees-v1/report.json\n- geometry: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-continuous-gram-curvature-support-v1/report.json\n- legacy_closed: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-closed-phase-grip-v1/report.json\n- legacy_tube: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json\n- R723_closed: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json\n- R723_tube: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/R716-unmarked-outward-tube.json\n- common_moments: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-r716-complete-moment-integrals/report.json\n- legacy_centred: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R722-r716-complete-centred-moments/report.json\n- R723_centred: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-r716-complete-centred-moments/report.json\n- mesh_final: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-v1/report.json\n- mesh_packet: {work}/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-v1/report.json\n\nnormal/geometry与两类closed的完整ready由root拥有；本包精确引用其whole记录。公共矩producer须有自己的完整同点normal费用；legacy consumer再需002eb完整closed链，R723 consumer再需1782完整closed链。mesh final等待真正final13，packet等待真正完整immutable snapshot，二者都不因可变progress存在而可启动，也不以缺失的可选closed路径作门。各post预算耗尽或partial报告应保原失败/未付状态，不能为了联通后继改schema或预填proof。\n\n本件只给完整可复用step及其依赖，未排队。8个step出现位置中，公共producer有2个相同引用，唯一执行任务为7个；root按实际输入决定取哪些完整任务及顺序。所有科学raw、13成员checkpoint、快照、root盒、whole journals、NPY/PLY与预览都仅在公开Actions runner scratch。Git保存完整source、完整参数、来源与真实有界输出身份，不保存raw数组。\n\n## 9. 完整文本再生与状态边界\n\n完整Node再生器只读取本件固定whole父JSON、root21完整科学binding及完整参数文件，核其原字节，执行明确字符串/JSON构造并写出当前binding、四ready、此说明与完整delivery。它不导入或调用任何Python科学模块，不读取科学raw，不生成F/J/root/mesh/fee；它不作为solver前门或队列中的附加验证步骤。两种namespace映射、所有父whole文件与共享runtime记录均完整嵌入构造规范。可选--output-directory只控制完整文档输出地点，不变科学参数。\n\n调用协议：node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_moment_mesh_parameters.mjs --repo <完整仓库> --output-directory <独立完整文档输出目录>。程序可从原路径读取完整父文件；若路径内容版本不同，只按既定Git blob读取相同原字节，不按当前近似文件替代。每件生成文档必须小于100000字节，不以截断满足限制。\n\n本次实际做的是完整文本/JSON来源阅读、确定性参数构造及whole身份保护；没有运行该Node再生器、科学求解、AST、编译或数值试验。当前新run、input/ref、model、point、snapshot、final、normal/geometry/closed/moment/mesh输出和delta_E一律未填。prepared、已保护blob、源码中存在validator或完整ready均不等于实际结果。原19/20及全部未知peer责任仍在完整父件与当前binding中。\n";


const clone = value => JSON.parse(JSON.stringify(value));
const serial = value => JSON.stringify(value, null, 2) + "\n";
const equal = (a, b) => JSON.stringify(a) === JSON.stringify(b);
function requireValue(condition, message) { if (!condition) throw new Error(message); }
function selectorCount(value) { return Object.values(value || {}).reduce((sum, fields) => sum + Object.keys(fields).length, 0); }
function rename(value, spec, reverse = false) {
  let pairs = [[spec.old_namespace, spec.namespace], [spec.old_short_namespace, spec.short_namespace], ["bhalf-first", "bfiveeighths-first"]];
  if (reverse) pairs = pairs.map(([a, b]) => [b, a]);
  if (typeof value === "string") return pairs.reduce((s, [a, b]) => s.split(a).join(b), value);
  if (Array.isArray(value)) return value.map(x => rename(x, spec, reverse));
  if (value && typeof value === "object") return Object.fromEntries(Object.entries(value).map(([k, v]) => [rename(k, spec, reverse), rename(v, spec, reverse)]));
  return value;
}
function stepCounts(step) {
  return {argv_words: step.args.length, formal_selector_pairs: selectorCount(step.summary), live_selector_pairs: selectorCount(step.progress_summary)};
}
function currentSteps(kind, inputs, spec) {
  const steps = rename(inputs[kind].steps, spec);
  requireValue(equal(rename(steps, spec, true), inputs[kind].steps), "Full inverse parameter transformation changed parent " + kind);
  if (kind === "R723_R716") requireValue(equal(steps[0], rename(inputs.R716.steps[0], spec)), "The common 45ca producer must be the exact same complete step");
  if (kind.startsWith("mesh_")) {
    requireValue(steps[0].args.length === 32 && steps[1].args.length === 6, "Keep both complete mesh argv arrays");
    requireValue(!steps[0].args.includes("--closed-phase-report"), "Do not invent or remove an optional closed-report pair");
  }
  return steps;
}
function fileRecord(value) {
  return Object.fromEntries(["name", "path", "bytes", "sha256", "git_blob_sha", "fixed_publication_commit"].filter(k => value[k] !== undefined).map(k => [k, value[k]]));
}
function futureActual() {
  return {run_id: null, run_attempt: null, actual_complete_reference_inputs: null, reference_report_sha256: null,
    input_binding_sha256: null, model_identity_sha256: null, full_point_sha256: null, snapshot_identity_sha256: null,
    final_thirteen_member_checkpoint_sha256: null, scientific_complete_report_sha256: null,
    complete_normal_fee_report_sha256: null, continuous_geometry_report_sha256: null,
    legacy_closed_main_report_sha256: null, R723_closed_main_report_sha256: null,
    unmarked_outward_tube_report_sha256: null, complete_moment_report_sha256: null,
    centred_invariant_or_delta_E: null, mesh_report_sha256: null, mesh_or_time_refinement_results: null};
}
function paths(spec) {
  const w = "{work}/" + spec.namespace;
  return {scientific_report: w + "/report.json", scientific_command: w + "-command.json",
    normal: w + "-R722-normal-root-and-sixjet-fees-v1/report.json",
    geometry: w + "-R722-continuous-gram-curvature-support-v1/report.json",
    legacy_closed: w + "-R722-complete-closed-phase-grip-v1/report.json",
    legacy_tube: w + "-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
    R723_closed: w + "-R723-directional-closed-phase-grip-v1/report.json",
    R723_tube: w + "-R723-directional-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
    common_moments: w + "-R722-r716-complete-moment-integrals/report.json",
    legacy_centred: w + "-R722-r716-complete-centred-moments/report.json",
    R723_centred: w + "-R723-r716-complete-centred-moments/report.json",
    mesh_final: w + "-same-field-phase-mesh-final-v1/report.json",
    mesh_packet: w + "-same-field-phase-mesh-packet-v1/report.json"};
}
function makeBinding(inputs, spec) {
  const base = inputs.current_binding;
  const science = inputs.current_science.steps[0];
  requireValue(equal(base.current_complete_scientific_argv, science.args), "The common current scientific projection changed");
  requireValue(science.args.length === 157, "Retain all 157 current scientific argv words");
  requireValue(Object.keys(base.all_137_complete_current_source_roles).length === 137, "Retain all 137 source roles");
  requireValue(Object.keys(base.all_18_current_runtime_records).length === 18, "Retain all 18 runtime records");
  requireValue(equal(base.all_137_complete_current_source_roles, inputs.current_science_delivery.current_complete_source_role_registry), "The full current source registry differs");
  requireValue(equal(base.entire_external_peer_obligations, inputs.current_science.external_unregistered_peer_obligations), "Do not truncate external peer provenance");
  requireValue(base.current_seed_parameters.relative_boundary_total_length === "5/8" && base.current_seed_parameters.profile_delta === "1/32", "Keep the selected seed definition");
  requireValue(science.args[science.args.indexOf("--restoration-damping") + 1] === ".01" &&
    science.args[science.args.indexOf("--damping") + 1] === ".01", "Run20 damping is not a run21 input");
  const kinds = ["R716", "R723_R716", "mesh_final", "mesh_packet"];
  const plans = Object.fromEntries(kinds.map(k => [k, currentSteps(k, inputs, spec)]));
  const common = plans.R716[0];
  const scope723 = clone(inputs.sharing_binding20.R723_entire_physical_scope);
  scope723.seed_boundary_total_length_relative = "5/8";
  scope723.seed_profile_delta = "1/32";
  return {
    schema: "fixed-fejer-bfiveeighths-complete-moment-mesh-shared-parameter-binding-v1",
    repository: spec.repository, topic: spec.topic, prepared_utc: spec.prepared_utc,
    executed: false, queued: false, runtime_sources_rewritten: [], scientific_calls: 0,
    current_namespace: spec.namespace,
    full_current_normal_closed_scientific_binding: spec.parents.current_binding,
    full_current_normal_closed_parameter_delivery: spec.parents.current_post_delivery,
    complete_current_science_parameter_file: spec.parents.current_science,
    complete_current_pure_parameter_file: spec.parents.current_pure,
    complete_current_scientific_parameter_delivery: spec.parents.current_science_delivery,
    current_scientific_projection: {
      complete_argv: clone(science.args), source_role_count: 137, runtime_file_count: 18,
      all_137_source_records_json_pointer: "/all_137_complete_current_source_roles",
      all_18_runtime_records_json_pointer: "/all_18_current_runtime_records",
      exact_container: spec.parents.current_binding,
      actual_driver_sha256: "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      actual_reader_sha256: "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49",
      actual_launcher_sha256: "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
      all_original_120_source_path_and_SHA_pairs_preserved: true,
      complete_science_formal_projection_pairs: 458, complete_pure_formal_projection_pairs: 445, complete_science_live_projection_pairs: 48,
      complete_projection_origins: {science: spec.parents.current_science, pure: spec.parents.current_pure},
      planned_seed_parameters: clone(base.current_seed_parameters), planned_initial_damping: clone(base.current_initial_damping),
      full_delta_from_original_run19: clone(base.current_complete_scientific_parameter_delta),
      maker_and_reference_numerical_parameters_changed: false,
      fixed_g_is_shared_but_supported_seed_model_and_physical_field_are_new: true,
      no_previous_point_root_branch_certificate_or_accepted_state_inherited: true
    },
    full_external_peer_obligations: clone(base.entire_external_peer_obligations),
    full_external_peer_status: base.full_external_peer_status,
    new_verified_external_peer_records: clone(base.new_verified_external_peer_records),
    full_original_five_supported_pending_CLI_pairs_in_the_complete_current_argv: true,
    unknown_complete_typed_histories_not_replaced_with_empty: true,
    original_full_parameter_history: Object.fromEntries(kinds.map(k => [k, {
      complete_file: spec.parents[k], whole_original_metadata_json_pointer: "",
      every_original_top_level_key: Object.keys(inputs[k]), all_original_nested_fields_preserved_in_whole_file: true,
      original_steps_json_pointer: "/steps", current_steps_file: spec.topic + "/" + spec.paths[k]
    }])),
    storage_sharing_method_parent: {full_binding: spec.parents.sharing_binding20, full_delivery: spec.parents.sharing_delivery20,
      old_run20_actual_fields_damping_and_namespace_are_historical_only: true},
    complete_metadata_recovery: {
      rule: "All original parent objects, including every top-level and nested provenance field, remain in their exact whole files. The current ready keeps complete executable step objects. This shared binding and the full current 033bc binding provide the current scientific projection; historical files are not relabelled as current fields.",
      no_parent_parameter_source_or_metadata_field_deleted: true,
      original_scientific_runtime_files_and_history_are_immutable: true,
      whole_references_are_storage_reuse_not_reduced_scientific_parameters: true,
      each_current_step_inverse_namespace_transform_recovers_the_entire_original_parent_step: true,
      transform_pairs: [[spec.old_namespace, spec.namespace], [spec.old_short_namespace, spec.short_namespace], ["bhalf-first", "bfiveeighths-first"]]
    },
    complete_reused_runtime_source_records: clone(spec.runtime_sources),
    complete_current_dependency_ready_files: inputs.current_post_delivery.parameter_stages.map(s => ({
      complete_file: fileRecord(s.file), step_id: s.id, script: s.script, argv_words: s.argument_count, formal_selector_pairs: s.formal_selector_count
    })),
    current_actual_input_and_output_paths: paths(spec),
    complete_moment_contract: {
      exact_phi_over_pi: ["0", "2"], exact_radial_affine_in_S: [["0", "0"], ["1", "0"]],
      all_original_normal_stages: 32, all_upstream_full_angle_cells: 1024,
      all_original_radial_cells: 922, all_exact_support_profile_control_cuts_and_scalar_tail_retained: true,
      twelve_channels: clone(inputs.R716.all_twelve_integral_channels),
      original_seconds: 600, maximum_angle_blocks: 0,
      producer_argv_words: 10, producer_formal_selector_pairs: 34,
      legacy_consumer_argv_words: 8, legacy_consumer_formal_selector_pairs: 60,
      R723_consumer_argv_words: 8, R723_consumer_formal_selector_pairs: 65,
      original_60_R716_selector_pairs_retained_in_R723_consumer: true,
      physical_centred_comparison_times: ["0", "1/2", "1"],
      general_full_centroid_and_mixed_tensor_algebra_retained_without_half_turn: true,
      simplified_compensation_requires_actual_all32_signed_half_turn_root_inclusion: true,
      whole_same_point_normal_mean_R722_domain_and_full_stream_binding_required: true,
      any_missing_complete_domain_keeps_whole_domain_moments_null: true,
      conditional_flux_is_not_an_embedded_volume_certificate: true,
      delta_E_requires_complete_outward_body_independent_unmarked_tube_positive_volume_and_nonzero_centred_invariant: true,
      legacy_d0fe_consumes_only_its_exact_002eb_complete_main_and_sidecar_chain: true,
      compatible_3c0d_dispatches_actual_1782_R723_main_and_retains_the_exact_legacy_branch: true,
      R723_original_eight_beta_claims_stay_false: true,
      R722_mean_existence_or_R718_holding_distance_does_not_pay_R716: true,
      complete_existing_R723_independent_contract: clone(inputs.sharing_binding20.R716_entire_independent_consumption_contract)
    },
    complete_R723_dependency_physical_scope: scope723,
    R723_closed_plan_is_owned_by_the_current_root_delivery_not_duplicated_here: true,
    common_producer_execution: {
      whole_step: clone(common), id: common.id,
      same_complete_step_in_legacy_and_R723_readies: true, total_executions_if_both_consumers_requested: 1,
      producer_already_queued_or_returned_means_take_only_the_second_R723_step: true,
      do_not_deduplicate_different_point_or_report_inputs_by_name: true,
      require_complete_step_equality_before_reusing_a_queued_step: true,
      no_automatic_queue_or_future_result_is_created: true
    },
    complete_mesh_scope: clone(inputs.mesh_final.complete_field_scope),
    all_mesh_parameters: clone(inputs.mesh_final.full_mesh_parameters),
    all_mesh_output_boundaries: clone(inputs.mesh_final.output_boundary),
    planned_mesh_counts_per_selected_point: {spatial_levels: 3, physical_times: 5, complete_scientific_meshes: 15, standalone_rendering_previews: 5, complete_time_partition_counts: [4, 8, 16]},
    two_mesh_point_modes: {
      final: "The actual complete scientific report and genuine full thirteen-member final checkpoint are mandatory; no initial or mutable progress substitution.",
      packet: "A genuinely captured complete-required-angle immutable snapshot is mandatory. It may be a trial/cache point; no acceptance or final success is inferred.",
      every_mesh_and_physical_t_uses_one_complete_selected_point_and_fixed_g: true,
      each_branch_has_complete_32_word_mesh_and_6_word_pure_argv: true,
      mesh_formal_selector_pairs: 110, pure_formal_selector_pairs: 58, live_selector_pairs: 48
    },
    exact_optional_mesh_evidence_contract: {
      actual_input_source: clone(inputs.mesh_final.complete_runtime_source_records[0]),
      these_complete_32_word_plans_contain_closed_phase_report_argument: false,
      no_argument_pair_was_removed_from_the_parent: true,
      optional_legacy_metadata: rename(inputs.mesh_final.optional_complete_closed_phase_evidence, spec),
      no_path_supplied_means_no_optional_accurate_closed_evidence_claim: true,
      supplied_path_missing_incomplete_or_wrong_source_is_rejected: true,
      existing_2ef3_optional_branch_accepts_002eb_only_not_1782_R723: true,
      no_R723_path_inserted_into_the_old_mesh_source: true,
      any_future_R723_compatible_mesh_source_is_a_separate_explicit_source_family: true,
      absence_of_optional_closed_proof_does_not_remove_any_numeric_mesh_domain_or_budget: true,
      working_mesh_errors_are_not_paid_by_any_accurate_field_certificate: true
    },
    conditional_step_order: {
      normal_and_geometry_and_each_closed_report_must_actually_satisfy_their_consumers: true,
      producer_runs_after_complete_same_point_normal_fees: true,
      legacy_consumer_uses_shared_moments_and_002eb_complete_closed_chain: true,
      R723_consumer_uses_shared_moments_and_1782_complete_closed_chain: true,
      mesh_final_uses_actual_complete_final_and_mesh_packet_uses_actual_complete_snapshot: true,
      mesh_does_not_wait_for_absent_optional_closed_evidence: true,
      no_partial_math_progress_is_a_complete_field_or_fee_input: true,
      all_runnable_step_objects_are_retained_but_this_package_does_not_enqueue_them: true
    },
    future_actual: futureActual(),
    source_reproducer_path: spec.topic + "/" + spec.paths.reproducer,
    no_scientific_AST_compile_fixture_benchmark_or_new_admission_gate: true,
    no_ref_queue_job_or_running_parameter_mutation: true,
    raw_arrays_checkpoints_root_packets_journals_meshes_and_previews_only_public_runner_scratch: true
  };
}
function makeReady(kind, bindingRecord, inputs, spec) {
  const steps = currentSteps(kind, inputs, spec);
  const mesh = kind.startsWith("mesh_");
  const names = {R716: "legacy-R722-R716", R723_R716: "R723-compatible-R716", mesh_final: "same-field-phase-mesh-final", mesh_packet: "same-field-phase-mesh-packet"};
  const value = {
    schema: "fixed-fejer-bfiveeighths-complete-" + names[kind] + "-parameters-v1",
    prepared_utc: spec.prepared_utc, executed: false, queued: false,
    scientific_execution_permitted_only_in_public_Actions: true,
    complete_current_parameter_binding: fileRecord(bindingRecord),
    full_current_scientific_normal_closed_binding: spec.parents.current_binding,
    complete_immediate_parameter_parent: spec.parents[kind],
    complete_original_parent_metadata_retained_by_exact_whole_file: true,
    no_parent_top_level_or_nested_parameter_history_or_source_field_deleted: true,
    current_namespace: spec.namespace,
    planned_seed_parameters: clone(inputs.current_binding.current_seed_parameters),
    planned_initial_damping: clone(inputs.current_binding.current_initial_damping),
    complete_parent_steps_json_pointer: "/steps",
    complete_argument_and_namespace_correspondence: steps.map((s, i) => ({
      original_step_id: inputs[kind].steps[i].id, current_step_id: s.id,
      complete_original_argument_word_count: inputs[kind].steps[i].args.length,
      complete_current_counts: stepCounts(s),
      complete_changed_argument_words: s.args.flatMap((v, j) => v === inputs[kind].steps[i].args[j] ? [] : [{index: j, before: inputs[kind].steps[i].args[j], after: v}]),
      all_parent_step_fields_inverse_recoverable_by_only_declared_namespace_map: true,
      original_scope_and_every_selector_output_cleanup_or_retention_field_preserved: true
    })),
    no_runtime_source_or_numerical_domain_or_budget_changed: true,
    no_future_actual_point_model_reference_snapshot_or_fees_prepopulated: true,
    future_actual: futureActual(),
    complete_reproducer_path: spec.topic + "/" + spec.paths.reproducer,
    steps
  };
  if (!mesh) {
    value.common_complete_producer_step_id = steps[0].id;
    value.producer_source_sha256 = "45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8";
    value.producer_original_seconds = 600;
    value.maximum_angle_blocks = 0;
    value.if_identical_producer_already_queued_or_returned_execute_only_second_step = true;
    value.two_consumer_modes_share_one_actual_producer_execution = true;
    value.complete_required_closed_plan = fileRecord(inputs.current_post_delivery.parameter_stages.find(s =>
      kind === "R716" ? s.script.endsWith("/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py") :
      s.script.endsWith("/fixed_fejer_R723_directional_closed_phase_grip_evidence.py")).file);
    value.consumer_source_sha256 = kind === "R716" ? "d0fe262ba0208562ed5578a17b22847659a5e747b601441b65b2e73d50462e63" :
      "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b";
    value.R723_original_eight_beta_claims_are_not_paid_by_this_plan = true;
  } else {
    value.point_source_mode = kind === "mesh_final" ? "final" : "packet";
    value.full_spatial_levels_times_and_time_refinement = clone(inputs[kind].full_mesh_parameters);
    value.optional_closed_phase_report_argument_present = false;
    value.original_parent_already_omitted_this_optional_argument = true;
    value.no_parameter_pair_deleted_and_no_optional_R723_path_added = true;
    value.source_remains_original_2ef3_b399_8197_family = true;
    value.full_15_scientific_meshes_and_five_complete_previews_retained = true;
    value.mesh_samples_do_not_claim_continuous_geometry_or_certificates = true;
  }
  return value;
}


function makeManifest(inputs, spec, records) {
  const kinds = ["R716", "R723_R716", "mesh_final", "mesh_packet"];
  const plans = Object.fromEntries(kinds.map(k => [k, currentSteps(k, inputs, spec)]));
  const unique = [["R716",0], ["R716",1], ["R723_R716",1], ["mesh_final",0], ["mesh_final",1], ["mesh_packet",0], ["mesh_packet",1]];
  return {
    schema:"fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery-v1",
    repository:spec.repository,topic:spec.topic,prepared_utc:spec.prepared_utc,
    status:"complete-source-and-parameter-documents-prepared-not-executed-or-queued",
    current_namespace:spec.namespace,runtime_sources_rewritten:[],refs_or_queues_modified:false,
    complete_current_normal_closed_scientific_binding:spec.parents.current_binding,
    complete_current_normal_closed_delivery:spec.parents.current_post_delivery,
    complete_current_science_parameter_file:spec.parents.current_science,
    complete_current_pure_parameter_file:spec.parents.current_pure,
    complete_current_scientific_delivery:spec.parents.current_science_delivery,
    artifacts:Object.values(records).map(fileRecord),
    artifact_count_excluding_this_manifest:Object.keys(records).length,
    artifact_bytes_excluding_this_manifest:Object.values(records).reduce((n,r)=>n+r.bytes,0),
    largest_new_complete_file_bytes:Math.max(...Object.values(records).map(r=>r.bytes)),
    all_complete_new_files_below_100000_bytes:true,
    exact_full_original_parameter_parents:spec.parents,
    complete_shared_runtime_files:clone(spec.runtime_sources),
    current_scientific_source_role_count:137,current_scientific_runtime_file_count:18,
    science_argv_words:157,science_formal_selector_pairs:458,pure_argv_words:7,pure_formal_selector_pairs:445,science_live_selector_pairs:48,
    full_137_and_18_records_are_in_the_exact_shared_current_binding_not_truncated_summaries:true,
    all_original120_source_pairs_and_all_supported_CLI_and_external_peer_responsibilities_retained:true,
    planned_seed_parameters:clone(inputs.current_binding.current_seed_parameters),
    planned_initial_damping:clone(inputs.current_binding.current_initial_damping),
    current_post_plans:kinds.map(k=>({role:k,complete_file:fileRecord(records[k]),
      steps:plans[k].map((s,i)=>({index:i,id:s.id,script:s.script,counts:stepCounts(s),
        full_arguments_in_exact_file:true,all_output_selector_scope_cleanup_retention_and_parent_fields_preserved:true}))})),
    common_producer:{
      source_sha256:"45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8",
      step_id:plans.R716[0].id,exact_same_complete_object_in_both_ready_files:true,
      exact_ready_occurrences:[{file:fileRecord(records.R716),step_index:0},{file:fileRecord(records.R723_R716),step_index:0}],
      execution_count_if_both_consumers_are_requested:1,seconds:600,maximum_angle_blocks:0
    },
    unique_complete_step_locations:unique.map(([k,i])=>({file:fileRecord(records[k]),step_index:i,id:plans[k][i].id})),
    unique_step_count:7,total_step_occurrences_in_all_ready_files:8,
    R723_closed_dependency_is_root_owned_and_not_duplicated:clone(inputs.current_post_delivery.parameter_stages.find(s=>s.script.endsWith("/fixed_fejer_R723_directional_closed_phase_grip_evidence.py"))),
    original_002eb_closed_dependency_is_root_owned_and_not_duplicated:clone(inputs.current_post_delivery.parameter_stages.find(s=>s.script.endsWith("/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py"))),
    runtime_dispatch_boundary:{
      common_producer:"45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8",
      legacy_consumer:"d0fe262ba0208562ed5578a17b22847659a5e747b601441b65b2e73d50462e63",
      R723_compatible_consumer:"3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
      legacy_closed:"002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
      R723_closed:"1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
      original_mesh_input:"2ef316b9075f14af66e1deda235c4df9319a0c29cfeddb10a40130712a12d76c",
      no_R723_optional_report_inserted_into_original_mesh_source:true
    },
    mesh_modes:{final_argv:32,packet_argv:32,pure_argv:6,formal_fields:110,pure_fields:58,live_fields:48,
      original_parent_argv_already_had_no_closed_phase_report_flag:true,no_pair_removed:true,
      all_spatial_levels:3,all_physical_times:5,complete_scientific_meshes:15,complete_rendering_previews:5,time_refinement:[4,8,16],
      final_requires_real_complete_report_and_final13:true,packet_requires_real_complete_required_angle_snapshot:true,
      both_modes_use_one_same_field_for_all_meshes_and_times:true,mesh_samples_are_not_continuous_certificates:true},
    metadata_storage_reuse:{
      whole_original_parent_top_level_and_nested_metadata_preserved_by_exact_file_references:true,
      complete_current_executable_step_objects_present_in_every_ready:true,
      original_scientific_or_post_numeric_parameters_or_domains_not_removed:true,
      current_137_source_registry_and_157_argv_are_bound_to_the_complete_current_root_file:true,
      template_run20_damping_or_actual_field_not_inherited:true
    },
    future_actual:futureActual(),
    full_text_reproduction:{
      complete_source:fileRecord(records.reproducer),
      invocation:["node",spec.topic+"/"+spec.paths.reproducer,"--repo","<complete-repository>","--output-directory","<independent-document-output-directory>"],
      reads_only_complete_fixed_metadata_and_parameter_parents:true,
      no_scientific_module_AST_compile_fixture_benchmark_or_ref_queue_operation:true,
      not_added_as_a_solver_gate_or_queue_step:true,
      source_constructed_as_text_and_not_executed_in_this_session:true
    },
    all_raw_arrays_packets_checkpoint_words_fees_and_meshes_remain_runner_only:true,
    actual_step_order_waits_for_real_input_completeness_not_future_hashes:true
  };
}


function sha256(bytes) { return createHash("sha256").update(bytes).digest("hex"); }
function blobSHA(bytes) {
  return createHash("sha1").update(Buffer.from("blob " + bytes.length + "\0")).update(bytes).digest("hex");
}
function recordFor(role, text) {
  const bytes = Buffer.from(text, "utf8");
  if (bytes.length >= 100000) throw new Error("Refuse truncation: complete new file is at least 100000 bytes: " + role);
  const path = SPEC.topic + "/" + SPEC.paths[role];
  return {name: path.split("/").pop(), path, bytes: bytes.length, sha256: sha256(bytes), git_blob_sha: blobSHA(bytes)};
}
function parseArguments(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    if (!["--repo", "--output-directory"].includes(key) || !argv[i + 1]) throw new Error("Usage: --repo <complete-repository> --output-directory <independent-document-output-directory>");
    if (out[key]) throw new Error("Do not repeat " + key);
    out[key] = argv[i + 1];
  }
  if (!out["--repo"] || !out["--output-directory"]) throw new Error("Both --repo and --output-directory are required");
  return {repo: resolve(out["--repo"]), output: resolve(out["--output-directory"])};
}
function readWholeParent(record, repo) {
  if (record.bytes >= 100000 || !/^[0-9a-f]{64}$/.test(record.sha256) || !/^[0-9a-f]{40}$/.test(record.git_blob_sha)) {
    throw new Error("This complete metadata constructor only reads the declared sub-100000-byte whole parents");
  }
  let bytes = null;
  try { bytes = readFileSync(resolve(repo, record.path)); } catch (_) {}
  if (bytes === null || bytes.length !== record.bytes || sha256(bytes) !== record.sha256 || blobSHA(bytes) !== record.git_blob_sha) {
    bytes = execFileSync("git", ["-C", repo, "cat-file", "blob", record.git_blob_sha], {maxBuffer: 100000, stdio: ["ignore", "pipe", "pipe"]});
  }
  if (bytes.length !== record.bytes || sha256(bytes) !== record.sha256 || blobSHA(bytes) !== record.git_blob_sha) {
    throw new Error("The full exact metadata parent is unavailable: " + record.path);
  }
  return JSON.parse(bytes.toString("utf8"));
}
function writeWhole(path, text, output) {
  const destination = resolve(output, path);
  const bytes = Buffer.from(text, "utf8");
  if (existsSync(destination)) {
    if (!readFileSync(destination).equals(bytes)) throw new Error("Do not overwrite a different existing document: " + destination);
    return;
  }
  mkdirSync(dirname(destination), {recursive: true});
  writeFileSync(destination, bytes, {flag: "wx"});
}
function main() {
  const args = parseArguments(process.argv.slice(2));
  const inputs = Object.fromEntries(Object.entries(SPEC.parents).map(([k, r]) => [k, readWholeParent(r, args.repo)]));
  const texts = {};
  const records = {};
  texts.binding = serial(makeBinding(inputs, SPEC));
  records.binding = recordFor("binding", texts.binding);
  for (const kind of ["R716", "R723_R716", "mesh_final", "mesh_packet"]) {
    texts[kind] = serial(makeReady(kind, records.binding, inputs, SPEC));
    records[kind] = recordFor(kind, texts[kind]);
  }
  texts.note = NOTE_TEXT;
  records.note = recordFor("note", texts.note);
  texts.reproducer = readFileSync(fileURLToPath(import.meta.url), "utf8");
  records.reproducer = recordFor("reproducer", texts.reproducer);
  texts.manifest = serial(makeManifest(inputs, SPEC, records));
  const manifestRecord = recordFor("manifest", texts.manifest);
  for (const [kind, text] of Object.entries(texts)) writeWhole(SPEC.paths[kind], text, args.output);
  process.stdout.write(serial({schema: "complete-parameter-document-reproduction-result-v1",
    scientific_calls: 0, refs_or_queues_modified: false, complete_files: [...Object.values(records), manifestRecord]}));
}
main();

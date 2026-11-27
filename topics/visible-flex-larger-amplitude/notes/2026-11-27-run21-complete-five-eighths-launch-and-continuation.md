# 第21轮：同g b/S=5/8 完整独立科学启动与继续记录

准备时间：2026-11-27 23:32:40 UTC。会话 Astra-larger-e4e2a2bf-20261126。本文最初是完整启动源/请求准备记录，官方run/job和每个实际步骤须在真实启动与返回后追加，不能由请求推出。已刊6件全参数在 `dd02e95f7ee748618e0657ac42c8e69d056a3587`；本文和启动总表不改其prepared历史语义。

## 1. 明确选择与当前目标

[完整宽度分析](2026-11-27-supported-seed-five-eighths-three-quarters-and-existing-geometry-observations.md)已刊。第19初有限reach与distance_plus比bquarter改善但仍为正，第一次恢复也没有使其可行。这里继续选择较温和的下一width-only输入 b/S=5/8、delta=1/32；两项初始阻尼仍.01，直接与19比较宽度，未带入20的mu.001。

唯一数值科学argv变化是19父argv113的1/2→5/8；argv71输出namespace改为 fixed-fejer-meridian-batched-bfiveeighths-first。原固定g、完整Fejér/R690标量和图、M160/J923/N2048、完整32stage、全变量、范数、192原active选择及额外typed永久并集、所有原容差/谱参数、metric1方向/maxiter16、恢复4方向/maxiter64、15回溯和全部mean/normal/root预算完整保。完整157词和7词pure可逐字见总表与原ready；此处举例不代原全参。

新每个端层5S/32、每个中央S/8；精确支持定义合法不代实际mean/r/λ/frame/root存在。端层显式4/5与中央(3/2)λ比是条件尺度，不预测真实principal curvature或通过。先前所有R709/R722/R723责任不变，不加独立前门。

## 2. 完整源与两步必要输入

[完整参数总表](../computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json)保全部137角色、18current runtime、原120source pairs和所有历史。运行体不改：10fa driver、8027 reader、f600 launcher、5730 geometry、9104 binding、d892 input。

maker89cc与reference e717本身没有width参数。它们按原全6/26词命令在新runner真实重建固定目标输入，原全部output、summary和cleanup对象保。不能把科学width变化说成参考目标变化，也不从19/20复制raw或旧report/point/checkpoint。

新完整初队列有3个whole steps：

```json
[
  {
    "id": "prepare-complete-fixed-fejer-r690-inputs-20261127",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
    "args": [
      "--repo",
      "{repo}",
      "--outdir",
      "{work}/fixed-fejer-r690-inputs",
      "--panels",
      "128"
    ],
    "outputs": [
      "fixed-fejer-r690-inputs/report.json",
      "fixed-fejer-r690-inputs/fixed-reference-input.npz",
      "fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "fixed-fejer-r690-inputs/fixed-scalar-input.json"
    ]
  },
  {
    "id": "prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run21",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
    "args": [
      "--repo",
      "{repo}",
      "--fixed-input",
      "{work}/fixed-fejer-r690-inputs/fixed-reference-input.npz",
      "--fixed-input-report",
      "{work}/fixed-fejer-r690-inputs/report.json",
      "--node-report",
      "{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "--scalar-input",
      "{work}/fixed-fejer-r690-inputs/fixed-scalar-input.json",
      "--manifest",
      "{repo}/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json",
      "--outdir",
      "{work}/fixed-fejer-reference",
      "--angles",
      "2048",
      "--seed-integration-order",
      "8",
      "--panels",
      "128",
      "--scalar-leaf-count",
      "2218",
      "--scalar-integral-tolerance",
      "1e-18",
      "--scalar-tail-cutoff",
      "1/8"
    ],
    "parent_bundle": null,
    "outputs": [
      "fixed-fejer-reference/report.json",
      "fixed-fejer-reference/reference.npz",
      "fixed-fejer-reference/observations.npz",
      "fixed-fejer-reference/locations.json",
      "fixed-fejer-reference/supplied-location-provenance.json",
      "fixed-fejer-reference/fixed-target-definition.json",
      "fixed-fejer-reference/material-envelope-carrier-binding.json"
    ]
  },
  {
    "id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-20261127",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py",
    "args": [
      "--repo",
      "{repo}",
      "--reference-bundle",
      "{work}/fixed-fejer-reference/reference.npz",
      "--preparation-report",
      "{work}/fixed-fejer-reference/report.json",
      "--carrier",
      "{work}/fixed-fejer-reference/observations.npz",
      "--node-report",
      "{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "--scalar-input",
      "{work}/fixed-fejer-r690-inputs/fixed-scalar-input.json",
      "--angles",
      "2048",
      "--stage-block",
      "64",
      "--angle-block",
      "8",
      "--integration-order",
      "8",
      "--norm-kind",
      "jet-sum",
      "--radial-norm-length",
      ".05",
      "--angular-transition",
      "24",
      "--torch-threads",
      "4",
      "--damping",
      ".01",
      "--directions",
      "1",
      "--maxiter",
      "16",
      "--restoration-directions",
      "4",
      "--restoration-damping",
      ".01",
      "--restoration-maxiter",
      "64",
      "--line-trials",
      "15",
      "--active-rows",
      "192",
      "--qp-atol",
      "0",
      "--qp-rtol",
      "1e-6",
      "--reach-ratio",
      ".03",
      "--reach-safety-factor",
      ".992",
      "--active-band",
      ".025",
      "--marked-diameter-budget",
      "4.2",
      "--witness-lower-budget",
      ".9",
      "--amplitude-height-floor",
      "1.01",
      "--spectral-p",
      "4",
      "--spectral-epsilon",
      ".001",
      "--spectral-scale",
      ".05",
      "--legacy-fraction",
      ".5",
      "--target",
      "1e-9",
      "--outdir",
      "{work}/fixed-fejer-meridian-batched-bfiveeighths-first",
      "--panels",
      "128",
      "--endpoint-bubble-1-left",
      "1/32",
      "--endpoint-bubble-1-middle",
      "1/4",
      "--endpoint-bubble-1-right",
      "15/32",
      "--endpoint-bubble-2-left",
      "17/32",
      "--endpoint-bubble-2-middle",
      "3/4",
      "--endpoint-bubble-2-right",
      "31/32",
      "--endpoint-root-tolerance",
      "2e-12",
      "--endpoint-root-iterations",
      "24",
      "--endpoint-root-backtracks",
      "18",
      "--endpoint-root-armijo",
      "1e-4",
      "--moment-definition-sha256",
      "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
      "--moment-input",
      "{repo}/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
      "--moment-input-sha256",
      "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
      "--endpoint-control-radius",
      "2",
      "--gamma-left",
      "1/16",
      "--gamma-middle",
      "1/8",
      "--gamma-right",
      "3/16",
      "--moment-input-binding",
      "supported-smooth-triangle-reference",
      "--normal-stages",
      "32",
      "--seed-boundary-total-length",
      "5/8",
      "--seed-profile-delta",
      "1/32",
      "--seed-radial-quadrature-order",
      "8",
      "--seed-profile-quadrature-order",
      "16",
      "--seed-mean-maxiter",
      "128",
      "--seed-mean-tolerance",
      "2e-12",
      "--seed-mean-backtracks",
      "24",
      "--seed-mean-armijo",
      "1e-4",
      "--seed-scalar-iterations",
      "64",
      "--manifest",
      "{work}/fixed-fejer-reference/locations.json",
      "--material-envelope-binding",
      "{work}/fixed-fejer-reference/material-envelope-carrier-binding.json",
      "--envelope-near-active-rows",
      "32",
      "--independent-envelope-branch",
      "--pending-parallel-envelope-run",
      "45909290354/1",
      "--pending-parallel-envelope-source",
      "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
      "--pending-parallel-envelope-run",
      "45929088658/1",
      "--pending-parallel-envelope-source",
      "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
      "--pending-parallel-envelope-run",
      "45943410994/1",
      "--pending-parallel-envelope-source",
      "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
      "--pending-parallel-envelope-run",
      "45972294636/1",
      "--pending-parallel-envelope-source",
      "45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
      "--pending-parallel-envelope-run",
      "46011377225/1",
      "--pending-parallel-envelope-source",
      "46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
    ],
    "parent_bundle": "fixed-fejer-reference/reference.npz",
    "outputs": [
      "fixed-fejer-meridian-batched-bfiveeighths-first/report.json",
      "fixed-fejer-meridian-batched-bfiveeighths-first-command.json"
    ]
  }
]
```

完整summary和progress映射在原whole队列，不是本段预览省掉的字段。其字节数73309小于原95KB上限。科学与pure同时排入的whole envelope为117338B pretty / 104110B compact，不能削字段挤入。科学自然返回后，保全所有完整实际对象与身份，再卸下真正已返steps、整接原7词/445选择pure及后继。

## 3. 控制器与完整旧请求

本controller从20原完整19,984B源只换四个H槽文字；workflow只换请求文件名、并发组、controller路径和说明标签。原350分钟job、20000秒controller、finish_when_done=false、依赖版本、四个BLAS线程变量、部分克隆、无持久凭据、逐实际source checkout、低频只读小progress、至少每小时真pull/只读双README新diff、NFF rebase普通推循环与所有保存界限均不变。时长和iteration_limit不作为课题完成。

原19启动请求27133B完整保在固定543cf；所有本次修改过的旧完整字段在新request的 complete_original_run19_metadata_changed_for_current_request 全保，包含原请求中旧1/4或旧source说明的历史原字，不能把它误认成当前参数。当前正文已准确写5/8和10fa/8027/f600。controller/workflow的完整父则是20固定85cd。

原五个受支持pending CLI对与原六external全部保，再把真实官方19/20列为两个external未知历史责任。它们未加入不支持的PARENT_FAMILIES，未假造typed迁移；其实际accepted/未知final也不作本轮输入。新21无需等旧19/20科学返回才开始自己的两个必要输入和完整科学。

## 4. 启动材料完整身份

| 文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel21_compact_metadata.py | 19984 | e754e7927e97de3d83efcb3be1752ce25de7f6d190b02651c462a3463e39ae6d | 442043546abd7f0750b88e3df1f3bff8f3b45126 |
| .github/workflows/visible-larger-20261127-parallel21.yml | 2227 | 335311afa9030fa68ccdb8e42e1621a3c5f65f7b802ca9f7bd2eb94eb09b921b | ced5b49317820cb903777da90c610b533a36c376 |
| topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-21.json | 73309 | c83981e0ed294593207c780a863f9328d120103929cbd58f58810e42f3af9d6c | 77de38c0c993b4c84487a16557a11c564c83b9ed |
| topics/visible-flex-larger-amplitude/computations/resume-20261127-actions-request-21.json | 51519 | 9599d90d59db0e3398300645e5c16d9ca2a4c62f310ece96b476ea0f3744182c | a7c0e4e77e3a9764e62031a7d713d0ea8d456d80 |
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-launch-delivery.json | 20538 | af44e3a65d6ee1fe837fd912efa754cef12a7b13e9228a84a003fc5c61052e2e | 8c820da008fe3e41526eb420adae58ccf870e7a3 |

workflow原未存在的判断来自完整未截断Git tree，非只能返回1000项的contents目录列表；完整HEAD/tree/count在总表，最终发布还要fresh tree避免撞同名workflow。此为唯一新21请求，启动后不改它以免重触发同一workflow；后续通过原followup whole step排入。

## 5. 后续真实材料与未完成责任

完整科学报告及全13final未实际取得；费用可用的完整source-bound required-angle immutable snapshot与final是原不同接口，绝不能拿mutable progress顶替。normal续费须用原实际来源绝对目录/报告/快照绑定，完整后再生成绑定其whole SHA的geometry；R723与R716按各自完整主副件和独立unmarked条件读取。此前partial下游不能原地改身份；若发生，保存旧件另排新鲜outdir。具体真实路径须等本轮原命令与record产生后使用，不在此猜runner路径。

所有原五t、三级空间/频率/时间、完整mesh与同g同参数误差仍待真正计算；raw只runner，Git保完整源码、全部参数、紧凑实际证据与恢复责任。当前未达README完成标准，继续真正求解，不以准备、一次有限接受、某轮完成或时限收尾。

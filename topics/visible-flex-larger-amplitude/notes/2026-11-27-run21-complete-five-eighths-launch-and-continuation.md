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

## 6. 2026-11-27 23:48:59 UTC — 官方实际启动

完整启动实际提交 `95ae5c2399664bed1b9597611b7385cb4e8d6d5e`；前一次普通ref更新碰到并行提交，freshHEAD完整合并后成功，无force也不冒终端pull。官方[run46084442413/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46084442413) 于2026-11-27T23:47:39Z实际created/started，job140790598810。以下为第一次真实查询返回的完整run与jobs对象，保所有原字段；查询来源分别为该启动head的actions/runs和官方run jobs接口。此时status=in_progress/conclusion=null，checkout/setup已success，依赖安装in_progress，科学步骤pending。不能把这些状态填成实际科学input/source/model/point或完成；后续状态由控制器与真实返回另记。

### 首次官方run完整对象

```json
{
  "id": 46084442413,
  "name": "Visible larger amplitude complete five-eighths supported seed 20261127 21",
  "node_id": "WFR_kwLOVt5L2s8AAAAKutjJLQ",
  "head_branch": "main",
  "head_sha": "95ae5c2399664bed1b9597611b7385cb4e8d6d5e",
  "path": ".github/workflows/visible-larger-20261127-parallel21.yml",
  "display_title": "Launch complete five-eighths supported-seed branch with unchanged fix…",
  "run_number": 1,
  "event": "push",
  "status": "in_progress",
  "conclusion": null,
  "workflow_id": 433258281,
  "check_suite_id": 124672751472,
  "check_suite_node_id": "CS_kwDOVt5L2s8AAAAdBxM3cA",
  "url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413",
  "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46084442413",
  "pull_requests": [],
  "created_at": "2026-11-27T23:47:39Z",
  "updated_at": "2026-11-27T23:47:41Z",
  "actor": {
    "login": "Rogerhu12",
    "id": 199914264,
    "node_id": "U_kgDOC-pzGA",
    "avatar_url": "https://avatars.githubusercontent.com/u/199914264?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/Rogerhu12",
    "html_url": "https://github.com/Rogerhu12",
    "followers_url": "https://api.github.com/users/Rogerhu12/followers",
    "following_url": "https://api.github.com/users/Rogerhu12/following{/other_user}",
    "gists_url": "https://api.github.com/users/Rogerhu12/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/Rogerhu12/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/Rogerhu12/subscriptions",
    "organizations_url": "https://api.github.com/users/Rogerhu12/orgs",
    "repos_url": "https://api.github.com/users/Rogerhu12/repos",
    "events_url": "https://api.github.com/users/Rogerhu12/events{/privacy}",
    "received_events_url": "https://api.github.com/users/Rogerhu12/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": false
  },
  "run_attempt": 1,
  "referenced_workflows": [],
  "run_started_at": "2026-11-27T23:47:39Z",
  "triggering_actor": {
    "login": "Rogerhu12",
    "id": 199914264,
    "node_id": "U_kgDOC-pzGA",
    "avatar_url": "https://avatars.githubusercontent.com/u/199914264?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/Rogerhu12",
    "html_url": "https://github.com/Rogerhu12",
    "followers_url": "https://api.github.com/users/Rogerhu12/followers",
    "following_url": "https://api.github.com/users/Rogerhu12/following{/other_user}",
    "gists_url": "https://api.github.com/users/Rogerhu12/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/Rogerhu12/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/Rogerhu12/subscriptions",
    "organizations_url": "https://api.github.com/users/Rogerhu12/orgs",
    "repos_url": "https://api.github.com/users/Rogerhu12/repos",
    "events_url": "https://api.github.com/users/Rogerhu12/events{/privacy}",
    "received_events_url": "https://api.github.com/users/Rogerhu12/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": false
  },
  "jobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413/jobs",
  "logs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413/logs",
  "check_suite_url": "https://api.github.com/repos/Rogerhu12/math-research-public/check-suites/124672751472",
  "artifacts_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413/artifacts",
  "cancel_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413/cancel",
  "rerun_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46084442413/rerun",
  "previous_attempt_url": null,
  "workflow_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/workflows/433258281",
  "head_commit": {
    "id": "95ae5c2399664bed1b9597611b7385cb4e8d6d5e",
    "tree_id": "b4a96b86c76b3cfb2a36cd76b4d92e6f15016055",
    "message": "Launch complete five-eighths supported-seed branch with unchanged fixed target and full budgets",
    "timestamp": "2026-11-27T23:47:35Z",
    "author": {
      "name": "Boyang Hu",
      "email": "2538238358@qq.com"
    },
    "committer": {
      "name": "Boyang Hu",
      "email": "2538238358@qq.com"
    }
  },
  "repository": {
    "id": 1457408986,
    "node_id": "R_kgDOVt5L2g",
    "name": "math-research-public",
    "full_name": "Rogerhu12/math-research-public",
    "private": false,
    "owner": {
      "login": "Rogerhu12",
      "id": 199914264,
      "node_id": "U_kgDOC-pzGA",
      "avatar_url": "https://avatars.githubusercontent.com/u/199914264?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/Rogerhu12",
      "html_url": "https://github.com/Rogerhu12",
      "followers_url": "https://api.github.com/users/Rogerhu12/followers",
      "following_url": "https://api.github.com/users/Rogerhu12/following{/other_user}",
      "gists_url": "https://api.github.com/users/Rogerhu12/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/Rogerhu12/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/Rogerhu12/subscriptions",
      "organizations_url": "https://api.github.com/users/Rogerhu12/orgs",
      "repos_url": "https://api.github.com/users/Rogerhu12/repos",
      "events_url": "https://api.github.com/users/Rogerhu12/events{/privacy}",
      "received_events_url": "https://api.github.com/users/Rogerhu12/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "html_url": "https://github.com/Rogerhu12/math-research-public",
    "description": "Open research computations: flexible closed surfaces, Serre uniformity, rank-two Sha, invariant subspaces",
    "fork": false,
    "url": "https://api.github.com/repos/Rogerhu12/math-research-public",
    "forks_url": "https://api.github.com/repos/Rogerhu12/math-research-public/forks",
    "keys_url": "https://api.github.com/repos/Rogerhu12/math-research-public/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/Rogerhu12/math-research-public/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/Rogerhu12/math-research-public/teams",
    "hooks_url": "https://api.github.com/repos/Rogerhu12/math-research-public/hooks",
    "issue_events_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues/events{/number}",
    "events_url": "https://api.github.com/repos/Rogerhu12/math-research-public/events",
    "assignees_url": "https://api.github.com/repos/Rogerhu12/math-research-public/assignees{/user}",
    "branches_url": "https://api.github.com/repos/Rogerhu12/math-research-public/branches{/branch}",
    "tags_url": "https://api.github.com/repos/Rogerhu12/math-research-public/tags",
    "blobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/Rogerhu12/math-research-public/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/Rogerhu12/math-research-public/languages",
    "stargazers_url": "https://api.github.com/repos/Rogerhu12/math-research-public/stargazers",
    "contributors_url": "https://api.github.com/repos/Rogerhu12/math-research-public/contributors",
    "subscribers_url": "https://api.github.com/repos/Rogerhu12/math-research-public/subscribers",
    "subscription_url": "https://api.github.com/repos/Rogerhu12/math-research-public/subscription",
    "commits_url": "https://api.github.com/repos/Rogerhu12/math-research-public/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/Rogerhu12/math-research-public/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/Rogerhu12/math-research-public/contents/{+path}",
    "compare_url": "https://api.github.com/repos/Rogerhu12/math-research-public/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/Rogerhu12/math-research-public/merges",
    "archive_url": "https://api.github.com/repos/Rogerhu12/math-research-public/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/Rogerhu12/math-research-public/downloads",
    "issues_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues{/number}",
    "pulls_url": "https://api.github.com/repos/Rogerhu12/math-research-public/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/Rogerhu12/math-research-public/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/Rogerhu12/math-research-public/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/Rogerhu12/math-research-public/labels{/name}",
    "releases_url": "https://api.github.com/repos/Rogerhu12/math-research-public/releases{/id}",
    "deployments_url": "https://api.github.com/repos/Rogerhu12/math-research-public/deployments"
  },
  "head_repository": {
    "id": 1457408986,
    "node_id": "R_kgDOVt5L2g",
    "name": "math-research-public",
    "full_name": "Rogerhu12/math-research-public",
    "private": false,
    "owner": {
      "login": "Rogerhu12",
      "id": 199914264,
      "node_id": "U_kgDOC-pzGA",
      "avatar_url": "https://avatars.githubusercontent.com/u/199914264?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/Rogerhu12",
      "html_url": "https://github.com/Rogerhu12",
      "followers_url": "https://api.github.com/users/Rogerhu12/followers",
      "following_url": "https://api.github.com/users/Rogerhu12/following{/other_user}",
      "gists_url": "https://api.github.com/users/Rogerhu12/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/Rogerhu12/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/Rogerhu12/subscriptions",
      "organizations_url": "https://api.github.com/users/Rogerhu12/orgs",
      "repos_url": "https://api.github.com/users/Rogerhu12/repos",
      "events_url": "https://api.github.com/users/Rogerhu12/events{/privacy}",
      "received_events_url": "https://api.github.com/users/Rogerhu12/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "html_url": "https://github.com/Rogerhu12/math-research-public",
    "description": "Open research computations: flexible closed surfaces, Serre uniformity, rank-two Sha, invariant subspaces",
    "fork": false,
    "url": "https://api.github.com/repos/Rogerhu12/math-research-public",
    "forks_url": "https://api.github.com/repos/Rogerhu12/math-research-public/forks",
    "keys_url": "https://api.github.com/repos/Rogerhu12/math-research-public/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/Rogerhu12/math-research-public/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/Rogerhu12/math-research-public/teams",
    "hooks_url": "https://api.github.com/repos/Rogerhu12/math-research-public/hooks",
    "issue_events_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues/events{/number}",
    "events_url": "https://api.github.com/repos/Rogerhu12/math-research-public/events",
    "assignees_url": "https://api.github.com/repos/Rogerhu12/math-research-public/assignees{/user}",
    "branches_url": "https://api.github.com/repos/Rogerhu12/math-research-public/branches{/branch}",
    "tags_url": "https://api.github.com/repos/Rogerhu12/math-research-public/tags",
    "blobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/Rogerhu12/math-research-public/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/Rogerhu12/math-research-public/languages",
    "stargazers_url": "https://api.github.com/repos/Rogerhu12/math-research-public/stargazers",
    "contributors_url": "https://api.github.com/repos/Rogerhu12/math-research-public/contributors",
    "subscribers_url": "https://api.github.com/repos/Rogerhu12/math-research-public/subscribers",
    "subscription_url": "https://api.github.com/repos/Rogerhu12/math-research-public/subscription",
    "commits_url": "https://api.github.com/repos/Rogerhu12/math-research-public/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/Rogerhu12/math-research-public/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/Rogerhu12/math-research-public/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/Rogerhu12/math-research-public/contents/{+path}",
    "compare_url": "https://api.github.com/repos/Rogerhu12/math-research-public/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/Rogerhu12/math-research-public/merges",
    "archive_url": "https://api.github.com/repos/Rogerhu12/math-research-public/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/Rogerhu12/math-research-public/downloads",
    "issues_url": "https://api.github.com/repos/Rogerhu12/math-research-public/issues{/number}",
    "pulls_url": "https://api.github.com/repos/Rogerhu12/math-research-public/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/Rogerhu12/math-research-public/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/Rogerhu12/math-research-public/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/Rogerhu12/math-research-public/labels{/name}",
    "releases_url": "https://api.github.com/repos/Rogerhu12/math-research-public/releases{/id}",
    "deployments_url": "https://api.github.com/repos/Rogerhu12/math-research-public/deployments"
  }
}
```

### 首次官方jobs完整对象

```json
{
  "jobs": [
    {
      "id": 140790598810,
      "name": "Construct the same fixed target and solve the complete five-eighths supported seed",
      "status": "in_progress",
      "conclusion": null,
      "run_id": 46084442413,
      "logs_url": null,
      "steps": [
        {
          "name": "Set up job",
          "status": "completed",
          "conclusion": "success",
          "number": 1
        },
        {
          "name": "Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
          "status": "completed",
          "conclusion": "success",
          "number": 2
        },
        {
          "name": "Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
          "status": "completed",
          "conclusion": "success",
          "number": 3
        },
        {
          "name": "Install the recorded numerical and automatic differentiation dependencies",
          "status": "in_progress",
          "conclusion": null,
          "number": 4
        },
        {
          "name": "Execute public research and publish independent compact records",
          "status": "pending",
          "conclusion": null,
          "number": 5
        },
        {
          "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
          "status": "pending",
          "conclusion": null,
          "number": 9
        },
        {
          "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
          "status": "pending",
          "conclusion": null,
          "number": 10
        }
      ]
    }
  ]
}
```

## 7. 2026-11-28 00:01:56 UTC — 第一个必要输入真实返回

maker步骤真实returncode=0，总6.160448841999994秒，实际source bce727d650913286f0710e28736afecd599cb9d1/89cc，准备报告65334B/SHA a052a2ea0e07f10e67d93eb4e7b5b1138659fe9127a91b3b0d822d527c03b7ea。固定NPZ4334B/SHA b9e12a03...、完整nodes144306B及scalar40488B身份都在下面原whole记录；nodes/NPZ仅metadata未读取。target957cf0...是原固定数学，不是新候选场。此处仅maker已经返回，固定参考第二步和science尚未在本固定记录返回，所有本轮model/point/final/费用仍未知。

以下完整保存本次小分卷原所有字；实际运行、全部source、每项输出完整SHA、完整命令/输入/cleanup/错误均不删。没有重算输入或搬运raw。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1-part-001.md",
  "bytes": 5756,
  "sha256": "caf0a4e6c6cfd6e486e3bc2e5efefc6268980cf511403f6637cc5acdec5707df",
  "git_blob_sha": "46f3cc8f5fc8dcdd913c8e729a9d8fad52249a24",
  "fixed_commit": "e9d1ed055bce5e239d8ea2d28e08915ba3275db2"
}
```

# 公开Actions 46084442413/1：实际阶段 1–1

[运行](https://github.com/Rogerhu12/math-research-public/actions/runs/46084442413)；[总索引](2026-11-27-public-actions-46084442413-1.md)。

本卷完整保留这些实际阶段的紧凑输入/源码/参数/输出身份，不存科学数组或逐点报告。

## 1. followup:prepare-complete-fixed-fejer-r690-inputs-20261127

```json
{
  "name": "followup:prepare-complete-fixed-fejer-r690-inputs-20261127",
  "state": "completed",
  "returncode": 0,
  "seconds": 6.160448841999994,
  "scope": "Necessary complete deterministic new mathematical input. Restore the exact accepted099 scalar-parameter source; extract the whole e640 projection; construct the fixed seven-mode RN-even Fejer chart, all 923 exact affine nodes and complete FullHold node/radius error ledger. No warm/BVP/pulse field, old core, old final, F/J/normal root or geometric certificate is used. This is a new fixed target; original branches and old literal-address provenance are retained explicitly.",
  "metrics": {
    "fixed-fejer-r690-inputs/report.json": {
      "schema": "complete-fixed-fejer-r690-input-preparation-v1",
      "source": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
      "status": "complete",
      "complete": true,
      "seconds": 0.6605406280000068,
      "definition": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
      "target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "actual_run": "46084442413",
      "actual_attempt": "1",
      "actual_source_commit": "bce727d650913286f0710e28736afecd599cb9d1",
      "all_input_source_output_rechecked": true,
      "physicalF": 0,
      "J_evaluations": 0,
      "normal_roots": 0
    }
  },
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/report.json",
      "sha256": "a052a2ea0e07f10e67d93eb4e7b5b1138659fe9127a91b3b0d822d527c03b7ea",
      "bytes": 65334
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
      "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "bytes": 4334
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "bytes": 144306
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
      "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "bytes": 40488
    }
  ],
  "input_files": [
    {
      "role": "source",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
      "commit": "bce727d650913286f0710e28736afecd599cb9d1",
      "sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
    },
    {
      "role": "followup_queue",
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-21.json",
      "path_commit": "95ae5c2399664bed1b9597611b7385cb4e8d6d5e",
      "checkout_commit": "bce727d650913286f0710e28736afecd599cb9d1",
      "sha256": "c83981e0ed294593207c780a863f9328d120103929cbd58f58810e42f3af9d6c"
    }
  ],
  "source_commit": "bce727d650913286f0710e28736afecd599cb9d1",
  "source_sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/followup-sources/0001-167d7c1a5813-bce727d65091/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
    "--repo",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/followup-sources/0001-167d7c1a5813-bce727d65091",
    "--outdir",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs",
    "--panels",
    "128"
  ],
  "cleanup_generated": {
    "deleted": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "skipped": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "scope": "Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"
  },
  "step_id": "prepare-complete-fixed-fejer-r690-inputs-20261127",
  "summary_errors": [],
  "missing_outputs": []
}
```



## 2026-11-28 00:11:49 UTC — 21两完整输入真0及新model初统计返回

第二完整参考构造自然返回0，用时519.771413671秒（报告内部515.729490529秒），实际source commit 185679de628e5bee09652e5f8ec9beeff8ff247a。原report=84966B/6e4e88ff609cfe606e013e6631cb6e93327b7b9f11f497491b4019b8fb8ed2ba；全部原命令、七输出身份、输入绑定和cleanup/缺件数组保下面第二步骤全对象。M160/J923/P7377/N2048、height1.947054437068418；原2218叶complete=true但accuracy_reached=false、whole_tail=true，无丢尾或新证书。仅原二输入完成，不代科学完成。

科学实际00102534c51acf39f0e6f27bc34d37db3bebd6ec/f600/PID3644，model=9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63；初点7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47于2026-11-27T23:59:49.654114+00:00原统计返回Phi=3233.3855489912225、Gram=0.6568825757487662。初有限几何/六族g/K/D尚未返回；accepted0/reportfalse，不从别的width/model填值。以下whole part身份后只追加尚未登记的第二原步骤，第一原步骤已经在前节完整保留。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1-part-001.md",
  "bytes": 16602,
  "sha256": "99d55bedb730b8e764848c5717206e7e99be5145e971c2b3f906fad91760b24c",
  "git_blob_sha": "a983cf74fdb10219c9c53f434dfcf10a1e7a6f80",
  "fixed_commit": "920546134cd72cab133165c2be7a5380204dabd9"
}
```

```json
{
  "name": "followup:prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run21",
  "state": "completed",
  "returncode": 0,
  "seconds": 519.771413671,
  "scope": "Necessary complete reference construction for the one predeclared Fejer RN-even64 chart and complete original R690 scalar. Consume all real fixed-input products from the independent formula maker, preserve all 923 exact nodes, 7377 positive observations and every eight-Gauss/reference scalar jet. The scalar integer table uses a predeclared 2218-leaf rule; H is the original complete normalized-c Gauss seed and remains free. Reinterpret the full ordered eleven-payload historical literals explicitly on the new target and mesh, without claiming same physical s/point or inheriting unknown old history, field values, certificates, or completion. This is necessary input construction, not a scientific fixture or proof.",
  "metrics": {
    "fixed-fejer-reference/report.json": {
      "schema": "R690-fixed-fejer-axisymmetric-SO3-preparation-v1",
      "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "185679de628e5bee09652e5f8ec9beeff8ff247a",
      "complete": true,
      "seconds": 515.729490529,
      "reference_model": "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
      "fixed_scalar": "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
      "scalar_parameters": "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa",
      "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "full_target": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      "fixed_recipe": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
      "model_chart": "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
      "model_mesh": "ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc",
      "core0": "0x1.c000000000000p-2",
      "core1": "-0x1.3333333333333p-4",
      "core2": "0x1.b6db6db6db6dbp-6",
      "M": 160,
      "J": 923,
      "P": 7377,
      "N": 2048,
      "height": 1.947054437068418,
      "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "input_preparation": "a052a2ea0e07f10e67d93eb4e7b5b1138659fe9127a91b3b0d822d527c03b7ea",
      "locations": "65e87a579c561408a22a2a5990517a6dd0bce354651a960e2f9ab9bb01b89bef",
      "location_provenance": "8436f76476f6eb8d927745e37de0689adde56cd6c81eb2a60d36f3825415ff8d",
      "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "leaf_target": 2218,
      "actual_leaves": 2218,
      "accuracy_reached": false,
      "integral_width_exact": "20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000",
      "whole_tail": true,
      "unresolved_tail_dropped": false,
      "clock_selects_leaves": false,
      "old_warm_not_required": true,
      "old_surface_used": false,
      "old_directions_replayed": false,
      "old_certificates_inherited": false,
      "physical_field_read": false,
      "new_field_still_required": true,
      "run": "46084442413",
      "attempt": "1"
    },
    "fixed-fejer-reference/material-envelope-carrier-binding.json": {
      "schema": "complete-fixed-fejer-actual-reference-binding-v1",
      "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "185679de628e5bee09652e5f8ec9beeff8ff247a",
      "run": "46084442413",
      "attempt": "1",
      "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "full_reference_definition": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "preparation": "6e4e88ff609cfe606e013e6631cb6e93327b7b9f11f497491b4019b8fb8ed2ba",
      "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "history": "8436f76476f6eb8d927745e37de0689adde56cd6c81eb2a60d36f3825415ff8d",
      "all_six_actual": true,
      "old_values_or_unknown_history_inherited": false
    }
  },
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/report.json",
      "sha256": "6e4e88ff609cfe606e013e6631cb6e93327b7b9f11f497491b4019b8fb8ed2ba",
      "bytes": 84966
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/reference.npz",
      "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "bytes": 894879
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/observations.npz",
      "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "bytes": 205842
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/locations.json",
      "sha256": "65e87a579c561408a22a2a5990517a6dd0bce354651a960e2f9ab9bb01b89bef",
      "bytes": 106771
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/supplied-location-provenance.json",
      "sha256": "8436f76476f6eb8d927745e37de0689adde56cd6c81eb2a60d36f3825415ff8d",
      "bytes": 223955
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/fixed-target-definition.json",
      "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "bytes": 30919
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
      "sha256": "9e8e8ea20684c75db7df9705545bb4d0cb7e61019ecf5c169a17862cfd5e9f22",
      "bytes": 35712
    }
  ],
  "input_files": [
    {
      "role": "source",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
      "commit": "185679de628e5bee09652e5f8ec9beeff8ff247a",
      "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
    },
    {
      "role": "followup_queue",
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-21.json",
      "path_commit": "95ae5c2399664bed1b9597611b7385cb4e8d6d5e",
      "checkout_commit": "bce727d650913286f0710e28736afecd599cb9d1",
      "sha256": "c83981e0ed294593207c780a863f9328d120103929cbd58f58810e42f3af9d6c"
    }
  ],
  "source_commit": "185679de628e5bee09652e5f8ec9beeff8ff247a",
  "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/followup-sources/0002-32be9120e18b-185679de628e/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
    "--repo",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/followup-sources/0002-32be9120e18b-185679de628e",
    "--fixed-input",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
    "--fixed-input-report",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/report.json",
    "--node-report",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
    "--scalar-input",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
    "--manifest",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/followup-sources/0002-32be9120e18b-185679de628e/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json",
    "--outdir",
    "/home/runner/work/_temp/visible-larger-research-46084442413-1/research/fixed-fejer-reference",
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
  "cleanup_generated": {
    "deleted": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "skipped": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "scope": "Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"
  },
  "step_id": "prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run21",
  "summary_errors": [],
  "missing_outputs": []
}
```

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
  "bytes": 61814,
  "sha256": "372255048ffb853d16ce84d8d6ec9bc8336aa6eb80b56b87d0bb8fbcb38ca6b4",
  "git_blob_sha": "427ad0d78e580b41c8f0d955dfd83a265d6c31ac",
  "fixed_commit": "920546134cd72cab133165c2be7a5380204dabd9"
}
```

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-20261127",
  "scientific_source_commit": "00102534c51acf39f0e6f27bc34d37db3bebd6ec",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3644,
  "observations": {
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-28 00:02:41 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 537,
      "closure_original_returns": 4658,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T23:59:49.654114+00:00",
      "math_event": "initial-statistics-returned",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 3233.3855489912225,
      "initial_Gram": 0.6568825757487662,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 3233.3855489912225,
      "current_Gram": 0.6568825757487662,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json",
      "bytes": 3295,
      "sha256": "e8dfc2caba116df0e699cec39ca3c0507d5de78084e5c8e35b5136d3e5dbc7c6",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "bytes": 3529,
      "sha256": "ab5eb623d3743c46ef2389333a7112d4f3d5b0c991883156ad099b06f6f404ae",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "initial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "initial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "initial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.reach",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.body_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_plus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_minus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.cap_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.height_floor",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "5f2190a91b9625ca5bbe515d7c777008ce60e3df617d518a127effecb661e946",
  "observed_utc": "2026-11-28T00:02:42Z"
}
```

## 2026-11-28 00:17:39 UTC — 21初完整有限六族几何返回；22改以19半宽作对照

21初/当前仍同7e06点、model9387。正常进度记initial-complete-geometry-returned@00:08:56 UTC；数学进度最新current-geometry-returned@2026-11-28T00:10:54.606461+00:00，并非准确首次数学geometry事件时刻。真实六g为reach +2.541916739245917、body_diameter −0.036200119916736107、distance_plus −0.05389631415885021、distance_minus −3.0936337267043594、cap_diameter −0.06715131487906445、height_floor −1.0411715967426867。Phi3233.3855489912225/Gram.6568825757487662，accepted0/reportfalse。比19原b/S1/2初reach+.9684249942095058更差，但distance_plus从+.005863061771032241变负，不能宣总体单调改善。K/D分别、准确alpha及连续全域费用仍未知。由此22拟以完整19 b/S1/2、δ1/32、两μ.01和全部原预算，只改成对半波seed；早期5/8准备记录保为历史，不冒实际run或改已运行21。尚无22真实输出。

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
  "bytes": 59643,
  "sha256": "90f4f2cb5219ddd9d91919b8b47457d6e207adf6e2a822ac1403b08567bd42ed",
  "git_blob_sha": "6fce20fe70b261b134516b578e555c6bb448e5e6",
  "fixed_commit": "0d5f25d1fc7e00e48eede73f5ddf02f734ce7710"
}
```

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-20261127",
  "scientific_source_commit": "00102534c51acf39f0e6f27bc34d37db3bebd6ec",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3644,
  "observations": {
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json": {
      "phase": "initial-complete-geometry-returned",
      "at": "2026-11-28 00:08:56 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 1448,
      "closure_original_returns": 8762,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T00:10:54.606461+00:00",
      "math_event": "current-geometry-returned",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 3233.3855489912225,
      "initial_Gram": 0.6568825757487662,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 2.541916739245917,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 3233.3855489912225,
      "current_Gram": 0.6568825757487662,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 2.541916739245917,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 2.541916739245917,
      "current_g_body_diameter": -0.036200119916736107,
      "current_g_distance_plus": -0.05389631415885021,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json",
      "bytes": 3332,
      "sha256": "d09dd41c005c996945b4f19d3e673960f494e250e7ee0a801b319f60e505227d",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "bytes": 6173,
      "sha256": "c7fbd04b404978f2c58d8197be527d23ed01704e93e6dbe6a0bc6dcabadb8d2d",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "b1ecc433a9072a3b50fad5a01b784137f3714388d6b93008c13786f6d9045afd",
  "observed_utc": "2026-11-28T00:12:43Z"
}
```

## 2026-11-28 00:44:52 UTC — 21首观测试点统计真实返回，六族几何待返

同一9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63模型与00102534c51acf39f0e6f27bc34d37db3bebd6ec/f600/PID3644，首观测试点df8d2b3af9ab18ef809936ffd90e9001a558cd9b54c99e3e99965d9f4eedd4bc在2026-11-28T00:25:57.351889+00:00返回Phi3233.3855388300776、finite Gram0.6568825814651759。当前trial geometry、alpha及决定未知，不能以Phi微降推几何接受。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、accepted0；原六g保持：reach2.541916739245917，其余五负，reportfalse。normal最新00:37:46在该trial、缓存513角、closure失败0；尚无完整科学返回或连续证书。22完整源已经独立刊出、参数锁定，仍无其真实输入/模型/场结果。00:40发布连接中断及store重置后，已据真实main确认17第三接受484b94f、18下一trial统计88cf5b1已成功，21本条尚未发布，故只续本条，不重复原两结论；新reset后唯一pwd探测仍无执行环境，未做本地科学。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
  "bytes": 58911,
  "sha256": "0f7bb0614f43df755ad8249d343de574ee8bbd976e58d5092c2163ea56f29a21",
  "git_blob_sha": "d82c8b7d88a1bca4c6c440ba6e41c8f8813b4b78",
  "fixed_commit": "93c9dcfa550ce4ac1c2e9b34492ccffd92adb3ad"
}
```

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-20261127",
  "scientific_source_commit": "00102534c51acf39f0e6f27bc34d37db3bebd6ec",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3644,
  "observations": {
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-28 00:37:46 UTC",
      "point": "df8d2b3af9ab18ef809936ffd90e9001a558cd9b54c99e3e99965d9f4eedd4bc",
      "cached_angle_roots": 513,
      "closure_original_returns": 28905,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T00:25:57.351889+00:00",
      "math_event": "trial-statistics-returned",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 3233.3855489912225,
      "initial_Gram": 0.6568825757487662,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 2.541916739245917,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 3233.3855489912225,
      "current_Gram": 0.6568825757487662,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 2.541916739245917,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "df8d2b3af9ab18ef809936ffd90e9001a558cd9b54c99e3e99965d9f4eedd4bc",
      "trial_Phi": 3233.3855388300776,
      "trial_Gram": 0.6568825814651759,
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 2.541916739245917,
      "current_g_body_diameter": -0.036200119916736107,
      "current_g_distance_plus": -0.05389631415885021,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json",
      "bytes": 3347,
      "sha256": "f90d01081ad88d03689e908f2e98d244e427cdb25c1374f01ebd62723c30b000",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "bytes": 7272,
      "sha256": "2d29e470baaf873654812ed7b8fa3ed8ca84f68806574dbc9d29cae2ad6e7c39",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "024dcc0c7c0df437ead2e854a7badbe3d20b0291f5706122e86c65202c438852",
  "observed_utc": "2026-11-28T00:37:49Z"
}
```

## 2026-11-28 01:19:24 UTC — 21首试步实际拒绝与下一试步开始

原run46084442413/1、science00102534c51acf39f0e6f27bc34d37db3bebd6ec/f600/PID3644/model9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63保持。首trialdf8d2b3af9ab18ef809936ffd90e9001a558cd9b54c99e3e99965d9f4eedd4bc现真实返回最大几何违反2.541904432457273、最大族reach、accepted=false；原已返Phi3233.3855388300776/Gram.6568825814651759保留。即使最大违反小幅下降也不能擅自改成通过原接受规则；这里仅记录真实拒绝，未由observer得知完整线性模型、alpha或拒绝决定时刻。

下一point700e41888de5d77a8f49fcb0405b9e47af383188985b4f7d4e926b7f34e6d6a6于01:05:14.368451 trial-start；观察01:12:57Z时统计、几何、接受均未知。current仍初7e06/accepted0，Phi3233.3855489912225/Gram.6568825757487662/g2.541916739245917及六族全保。完整report尚未自然返回；宽度5/8的结果不移作22半波场或23恢复策略场。研究继续各自原完整科学预算。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
  "bytes": 58229,
  "sha256": "a56348a3d2497835a9e98d3afbf2bd69a05ff8d399f46cbe3d870eca2ffde7a7",
  "git_blob_sha": "a7bef65d57a49b02e42c0c795482609b92ee4b62",
  "fixed_commit": "7e40321a66fe496bbef13724faffb7a7801e106d"
}
```

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-20261127",
  "scientific_source_commit": "00102534c51acf39f0e6f27bc34d37db3bebd6ec",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3644,
  "observations": {
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-28 01:12:55 UTC",
      "point": "700e41888de5d77a8f49fcb0405b9e47af383188985b4f7d4e926b7f34e6d6a6",
      "cached_angle_roots": 480,
      "closure_original_returns": 50762,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T01:05:14.368451+00:00",
      "math_event": "trial-start",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 3233.3855489912225,
      "initial_Gram": 0.6568825757487662,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 2.541916739245917,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 3233.3855489912225,
      "current_Gram": 0.6568825757487662,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 2.541916739245917,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "700e41888de5d77a8f49fcb0405b9e47af383188985b4f7d4e926b7f34e6d6a6",
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 2.541916739245917,
      "current_g_body_diameter": -0.036200119916736107,
      "current_g_distance_plus": -0.05389631415885021,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867,
      "previous_completed_trial_point": "df8d2b3af9ab18ef809936ffd90e9001a558cd9b54c99e3e99965d9f4eedd4bc",
      "previous_completed_trial_g": 2.541904432457273,
      "previous_completed_trial_accepted": false,
      "previous_completed_trial_maximum_families": "reach",
      "previous_completed_trial_Phi": 3233.3855388300776,
      "previous_completed_trial_Gram": 0.6568825814651759
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-normal-evaluation-progress.json",
      "bytes": 3365,
      "sha256": "81fbfa8cb5fcef7fc59b58fe435cc93be8c1725fb20e0d7bf681ce3181c86c27",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "bytes": 10151,
      "sha256": "2f088e9656958e21f1972ad3153f3d41fa89c0a2c73f5978e33eff791fe2f200",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "25afb9819249d507d78f15b107ddcebc93696f73cf0c17854cbf7bcdc76ceae8",
  "observed_utc": "2026-11-28T01:12:57Z"
}
```

## 2026-11-28 02:08:32 UTC — 21第二观测试点实际拒绝及下一统计返回

同science00102534c51acf39f0e6f27bc34d37db3bebd6ec/PID3644、driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f、model9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63。此前仅开始的700e41888de5d77a8f49fcb0405b9e47af383188985b4f7d4e926b7f34e6d6a6现真实完成：Phi3233.3855440681737/Gram.6568825785908023、actual_positive_physical_g2.5419057471738853、最大reach、accepted=false。小于初g2.541916739245917不等于通过原接受规则；alpha/选中预测等未返，不推其方向号或拒绝机制。

下一trial1b3b620acf659c388cc66933702465447fca5bf1b1b9ad3a6b9d331ef3b2190f于01:59:51.715709+00:00真实统计Phi3233.3855466914256/Gram.6568825771697846，02:03:11Z尚无几何/决定。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、accepted0/Phi3233.3855489912225/Gram.6568825757487662及原完整六族；complete_report=false、child_exit_code=null。首df8d真实拒绝也保前文。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
    "bytes": 57855,
    "sha256": "f33015a6a4ab448a135fa46d58310d03922e3399a2b62016115d39a03bb99f2d",
    "git_blob_sha": "06d1457ebc2327e480da608558ccd12dceab962c",
    "fixed_commit": "dbbcd99a1c6c15f25224f57424985d8ac2ccf01c",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 03:10:30 UTC — 21第三观测试点实际拒绝及新试点统计

同science00102534c51acf39f0e6f27bc34d37db3bebd6ec/launcherf600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506/PID3644/driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f/model9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63。上一仅统计试点1b3b620acf659c388cc66933702465447fca5bf1b1b9ad3a6b9d331ef3b2190f现真实完成，Phi=3233.3855466914256/Gram=0.6568825771697846、actual_positive_physical_g=2.541911243209535、最大族reach、accepted=false。其g略低于初g2.541916739245917并不等于满足原接受条件；alpha/预测未返，不能猜方向或拒绝原因。前df8d及700e真实拒绝仍保。

下一点5f731a046420ae60f207f8e6ff55b7aa0f8b84552f7b3a6ac9c80baa9a67bdc9于2026-11-28T02:45:51.481212+00:00返回统计Phi=3233.3855480813995/Gram=0.6568825764431082。截至原索引2026-11-28T03:03:27Z，其完整几何和接受决定未知，原缺值TypeError未填。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，accepted0，Phi3233.3855489912225/Gram.6568825757487662及全部原六g不变；最大reach2.541916739245917仍正。complete_report=false/child_exit_code=null，连续费用及完整typed史未付。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
    "bytes": 57855,
    "sha256": "59c758c2cf0ba200fb9829889bc9e2690bac140acbe91530b4619e51ec5335a6",
    "git_blob_sha": "e138cf2bfe5f3bce56e5e33e692de9be8410a833",
    "fixed_commit": "4e37ab47ceeb4d753297742a00b077d28baeb71e",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 03:46:04 UTC — 21第四真实拒绝与下一统计

实际索引03:38:37Z。上一5f731a046420ae60f207f8e6ff55b7aa0f8b84552f7b3a6ac9c80baa9a67bdc9真实几何g2.541913991322188、accepted=false；其Phi3233.3855480813995/Gram.6568825764431082原值保。下一379965d33e179e8babd5b6c11967331c4564723f4f48ae0d29c8ea8b7a93b579于03:31:30.349401仅统计返回，Phi3233.3855485375534/Gram.6568825760949264；几何与接受未知，原三项NoneType缺值不补0。初7e06/accepted0/g2.541916739245917不变。完整报告未返，不由g小幅变化推方向号、可行或转移历史。

```json
{
  "mathematical": {
    "math_at": "2026-11-28T03:31:30.349401+00:00",
    "math_event": "trial-statistics-returned",
    "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
    "math_model": "9387a145b382e2afc2eaca4f68f7370b91697008e0720e1d8202d22bf878fd63",
    "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
    "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
    "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "initial_Phi": 3233.3855489912225,
    "initial_Gram": 0.6568825757487662,
    "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "initial_violation": 2.541916739245917,
    "initial_geometry_complete": true,
    "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "current_Phi": 3233.3855489912225,
    "current_Gram": 0.6568825757487662,
    "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "current_violation": 2.541916739245917,
    "current_geometry_complete": true,
    "current_state": "initial statistics returned; no accepted direction",
    "trial_point": "379965d33e179e8babd5b6c11967331c4564723f4f48ae0d29c8ea8b7a93b579",
    "trial_Phi": 3233.3855485375534,
    "trial_Gram": 0.6568825760949264,
    "trial_accepted": null,
    "accepted_directions": 0,
    "complete_report": false,
    "stop_reason": null,
    "observer_failures": 0,
    "current_g_reach": 2.541916739245917,
    "current_g_body_diameter": -0.036200119916736107,
    "current_g_distance_plus": -0.05389631415885021,
    "current_g_distance_minus": -3.0936337267043594,
    "current_g_cap_diameter": -0.06715131487906445,
    "current_g_height_floor": -1.0411715967426867,
    "previous_completed_trial_point": "5f731a046420ae60f207f8e6ff55b7aa0f8b84552f7b3a6ac9c80baa9a67bdc9",
    "previous_completed_trial_g": 2.541913991322188,
    "previous_completed_trial_accepted": false,
    "previous_completed_trial_maximum_families": "reach",
    "previous_completed_trial_Phi": 3233.3855480813995,
    "previous_completed_trial_Gram": 0.6568825764431082
  },
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bfiveeighths-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ]
}
```

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46084442413-1.md",
    "bytes": 57855,
    "sha256": "ac343fae000fad1033f51de38e644471c865571ac0c5e1a80035c7543b033c02",
    "git_blob_sha": "c80cf143270119864181c6170899eaf2d98da837",
    "fixed_commit": "9d4df9a9ef341a72b6f8976141e64cf61caaaaf8",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

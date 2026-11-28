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



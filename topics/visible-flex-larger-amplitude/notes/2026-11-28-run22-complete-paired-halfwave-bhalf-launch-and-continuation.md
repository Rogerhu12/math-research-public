# 22：完整成对半波、半宽基线的真实启动与续求

2026-11-28 UTC；Astra-larger-e4e2a2bf-20261126。当前是完整启动包：真正run号、job、来源commit、输入返回和新场均须等公开Actions真实事件后另记。本文件不把准备当执行。

## 1. 科学选择与全部预算

完整19数值基线 b/S=1/2、delta=1/32、metric/restoration damping均.01，M160/J923/N2048/P7377、32法向阶段、全自由变量、根和回溯、QP、全角/径向/几何域全部保。新来源实现R724的成对半波：两个等长中央分别+h_delta(t/2)、−h_delta(t/2)。它有相同准确跨段均值及两角根方程，中央切向导数减半，但中间区域出现真实位移；whole Gram、D、主曲率与reach不能由这个局部结论填入。

21原五分之八初reach违反2.541916739245917，比19半宽.9684249942095058差，distance-plus则转负；完整原实测已分别刊各note。故本分支保19半宽以单独比较半波机制。早期5/8准备只是历史，未执行为22；恢复自适应阻尼与geometry-first都不混入本轮。

两个完整必要input构造器先在同runner重新生成固定g与全部参考输入，随后157词科学整步。原角2048、stage-block64、angle-block8、integration8、seed radial8/profile16；endpoint root24迭代/18backtracks、seed mean128/24及scalar64；metric方向1/QP16，restoration方向4/QP64，line-trials15、active192、near-active32，QP0/1e−6与metric目标1e−9全保。完整每一argv、selector和输出以已刊whole ready为准，下面表只是索引。

| 步骤 | 原字参数词 | 完整正式投影 | 接入条件 |
|---|---:|---:|---|
| 必要固定输入 | 6 | 14 | 新runner自身重建 |
| 完整参考 | 26 | 62 | 前步真实返回 |
| 新半波科学 | 157 | 458 | 两完整input真实返回 |
| 新半波pure | 7 | 445 | 科学真实自然返回后整步接 |

原48个live投影、清理仅已返child新生成rows-*缓存的完整范围、保同场reference cache规则都原样。全science+pure最小完整队列110351B，超过原95000B限额；初三步完整63721B，不裁字段挤入。pure完整准备已刊，只有真正返回才退休已返项并接入，队列钟和平台钟都不是数学完成。

## 2. 完整来源与参数

全部20新源、137科学角色/18runtime与三个完整源码再生器已刊于7d34ebe278826c68a9e84c32179251220bf2fc3b。相对完整19/21当前父，17对实际替换、120对原样；这个120不是此前某个历史original120的全不变断言。原source paths/whole SHA全部保。完整seed物理与Q/binder严格新模型，不从旧identity去掉不同字段后冒同场。

完整六参数件已刊于637fc22a3d9b67f62d9fd3546028d443ec869b98：[全参数总表](../computations/fixed-fejer-paired-halfwave-bhalf-complete-parameter-delivery.json)，合279148B。三ready/display与再生器/说明/总表完整，不以本文摘要替代参数。两个大历史metadata只用精确whole父+JSON pointer共享，原字段和所有旧值可完整恢复；旧源码构造器保持原历史义，不冒新家族生成器。

当前driver 095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec，launcher6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c，pure be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92；完整137对与每个整文件bytes/blob保[当前绑定](../computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json)。

## 3. 原历史、peer与新场边界

原五组受支持peer CLI逐词保留。原六external职责与真实19/20/21另外三组完整保，后三仍是其真实10fa来源，不塞入新PARENT_FAMILIES，也不改成095b。已有P0/G/typed discovery顺序、失败和unknown完整保；任何旧live或accepted点不作跨runner raw。12–17官方取消和未自然返回是分开的事实，不能造全final或空typed历史。

请求完整保全部原19顶层字段；对改变的当前字段，明确指向27133B原19whole request及准确JSON pointer，其他原字段仍inline。原workflow/controller谱系也完整保；当前控制器仅21→22槽名和索引日期2026-11-28，35原pins、同步/pull/rebase、预算及全部原执行流不改。当前工作流只新请求路径触发，独立concurrency，不取消旧runner。

## 4. 原始数据与README同步

科学只在本公开仓库Actions。完整raw、参考数组、snapshot、accepted/final、root packet、per-cell费用和mesh只在runner/scratch；不写Git/Release/artifact，不换名字跨run迁移。保完整源/配方/真实run与whole输出SHA。当前2input和新全场都必须真实返回自身身份。

350分钟工作流与20000秒controller checkpoint保原；活科学child继续按原流观察至自然返回，时长不是允许根代理停止研究的理由。每次真实pull比较两个README的diff，变更立即执行，已读commit写独立HANDOFF槽。root当前本地执行环境仍不可用，云端metadata确认不冒本地pull；各活controller真实pull继续。非快进或并发拒绝按当前可用机制鲜HEAD普通整合重推，不force覆盖。

## 5. 完整未付数学责任

准确费用链必须用新物理六片：每中央t/2、相反符号、全切点进入准确全域径向划分，跨段横向均值抵消不冒单段积分为零。辅助A仍原f848十二片。seed计划含cuts不表示原working whole-cell八Gauss及partial积分自动分片；working误差继续未付。

全部32stage/六jet/连续branch/全角1024胞/922径向加cuts/完整无限尾、R722域三残差和误差传播，以及Gram、上/下帽、mixed/allphase、R723五角色、R718 marked sigma、R716无标记管/正V/非零中心不变量必须同一新场真正完成。normal.complete不替连续分支，mean J不替Cu，旧R709 bool保真。immutable required-angle packet可为trial，但mutable progress不可作准确输入，全13final才满足same-source restart原合同。

全t闭连通C²嵌入/强C²连续、固定有内点H且diamH≥.2D、整像δhold≥.2D、含反射δE>0、reach≥.03D、整面relative metric≤1e−6仍全部未证。之后必须冻结同g/参数/t范围做真实网格、频率、时间加密至机器或原容差，输出多个各<5MB完整mesh的可复现源码及真实身份，说明严格存在缺口并继续增强比例。本次完整启动不是完成标准。

## 6. 完整启动对象身份

下面每条为实际完整对象；都已保护原bytes，不含令牌。真正发布commit与Actions状态随后根据实际事件追加。

```json
{
  "controller": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel22_compact_metadata.py",
    "bytes": 19984,
    "sha256": "0f6a636e438628a312c9c86091a8f69d503dfdd94218f5a5872f17352a244a84",
    "git_blob_sha": "f6fe15f414e431ca95ba4297d3e95df4ca252271"
  },
  "workflow": {
    "path": ".github/workflows/visible-larger-20261128-parallel22.yml",
    "bytes": 2225,
    "sha256": "5026b84e65bd09f4461d87a14b209721919ed5511ed12fe1fd9efe255f1939a6",
    "git_blob_sha": "0651e95f8bd7a9474ad11abdca0d4ddeacff0879"
  },
  "request": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-22.json",
    "bytes": 36444,
    "sha256": "0a657604fccc2757dcc403f35329194fbf5e81b7850ff34afcced8e2ad2e760d",
    "git_blob_sha": "74bbd19b9c51859c939fd3a7dea93c5fb03c1c3f"
  },
  "initial_queue": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-22.json",
    "bytes": 63721,
    "sha256": "99207324fd997b2bb4d01dc941ed68f3b476f4c10c88b95f0727506f2cd8a588",
    "git_blob_sha": "a6b74b70f5544181ccf44ba583ea1935d720e6be"
  },
  "complete_parameters": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-complete-parameter-delivery.json",
    "bytes": 23548,
    "sha256": "ed050212100d597aa6e43af283aad16ad46a7819f73b2db32e4c21e2ce76c05d",
    "git_blob_sha": "6e42ab000ab2f74a4628bf340669c23bace8a410"
  },
  "complete_sources": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-complete-scientific-source-delivery.json",
    "bytes": 26658,
    "sha256": "f5e7ca6bd04ff3cc73d4cd17decfce15e3500bb71ea47bd0f589e13e4e1e5151",
    "git_blob_sha": "e8e9aaf67a31ae2a380bc88a714944bb00b9cf13"
  },
  "current_binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json",
    "bytes": 67013,
    "sha256": "6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638",
    "git_blob_sha": "4f20af6e3663bdf69aca7193bc29624dc706411c"
  }
}
```

## 2026-11-28 01:03:47 UTC — 官方22实际启动

公开run[46090913581/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46090913581)已于2026-11-28T01:00:48Z启动，event=push、head=18081452c5181d958bb5432c4045c067bf1d1caa；官方in_progress。job140811337445的checkout/setup/dependencies已真success，原研究步骤in_progress。下面保完整返回的job对象；此时没有读取22的新科学输入返回、模型、point、六g、接受或完整report，全部保持未知。单是job开始不证输入成功或数学进步。

原完整源/参数/请求/queue已经同提交或其祖先刊出；继续按两实际input、science真实返回、完整pure与全部准确费用的原条件接续。

```json
{
  "source_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs?head_sha=18081452c5181d958bb5432c4045c067bf1d1caa",
  "scope": "Exact selected official run fields; repository/avatar boilerplate not reproduced",
  "id": 46090913581,
  "run_attempt": 1,
  "name": "Visible larger amplitude complete paired half-wave supported seed 20261128 22",
  "status": "in_progress",
  "conclusion": null,
  "head_sha": "18081452c5181d958bb5432c4045c067bf1d1caa",
  "event": "push",
  "created_at": "2026-11-28T01:00:48Z",
  "run_started_at": "2026-11-28T01:00:48Z",
  "updated_at": "2026-11-28T01:00:51Z",
  "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46090913581",
  "workflow_id": 433299248
}
```

```json
{
  "jobs": [
    {
      "id": 140811337445,
      "name": "Construct the same fixed target and solve the complete paired half-wave seed",
      "status": "in_progress",
      "conclusion": null,
      "run_id": 46090913581,
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
          "status": "completed",
          "conclusion": "success",
          "number": 4
        },
        {
          "name": "Execute public research and publish independent compact records",
          "status": "in_progress",
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

## 2026-11-28 01:17:44 UTC — 22两个完整输入与初统计实际返回

真实run46090913581/1的两个完整输入步骤均completed/exit0：输入构造耗时5.928990263999992s，source89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60，实际commit0bfb66f595ebff65a2abf59143b93c4921f0231f；完整参考耗时481.429137124s（内部478.64331817s），sourcee7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb，实际commit3ecc2f9b472810c298b2f066637520eb4ff1b8fb。完整M160/J923/P7377/N2048、2218叶和height1.947054437068418；accuracy_reached=false、whole_tail=true，未冒精化或几何证书。完整原command/全部指标/输入与11输出/cleanup/缺项保下列固定Git原卷两个全JSON块，未以摘要替换原记录。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46090913581-1-part-001.md",
  "bytes": 16601,
  "sha": "ece3181bad61eae661a6480ddec59ff8976f83a4",
  "sha256": "bb8a6ffda09602e32a0689be7dec7a87393440a72b46d19e1454ac9b462c9d7a",
  "ref": "7e40321a66fe496bbef13724faffb7a7801e106d",
  "complete_stage_blocks": [
    {
      "heading": "followup:prepare-complete-fixed-fejer-r690-inputs-20261127",
      "step_id": "prepare-complete-fixed-fejer-r690-inputs-20261127",
      "returncode": 0,
      "seconds": 5.928990263999992,
      "source_commit": "0bfb66f595ebff65a2abf59143b93c4921f0231f",
      "source_sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-r690-inputs/report.json",
          "sha256": "df4b3813457d276c44854dc591c1c81889a0641f766c35557093316ca01212d6",
          "bytes": 65338
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
          "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "bytes": 4334
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
          "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "bytes": 144306
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
          "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "bytes": 40488
        }
      ]
    },
    {
      "heading": "followup:prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run22",
      "step_id": "prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run22",
      "returncode": 0,
      "seconds": 481.429137124,
      "source_commit": "3ecc2f9b472810c298b2f066637520eb4ff1b8fb",
      "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/report.json",
          "sha256": "5e0cfbb397f74f5257a50320e0d49106a5566776bbcb3f1d3c45ef3ecd90d49b",
          "bytes": 84965
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/reference.npz",
          "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "bytes": 894879
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/observations.npz",
          "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "bytes": 205842
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/locations.json",
          "sha256": "082fc635c704a6b59a834204e65a342efb279ec504f2e70dc2987decd0025f51",
          "bytes": 106771
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/supplied-location-provenance.json",
          "sha256": "4e4be359a12856b6a5497604477b1182cbf520c24f001355d1f5e4f0187a60c5",
          "bytes": 223955
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/fixed-target-definition.json",
          "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "bytes": 30919
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46090913581-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
          "sha256": "4e30d6f39143b076ec3ecd85f4988e5eab37917514ef430c6c9cf904f416e1ec",
          "bytes": 35712
        }
      ]
    }
  ]
}
```

同一新半波science实际sourcecommit c6517a030888df2bf0ca51efade67b7693102785，launcher6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c/PID3541；完整driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec。新model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef，旧坐标身份7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47并不表示旧物理场。

01:12:40.949868初统计真实返回Phi681.6517423825409、Gram0.40616525311769985，accepted0/reportfalse。观察至01:15:12Z，初始/当前几何、六族、试步及final均未返回；相应None读取错误是字段尚无值，不补值、不当科学失败。法向进度513角根/closure failures0只是当前只读进度。继续完整几何及原预算科学步骤。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46090913581-1.md",
  "bytes": 52253,
  "sha256": "688a8a336b67e461a8c60991068808dd2bead190c534dde211e2e3c5f522743e",
  "git_blob_sha": "420285a0cce4190a2b6a3a508bbb57fb3f3146fe",
  "fixed_commit": "7e40321a66fe496bbef13724faffb7a7801e106d"
}
```

```json
{
  "step_id": "complete-fixed-fejer-paired-halfwave-bhalf-first-20261127",
  "scientific_source_commit": "c6517a030888df2bf0ca51efade67b7693102785",
  "scientific_source_sha256": "6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c",
  "pid": 3541,
  "observations": {
    "fixed-fejer-paired-halfwave-bhalf-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-28 01:15:11 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 513,
      "closure_original_returns": 4074,
      "closure_logical_failures": 0
    },
    "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T01:12:40.949868+00:00",
      "math_event": "initial-statistics-returned",
      "math_driver": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
      "math_model": "6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 681.6517423825409,
      "initial_Gram": 0.40616525311769985,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 681.6517423825409,
      "current_Gram": 0.40616525311769985,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-paired-halfwave-bhalf-first/actual-normal-evaluation-progress.json",
      "bytes": 3294,
      "sha256": "b8d5ce0deacdf0e19eba180c0a5f9ce4dc74bbde8d51900cd6882c1a945c153d",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "bytes": 3527,
      "sha256": "679086742e14c8a5269acba6ff97236fdbfacc8fbd470a40816f5d00c369900f",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "initial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "initial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "initial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.reach",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.body_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_plus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_minus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.cap_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.height_floor",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "a8137c20cda92b9b56e45d81df040bdd517ac3ed6ae6cb69cca9115762297c94",
  "observed_utc": "2026-11-28T01:15:12Z"
}
```

## 2026-11-28 01:28:06 UTC — 22初始完整六族几何实际返回

run46090913581/1的原science c6517a030888df2bf0ca51efade67b7693102785/launcher6fd57/PID3541、driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec和新半波model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef保持。初完整几何进度事件在01:22:55 UTC已返；01:24:50.545031的current-geometry-returned以及01:25:18Z完整小观察均绑定初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47。initial/current_geometry_complete=true。

六族真实值：reach0.5305849371949052，body_diameter−0.03813552733778258，distance_plus0.11391238912344381，distance_minus−3.0936337267043594，cap_diameter−0.06715131487906445，height_floor−1.0411715967426867；最大正违反0.5305849371949052。Phi681.6517423825409/Gram.40616525311769985、accepted0保持。reach及distance_plus仍正，故该初值不满足有限工作约束，更不构成连续reach/嵌入/1e−6的完成证书。其余四族负不能替代未付连续费用。

与19同固定target/数值参数/初坐标下的原全波model0abfbf真实初值g.9684249942095058、distance_plus.005863061771032241、Phi3825.0583894874153/Gram.6460503011117507相比，半波初值的最大违反、Phi、Gram较小，distance_plus较大。这是两次真实初场工作数值的比较，不是R724自动推出的wholeK/reach/直径单调定理；两source/model不同，当前点SHA相同不能冒同物理场。原19完整初观测保其同名note。

此刻没有任何trial/accepted direction；latest/last trial读取None的原错误保留。完整子进程未自然返回、reportfalse，正继续原完整恢复与度量预算。没有改seed、参数、目标或运行中的源。

队列计数注：保持22完整原step值，仅按compact UTF-8 JSON+LF计数，原63721B三步，science+pure两步103752B，全四步110351B。原request同名minimal字段110351实际是四步计数；旧字节不改不重触发。两种包含pure的完整队列均>95000，因此自然返回后整接pure的责任不变。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

```json
{
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46090913581-1.md",
  "bytes": 50179,
  "sha256": "c235e12015495f77221618b798a439eb9bfbed36b4a9faa59d546a6b72fff2da",
  "git_blob_sha": "42af20c0a8945837b7dcb72610f572240e914489",
  "fixed_commit": "82a95d5050561b8d8dfdfdad1219b74048748c7c"
}
```

```json
{
  "step_id": "complete-fixed-fejer-paired-halfwave-bhalf-first-20261127",
  "scientific_source_commit": "c6517a030888df2bf0ca51efade67b7693102785",
  "scientific_source_sha256": "6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c",
  "pid": 3541,
  "observations": {
    "fixed-fejer-paired-halfwave-bhalf-first/actual-normal-evaluation-progress.json": {
      "phase": "initial-complete-geometry-returned",
      "at": "2026-11-28 01:22:55 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 1448,
      "closure_original_returns": 8762,
      "closure_logical_failures": 0
    },
    "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T01:24:50.545031+00:00",
      "math_event": "current-geometry-returned",
      "math_driver": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
      "math_model": "6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 681.6517423825409,
      "initial_Gram": 0.40616525311769985,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 0.5305849371949052,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 681.6517423825409,
      "current_Gram": 0.40616525311769985,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 0.5305849371949052,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 0.5305849371949052,
      "current_g_body_diameter": -0.03813552733778258,
      "current_g_distance_plus": 0.11391238912344381,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-paired-halfwave-bhalf-first/actual-normal-evaluation-progress.json",
      "bytes": 3333,
      "sha256": "96214f547c18bd527d8942c13a7ab3fbdf116051f5e996e133749f9b5b70fc84",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "bytes": 6173,
      "sha256": "c70f3ccc744a082a2acb126582ff2fc6b67f9e85f0c656c6f7df26f67b39ef32",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-paired-halfwave-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "6d3befc2e352e229567046ff0fd50e28bb703b08acbcc88bff405a59eb1a42c5",
  "observed_utc": "2026-11-28T01:25:18Z"
}
```

## 2026-11-28 02:00:28 UTC — 22首个观测试点统计返回，几何与接受仍未知

同一真实科学子进程 c6517a030888df2bf0ca51efade67b7693102785 / launcher 6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c / PID3541，driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec，model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef。首观测试点97fbb982b31c713cc71b8cb0d44f255127380185bcfb68be53e29dd19d9b579c在2026-11-28T01:43:47.960927+00:00实际返回Phi681.6511710299278及max_relative_gram0.4061652579029476。截至原索引01:50:33Z，trial geometry、trial_accepted与last_completed_trial均未返，原缺值TypeError照实保完整索引；不得从统计下降推接受。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、Phi681.6517423825409、Gram.40616525311769985、g.5305849371949052、accepted0；原六族不变，complete_report=false、child_exit_code=null。normal进度01:50:31仍在该试点、cached_angle_roots513/closure_original_returns29014/logical_failures0；这些计数不付准确费用或连续根存在。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46090913581-1.md",
    "bytes": 49478,
    "sha256": "e9932381ed55a117ae442647956d699079f62ebd1ba8f393808d86f75d5b83f0",
    "git_blob_sha": "f14788b54aef868f6a9d7186bc9ebf1163520d89",
    "fixed_commit": "69b10ba8993f785379ab63a4395353386a1cf172",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

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

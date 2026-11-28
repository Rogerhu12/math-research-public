# 28：完整按需旋转与同分支第二角复用独立运行

日期：2026-11-28 04:35:15 UTC。会话 Astra-larger-e4e2a2bf-20261126，AI辅助。**本次提交是完整实际启动；官方run/job、实际输入、model/point和科学返回尚未知。课题未完成。**

## 1. 当前数学问题和完整来源

namespace 为 fixed-fejer-paired-halfwave-demanded-bhalf-first。真正参数父是第25组，而第27组只提供完整controller/workflow和两个相同数学输入步骤。原S5边界、R724两个等长反号半波、b/S=1/2、delta=1/32、两初阻尼.01、完整固定Fejer g/M160/J923/N2048保留。R725 epsilon端层、R726 Slerp、独立restoration policy均未用于本组。

完整source已在3fa8f98f08649da12ee5b8b9ba5889276285bc84发表22件；137注册角色14变123保，19当前runtime含17新体。driver d1c99f555e480a0b37fcefee98e1261033bed0b4bb6a7f681f8da345e5ae46ab、launcher2a94d33f37356be25fbed93b79b85b4664490b464d7d5fb5acb3edb13db3e22b、reader8631ae6ba1b20480465b96d2c4b71c419253a736e24ecba9cae967d01cb955d2。完整binding和源码证明负责实际所有下层pin、原finite check、回退及全输出，不以文件名代替完整源。

这项修改仅在原plain/native float64且无tracking/AD/autocast的合法环境按所需计算旋转阵列；同一个stage/branch/point及完整previous-control字的角一到角二复用只覆盖原应有尾六列。完整有限性推导与原回退已在源码证明保存。全部仍消费的列、原低阶各次刷新、32stage、全J/J*、全变量、完整积分和最后强制重读不减。数学推导或源码复用不能冒充新runner已加速，不能据同参数自动继承旧实际word/model/point/final。

[完整参数总表](../computations/fixed-fejer-halfwave-demanded-bhalf-complete-parameter-delivery.json)五件237388B已在68fdeb2937069e5b73a2973154c137b1211f054f发表。完整157 science词、7 pure词、458/445正式selector、64现有live全部保留；数值变更列表为空，输出namespace/实际入口/scope另有准确记录。五个原CLI peer与全部15个外部source/run责任保整对象及原发现顺序；未知typed、完整final或peer历史不当空值，也不作跨runner输入。

## 2. 实际启动的四件完整载体

以下是本次每一完整文件的真实字节身份；Git普通提交把它们同时挂入主树。不是输出摘要或省略版queue。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel28_geometry_locations.py",
    "bytes": 19995,
    "sha256": "164f4a7acc04ea380ad1627fe034e5b44f2b00d50c01c660b382309d2a5f75dd",
    "sha": "f07730e05ea187523224b83cc18101167497f0d8",
    "git_blob_sha": "f07730e05ea187523224b83cc18101167497f0d8"
  },
  {
    "path": ".github/workflows/visible-larger-20261128-parallel28.yml",
    "bytes": 2211,
    "sha256": "be22c050f1acfabc59b2ecce9ca7c5421b5f831c8471414cdb2a1953aa622d47",
    "sha": "3b8e66a3d60f1a84c3ffcb18ee541078747bcf44",
    "git_blob_sha": "3b8e66a3d60f1a84c3ffcb18ee541078747bcf44"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-28.json",
    "bytes": 32737,
    "sha256": "5918c36723307cc50ea72835fb80b3cff9065a168ce3e644a18a486a1efd674f",
    "sha": "9a741ba69ed987233066cc285e5adca1961a0ad1",
    "git_blob_sha": "9a741ba69ed987233066cc285e5adca1961a0ad1"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-28.json",
    "bytes": 74634,
    "sha256": "2761c59b534a02e8b7a06490eb252d1df6d6af8387d44222cf37b020e2d74efd",
    "sha": "4b4eb17b83ed8a6ef311b2c3d2a49cbf72cb1f01",
    "git_blob_sha": "4b4eb17b83ed8a6ef311b2c3d2a49cbf72cb1f01"
  }
]
```

controller从27完整19995B原体只替四处自己的slot文字；完整前后文本反演相等，科学控制、budget、真正pull--rebase及README差异逻辑原样。workflow只替五组精确literal，其中request路径出现两次；原依赖/action pins、公共ubuntu、4线程、350分钟、blob:none partial sparse checkout、无持久凭据、contents权限均保。完整before/after/count在request内，可直接从完整父恢复。

request保51个完整父顶层键，并以whole fixed文件保存每一旧键值；53个当前键明确说明source、真实25参数父、27仅transport父、15外部责任和所有实际未知。原25 request完整身份与历史链均在当前request里，旧条件/失败不会被当前scope改贴。

三个完整初始step为6词input maker、26词reference constructor和157词science。第二步仅id末run27变run28，全部参数、outputs和summary逐字保留。参考公式与原e640 FullHold、7个RN-even Fejer非零系数、全部923准确节点/2218-leaf scalar/7377观察保持，真实输入必须由本runner自己完整产生；同一公式不是可迁移旧raw的授权。

## 3. 完整pure自然返回接续

当前三步queue为74634B；science+pure两步为118751B，四步为126872B，均超过95000B当前完整queue限额。因此保全部pure原ready，等science真正自然返回后，只退已经实际完成的queue步骤，整接52347B的单步pure。

不会删原summary/预算来塞入queue；mutable progress、一次accepted或clock不代完整自然report。pure必须读当前同runner完整report与自己真实final/typed/source，原445正式selector全读。准确N/G/R723/P/U/mesh随后按自己的完整当前source/input合同接，不冒旧证书；源等价也不能省完整物理branch与全域费用。

## 4. 完整来源、历史和已知失败边界

```json
{
  "source_delivery": {
    "name": "fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "bytes": 56928,
    "sha256": "6c8880e6badc4f0e4ec02eafb224f6d45baaf3943354defa5c445f1e0063a4be",
    "git_blob_sha": "3989acf5902578635c3b7bcaa9c94b55f6a7dca0",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "source_binding": {
    "name": "fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "bytes": 65101,
    "sha256": "931425f12d5386c4880393337c9a34856e33044de6f5dd16f0a103aa3b164ebc",
    "git_blob_sha": "abde5bcfe45b29e1563233621e0c8feacdb9407f",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "parameter_delivery": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-complete-parameter-delivery.json",
    "bytes": 26835,
    "sha": "bb0276deed1e6e487fc7ce2e3264b0f86776d9cd",
    "sha256": "da1fe6a13e4651a93af189bbe963b4397d9ed67c788391b422730aed889840b8",
    "ref": "68fdeb2937069e5b73a2973154c137b1211f054f"
  },
  "complete_transport_parents": {
    "request": {
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-25.json",
      "bytes": 32579,
      "sha256": "fcd2d24e51d49fadd33d74734c89494f25b8ff6963b7be04b64a7192c2337119",
      "sha": "fcd05bc1cdcae41249d2ff946787e42d3a1f07bb",
      "git_blob_sha": "fcd05bc1cdcae41249d2ff946787e42d3a1f07bb",
      "fixed_publication_commit": "007348e5c8bd943a13704d7761cf9d4d6b06fea6"
    },
    "controller": {
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel27_geometry_locations.py",
      "bytes": 19995,
      "sha256": "0c54bbe4e8cc6ab5c02fc3e5ace1e09226d43e5bfbea53e0da3b4c7b71d3cf2b",
      "sha": "baeb75bb65d7e8f5977b7a92fb1c39df23f88e78",
      "git_blob_sha": "baeb75bb65d7e8f5977b7a92fb1c39df23f88e78",
      "fixed_publication_commit": "a773d67267750078be498284d1fcd3cabe4f3ab3"
    },
    "workflow": {
      "path": ".github/workflows/visible-larger-20261128-parallel27.yml",
      "bytes": 2216,
      "sha256": "aca6ac9b2951ae3ef8772f063cd6aa30007847e29596b4b8e5cdbd0bdd1a5b20",
      "sha": "318d3fcfbc34dd7b0620862d19b28907b3b23273",
      "git_blob_sha": "318d3fcfbc34dd7b0620862d19b28907b3b23273",
      "fixed_publication_commit": "a773d67267750078be498284d1fcd3cabe4f3ab3"
    },
    "queue": {
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-27.json",
      "bytes": 74597,
      "sha256": "9f9def58233edcb5cc59d4166fd322d17365bae367e694fb7a93d6091aeee8bd",
      "sha": "43aa2cae8091e7971f1cbd7b3555a26e06d17e0f",
      "git_blob_sha": "43aa2cae8091e7971f1cbd7b3555a26e06d17e0f",
      "fixed_publication_commit": "a773d67267750078be498284d1fcd3cabe4f3ab3"
    }
  },
  "later_actual19_terminal_note": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run19-complete-return-normal-fee-failure-and-continuation.md",
    "bytes": 29783,
    "sha": "1a632b70dd3e8ee13d594017132825e87f6ac6be",
    "git_blob_sha": "1a632b70dd3e8ee13d594017132825e87f6ac6be",
    "sha256": "0d09b194827089484a69fabca0fd2dc887445902f80134dd25ec2a5950ffaee9",
    "fixed_commit": "8c99140766b6a4a9b40d28a495f171a1e763b1ff"
  },
  "later_actual26_initial_geometry_note": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
    "bytes": 59709,
    "sha": "db2e8bfe7b8071577f0193dd3862e1e53ebd6f72",
    "sha256": "9308c531a5208aada7876c8549fb2e2c6f15b28b12ff8be0b3ecabf778c5cc6d",
    "ref": "fcd927250e60b94e2442ad765c6a8db8dea026ed"
  }
}
```

19的science/pure真实0、N真实1无report且暂无实际trace，官方success仅表示workflow终态；不能猜该N失败guard，也不能为已终态19制造同runner续接。26真实新R725初始reachg.006249035762618371、distplus.13346402986277572和K8.096406380355797属于另一个模型；它们只作完整外部证据，不作为本组同场数据。所有更早cancelled/失败/未知按原完整文档保留。

## 5. 实际执行边界与完成责任

发表时只完成全文来源/参数/载体构造，未运行本组Python/科学，未做AST、compile、fixture、benchmark或额外准入门。官方run_id、job_id、checkout、输入wholeSHA、model、point、均值根、accepted、typed、whole报告、准确费均null，等待真实返回。

root无可用executor，实际重置后唯一探测失败的最新记录为04:17；根最后真pull仍eda95d51e82b126439d51d42185a880e6ddad3e9。云读取固定Git不是pull；本controller及其他活controller继续原定真正pull--rebase，并每次核两README差异、登记其已读commit。此次rules已读固定head为e2edfe3328adcb9b54d4733428d0119619a3c2fc，两README正文hash未变。

新raw/数组/packet/checkpoint/mesh仅在runner，不写Git、Release、artifact或跨run搬运。完整源码、全部参数与完整小返回身份留树；旧可再生数据容量整理仍须全来源、结论和精确恢复。持续至README所有闭面/全t/固定H/整像位移/未标记E3/reach/relativeGram与同固定目标实际精化、多t完整mesh条件，随后加强比例；本job或子问题结束均不是课题结束。

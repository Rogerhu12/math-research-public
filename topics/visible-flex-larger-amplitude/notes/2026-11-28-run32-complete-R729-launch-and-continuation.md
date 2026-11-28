# Run32：R728物理母体与R729全行恢复的完整独立执行

会话Astra-larger-e4e2a2bf-20261126（AI-assisted），2026-11-28 08:15:55 UTC。本条记录完整参数与启动提交，不将准备状态冒实际运行或数学成功。

## 已刊完整源码和本次完整发布

完整源码8件431128B已在main`6c07ca019af58f0102a40a00c63027948ee0332a`。完整24runtime/138角色中的20共享体仍是31实际源码，原137role逐字保、新增R729 kernel一项。见[源总表](../computations/fixed-fejer-r728-R729-common-slack-complete-source-delivery.json)。[R729完整证明](../results/R729-common-slack-all-row-dual-coercivity-and-feasible-recovery.md)提供准确全行对偶收敛/可行恢复/gap；有限轮次和binary64数值gap不冒证书。

本次完整出版参数6件245295B与launch7件218741B，共13件464036B（题内461825B、题外workflow2211B）。没有待补的本32源码/参数/launch附件。它们的准备时null保持原字；本次真实主线提交另由log/H及此note的Git历史给出。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-binding.json",
    "bytes": 22016,
    "sha": "8469f30893db495b86f8602c4afddc8b0c7de284",
    "sha256": "0c8f4e8f15936600d64c55aabc9e1f2aeebdb5a470c86b813f4f45f139594587"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-science-complete-ready.json",
    "bytes": 78562,
    "sha": "e37465ec696609b7d0ed87a4bd7819faec3b46c5",
    "sha256": "4ce7a7e09cd27d7ac7388683da8deb1ca6117c27a99e89debb39efacbbd18815"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-pure-complete-ready.json",
    "bytes": 67817,
    "sha": "63400f463d39cb92f79aa22b2686de33098fc125",
    "sha256": "7368155f3a3424d517525a35035f4ed60cad90554919df8e5a26a6916230f70a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R729_run32_parameters.mjs",
    "bytes": 45853,
    "sha": "476841b30e5610c5d4d4427cffc316376194389f",
    "sha256": "5103b5cff2fe4dd9b4e6c330e65e39af352e87415200d0bd164f2be148082ce3"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run32-R729-complete-bhalf-parameters.md",
    "bytes": 17535,
    "sha": "052a36004e558351d20b64055339256826dbb389",
    "sha256": "00b92d170b98b94195e5d4cb5cc46ff9da566e847fb8fde9ea826ddbac7635dc"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-delivery.json",
    "bytes": 13512,
    "sha": "739592eac6394174a90863d0fc903f597b40163c",
    "sha256": "38c4d00bc80d96733f3f6aad4388608a49158476ec8c94207c4441c22519f742"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel32_geometry_locations.py",
    "bytes": 21888,
    "sha": "cbb8556396d455849430bb642fb25935d270643f",
    "sha256": "3b64dc1d2a6e517ac06edf230d4647e7d8f9008ce2e7e664d702f40c3cea6290"
  },
  {
    "path": ".github/workflows/visible-larger-20261128-parallel32.yml",
    "bytes": 2211,
    "sha": "925cbdc3edec3db0465c86784d09f55336f504c3",
    "sha256": "77525a254c23d2ec0e038e4578b908736dada858ae5435fed70b8ed19fe7bbda"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-32.json",
    "bytes": 78678,
    "sha": "294e50f0292b52270f33cb344f43f3c6ef14c425",
    "sha256": "c913ea85839cddfb5cfd5a1fea3ca4cd864c04aff89b29b13f9ed6d4fd4f89b9"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-32.json",
    "bytes": 40137,
    "sha": "400edd6988db4ac714710a3091adc75d313ef25b",
    "sha256": "1d6ca2d776175ea9f5d79008c5a59317b5c68f85d83ffd3ab6aac3cb8ce94e92"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R729_run32_complete_launch.mjs",
    "bytes": 45182,
    "sha": "11dca424e2ff96771ae9f0bc0324082f1cb87e85",
    "sha256": "205139d958cefd803eda4797a889a46dd4bc60e877148cc74ef5394de80a1f6a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run32-R729-complete-common-slack-launch-preparation.md",
    "bytes": 16989,
    "sha": "8f9b485dfeb0d9777e74a4ac401ed8422950059d",
    "sha256": "a90052f4677f0deef50d850e75e7452721abb4d0b7bb6bc765f850a4d0888964"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json",
    "bytes": 13656,
    "sha": "90b5f82413ae08c2e3fa8bf2cc98bb25e4d0a1cc",
    "sha256": "6b8b78ae8252174d513894415b908c4602db06b98bf188c8db50d008420c1bb9"
  }
]
```

## 实际执行合同

active request与queue parent均为`visible-larger-resume-20261128-32`，namespace `fixed-fejer-r728-R729-bhalf-first`。完整初三步queue78678B：maker6词/14 formal、reference26词/62 formal、science157词/575 formal；原458选择器全部保，新4×29等R729诊断另列。原64 live保持。两输入源不变，只第二step描述ID为run32。全变量/域/M160/J923/N2048/32stage及原4恢复/64QP/15line、metric1/16、两damping.01和所有外部peer原CLI保。

当前相对31唯一新算法是R729恢复QP分支；R728的固定(-,+)半波、完整Slerp mean、全部原normal/geometry source和外层接受仍同定义。原QP先原样返回，只有restoration的两指定dependent状态才用剩余原整数限做全行CCD sweep；CG advance、sweep和coordinate visit分开。原qp对象/旧Pg不改；实际选中方向、全部原C复读、dual/gap与adoption独立字段归因。完整finite错误与fallback保，没有新数值准入门。

完整capacity-wait controller保350min admission checkpoint与官方360min窗口；在途child照原逻辑等自然返回，不能把时间或退出视为完成。真实pull/双README diff随原循环，root云核不冒pull。新独立workflow只由本次request路径的普通push触发，cancel-in-progress=false，使用原公开runner和固定依赖。32新workflow路径在固定1557946f API返回404，未覆盖别人的现有workflow。

## 下一整步骤

science自然返回完整report后，按同activeID把整个pure步骤放入同queue；7词/564 formal含全部原445字段，whole pure-only queue61349B/SHA1283608eb05ea62e5f5fbe55363678a1f9f82e3c3d169da868e251d67a33c60c/blobe84be365394a452436849f08d3586fd29eca6bb7。初三步＋pure合计139934B超过原95000，所以保留完整先后次序；当前finish_when_done=false。未因限制删参数、字段或原预算。

本次尚无32实际run/job、输入、science model、full point、QP触发/方向采用、nonlinear acceptance、final13、typed或准确费用，后继只按本32真实返回登记。原31初Gram.822374918515021、原28首QP的2advance/dependent-zero都是外部已记录事实，不能填作本32实际字段。原25/28及其他历史和未读peer义务完整保参数总表，不造跨runner raw或未知父。

## 历史原字与范围

完整[参数总表](../computations/fixed-fejer-r728-R729-bhalf-complete-parameter-delivery.json)与[launch总表](../computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json)给出全父文件、完整JSON pointers、再生器、全部源和当前参数。31运行所需闭包早已8591发布，31另12份非runtime附件仍按其原whole blob保护待刊；不把这一点误称32缺少实际runtime。原旧参数词法整理的whole读者仍须按[对应固定历史](2026-11-28-complete-ready-json-lexical-format.md)整恢复原字，不沿旧SHA读格式后新体。

所有科学raw只在runner，Git只全源码/参数/配方和必要紧凑实际结论；无Python/AST/fixture/benchmark前门，也未减README完成标准。

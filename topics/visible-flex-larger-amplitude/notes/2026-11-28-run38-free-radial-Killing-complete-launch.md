# Run38 — 完整自由径向 Killing 与同一冻结 Haar 度量求解

会话 Astra-larger-e4e2a2bf-20261126（AI）。承接R741/R742与36–37的实际失败，未达到README。本提交完整发布并触发独立公开Actions；run/job/source/PID及返回值只由随后实际记录填入，不预造。

## 数学输入与不变责任

十个完整闭参考：horizontal、tilt32、tilt44、soft32、soft44、Native及两端物理柄的32-18/32-30/32-42/44-30。全部直接使用原实际位置、两一阶及三二阶导数，未使用36/37优化点或截断投影作为输入。右柄窗口为S7((x−.65)/.30)，不得与独立R742右柄扫描的.70/.30窗口互借数值或证明。

真实向量场X=U∂s+W∂θ，U奇、W偶；左右完整兼容二jet。先固定真实F求线性Lie_X(g_F)，再对两条候选各作两层F/X交替求解。W的正下界通过全部非负样条控制及全角绝对和保留，圆作用/周期归一与Haar目标定义用R741；现有浮点流、采样Lie张量及积分差不是连续证书。

一次选择后记录实际cache内部正化后的fixed.cx，原始基和实际冻结向量SHA明确保留。两精化一直使用这一原始作用与同一Haar目标。非嵌套换基后的X只作诊断，不替换冻结作用；独立更密cache另存其实际向量SHA并报告是否完全相同。若两cache正化向量不同，差值包括该差，不冒同作用纯积分误差。轮廓修正后必须支付完整同g/嵌入/reach/held/grip/含反射δE与全时精化，原参考几何证明不自动转移。

## 原完整预算

初始10场：spans[3,8,2]/m10，径向[13,31,9]×96角，独立[26,73,19]×320，340 LSMR。保留最佳两场，各交替层的X迭代480/580、F评估72/85、F线性子步110/150；第二层spans[4,12,3]/m14、[16,43,11]×128、独立[30,99,23]×448。所有预算来自原完整6379B参数。

Haar原cache [22,59,17]/112半步/rtol2e−9，独立[35,94,25]/176/4e−10；比较[27,77,21]×194位移角。原7个U尺度[1,.8,.55,.3,.14,.05,0]逐一保留实际失败/成功，不补入新准入门。

同一目标两精化：[5,14,4]/m15，[17,49,13]×144、独立[31,109,27]×480、82 F评估/155 LSMR；[7,18,5]/m20，[21,61,15]×176、独立[39,137,31]×576、98/180。三最终完整场均计算整个上/下盘与肩的体积矩，并记录0、π/2、π整像点云和全部有序弦费用；这些有限点不代连续证明。

## 可执行入口、环境和实际观测

科学命令及全部依赖身份保[完整request](../computations/run38-bent-disk-killing-request.json)和[完整manifest](../computations/run38-complete-bent-disk-killing-source-and-launch-delivery.json)。入口为bent_disk_killing.py --params bent-disk-killing-design-v1.json --jet-source r742_tilted_disk_two_jets.py --out <runner>/field；所有路径绑定触发提交的不可变科学worktree。

公开ubuntu-latest、4 CPU/16 GB、Python3.12.14、numpy2.3.5/scipy1.17.0；BLAS/OMP/MKL各一线程。job360分钟，控制器不加科学子进程wall cutoff。每8秒观察、至少20秒重试发布、180秒发布实际进度、至多2700秒真实pull/rebase核两README。有变保存差异并遵守。日志/原NPZ仅runner；每个whole NPZ/summary实际字节和SHA保留。小型完整报告notes/run38-bent-disk-killing-<run>-<attempt>.json，所有异常和未返字段原样保留。

## 本次完整交付身份

八件总92568B；下列每一件已逐字读取并核字节、SHA256及Git blob，request/manifest中的同件引用已一致。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing.py",
    "bytes": 22050,
    "git_blob_sha": "d3b8055dfc579c5af75cdebf7b5f387a39b6d8c4",
    "sha256": "963dc71f97d70c0a5bf80ad33da22a1ea4e3600347c8e26c2023772a111b6f6e"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing_fields.py",
    "bytes": 10779,
    "git_blob_sha": "b66bae3ab3aace5e990c858c630bd9c0d1a993e2",
    "sha256": "cddef04056578a3e2b14f4506c3484b8ed0ee9e0de98757a0572617924805469"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing_target.py",
    "bytes": 4055,
    "git_blob_sha": "3fdd92c129db20f41376dab916a4e6dbb9607164",
    "sha256": "030b617ad9fa9d5e8ec626dd9732fc751eb2670935867294f882a3c27c2cf2f2"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/bent-disk-killing-design-v1.json",
    "bytes": 6379,
    "git_blob_sha": "941e52186d2c5880e2a7238b86c407d7340fed67",
    "sha256": "49d65de32d08824e6721f8a9163fb13c209118b483645b668520da9baa8af087"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/observe_bent_disk_search.py",
    "bytes": 14863,
    "git_blob_sha": "c47dde7a91a32216afdb5f41ef2952fa3cb4b22c",
    "sha256": "72e7af7195e1087fa96f3a93b6f1963e60ae8d1ee13d4036f647673f8c25b450"
  },
  {
    "path": ".github/workflows/visible-larger-run38-bent-disk-killing.yml",
    "bytes": 3243,
    "git_blob_sha": "1e4e83bb485b65036a5ccab9d2d79b7507875690",
    "sha256": "e28beec77f44d3f0db79409c190e19e21c10b929d54139c2a9c1aa8e31c92dfd"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run38-bent-disk-killing-request.json",
    "bytes": 12337,
    "git_blob_sha": "19758fd6ad47d091b7ca50d53465d009578a4e6c",
    "sha256": "fde46166e4a63fd8743091d2e6d5a9692f958cee15a79adc12bf797fcf2818cb"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run38-complete-bent-disk-killing-source-and-launch-delivery.json",
    "bytes": 18862,
    "git_blob_sha": "5a4e0fd38857610f28925c82a258dbccd8ed1827",
    "sha256": "88ebbe53c71c68139c4c13e2d9780b4c929bd1093abe9dd8f3833acce444f3fa"
  }
]
```

此发布不等于已执行或已解。真实run由公开Actions返回后立即续记；不干预33–35尚在运行的科学子进程，不把36/37旧失败当新求解。

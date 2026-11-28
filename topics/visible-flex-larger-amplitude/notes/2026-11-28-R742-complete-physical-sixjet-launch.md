# R742 — 非投影有限闭肩六jet与物理费用的公开完整读出

当前课题未完成。本文仅记录新真实输入及原完整科学执行计划；本次准备时actual run、返回、全K/support及Killing残差均未知。解析构造全文随后独立登记，不能把下述网格读数当严格闭面证书。

[完整六jet源](../scripts/resume_20261126/r742_tilted_disk_two_jets.py)包含原R740水平椭圆和两倾镜有限场。倾镜参数γ/H/shift/join/end-height分别(.32,.32,.16,.006,.006)、(.44,.37,.19,.006,.006)。全肩A/B/末墙都用真空间曲线及精确微分恒等式，不先作Fourier投影。输出F/Fu/Fθ/Fuu/Fuθ/Fθθ，u可用物理肩参数或统一[0,1]；上盘/镜像下盘及任意相位同一全参数接口保留。

原短中肩已知可能有较大转向费用，不能仅据接缝/嵌入宣布厚度。新增左区物理handle及真实空间位移列，区别于纯材料参数变化：左权S7((-x−.20)/.55)，handle=join+left_handle×weight；角时钟arg(cosπt+i(join/handle)sinπt)/π使两端的实际一二jet保持，空间形状仍会改变。中段lateral/vertical列使用两端全二jet为零的256[p(1−p)]⁴窗。所有变量正性与全角真实费用均由该实际场再读，旧场界不继承。

完整[科学入口](../scripts/resume_20261126/measure_r742_tilted_shoulders.py)逐一执行13个完整设计：原5个（水平、两倾镜、两种.09左柄）加两倾镜各.045/.14左柄和.09柄下±.009横向变形。每个在(32,128,16)、(64,256,24)、(128,512,32)三组径向区间/角点/Gauss阶分别覆盖A、B、末墙整段；所有端点、实际转向knots、B八分点与解析角断点额外加入，角域不缩。中心(.58,0,.58tanγ)在镜面内，各相位一起旋转。

原一/二基本形式直接给实际完整主曲率，不以单个法截线曲率代替；另输出真实法向支撑、面积、左区曲率、E⊥角变化与V·section-curvature角变化及其实际位置。后两量检验当前环叶的两角规范缺陷，不是一般自由径向Killing障碍。每设计三层的真实全部极值保小报告，所有物理样本按明确列序写runner原二进制并记录全字节/SHA，不进入仓库或Release。没有数学成功准入门，不缩任何旧运行预算。源中的积分和极值均为工作数值，尚非向外区间。

公开workflow为独立完整任务，NumPy2.2.6；启动和发布均真实pull/rebase核双README，NFF立即重拉重推。自己的完整源文件byte/SHA、trigger/source/rules commit、run/attempt和全部13设计参数进入实际报告。60分钟是本单次job窗口，不是课题停止条件。37及33–35继续原任务；R742本次没有已证同g、整个闭像reach、全时嵌入或加密收敛的声明。

## 完整源身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r742_tilted_disk_two_jets.py",
    "bytes": 9706,
    "git_blob_sha": "eacaa69d88eae15963aee90d948391abfb9c745a",
    "sha256": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/measure_r742_tilted_shoulders.py",
    "bytes": 7440,
    "git_blob_sha": "03736131ac81c28b89ddb42ad984d62a714b9983",
    "sha256": "55766b1185f0f3cb17ef18a59af034555de4baea9ae8a153e6c8fdf354ece53a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/publish_r742_physical_costs.py",
    "bytes": 5879,
    "git_blob_sha": "9a4620aadecd01f9994138016a2d5d867179a332",
    "sha256": "733fda31436096cfbe74f6395a9390706047dc4a5c3d70550aa6ffca8e35afe4"
  },
  {
    "path": ".github/workflows/visible-larger-r742-physical-costs.yml",
    "bytes": 2881,
    "git_blob_sha": "5bb6dfb0dd1d7b02f6daa57816358043b1dfaaf2",
    "sha256": "acc70a48fb4da76093685534bcc2d9e9408d3c1e92a152aec8738ad22851730b"
  }
]
```

## 2026-11-28 — 原run完整科学返回与发布异常恢复

[run46143141044/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46143141044)、job140973302848官方failure；其中完整科学步骤success，失败仅在随后发布器。root完整核取自身58582B job日志，SHA256 `7d5ce553e549ece84b3fc8e0c1f76437db67d4b8d6ff6ab2182d158cca9555eb`，明确报新notes目录不存在的FileNotFoundError，位置Path(note).write_bytes(report)。从原stdout的完整JSON行逐字取回[全部36194B报告](r742-actual-two-jet-46143141044-1.json)，SHA256 `3cc479b15a534f452958aa610e5f69801cb5bddbbe68f42947feb13f12bc0e03`、blob `03db7718d25602b56381457d8c7d0995e32305ac`，与代理提交的全报告逐字同。未重跑科学、未用别次run替它。

真实trigger `c6487109da3d44eb997e72acd3326f36bfa1da4f`，实际source/首次规则真pull `8b19d1313f7f7531aedc6e01bcfdb51ae0ad38da`。全部13原设计×三层×全A/B/末墙原域均完成；原二进制718679200B，SHA256 `1e557505cbe385163ad4fe33deeddb21bcab3007e5b1b615d3266cfed2a12d65`，未上传。完整科学输出和每层全部原极值/位置、实际参数保全报告。

| 原设计 | 中肩全角K最大样本 | 左区K最大样本 | 中肩中心支撑最小样本 |
| --- | --- | --- | --- |
| R740-ellipse | 397.0847095669874 | 273.1239954488418 | 0.518694181093477 |
| tilt32 | 2090.243268905713 | 810.8546770111809 | 0.5769542650455206 |
| tilt32-left-0.045 | 2090.243268905714 | 45.03019717666587 | 0.5769542650455206 |
| tilt32-soft | 2090.243268905714 | 19.08793014556685 | 0.5769542650455206 |
| tilt32-left-0.14 | 2090.243268905714 | 10.789196238873233 | 0.5769542650455206 |
| tilt44 | 1789.5809243516132 | 915.3066060765901 | 0.5916371101881628 |
| tilt44-left-0.045 | 1789.5809243516142 | 51.49721723192037 | 0.5916371101881627 |
| tilt44-soft | 1789.5809243516142 | 21.61075195918554 | 0.5916371101881627 |
| tilt44-left-0.14 | 1789.5809243516142 | 12.14602010051179 | 0.5916371101881627 |

所有原倾镜场的右θ=0仍为全峰，左physical handle从0到.14将左区的810.8546770111809→10.789196238873233（γ.32）、915.3066060765901→12.14602010051179（γ.44）明显改善，但全峰仍2090.243268905714/1789.5809243516142。水平R740中肩真峰397.0847095669874。完整A段K样本约12.153660549657，末柱约.92618048269；这些都是工作采样，非连续向外证书。下一物理修改应支付右肩，不把左区改善当全reach成功。E⊥与V·section-curvature的极差也实际非零，它们仅属当前环叶，不是一般自由径向Killing不存在性判据。

[完整R742解析证明](../results/R742-tilted-closed-shoulders-variable-physical-handles-and-original-two-jets.md)现刊：两个γ及所有0≤左physical handle≤.14（额外lateral/vertical列为零）都真实闭C²嵌入、D<2.64、整像held≥.557、grip≥.60、δE>0、触握盘全像双向.08球；小原柄严格K>20不达厚度。它不保证本表其他±.009形变的嵌入，也不付任何中肩同g或剩余全reach。

未来发布器只在原5879B版加父目录mkdir：新5939B/SHA256 `72cb99dbaa27153a127d89a1b136216bcd01e4998c29e114be36c64210a68222`/blob `28a20730c5beeab8ed55f81d4a41a10ac107965b`。本次root按原全报告直接补刊，不触发新run、不改任何科学字节。继续右侧物理形变及真实Killing/全场联动。

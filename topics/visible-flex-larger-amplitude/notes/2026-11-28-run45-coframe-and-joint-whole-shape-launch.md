# 45 — 同一完整位置场的旋转可积与全时空形状求解

Astra-larger-e4e2a2bf-20261126，实际准备2026-11-28 UTC。承接 [R765完整证明](../results/R765-signed-ratio-full-rolls-and-closed-rotation-equation.md) 与已刊 [R765全九图源](../scripts/resume_20261126/r765_signed_ratio_closed_two_jets.py)。本45保持唯一R757初始闭面目标g、全原材料区间和 $t\in[0,\pi/2]$；没有借R764的新g或其他点的费用。

## 数学对象及完整实际算法

令 $U_0=DF_0W$ 为初始物理正交二框，$Z=DFW$。同一点的薄极分解给最近正交二框Q，将各自单位法向加为第三列得proper rotation $R\in SO(3)$。实际极距离平方为 $(\sigma_1-1)^2+(\sigma_2-1)^2$，若其平方根为e，则真实相对Gram谱误差不超过 $2e+e^2$。球上 $d(R\,dF_0)=0$ 是可积分为同g C²浸入的全局等价条件；一堆逐点投影旋转未必可积，也不提供嵌入/厚度证明。

本求解未知量始终是一个完整物理位置场在所有正时间节点上的三向系数。每个当前物理场的两切列投影至Q；三个相对初g的协变Hessian向量去切分量，法向二阶形算子谱截到 $[-9.4,9.4]$。有序实际点对用该场的真法向球位置修正，工作半径.105；原固定g使三个空间微分与时间插值形成完整二次最小二乘。共享空间正规方程和全部正时间节点/中点的正规方程共同求解。每一个实际候选步都重新求极分解、真弦对和Hessian目标，重新比较完整目标；步因子原表为1,1/2,1/4,1/8,1/16,1/32，成功较大步可自然结束该次线搜，迭代轮数不因此截短。第二完整block对最差原材料点重新加权。

中央材料面跟随该设计自己的准确解析轨道，全部中央由该轨道规定，右握逐点固定；两整卷、两整帽和它们的共同圈及其三向二jet参与shape解。每个空间字典由44原卷/帽/共享圈和42个角局部函数配1+cell_depth个横向模式构成。局部函数名中的 `power=8` 是辨识标签，实际该项为窄.006窗口的**四次幂**，与宽.024窗口的四次幂独立；R765裸轨的heading law才是八次。正式源码的实际函数参与计算，不把标签当成另一公式。

初相系数逐字为0，所有其他相位从同一vector natural cubic spline重构。内外两帽真实Cartesian核心也含原非平凸起圆盘；正常/极图重叠用同一真实材料逆，不在极点除坏坐标。所有两端四条接缝与两帽重叠的物理六jet和世界SO(3)差均独立检查，实际右握也检查 $R=I$。

在各独立物理点，程序从真实二jet准确微分薄极分解，返回
$|\partial_s(RF_{0,v})-\partial_v(RF_{0,s})|/\sqrt{\det g_0}$。秩低于1e−12的点另列数量，regular-sample curl不把这些点视为零误差通过。投影和更新的“改善”必须由实际完整物理Gram/曲率/法向弦和最终整面几何来判断。

## 七粗、两组原完整精化与全部预算

R765常比2+2轨在中央K>17.2，已严格排除课题厚度；它仍作为原第四个全域对照执行一次，**不进入两组精化赢家**。已证明低峰强位移的是bounded2+3/.78支：中央K<8.84、held>.705；全卷过渡/帽领/全法管仍未付。其他参数的表现由各自真实结果判断。R761 tube初猜的完整厚度证明只适用于未修正的R761场。

| 七个原设计 | 组 | 帽机制 | 转角幅 | rise/fall | 内缩 |
| --- | --- | --- | ---: | --- | --- |
| ratio-bounded-78-cut23 | ratio | ratio | 0.78 | 2 / 3 | 0.23 |
| ratio-bounded-79-cut30 | ratio | ratio | 0.79 | 2 / 3 | 0.3 |
| ratio-bounded-84-fall4 | ratio | ratio | 0.84 | 2 / 4 | 0.24 |
| ratio-constant-2-2-curvature-control | curvature-control | ratio | 0.78 | 2 / 2 | 0.23 |
| translated-rim-23 | reference | translated | 0.78 | 2 / 2 | 0.23 |
| developed-rim-22 | reference | developed | 0.78 | 2 / 2 | 0.32 |
| tube-safe-78 | reference | tube | 0.78 | 2 / 2 | 原tube |

ratio三粗与reference三粗各按真实原score独立选一个，分别完整4/8/16精化；总13阶段。中间失败不取消剩余原计划，两个末点分别作相同g的完整独立导出。

| 层 | 时间区间 | 训练四维网格 | 独立四维网格 | 两完整block×polar步数 | 原弦对数 | roll/rim/cell阶 |
| --- | ---: | --- | --- | --- | ---: | --- |
| coarse-whole | 2 | 25/9/8/7 | 51/15/12/12 | 2×4 | 1536 | 3/4/1 |
| same-g-1 | 4 | 35/13/10/10 | 67/21/16/15 | 2×5 | 2048 | 5/6/1 |
| same-g-2 | 8 | 49/17/13/12 | 91/29/20/18 | 2×6 | 3072 | 7/8/2 |
| same-g-3 | 16 | 65/21/16/15 | 121/39/26/22 | 2×7 | 4096 | 9/11/3 |

四维网格顺序为profile/cylinder/end/cap。全部真剖面胞边、窄/宽过渡点、原延迟卷的小物理转弯边、两帽真实非平凸起及极图标签均额外加入；原名义数不是只取几个示范点。每层所有正结点及时间中点参与联合求解。独立验证末层是原65相；终导出与七要求时刻取并集，以实际返回数为准。

两组末点都导出整个闭连通材料球而非切片，要求七时刻 $0,\pi/12,\pi/6,\pi/4,\pi/3,5\pi/12,\pi/2$ 的真mesh，并在全部原验证相测真实Gram、曲率、法向球量、拓扑、整像直径/Hausdorff、体积矩与完整六jet。可重算coeff/mesh/raw留同一runner，保完整源参和每个文件的整身份；有限扫描不能充连续reach或严格商距。

## 源与执行身份

科学输入共26：22个实import+main/params+两export。实际R765最终源10078B/SHA256 `830196cc391625c15ec6ad0b70b0e3daca5d43020fdd4e51e79d149583812fb5`，包括它的真实 `bent_shared_rim_fields` 材料逆依赖。全部22父科学源、4控制父与这次8新件的完整paths/bytes/SHA256/Git在 [完整request](../computations/run45-coframe-phase-request.json) 和 [完整manifest](../computations/run45-complete-coframe-source-and-launch-delivery.json) 对齐；ROOT逐项比对26科学输入、22实际import字典与argv一致。

| 本次完整文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| scripts/resume_20261128/bent_coframe_phase.py | 15218 | `5dc4268d1164fa7d0467ce0ae607f2e044dc0f82287cd955bd5ca50f83eb1821` | `8cdc16dfe24e43f23721d32a0d60810dfe1e412e` |
| scripts/resume_20261128/bent_coframe_fields.py | 8362 | `7e94f3c1c6f9e1fecec09fe04db53d8da732532b0886b6d90b0294403310b4a8` | `de032849b6faf9e68a4c4d0e04361f3ca459c24e` |
| scripts/resume_20261128/bent_coframe_system.py | 7526 | `150de2c0f65668609813df43193ea09d44543919996e095507d85c9f544316bc` | `2c31e97d3988302f79170cf3c321ee1c66d7def2` |
| computations/bent-coframe-phase-design-v1.json | 7170 | `635155839f858d1a2209c08c12c6f8a0b47e58ec5141484fff25790ecb0cb49e` | `07cbf1a0373885080f5cc19c5596b231801a9ccd` |
| scripts/resume_20261128/observe_bent_coframe_search.py | 1558 | `36ee5d6a5228a67f8dc2d0c142f8f509df0a3b2eadda100cc944379085c8d313` | `fcda6545e9707f323eb978ef694e22302fd35b53` |
| .github/workflows/visible-larger-run45-coframe-phase.yml | 5250 | `08820722f0690e4c4e33c11d588772d749715c95d78afcc7a6a375059b0851d2` | `03f18de37c7c61167566e8f66aa0029fc68af79f` |
| computations/run45-coframe-phase-request.json | 26772 | `62ab55a0c0c88eb8c952423b2e1c77385c413beab838c999a06db4126f02250d` | `3799b7609a2b28adb2345af43d8702f8a2989ad5` |
| computations/run45-complete-coframe-source-and-launch-delivery.json | 26533 | `39b7b9638c910d30908dc108d4acf5babb534ccd94f4563e324a281429155ef6` | `a7d5c14704fecd37c3f43ce13d7019df4ac0a4f5` |

实际原命令在trigger不可变工作树执行：

```text
python -u scripts/resume_20261128/bent_coframe_phase.py
  --params computations/bent-coframe-phase-design-v1.json
  --geometry-source scripts/resume_20261126/r765_signed_ratio_closed_two_jets.py
  --export-source scripts/resume_20261128/closed_body_mesh_terminal.py
  --out <runner_temp>/run45-coframe-phase-<run>-<attempt>/field
```

公开ubuntu-latest 4vCPU/16GB，Python3.12.14、NumPy2.3.5、SciPy1.17.0、CPU JAX/jaxlib0.7.1与x64，原各BLAS线程1。source trigger与后续规则HEAD分离，2700秒真实pull/rebase并仅读双README差异，原observer完整发表两份独立末几何索引与每阶段返回；NFF正常rebase循环。360分钟为原平台预算，无新增子进程墙钟。只做普通完整push触发，不加额外fixture/AST/预筛门。

本条发表时run/job/PID及任何实际结果仍未知，request actual全部null。完整配置不是求解成功；每次真实返回后按全点/全文件身份登记。全闭C²嵌入、真实全t reach/同g误差、同参数精化、宏观held/商距及更优比例须分别实际支付，达到README标准以前继续。

## 实际公开入口与首四个完整粗阶段

真实触发提交 `21586d44617651b61888018d65bd5a888ad967b4`；[run 46163490136/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46163490136)，job `141035792653`。ROOT独立读取官方步骤，科学步骤实际in_progress；其控制器小原件记载科学子进程 `2026-11-28T16:08:23Z`、PID `2746`、4个逻辑CPU、affinity `[0,1,2,3]`，numpy/scipy/JAX/JAXlib为 `2.3.5/1.17.0/0.7.1/0.7.1`。完整命令身份 `13b129a45d449c40c31b0f7550bb966c94256d24cf44ca8818cedd78a467391c`。实际读取26个冻结源/参数的原path、bytes、SHA256、Git blob逐一与本次request完全一致；非仅工作流配置值。source与初次规则读取均为上述真实提交。

以下固定于 `1bfa1b4d6126ca5f5884005d0b86ae00abcd631e` 的前四个自然返回粗阶段，均完成原两个block×四次物理极分解步；每次真实线搜索记录及物理/旋转/重叠检查留原件。三低峰支及已经数学排厚的常比例对照不能混为同族胜出者。

| 设计 | 真闭物理点 | 独立relative Gram最大值 | 最大绝对主曲率 | 有序逆法弦 |
|---|---|---:|---:|---:|
| ratio-bounded-78-cut23 | `64f480fad00ec6d1d91b9af682bb71e47b23778e630334fd8618e96e06328541` | 357643687044138000 | 5882593.262852671 | 13632.010191324724 |
| ratio-bounded-79-cut30 | `07f10119f1902ca8f23f52fbe9bd41dfbe603feb8703c51f554c5ccd8ce0a59b` | 359304039626596740 | 204738.91903404417 | 13787.509830562174 |
| ratio-bounded-84-fall4 | `a18f6b1d1a018462c361c8746b5b6de8bb967866b3c0ce7f9bb0ca9a7d57276a` | 314127742063113860 | 169927.15900278988 | 12534.387555362973 |
| ratio-constant-2-2-curvature-control | `9a26c9d1d4670f4994308e8c2491040d096275d0f63d4e9a0bdf027dcd48ac5c` | 160373326091676.75 | 4462145.881245473 | 2774.184214948013 |

三个低峰支的整帽误差约 `3.1–3.6e17`；常比例对照约 `1.6037332609167675e14`。第零支最坏Gram在相位 `1.1780972450961724`、`cap-`、材料 `(.33491333933576684,.9427272727272727)`。这些都是完整独立检查的明确失败，不能用中央 `4.44e−16` 的准确或握持旋转 `4.440892098500626e−16` 掩盖。首支极分解距离 `598033246.587971`、regular projected curl `2514869.9047882273`；其他支的完整数值也保原件。各四缝物理二jet近数值舍入，但首支外缝最大 `1.1175870895385742e−8`，旋转缝约 `6.15e−14`；这些局部接缝测量不支付全g与法管。

实际第零支更新前训练极分解误差已 `39298.025082174136`，原协变Hessian峰值 `10063806566.002342`。第一步系数L2为 `20270494.710732926`，加权merit从 `1117871973726508.8` 降到 `1086768209062797.4`，下一步前polar却升到 `10543390.371899404`。因此目前原二阶量的巨大尺度支配了这组总目标，merit下降不表示真实度量改善；真正的最终独查已直接否定该步场。这个诊断来自已执行步与既定目标公式，不能升级成所有可能算法的不可行证明。

截至上述固定记录，原七粗中的前三低峰和一个对照已自然返，未把其余三参考或任一细化伪装成已完成。原各族胜出后4/8/16、两个末点各65相与七整网以及全部迭代预算保持，公开子进程继续。未来新构造/算法单独交付完整源参；原45不会因本段失败而删相、提前停或改目标。

### 原件全身份

全部完整命令、26个实际输入、物理场/NPZ/系数点身份、八步真实merit、全独查值/缺项可由以下固定原件恢复；raw只留runner，不重复入Git。

| notes下原件（固定提交同上） | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| `run45-coframe-phase-46163490136-1.json` | 26321 | `29371b20e860f34dc53d0f6dfb11f3a73b2edeba8d326930d8fed34965923f20` | `9532c945862ef11b38b39f3856a310a1568b5519` |
| `run45-coframe-phase-46163490136-1-stage-00-return.json` | 14069 | `e090d5fbadb45cacccc4df0b3e98728a264fed01cedeb4fb98b828fed1e1b1d0` | `22f971565eafaca47184ea1c48c9fcca31b7f16d` |
| `run45-coframe-phase-46163490136-1-stage-01-return.json` | 14080 | `451a56bd6577abed38040f1ac23fd326f3ede8927a3812e7aa4c5976ccb9bad5` | `94e304b25a2ee5b359278e396e91c58bf21afbef` |
| `run45-coframe-phase-46163490136-1-stage-02-return.json` | 14096 | `6eb3a10a44ada4fda3869a844aa94563b0baf912f16013d6f2122be89a8f1a37` | `f418c9afe9583b6929c226a29357c548b4cefa4c` |
| `run45-coframe-phase-46163490136-1-stage-03-return.json` | 13947 | `8259f28de6c447e84fb77e942a6a7690d30b7c92e87870018d4a8b5b7f23ad8f` | `bb8dd1547d1a1f15d0f28b2f681525ecf9dfe874` |

本次同时把HANDOFF与open§7的已闭导航移到固定 `3882b582ef0228b32da53489b2db1838c234824e` 的完整版本；全部旧科学说明、原件与最后真pull记录保留，活34/35及40/41/43/44/45/R764状态块继续随实际发布更新。课题仍未达到README。

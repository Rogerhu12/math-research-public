# R248 的首次完整生产扩展及原 polar 第11态的径向漏峰

日期：2026-11-28。状态：**真实有限数值证据与准确空间包含的实际消费**。这不是新的等距解、连续曲率上界、reach 证书或优化接受。

## 1. 原输入恢复与准确同一暖场

旧临时目录 `/tmp/visible-flex-6a65e705` 已不存在。本次按公开源码重生 gap105/v045 两个 master（40.564 秒、实际退出 0）；ramp/coast SHA 分别仍为 `0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7`、`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`，与 R233 输入逐字一致。独立目标零参数定义仍为 `dacede8a21b610d25fae4d0a5c3ffed6896b1693e9fbe7f7538234f970d7689f`。

原 97×128/192 两缓存实际自然退出 0，外层耗时 141.207/187.906 秒。按原 v2 入口每进程一步恢复前11次接受；最后原有限指标逐位复现已登记第11步：R14² = 0.21888921377279036，metric = 0.6357568322618481，曲率 = 32.99525007335012。这些是恢复继续输入，全部不计新接受。prepared 含本次真实路径/UUID，故本次 state 的文件 SHA 与旧环境不同。

## 2. 第一次实际完整前缀支撑和全 span 新节点

消费 R248 的 `6a65-cartesian-c2-support-extension.py`，把修正支撑从 `[b,S]` 扩为 `[c,S]`，其中 c=.1015625，b=.1815625，S=.9772364498716914。新增左内部 knot 是原16个 ramp 内部/末端源节点，各重3，原 b 也成为三重内部 knot。原36个径向基、147个角通道准确包含于新87×147=12789列空间。所有三个 Cartesian 分量和完整实 Fourier 通道保留；中央开柱和真正 R205 尾/平领的两阶端迹固定。

在全部54个非空新 spline span 内各添加两个 Gauss 内点，共108个新径向节点；与全部旧97个节点取并，得到205个节点、两个128/192角训练组，共65600点、918400个13+q2行。新径向权是同一物理域上的非均匀梯形权，每组半权。全部 span 至少两个正权内点，R248 的离散 H2 正定性条件得到实际覆盖。新的有限求积因此有自己的成本基线，不能把其成本67.537与旧成本.218889当同一目标的增减。

每组仅真正重算108个新源点；旧97行的背景全部六 jets 与目标 a/a_s/a_ss 数组逐字拷贝且逐字比较通过。两补源进程实际自然退出0，外层耗时161.003/210.167秒；assemble 退出0。冻结 g、几何参数、目标原始定义、全物理范围均不变。

原5292个系数逐字复制到新位置，新增7497系数严格为零，没有投影、拟合或对原系数作算术。R248 的准确七 knot 恒等式给准确数学场及全部两 jets 全域相等。另对本次205×(128+192)=65600点逐点实算新旧 spline/FFT，两组全部六 jet 最大绝对差均为0，包括108个新点和全部旧点。这个有限浮点比较不声称已经给出原背景求积、反参或所有连续域浮点误差界；原背景数值误差没有因此消失。

## 3. 同一第11态确实存在旧节点未测到的峰

| 有限观察指标 | 原97节点两组 | 新205节点两组 |
| --- | ---: | ---: |
| 相对度量谱误差 | 0.63575683226184809 | 1.5725803701099181 |
| 自身主曲率绝对值 | 32.995250073350121 | 4050.8719414697048 |
| 归一化 Gram 行列式 η | 0.83702772366715705 | 0.041374154617866581 |
| held 见证最小距离 | 0.74495134414928588 | 0.74492169823382548 |
| 面积比 σ | 0.9148921923741381 | 0.20340637801668507 |

新最坏 metric 采样点为 `(s,u)=(0.5286291493320606, 5.432337296832351)`，E−1=1.5725549478374758，F/a=−.006269470312790787，G/a²−1=.026445653308943662。

新最坏曲率采样点为 `(s,u)=(0.5337244732824561, 3π/2)`，两个自身主曲率约为 `(0.007584350310025911, -4050.871941469705)`。同 s、u 的面积比约.2034063780，E=.04056114591，F/a约4.74e−14，G/a²=1.020044027；实际经线速度约.201398，源经线速度约.931308，修正经线速度约.874586。

新完整成本 R14²=67.53714420829019，分解为 metric 4.744229702178739、curvature 62.78078758395111、geometry 0、area .012126922160342602。新采样曲率约4050.87是一个已计算到的值，不是全域最大值的严格上界；原32.995同样只保持其97节点有限语义。当前暖场显然不能按原33的采样值当作厚度合格。

本条的新优化接受数为0。随后完整12789列真实求解另行登记；不得用有限成本下降替代全域等距、连续浸入或全闭 reach。

## 4. 复生命令与实际身份

先按 `6a65-geometry-polar-v2-actual-complete-baseline` 的公开命令重生原 prepared，并逐进程用 `6a65-geometry-nonfold-polar-q2-full-normal-v2.py --steps 1` 恢复11态。随后对两个 group 分别执行：

```sh
python "$SCRIPTS/2ecf-polar-c2-prefix-prepare.py" cache \
  --scripts "$SCRIPTS" --parent-prepared "$SCRATCH/polar-recovered-prepared.json" \
  --candidate "$TOPIC/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json" \
  --target-definition "$SCRATCH/target-zero.json" \
  --ramp-master "$SCRATCH/gap105-prefix-ramp-master.npz" \
  --coast-master "$SCRATCH/gap105-prefix-coast-master.npz" \
  --prefix "$SCRATCH/polar-c2-extended" --group training
# 同一命令另用 --group observer；两实际进程都退出0之后：
python "$SCRIPTS/2ecf-polar-c2-prefix-prepare.py" assemble \
  --scripts "$SCRIPTS" --parent-prepared "$SCRATCH/polar-recovered-prepared.json" \
  --ramp-master "$SCRATCH/gap105-prefix-ramp-master.npz" \
  --prefix "$SCRATCH/polar-c2-extended"
python "$SCRIPTS/2ecf-polar-c2-prefix-solve.py" \
  --scripts "$SCRIPTS" --prepared "$SCRATCH/polar-c2-extended-prepared.json" \
  --warm-state "$SCRATCH/polar-recovered-lm11-step01-state.json" \
  --prefix "$SCRATCH/polar-c2-baseline" --steps 0
```

实际首求解进程先完整写出这里的基线，再开始任何 normal 或试步。完整原始数组/状态/回执只在临时输出目录；本条仅发布源码、参数、摘要及SHA。

| 对象 | SHA-256 |
| --- | --- |
| `2ecf-polar-c2-prefix-prepare.py` | `46717cf593c1dc3a309a9e983e0a2440eed14eb9c83f9f6359a25a5f8e45b010` |
| `2ecf-polar-c2-prefix-solve.py` | `0a5bee1762c9a3424a544f6f4a211f07558dc7f2f22419da80b4b7ce902df928` |
| `2ecf-polar-c2-prefix-warm-audit.py` | `4a17671f95ae6f35a89c766ba84b76332234770a2e5adce20ac5215e8e218f53` |
| `polar-c2-extended-prepared.json` | `e8803bd9fd40c5e1edb298af42ed3b78585ebb02914e4aee26cf75a79daf8a03` |
| `polar-recovered-lm11-step01-state.json` | `8af9963178ee562cf42685f593823bc282e3302754d40c609c8cf540898b60f5` |
| `polar-c2-step01-initial.json` | `3b6dd729118113bda7f2d0edb36fa67d2095ac10a88a92bd8022043f97fce689` |
| `polar-c2-warm-audit.json` | `19785554ca786397c341cdad500eee97017bcb00d4e1513794d950ea0f1549d7` |
| `extended-cache-training-exit.json` | `92d58031db83723b7e5e35d5023f89a73a01df3855a3a4e314e3a216cc2f2882` |
| `extended-cache-observer-exit.json` | `c58638c7d1573af9d385ca5ae4a5b70384bebac8706485dd4cf5187e7f8443e2` |

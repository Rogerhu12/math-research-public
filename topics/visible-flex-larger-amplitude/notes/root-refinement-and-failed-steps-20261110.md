# 真实求解的几个失败步与强前缀二级 boost

2026-11-10，visible-larger-astra-20261110。**状态：数值记录；都不是闭曲面完成结果。**

## 1. 减小负 cos4 的进一步尝试

从成功的 `root-neck-eighth-balanced-q4-q003-m8.json.gz` 出发，保持 q=.003，把二次律 q4=−scale·q² 的 scale 从3降到1，使用同一 all-knots C² 数值坐标与 M8。实际边值求解到2104节点后触及节点上限，最大相对配点残差3.8904381e−6；真实Newton有164个 merit 拒绝、5次无可接受步。未报告合格的 metric 或 κ。

诊断文件是 `root-neck-small-balanced-q4-q003-m8-summary.json`。保存的失败迭代给 delta=.118528789867、vd=.973688144563，但它们不是成功解参数，也不构成不存在结论。原计划的下一 scale=.2 没有执行。本轮把计算优先级转移到固定 vd=.98、控制 delta 与 boost_length 的新真分支。

## 2. 旧K8 q=.02 与真实非线性尾的耦合停滞

`root-neck-q020-actual-outer-m12` 使用真实 M12 有限尾、解析 first-slope/mean Jacobian、8 shooting parts、每部分12积分步，前缀目标 tol=1e−6。第一次外层的真实尾请求成功，随后前缀对该真实切线的边值解在最大相对残差约1.4567921e−6处停滞。

配点从522增至2487，下一次需再加1536点，超过3000上限；全程没有 Frenet domain 拒绝，但有296个 merit 拒绝、10次无可接受步。边界残差已到6.91e−16，不能用它代替未过的内部配点残差。总用时约963秒；`solver_success=false`。因此只发生了一个真实尾请求，尚未通过候选点处的原非线性D-N外校正，不把这次迭代称作实际耦合成功。

配置及完整失败摘要为 `root-neck-q020-actual-outer-m12-config.json`、`root-neck-q020-actual-outer-m12-summary.json`。旧线性尾 q=.02 的成功解仍然有效；本失败不否定它，也不否定新固定速度分支。

新的实际耦合尝试使用成功的 K7/vd=.98/q=.04/M14 解，仍固定 vd，以 delta、boost_length 为设计控制；先用 tol=2e−6 和原真实尾接受条件1e−10，再独立检查全Cartesian接缝和实际metric。此项已实际成功：803节点、配点残差1.99377e−6、prefix metric4.31644e−8，真尾外复求BC2.99954e−15；tail metric4.66347e−15、fullD8.44799e−16。完整Cartesian接缝最大1.97015e−10，包含mean一阶−5.94873e−12、二阶1.39271e−10；仍有限尾而非闭解。详 `root-neck-k7-v098-q040-actual-m14-summary.json` 和 `root-neck-k7-v098-q040-actual-seam.json`。

## 3. 强 q=.38 核心的第二级提速

从已验证的 `.25→.65` 真实开放前缀
`alternative-late-boost-025to065-m96.json`（终点s=.85）继续：

- 常速度 .65 行进 .15；
- 在长度 .15 上以三次Hermite速度把 .65 提到 .87；
- 到 s=1.15，a=1.39859375，a'=.87。

两次积分的物理 profile、初始数据和区间完全一致，只改变表示与积分精度。M128从原M96初值补零高模，继承的前缀误差仍单独保留。

| 表示 | 角向点数 | rtol / 最大步长 | 第二级段 metric 最大样本 | 最小 Frenet margin | 该段 κ 最大样本 | 核心见证到此段最小距离 |
|---|---:|---|---:|---:|---:|---:|
| M96 | 1536 | 2e−11 / .0005 | 3.02066e−4 | .0605074 | 5.37162 | .723662 |
| M128 | 2048 | 1e−12 / .0003 | 1.18681e−4 | .0776672 | 5.36454 | .723647 |

两次都到达目标且未退出实际平方根域。误差有所下降，但仍大于1e−6，不构成完成的同g精度结果。更关键的是，这一段已经遮挡原本的 .76 位移见证；不能把 `.65` 前缀的 .76 直接转给第二级 boost。终点平均高度1.053642、最高点约1.142850、以原点计的最大球半径约1.847651。只有开放片，后续 turn、neck、尾及帽尚未构造。

重现命令（在课题目录）：

```bash
python computations/alternative-controlled-profile.py \
  --input notes/alternative-late-boost-025to065-m96.json \
  --M 96 --N 1536 --coast .15 --turn-length .15 --turn-speed .87 \
  --rtol 2e-11 --maxstep .0005 --steps 60 \
  --out notes/root-strong-double-boost-q038-m96.json

python computations/alternative-controlled-profile.py \
  --input notes/alternative-late-boost-025to065-m96.json \
  --M 128 --N 2048 --coast .15 --turn-length .15 --turn-speed .87 \
  --rtol 1e-12 --maxstep .0003 --steps 60 \
  --out notes/root-strong-double-boost-q038-m128.json
```

两个输出均记录完整系数状态、source/input hashes及参数。当前没有继续暴力提高该IVP阶数：其空间位移代价尚未解决，优先推进真实边值分支。

## 4. 旧q=.02实际耦合的重启成功及因果限制

从第2节保存的失败迭代重新启动，`root-neck-q020-actual-refresh-m12` 用同一实际有限尾和同一接受条件，6次外层配点迭代后以952节点通过：最大配点残差9.96295e−7，prefix metric3.01158e−9、flow defect3.2433e−9、Cartesian Darboux6.69456e−7；真非线性尾复求的physical BC为5.23043e−19、tail残差2.33324e−10。κ样本8.409930，height1.860029。这次只把旧失败点变成了真实有限耦合成功，不是闭合结论。

配置选择了新增的`refresh` Newton后端，但其计数`stale_lu_retries=0`、`fresh_lu_recovered=0`：新回退分支根本没有执行。因此**不能把重启成功归因于Jacobian刷新修复**；证据只支持较近的保存迭代作为warm start后求解成功。原后端是否也能从这个warm start成功没有比较，也无必要为此额外重跑。

完整配置、摘要和最终实际尾响应见`root-neck-q020-actual-refresh-m12-config.json`、`-summary.json`、`-tail-response_0003.json.gz`。失败摘要仍保留；不删除先前未过内部残差的事实。

## 5. 第三个核心谐波的真实三控制试算

`computations/root_triple_core_bvp.py`在q2、q4原有约束之外指定cos6系数，以delta、boost_length、boost_speed三个真实物理量为未知设计控制；cos8及以上仍由BVP解出。每次改变这些量都产生新g，绝不标作同g加密。warm经过真实物理角拉回和明确的入口变形，只作为初猜，保存成功必须通过原非线性前缀与完整有限linear-DN边界。

基点为旧loop K8/sync K7、vd=.98的q=.07/M18成功解。自然cos6为−.00017803844320923。

| 目标cos6 | 求解状态 | metric | κ最大样本 | height最大样本 | 解释 |
|---|---|---:|---:|---:|---|
| −.0000890192216046（绝对值减半） | 失败，下一mesh3429超2800 | 未报告合格值 | 未报告 | 未报告 | 两轮内部残差.0257→.0362，21次domain拒绝、54次merit拒绝；只能判断此大warm步失败 |
| −.000186940365370（绝对值增5%） | 成功，1203节点 | 9.49533e−9 | 8.812083 | 1.872068 | 4轮，最大内部残差9.93e−7，真有限linear-DN BC4.78e−19 |

成功点的设计量为delta=.12128844133、boost_length=.17393595598、boost_speed=.88667149452。比原基点height下降约.01394，但κ上升，必要局部预算乘积`κ*2height`约32.99，未优于原约32.93。不能单凭height下降称作整曲面优化。该点尾口高度最大2.31906e−5；尚无实际非线性尾耦合、固定g加密、完整曲率包络或闭图。

相应文件为`root-neck-triple-q070-c6half-m18-summary.json`（仅失败摘要）及`root-neck-triple-q070-c6more-m18*`（真实成功checkpoint与摘要）。负数科学记数CLI参数应写成`--third-support=-8.90192216046e-5`；曾有一次分开传值被argparse拒绝，未进入数学求解，不计作数学失败。

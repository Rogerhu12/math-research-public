# q=.04真实非线性尾耦合的固定度量加密

2026-11-10，visible-larger-astra-20261110。**状态：实际有限耦合问题的数值收敛记录；不是完整闭曲面的完成声明。**

## 冻结哪些量

基准为已成功的`root-neck-k7-v098-q040-actual-m14.json.gz`。新增包装器`root_actual_fixed_refinement.py`冻结其全部物理profile、tail parameters、cut、弧长、gauge及物理角reference chart。固定profile后的未知数改为全部核心支撑系数；第一系数通过`log(actual_q/gauge_q)`求解，gauge保持.04。求得的第一系数微变是固定g的未知嵌入场更新，不是重新选取设计度量。

真实尾仍保持8个物理层、8个shooting部分；完整高度向量送入实际非线性D-N，每轮候选处重新求原非线性尾，接受条件仍为physical BC≤1e−10。没有扩大cache、改为线性代理或重置每个纬圈的平均高度。只增加Fourier阶数、角向积分点、前缀配点与精度；线性远端仅作原实际有限尾求解器的端条件。

旧16项port通过`--frozen-port`验明原样保留，较高项来自实际2048步线性积分；physical parameters/cut按canonical JSON逐字相同。`root_fixed_chain_audit.py`再独立拒绝任何profile、tail、cut、reference chart、gauge、物理长度或有限尾拓扑变化。

## 已完成数值

| checkpoint | M / 角向N | 配点数 / tol | prefix metric | flow defect | Cartesian Darboux | 真尾BC |
|---|---|---|---:|---:|---:|---:|
| 基准实际耦合M14 | 14 / 256 | 803 / 2e−6 | 4.31644e−8 | 3.38741e−8 | 6.07372e−6 | 3.00e−15 |
| frozen M14 | 14 / 256 | 3040 / 1e−8 | 1.96993e−10 | 1.26160e−9 | 1.14224e−7 | 8.56e−19 |
| frozen M20 | 20 / 512 | 3040 / 1e−8 | 2.88316e−11 | 6.66760e−11 | 9.02627e−8 | 2.61e−19 |

后两者height分别1.843272871751492与1.843272871751495；κ样本8.38687557287与8.38687557249。真正未改变的g和chart的hash、原checkpoint及系数块hash、各项tail audit均在`root-fixed-neck-q040-through-m20-chain.json`。

对相同物理s、相同材料角θ及完整平均高度作两jet比较：

| 相邻两解 | 位置差最大样本 | Fs差 | Fθ差 | Fss差 | Fsθ差 | Fθθ差 |
|---|---:|---:|---:|---:|---:|---:|
| 基准→frozen M14 | 2.52604e−8 | 7.46053e−8 | 3.85731e−8 | 3.02745e−4 | 1.53471e−7 | 8.07784e−8 |
| frozen M14→M20 | 4.36183e−11 | 2.31936e−9 | 1.24853e−9 | 1.49179e−7 | 6.38038e−8 | 3.44350e−8 |

这里的角向网格为256，径向含两个保存网格及201个补点，属于空间样本比较，不能直接替代连续包络。保存的物理PPoly是五次，未把源求解器三次插值错误当作最终C²表示。

## 完整尾缝

`root-fixed-neck-q040-m20-seam.json`用g−dZ²的平面连接重建完整Cartesian两jet；N512/1024结果一致至约1e−15。最大误差为Fss约6.81e−12，位置约1.01e−13；平均高度一阶差2.39e−13、二阶差−5.56e−12，角向holonomy≤1.40e−15、平面闭合≤6.15e−16。接缝高度平移只配零阶，未拿它消去两阶导数。

## 精确复现

从本课题目录运行；`SOURCE`仅表示经依赖manifest重建的源topic路径，不能改用另一会话的活动源文件。所需config已保存，原profile由包装器自动写出冻结副本。

```bash
python -u computations/root_actual_fixed_refinement.py \
  --fixed-reference notes/root-neck-k7-v098-q040-actual-m14.json.gz \
  --tail-config notes/root-fixed-neck-q040-m14-config.json \
  --client analytic-first --coupling outer --source-topic "$SOURCE" \
  --port computations/alternative-neck-provider-smallcut30-port.json \
  --restart notes/root-neck-k7-v098-q040-actual-m14.json.gz \
  --modes 14 --angular 256 --nodes 0 --tol 1e-8 --max-nodes 6500 \
  --out-prefix notes/root-fixed-neck-q040-m14

python -u computations/root_actual_fixed_refinement.py \
  --fixed-reference notes/root-neck-k7-v098-q040-actual-m14.json.gz \
  --tail-config notes/root-fixed-neck-q040-m20-config.json \
  --client analytic-first --coupling outer --source-topic "$SOURCE" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --frozen-port computations/alternative-neck-provider-smallcut30-port.json \
  --restart notes/root-fixed-neck-q040-m14.json.gz \
  --modes 20 --angular 512 --nodes 0 --tol 1e-8 --max-nodes 6500 \
  --out-prefix notes/root-fixed-neck-q040-m20

python computations/root_fixed_chain_audit.py --source-topic "$SOURCE" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --checkpoints notes/root-neck-k7-v098-q040-actual-m14.json.gz \
    notes/root-fixed-neck-q040-m14.json.gz notes/root-fixed-neck-q040-m20.json.gz \
  --angular 256 --out notes/root-fixed-neck-q040-through-m20-chain.json
```

M28/N768/tol1e−10首轮在真实尾成功后，前缀只打印迭代表头即以exit137被外部终止，没有可验收的前缀结果。尾响应本身真实收敛至1.48886e−10并已保存；资源耗尽仅是怀疑，当前环境没有可读cgroup计数，不能把它当作已确认原因，更不能作数学失败。

现按完全相同物理数据和容差重试`root-fixed-neck-q040-m28-batched`：只将独立的径向flow/Jacobian求值分为48点小批，最终完整Jacobian仍供给原BVP。19点直接整批/5点分批比较见`root-radial-batching-check.json`，差异仅为矩阵运算舍入量级；这不改角向积分、方程、网格或接受门槛。真实已收敛M28尾包作warm input，仍重新走原非线性尾验收。

即使有限前缀和尾的数值误差继续下降，仍欠全频无限C²尾、与帽的精确闭合、该闭图的位移和全时reach。固定taper的极小非零缺陷不支付第5条。

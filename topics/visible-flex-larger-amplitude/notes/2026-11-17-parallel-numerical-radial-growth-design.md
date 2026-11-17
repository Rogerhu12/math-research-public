# 固定径向增长比例的新标量设计：c=.95 未接受

2026-11-17，Astra-larger-parallel-16f63c8b-20261117。**明确的新g设计及有限计算负结果。** 降低参考半径增长不等于已经降低真实闭面D；本次没有接受新几何。

## 1. 一次指定的整个标量函数

以已刊 exact-rational/quintic/解析延伸的 $a_{\rm base}(s)$ 为基础，选定正数c，定义

$$a_c(s)=1+c(a_{\rm base}(s)-1),\quad
 a_c'(s)=c a_{\rm base}'(s),\quad
 a_c''(s)=c a_{\rm base}''(s).$$

核心半径仍为1。这同时改变参考函数及其真实一、二阶导数，是新的共同度量设计 $ds^2+a_c(s)^2d\theta^2$。它不是旧g的网格精化；若获得候选，c和完整函数须在后续精化中冻结。数值程序的双精度评价不是严格区间包围。

[GrowthProfile](../scripts/parallel_20261117_growth_profile.py) 组合原Profile，不把比例缩放后的曲线误写为同一个常曲率圆弧；报告明确区分原 `base_angular_curvature` 与新的函数定义。下述驱动完整保留338维Frenet方程、全部模及mean状态，仍用真实新 $a_c'/a_c$ 计算。

## 2. 首次具体有限边界问题

接受父为 .992 M112/N2048 b677，SHA

```text
b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25
```

本次c=.95、duration0，整个区间仍为[0,.992]。固定前三核心系数

```text
.4619073494154277, -.05969451246161594, .015730056624372334
```

其余核心系数是未知状态。保留接受父保存的109条深端矩阵及右端，作为本次明确的有限设计约束。该选择并未证明新g的真实尾DN；也没有在运行中随试点重算边界。浅端229行加深端109行总计338。

设置tol1e−7、bc_tol1e−11、max_nodes1600、完整separated QR、已有同点fresh-J重试；没有删行、降频或以失败旧态作为父。

## 3. 实际失败范围

运行1809.0164秒，486→1454节点，之后需再增2900节点，超过1600预算；solver返回status1。最终

```text
collocation RMS = .03448569586422986
boundary max = 6.938893903907228e−18
```

最后状态仍不符合原本接受标准。其ODE诊断采样Gram分量约.016956、曲率约18074，不能用于真实C²几何或reach声明；低边界剩余不抵消内部失败。打印出来的core gap .96000759和直径proxy3.50282亦不计作已实现改善。

本结果只记录该c、这组保存边界、初猜、算法和预算的终态，不证明新的标量族无解。更小比例改动c=.995已经从原b677接受父独立启动，未使用本次失败态，结果未返回时不预填接受。

## 4. 源码与完整复现

```text
parallel_20261117_growth_profile.py
7a6348fa54a846c66f58c99676c9018cfdc7e994d93af0900fea66b465c42ef4
parallel_20261117_continue_growth.py
0b51cd0a46b149b6a67bd9697833a70656aba2f38c40f879c1c76662a19de62d
```

原BaseProfile SHA `08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3`；完整Frenet符号源 SHA `7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831`；使用既有 `computations/geometry_20261114_separated_qr_bvp.py`，并未更换线性方程或容量界。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue_growth.py \
 --input /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
 --growth-scale .95 --duration 0 --fixed-modes 3 --modes 112 --angles 2048 \
 --tol 1e-7 --max-nodes 1600 \
 --out /workspace/scratch/16f63c8bce6b/parallel-growth095-m112.json.gz
```

输出SHA `208e75154595abb6a5e649171e2bce485b7f9aa2c34365c6493f39b19cbfca43`。raw/QR临时对象不入库。新标量的实际几何读出必须用对应GrowthProfile，不能拿原未缩放Profile给它套度量；此处因未接受，没有冒用原readout。

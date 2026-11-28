# HF 实际曲面的新正长度旋转度量

**有限设计与完整重算。** 从[真实 HF64M80、固定 W、准确端口及角依赖径钟](2026-11-28-2ecf-strong-hf-true-radial-material-clock.md)重生母场。固定原材料标签 $x$、母场共用的径向函数 $a_0(x)$、真实母位置 $X(x,u)$。用端点三系数精确为零的五次 B 样条行 $B(x)$ 定义两个 45 维系数 $e,c$。定义新物理坐标与旋转度量
$$
s(x)=x+\int_b^x(\sqrt{1+B(t)e}-1)\,dt,\qquad
g=ds^2+a_0(x(s))^2[1+B(x(s))c]du^2 .
$$
在修改区外以端值平移 $s$，原 cuff 保留。两平方因子系数盒为 $[.8,1.2]$，由样条非负及单位分拆有全域正性。端值、一阶、二阶导数严格匹配。输出表中的数值长度用各独立样条片上 24 点 Gauss 积分。目标定义由系数与积分式给定。实际位置取 $X(x(s),u)$，按链式重算两阶导数，原 G10 积分权乘 $ds/dx$。前置场的 36 个角半径设计系数逐位与 HF 输入相同。

用两张 958 径点 G10（128、192 角）的全体材料点。固定 20 个等距测试切向，逐径点按全材料角取极值，解成对的上下矩阵二次型约束，附系数盒和速度平方一阶导数界 3、角半径比平方一阶界 2、二阶界 45。指定 $\int Be=2(.006)+(.006)^2/(S-b)$，实际 $\Delta S=.005947600505646481$，新 cut 为 .9831840503773379。九次二分后有限测试方向的浮点可行窗口为 [.11689453125,.117578125]。复核时直接取每个点的真实双特征值，双 G10 最大值为 .1182797429010514。上述窗口不界定连续最优值。

| 实际位置／网格 | 原 $g$ 的 metric | 新 $g$ 的 metric | 新 $g$ 曲率 | 新 $g$ held |
|---|---:|---:|---:|---:|
| G10，128 角 | .1139593901 | .1175915784 | 28.87184579 | .6581891770 |
| G10，192 角 | .1192061125 | .1182797429 | 28.87184579 | .6581891770 |
| 独立 G11，668×256 | .1205127434 | .1216074720 | 28.82481986 | .6582743032 |

每个 G10 的原 14 行综合成本分别为 .02552112767、.02551712870，共 .05103825637。倒面积行与原七个几何 guide 为零，曲率 guide 保留。G11 额外 540 径点及错移角始终在训练外。新 $g$ 两个曲率导数均重算，G11 样本上 $|a_{ss}/a|$ 最大 23.20346718。位置求解计数从零起。这个新输入尚无等距、全闭 reach 和可见性证书。

前一项对比将相同平方因子参数化用于完整旧位置加真实 6615 Cartesian 及 36 角半径设计的母场。半无限方向分离过程的 35 次截断不足以确定离散最优，浮点区间 [.14522078,.16942425]。实际输出 $\Delta S=.01856422$，G10 .16926962、G11 .16892355，曲率 18.04139、held .67959510。两项明确使用不同源与不同 $g$。

## 复算

使用[原正材料长度记录](2026-11-28-2ecf-strong-positive-meridian-length.md)的 SCRIPTS、DATA、common 与 G11 生成步骤，以及[HF 物理径钟记录](2026-11-28-2ecf-strong-hf-true-radial-material-clock.md)的准确原场、ramp、coast、径钟。SCRIPTS 为主题 scripts，DATA 为缓存与母场所在目录，HF 为重生的 HF 输出目录。下列文件名对应本次运行。四个积分与原曲面缓存不入库。

```bash
hfargs=("${common[@]}" --observer "$DATA/polar-physical-H65-independent.json" --hf-helpers "$SCRIPTS" --field "$HF/strong-physical-hf64m80-W.json.field.npz" --angular-clock "$HF/strong-hf-physical-radial-clock01.json" --ramp "$DATA/gap105-prefix-ramp-master.npz" --coast "$DATA/gap105-prefix-coast-master.npz")
python "$SCRIPTS/2ecf-strong-clock-diagonal-minimax.py" "${common[@]}" --observer "$DATA/polar-physical-H65-independent.json" --output clock-diagonal-chebyshev.json
python "$SCRIPTS/2ecf-strong-hf-diagonal-clock.py" "${hfargs[@]}" --delta .006 --box .20 --speed-first 3 --radius-first 2 --radius-second 45 --directions 20 --bisections 9 --output clock-hf-diagonal-d006.json
```

旧位置对比报告 SHA-256 为 `70c50a8104c78ac70ef6910cdb9151cf25302435041dcb27b89c57bc50ca79c3`。新 HF 度量定义 SHA-256 为 `b020fbbfcffde36b92fef17c278d52873a11cc90b8e33dbd765ff513774f1d1c`，本次新输入完整报告为 `60a97363af2b395f210de3dc7c2f509f098c53cc6c931d056693d9ac3543a0b1`。报告保存了每个 binary64 系数的十六进制字面值、源哈希及各自真实计时。再生时对比定义和物理数值。

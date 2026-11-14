# 准确仿射族的全核心支持函数与跨腰圈对数门

状态：**环境恢复后从零完成全覆盖与对数门组装。** 这次169个径向
闭单元全部通过，没有细分或失败，准确 Fraction 覆盖验证为 true。
丢失前仅有50个单元的进度没有沿用。

全部结论同时覆盖同一个准确 R57 仿射族的
$|\delta|\le\operatorname{binary64}(.01)$、
$|x|\le\operatorname{binary64}(.24)$ 及全部实角。原始 phase/mean
准确取 $c_0+\delta v$、$\alpha_0+\delta w$，随后作物理权重、显式
偶奇平均、准确 height slope 积分及真实无限 R33 原函数。没有作
Gaussian 卷积，也没有替换成 rounded predictor 或更大的独立控制盒。

## 1. 准确输入和四个不同几何量

原点 `type_fixed_step02_d5_jet_interval_inputs.npz` SHA256：

`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。

方向 `type_fixed_step02_d5_actual_parameter_direction.npz` SHA256：

`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。

始终采用

$$
\mathscr C=F_\theta\times F_x=aT\times F_x,\quad
\mathrm{area}=|\mathscr C|,\quad \nu=\mathscr C/\mathrm{area},
$$

$$
N_{\rm raw}=-a^2F_x\cdot(T\times T_\theta),\quad
N=N_{\rm raw}/\mathrm{area},\quad
J=F\cdot\mathscr C,\quad
h=F\cdot\nu=J/\mathrm{area},\quad
\zeta=h/|F|.
$$

先证明 $J>0$，已经排除 $\mathscr C=0$ 与 $F=0$，因此定义
单位法向及上述商不循环。每个闭单元上分别作有向除法，再取全域
极值；表中常数不是用不同位置的全局极值随意相除。

| 连续量 | 整个参数 / 核心安全界 |
|---|---:|
| $N_{\rm raw}$ | $<-.39098570$ |
| $N$ | $<-.31819107$ |
| $J$ | $>1.13806491$ |
| $h$ | $>.80589087$ |
| $\zeta$ | $>.68787339$ |
| 面积因子 | $.97140270<\mathrm{area}<1.41218241$ |
| $|F|$ 上界 | $<1.17505412$ |
| $|F_x|$ 上界 | $<1.28960301$ |

面积的新下界来自逐单元 Cauchy 不等式
$\mathrm{area}\ge J_-/|F|_+$。同理 $|F|\ge h_->0$。
负的 $N_{\rm raw}$ 除以正面积时，上界采用面积上界，其方向正确。

## 2. 同一真实对象的有限计算

源码只对冻结 `CoreTarget` 增加准确仿射相位和 mean 方向。高度
原函数也同步改为准确的
$Z_0+\delta Z_1$；$Z_1$ 是 $\sum_jw_jZ_j'$ 的准确积分再取奇部。
如果只改 slope 而保留原高度原函数，会定义另一个图，本实现没有
这样做。两个预检单元上已核高度原函数的一阶导包络与新 slope
相交，目标 $E$ 包络与原仿射 helper 相交；全覆盖随后从零重算。

径向分割含全部原、反射 knots 及0、右端。闭单元使用准确有理
中点与完整多项式 Taylor，因此相邻仅差一个 binary64 间距的
小 span 也不会跳过。phase 方向在径向 jet 层保持仿射形式。

角向原函数使用 quarter DFT 256，对应全圈1024点及最高
Cartesian频率509。直接区间三角运算和逐次向外 DFT 没有使用
未计费的浮点 FFT。真实无限原函数的截断与 alias 先加入节点
包络，再计算叉积和支持函数；全域最大尾费用分别为

$$
\epsilon_F\le3.37832\cdot10^{-16},\qquad
\epsilon_{F_x}\le3.03574\cdot10^{-14}.
$$

几何不变量按四重周期用4096个四分之一周期角节点，并扣除真实
角 Lipschitz 常数乘半网格宽 $\pi/(4\cdot4096)$。所用恒等式

$$
F_\theta=aT,\qquad F_{x\theta}=a'T+aT_x
$$

属于无限对象。它们给节点间的向量范数与几何三重积费用。
例如

$$
|\partial_\theta N_{\rm raw}|
\le a_+^2\{a_+\|T_x\|\|T_\theta\|
                  +\|F_x\|\|T_{\theta\theta}\|\},
$$

$$
|J_\theta|\le a_+\|F\|
\{\|T_\theta\|\|F_x\|+a_+\|T_x\|\}.
$$

完整闭 span、全部角间隙与整个实参数区间都被覆盖，故没有将
节点最小值充作连续结论。显式反射使 $N_{\rm raw},N,J,h,\zeta$
在负半轴具有相同值；并非假定旧 binary64 knots 自动反射。

## 3. 跨腰圈的正因子与 $\ell$

同族标量证书已实际重跑，给 $Q=F_z/x\ge .944828997102311$，其中
$x=0$ 取准确连续延拓。定义

$$
g_*=Q/|F|>0,\qquad u_z=F_z/|F|=xg_*,\qquad
\ell=\partial_\theta\log g_*.
$$

于是整个核心（包括腰圈）准确有
$(\partial_\theta-\ell)u_z=0$。这是同一实际图的平移核修正，
不用任意核心 cutoff，也没有把 $g_*$ 混同为面积平方 $G$。

有向组装给出安全常数

$$
.80407275<g_*<1.68792978,\qquad
|\ell|<1.80532198,
$$

$$
|\ell_\theta|<59.23091975,\qquad |\ell_x|<27.66332514.
$$

推导使用 $\ell=Q_\theta/Q-(F\cdot F_\theta)/(F\cdot F)$，
$|F|\ge h_-$，以及同一几何报告中的 $F_x,T_x,T_\theta$ 上界。
若 $a_j,g_j$ 为对应径向导数界、最大角频率为96，则

$$
|Q_{\theta\theta}|\le96a_0g_1,\qquad
|Q_{x\theta}|\le\tfrac12\{a_2g_0+2a_1g_1+a_0(g_2+g_0g_1^2)\}.
$$

后二式由准确径向奇性消去 $x=0$ 分母。对 $\log|F|$ 再求一次
导数的界分别为 $3a_0^2/h_-^2+a_0\|T_\theta\|/h_-$ 与
$3\|F_x\|a_0/h_-^2+(a_1+a_0\|T_x\|)/h_-$，所有商均向外
计算。样条给 $F\in C^4\cap W^{5,\infty}$；按
$Q=\int_0^1F_{x,z}(tx)dt$，$Q,g_*,\ell$ 至少为
$C^3\cap W^{4,\infty}$（每个固定有限角导数），满足相应 strict
区所需的较低径向正则性，但没有声明整体径向 $C^\infty$。

## 4. 冻结文件与重放

几何源码 `fourfold_phase_affine_core_interval.py` SHA256：

`748f5a43a51e3c4a7f51af387b9867522c48375c00afcb4b955cbf55cf49976f`。

几何报告 `type_fixed_step02_d5_affine_core_interval.json` SHA256：

`278bf0e855f9b4a8bfebb37ff1564659c874f143b394bbb81503a228910dbf51`。

对数源码 `fourfold_phase_affine_log_ground_state_gate.py` SHA256：

`197a4eb4c805ec87f02c45dd80cae2379dcd621c8d5b7386b3c41dff5be329da`。

对数报告 `type_fixed_step02_d5_affine_log_ground_state_gate.json`
SHA256：

`8805454a56f2c69e670221b4b54c46a30d87f1ca034e036dcd1244ef1f647aa0`。

两份报告均位于 `data/phase_ring_continuation/`；对数报告内部还保存
几何、标量两证书 hash。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_core_interval.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --parameter-left -.01 --parameter-right .01 --core .24 \
  --quarter-nodes 256 --angular-nodes 4096 \
  --out /tmp/visible-D5-affine-core-interval.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_log_ground_state_gate.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --scalar-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_affine_core_scalar_gate.json \
  --core-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_affine_core_interval.json \
  --out /tmp/visible-D5-affine-log-ground-state-gate.json
```

几何扫描每10次及每次二分保存进度，可 `--resume`；所有输入、方向、
源、依赖与参数须精确匹配。第一条若输出新路径，应把第二条
`--core-certificate` 改成该新报告；其运行耗时不同会改变文件 hash。

本包仅付整个实仿射核心的几何与正对数因子。不自行给复条带、
实际返回误差、非径向全频逆、正帽、残差方程解或闭合可见等距族。

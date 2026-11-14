# R73：同一精确参数小管在整个实核心上的复角分母门

2026-11-12，constructive-route。

**已证明并完成全部有限覆盖：** 下述同一精确 affine 家族，在
$|\delta-\delta_5|\le 5\times10^{-7}$、整个保存的实核心和物理角带
$|\operatorname{Im}\theta|\le1/56$ 上，原始二型分母 $N_{\rm raw}$
一致非零。本文使用 R57 已付的真实无限 primitive 实界与 R59
移动 frame 充分条件。径向变量和参数均保持为实数；没有据此得到
复时间域、完整流、返回映射或闭曲面非线性解。

## 1. 准确对象与范围

参数中心及半径为准确有理数

$$
 \delta_5=-\frac{7789843107295549}{4611686018427387904},
 \qquad \varepsilon=\frac1{2000000}.
 \tag{73.1}
$$

原始 spline 输入、方向及准确对象描述分别是

| 文件（均在 `data/phase_ring_continuation/`） | SHA256 |
|---|---|
| `type_fixed_step02_d5_jet_interval_inputs.npz` | `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b` |
| `type_fixed_step02_d5_actual_parameter_direction.npz` | `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab` |
| `type_fixed_step02_d5_exact_affine_step5_object.json` | `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` |

每个保存的 binary64 控制点和方向都按其准确 dyadic 值解释。
先以准确 affine 公式改变 phase 控制点与三项 mean 参数，再作既定
偶奇对称化，最后使用 R33 的真实无限角原函数。没有先将新的控制点
舍入为另一张 rounded 图，也没有以有限角原函数替代真实图。

径向范围准确为

$$
 |r|\le r_*:=\frac{1080863910568919}{4503599627370496}
               =\operatorname{binary64}(0.24).
 \tag{73.2}
$$

验证器将两个准确参数端点向外包入

$$
 [\delta_-,\delta_+]
 =[\operatorname{binary64}(-0.0016896529640502134),
   \operatorname{binary64}(-0.0016886529640502133)]
 \tag{73.3}
$$

并用 `Fraction` 逐项验证

$$
 [-\operatorname{binary64}(.01),\operatorname{binary64}(.01)]
 \supseteq[\delta_-,\delta_+]
 \supseteq[\delta_5-\varepsilon,\delta_5+\varepsilon].
 \tag{73.4}
$$

物理角宽度 $1/56$ 也向外包入准确 binary64

$$
 S_*:=\frac{5146971002709139}{288230376151711744}>\frac1{56}.
 \tag{73.5}
$$

因此在验证中使用稍大的参数与角域，只会增强对所声明准确域的覆盖。
归一物理角 $x=4\theta$ 的相应系数带为 $1/14$；这不是完整流的
初值标签带，不允许在未控制轨迹复像时将两者等同。

## 2. 同一实证书的继承与独立 scalar 包络

完成的 R57 实证书为
`type_fixed_step02_d5_parameter_N_interval.json`，SHA256
`b52537b755e7b5475dc945a5781c0d57a93e71ccdf39ec90891c236fcae2438a`。
其原始参数区间就是 (73.4) 左侧，且它在 $[0,r_*]$ 给出 592 个
相邻准确 dyadic 闭单元，对原独立控制盒的真实无限 primitive 已付
$X=F_r$ 的水平模、竖分量模及正下界，以及实 $N_{\rm raw}<0$。

包含关系 (73.4) 表明，本文每一个准确 affine 图都属于该已付范围。
因此这些实几何界可直接继承，且并未缩小其中的误差。另一方面，
在每个相同径向单元上，phase 和 mean 用较小参数包 (73.3) 重新求值：

$$
 c_i(\delta)=c_{i,0}+\delta d_i,\qquad
 \alpha_j(\delta)=\alpha_{j,0}+\delta e_j.
 \tag{73.6}
$$

各算术步骤向外舍入；保留各控制点之间相关性并非证明所必需，
把这些值独立包住仍含有所有实际 affine 图。五次 spline 的导数
控制点由准确差商公式逐阶区间化，闭 span 求值遵守 R55/R57 的
端点约定，包含极短相邻 binary64 knot 间隙。显式对称化保持不变。
因此新 phase/mean 包络与继承的实 $X,N_{\rm raw}$ 界针对同一图，
不存在把裸 mean 变分或旧 rounded 图的几何移用过来的步骤。

验证器检查：原实证书完成且无失败或待办；原始输入和方向的哈希
准确一致；方向 metadata 的原点一致；首单元始于 0、末单元止于
$r_*$、每一对邻接端点完全相同。负半轴由该同一显式反射覆盖。

## 3. 连续复角充分条件

沿用 R59 的准确移动 frame：

$$
 T=cU+s e_z,\quad c=\cos\gamma,\quad s=\sin\gamma,
 \quad P=1+\beta_\theta,\quad u=\gamma_\theta,
$$
$$
 Q=cX_z-s(X\cdot U),\quad v=X\cdot V,
 \qquad N_{\rm raw}=-a^2D,\quad D=PcQ-uv.
 \tag{73.7}
$$

在每个实径向闭单元及其完整实参数包上，R59 §3 由真实
$X_\theta=a'T+aT_r$ 沿竖直角线积分，给出复 $X$ 与 frame 投影上界；
有限 phase 的 cosh/sinh 系数和给出所有角导数上界。这一步使用
真实无限 primitive 的实值包络，未把截断原函数的角导数冒充 $aT$。

有限 phase 在边界的实部准确为

$$
 \operatorname{Re}P(\theta\pm iS_*)
 =1+\sum_{k\ge1}(4k)b_k\cos(4k\theta)\cosh(4kS_*).
 \tag{73.8}
$$

有限有向节点值加一阶导数乘半网格宽支付节点间隙。
两边界因实系数相同；周期调和最小值原理支付内部整个角带。
这给出 $P_->0$。R59 的连续界还给出

$$
 |c|\ge c_->0,\quad |X_z|\ge z_->0,\quad
 |Q|\ge c_-z_--S_0V_0=:Q_->0,
$$
$$
 |D|\ge P_-c_-Q_--|u|V_0=:D_->0,
 \qquad |N_{\rm raw}|\ge a_-^2D_-.
 \tag{73.9}
$$

这里 $V_0$ 包住两个水平 frame 投影，$S_0$ 包住 $|s|$。
正乘积条件全部单独核查。另保留独立的 R56 型实部门

$$
 \operatorname{Re}N_{\rm raw}(\theta+iy)
 \le N_{{\rm real},+}
       +\frac12S_*^2\|\partial_\theta^2N_{\rm raw}\|.
 \tag{73.10}
$$

若其右端为负，也给出一个模长下界。每格取两个已证明正下界的
较大值合法；若二者都不为正，必须保留失败，不能删去该径向单元。
全部 scalar 乘、加、除、cosh 和节点三角函数均使用继承的有向预算。

## 4. 已完成的全部 592 格结果

运行源为 `scripts/fourfold_phase_narrow_parameter_angle_strip.py`，
SHA256
`74970e790d68d86376eef92b1acee94cb3ea173077be48f8e7529da67824fc3c`。
它调用未更改的 R59 `strip_cell`，源码依赖哈希均写入报告。
完整报告
`data/phase_ring_continuation/type_fixed_step02_d5_step5_small_parameter_modulus_1over56.json.gz`
的 SHA256 为
`30001c1a7e7de13e89924163cdbf79c95a5a1e2269430d9f5ee93038c12f2e80`。

报告包含全部 592 个径向单元，0 失败，完整参数和连续角带均已覆盖。
逐格下界的最小保存值为
$0.22596578914855567$，因此可用更保守且准确的结论

$$
 \boxed{|N_{\rm raw}(r,\theta;\delta)|>
        \frac{2259}{10000}}
 \quad
 \left\{
 \begin{array}{l}
 |r|\le r_*,\quad r\in\mathbb R,\\
 |\delta-\delta_5|\le1/2000000,\quad\delta\in\mathbb R,\\
 |\operatorname{Im}\theta|\le1/56.
 \end{array}\right.
 \tag{73.11}
$$

保存的各格还给出 $m/N_{\rm raw}$、$G/N_{\rm raw}$ 的前两阶角导数
上界；它们由 R59 的完整商公式计算。为便于引用，取严格向上的
整数量级，可统一使用

| 商 | 零阶 | 一阶角导 | 二阶角导 |
|---|---:|---:|---:|
| $m/N_{\rm raw}$ | 9 | 7810 | 18,341,010 |
| $G/N_{\rm raw}$ | 7 | 13,406 | 58,588,972 |

这些界仅控制实 $r$ 的特征系数商。真实 $\sqrt{-K_0}$ 的分支、
时间变换和更精细的流导数需要另外计算，不把这些保守的大常数
直接代入指数后宣称可用。

重跑入口（从本课题目录运行）：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_narrow_parameter_angle_strip.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json \
  --width 1/56 --halfwidth 1/2000000 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_step5_small_parameter_modulus_1over56.json.gz
```

运行时长字段可变化；数学输入、完整覆盖、逐格不等式与依赖身份必须相同。

## 5. 更宽 $1/48$ 尝试与二阶角间隙

同一参数管、相同径向单元、相同实 primitive 界下，物理角宽度
$1/48$ 的直接 R59 门在 592 格中有 132 格未通过。完整失败报告
`type_fixed_step02_d5_step5_small_parameter_modulus_1over48.json.gz`
的 SHA256 为
`a1846d8cdf3db47d82c876c96bf80971e1356b7454d88c5816b5449d2110985c`。
它没有被较窄角带的成功结果覆盖或删除。

随后仅改进有限 $P$ 的节点间隙。令节点半间距为 $g$，在每个节点
有有向实部值 $P_j$、实角导数 $P'_j$，且

$$
 B_2\ge\sum_k(4k)^3|b_k|\cosh(4kS).
$$

对距离该节点不超过 $g$ 的任意实角，Taylor 积分余项给

$$
 \operatorname{Re}P(\theta+iS)
 \ge (P_j)_--g|P'_j|_+-\tfrac12g^2B_2.
 \tag{73.12}
$$

取全部节点的最小值，再用周期调和最小值原理，可将它与旧的一阶
下界取较大者。此处 $P$ 是准确有限 phase 导数，所以没有无穷
Fourier 尾；有向 cosh、带符号系数及所有三角函数误差仍全部保留。
其余 $c,z,Q,v,a$ 界维持同一原报告值，然后重新计算 (73.9) 和商界。
原来已经通过的格原样保留。没有只靠节点值授予连续结论。

该实现为 `scripts/fourfold_phase_angle_strip_second_gap.py`，SHA256
`591e1da6adc4a382d5af7e3f93207c07bc9f290b5ca6447a30aa6b7dd52a1336`。
全部 132 个原失败格重算后，64 格转为通过，仍有 68 格失败。
完整报告
`type_fixed_step02_d5_step5_small_parameter_modulus_second_gap_1over48.json.gz`
的 SHA256 为
`5676d00ce8f09d10dda6aec1ee3302d1a457ded0d7c24082d0fd5ef44a5dde31`。

失败只说明这些充分下界未能覆盖该范围，不证明这些单元实际存在
分母零点。R70 在另一个明确固定实径向中心对 $1/32$ 所证的四个
复零点也不得移用成这里 $1/48$ 全核心失败的解释。反过来，R70
单个时间 germ 的 $1/48$ 成功亦不得代付本文全部实核心。

## 6. 可用接口与仍未完成的部分

(73.11) 可作为这一准确参数管在每个实径向中心的共同复角锚。
扩展到任何复时间圆盘时，仍须付同一真实 germ 从该锚到复时间点的
$D$ 变化、target 根/消根商与平方根分支，并逐段付实际覆盖。
复角域与复时间域的不同成功证书不能取矩形包络拼成更大的 bidisc。

本结果没有改变此前冻结的 R59 大参数盒报告，也不替代 R65/R70
不同时间域的证明。完整两腿参考、连续缺陷、返回映射参数导数、
KAM、全 PDE 反演和本课题闭曲面的可见振幅与 reach 标准仍继续。

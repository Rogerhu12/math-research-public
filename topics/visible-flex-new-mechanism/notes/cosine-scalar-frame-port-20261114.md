# 准确余弦核心到单位正交框架的标量端口

日期：2026-11-14。实现：`../scripts/cosine_scalar_frame_port.py`。本模块是 R28 框架重构表示的端口接口，不是连接器求解或存在证明。它独立导入已冻结的准确核心和真实高阶材料导数模块，不修改物理曲线，不外推已冻结宽度。开发检查只使用人工圆与温和低模例。

基础几何见 [R9](../results/R9-rectifying-flat-core.md)、零 framing 及余弦对称见 [R24](../results/R24-space-star-height-parity-framing.md)，高阶输入推导见 [高阶材料切向接口](cosine-core-high-jets-20261114.md)。

## 1. 目标框架与两个真实端口

准确核心在固定材料坐标 \((s,\theta)\) 中满足

\[
 X_s=B,\qquad X_\theta=a_0T,
\]

其中 \(T,B\) 是中心空间曲线在隐式角 \(\phi(s,\theta)\) 处的 Frenet 切向和陪法向。正负侧的向外参数 \(t\) 分别满足

\[
 s=\sigma(w+t),\quad \sigma\in\{1,-1\},\qquad
 T_{\rm out}=T,\quad V_{\rm out}=\sigma B.
 \tag{1}
\]

实际端口为 \(t=0\)，开放核心缓冲区为 \(t<0\)。这里两个端口分别评价于 \(s=w\) 和 \(s=-w\)，不假设它们由 \(s\mapsto-s\) 的空间镜像相连。

标量参数化为

\[
 \psi=\theta+u,\qquad
 T=\frac{(-\sin\psi,\cos\psi,v)}{\sqrt{1+v^2}},
\]
\[
 N_0=(\cos\psi,\sin\psi,0),\quad M_0=T\times N_0,
 \qquad V=\cos\beta\,N_0+\sin\beta\,M_0.
 \tag{2}
\]

因为 \(r>0\)，中心曲线的水平速度 \(p=|\gamma'_{xy}|\) 严格正，材料切向的水平模也正。因此 (2) 在整个准确核心上有意义，而不是通过给小分母加常数正则化。

## 2. u 和 v 的准确值与材料二 jet

中心曲线为 \(\gamma=(r\cos\phi,r\sin\phi,z)\)。水平切向方向给

\[
 \psi(\phi)=\phi-\arctan\frac{r'(\phi)}{r(\phi)},\qquad
 u=\psi(\phi(s,\theta))-\theta,\qquad
 v=\frac{T_z}{|T_{xy}|}=\frac{z'}p.
 \tag{3}
\]

\(r>0\) 使这里的实 \(\arctan\) 分支连续。实现把材料角取同一 \([0,2\pi)\) 周期代表，并与核心返回的构造角相配；余弦对称有 \(q(0)=0\)，因此周期接缝没有额外随 \(s\) 变化的物理角常数。\(u\) 是 \(2\pi/3\) 周期的奇函数，\(v\) 同样为奇函数。

为避免对数值主值角作差分，所有导数直接由真实向量 jet 求出。对一个非零平面向量 \(H\)，记

\[
 [A,B]=A_xB_y-A_yB_x,\qquad
 \psi_i=\frac{[H,H_i]}{|H|^2},
\]
\[
 \boxed{\psi_{ij}=
 \frac{[H,H_{ij}]-\psi_i H\cdot H_j-\psi_j H\cdot H_i}{|H|^2}.}
 \tag{4}
\]

这里 \(i,j\) 是向外径向变量和同一个材料角 \(\theta\)。式 (4) 从一般非单位向量的幅角微分求得，已经包括水平模的导数，且对 \(i,j\) 对称。取 \(H=T_{xy}\) 后，\(u_i=\psi_i-\partial_i\theta\)，二阶导数则与 \(\psi\) 相同。

令 \(h=|H|\)。高度斜率的全部导数由

\[
 h_i=\frac{H\cdot H_i}{h},\qquad
 h_{ij}=\frac{H_i\cdot H_j+H\cdot H_{ij}-h_i h_j}{h},
\]
\[
 v_i=\frac{(T_z)_i-vh_i}{h},\qquad
 \boxed{v_{ij}=\frac{(T_z)_{ij}-vh_{ij}-v_i h_j-v_j h_i}{h}}
 \tag{5}
\]

给出。输入的 \(T_{ss}\) 来自 `cosine_core_high_jets.py` 的真实第五空间曲线导数及隐式材料链式公式，不是对原位置二 jet 名称的猜测。

## 3. beta 是连续周期原函数，不是采样 unwrap

为给 \(\beta\) 选定一个准确实值分支，设

\[
 p=|\gamma'_{xy}|,\quad V_c=|\gamma'|,\quad
 A=\gamma'_x\gamma''_y-\gamma'_y\gamma''_x,\quad
 \Omega=|\gamma'\times\gamma''|.
\]

正侧 \(B\) 在 \((N_0,M_0)\) 中的坐标是

\[
 F=\frac1\Omega(\mathcal L,\mathcal Q),\qquad
 \mathcal L=pz''-p'z',\qquad
 \mathcal Q=-\frac{V_cA}{p}.
 \tag{6}
\]

二者平方和为 \(\Omega^2>0\)。因而在不除以 torsion 或某个可能为零的单独分量的情况下，准确角导数为

\[
 b(\phi)=\frac{\mathcal L\mathcal Q'-\mathcal Q\mathcal L'}
                         {\mathcal L^2+\mathcal Q^2}.
 \tag{7}
\]

实现直接计算

\[
 \mathcal L'=pz'''-p''z',\qquad
 \mathcal Q'=-\frac{V_c'A+V_cA'}p+\frac{V_cAp'}{p^2},
\]

\[
 A'=\gamma'_x\gamma'''_y-\gamma'_y\gamma'''_x.
\]

由余弦高度反射，\(F\) 是偶函数且具有周期 \(P_3=2\pi/3\)，所以 \(b\) 为奇函数、每个周期的积分为零。定义

\[
 \boxed{\beta_+(\phi)=\beta_0+\int_0^\phi b(\eta)\,d\eta,\qquad
 \beta_0=\operatorname{atan2}(\mathcal Q(0),\mathcal L(0)).}
 \tag{8}
\]

则 \(\beta_+\) 是真正实值、偶且 \(P_3\) 周期的光滑分支，而不只是圆值角。它满足 \((\cos\beta_+,\sin\beta_+)=F\)。这是 R24 零 framing 在端口表示中的具体实现。单个半扇区内即使有多次转角，积分也会保留其正确累积，不能用逐点主值 \(\operatorname{atan2}\) 替代。

`BetaLiftPrimitive` 只在 \([0,\pi/3]\) 对 (7) 作固定格数、固定阶数 Gauss 求积，其他角度按偶周期代表计算。这里的**数学定义**是 (8)，偶周期关系来自准确对称定理；有限 Gauss 值的误差另行记录，尚未连续认证。

负侧取

\[
 \beta_-(s,\theta)=\beta_+(\phi(s,\theta))+\pi,
 \tag{9}
\]

对应 \(V=-B\)。\(\beta\) 的材料一、二阶导数不从求积表差分，而是对圆值向量

\[
 F_{\rm out}=(V\cdot N_0,V\cdot M_0)
\]

及其真实一、二阶 jet 使用同一一般幅角公式 (4)。所需 \(N_0,M_0\) 的导数由 (2) 和已求出的 \(\psi_i,\psi_{ij}\) 逐项叉乘求出。数值返回还核查 (8) 的相位回代误差，但这一回代误差不是全角求积误差的连续上界。

## 4. 正负侧符号与准确积分性核查

接口对每个指定的物理 \(s\) 显式记录 `outward_side`。由 (1)，

\[
 T_t=\sigma T_s,\quad T_{tt}=T_{ss},\quad
 T_{t\theta}=\sigma T_{s\theta},
\]
\[
 V_t=B_s,\quad V_{tt}=\sigma B_{ss},\quad
 V_{t\theta}=B_{s\theta}.
 \tag{10}
\]

所有纯角导数均保持相同材料角；对 \(V\) 还保留其整体 \(\sigma\) 符号。返回的标量字典键 `s,ss,st` 按该向外坐标解释，`theta,tt` 分别表示一、二阶材料角导数。

为交叉检查三个标量式，令 \(\alpha=\arctan v\)、\(C_\beta=\cos\beta\)、\(S_\beta=\sin\beta\)。残差

\[
 R=V_\theta-\partial_t(aT)
\]

在正交架 \((T,V,W=T\times V)\) 中的分量是

\[
 R_T=C_\beta\cos\alpha\,\psi_\theta+S_\beta\alpha_\theta-a',
\]
\[
 R_V=a(C_\beta\cos\alpha\,\psi_t+S_\beta\alpha_t),
\]
\[
 R_W=\beta_\theta+\sin\alpha\,\psi_\theta
      -a(S_\beta\cos\alpha\,\psi_t-C_\beta\alpha_t).
 \tag{11}
\]

在准确核心 \(a=a_0,a'=0\)，三者均应为零；开发检查把两侧标量 jet 代入 (11)，从而同时核查材料角、径向符号、\(\beta\) 分支及其导数。

## 5. API、身份和误差边界

```python
from cosine_rectifying_core import CosineRectifyingCore
from cosine_scalar_frame_port import BetaLiftPrimitive, scalar_frame_two_jets

core = CosineRectifyingCore.from_verified_report(frozen_report)
beta = BetaLiftPrimitive(core, cells=256, quadrature=16)
plus = scalar_frame_two_jets(core, +core.width, theta, beta, side=+1)
minus = scalar_frame_two_jets(core, -core.width, theta, beta, side=-1)
# plus['u'], plus['v'], plus['beta'] each contain:
# value, s, theta, ss, st, tt
```

`BetaLiftPrimitive` 与核心必须具有相同 canonical 物理身份 SHA256。结果保存完整身份、物理 \(s\)、材料 \(\theta\)、实际构造角、侧号、准确模型的浮点 \(a_0\)、弧长求积设置、材料反解残差、\(\beta\) 求积设置及相位回代误差。不会将一侧端口复制成另一侧，不会改变核心系数，不会超过 \(|s|\le w\)。

公式 (3)–(11) 针对同一准确模型成立；有限精度评价仍需要在未来连续误差证书中控制弧长、\(\phi\) 反解、\(\beta\) 原函数及各算术量。固定 Gauss 表的近似导数不被当作数学定义的导数，程序直接评价准确公式对应的 jet。若需要把最终连接器误差压到 \(10^{-6}\)，这些输入误差也要计入，而不只加密连接自由系数。

## 6. 已实际执行的合成检查

证据文件 `cosine-scalar-frame-port-check-20261114.json`。命令：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/cosine_scalar_frame_port.py \
  --check-only --out topics/visible-flex-new-mechanism/notes/cosine-scalar-frame-port-check-20261114.json
```

人工输入为单位圆柱，以及与高阶模块相同的温和例：
\(a=1/20,b=1/200,H=(1/25,-1/100,1/1000),z_0=1/11,w=1/100\)。没有运行任何研究候选或新几何优化。

| 检查 | 实际最大误差 |
| --- | --- |
| 单位圆柱两侧全部标量值/jet | \(6.67\times10^{-16}\) 以下 |
| 人工例的全部 \(u,v,\beta\) 一、二阶材料 jet 差分 | \(9.07\times10^{-9}\) 以下 |
| 从标量回代目标 \(T,V\) | \(8.89\times10^{-16}\) 以下 |
| 真正的两个人工边界 \(s=\pm w\) 与既有位置全二 jet 相容 | \(3.53\times10^{-16}\) 以下 |
| 两侧三个准确核心积分性残差 (11) | \(1.24\times10^{-15}\) 以下 |
| \(\beta\) 原函数相位回代 | \(1.19\times10^{-15}\) 以下 |
| \(\beta\) 周期/偶性 | \(1.14\times10^{-16}\) 以下 |

这里固定材料角的导数由独立正负径向增量及角增量作差分；混合导数从两个方向均交叉核查。输出为 `passed: true`，同时明确 `research_geometry_evaluated: false`、`optimization_performed: false`。这些开发结果没有证明真实宏观核心通过厚度门，也没有证明外部连接器、闭面或完整 reach。

独立只读复核：`repo_sources` 核对了 \(\mathcal L',\mathcal Q'\)、一般幅角的对称二 jet、\(\beta\) 原函数的偶周期分支与无 unwrap 实现、正负侧符号，以及 (11) 的全部三个分量；没有重复运行开发检查或评价真实候选。

## 7. 连接初值的整体幅角分支

平圆领V=−er可用β=π+2kπ表示。对当前正侧原始lift，tip β0在(−π,0)，自然尾值为−π；负侧加π后的lift自然接+π。也可对整条核心lift统一加一个2π整数后保持同一物理框架。该整数应作为设计定义冻结，不能逐点取模或unwrap。选择不同整体分支会改变Hermite初值的额外转角，不能把不必要的整周旋转当作几何强制。

# 偶高度准确平核的高阶材料切向接口

日期：2026-11-14。对应独立新模块 `scripts/cosine_core_high_jets.py`。本补记给 R28 的直接位置重构提供真正的核心 `Tss`，不修改已经冻结的 `cosine_rectifying_core.py`，不进行新研究候选求解。所有公式针对同一个准确有理物理身份及其准确弧长定义；浮点评估不是连续区间证书。

## 1. 为什么位置二 jet 还不够

R9 的准确材料坐标满足

\[
X_\theta=a_0T,\qquad X_s=B,
\]

其中 `T,B` 为中心空间曲线在隐式角处的 Frenet 切向、陪法向。R28 的位置重构为 `X=z_c e_z+a ΠT`。若只在一个端口硬拼位置 C2，重构中的 `Xss` 含有 `Tss`，后者是核心位置的三阶混合导数 `Xssθ/a0`。已有位置二 jet 接口不会自动提供它。

新模块由空间曲线的真实 Cartesian `gamma^(0),...,gamma^(5)` 推出所需量。它还返回 `T` 与 `B` 的完整材料二 jet，避免在后续框架表示中用未验证的有限差分冒充准确端口数据。

## 2. 第五物理导数

设

\[
\gamma(\phi)=\bigl(r(\phi)\cos\phi,r(\phi)\sin\phi,z(\phi)\bigr),
\quad r=1+a\cos3\phi+b\cos6\phi,
\quad z=c+\sum_j H_j\cos(3j\phi).
\]

在同一个转动正交架 `(er(phi),eθ(phi),ez)` 中，真实第五导数的分量是

\[
\gamma^{(5)}=
(r^{(5)}-10r^{(3)}+5r')e_r
+(5r^{(4)}-10r''+r)e_\theta
+z^{(5)}e_z,
\tag{1}
\]

其中 `z^(5)=-sum (3j)^5 H_j sin(3j phi)`。式 (1) 来自对 `r exp(i phi)` 五次求导，已经包含转动架的导数，不能再将第四导数的径向、切向分量逐个普通求导作为第五物理导数。

## 3. Frenet 不变量的二阶弧长导数

以下 `v_i=gamma^(i)`，下标 `phi` 表示构造角导数。记

\[
v=|v_1|,\quad C=v_1\times v_2,\quad \Omega=|C|,
\quad D=C\cdot v_3.
\]

准确微分为

\[
C_\phi=v_1\times v_3,\qquad
C_{\phi\phi}=v_2\times v_3+v_1\times v_4,
\]
\[
D_\phi=C\cdot v_4,\qquad
D_{\phi\phi}=C_\phi\cdot v_4+C\cdot v_5,
\tag{2}
\]
\[
v_\phi={v_1\cdot v_2\over v},\quad
v_{\phi\phi}={|v_2|^2+v_1\cdot v_3-v_\phi^2\over v},
\]
\[
\Omega_\phi={C\cdot C_\phi\over\Omega},\quad
\Omega_{\phi\phi}={|C_\phi|^2+C\cdot C_{\phi\phi}-\Omega_\phi^2\over\Omega}.
\tag{3}
\]

当 `v>0,Omega>0` 时，

\[
\kappa={\Omega\over v^3},\quad
\tau={D\over\Omega^2},\quad
q={\tau\over\kappa}={Dv^3\over\Omega^3}.
\]

令 `A=v^3/Omega^3`，以及

\[
\rho=3(v_\phi/v-\Omega_\phi/\Omega),
\]
\[
\rho_\phi=3\left(v_{\phi\phi}/v-(v_\phi/v)^2
-\Omega_{\phi\phi}/\Omega+(\Omega_\phi/\Omega)^2\right).
\]

则不除以可能为零的 `D`，也不除以 `tau`，即可计算

\[
q_\phi=A(D_\phi+D\rho),\quad
q_{\phi\phi}=A\{D_{\phi\phi}+2D_\phi\rho+D(\rho^2+\rho_\phi)\}.
\tag{4}
\]

因此对实际物理弧长 `ell`，

\[
q_\ell={q_\phi\over v},\qquad
q_{\ell\ell}={q_{\phi\phi}\over v^2}-{q_\phi v_\phi\over v^3},
\tag{5}
\]
\[
\kappa_\ell={1\over v}\left({\Omega_\phi\over v^3}
-{3\Omega v_\phi\over v^4}\right),\qquad
\tau_\ell={1\over v}\left({D_\phi\over\Omega^2}
-{2D\Omega_\phi\over\Omega^3}\right).
\tag{6}
\]

偶高度核心在镜面对称轴上的 `tau=0` 因而不会造成公式奇异。真正需要排除的是零速度、零空间曲率和后面的非正 `J`。新模块对这些情形明确报错，不以一个小常数替换分母。

## 4. 隐式材料坐标的全二 jet

材料坐标由准确弧长原函数定义：

\[
\ell+s q(\ell)=a_0\theta\pmod P,
\qquad P=2\pi a_0,\qquad J=1+s q_\ell>0.
\tag{7}
\]

在任一局部分支中，(7) 的右侧对 `s` 的导数为零。即使数值程序为选择周期分支使用了随 `s` 变化的起点，该起点也只选择整数周数，不能把它作为额外的物理径向导数。

隐式求导给

\[
\ell_s=-q/J,\qquad \ell_\theta=a_0/J,
\tag{8}
\]
\[
\ell_{ss}={2q q_\ell\over J^2}-{s q^2q_{\ell\ell}\over J^3},
\]
\[
\ell_{s\theta}=-{a_0q_\ell\over J^2}
+{a_0s q q_{\ell\ell}\over J^3},\qquad
\ell_{\theta\theta}=-{a_0^2s q_{\ell\ell}\over J^3}.
\tag{9}
\]

对任一仅依赖中心曲线弧长的向量场 `F(ell)`，统一使用

\[
F_i=F_\ell\ell_i,\qquad
F_{ij}=F_{\ell\ell}\ell_i\ell_j+F_\ell\ell_{ij}.
\tag{10}
\]

Frenet 公式给

\[
T_\ell=\kappa N,\quad
T_{\ell\ell}=-\kappa^2T+\kappa_\ell N+\kappa\tau B,
\]
\[
B_\ell=-\tau N,\quad
B_{\ell\ell}=\kappa\tau T-\tau_\ell N-\tau^2B.
\tag{11}
\]

(8)–(11) 提供五个一阶、二阶材料量 `Ts,Ttheta,Tss,Tst,Ttt` 及相应 `B` 量。特别地，合并可得所需准确公式

\[
\boxed{
T_{ss}={\tau^2\over J^2}(qB-T)
+{q\tau_\ell+\tau q_\ell-s\tau q q_{\ell\ell}/J\over J^2}N.}
\tag{12}
\]

这就是新接口真正补充的三阶位置信息，不能从原二 jet 的数值名称推测出来。

## 5. 正负两侧端口的符号与作用域

在侧号 `sigma=+1` 或 `-1` 上，连接器向外坐标 `t` 对应 `s=sigma(w+t)`。端口 `t=0` 处，目标框架是

\[
T_{out}=T,\qquad V_{out}=\sigma B.
\]

所以

\[
(T_{out})_t=\sigma T_s,\quad
(T_{out})_{tt}=T_{ss},\quad
(T_{out})_{t\theta}=\sigma T_{s\theta},
\]
\[
(V_{out})_t=B_s,\quad
(V_{out})_{tt}=\sigma B_{ss},\quad
(V_{out})_{t\theta}=B_{s\theta}.
\tag{13}
\]

纯角导数保持原有侧号。当前数值模块仍拒绝 `|s|>w`：获得边界导数不表示已经证明整个外延核心或连接器存在。开放核心缓冲区可以使用 `t<0`；外侧的有限维表示须由这些真实端口数据另行构造。

本模块返回框架向量及其导数，不把逐点主值 `atan2` 当作一个全周期的 `beta` lift。将框架转换成 R28 的标量 `u,v,beta` 时，仍须使用零 framing 所保证的连续周期分支，再对相应准确角函数求导。

## 6. 稳定 API 和身份

```python
from cosine_rectifying_core import CosineRectifyingCore
from cosine_core_high_jets import material_frame_two_jets

core = CosineRectifyingCore.from_verified_report(frozen_report)
jets = material_frame_two_jets(core, s, theta)
# jets['Tss'], jets['Tst'], jets['Ttt']
# jets['Bss'], jets['Bst'], jets['Btt']
```

返回值保留完整 `frozen_physical_identity`、其 canonical SHA256、固定 Gauss 弧长精度设置、实际材料方程反解误差及既有全宽 `J` 证书是否可用。继承核心构造器的证书身份校验，并在入口重新检查身份 hash。没有重新优化、拟合高度系数或改变 `a0` 的数学定义。

浮点 `a0` 来自同一个准确模型的固定积分评估。二 jet 的公式准确，不代表有限精度数值已经包围真实值；若后续要连续证明 C2 误差，仍需给第五导数、隐式反解及相应算术误差作连续包围。

## 7. 已执行的廉价开发检查

命令：

```bash
python topics/visible-flex-new-mechanism/scripts/cosine_core_high_jets.py \
  --check-only \
  --out topics/visible-flex-new-mechanism/notes/cosine-core-high-jets-check-20261114.json
```

只使用一个圆和一个人工温和低模曲线：`a=1/20,b=1/200,H=(1/25,-1/100,1/1000),c=1/11,w=1/100`。它们不是研究扫描或选出的宏观候选。

实际小 JSON 记录：圆例误差 `1.78e-15`；真实第五 Cartesian 导数差分相对误差 `1.03e-10`；`qell_ell` 和 `tauell` 约 `2.45e-10`；完整 `T/B` 二 jet 与一阶场差分的最大相对误差 `9.51e-9`。

更关键的是直接从原核心 `Xtheta/a0` 评价固定同一个材料 `theta` 的位置二差分：径向步长由 `2e-4` 减到 `1e-4`，`Tss` 相对误差由 `3.49e-5` 降至 `8.72e-6`，符合二阶截断行为。材料方程最大浮点残差 `9.28e-14`。式 (12) 与统一链式 (10) 的差为 `3.44e-16`。

这些检查验证的是开发接口与导数实现，未验证任何真实候选的宏观幅度、整核嵌入、完整闭面、reach 或题目完成标准。

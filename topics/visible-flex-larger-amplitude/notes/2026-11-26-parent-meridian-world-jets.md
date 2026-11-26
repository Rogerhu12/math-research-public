# 真实父场的 world meridian 四 jet 与归一化公式

日期：2026-11-26。**已证明的是以下代数和条件化导数恒等式；源码只做静态 AST/compile 检查，尚无本新入口的科学返回。**

完整源为 `scripts/resume_20261126/so3_parent_meridian_jet.py`，19901 B，
SHA-256 `d3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9`。
本模块为后继完整 SO(3) 构造提供一个实际父场的固定 meridian 方向及必要导数，保持原全部共享 quintic、core、H 和准确 f/h/k。它不修改 2e point adapter，不拟合旧场，也不声称新场已经等距或闭合。

## 1. 两种角坐标和 world frame

固定一个真实 R671 或 deep canonical 父场。以 $\phi$ 为物理极角，完整材料角为

$$
\Theta_0(\phi)=\phi+\delta_0(\phi),\quad
\delta_0=\sum_{j=1}^{M}\frac{1-\nu_j^2}{\nu_j}c_j\sin(\nu_j\phi),
\quad
\rho_0=1+\sum_{j=1}^{M}(1-\nu_j^2)c_j\cos(\nu_j\phi),\quad \nu_j=2j.
$$

令 $Q_\phi$ 为绕 z 轴旋转 $\phi$ 的矩阵。完整原场在旋转基中的形式为

$$
F_0=Q_\phi\bigl(L(s,\phi)+f(s)e_r(\delta_0)
                  +(h(s)H_0+k(s))e_z\bigr).
$$

这里 $L$ 的三分量保留全部 M 个模式：

$$
L_r=r_0+\sum r_j\cos(\nu_j\phi),\qquad
L_t=\sum t_j\sin(\nu_j\phi),\qquad
L_z=z_0+\sum z_j\cos(\nu_j\phi).
$$

原 2e six-jet/point 例程返回的是**物理导数在这个旋转基中的分量**。把这些分量当成固定 world 坐标直接积分会少掉基的旋转。新模块先在旋转基中支付完整连接项，再对每个物理向量 jet 统一乘 $Q_\phi$，因此返回真正的 world Cartesian jet。

所有带 phi 下标的返回均表示对物理 $\phi$ 求导，不是对材料 $\Theta_0$ 求导。它同时返回 $\Theta_0,\rho_0,\rho_{0,\phi}$，供后继完整构造按自己的实际材料坐标链式法则使用；没有将这两个角混成同一参数。

## 2. 完整 Fs、Fss、Fsphi、Fsphiphi

对旋转基中的任意三分量 $w=(w_r,w_t,w_z)$，定义

$$
Dw=(w_{r,\phi}-w_t,\ w_{t,\phi}+w_r,\ w_{z,\phi}),
$$

$$
D^2w=(w_{r,\phi\phi}-2w_{t,\phi}-w_r,\
       w_{t,\phi\phi}+2w_{r,\phi}-w_t,\
       w_{z,\phi\phi}).
$$

直接微分 $Q_\phi w$ 给

$$
\partial_\phi(Q_\phi w)=Q_\phi Dw,\qquad
\partial_{\phi\phi}(Q_\phi w)=Q_\phi D^2w.
$$

因 $\delta_{0,\phi}=\rho_0-1$，完整连接后的参考项满足

$$
De_r(\delta_0)=\rho_0e_t(\delta_0),\qquad
D^2e_r(\delta_0)=\rho_{0,\phi}e_t(\delta_0)-\rho_0^2e_r(\delta_0).
$$

所以若 $z_s=h_sH_0+k_s,\ z_{ss}=h_{ss}H_0+k_{ss}$，则准确有

$$
\begin{aligned}
V:=F_{0,s}&=Q_\phi(L_s+f_se_r(\delta_0)+z_se_z),\\
V_s:=F_{0,ss}&=Q_\phi(L_{ss}+f_{ss}e_r(\delta_0)+z_{ss}e_z),\\
V_\phi:=F_{0,s\phi}&=Q_\phi(DL_s+f_s\rho_0e_t(\delta_0)),\\
V_{\phi\phi}:=F_{0,s\phi\phi}
 &=Q_\phi\bigl(D^2L_s+
 f_s(\rho_{0,\phi}e_t(\delta_0)-\rho_0^2e_r(\delta_0))\bigr).
\end{aligned}
$$

只需要共享 quintic 的两个径向 jet 和 $q_s$ 的两个角向导数，不需要 $F_{\phi\phi\phi}$，也不引入一个新的 $a,b,c,\kappa$ whole-profile 接口。全部 $h_sH_0+k_s$、$h_{ss}H_0+k_{ss}$ 保留；其角向导数为零是因为它们的 world z 分量与角无关，不是删除 lift 项。

每个任意点 $(cell,u)$ 用原字节绑定的 `gauss_observed_closed_gram.hermite_weights` 对该胞的完整六端 jet 求值，直接得到 $q,q_s,q_{ss}$。源码 `problem.lift_at` 同时读取同一 context 的全部九个 scalar jets；没有对旧 mean 数组或 scalar 表作额外插值。

## 3. 归一化方向的四个 jet

在 $V\ne0$ 的区域，令

$$
n=|V|,\qquad T_0=V/n.
$$

由 $V=nT_0$ 与 $T_0\cdot T_0=1$，准确得到

$$
n_s=T_0\cdot V_s,\qquad n_\phi=T_0\cdot V_\phi,
$$

$$
T_{0,s}=\frac{V_s-T_0n_s}{n},\qquad
T_{0,\phi}=\frac{V_\phi-T_0n_\phi}{n}.
$$

再对 $n^2=V\cdot V$ 微分两次：

$$
n_{\phi\phi}=
\frac{|V_\phi|^2+V\cdot V_{\phi\phi}-n_\phi^2}{n}.
$$

对 $V=nT_0$ 的二阶角导数则给

$$
T_{0,\phi\phi}=
\frac{V_{\phi\phi}-T_0n_{\phi\phi}-2T_{0,\phi}n_\phi}{n}.
$$

这就是源码全部归一化公式。由于 $Q_\phi$ 正交，各点积可以用完整物理导数的旋转基分量计算；随后每个 vector jet 旋转一次成为 world 值。不能在这个最后的旋转之后再加一次连接，否则会重复计算。

数学上这些恒等式适用于所用导数存在且 n>0 的整个区域。数值源码只报告实际查询点的 n/rho 正性和 min/max；普通浮点求值不是向外误差包围。若后继要把 $T_0$ 作为全域准确系数使用，可消费同一真实父场已存在的完整 first 中 $E=|F_s|^2>0$ 的结果；不能跨父继承该正性或由有限采样声称全域非零。

## 4. 完整来源绑定与固定父语义

构造器只接受实际完整 canonical 模型：

- R671 factory 2e，$\lambda=1$；
- 或 deep factory 4ae、完整 deep scalar e091、原 base factory 2e，仍 $\lambda=1$。

两者的真实 context.definition/create_pair/reference_at 分别核对应源码。`lift_at`、`mix_profile`、`_point_definition` 正常来自原 2e，deep 的这些方法确实是原字节委托，不能把 factory=4ae 冒成 factory=2e。dense e7aa、batch 02a5、observed 26f 及全部 scalar/integer/Hold 源逐项核实际字节；当前 input scalar、node、observation carrier 与完整模型一致。

输入 bundle 中的整个 literal canonical definition 必须等于已正常重建的 context.definition。prepared 的完整 qjets、core 与 H 必须精确对应这个已保存的 actual parent；不能把另一个试点 prepared 塞到同一 parent 身份下。函数还允许传显式 expected bundle/model SHA，对实际选定父作额外直接归属。

固定父数据复制为 readonly，后续独立 $\omega$ 变量或自由 core 坐标由新的完整 SO(3) 求解器负责。这里冻结的只是一个真实初始化系数场，没有把后继新的 core 自由量设为父 core。新的积分、闭合/对称条件和全部几何仍须由那个真实新构造支付。

## 5. 精确 API

模块导入本身不做科学计算；构造及 evaluate 只允许 `Rogerhu12/math-research-public` 的公开 Actions。

```python
parent = meridian.ParentMeridianJet(
    actual_problem, actual_prepared_parent,
    expected_model_identity_sha256=actual_parent_model_sha,
    expected_bundle_sha256=actual_parent_bundle_sha)
jets = parent.evaluate(cells, local, phi)
```

`cells` 与 `local` 是一维配对的径向点数组；`phi` 是独立一维角列。四个 T0 jet 和四个原物理 V jet 的形状均为 `(len(cells),len(phi),3)`：

- `T0`、`T0_s`、`T0_phi`、`T0_phiphi`；
- `Fs`、`Fss`、`Fsphi`、`Fsphiphi`；
- `norm`、`norm_s`、`norm_phi`、`norm_phiphi`；
- 一维 `phi`、`theta_parent`、`rho_parent`、`rho_phi_parent`；
- 小 `metadata`。

需要多次径向积分或多批角值时复用同一对象，避免反复 hash 所有来源和复制父数组。便捷函数 `parent_meridian_jets(...)` 具有同样参数并一次构造/读取，不宜在每个积分叶片重复调用。所有返回数组 readonly。

`metadata` 明示完整父模型/bundle/source、实际行角数、全部模式数、查询点的 n/rho 正性，以及 continuous/metric/geometry 相关 false 旗标；大向量仅供实际 runner 内的求解器消费，不作为仓库数据输出。

## 6. 已做与尚未声称

已做：上述完整代数、所有原 q/H/k 来源的静态接口核、AST/compile 与重复字面 dict key/keyword 检查。没有在本地读科学候选、运行 F/J 或 normalization fixture。

本源没有运行完整新 SO(3) 方向，没有证明新积分场等距、core/帽反射接合、embedding、幅度、reach、含反射刚体商非平凡性或固定目标精化。即便 $T_0$ 在数学上单位，新场若另加闭合修正项，仍要按新场真实公式重新计算全部 Gram 和几何，不能只用单位 T0 代替全场误差。

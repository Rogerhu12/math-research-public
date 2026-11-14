# R133 补篇：完整 moving 帽接线、未保留高行与 regular 子空间入口

2026-11-14。**完整同切口矩阵及其高输出预算已经实际完成；整个帽的连续试解误差仍是待消费输入。** 本篇把已付的128个物理帽列接成真正的 moving 96个奇行及独立 mean 行。它给出一个可用的193态 regular 子空间提案，保留全部未保留 moving 高输出。没有把有限矩阵的秩或首批帽残差称作已经证明的连续主体逆。

实际 source 为 [fourfold_codazzi_complete_moving_cap_cut_boundary_v2.py](../scripts/fourfold_codazzi_complete_moving_cap_cut_boundary_v2.py)。背景是同 ac1 完整候选、准确连续修复定义 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，切口为准确有理数 $L=9/10$。

## 1. 完整函数空间中的接线

沿用实际反射类：$h_1$ 为奇函数，$h_2$ 为偶函数并保留 mean。圈上 $L^2$ 采用归一化测度。令

$$
\Theta(\varphi)=\varphi+\psi(\varphi),\qquad
\Theta_\varphi=v/m>0,\qquad m=\langle v\rangle_\varphi<0.
\tag{I.1}
$$

实际微分坐标变换的物理 $B,C$ 行记为 $H_B,H_C$。后者的非零物理模仅依赖 $h_2$，独立物理 mean 为

$$
H_{C0}h_2=-\langle h_2\rangle/m^2.
\tag{I.2}
$$

这些是完整函数算子，不是其有限矩阵。令 $\mathcal K$ 为已经证明的物理帽 Green 延拓：给定 $C_\perp(L)$，外端保留真正 regular、mean 和已声明的独立数据。记齐次外数据下的两个内端输出为 $\mathcal K_B,\mathcal K_0$。主体与帽的准确接线是

$$
H_B(h_1,h_2)-\mathcal K_BH_Ch_2=0,
\qquad
H_{C0}h_2-\mathcal K_0H_Ch_2=0.
\tag{I.3}
$$

普通源、散度源、独立外 $f_B$、全部 Robin 与 mean 数据产生原 Green 的仿射右端；它们没有被齐次矩阵列删除。

在第一行上使用准确可逆的同一物理角变换

$$
(\mathcal S f)(\varphi)=v(\varphi)f(\Theta(\varphi)).
\tag{I.4}
$$

由 $d\theta=(v/m)d\varphi$，直接得到

$$
\|\mathcal S\|_{L^2_\theta\to L^2_\varphi}
 \le \sqrt{|m|\sup|v|},\qquad
\|\mathcal S^{-1}\|
 \le (|m|\inf|v|)^{-1/2}.
\tag{I.5}
$$

实际同切口证书给出 $\|\mathcal S\|<3.228515$、$\|\mathcal S^{-1}\|<0.313899$。因此全函数层面上，(I.3)与变换后的第一行等价。

当 $h_2=0$ 时，坐标变分原函数和 mean 都为零，物理第一行准确为
$H_B(h_1,0)=(h_1/v)\circ\Theta^{-1}$。所以

$$
\boxed{\mathcal S H_B(h_1,0)=h_1.}
\tag{I.6}
$$

这给变换后奇分量的准确恒等块。在构造这个块时，没有使用两个有限截断矩阵相乘代替完整等式。

## 2. 真正的97个有限行与完整高行

定义正交头空间

$$
\mathcal O_{96}=\operatorname{span}\{\sqrt2\sin4j\varphi:1\le j\le96\},
\quad
\mathcal E_{96}=\operatorname{span}\{1,\sqrt2\cos4j\varphi:1\le j\le96\}.
\tag{I.7}
$$

输入维数为193。把(I.4)后的第一行投影到 $\mathcal O_{96}$，并保留(I.2)的独立 mean 行，得到97个有限行

$$
\mathcal B_{\rm low}=
\begin{pmatrix}I_{96}&J\\0&M\end{pmatrix},
\qquad
J=\Pi_{96}\mathcal S(H_{B,e}-\mathcal K_BH_C),
\quad M=H_{C0}-\mathcal K_0H_C.
\tag{I.8}
$$

这里 $H_{B,e}=H_B(0,\cdot)$。其余 moving 奇行仍为

$$
\mathcal B_{\rm high}h_2=
(1-\Pi_{96})\mathcal S(H_{B,e}-\mathcal K_BH_C)h_2.
\tag{I.9}
$$

它们是完整 high–head 接口的一部分，不能因为有限 regular 子空间维数为96而删除。输入中的高 even/odd 也在最终无限块系统中保留；本篇只计算(I.8)和(I.9)对完整193头的列。

这一定义与现有 moving $N=97$ 高块采用同一角坐标、同一 $L^2$ Gram。没有将128个物理奇行与96个 moving 奇行直接混同，也没有将129个物理条件强加为一个193态有限头的97行边界。

## 3. 真实有限矩阵及径向端值

令 $T$ 为已经保存全部共享节点值、两组单侧导数和所有257状态、97正交输入列的准确 dyadic Hermite 试解。其输入是实际 $H_C$ 的有向128物理行矩阵提案。

本消费者在准确 $L=9/10$ 处以有理 Hermite 基函数计算 $T_B(L)$、$T_0(L)$。原第一节点是 $L$ 的 binary64 邻点；报告明确保留这两个有理半径及全部四个 Hermite 权。计算的是已经定义的试解多项式，不把背景 PPoly 或目标系数外推到未声明的 germ。

已付 $K_{96\times128}$ 是 $\Pi_{96}\mathcal S\Pi_{128}$ 的准确有向矩阵。原 $H_B$ 的列使用 raw sine/mean/cosine 幅度；对其 even 非零输入列乘准确 $\sqrt2$，并对输出 sine 幅度除准确 $\sqrt2$，从而获得(I.7)中的真正正交矩阵。

若 $D=\operatorname{diag}(1,\sqrt2,\ldots,\sqrt2)$，则有限闭区间矩阵为

$$
J_T=K\,\frac{H_{B,e}^{(128)}D-T_B(L)}{\sqrt2},
\quad
M_T=\left(-m^{-2},0,\ldots,0\right)-T_0(L).
\tag{I.10}
$$

所有有向条目先在 Arb 中相乘，再将结果的中点转为准确 binary64 提案。完整条目区间对该提案的 Frobenius 误差界算子范数；真实物理未保留尾另乘(I.5)。每个矩阵 Schur 行/列最大值都先取有向上端点再比较。

当前实际结果是

$$
\|J_T-\widehat J_T\|+\|\mathcal S\|\,\tau_B
 <2.759501\,10^{-11}.
\tag{I.11}
$$

这里 $\tau_B$ 是已付完整物理 $B$ 高尾，包含 even mean 输入，不是将未保留条目置零。

## 4. 完整 moving 高输出的实际计算

仅有(I.11)不足以支付(I.9)。本消费者另直接计算其完整 Fourier 输出。
记 $A=i\psi$ 的实际32模 Laurent 多项式，$E_l=e^{-4lA}$，$V$ 为实际 $v$ 的完整32模 Laurent 多项式。对于 raw 物理输入 $\sin4l\theta$，准确有

$$
(\mathcal S\sin4l\theta)_j
 =(VE_l)_{l-j}-(VE_l)_{l+j}.
\tag{I.12}
$$

这与已付有限 $K_{j,l}=m(j/l)[(E_l)_{l-j}+(E_l)_{l+j}]$ 一致。本段使用(I.12)，以便无需对一个 $A^0$ 余项取角导。

对每个 $1\le l\le128$，将 $e^{-4lA}$ 分成正、负单侧指数；各有限多项式的完整 $A^0$ 尾为 $\epsilon_l$。实际 source 逐项选择已声明的复宽和阶数，保证 $\epsilon_l<2^{-180}$。将有限指数乘完整 $V$ 后，所有非零有限输出模都被保留，直到各自的真实最后支持。除此之外的完整函数误差不超过 $\|v\|_{A^0}\epsilon_l$。

因为物理输入正交基为 $\sqrt2\sin4l\theta$，整个未保留指数误差的算子范数被

$$
\varepsilon_{\exp}
 \le\left(2\sum_{l=1}^{128}\|v\|_{A^0}^2\epsilon_l^2\right)^{1/2}
\tag{I.13}
$$

控制。对有限差矩阵
$F=(H_{B,e}^{(128)}D-T_B)/\sqrt2$，全部 $j\ge97$ 的输出矩阵先准确相乘，再使用完整 Frobenius/Schur 范数较小的有向上界。最后加上 $\varepsilon_{\exp}\|F\|$ 和完整物理 $H_B$ 尾。

实际已经得到

$$
\|(1-\Pi_{96})\mathcal S(H_{B,e}-T_B)\|
 <3.893487\,10^{-7}.
\tag{I.14}
$$

这是整个 moving 高输出的界，包括全部无限输出尾；不是仅计算第97到128模的范数。奇输入 $h_1$ 对该高输出准确为零，依据是(I.6)，不是数值消减。

## 5. 完整帽误差与真实 moving 算子的费用

令 $\epsilon_{\rm cap}$ 是整个1977条真实闭片、全部普通/散度源、外端 true DN 和 mean 都完成后的物理帽矩阵误差

$$
\|\mathcal K H_C-T\|\le\epsilon_{\rm cap}.
\tag{I.15}
$$

它尚不能由当前任一已成前缀替代。对真正物理帽，低 odd 行、高 odd 行分别在(I.11)、(I.14)上增加 $\|\mathcal S\|\epsilon_{\rm cap}$，独立 mean 行增加 $\epsilon_{\rm cap}$。这些来自完整同一个 Green 比较，不要求误差保持有限角支持。

实际 moving Jacobi 帽还需已证残差敏感 $\Psi''$ 接线。已有完整 cap bridge 给
$\chi<0.003840161210$，且仅消费了准确 $\eta=\eta_0$ 的全径向残差；其背景和物理帽系数的 whole-$\eta$ 范围不能将这笔残差费用免费扩为 whole-$\eta$。

在已付同一函数空间中，粗而合法的额外差为

$$
\epsilon_{\rm bridge}
 \le\frac{\chi}{1-\chi}\,G_L\|H_C\|.
\tag{I.16}
$$

本次严格矩阵 Schur 范数给 $\|H_C\|<0.203079490$，从而
$\epsilon_{\rm bridge}<0.010424712$。对真实 $\eta_0$ moving 帽，将上段的 $\epsilon_{\rm cap}$ 换成
$\epsilon_{\rm cap}+\epsilon_{\rm bridge}$ 即合法。后续可直接消费同一试解的完整局部 Hessian 源；准确较紧恒等式是

$$
\epsilon_{\rm moving}
 \le\frac{\epsilon_{\rm cap}+\|G\Psi''[R,T]\|}{1-\chi}.
\tag{I.17}
$$

这里普通源按真实径向 $L^2$ 支付，散度源在每物理 Fourier 模先取径向 supremum，不能乘一个不存在的径向长度因子。原独立 $f_B$、全部外源和 mean 仍由已证 Green 列保留。

当前 mean 第0列在扣除(I.16)后尚有

$$
|M_{T,0}|-\epsilon_{\rm bridge}>0.0867789975.
\tag{I.18}
$$

所以只要后续实际 $\epsilon_{\rm cap}$ 小于这个严格数，完整有限切口的 mean 系数仍不为零。这是明示待付输入的判据，不是已经宣布原帽全域误差闭合。

## 6. 全 regular 子空间提案及后续连续门

令 $\widehat J,\widehat M$ 为(I.10)的完整 binary64 中点。用全部96个非零 even 幅度为自由列，写

$$
E=\begin{pmatrix}-\widehat M_{\perp}/\widehat M_0\\ I_{96}\end{pmatrix},
\qquad
X=\begin{pmatrix}-\widehat J E\\E\end{pmatrix}.
\tag{I.19}
$$

这保留真正 mean 的响应，不把它设为零。对整个 $193\times96$ 矩阵作正对角 QR，产生完整物理正交 Gram 下的入口 frame。实际完整模型核和 Gram 诊断分别通过原 $10^{-10}$、$10^{-11}$ 门。

这个 frame 仅是连续 regular 子空间的提案。实际继续必须逐真实径向闭盒支付
[连续头 Green 定理](R133-supplement-continuous-head-Green-from-a-regular-subspace.md)
的 Gram、投影残差、两个有符号对角率、两端数据以及全部 high 反馈。提案的 QR 条件数或(I.18)不代替这些连续门。

本次 v2 实际正常返回0，16.111761秒，最大 RSS130240 KiB；核心有向计算11.000620秒。v1 的矩阵 Schur 最大值在区间加法后直接比较，本次将它改为先逐项提取有向上端点；v1 小过程和输入身份保留，数学数值引用 v2。原始全部帽矩阵数组、其 SHA 和重建入口保留，未新增另一套近似 seed。

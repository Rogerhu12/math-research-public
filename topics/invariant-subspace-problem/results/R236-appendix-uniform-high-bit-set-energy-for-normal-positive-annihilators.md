# R236 附录：正常正消去源在任意高位集合上的统一能量下界

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文把[任意秩正常正源的多项式柱尾](R236-appendix-polynomial-cylinder-tail-for-all-normal-positive-annihilators.md)加强为任意有限高位集合的统一下界，常数不依赖集合跨度、源的秩或放大维数。再得到完整系数 $\ell^2$ 尾、原商压缩上的算子序和单个位删除的实际闭值域。所有结论仍是必要条件，未证明正常源不存在或原 ISP 完成。

## 1. 对象与主定理

在原 Haar/Walsh Hilbert 空间上，沿用原实际模型
$$X=\sum_{i\ge0}a_iX_i,\qquad X_i\in\{\mathsf N_i,\mathsf Y_i\},$$
允许逐位混合，系数可以有复相位。假设
$$|a_i|\le A(i+1)^{-2}\quad(i\ge0),\qquad
|a_i|\ge a_-(i+1)^{-2}\quad(i\ge i_0),$$
其中 $A,a_->0$。使用前稿已证的原算子估计
$$\|X_i\|\le3,\quad \|X_i-E_i\|\le4\eta_i,\quad
\|X_i-X_i^{[p]}\|\le9\eta_{p-1}\quad(i<p),$$
$$0<\eta_i\le e^{-770\,16^i}.\tag{1.1}$$
$X_i^{[p]}$ 保留前 $p$ 位的实际进位，$E_i$ 是纯 Walsh 删除；二者不混同。

设 $\rho\ge0$ 是任意非零迹类算子，$\tau=\operatorname{Tr}\rho$，并满足同一个原代数上的右消去方程
$$\boxed{\operatorname{Tr}(\rho XG)=0\qquad(G\in\mathcal A).}\tag{1.2}$$
这里 $\mathcal A$ 是原实际算子的闭幺代数；若已知整个交换子代数上的方程，则当然满足 (1.2)。正文仅用 (1.2)。

记 $Q_i^-$ 为第 $i$ 位的 Walsh minus 投影。对非空有限集合 $I$，置
$$p=\min I,\qquad q=1+\max I,\qquad
R_I=\prod_{i\in I}(I-Q_i^-).$$
$R_I$ 只要求选中的位为 plus，其余所有位任意，通常是无限秩投影。

**定理。** 存在只依赖 $A/a_-$、原实际模型和 $i_0$ 的 $p_0$，使每个 $\min I\ge p_0$ 均有
$$\boxed{\frac{\operatorname{Tr}\rho(I-R_I)}{\tau}
\ge\frac{\sum_{i\in I}|a_i|^2}{9\cdot2^{26}A^2}.}\tag{1.3}$$
$p_0$ 与 $\max I$、$|I|$、$\rho$、其秩及放大维数无关。

## 2. 原实际代数中的测试元

把 $a_i$ 的相位分成四个宽度 $\pi/2$ 的扇区，选择平方能量最大的一组 $F\subset I$，记
$$c_i=|a_i|,\quad B^2=\sum_{i\in F}c_i^2,\quad s_F=\sum_{i\in F}c_i.$$
有某个角 $\vartheta$ 使
$$B^2\ge\frac14\sum_{i\in I}|a_i|^2,\qquad
\operatorname{Re}(e^{-i\vartheta}a_i)\ge\frac23c_i\quad(i\in F).\tag{2.1}$$
因为 $I$ 含最小位 $p$，
$$B\ge\frac{a_-}{2(p+1)^2}\ge\frac{a_-}{8p^2},\qquad
s_F\le A/p,\qquad s_F/B\le8(A/a_-)p.\tag{2.2}$$

令原 accretive 算子
$$V_i=(I-\mathsf N_i)(I+\mathsf N_i)^{-1}
=I-2\mathsf Y_i,\qquad D_i=I-2E_i.$$
定义
$$L=\sum_{i\in F}c_iV_i,\quad L_0=\sum_{i\in F}c_iD_i,\quad t=12B,$$
$$H=t(t+L)^{-1},\qquad H_0=t(t+L_0)^{-1}.$$
有 $\|H\|,\|H_0\|\le1$。有限个原交换拟幂零元的逆展开说明 $H\in\mathcal A$；这是前稿已完整证明的实际代数步骤。记全 plus 真空态为 $\omega$，置
$$G=H-\omega(H)I,\qquad G_0=H_0-\omega(H_0)I.$$
于是 $G\in\mathcal A$、$\|G\|,\|G_0\|\le2$，且 $\omega(G)=\omega(G_0)=0$。由实际 resolvent 身份及 $\|V_i-D_i\|\le18\eta_i$，
$$\|G-G_0\|\le3(s_F/B)\eta_p
\le24(A/a_-)p\eta_p.\tag{2.3}$$

前稿的真空二步展开适用于任意有限 $F$，不要求连续区间。为明确尺度，令 $w=\sum_{i\in F}c_i\chi_i$，则
$$L_0\Omega=w,\qquad
L_0^2\Omega=-B^2\Omega+2\sum_{i\in F}c_i^2\chi_i
+2\sum_{i<j,\ i,j\in F}c_ic_j\chi_{\{i,j\}},$$
$$\|L_0^2\Omega\|^2=3B^4+2\sum_i c_i^4\le5B^4.$$
两步 resolvent 恒等式给
$H_0\Omega=\Omega-w/t+r$，$\|r\|\le1/48$。若 $g_i$ 为其单 Walsh 系数，(2.1) 给
$$\operatorname{Re}\left(e^{-i\vartheta}\sum_{i\in F}a_ig_i\right)
\le-5B/144\le-B/32.$$
所以纯局部压缩的标量
$$\kappa_0=\omega\left(\sum_{i\in F}a_iE_iG_0\right)
=\frac12\sum_{i\in F}a_ig_i$$
满足
$$\boxed{|\kappa_0|\ge B/64.}\tag{2.4}$$
这里只利用任意有限集合上的正交 Walsh 展开；没有按集合大小支付额外费用。

## 3. 跨度无关的实际背景分解

为了压缩到 $R_I$，定义
$$X_{\rm mix}=
\sum_{i<p}a_iX_i^{[p]}
+\sum_{p\le i<q}a_iE_i
+\sum_{i\ge q}a_iX_i.\tag{3.1}$$
中间整个区间均换成纯删除，包括不属于 $I$ 的位。低位保留真实截头，高位保留原 $X_i$。因此 (3.1) 的 $I$ 外背景严格作用在选中集合之外；其与 $G_0$ 的 $R_I$ 压缩因 $\omega(G_0)=0$ 消失。$I\setminus F$ 的纯删除项也同样消失。故有精确算子身份
$$\boxed{R_I X_{\rm mix}G_0R_I=\kappa_0R_I.}\tag{3.2}$$
这不是取一个标量边缘态后猜测整个背景消失。

由 (1.1) 和 $\sum_i(i+1)^{-2}<2$，
$$\|X-X_{\rm mix}\|
\le18A\eta_{p-1}+\frac{4A}{p}\eta_p,\qquad \|X\|\le6A.$$
从
$$XG-X_{\rm mix}G_0=(X-X_{\rm mix})G_0+X(G-G_0)$$
得到
$$\boxed{\|XG-X_{\rm mix}G_0\|\le e_p:=
36A\eta_{p-1}+
\left(\frac{8A}{p}+\frac{144A^2p}{a_-}\right)\eta_p.}\tag{3.3}$$
所有上界只依赖最小位 $p$，不依赖 $q$。

选一个统一 $p_0$ 使
$$e_p\le\frac{a_-}{2048p^2}\le B/256\qquad(p\ge p_0).\tag{3.4}$$
超指数衰减保证这样的 $p_0$ 存在。这个选择在源 $\rho$ 给出之前即可完成。

## 4. 正源压缩与精确常数

令
$$\rho_I=R_I\rho R_I,\qquad
r_I=\operatorname{Tr}\rho(I-R_I),\qquad
\tau_I=\tau-r_I.$$
正迹类的 gentle compression 估计为
$$\|\rho-\rho_I\|_1\le2\sqrt{\tau r_I}.\tag{4.1}$$
由 (3.2)–(3.4)，
$$|\operatorname{Tr}(\rho_I XG)|
\ge(|\kappa_0|-e_p)\tau_I\ge(B/256)\tau_I.$$
另一方面，由同一个原方程 (1.2)、
$\|XG\|\le12A$ 和 (4.1)，
$$|\operatorname{Tr}(\rho_I XG)|
\le24A\sqrt{\tau r_I}.$$
若 $r_I\le\tau/2$，则
$$\frac{r_I}{\tau}\ge\frac{B^2}{(12288A)^2}
\ge\frac{\sum_{i\in I}|a_i|^2}{9\cdot2^{26}A^2}.$$
若 $r_I>\tau/2$，(1.3) 由
$\sum_i|a_i|^2<2A^2$ 自动成立。主定理得证。

整个论证只用原算子范数、正迹范数、有限局部代数和同一个 $\rho$。因此原空间张量任意辅助 Hilbert 空间、所有算子张量恒等后，证明和常数完全相同。

## 5. 完整系数尾与原压缩的算子序

令 $\Pi_p$ 为前 $p$ 位任意、所有 $i\ge p$ 位均为 plus 的柱投影。取 $I=[p,q)$，随 $q\to\infty$ 有 $R_I\downarrow\Pi_p$。这里只对正投影和正迹作单调极限，不要求相应测试元 $G$ 存在极限。由 (1.3)，
$$\boxed{\frac{\operatorname{Tr}\rho(I-\Pi_p)}\tau
\ge\frac{\sum_{i\ge p}|a_i|^2}{9\cdot2^{26}A^2}.}\tag{5.1}$$
这保留全部实际系数，而非只使用某个 dyadic 块的统一下界。特别
$$\operatorname{Tr}(\rho Q_i^-)
\ge\frac{\tau|a_i|^2}{9\cdot2^{26}A^2}\qquad(i\ge p_0).\tag{5.2}$$

再设 $N\subset M$ 是原不变旗，$E=M\ominus N$，且原商表示满足 $\pi(X)=0$。每个支撑在 $E$ 上的正迹类源均满足 (1.2)，所以对所有 $f\in E$ 应用 (1.3)，得原 Hilbert 度量中的算子序
$$\boxed{P_E(I-R_I)|_E
\succeq\frac{\sum_{i\in I}|a_i|^2}{9\cdot2^{26}A^2}I_E.}\tag{5.3}$$
这是同一个物理正压缩，没有改变商范数。

若 $b_i$ 是标准 Walsh 删除，$b_i^*b_i=Q_i^-$，则
$$\boxed{\|b_if\|\ge\frac{|a_i|}{3\cdot2^{13}A}\|f\|
\quad(f\in E,\ i\ge p_0).}\tag{5.4}$$
因此 $b_i|_E$ 单射、值域闭，其在 $b_iE$ 上的逆范数至多
$3\cdot2^{13}A/|a_i|=O(i^2)$。实际正压缩 $P_EQ_i^-|_E$ 的逆范数为 $O(i^4)$。

(5.4) 没有声称 $b_iE$ 不变，也没有给出原 $M/N$ 删除商的逆。具体地，对 $j>i$ 写原块
$$\mathsf N_jf=B_jf+C_jf,\qquad
B_jf\in N,\quad C_jf=\pi(\mathsf N_j)f\in E.$$
原 $b_i$ 与 $\mathsf N_j$ 交换，故
$$b_iC_jf=\mathsf N_jb_if-b_iB_jf.\tag{5.5}$$
(5.4) 尚不控制 $b_if$ 到 $\overline{b_iN}$ 的距离，(5.5) 中的原源 $b_iB_jf$ 仍需支付。

## 6. 下界的准确边界

令
$$c_*=(9\cdot2^{26}A^2)^{-1},\quad
\nu_i=c_*|a_i|^2,\quad \nu=\sum_i\nu_i<1,$$
并取真正单位向量
$$f=\sqrt{1-\nu}\,\Omega+\sum_i\sqrt{\nu_i}\,\chi_i.$$
对 $\rho_f=|f\rangle\langle f|$ 和每个有限 $I$，
$$\operatorname{Tr}\rho_f(I-R_I)=\sum_{i\in I}\nu_i.$$
所以仅这些集合能量下界本身彼此相容，甚至可由一个 Walsh 次数至多一的秩一态同时饱和。这个向量并未被声称满足原消去方程；前面关于有限 Walsh 次数的排除结论适用时会排除它作为真正消去源。这里只说明不能从 (1.3)–(5.3) 单独推出源为零。

在 $|a_i|\asymp(i+1)^{-2}$ 时，它也有临界位置三阶矩发散。这与前稿 $\operatorname{Tr}(\rho M^3)=\infty$ 的必要条件相容，并非矛盾。

[R213 的 Walsh 块删除](R213-walsh-block-deletion-and-coefficient-tail-kernel-obstruction.md)已在特定危险核向量上出现系数 $\ell^2$ 尾和临界矩机制。本稿的新范围是同一原右消去方程下任意正迹类源、任意有限高位集合及原压缩上的统一算子序，未把既有尾指数宣称为首次发现。

后续真正未付的对象仍是 (5.5) 的非对角源与双零商的共同正性；本文不从对角必要能量直接宣布正常源排除。

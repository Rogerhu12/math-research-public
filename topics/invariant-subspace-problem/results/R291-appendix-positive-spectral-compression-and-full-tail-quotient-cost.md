# R291 附录：最大尾谱压缩与完整尾理想距离的非纯质量界

2026-11-14，normal-annihilator / 789f；正常头相干性消去 carry 损失的主思路由根代理提出，本稿补全真实来源、正部分迹改进及完整尾理想优化。**状态：以下结论已证明；一般正常见证与普通 ISP 仍开。**

本稿加强[归一化矩阵附录的一位谱界](R291-appendix-normalized-tail-moments-and-explicit-spectral-mass.md)。(5.5) 中的 $\eta_j^6\eta_{j+1}^2$ 可以在同一正常链上去掉：最大谱压缩的正头结构给一个大小固定的常数项锚。真实商或其完整尾理想距离仍须保留。

## 1. 对象及结论：控制谱非纯质量，非仅真空泄漏

在一个真实一位切分中写

$$
H=\mathbb C^2\otimes H_{\rm next},\qquad
N=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
t=\eta N_{\rm next},\qquad\|N\|=1,\quad0<\eta\le1/64.
\tag{1.1}
$$

把当前首阶一符号按真实偶奇块规范化为

$$
S=C+ND=D(N+Z),\qquad
D\in\mathcal B_{\rm next}^{\times},\qquad Z=D^{-1}C.
\tag{1.2}
$$

取任意迹为一的正正常密度 $\rho$，假设它满足原右湮灭条件，因而

$$
\operatorname{Tr}[\rho(N+Z)G]=0
\quad\text{对所有当前实际代数中的 }G.
\tag{1.3}
$$

记

$$
\nu=\operatorname{Tr}_{\mathbb C^2}\rho,
\qquad \epsilon=1-\lambda_{\max}(\nu),
$$

$$
r=\operatorname{Tr}\bigl[\rho(|\Omega_-\rangle\langle\Omega_-|\otimes I)\bigr],
\qquad \Omega_-=(e_0-e_1)/\sqrt2.
\tag{1.4}
$$

**定理。** 若 $r\le1/8$，则

$$
\boxed{
1-\lambda_{\max}(\nu)
\ge\frac1{128^2(1+\|Z\|)^2}.
}
\tag{1.5}
$$

不要求 $\rho$ 有限秩。若 $\mathcal J$ 是同一原理想的完整下一尾交，且每个 $H\in\mathcal J$ 的恒等提升及其当前右倍数都被同一 $\rho$ 湮灭，令

$$
m=\operatorname{dist}(Z,\mathcal J).
$$

则同样有更强的

$$
\boxed{
1-\lambda_{\max}(\nu)
\ge\frac1{128^2(1+m)^2}.
}
\tag{1.6}
$$

这里的 $\mathcal J$ 必须来自同一个原实际理想；不能用仅满足 $\operatorname{Tr}(\nu H)=0$ 的任意尾算子代替。

## 2. 最大谱压缩给出的正头矩阵与真实相干性

正迹类 $\nu$ 有最大特征值 $\tau=1-\epsilon>0$，取相应单位特征向量 $v$。令 $P_v=|v\rangle\langle v|$，并置

$$
\sigma=(I\otimes P_v)\rho(I\otimes P_v)
=H\otimes P_v,
\qquad
H=\begin{pmatrix}a&b\\\overline b&d\end{pmatrix}\ge0,
\qquad \operatorname{Tr}H=\tau.
\tag{2.1}
$$

正性保证

$$
|b|\le\tau/2.
\tag{2.2}
$$

设 $\mu=\operatorname{Tr}_{H_{\rm next}}\rho$ 是本位头边缘。对尾空间分解为 $\mathbb Cv\oplus v^\perp$ 作部分迹时，两个交叉块的迹为零，所以

$$
\mu-H
=\operatorname{Tr}_{H_{\rm next}}
\bigl[(I\otimes(I-P_v))\rho(I\otimes(I-P_v))\bigr]\ge0,
\qquad \operatorname{Tr}(\mu-H)=\epsilon.
\tag{2.3}
$$

因而 $|(\mu-H)_{01}|\le\epsilon/2$。又由 (1.4)，

$$
\operatorname{Re}\mu_{01}=\frac12-r.
$$

于是得到不含平方根误差的准确头相干下界

$$
\boxed{\operatorname{Re}b\ge\frac\tau2-r.}
\tag{2.4}
$$

若 $\epsilon<1/2$ 且 $r\le1/8$，则 $\tau>1/2$，从 (2.4) 得

$$
\boxed{|b|\ge\tau/4.}
\tag{2.5}
$$

这里没有独立重选某个尾边缘；$H$、$v$、$\nu$ 和 $r$ 都来自同一个 $\rho$。

正压缩的标准 Hilbert–Schmidt 因式估计还给

$$
\boxed{\|\rho-\sigma\|_1\le2\sqrt\epsilon.}
\tag{2.6}
$$

例如写 $P=I\otimes P_v$，则
$\rho-P\rho P=(I-P)\rho+P\rho(I-P)$；两项迹范数分别不超过 $\sqrt\epsilon$ 与 $\sqrt{\epsilon(1-\epsilon)}$。

## 3. 一个真实二次身份与固定常数项锚

在同一实际尾代数中定义

$$
R_b=bI+\overline b\,t,
\qquad P_b=\tau N-I\otimes R_b,
$$

$$
C_b=\tau Z-R_b,
\qquad p_b=R_b^2-\tau^2t.
\tag{3.1}
$$

它们都是真实有界算子。$P_b$ 是当前 $N$ 的普通二次多项式，因为 $I\otimes t=N^2$。全部系数与 $N$ 交换，故有准确算子身份

$$
\boxed{
I\otimes p_b
=P_b(I\otimes C_b)-\tau(N+Z)P_b.
}
\tag{3.2}
$$

另一方面，原物理块直接给

$$
\operatorname{Tr}_{\mathbb C^2}(HN)=bI+\overline b\,t=R_b.
$$

所以对任意尾 $F\in B(H_{\rm next})$，

$$
\operatorname{Tr}\bigl[\sigma P_b(I\otimes F)\bigr]=0.
\tag{3.3}
$$

这里只是对真实比较密度 $\sigma=H\otimes P_v$ 的准确张量身份；没有声称原 $\rho$ 满足 raw 尾零式。

用 (1.3) 中的真正右源 $G=P_b$，再以 (3.3) 取 $F=C_b$，(3.2) 便给

$$
\boxed{
\operatorname{Tr}(\nu p_b)
=\operatorname{Tr}\bigl[(\rho-\sigma)P_b(I\otimes C_b)\bigr].
}
\tag{3.4}
$$

相对于未规范化的 $S$，此处右源为 $D^{-1}P_b$，其范数至多 $2\tau\|D^{-1}\|$。实际单位逆没有从原理想归属中消失；下面估计的是输出范数。

展开

$$
p_b=b^2I+(2|b|^2-\tau^2)t+\overline b^{\,2}t^2.
\tag{3.5}
$$

在 $\epsilon<1/2$ 的分支，(2.2)、(2.5) 以及 $\|t\|\le\eta$、$\|t^2\|\le\eta^2$ 给

$$
\begin{aligned}
|\operatorname{Tr}(\nu p_b)|
&\ge |b|^2-\tau^2\eta-|b|^2\eta^2\\
&\ge\tau^2\left(\frac1{16}-\eta-\frac{\eta^2}{4}\right)
\ge\frac{\tau^2}{32}.
\end{aligned}
\tag{3.6}
$$

最后一步由 $\eta\le1/64$ 保证。固定非零锚来自正头矩阵的相干常数项 $b^2$；没有用极小的 $t$ 项代替它。

所有实际范数满足

$$
\|P_b\|\le\tau+|b|(1+\eta)\le2\tau,
$$

$$
\|C_b\|\le\tau\|Z\|+|b|(1+\eta)
\le\tau(1+\|Z\|).
\tag{3.7}
$$

于是 (3.4)、(3.6)、(3.7) 给

$$
\|\rho-\sigma\|_1\ge\frac1{64(1+\|Z\|)}.
$$

再用 (2.6) 得到 (1.5)。若 $\epsilon\ge1/2$，(1.5) 的右端至多 $128^{-2}$，该结论自动成立；所以两种分支均已覆盖。

## 4. 同一完整尾理想中的优化与全链后果

对任意 $H_0\in\mathcal J$，将第 3 节中 $Z$ 换成 $Z-H_0$，而 $R_b,P_b,p_b$ 全部保持。
同一原理想零式保证

$$
\operatorname{Tr}\bigl[\rho(N+Z-H_0)P_b\bigr]=0.
$$

其来源合法性要求 $I\otimes H_0$ 来自原完整下一尾交、且 $P_b$ 是原当前右因子；这正是定义 $\mathcal J$ 时保留的条件。若 $H_0$ 只在原理想的范数闭包中，正常迹配对的范数连续性给同样的准确零式。

于是对每个 $H_0$ 都有

$$
\epsilon\ge\frac1{128^2(1+\|Z-H_0\|)^2}.
$$

取逼近距离的序列，不假定最小值达到，即得 (1.6)。这一步没有给出 $H_0$ 的有限源表示或其源范数；在带残量的近似构造中仍必须重新支付那些费用。

对原同一正常链，记

$$
\epsilon_{j+1}=1-\lambda_{\max}(\nu_{j+1}),\qquad
r_j=\operatorname{Tr}(\rho_0Q_j^-),\qquad
m_j=\operatorname{dist}(Z_j,\mathcal J_{j+1}).
$$

有限 Walsh 柱最终被单个远位 $Q_j^-$ 杀掉，所以 $Q_j^-\to0$ 强，正常性给 $r_j\to0$。因此在所有充分深 $j$，

$$
\boxed{
\epsilon_{j+1}\ge\frac1{128^2(1+m_j)^2}
\ge\frac1{128^2(1+\|Z_j\|)^2}.
}
\tag{4.1}
$$

它控制的是下一尾最大特征值以外的总质量。与指定真空泄漏 $\delta_{j+1}$ 的关系仅为 $\epsilon_{j+1}\le\delta_{j+1}\to0$。

还可保留未取阈值的形式。由 (2.4)，令

$$
s=\left(\frac12-\frac r{1-\epsilon}\right)_+,
$$

重复 (3.6) 而不使用 $|b|\ge\tau/4$，得到

$$
\boxed{
(1+m)\sqrt\epsilon
\ge\frac14\left[s^2-\eta-\frac{\eta^2}{4}\right]_+.
}
\tag{4.2}
$$

其中 $(x)_+=\max(x,0)$。同一正常链上 $r_j,\epsilon_{j+1},\eta_j\to0$，所以

$$
\boxed{
\liminf_{j\to\infty}m_j\sqrt{\epsilon_{j+1}}\ge\frac1{16}.
}
\tag{4.3}
$$

因为 $\sqrt{\epsilon_{j+1}}\to0$，从 $1+m_j$ 换成 $m_j$ 不改变该下极限结论。

## 5. 与旧结果的准确区分及剩余问题

已全文复核的旧[正交叉块与条件锚稿](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)给的是本位 Walsh-minus 质量 $r_j$ 的必要下界及有限连续头不能恰为纯态；旧[完整尾理想商距离稿](R236-appendix-full-tail-ideal-quotient-cost-and-normal-anchors.md)将同一个 $r_j$ 界优化到完整尾理想。它们没有给下一尾的 $1-\lambda_{\max}$ 下界。

本稿新增的是同一完整尾理想距离与真实谱非纯质量之间的 (4.1)–(4.3)。它对任意秩正常态适用，未使用原有限秩假设，也没有把大支撑秩等同于大谱质量。

仍不能由这些界宣布不存在正常见证。原 $S_N$ 的未修正 $\|Z_j\|$ 已知增长很快，而它的增长不自动给 $m_j$ 的上界。只要没有控制同一完整尾理想中的实际 $m_j$，(4.1) 仍容许谱质量很小。它没有产生熵正密度，也没有与 R289 的正常有限秩尾熵界矛盾。

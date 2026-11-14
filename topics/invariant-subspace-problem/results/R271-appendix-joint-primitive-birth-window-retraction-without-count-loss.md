# R271 附录：整段 primitive 出生的联合回缩，不付出生数因子

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。

状态：**已证明。** 本稿将[任意远尾出生的已付回缩](R271-appendix-shifted-primitive-retractions-and-paid-actual-source-removal.md)联合成同一个原远尾中的整段出生空间。全部不同出生的交叉 Gram 使用原短 canonical 塔统一支付，所以源子空间扩大后，$\lambda\le C\alpha$ 中的常数不乘出生数或其平方根。原真正两费用投影及闭余图约束仍按前稿执行。

## 1. 固定同一个远尾，联合一整段出生

固定原 $m\ge5,d=2^m,A=A_m,D=D_m$ 和合法 $q$。取整数
$$
q=n+s,\qquad k\ge1,\qquad k-1\le T\le s,\qquad n\ge0.
$$
保留前 $k$ 个真实尾位，随后取 $n$ 个原相邻暗对。远尾起点为
$$
J=m+k+2n.
$$
记 $D_J$、$S_J$ 为这个**同一个**原远尾的删除与平方权和，且
$$
K_b^{(J)}=\ker D_J\cap\mathcal H_b^{(J)}.
$$
联合出生集合为
$$
\boxed{\mathcal I=[s-T,s-k+1]\cap\mathbb Z.}
\tag{1.1}
$$
它是一个非空有限整数区间，每个出生保留整个 $K_b^{(J)}$。

置
$$
H=T+d+1,\qquad P=s+d,\qquad
\boxed{\theta=\frac{12HP}{J+1}<\frac12,}
$$
$$
\boxed{
R=\exp\!\frac2{m+k+1},\qquad
\kappa^2=\frac{1-\theta}{1-2\theta},\qquad C=R\kappa.
}
\tag{1.2}
$$

模型第 $p$ 层为原 Hilbert 外直和
$$
\widehat{\mathcal H}_p=
\bigoplus_{\substack{b\in\mathcal I\\b\le p}}
\ \bigoplus_{\substack{I\subset\{m,\ldots,m+k-1\}\\|I|\le p-b}}
|I\rangle\otimes e_{p-b-|I|}\otimes K_b^{(J)}.
\tag{1.3}
$$
不同 $b$ 在模型中正交，但没有假设它们经原 canonical 截面后的像正交。模型删除在每个 $b$ 上是
$$
\widehat D=
\sum_{i=m}^{m+k-1}(i+1)^{-2}E_i+\sqrt{S_J}\,\mathfrak b,
\tag{1.4}
$$
并在系数空间 $K_b^{(J)}$ 上为恒等。源模型层为 $p=s$；原物理层比模型层多固定的 $n$ 孔。头始终是实际 $A_m$。

## 2. 联合分析行是整个创建塔的压缩

在原远尾第 $\ell$ 层，全部创建列组成的算子为
$$
W_\ell(f_b)_{b\le\ell}
=\sum_{b=0}^{\ell}
\frac{(D_J^*)^{\ell-b}f_b}
     {\sqrt{(\ell-b)!S_J^{\ell-b}}}.
$$
[完整双 Fock 塔](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)证明
$$
W_\ell=Q_\ell\mathcal U_\ell,\qquad
W_\ell^*W_\ell\preceq I,
$$
其中 $\mathcal U_\ell$ 是全部不同出生的玻色等距列。因此
$$
\boxed{\|P_{\mathcal I}W_\ell^*\|\le1.}
\tag{2.1}
$$
这里 $P_{\mathcal I}$ 只保留 $b\in\mathcal I$ 且 $b\le\ell$ 的外直和行。其第 $b$ 行准确为
$$
\frac{P_{K_b^{(J)}}D_J^{\ell-b}}
     {\sqrt{(\ell-b)!S_J^{\ell-b}}}.
\tag{2.2}
$$
不能只把逐行范数加起来；(2.1) 已经同时处理所有出生。

反向使用同一个原 canonical 塔
$$
V_\ell=(W_\ell^*)^{-1}.
$$
在使用的所有左右层中，$\ell\le s+d=P$。若 $b\in\mathcal I$ 且该列存在，则
$$
0\le\ell-b\le s+d-(s-T)=T+d<H.
$$
所以全部选中列都属于[短核 canonical 塔](R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md)的同一短列空间。由于
$4\delta_JHP\le\theta$，该稿的完整混合出生 Gram 给
$$
\boxed{\|V_\ell|_{\mathcal I}\|\le\kappa.}
\tag{2.3}
$$
这不是逐列估计的三角不等式。

还有完整的双正交恒等式
$$
\boxed{
(P_{\mathcal I}W_\ell^*)(V_\ell|_{\mathcal I})=I.
}
\tag{2.4}
$$
直接核验也成立：若一个分析行比截面的创建次数大，余下删除作用于 primitive 而为零；若较小，剩余正次 canonical 原像属于 $\operatorname{Ran}D^\dagger$，与对应 primitive 投影正交；次数相同才给恒等。没有把混合出生 Gram 置为对角。

## 3. 联合原尾回缩的统一范数和全部核旗

将 (2.1)--(2.4) 与强位恒等、中间原暗对泛函及单位暗向量张量，按全部使用层取直和。得到
$$
\boxed{
\mathsf T\mathsf B=I,\qquad
\|\mathsf T\|\le R,\qquad \|\mathsf B\|\le\kappa,
}
$$
$$
\boxed{
\mathsf TD=\widehat D\mathsf T,\qquad
D\mathsf B=\mathsf B\widehat D.
}
\tag{3.1}
$$
每个分析出生行按其准确平方根阶乘系数下降，模型删除保留出生 $b$；截面的同一恒等式来自 canonical 塔。

所以两向映射保全部 $D^h$ 核旗、原逐头旗和完整链方程。源截面的像
$$
\boxed{
\mathscr E_{\mathcal I}
=\mathsf B_s\left[
\bigoplus_{i=0}^{d-2}
e_i\otimes(\ker\widehat D^{d-i-1}\cap\widehat{\mathcal H}_s)
\right]\subseteq\mathscr R_q
}
\tag{3.2}
$$
是闭的，因为源分析是它的有界左逆。

对每个 $b\in\mathcal I$，
$$
s-b\ge k-1.
$$
因而在第 $j$ 个右段，有限的强位—单模式矩阵
$$
\widehat D^{j-1}:
\widehat{\mathcal H}_{s+j}^{(b)}
\longrightarrow\widehat{\mathcal H}_{s+1}^{(b)}
$$
已经在强位维数饱和区间，故为方形可逆矩阵张量 $I_{K_b^{(J)}}$。模型高输入在每个出生块上都为零，联合以后仍为零。于是
$$
\widehat\lambda=\widehat\alpha.
$$
借助保高域的准确距离运输，得到联合源子空间上的原结论
$$
\boxed{\lambda(r)\le C\alpha(r)
\qquad(r\in\mathscr E_{\mathcal I}).}
\tag{3.3}
$$
同一个 $C$ 与 $|\mathcal I|$ 无关。原新高 Schur 能量因此满足
$$
\boxed{
\lambda(r)^2-\alpha(r)^2
\le(C^2-1)\alpha(r)^2
\qquad(r\in\mathscr E_{\mathcal I}).
}
\tag{3.4}
$$
未对纯 $S_H^\dagger$ 修复作替换。

## 4. 整段出生的一组统一原预算

令 $H=T+d+1$，再要求
$$
\boxed{
q\ge128H^2,\qquad
T\le s\le\left\lfloor\frac q{192H}\right\rfloor,
\qquad n=q-s.
}
\tag{4.1}
$$
在这组参数非空时，$J+1\ge q$ 且 $d\le H$，所以
$$
\theta
\le\frac{12H(s+d)}q
\le\frac1{16}+\frac3{32}
=\frac5{32}<\frac14.
$$
从而
$$
\boxed{\kappa^2\le\frac32,\qquad C<2.}
\tag{4.2}
$$
例如可取 $T=d-1$ 并保留所有 $1\le k\le d$，只要 (4.1) 的 $s$ 区间非空。联合出生数此时为 $d-k+1$，仍没有新增该数量的范数因子。

这里固定的是同一个 $k$、同一个中间配对区和同一个远尾。不同 $k$ 或不同中间配对位置的源空间并未被免费相加；它们之间的交叉 Gram 若要联合，仍须另付。

## 5. 原实际源及既有余图上的完整删除

使用[已付实际源删除稿](R271-appendix-shifted-primitive-retractions-and-paid-actual-source-removal.md)的原两费用
$$
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle\mathfrak Mr,r\rangle,\qquad
\mathfrak M=J_{\rm bare}^{-1}
 +J_{\rm left}^{-1}J_{\rm right}J_{\rm left}^{-1}.
$$
令 $\mathscr D$ 为须保持的原闭源空间，包括已付的真正负图或其闭余图，取
$$
\mathscr Z=\mathscr E_{\mathcal I}\cap\mathscr D,\qquad
p=P_{\mathscr Z}^{\mathfrak M}r,\qquad r_{\rm rem}=r-p.
$$
则
$$
\boxed{
\Xi(r)^2=\Xi(p)^2+\Xi(r_{\rm rem})^2,\qquad
p,r_{\rm rem}\in\mathscr D,
}
$$
$$
\boxed{
\mu(p)\le\sqrt{C/2}\,\Xi(r),\qquad
\lambda(p)\le C\Xi(r).
}
\tag{5.1}
$$
证明仍是同一个原源上的
$\mu(p)^2\le\lambda(p)\lambda_{\rm flat}(p)
\le C\alpha(p)\lambda_{\rm flat}(p)$，继以真正 $\mathfrak M$ 投影的 Pythagoras。新残源的 flat 费用在这个真实度量内支付，没有从另一模型源搬来。

因此在 (4.1) 范围内，可统一用
$$
\mu(p)\le\Xi(r),\qquad
\lambda(p)\le2\Xi(r).
$$
对已经合法取得的实际族 $E_q^\dagger r\to w$、$\Xi(r)\to0$，新的左像仍趋于同一个 $w$，完整费用差趋零，两费用总和收缩。全部同头窗口的平方求和同样不增加出生数或窗数。

余源的条件始终是对真实交空间 $\mathscr Z$ 的 $\mathfrak M$ 正交；并不是在原物理空间中把 (1.1) 所列出生列坐标置零。一般剩余窄源、高费用比较及无权 $N=M$ 继续开放。

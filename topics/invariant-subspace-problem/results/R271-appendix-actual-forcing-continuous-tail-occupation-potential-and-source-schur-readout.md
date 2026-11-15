# R271 附录：实际 forcing 的连续尾占据势与受限逆的完整源读数

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文从实际 forcing 的全对正 Gram 得到一个准确的正对角占据势。它保全部碰撞，并给出原连续尾上真正受限来源的局部 Moore–Penrose 读数。所有先取逆／消核的操作均在同一个实际 forcing Gram 中进行。

这里的受限来源是原投影像，或原两个缺陷的直和。本文不把它替换成整个固定孔层，不把结果说成原环境 $D^\dagger$ 的新上界，也不删掉实际 $u_f$ 中两缺陷的抵消。帽返回投影后的像识别仍未支付。

依赖：[实际低端 forcing 的正删除 Gram 与完整 creation 行](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md)。下面重给所需原式与新结论的全部证明。

## 1. 同一个实际列与精确对角势

固定原强头、远尾起点 $x$ 和合法有限窗口。远尾为
$$
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
令 $\mathcal F$ 为原有限强头 forcing 空间，$i_0$ 为远真空嵌入。原 $K\subset V$ 与 $P_U=P_V-P_K$ 不变。取
$$
Z=P_Vi_0,\quad P_Ki_0,\quad\text{或 }(I-P_V)i_0.
$$
前稿在同一 $\mathcal F$ 上准确证明
$$
Z^*E_i^*E_jZ=
\frac{b_ib_j}{b_i^2+b_j^2}
 Z^*(n_i+n_j-2n_in_j)Z\qquad(i\ne j).
\tag{1.1}
$$
右边是正算子。它由原加权交换的压后谐和身份得到，未对单孔层重新选择来源。

对有限尾占据集 $I$ 定义
$$
\mathcal V_x(I)=
\sum_{i\in I}b_i^2+
2\sum_{\substack{i\in I\\j\ge x,\ j\notin I}}
\frac{b_i^2b_j^2}{b_i^2+b_j^2}.
\tag{1.2}
$$
令 $\mathcal V_x$ 为相应的物理对角算子，真空处取零。则
$$
\boxed{Z^*D^*DZ=Z^*\mathcal V_xZ.}
\tag{1.3}
$$

证明：展开 $D^*D$，对角项是 $\sum_i b_i^2n_i$。对每个无序对 $\{i,j\}$，两个非对角项由 (1.1) 合成
$$
2\frac{b_i^2b_j^2}{b_i^2+b_j^2}
(n_i+n_j-2n_in_j).
$$
这个对角因子恰在一位占据、一位空时为 $1$，其余为 $0$，故得到 (1.2)。所有原算子双和因 $b\in\ell^1$ 而绝对收敛；下文的上界也直接证明 $\mathcal V_x$ 有界。$\square$

(1.3) 是完整来源上的相等。虽然右边可以按孔数分解，不能仅由总和相等就宣布每个 $Zg$ 的单独孔分量仍满足 (1.1) 或 (1.3)。

## 2. 原连续位置的双侧势界

若 $I\ne\varnothing$ 且 $n=|I|$，则
$$
\boxed{
\frac13\sum_{i\in I}\frac1{(i+n+1)^3}
\ \le\ \mathcal V_x(I)\
\le\frac83\sum_{i\in I}\frac1{(i+1)^3}.
}
\tag{2.1}
$$
这两个常数不依赖 $n,x,Q$ 或强头维数。

对下界，固定 $i\in I$。当 $j>i$ 时 $b_j\le b_i$，所以
$$
\frac{2b_i^2b_j^2}{b_i^2+b_j^2}\ge b_j^2.
$$
在所有 $j>i$ 中最多有 $n-1$ 个已占据。由于 $b_j^2$ 递减，删去任意这些项后的和不小于删去最前的 $n-1$ 项后的和。因此
$$
2\sum_{\substack{j>i\\j\notin I}}
 \frac{b_i^2b_j^2}{b_i^2+b_j^2}
\ge\sum_{j\ge i+n}b_j^2
\ge\int_{i+n+1}^\infty t^{-4}\,dt
=\frac1{3(i+n+1)^3}.
$$
对所有 $i\in I$ 求和即可。这里使用的是仍为空的真正无限后尾，不是把有限临界池外的权置零。

对上界，保同一个 $i$，向较早位置的每项不超过 $2b_i^2$，向较晚位置的每项不超过 $2b_j^2$，所以
$$
\begin{aligned}
b_i^2+
2\sum_{j\notin I}\frac{b_i^2b_j^2}{b_i^2+b_j^2}
&\le [1+2(i-x)](i+1)^{-4}
 +2\sum_{j>i}(j+1)^{-4}\\
&\le\frac2{(i+1)^3}+\frac2{3(i+1)^3}.
\end{aligned}
$$
求和得 (2.1)。它同时给出 $\mathcal V_x\le\frac83\sum_{i\ge x}(i+1)^{-3}I$，故整个 Fock 空间上的对角势有界。

若 $\mathcal N$ 为远孔数，(1.3)--(2.1) 等价于同源二次型比较
$$
\boxed{
\frac13 Z^*\left[\sum_{i\ge x}
   \frac{n_i}{(i+\mathcal N+1)^3}\right]Z
\preceq Z^*D^*DZ
\preceq\frac83 Z^*\left[\sum_{i\ge x}
   \frac{n_i}{(i+1)^3}\right]Z .
}
\tag{2.2}
$$
中间从始至终是完整 $DZ$，不是先逐孔删去 nuisance 后得到的替代项。

## 3. 一个真正的受限源逆读数

对整数 $1\le p\le r$、$L\ge x$，令 $\Pi_{p,r,L}$ 是物理正交投影，保留
$$
p\le\mathcal N\le r,\qquad I\subseteq\{x,\ldots,L\}
$$
的占据配置，头部为恒等。它不被假定与原 $V,K$ 投影交换。

在这些配置上，(2.1) 给
$$
\mathcal V_x\ge\frac{p}{3(L+r+1)^3}.
$$
由正对角势，直接得到
$$
\boxed{
(\Pi_{p,r,L}Z)^*(\Pi_{p,r,L}Z)
\preceq c_{p,r,L}\,\mathcal G_Z,\qquad
c_{p,r,L}=\frac{3(L+r+1)^3}{p},\quad
\mathcal G_Z=Z^*D^*DZ.
}
\tag{3.1}
$$

这里 $\mathcal G_Z$ 是原有限 forcing 空间上的完整源 Gram，可以奇异。式 (3.1) 已证明
$\ker\mathcal G_Z\subseteq\ker(\Pi_{p,r,L}Z)$。因此有限维 Douglas 分解或直接平方根分解给
$$
\boxed{
\Pi_{p,r,L}Z\,\mathcal G_Z^\dagger Z^*\Pi_{p,r,L}
\preceq c_{p,r,L}I.
}
\tag{3.2}
$$
证明可以不假定普通逆存在：令
$A=DZ$、$B=\Pi_{p,r,L}Z$，在 $\operatorname{Ran}\mathcal G_Z^{1/2}$ 上
$B\mathcal G_Z^{\dagger/2}$ 的范数由 (3.1) 不超过
$\sqrt{c_{p,r,L}}$，在核上置零；乘其伴随即 (3.2)。

这也有真实物理 MP 的准确表述。令
$\mathcal Z=\operatorname{Ran}Z$，用原物理范数在 $\mathcal Z$ 中最小化，
$$
D_{\mathcal Z}=D|_{\mathcal Z}.
$$
$\mathcal Z$ 有限维，故其像闭，$D_{\mathcal Z}^\dagger$ 无域歧义。
对任意 $y\in\operatorname{Ran}(DZ)$，
$$
\boxed{
\|\Pi_{p,r,L}D_{\mathcal Z}^\dagger y\|
\le\sqrt{c_{p,r,L}}\,\|y\|.
}
\tag{3.3}
$$
确实任何 $z\in\mathcal Z$ 满足 $Dz=y$ 时都满足 (3.1) 的相应向量界；
两种原像的差在 $\mathcal Z\cap\ker D$，由 (1.3) 及 (2.1) 只可能有远真空，因此被 $\Pi_{p,r,L}$ 消掉。故 (3.3) 的读数独立于如何选原像。

完整 $\mathcal G_Z^\dagger$ 已先在全部 forcing 上消核后进入 (3.2)，没有先压到某个低维测试块再取逆。反过来，(3.3) 的定义域是实际像 $\mathcal Z$；它不能作为整个固定孔层的 $D^\dagger$ 上界。特别不与原连续尾的全层 primitive 逆下界冲突。

当 $p$ 与 $r,L$ 同阶时，这个实际来源的局部逆平方费用是 $O(p^2)$。此话仅指 (3.2)--(3.3) 的显示读数；所有更远位置以及物理再次投影都仍须保留。

## 4. 真正共同 head 合同和变化的来源族

对任意共同来源矩阵 $R:\mathcal G\to\mathcal F$，将 $Z$ 换成 $ZR$ 后，
(1.3)、(2.2)、(3.1)--(3.3) 全部成立，准确使用
$$
\mathcal G_{ZR}=R^*\mathcal G_ZR.
\tag{4.1}
$$
不要求 $R$ 可逆，也不以 $\|R\|^2$ 代替这个源 Gram。

同样，前稿的完整 creation 行保任意这样的合同。特别，对原实际
$$
Z_u=P_Ui_0,\qquad G_\Delta=I-i_0^*P_Ui_0,
$$
前稿准确有
$$
\sum_{i\ge x}\frac1{i+1}
E_iZ_uG_\Delta^\dagger Z_u^*E_i^*\preceq\frac83 I.
\tag{4.2}
$$
它还允许每个位置用不同的 head 来源，仍保共同缺陷度量。对任意有限族
$g_i\in\mathcal F$，
$$
\boxed{
\left\|\sum_i\frac{E_iZ_ug_i}{\sqrt{i+1}}\right\|^2
\le\frac83\sum_i\langle G_\Delta g_i,g_i\rangle .
}
\tag{4.3}
$$
证明只需令 $T_i=E_iZ_uG_\Delta^{\dagger/2}/\sqrt{i+1}$。
(4.2) 是整个合成行 $\sum_iT_iT_i^*\le8I/3$；
而 $\ker G_\Delta$ 上每个 $E_iZ_u$ 为零，故
$E_iZ_ug_i/\sqrt{i+1}=T_iG_\Delta^{1/2}g_i$。
因此任意共同 head 算子族 $R_i$ 给
$$
\left(\sum_i\frac{E_iZ_uR_i}{\sqrt{i+1}}\right)^*
\left(\sum_i\frac{E_iZ_uR_i}{\sqrt{i+1}}\right)
\preceq\frac83\sum_iR_i^*G_\Delta R_i.
\tag{4.4}
$$
这是不同来源的共同合成行，不是声称固定 $g$ 有
$\sum_i\|E_iZ_ug\|^2$ 上界。所有极限按右边平方可和的自然域取。

## 5. 同一个 $u_g$ 的两缺陷逆源，不删除其交叉

令
$$
\widetilde Zg=(e_g,k_g),\qquad
\mathcal A_\Delta=\operatorname{diag}(D,D)\widetilde Z,\qquad
\mathcal G_{\Delta,D}=\mathcal A_\Delta^*\mathcal A_\Delta.
$$
两个分量分别适用 (1.3)--(3.1)。由于 $p\ge1$，$\Pi_{p,r,L}i_0=0$，
所以
$$
\Pi_{p,r,L}u_g=-\Pi_{p,r,L}(e_g+k_g).
$$
只在最后用 $\|(a+b)\|^2\le2(\|a\|^2+\|b\|^2)$，得到
$$
\boxed{
(\Pi_{p,r,L}Z_u)^*(\Pi_{p,r,L}Z_u)
\preceq2c_{p,r,L}\,\mathcal G_{\Delta,D}.
}
\tag{5.1}
$$
由同一个有限维消核论证，
$$
\boxed{
\Pi_{p,r,L}Z_u\,\mathcal G_{\Delta,D}^\dagger
 Z_u^*\Pi_{p,r,L}\preceq2c_{p,r,L}I.
}
\tag{5.2}
$$
这保原同一个 forcing $g$，以及真正的联合源
$(De_g,Dk_g)$。不能把
$\mathcal G_{\Delta,D}=Z_e^*D^*DZ_e+Z_K^*D^*DZ_K$
换成 $Z_u^*D^*DZ_u$；后者中的 $De_g+Dk_g$ 可能相消。

因此本文得到的是同一个实际来源的联合局部读数，不是为两缺陷各选新的源，更不是原 $u_g$ 的独立环境逆估计。

## 6. 另一个准确的联合正性及未付接口

原 $[D,D^*]=S_xI-2W_x$，其中
$S_x=\sum_{i\ge x}b_i^2$、$W_x=\sum_{i\ge x}b_i^2n_i$。
由 (1.2)--(1.3) 立即有
$$
Z^*(D^*D+DD^*)Z
=S_xZ^*Z+
4Z^*\left[
\sum_{\substack{i\in I\\j\notin I}}
 \frac{b_i^2b_j^2}{b_i^2+b_j^2}
\right]_{\mathrm{diag}}Z
\succeq S_xZ^*Z.
\tag{6.1}
$$
这是本实际 forcing 像上的联合 gap，不是整个环境上的 gap；
即使有这个 gap，也不能单独推出原环境 MP 的界。

尚未闭合的原主配对仍含
$P_{\mathscr E_n}Y_{u_g,n}$ 以及其真正 inverse-adjoint／帽投影。
它们还没有被识别为本文的 $ZR$。
(4.3)--(4.4) 可直接用于已经明确写成共同 head 来源的行；
不能据此把任意物理左投影当作源合同。原顺次 MP 两端 partial sum
的负部也没有被 (3.2) 自动支付。

后继须把实际两端配对中的来源确实送入上述同源受限逆，
或控制剩余完整返回反馈。普通 $N=M$ 仍未由本文完成。

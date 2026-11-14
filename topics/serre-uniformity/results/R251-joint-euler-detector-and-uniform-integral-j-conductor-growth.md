# R251：联合 Euler 检测与变化二次域上的整 $j$ 导子下界

日期：2026-11-13。

**状态：已证明。** 本文在 R96 的同一个实际小惯性设置下证明：若 $j(E)\in\mathbb Z$，且实际正规化子商域 $K\ne\mathbb Q(\sqrt{-3})$，则对每个 $\delta>0$ 有绝对且有效的常数 $c_\delta>0$，使

$$\boxed{|D_K|\,c\ge c_\delta p^{5/3-\delta}.} \tag{251.1}$$

这里 $c\mathcal O_K$ 是实际 Cartan 三次商的精确导子。$K$ 可以变化，无类数限制，常数不依赖 $K$、$p$、$c$ 或额外偶阶导子 $b$。证明把实际 $E[3]$ 的三次 Kummer 角色放在固定域 $H=\mathbb Q(\zeta_3)$ 上，同时检测在 $K$ 中惰性的有理素数。所得是必要的下界；没有得到共同导子的上界，没有排除全部整 $j$，也不包括 $K=H$。

## 1. 实际对象与定理范围

设 $E/\mathbb Q$，$p>37$，并采用 R96 的精确假设

$$
\rho_{E,p}(G_{\mathbb Q})=N_{\rm ns}(p),\qquad
\rho_{E,p}(I_p)=C^3,\qquad j(E)\in\mathbb Z.
\tag{251.2}
$$

令 $K$ 为实际正规化子商二次域，$D=|D_K|$，$\lambda=\rho_{E,p}|_{G_K}$，并取阶恰为三的 $\vartheta:C\to\mu_3$。为区分两个不同三次角色，记

$$
\eta_K=\vartheta\circ\lambda,\qquad
\mathfrak f(\eta_K)=c\mathcal O_K.
$$

R66/R96 给

$$
p\equiv2,5\pmod9,\qquad
c=3^a R,\quad R\text{ 平方自由},\quad(R,3Dp)=1.
\tag{251.3}
$$

令 $\Delta$ 为全局最小判别式。R96 定理 96.1 的完整结论是

$$
q\mid R\ \Longleftrightarrow\ 3\nmid v_q(\Delta)
\quad(q\ne3,p),\qquad
3\nmid v_p(\Delta),
\tag{251.4}
$$

以及实际商域恒等式

$$
\mathcal L_3(E)=\mathbb Q(\zeta_3,\sqrt[3]{\Delta}),\qquad
\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3.
\tag{251.5}
$$

其中 (251.4) 包括 $q=2$。特别地，$\Delta$ 非立方；下文固定域上的三次角色没有遗漏平凡分支。

**定理 251.1。** 在 (251.2) 下，若 $K\ne H:=\mathbb Q(\zeta_3)$，则 (251.1) 成立。

本定理不需要无 CM 假设；若一个 CM 曲线满足全部实际假设，也必须满足同一下界。这不会把 $K=H$ 的 CM 分支错误地排除。

## 2. 固定域 $H$ 上两个角色的准确导子

取 $\eta=\eta_\Delta$ 为循环三次扩张

$$H(\sqrt[3]{\Delta})/H$$

的两个非平凡 Hecke 角色之一。由 (251.4)，$\eta$ 的阶恰为三。它不是 $\eta_K$；这里只用实际 $E[3]$ 商域把两者的分歧支撑联系起来。

### 2.1 三次角色

若 $q\ne3$，$H/\mathbb Q$ 在 $q$ 不分歧。Kummer 理论与 (251.4) 给：$\eta$ 在 $q$ 上方分歧，当且仅当 $q=p$ 或 $q\mid R$。分歧时为温和循环三次分歧，每个素理想处的导子指数为一。$q$ 上方全部素理想范数的积等于 $q^2$。

在 $3$ 处，令 $\pi=1-\zeta_3$，并记 $U_n=1+\pi^n\mathcal O_{H_3}$。有 $v_\pi(3)=2$。对数及指数在 $U_2$ 上互逆，且

$$\log(U_2)=\pi^2\mathcal O_{H_3},\qquad
3\pi^2\mathcal O_{H_3}=\pi^4\mathcal O_{H_3}.$$

因而

$$U_4=(U_2)^3.$$

每个阶三局部角色都杀掉 $U_4$，所以三处导子指数至多四。由此得到足够且统一的界

$$\boxed{N_H\mathfrak f_\eta\le81p^2c^2.} \tag{251.6}$$

这一步允许 $3\mid c$ 及所有野分歧分支，不要求三处导子达到这个上界。

### 2.2 检测变化二次域的角色

令 $\chi_K$ 为 $K/\mathbb Q$ 的二次 Dirichlet 角色，并在 $H$ 上定义

$$\mu=\chi_K\circ N_{H/\mathbb Q}.$$

因为 $K\ne H$，$KH/H$ 是非平凡二次扩张，所以 $\mu$ 的阶恰为二。其导子满足

$$\mathfrak f_\mu\mid D\mathcal O_H,
\qquad N_H\mathfrak f_\mu\le D^2. \tag{251.7}$$

例如，在有限点上，若 $u\equiv1\pmod{D\mathcal O_H}$，则 $N(u)\equiv1\pmod D$；这直接给所需的模数上界，也涵盖 $D$ 的野分歧部分。

记

$$\xi=\mu\eta.$$

$\mu$ 与 $\eta$ 的阶互素，所以 $\xi$ 的阶恰为六，特别是非实角色。它的导子整除两个导子的最小公倍数。对固定虚二次域使用有限解析导子

$$C_\chi=|D_H|N_H\mathfrak f_\chi=3N_H\mathfrak f_\chi,$$

有

$$
C_\mu C_\eta\le729D^2p^2c^2,
\qquad C_\xi\le C_\mu C_\eta.
\tag{251.8}
$$

## 3. 非实有限阶角色的有效 $L(1)$ 下界

下面只在固定域 $H$ 上使用此引理。

**引理 251.2。** 对任意阶恰为六的 Hecke 角色 $\xi$，任意 $\epsilon>0$，有有效的

$$|L(1,\xi)|\gg_{H,\epsilon} C_\xi^{-\epsilon}. \tag{251.9}$$

**证明。** 令 $T/H$ 为 $\xi$ 切出的循环六次扩张。其全部角色是 $\xi^j$，导子均整除 $\mathfrak f_\xi$。Thorner–Zaman 的 Theorem 3.1 应用于 $T/H$：存在绝对有效的 $c_0>0$，使所有这些 $L$ 函数的乘积在

$$\Re s>1-\frac{c_0}{\log(4C_\xi(|\Im s|+3)^2)}$$

至多有一个零点，且若存在，必为某个实角色的简单实零点。非实的 $\xi$ 因而在此区域无零点。$L(1,\xi)\ne0$ 也由同一 abelian 分解与 Dedekind zeta 的简单极点得到。

取 $Q\ge\max(3,C_\xi)$，并把 $c_0$ 缩小为固定有效常数，令

$$r=\frac{c_0}{100\log(100Q)},\qquad z_0=1+2r.$$

闭圆盘 $|s-z_0|\le4r$ 落在上述无零区中；取与 $z_0$ 处 Euler 展开一致的解析分支 $F(s)=\log L(s,\xi)$。在圆心，绝对收敛的 Euler 展开给

$$|F(z_0)|\le\log\zeta_H(1+2r)=O_H(1+\log\log(100Q)). \tag{251.10}$$

标准有效凸性估计由 Hecke 函数方程、右半平面 Euler 界和 Phragmén–Lindelöf 原理给出：对任意 $u>0$，在这个圆盘上

$$|L(s,\xi)|\ll_{H,u} Q^{r+u}\ll_{H,u}Q^u.$$

故 $\sup\Re F\le u\log Q+O_{H,u}(1)$。在同心半径 $3r$ 的圆盘应用 Borel–Carathéodory 不等式；$s=1$ 位于其中，且两个半径之比固定，于是

$$|F(1)|\le 6u\log Q+O_{H,u}(1+\log\log(100Q)).$$

给定 $\epsilon$，先选足够小的 $u$，再把 $\log\log Q$ 项吸收入 $\epsilon\log Q$，得到有效的 $|L(1,\xi)|\gg_{H,\epsilon}Q^{-\epsilon}$。取 $Q=\max(3,C_\xi)$ 即得 (251.9)。所有常数可有效取得；没有使用实二次角色的 Siegel 下界。证毕。

## 4. 联合 Euler 检测定理

**定理 251.3。** 固定虚二次域 $H$，并令 $C_\chi=|D_H|N_H\mathfrak f_\chi$。设 $\mu$ 是非平凡二次 Hecke 角色，$\eta$ 是非平凡三次 Hecke 角色，且 $\xi=\mu\eta$。设

$$Q\ge\max(3,C_\mu C_\eta),$$

并令 $\mathcal B$ 为包含两角色全部分歧素理想的有限集合，满足

$$\prod_{\mathfrak q\in\mathcal B}N\mathfrak q\le Q^A$$

中的固定 $A>0$。则对任意 $\epsilon>0$，存在 $\mathfrak q\notin\mathcal B$ 使

$$\boxed{
\mu(\mathfrak q)=-1,\qquad \eta(\mathfrak q)\ne1,\qquad
N\mathfrak q\ll_{H,A,\epsilon}Q^{3/8+\epsilon}.
} \tag{251.11}$$

常数有效。

### 4.1 完整局部 Euler 恒等式

上标 $\mathcal B$ 表示删除集合内的全部 Euler 因子。考虑

$$
F_+(s)=\zeta_H^{\mathcal B}(s)L^{\mathcal B}(s,\xi),
\qquad
F_-(s)=L^{\mathcal B}(s,\mu)L^{\mathcal B}(s,\eta).
\tag{251.12}
$$

在 $\mathfrak q\notin\mathcal B$ 处，置 $x=(N\mathfrak q)^{-s}$，两侧局部因子分别为

$$
\frac1{(1-x)(1-\mu(\mathfrak q)\eta(\mathfrak q)x)},
\qquad
\frac1{(1-\mu(\mathfrak q)x)(1-\eta(\mathfrak q)x)}.
\tag{251.13}
$$

若 $\mu(\mathfrak q)=1$ 或 $\eta(\mathfrak q)=1$，这两个有理函数完全相同；相同的不只是一次系数，而是所有素理想幂的系数。在 $\mathcal B$ 内两侧因子均为一。

因此，若 $N\mathfrak q\le X$ 时都没有 (251.11) 的角色值组合，则 $F_+$ 和 $F_-$ 的每个范数至多 $X$ 的理想系数相等。

### 4.2 变化坏集合的完整乘子

删除任意一个 $L(s,\chi)$ 的坏因子，乘上的是

$$P_{\chi,\mathcal B}(s)=\prod_{\mathfrak q\in\mathcal B}
(1-\chi(\mathfrak q)(N\mathfrak q)^{-s}),$$

其中分歧处按惯例置 $\chi(\mathfrak q)=0$；对 zeta 置 $\chi=1$。对任意 $u>0$，

$$\sup_t|P_{\chi,\mathcal B}(1/2+it)|\ll_{H,A,u}Q^u. \tag{251.14}$$

证明是把每个因子界为 $1+(N\mathfrak q)^{-1/2}$，并对足够大的范数用
$1+n^{-1/2}\le n^{u/A}$；所有小范数素理想只给固定有限积。两个因子的乘积只需把 $u$ 再缩小。

同理，对任意 $u>0$，

$$\prod_{\mathfrak q\in\mathcal B}(1-(N\mathfrak q)^{-1})
\gg_{H,A,u}Q^{-u}. \tag{251.15}$$

这里使用大范数时 $1-n^{-1}\ge n^{-u/A}$，并显式保留固定有限的小范数积。因此截断主项和误差都没有隐藏依赖于变化集合的常数。

### 4.3 紧支撑 Mellin 比较

取

$$w(t)=(1-t)^8\quad(0\le t\le1),\qquad w(t)=0\quad(t>1).$$

它的 Mellin 变换为

$$\widehat w(s)=\frac{8!}{s(s+1)\cdots(s+8)},\qquad
\widehat w(1)=\frac19. \tag{251.16}$$

写 $F_\pm(s)=\sum_{\mathfrak a}a_\pm(\mathfrak a)(N\mathfrak a)^{-s}$，并令

$$S_\pm(X)=\sum_{\mathfrak a}a_\pm(\mathfrak a)w(N\mathfrak a/X).$$

如果目标素理想在 $X$ 以内不存在，§4.1 给准确等式 $S_+(X)=S_-(X)$。这是采用紧支撑权的原因：没有未受控制的尾部。

Yang 的 Corollary 1.2（R229 §2 已核准其固定域 Eisenstein 特化的有效性）给任意酉 Hecke 角色

$$|L(1/2+it,\chi)|\ll_{H,u}
C_\chi^{3/16+u}(1+|t|)^{3/8+2u}. \tag{251.17}$$

对 $F_-$ 使用两个该估计，利用 $C_\mu C_\eta\le Q$。对 $F_+$ 使用 $C_\xi\le Q$ 的同一估计，以及固定函数 $\zeta_H(1/2+it)$ 的凸性增长。结合 (251.14) 和 (251.16) 的 $O((1+|t|)^{-9})$ 衰减，Mellin 移线从 $\Re s=2$ 到 $1/2$ 给

$$
S_-(X)=O_{H,A,u}(Q^{3/16+u}X^{1/2}),
\tag{251.18}
$$

$$
S_+(X)=\frac{\mathcal R X}{9}
+O_{H,A,u}(Q^{3/16+u}X^{1/2}).
\tag{251.19}
$$

这里 $F_-$ 整，$F_+$ 仅在 $s=1$ 有一个简单极点，其留数为

$$
\mathcal R=\operatorname{Res}_{s=1}\zeta_H(s)\,L(1,\xi)
\prod_{\mathfrak q\in\mathcal B}
\left(1-\frac1{N\mathfrak q}\right)
\left(1-\frac{\xi(\mathfrak q)}{N\mathfrak q}\right).
\tag{251.20}
$$

小参数 $u$ 已在 (251.18)–(251.19) 中重新命名。水平边由同一固定次数的凸性增长及 (251.16) 消失；有限 Euler 多项式在整个闭条带 $1/2\le\Re s\le2$ 的界同样由 (251.14) 的证明控制。没有假设角色 $\mu$ 的零点不靠近一；零点不妨碍此次移线。

由引理 251.2、(251.15) 和

$$\left|1-\frac{\xi(\mathfrak q)}{N\mathfrak q}\right|
\ge1-\frac1{N\mathfrak q},$$

对任意 $u>0$ 有有效的

$$|\mathcal R|\gg_{H,A,u}Q^{-u}. \tag{251.21}$$

留数可以是复数，证明只使用其绝对值，不假装谱或系数为正。若 $S_+=S_-$，(251.18)–(251.21) 强迫

$$X\ll_{H,A,u}Q^{3/8+4u}.$$

先选 $4u<\epsilon$，再取 $X$ 为足够大有效常数乘以 $Q^{3/8+\epsilon}$，即产生矛盾。定理 251.3 得证。

## 5. 保留指定 Frobenius 的全分歧好约化扩张

下面引理不要求惯性像交换，也不要求所取扩张为 Galois 扩张。

**引理 251.4。** 设 $E/F$ 为非阿基米德局部域上的潜在好约化椭圆曲线，剩余域为 $\mathbb F_q$。给定任意映到 $1\in\widehat{\mathbb Z}=G_F/I_F$ 的算术 Frobenius 提升 $\phi\in G_F$，存在有限全分歧扩张 $F_\phi/F$，使 $E$ 在其上好约化，且 $\phi\in G_{F_\phi}$ 是该好约化模型的 Frobenius 提升。

**证明。** 选剩余特征以外的素数 $\ell$。令

$$J=\ker\bigl(I_F\longrightarrow\operatorname{Aut}T_\ell(E)\bigr),
\qquad\Gamma=I_F/J.$$

潜在好约化给 $\Gamma$ 有限，且 $J$ 是 $G_F$ 的闭正规子群。于是

$$1\longrightarrow\Gamma\longrightarrow G_F/J
\longrightarrow\widehat{\mathbb Z}\longrightarrow1.$$

令 $P$ 为 $\phi$ 在 $G_F/J$ 中的像所生成的闭子群。$P$ 是 procyclic 群，且映满 $\widehat{\mathbb Z}$。procyclic 群若有这样的满商，其每个素数的 supernatural 阶指数均为无穷，故 $P\simeq\widehat{\mathbb Z}$；所给生成元映到 $1$，所以该映射是同构。特别地，$P\cap\Gamma=1$。这给出明确截面和分解

$$G_F/J=\Gamma\rtimes P.$$

取 $P$ 在 $G_F$ 中的逆像 $G_\phi$。它是指数 $|\Gamma|$ 的闭子群，因而开；同时

$$G_\phi\cap I_F=J,\qquad
G_\phi\longrightarrow\widehat{\mathbb Z}\text{ 满射}.$$

其固定域 $F_\phi$ 的剩余次数为一，分歧指数为 $|\Gamma|$，所以扩张全分歧。其惯性为 $J$，在 $T_\ell(E)$ 上作用平凡。Néron–Ogg–Shafarevich 判据给好约化，而 $\phi\in G_\phi$ 仍映到剩余群中的 $1$。证毕。

因此，若 $F=\mathbb Q_q$，此指定提升的特征多项式在任意素于 $q$ 的 Tate 模上都是

$$T^2-aT+q,\qquad a\in\mathbb Z,\quad |a|\le2\sqrt q. \tag{251.22}$$

同一个整数 $a$ 同时控制模 $p$ 和模 $3$ 表示。

## 6. 联合检测素数的实际矛盾

把定理 251.3 应用于 §2 的 $H=\mathbb Q(\zeta_3)$、$\mu$、$\eta$，取

$$Q=729D^2p^2c^2,$$

并令 $\mathcal B$ 包含 $6Dpc$ 上方的全部素理想。则

$$\prod_{\mathfrak q\in\mathcal B}N\mathfrak q
\le(6Dpc)^2\le Q,$$

所以 $A=1$，常数对变化的 $K$ 仍统一。

若未分歧有理素数 $q$ 在 $H$ 中惰性，其上方素理想范数为 $q^2$，并且

$$\mu(\mathfrak q)=\chi_K(q)^2=1.$$

故 (251.11) 的素理想必有剩余次数一，写 $N\mathfrak q=q$。得到有理素数

$$
q\equiv1\pmod3,\quad \chi_K(q)=-1,\quad
q\nmid6Dpc,\quad \eta(\mathfrak q)\ne1,
\tag{251.23}
$$

以及重新命名 $\epsilon$ 后的有效界

$$\boxed{q\ll_\epsilon(Dpc)^{3/4+\epsilon}.} \tag{251.24}$$

因为 $j(E)$ 整，$E/\mathbb Q_q$ 潜在好约化。任取算术 Frobenius 提升 $\phi$。$q$ 在 $K$ 中惰性且 $K$ 在 $q$ 不分歧，所以 $\rho_{E,p}(\phi)$ 位于 $N\setminus C$，迹为零。对引理 251.4 的好约化模型，(251.22) 给

$$a\equiv0\pmod p.$$

若 $q<p^2/4$，Hasse 界强迫 $a=0$。再看同一 Frobenius 在 $E[3]$ 上的矩阵 $A$。由 $q\equiv1\pmod3$，

$$\operatorname{Tr}A=0,\quad\det A=1,\quad A^2=-I.$$

$A$ 的阶为四，且位于 $\operatorname{SL}_2(\mathbb F_3)$。由于 $\operatorname{SL}_2(\mathbb F_3)/Q_8$ 的阶为三，$A$ 的 $S_3$ 商像为一。

然而 (251.5) 是同一个实际 $E[3]$ 的商域。$q\nmid3pc$ 保证该商在 $q$ 不分歧，所以无论选择哪一个 Frobenius 提升，其在商域中的像都由 (251.23) 的 $\eta(\mathfrak q)\ne1$ 给出一个非平凡三循环。这与上段矛盾。

因此检测到的素数必须满足

$$q\ge p^2/4. \tag{251.25}$$

结合 (251.24)，

$$Dc\gg_\epsilon p^{2/(3/4+\epsilon)-1}.$$

该指数当 $\epsilon\to0^+$ 时趋于 $5/3$。对任意 $\delta>0$ 选足够小的 $\epsilon$，即得 (251.1)。所有 Hecke 估计都在固定域 $H$ 上进行；变化域的依赖已经完整计入 $D$，从而常数是绝对且有效的。定理 251.1 得证。

## 7. 准确后果与尚未闭合的方向

对任意固定 $K\ne H$，定理立即给 $c\gg_{K,\delta}p^{5/3-\delta}$；但本定理更强的部分是允许 $D$ 变化的 (251.1)。没有使用 $h_K=1$、固定 CM 参考曲线或非平凡六次差角色的额外分支。

对一般变化 $K$，(251.1) 不能改写成 $c\gg p^{5/3-\delta}$，因为 $D$ 本身可能增长。它也不能反向提供 $M_*=D(bc)^2$ 的上界。特别地，R249 已解决实际 CM 因子的秩零接口后，仍需要额外的全局限制才能排除所有整 $j$。

$K=H$ 时 $\mu=1$，(251.12) 两个函数处处相等；联合检测不存在。这个分支必须使用不同的实际角色约束，本证明没有覆盖它。

## 8. 依赖与来源

- [R96：实际判别式的三次支撑与 $3$ 处的精确导子分支](../results/R96-actual-cubic-discriminant-support-and-local-three-branches.md)，定理 96.1、§2.1–2.3：实际 $E[3]$ 商域、全部 $q\ne3,p$ 的判别式支撑、$3\nmid v_p(\Delta)$。其证明已经包括野特征二，本文不重用只对交换惯性成立的旧局部引理。
- [R229：三次 Hecke 角色的小素理想与更强的实际导子增长](../results/R229-cubic-hecke-burgess-and-stronger-conductor-growth.md)，§2：Yang 的固定域 GL(1) Burgess 界及本题 Eisenstein 特化的有效性。
- Liyang Yang，*Relative trace formula and twisted L-functions: the Burgess bound*，Compositio Mathematica **162** (2026), no.11, 2591–2641，DOI [10.1017/S0010437X26103327](https://doi.org/10.1017/S0010437X26103327)，Corollary 1.2，式 (1.3)；作者稿 [arXiv:2305.10719](https://arxiv.org/abs/2305.10719)。本文只使用固定域 GL(1) 推论，并以 $\chi|\cdot|^{it}$ 处理竖线。
- Jesse Thorner、Asif Zaman，*A unified and improved Chebotarev density theorem*，Algebra & Number Theory **13** (2019), 1039–1068，DOI [10.2140/ant.2019.13.1039](https://doi.org/10.2140/ant.2019.13.1039)，[出版者全文](https://msp.org/ant/2019/13-5/ant-v13-n5-p02-p.pdf)。准确使用 §2 的 (2-14)–(2-18) 及 p.1051 的 Theorem 3.1；§3 的 $Q$ 定义为 $D_H\max_jN\mathfrak f_{\xi^j}[H:\mathbb Q]^{[H:\mathbb Q]}$，在本题至多 $4C_\xi$。只调用其有效无零区，不调用变化底域的最小素数结论。

本文是纯证明稿，没有计算证书、脚本或数据依赖；主定理的全部变化参数、坏 Euler 因子和局部 Frobenius 构造均在正文明确追踪。

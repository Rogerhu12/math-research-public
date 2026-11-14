# R243附录：指数圆周预算去掉尾条件的对数损失

日期：2026-11-13（UTC+8）。作者：kernel；Astra-ISP-1cf8c51d 复核。状态：已证明。末节覆盖任意缓慢满足 $a_j=o((j+1)^{-1})$ 的明确交替类。

## 1. 新判据

沿用
$$
X=X_{a_*+\sum_j a_j\chi_j},\qquad
s_m=a_*+\sum_{j<m}a_j,\qquad
g_m=\|a_{\ge m}\|_2.
$$
假设存在 $b<\infty$，使充分大 $j$ 满足
$$
|a_j|\le\frac b{j+1}.
\tag{1.1}
$$
设某个趋无穷序列 $m=m_\nu$ 满足
$$
t_m:=m g_m^2\longrightarrow0.
\tag{1.2}
$$
则存在完全由该实际系数行决定的整数 $p_m\to\infty$ 与数 $\varepsilon_m\to0$，使
$$
\boxed{
\|(X^*-\overline{s_m}I)^{p_m}Q_m\|
\le\varepsilon_m^{p_m}.
}
\tag{1.3}
$$
$Q_m$ 仍是所有前 $m$ 位柱函数的投影，且其中向量确在所需自然幂域中。

因此[R243](R243-partial-sum-centers-and-log-tail-polynomial-cyclicity.md)中的所有谱位置／Bell 核推论，都可以在 (1.1) 下把原条件
$$
m g_m^2(1+\log(1+B_m))\to0
$$
减弱为 (1.2)。具体而言：

- 若同时 $s_m\to s$，每个非零闭有界 $X$ 不变分支的谱都包含 $s$；有有限谱时，其谱只能为 $\{s\}$。
- 对任意非零标量多项式 $q$、任意第一阶复 $\ell^2$ 指数权 $w$，若 $q(s)\ne0$，则 $q(u)e^w$ 循环。
- 若部分和有两个不同聚点，各自沿满足 (1.2) 的序列取得，则全部非零 $q(u)e^w$ 循环。

证明不以一个未知核上的尾速率作为输入。(1.1)–(1.2) 都是原系数行的可核条件。

## 2. 真实自然幂与整向量轨道

仍写
$$
X-s_mI=H_m+Z_m,\qquad
H_m=\sum_{j<m}a_j(V_j-I).
\tag{2.1}
$$
$H_m$ 有界，与闭尾 $Z_m$ 域交换，且其有界扰动的自然幂域相同。R207 附录 A–B 给固定模型常数 $C$（可取 17），使
$$
\|Z_m^rQ_m\|\le(Cg_m\sqrt r)^r\qquad(r\ge1).
\tag{2.2}
$$
这些是实际自然幂。

因此算子值级数
$$
\mathcal E_{Z_m}(z)Q_m
=\sum_{r=0}^\infty\frac{z^r}{r!}Z_m^rQ_m
$$
在每个紧圆盘上按算子范数一致收敛，定义一个整函数。这里并不声称无界 $Z_m$ 在全 $H$ 上有有界指数算子。

由 (2.2)，对 $R=|z|$，
$$
\|\mathcal E_{Z_m}(z)Q_m\|
\le\sum_{r=0}^\infty
 \frac{(Cg_mR\sqrt r)^r}{r!}
\le\sqrt2\exp(e^2C^2g_m^2R^2).
\tag{2.3}
$$
最后一个估计完全初等：$r!\ge(r/e)^r$ 使第 $r$ 项不超过
$(eCg_mR)^r/r^{r/2}$，再用 $r!\le r^r$ 及 Cauchy–Schwarz，
$$
\sum_{r\ge0}\frac{x^r}{\sqrt{r!}}
=\sum_{r\ge0}2^{-r/2}\frac{(\sqrt2x)^r}{\sqrt{r!}}
\le\sqrt2e^{x^2}.
$$
$r=0$ 的项按 1 解释。

真实二项式与绝对收敛允许重排，从而
$$
\boxed{
\mathcal E_m(z):=
\sum_{p=0}^\infty\frac{z^p}{p!}(X-s_mI)^pQ_m
=e^{zH_m}\mathcal E_{Z_m}(z)Q_m.
}
\tag{2.4}
$$
这只是具体有限柱输入上的整轨道，足以合法应用算子值 Cauchy 系数估计。

## 3. 单个位的实际 Cayley 指数预算

记
$$
G_j=a_j(V_j-I)=-2a_jN_j(I+N_j)^{-1}.
$$
由 $N_j^2=\eta_jN_{j+1}$ 与实际逆界 $\|(I+N_j)^{-1}\|\le3$，
$$
G_j=-2a_jN_j+K_j,\qquad
K_j=2a_jN_j^2(I+N_j)^{-1},\qquad
\|K_j\|\le6|a_j|\eta_j.
\tag{3.1}
$$
$K_j$ 与 $N_j$ 交换，所以指数确实分解。

置 $r=|za_j|$。偶次与奇次分别估计给
$$
\begin{aligned}
\|e^{-2za_jN_j}\|
&\le \cosh(2r\sqrt{\eta_j})
 +2r\,\frac{\sinh(2r\sqrt{\eta_j})}{2r\sqrt{\eta_j}}\\
&\le(1+2r)e^{2r\sqrt{\eta_j}}.
\end{aligned}
$$
当 $r=0$ 时按连续值解释。故
$$
\boxed{
\|e^{zG_j}\|
\le(1+2|za_j|)
\exp\bigl((2\sqrt{\eta_j}+6\eta_j)|za_j|\bigr).
}
\tag{3.2}
$$
这一步保留了所有真实进位与 Cayley 分母；没有把 $N_j$ 换成平方零矩阵。

定义有限尾成本
$$
\kappa_J=\sum_{j\ge J}|a_j|(2\sqrt{\eta_j}+6\eta_j).
\tag{3.3}
$$
由 $a\in\ell^2$ 和 $\eta_j\le e^{-770\,16^j}$，该级数收敛且
$\kappa_J\to0$。

## 4. 有限低头的指数增长显式小于线性半径

前稿的进位计数给
$$
\|H_J^k\|\le(6B_J)^k
\quad(k\ge0),\qquad
\|H_J^k\|\le(6B_J)^k e^{-\gamma k^4}
\quad(k\ge\max(2J,16)),
\tag{4.1}
$$
其中 $B_J=\sum_{j<J}|a_j|$、$\gamma=770/16^4$。

对 $J\ge8$、$R\ge1$，记
$$
w=6B_JR,\quad
L=\log(1+w),\quad
C_\gamma=\sum_{k\ge0}e^{-\gamma k^4/2}<\infty,\quad
c_\gamma=\frac{3}{4(2\gamma)^{1/3}}.
$$
指数级数中 $k<2J$ 的和至多 $2J(1+w)^{2J}$。对 $k\ge2J$，弃去分母 $k!$ 并使用
$$
k\log_+w-\gamma k^4
\le c_\gamma(\log_+w)^{4/3}-\frac\gamma2k^4,
$$
得到
$$
\|e^{zH_J}\|
\le2J e^{2JL}+C_\gamma e^{c_\gamma L^{4/3}}
\le e^{F_J(R)}
\qquad(|z|=R),
\tag{4.2}
$$
其中完全显式地取
$$
F_J(R)=\log(2J+C_\gamma)+2J\log(1+6B_JR)
+c_\gamma\bigl[\log(1+6B_JR)\bigr]^{4/3}.
\tag{4.3}
$$

若 $J\le\sqrt R$，则 $B_J\le\|a\|_2\sqrt J\le\|a\|_2R^{1/4}$，所以
$$
\frac{F_J(R)}R
=O\!\left(\frac{\log(2+R)}{\sqrt R}
+\frac{[\log(2+R)]^{4/3}}R\right)\longrightarrow0.
\tag{4.4}
$$
该估计对所有这样的 $J\ge8$ 一致。没有使用一个只知存在而无增长预算的低头预解常数。

## 5. 高头的坐标包络只支付 $\log(R/m)$

令 $m\ge J$，且 $J$ 大到足以使用 (1.1)。所有 $G_j$ 彼此交换，由 (3.2)、(4.2)，
$$
\log\|e^{zH_m}\|
\le F_J(R)+
\sum_{j=J}^{m-1}\log\left(1+\frac{2bR}{j+1}\right)
+R\kappa_J.
\tag{5.1}
$$
对 $x>0$，记
$$
I(x)=(1+x)\log(1+x)-x\log x
=\log(1+x)+x\log(1+1/x).
$$
因 $t\mapsto\log(1+2bR/t)$ 递减且在 0 附近可积，
$$
\sum_{j=1}^m\log(1+2bR/j)
\le\int_0^m\log(1+2bR/t)\,dt
=mI(2bR/m).
$$
再用 $x\log(1+1/x)\le1$，得到
$$
\boxed{
\log\|e^{zH_m}\|
\le F_J(R)
+m\bigl[\log(1+2bR/m)+1\bigr]
+R\kappa_J.
}
\tag{5.2}
$$
与直接把 $H_m$ 范数写成 $6B_m$ 不同，这里没有产生 $m\log B_m$ 的预算。

## 6. 半径、阶数与整个全柱幂界

先考虑无限支撑，故 $g_m>0$。沿 (1.2) 的序列，选取
$$
L_m=t_m^{-1/2},\qquad
R_m=mL_m,\qquad
J_m=\min\{m,\lfloor\sqrt{R_m}\rfloor\}.
\tag{6.1}
$$
则
$$
L_m\to\infty,\quad R_m\to\infty,\quad J_m\to\infty,\quad
J_m\le\sqrt{R_m},\quad
g_m^2R_m=t_mL_m=\sqrt{t_m}\to0.
\tag{6.2}
$$
最终 $J_m\ge8$ 且已超过 (1.1) 的起点。

将 (2.3)、(2.4)、(5.2) 合并，得到
$$
\sup_{|z|=R_m}\|\mathcal E_m(z)\|\le e^{\Lambda_m},
\tag{6.3}
$$
其中实际有限上界为
$$
\begin{aligned}
\Lambda_m={}&F_{J_m}(R_m)
+m\bigl[\log(1+2bL_m)+1\bigr]
+R_m\kappa_{J_m}\\
&+\tfrac12\log2+e^2C^2g_m^2R_m^2.
\end{aligned}
\tag{6.4}
$$
每一项除以 $R_m$ 后都趋零：

- 第一项由 (4.4)；
- 第二项为 $[\log(1+2bL_m)+1]/L_m\to0$；
- 第三项为 $\kappa_{J_m}\to0$；
- 常数项除以 $R_m$ 趋零；
- 最后一项为 $e^2C^2g_m^2R_m=e^2C^2\sqrt{t_m}\to0$。

所以
$$
\Lambda_m/R_m\longrightarrow0.
\tag{6.5}
$$
现在选真实整数
$$
p_m=\left\lceil\sqrt{R_m(1+\Lambda_m)}\right\rceil.
\tag{6.6}
$$
于是
$$
p_m\to\infty,\qquad
p_m/R_m\to0,\qquad
\Lambda_m/p_m\to0.
$$
对 (2.4) 的整函数作 Cauchy 系数估计，再用 $p!\le p^p$，得到
$$
\begin{aligned}
\|(X-s_mI)^{p_m}Q_m\|^{1/p_m}
&\le \frac{(p_m!)^{1/p_m}}{R_m}e^{\Lambda_m/p_m}\\
&\le \frac{p_m}{R_m}e^{\Lambda_m/p_m}
=:\varepsilon_m\longrightarrow0.
\end{aligned}
\tag{6.7}
$$
$CQ_m=Q_mC$ 与 $X^*=CXC$ 在具体自然幂域上给相同的伴随界，即 (1.3)。

如果 $a$ 有有限支撑，则充分大 $m$ 的尾为零，直接用有限解析头的四次型幂估计即可；这一退化情况不需要 (6.1)。

## 7. 原 Haar 核上的推论，不越过一般谱缺口

为保持推理完整，设 $0\ne M$ 闭，
$M\subseteq\operatorname{Dom}X$、$XM\subseteq M$，并令 $Y=X|_M$。闭图定理给 $Y$ 有界，且通常伴随域上有
$$
P_MX^*=Y^*P_M.
$$
若沿同一序列 $s_m\to s\in\rho(Y)$，则 $\|(Y-s_m)^{-1}\|$ 最终一致有界。真实迭代和 (1.3) 给
$$
\|P_MQ_m\|
\le\left(\|(Y-s_m)^{-1}\|\varepsilon_m\right)^{p_m}
\longrightarrow0,
$$
与 $Q_m\to I$ 强矛盾。因此 $s\in\sigma(Y)$。

只有在 $\sigma(Y)$ 有限时，才对每个非零 Riesz 子空间重复上述论证，推出 $\sigma(Y)=\{s\}$。两个不同的相应聚点则排除全部有限谱有界分支。

R176 的真实 Bell 多项式核与倾斜核正好具有这种有限谱分支结构，且其谱包含于 $q$ 的有限零集。所以本稿 §1 的全部循环性推论成立。一般有界分支的谱并未被自动缩成单点；也未由此推出所有未知不变限制像稠密。

## 8. 任意缓慢趋零的交替振幅

取正数列
$$
\epsilon_0=1,\qquad
\epsilon_j\downarrow0,\qquad
\sum_{j\ge0}\frac{\epsilon_j}{j+1}=\infty,
$$
并令
$$
a_j=\frac{(-1)^j\epsilon_j}{j+1},\qquad a_*=0.
\tag{8.1}
$$
这些系数满足 $a_0=1$、$a_j=o((j+1)^{-1})$。对每个 $m$，
$$
m g_m^2
\le m\epsilon_m^2\sum_{j\ge m}(j+1)^{-2}
\le\epsilon_m^2\longrightarrow0.
\tag{8.2}
$$
所以 (1.1)–(1.2) 成立，没有对 $\epsilon_m$ 的下降速率加任何进一步要求。

交错级数给
$$
s_m\longrightarrow s,\qquad 0<s<1.
$$
正、负子列的绝对和都发散：递减正项的交错部分和有界，而两侧总和的和发散，因此两侧必须同时发散。故 R138 给这些 first 全平面连续谱。

取危险点态平方 $q(z)=z^2-1$。因 $q(s)\ne0$，得到
$$
\boxed{(u^2-1)e^w\text{ 对 }A\text{ 循环}}
\tag{8.3}
$$
对每个第一阶复 $\ell^2$ 指数权 $w$ 成立，特别 $u^2-1$ 循环。实际 Bell 算子 $X^2+B_2-I$ 的自然域核为零。这里保留 $a_*=0$，确实对应首位系数为 1 的原危险平方。

一个比此前固定对数幂更慢的具体例子是
$$
\epsilon_j=
\bigl[\log\log(j+e^e)\bigr]^{-1/4}.
\tag{8.4}
$$
它在 $j=0$ 等于 1，单调趋零，而 $\sum\epsilon_j/(j+1)$ 仍发散。初等积分比较给
$$
m g_m^2\asymp(\log\log m)^{-1/2},\qquad
\log(1+B_m)\asymp\log\log m.
$$
因此旧的 $m g_m^2(1+\log(1+B_m))$ 反而趋无穷；本稿的新判据仍适用。上述比较可分别对函数
$x^{-2}(\log\log x)^{-1/2}$、
$x^{-1}(\log\log x)^{-1/4}$ 积分，并对候选主项求导核实。

常数振幅 $\epsilon_j\equiv1$ 不满足 (1.2)。所以本稿没有通过取极限关闭规范交替调和行。


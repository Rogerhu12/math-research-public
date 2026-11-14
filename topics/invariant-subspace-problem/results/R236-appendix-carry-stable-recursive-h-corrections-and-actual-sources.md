# R236 附录：原慢行的 carry 稳定 h 修正与全层实际源预算

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的实际构造。** 对原 $S_N$、$S_Y$，本文逐层构造完整尾理想中的正规化首行，并以常数项加极小 carry 的逆替代未控制的奇块逆。给出原右源、真实下一尾代表和条件真空锚；没有得到随层一致有界的代表，也未排除正常见证。

## 1. 原模型中的准确 carry 尺度

原实际归一化幂满足
$$
N_j=\begin{pmatrix}0&\eta_jN_{j+1}\\I&0\end{pmatrix},\qquad
\|N_j\|=1,
$$
其中 [R12 §1](../results/R12-normalized-powers-and-compact-commutant.md) 的准确数值为
$$
u_j:=-\log\eta_j
=1400\,16^j-630\,8^j+300\,2^j.
\tag{1.1}
$$
特别
$$
770\,16^j\le u_j\le1400\,16^j,
\qquad \eta_0=e^{-1070},\qquad 0<\eta_j<1/100.
\tag{1.2}
$$
以下每一项均在原真实范数尾代数中；完整 $A'$ 只在解释完整理想时使用。

## 2. 一次 h 修正的完整代数恒等式

假设已得到当前尾行
$$
P_j=N_j+R_j,\qquad R_j\in\mathcal B_{j+1},\qquad \chi(R_j)=0.
$$
把 $R_j$ 再按下一物理位分块：
$$
R_j=p+Nb,\qquad N=N_{j+1},\qquad
N^2=t=\eta_{j+1}N_{j+2},\qquad p,b\in\mathcal B_{j+2}.
\tag{2.1}
$$
这些是真实块系数，故
$$
\|p\|,\|b\|\le\|R_j\|.
$$
令 $\tau=\eta_j$。准确尾交生成元为
$$
h_j=R_j^2-\tau N=C+Nd,
$$
$$
C=p^2+tb^2,\qquad d=2pb-\tau I.
\tag{2.2}
$$
由于 $\chi(p)=0$，$\chi(d)=-\tau\ne0$，所以 $d$ 是实际单位。
直接正规化会得到 $G=C d^{-1}$，其范数目前没有可用的一致预算。

改为定义下一真实尾的单位
$$
q=\tau^2 I+4tb^4
\tag{2.3}
$$
以及
$$
\boxed{
R_{j+1}=
[-2bp^3-\tau p^2+6tb^3p-5\tau tb^2]q^{-1}.
}
\tag{2.4}
$$
$q$ 的常数字符为 $\tau^2$；下一节还将直接支付其 Neumann 小参数逆。
$R_{j+1}\in\mathcal B_{j+2}$，且 $\chi(R_{j+1})=0$。

定义原当前尾中的真实源因子
$$
\boxed{
A_j=[4b^2N-(\tau I+2pb)]q^{-1}.
}
\tag{2.5}
$$
则有完整算子恒等式
$$
\boxed{N_{j+1}+R_{j+1}=h_j A_j.}
\tag{2.6}
$$
因此新行仍来自原实际理想，而且在目标和前向源中都没有 $d^{-1}$。

**核验。** 用 $N^2=t$ 展开 $(C+Nd)[4b^2N-(\tau+2pb)]$。
其奇块系数是
$$
4b^2C-d(\tau+2pb)
=4b^2(p^2+tb^2)-(2pb-\tau)(2pb+\tau)=q.
$$
其偶块是
$$
4tb^2d-(\tau+2pb)C
=-2bp^3-\tau p^2+6tb^3p-5\tau tb^2.
$$
乘 $q^{-1}$ 正是 (2.6)。全部 carry 均被保留。

这也是一个明确的下一层 $h$ 修正，而非只换了一个相似记号。
对直接正规化的 $G=Cd^{-1}$，置
$$
h_{\rm raw}=G^2-t,\qquad W=4b^2d q^{-1}.
$$
直接乘法给
$$
\boxed{G-R_{j+1}=h_{\rm raw}W.}
\tag{2.7}
$$
一个无需除 $b$ 的核验式是
$$
Cq-d[-2bp^3-\tau p^2+6tb^3p-5\tau tb^2]
=4b^2(C^2-td^2).
$$
所以 (2.4) 确实使用了全部实际 $h$ 关系来削去原奇块逆。

## 3. 真逆、目标与源的逐步预算

令 $M\ge\max\{1,\|R_j\|\}$，并记
$$
\epsilon_j=\frac{4\eta_{j+1}M^4}{\eta_j^2}.
\tag{3.1}
$$
若 $\epsilon_j\le1/2$，则 (2.3) 的逆可直接按原范数求和：
$$
q^{-1}=\tau^{-2}\sum_{r=0}^{\infty}
(-4\tau^{-2}tb^4)^r,
\qquad
\boxed{\|q^{-1}\|\le2\tau^{-2}.}
\tag{3.2}
$$
因此 (2.4)–(2.5) 给
$$
\boxed{
\|R_{j+1}\|\le8M^4\eta_j^{-2},\qquad
\|A_j\|\le14M^2\eta_j^{-2}.
}
\tag{3.3}
$$
例如第一式的分子范数至多
$(2+6\eta_{j+1})M^4+\eta_j(1+5\eta_{j+1})M^2$；
结合 $\eta_j,\eta_{j+1}<1/100$ 和 (3.2)，(3.3) 有充分余量。
同样，(2.7) 的实际 $h$ 修正源满足
$$
\boxed{\|W\|\le24M^4\eta_j^{-2}.}
\tag{3.4}
$$

若此前已经有原右源
$$
P_j=S\,\mathcal U_j,
$$
则
$$
h_j=(R_j-N_j)P_j
$$
和 (2.6) 给可执行的下一源
$$
\boxed{
\mathcal U_{j+1}=\mathcal U_j(R_j-N_j)A_j,
\qquad P_{j+1}=S\mathcal U_{j+1}.
}
\tag{3.5}
$$
由 (3.3)，
$$
\boxed{
\|\mathcal U_{j+1}\|
\le28\|\mathcal U_j\|M^3\eta_j^{-2}.
}
\tag{3.6}
$$
这里没有把源只当成某个抽象闭理想成员。
每一层都给一个有限次有理运算定义的真实 $\mathcal A$ 右因子。

### 3.1 关于反向单位的范围

$A_j$ 的常数字符准确为 $-1/\eta_j$，所以它是实际单位。
若只需代数理想身份，确有
$P_{j+1}\mathcal C_{j+1}=h_j\mathcal C_{j+1}$。
但本文的定量前向源 (3.5) 不使用 $A_j^{-1}$。

为明确保留反向的实际费用，令
$Z_j=2pb-4b^2N$，则
$$
A_j^{-1}
=-\eta_j^{-1}q\sum_{r=0}^{\infty}(-\eta_j^{-1}Z_j)^r,
$$
$$
\|A_j^{-1}\|
\le\frac{\|q\|}{\eta_j}
\sum_{r=0}^{\infty}\eta_j^{-r}\|Z_j^r\|<\infty.
\tag{3.7}
$$
$Z_j$ 零字符且属于单生成拟幂零范数代数，故该 Neumann 级数按算子范数收敛。
(3.7) 没有被声称满足 (3.3) 的廉价上界，也没有进入下面的前向预算。
即使完全不使用此反向单位，(2.6)、(3.5) 仍独立证明每个 $P_j$ 的实际来源。

## 4. 原 $S_N$、$S_Y$ 都有便宜的起点

现在固定原两条慢行之一
$$
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jN_j(I+N_j)^{-1},\qquad
a_j=(j+1)^{-2}.
$$
这里 $a_0=1$，且
$$
\sum_{j\ge1}a_j
\le\frac14+\int_2^\infty x^{-2}\,dx=\frac34.
$$

对 $S_N$，直接取
$$
R_0=\sum_{j\ge1}a_jN_j,\qquad
\mathcal U_0=I,
$$
故 $P_0=S_N$、$\|R_0\|<1$。

对 $S_Y$，记 $t_0=\eta_0N_1$、
$F_1=\sum_{j\ge1}a_jN_j(I+N_j)^{-1}$。
恒等式
$$
N_0(I+N_0)^{-1}=(N_0-t_0)(I-t_0)^{-1}
$$
给
$$
R_0=(I-t_0)F_1-t_0,\qquad
\mathcal U_0=I-t_0,
\qquad P_0=S_Y\mathcal U_0=N_0+R_0.
\tag{4.1}
$$
又
$$
\|N_j(I+N_j)^{-1}\|
\le\frac{1+\eta_j}{1-\eta_j}\le\frac{101}{99},
$$
所以
$$
\|R_0\|
\le\frac{(1+1/100)^2}{1-1/100}\frac34+\frac1{100}<1,
\qquad \|\mathcal U_0\|<2.
\tag{4.2}
$$
两者都满足下节的同一初值，不需要 $S_Y$ 的消元商有保函数锥符号。

## 5. 全层 Neumann 条件与明确单指数预算

定义
$$
E_j=\exp(240\,16^j).
$$
对上节任一原慢行，(2.1)–(3.5) 给所有层的实际构造，且
$$
\boxed{
\|R_j\|\le E_j,\qquad
\|\mathcal U_j\|\le E_j.
}
\tag{5.1}
$$

证明：初值由 §4 成立。假设第 $j$ 层成立，在 (3.1) 取 $M=E_j$。
由 (1.2)，
$$
\epsilon_j
\le4\exp\{[-770\cdot16+4\cdot240+2\cdot1400]16^j\}
=4e^{-8560\,16^j}<\frac12.
\tag{5.2}
$$
所以所有实际 $q^{-1}$ 都已由 (3.2) 支付。
再用 (3.3)、(3.6)，目标和源分别至多
$$
8e^{3760\,16^j},\qquad28e^{3760\,16^j}.
$$
二者均不超过
$e^{3840\,16^j}=E_{j+1}$，归纳完成。

还可记录较准确的预算。令 $L_0=0$、
$$
L_{j+1}=4L_j+2u_j+\log8.
$$
则
$$
\boxed{
\|R_j\|\le e^{L_j},\qquad
\|\mathcal U_j\|\le2(7/2)^j e^{L_j}.
}
\tag{5.3}
$$
第二式由 (3.6) 与 $L_{j+1}$ 逐步相减得到。
(1.1) 的几何求和给
$$
\begin{aligned}
L_j={}&\frac{700}{3}(16^j-4^j)
-315(8^j-4^j)+300(4^j-2^j)\\
&+\frac{\log8}{3}(4^j-1).
\end{aligned}
\tag{5.4}
$$
因此
$$
\boxed{
\limsup_{j\to\infty}16^{-j}\log\max\{1,\|R_j\|\}
\le\frac{700}{3},
\quad
\limsup_{j\to\infty}16^{-j}\log\max\{1,\|\mathcal U_j\|\}
\le\frac{700}{3}.
}
\tag{5.5}
$$
这是真正原度量下的有限上界，不是将 $\|\pi(G_j)\|\le1$ 当作提升估计。

## 6. 对原完整 $h/k$ 商的含义

令 $G_j^{\rm old}$ 表示未作本修正的原一次尾交递推商。
每个 $P_j=N_j+R_j$ 都由 (3.5) 属于原 $S\mathcal A$，同时是实际第 $j$ 层尾。
原规范仍为 $S_j^{\rm old}=D_j^{\rm old}(N_j+G_j^{\rm old})$，
故完整余式是 $\mathfrak r_j(a+N_jb)=a-G_j^{\rm old}b$。特别
$$
\mathfrak r_j(N_j+R_j)=R_j-G_j^{\rm old}\in\mathcal J_{j+1}'(S).
$$
于是
$$
\boxed{
\operatorname{dist}(G_j^{\rm old},\mathcal J_{j+1}'(S))
\le\|R_j\|\le e^{L_j}.
}
\tag{6.1}
$$
对超弱闭尾理想同样成立。若还有第二生成元 $Z$，完整联合尾理想更大，
(6.1) 仍给有效上界；每个前向证书只用原 $S$，没有把 $Z$ 的系数或 $k$ 的逆藏入常数。

(2.7) 同时展示了在每一新正规化下的实际 $h$ 修正源及其 (3.4) 费用。
本文没有声称把这些修正重新写回旧规范的每个 $h/k$ 系数时，所有反向单位仍遵守 (5.3)。
真正用于原理想和正常配对的、已支付的前向证书是 (3.5)。

因此这不是对 raw $G_j$ 范数作下界后误称为商距离；
它是通过明确实际理想修正而得到的完整商**上界**。
不过该上界仍增长，不能推出排正常湮灭所需的有界子列。

## 7. 同一原正常态、实际源与条件真空锚

在第 $j$ 位令 $e=(e_0+e_1)/\sqrt2$，定义
$$
\Theta_j=2(N_j+R_j)(I+N_j)^{-2}.
\tag{7.1}
$$
由于 $R_j$ 属于下一尾，真实二乘二计算给
$$
e^*(I+N_j)^{-2}e=0,\qquad
e^*N_j(I+N_j)^{-2}e=\frac12I.
$$
故
$$
\boxed{e^*\Theta_j e=I,\qquad\omega_j(\Theta_j)=1.}
\tag{7.2}
$$
该锚未用纯模型替代原 carry。

实际原源为
$$
\boxed{\Theta_j=S\,[2\mathcal U_j(I+N_j)^{-2}],}
\tag{7.3}
$$
并且
$$
\|2\mathcal U_j(I+N_j)^{-2}\|
\le\frac8{(1-\eta_j)^2}\|\mathcal U_j\|,
$$
$$
\|\Theta_j\|
\le\frac{8(1+\|R_j\|)}{(1-\eta_j)^2}
\le17e^{L_j}.
\tag{7.4}
$$
因此这些指定目标的范数归一锚至少为 $\frac1{17}e^{-L_j}$。
没有声称它有不消失的统一下界，也没有将该下界计作改进既有全部目标的最佳 $q_j$ 估计。

若同一个原正正常 $\rho$ 湮灭 $S\mathcal A'$，
(3.5)、(7.3) 保证它湮灭全部本稿行及目标，不改变 $\rho$。
在[原正交叉块稿 §§2–3](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)中，
令 $\Lambda_j=(I+t_j)/2$、$t_j=\eta_jN_{j+1}$，
小范数正常泛函是 $\psi_j(V)=\operatorname{Tr}(\rho_{j+1}(R_j+\Lambda_j)V)$。
准确身份
$$(R_j+\Lambda_j)(R_j-\Lambda_j)=R_j^2-t_j-(I-t_j)^2/4$$
解释了以下测试中出现 $R_j-\Lambda_j$：代入
$V=(R_j-\Lambda_j)(I-t_j)^{-2}$，前一项由原完整尾理想湮灭，故配对为 $-\tau_\rho/4$。
由同一正交叉块界，得到个别位的明确必要条件：
记 $r_j=\operatorname{Tr}(\rho P_{\chi_j})$、$\tau_\rho=\operatorname{Tr}\rho$，则
$$
\|R_j-(I+\eta_jN_{j+1})/2\|
\ge\frac{(1-\eta_j)^2}{4(1+\eta_j)}
\sqrt{\frac{\tau_\rho}{r_j}}.
$$
结合 (5.3) 和 $\eta_j<1/100$，例如有
$$
\boxed{r_j\ge\frac{\tau_\rho}{64}e^{-2L_j}.}
\tag{7.5}
$$
这仍与正常性相容；不能对所有正常态额外假设 $\sum_jr_j<\infty$。

## 8. 当前已新增的内容与仍需继续的实际问题

本文新增的是完整、可重复执行的原 $h$ 修正 (2.4)–(2.7)，
其所需逆的真实小参数预算，以及 $S_N/S_Y$ 全层的前向源和同一正常锚。
原奇块逆的任意增长没有被当成既定商障碍；它已被实际改写为 (5.3) 的可支付单指数预算。

仍须继续使用第二生成元或更有效的修正，把 (6.1) 的增长降到足以保住统一正常锚的尺度，
或者构造另一族带已付原源的目标。
本稿不把这种明确但增长的上界当作普通 ISP 或原正常湮灭问题的完成。

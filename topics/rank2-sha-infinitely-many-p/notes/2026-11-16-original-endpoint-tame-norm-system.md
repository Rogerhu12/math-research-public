# 原 q/q⁴ 端点的全 split tame 范数系统与不改变首层的整修正

日期：2026-11-16。**状态：下述有限层范数系统已证明。** 本篇直接从 R831/R832 的原端点循环出发，构造全部良好分裂辅助素数上的四维 Euler 范数系统。首层准确是该原循环的 étale Abel–Jacobi 类；所有层的分母有统一界。证明不要求先把 R885 的 DR wild 提升与 ACR §6 的整套提升相认。

本篇不证明首层类非零，不使用 Selmer 群消失，也不把四维系统投到一维后仍出现的另外三个 Euler 因子删除。最后一节明确保留这个区别。本文只有符号证明，没有数学数值执行。

## 1. 原来源、全四维表示与首层规范

取 R885 的原 K=Q(ω)、ψ₀、十八阶 η，以及
$$
\eta_4=\eta^{13},\quad \eta_{10}=\eta,\quad
\eta_{16}=\eta^7,\quad
\psi=\psi_{17}=\eta^3\psi_0,\quad
\beta_j=\eta_j^{-2}\psi_0.
\tag{1}
$$
固定一个原有序对
$$
(j,k)=(10,16),(16,4),(4,10),
\qquad (f,g,h)=
(\theta_\psi,\theta_{\beta_j},\theta_{\beta_k}).
\tag{2}
$$
共同 tame 层是 N=10404，g、h 的新层是 M=2601。
三者均为权2、平凡 nebentypus。实际旧向量仍为
$$
f(Q),\qquad g(Q),\qquad 4h(Q^4).
\tag{3}
$$
这里第三槽的4来自 τ↦4τ 对微分的真实拉回。

令 W 为先取 f 的指定 K-CM 符号后得到的原四维表示。按照 R885 的算术互反与 Tate 规范，
$$
W=(V_g\otimes V_h)\widehat\psi\,\varepsilon_{\rm cyc}^{-1}.
\tag{4}
$$
在 ACR 的几何记号中，同一个表示写作
$V_g\otimes V_h(\psi_{\mathfrak P}^{-1})(-1)$。
本文所有 Frobenius、CM 商和 Euler 多项式使用这一组相容约定。

记 $\mathcal Z_{02}$ 为 R831(4) 在共同目标
$X_0(N)\times X_0(M)^2$ 中的原端点类，再取 f 的这个 CM 符号。
用原固定对应定义
$$
z^{\rm end}_p=\operatorname{AJ}_{p,W}(\mathcal Z_{02})
\in H^1(K,W).
\tag{5}
$$
它的最高 CM 分量就是 R885 的 $z^{\rm end}_{\ell,p}$。
不在构造前删掉 W 的其余三个分量。

以下 $p>211$ 属于原普通 ray。固定包含原全部角色值的有限 p-adic 系数域 E，环为 O。
若 T⊂W 是固定稳定格，则存在一个与 n 无关的整数 $c_p\ge0$，
以及对全部平方自由良好分裂 n 的类
$$
c_n\in H^1(K[n],p^{-c_p}T),
\tag{6}
$$
满足
$$
\boxed{\quad c_1=z^{\rm end}_p,\qquad
\operatorname{cor}_{K[nq]/K[n]}c_{nq}
=P_{\mathfrak q}(\mathrm{Fr}_{\mathfrak q}^{-1})c_n .\quad}
\tag{7}
$$
这里 q∤Np n，q 在 K 中分裂，选 $(q)=\mathfrak q\bar{\mathfrak q}$；
$K[n]$ 是导子 n 的环类域的最大 p 子扩张，且
$$
P_{\mathfrak q}(X)
=\det(1-\mathrm{Fr}_{\mathfrak q}^{-1}X\mid W^\vee(1)).
\tag{8}
$$
换用格 $p^{-c_p}T$ 后，(6)是整系统。本文不将该统一清分母说成原循环在任意格上本原。

## 2. 原端点在 ACR 有限层构造中的准确位置

使用 ACR §4 的模曲线
$$
Y(m)=Y(1,N(m)).
$$
其额外 m 部分是 cyclic 子群的 Γ₀(m) 条件；
不选择该子群的生成元，也不为每个新 q 作 $1/(q-1)$ 平均。

ACR Definition4.1 取
$$
(r_1,r_2,r_3)=(0,0,0),\qquad r=0.
\tag{9}
$$
所以 determinant section 精确为1，所有 symmetric-power 系数层为常数层。
原类 $\kappa_m^{(1)}$ 是该模曲线小对角的 Gysin/HS 类，
再取三份 $h^1$ 分量。这个权零系数构造本身适用(9)；
不使用仅在三个权均至少3时陈述的 BSV Proposition8.3。

取 n 平方自由，定义 ACR 的 asymmetric 类
$$
\kappa_n^{(2)}
=(1,1,\langle n\rangle')_*
 (1,\pi_1,\pi_2)_*\kappa_{n^2}^{(1)}.
\tag{10}
$$
$\pi_1,\pi_2:Y(n^2)\to Y(1)$ 是逐步忘记、quotient 该 cyclic 部分的实际退化映射。
(9)使原 $n^{r_2}$ 系数为1。
第三槽 diamond 在本文平凡 nebentypus 上最终作用为1，但在执行(10)之前保留它。

在第二、三槽施原 R831 的 $q_0,q_2$ 提取映射，而非任意同表示的线性映射；
第一槽施原 f 新因子。
ACR §4（刊本 p16）明确允许这些任意固定旧向量，且各映射在所有 n 上由同一 tame 对应给出。
由于 q∤N，新增 q 退化对应与原二处 $q_0/q_2$ 对应交换。

在 n=1 时，(10)中所有新增退化映射与 diamond 都是恒等。
此时小对角与原 modified diagonal 之差均含至少一个零次或二次 CK 因子，
被三份 $h^1$ 提取杀掉；原 cusp CK 相容已由 R829/R831 的 Manin–Drinfeld 证明支付。
因此最低层不是仅与原循环同表示，而是原循环本身的 AJ。

还可用固定 θ₅ 保证这一识别与原同调平凡化完全一致：
$$
\vartheta_5=(T_5-6)^{\otimes3},\qquad
C_5=(-6)^3=-216 .
\tag{11}
$$
5 在 K 中惰性，故三条原 CM 形式及第一槽的所有环类变形均有 $a_5=0$。
5 不属于本文的分裂辅助素数集合。
所以 $\vartheta_5/C_5$ 在全部已选 cuspidal 商上恒为1，且 p>211 时其分母为单位。
此处没有 R804 的椭圆单位30平滑因子。

## 3. X₀/X₁ 与旧副本的倍率不随 n 改动

为与 ACR 的 $X_1$ 呈示比较，始终用 R831(21)–(25)的原遗忘映射：
$$
D_X=1632,\qquad D_C=816,\qquad
A_*\mathcal Z_{02}^{(1)}=D_X\mathcal Z_{02},\qquad
\mathcal Z_{02}^{(1)}=D_C^{-2}A^*\mathcal Z_{02}.
\tag{12}
$$
回到 $X_0(N)^3$ 的指定 old 副本时保留 $6^{-2}$；
回到 $X_1(N)^3$ 时保留 $12^{-2}$。
这些都是开始时固定的对应，不随辅助层增长。
本文的 $c_1$ 使用共同目标的(5)；若从 $X_1$ 执行，则按(12)作一次固定返回。
这样(7)没有未显示的 $D_X$、6、12 或第三槽4。

ACR 的 CM/Shapiro 系统只在第一槽变动。
ACR Theorem3.3、Corollary3.6给所有 n 上相容的整 CM Hecke 商同构，
并使其 norm 对应变成诱导表示的真正 norm。
在 n=1 将同构一次校准为(5)中固定的 K-CM 符号识别；
对全部 n 使用同一个常数校准。
允许这个固定基变换有 p 分母，但它不产生层数相关的分母。

由此，按 ACR §4 的真实 CM 商、投到 $O[\operatorname{Gal}(K[n]/K)]$
并施 Shapiro，得到原始类
$$
\widetilde c_n\in H^1(K[n],W),
\qquad \boxed{\widetilde c_1=z^{\rm end}_p.}
\tag{13}
$$
从固定导子环类群取商时，η仍在表示 $\psi_{\mathfrak P}^{-1}$ 内；
没有把有限十八阶角色连同系数群一起取平凡平均。

## 4. 八个单步几何对应与三条双步行

为说明同源范数，先保留三槽而不投特征值。
在 r=0、平凡 diamond 的本文情形，ACR Lemma4.2给
$$
\begin{array}{c|c}
\text{推前}&\text{在 }\kappa_m^{(1)}\text{ 上的作用}\\ \hline
(\pi_2,\pi_1,\pi_1)&(T_q,1,1)\\
(\pi_1,\pi_2,\pi_2)&(T'_q,1,1)\\
(\pi_1,\pi_2,\pi_1)&(1,T_q,1)\\
(\pi_2,\pi_1,\pi_2)&(1,T'_q,1)\\
(\pi_1,\pi_1,\pi_2)&(1,1,T_q)\\
(\pi_2,\pi_2,\pi_1)&(1,1,T'_q)\\
(\pi_1,\pi_1,\pi_1)&q+1\\
(\pi_2,\pi_2,\pi_2)&q+1 .
\end{array}
\tag{14}
$$
最后两行假设 q∤m；前六行也用于 q 已在中间层的第二次下降。
$T_q,T'_q$ 是 ACR §2.4 的互为 Poincaré 伴随的两个方向，不能在全来源上先混同。
在最后的平凡 nebentypus权2新形式商上，它们才有相同特征值。

(14)来自“共同 cyclic q 子群”与“对其中一个槽作 q-isogeny”的有限 Cartesian 图：
忘记共同子群有 q+1 个选择；
单槽 quotient 给 Hecke 图形；
两槽 quotient 经 dual isogeny 给伴随图形。
在常数系数(9)下，isogeny 对系数层没有附加 q 幂。
这些图形保留所有原 N-level 和二处端点数据。
没有对 q+1 个子群或 q−1 个生成元除法。

令 $\pi_{ij}$ 表示在第一槽连续两次下降 q。
把(14)代入(10)，使用中间层的 $T_q^2$ 分解，
ACR Lemma4.4在本文给三条完整行
$$
\begin{aligned}
(\pi_{11},1,1)_*\kappa_{nq}^{(2)}
 &=\bigl((1,1,T_qT'_q)-(q+1)\bigr)\kappa_n^{(2)},\\
(\pi_{21},1,1)_*\kappa_{nq}^{(2)}
 &=\bigl((1,T'_q,T'_q)-(T'_q,1,1)\bigr)\kappa_n^{(2)},\\
(\pi_{22},1,1)_*\kappa_{nq}^{(2)}
 &=\bigl((1,(T'_q)^2,1)-(q+1)\bigr)\kappa_n^{(2)}.
\end{aligned}
\tag{15}
$$
所有 diamond 因子在这三行已经按原平凡字符求值。
(15)中第二、三槽仍是(3)，并未重新取 spherical 同副本。

## 5. 原始四次 Laurent 范数因子

令
$$
A_q=a_q(g),\quad B_q=a_q(h),\quad
a_{\mathfrak q}=\psi(\mathfrak q),\quad
a_{\bar{\mathfrak q}}=\psi(\bar{\mathfrak q}).
$$
q 在 K 中分裂、三形式中心特征为1，故
$$
a_{\mathfrak q}a_{\bar{\mathfrak q}}=q.
\tag{16}
$$
在环类系数群中，$(q)$ 为主理想，两个 Frobenius 互逆。
写
$$
x_q=\frac{a_{\mathfrak q}}q\,\sigma_{\mathfrak q}^{-1},
\qquad
y_q=\frac{a_{\bar{\mathfrak q}}}q\,\sigma_{\mathfrak q},
\qquad x_qy_q=q^{-1}.
\tag{17}
$$
这些都是整群环的单位：q≠p，$a_{\mathfrak q}$ 是 p 单位。

ACR 的真正第一槽 CM norm 为
$$
\pi_{11*}-(x_q+y_q)\pi_{21*}+q^{-1}\pi_{22*}.
\tag{18}
$$
第一槽 $T'_q$ 的 CM 商值是 $q(x_q+y_q)$。
将(15)逐项代入(18)，得到
$$
\begin{aligned}
Q_q
&=B_q^2-(q+1)
 -(x_q+y_q)\bigl(A_qB_q-q(x_q+y_q)\bigr)
 +q^{-1}\bigl(A_q^2-(q+1)\bigr)\\
&=\boxed{\;
q(x_q^2+y_q^2)-A_qB_q(x_q+y_q)
 +A_q^2/q+B_q^2-q-q^{-1}.\;}
\end{aligned}
\tag{19}
$$
于是同一个原始来源严格满足
$$
\operatorname{cor}_{K[nq]/K[n]}\widetilde c_{nq}
=Q_q\,\widetilde c_n .
\tag{20}
$$
这就是 ACR Proposition4.5(i)在原权2、原角色上的完整式。
尤其 $A_q^2/q$ 与 $B_q^2$ 的不对称来自(10)，不能凭张量交换自由改写。

## 6. 标准 Euler 因子与显式二次误差

在本文记号中，(8)在 $X=\sigma_{\mathfrak q}^{-1}$ 处准确为
$$
\boxed{\;
P_q=
1-\frac{A_qB_q}{q}x_q
+\left(\frac{A_q^2+B_q^2}{q}-2\right)x_q^2
-\frac{A_qB_q}{q}x_q^3+x_q^4 .
\;}
\tag{21}
$$
例如 g、h 的两个根各乘积为 q；把四个乘积根除以 q，再乘 $x_q$，
即得到(21)。这同时核定了 $W^\vee(1)$ 和 Frobenius 逆的方向。

定义单位 monomial
$$
m_q=q^{-1}x_q^2,\qquad F_q=m_qQ_q .
$$
利用 $y_q=(qx_q)^{-1}$，直接展开(19)，得到一个比“模 q−1 相同”更精确的恒等式：
$$
\boxed{\;
P_q-F_q=
\frac{q-1}{q^2}
\left((q+1)-A_qB_qx_q+(A_q^2-q-1)x_q^2\right).
\;}
\tag{22}
$$
右边最高次数只有2。(22)保留原第二、三槽的不对称；
没有把原始范数式误认成已经标准化的 Euler 多项式。

## 7. 原环类 p 扩张的直积与相容 Frobenius 提升

因为 $h_K=1$、$O_K^\times=\mu_6$，且 p>211，
平方自由分裂 n 的环类群的 p 部分准确为
$$
G_n=\operatorname{Gal}(K[n]/K)
\simeq \prod_{q\mid n}G_q,\qquad
|G_q|=h_q=p^{v_p(q-1)}.
\tag{23}
$$
证明来自环类群的标准局部单位正合列：
每个分裂 q 的
$(O_K/qO_K)^\times/(\mathbf Z/q\mathbf Z)^\times$
为循环 q−1 阶群；全局单位的像阶整除3，对 p 部分没有影响。
取 p-primary quotient 后各局部因子独立。
特别 $K[d]\cap K[e]=K[\gcd(d,e)]$，并有实际 compositum 公式。

对每个 q，一次选定在所有这些有限阿贝尔扩张上的相容 Frobenius 提升。
在含 q 的层，它只是一个所选 lift；不冒称该 ramified 层有未定义的 canonical Frobenius。
在不含 q 的层，它限制为原 Frobenius。
可先在不含 q 的全扩张选原 Frobenius，再由总群到该商的满射取一个 lift。
$\bar{\mathfrak q}$ 的 lift 取其逆，以保(17)。

以下所有群环系数均由这些固定 lift 求值。
因此 corestriction、restriction 与系数作用相容。
若 $h_q=1$，则 $K[q]=K$；下面公式仍逐字有效。

## 8. 不改变 n=1 的整修正

先置
$$
b_n=\left(\prod_{q\mid n}m_q\right)\widetilde c_n .
\tag{24}
$$
由(20)和相容 lifts，
$$
\operatorname{cor}_{K[nq]/K[n]}b_{nq}=F_qb_n.
\tag{25}
$$
根据(22)，
$$
D_q=\frac{P_q-F_q}{h_q}
=\frac{q-1}{h_qq^2}
\left((q+1)-A_qB_qx_q+(A_q^2-q-1)x_q^2\right)
\tag{26}
$$
是整群环元素；$(q-1)/h_q\in\mathbf Z_p^\times$。
这并不是对未知的群环元素任意除 $h_q$，其整性已经由显示式付清。

定义
$$
\boxed{\;
c_n=
\sum_{d\mid n}
 \left(\prod_{q\mid n/d}D_q\right)
 \operatorname{res}_{K[n]/K[d]}b_d .
\;}
\tag{27}
$$
系数乘积在目标层 $G_n$ 求值。
由于(23)，对一个新增 q，把(27)中 $d$ 和 $dq$ 两项配对，
Mackey 公式精确给
$$
\begin{aligned}
\operatorname{cor}_{K[nq]/K[n]}
 \operatorname{res}_{K[nq]/K[dq]}b_{dq}
 &=\operatorname{res}_{K[n]/K[d]}
   \operatorname{cor}_{K[dq]/K[d]}b_{dq},\\
\operatorname{cor}_{K[nq]/K[n]}
 \operatorname{res}_{K[nq]/K[d]}b_d
 &=h_q\,\operatorname{res}_{K[n]/K[d]}b_d .
\end{aligned}
\tag{28}
$$
各对的贡献是
$$
(F_q+h_qD_q)
 \left(\prod_{v\mid n/d}D_v\right)
 \operatorname{res}_{K[n]/K[d]}b_d
=P_q
 \left(\prod_{v\mid n/d}D_v\right)
 \operatorname{res}_{K[n]/K[d]}b_d .
$$
求和即为(7)的标准范数关系。

在 n=1，两个空乘积均为1、只有 d=1 一项，因此
$$
\boxed{\qquad c_1=b_1=\widetilde c_1=z^{\rm end}_p.\qquad}
\tag{29}
$$
没有乘一个未知的 Frobenius 多项式，也没有除增广参数。
这给本题所需的 Rubin 式修正的完整特例证明；无需把“存在一套标准系统”反推其首层保持原类。

## 9. 全部层的分母统一有界

原有限几何 Gysin、restriction、corestriction、退化映射及 Γ₀ 层的图形推前均为整操作。
ACR Theorem4.6的分母来源是 $(l-2)!(m-2)!$；
此处 l=m=2，等于1。

剩余可能的固定分母只来自：

- 开始时选定的原 tame Hecke/CM 对应与固定稳定格；
- (12)的一次 $X_1/X_0$、oldcopy 返回；
- CM 同构在 n=1 与原 Tate 模对应的一次常数校准。

这些对应不随 n 改变。
ACR Theorem3.3与Corollary3.6给同一个整 norm-compatible CM 商系统；
它不是逐层任意选择的有理同构。
(11)的平滑分母 −216 是 p 单位。
有限 η 幂等元的阶整除18，同样为 p 单位。

最后，(24)只乘整群环单位，(26)为整群环元素，
(27)只有限求和与 restriction。
所以若所有原始 $\widetilde c_n$ 落在固定 $p^{-c_p}T$，
最终所有 $c_n$ 仍落在同一个格。
辅助素数个数、其 $v_p(q-1)$、n的大小均不增加分母界。

## 10. 无挠、几何局部条件和本篇未作的应用

R885(8)给 W 在17惯性的四个指数：
$$
(5,1,15,9),\quad(17,7,15,9),\quad(11,13,9,15).
\tag{30}
$$
ψ₀在17不分歧，η在17的像是 μ₁₈。
这些指数均非0 mod18，p>211，故一个原惯性生成元的 $g-1$
在 T 上可逆。所有 $K[n]/K$ 在17不分歧，因而
$$
H^0(K[n],W/T)=0,\qquad H^1(K[n],T)\ \text{无 O-torsion}.
\tag{31}
$$
这逐项支付 ACR Theorem4.6列出的无挠条件，而不是借后续“大像”定理。

原始类来自实际几何 AJ，故在 p 位为几何/Bloch–Kato finite 类；
有限 tame restriction、corestriction 与整群环组合保留这一条件。
全部非 p 位（包括新增 $q\mid n$）的真正 Greenberg 条件还可直接付清。
ACR Proposition4.9 的证明在本权(2,2,2)同样适用：其几何 Frobenius规范下 W 纯重 $-1$，
且 W 共轭自对偶，因而未分歧 $H^1$、$H^0$ 与 Tate-dual 的 $H^0$ 都为零；
局部 Euler 特征与 Tate 对偶给
$H^1(K[n]_v,W)=0$。
故每个整局部像自动位于从这个有理零子空间传播的 Greenberg 条件中。
这包括有限整局部挠类，未把它们擅自设零。
在 p 位，原同源几何类的 finite 条件等于 balanced 条件；
(24)、(27)的群环作用及 restriction/corestriction保留它。
因此(6)的全部 c_n 实际属于
$\operatorname{Sel}_{\rm bal}(K[n],p^{-c_p}T)$。
投到最高原 $\lambda$ 时，仍是同一 $\mathfrak p$ 全、$\bar{\mathfrak p}$ 零的局部条件。

投到最高 CM 一维 $V_\ell$ 后，(7)仍以完整四次 $P_q$ 作用。
若只在某个 Chebotarev 子集上证明另外三因子为群环单位，
那是后续的实际归一问题；本篇没有把“该子集足够用于某个 Euler-system 定理”作为结论。
这里确已构造全部良好分裂 q 的四维系统，并准确保留其原首层。

R885 已独立给同一首层的有界 wild 提升，带其显示的单位 $\mathscr E_p$。
本篇不声称(27)的各 tame 层已经与那一条 DR wild 提升相容；
若要同时使用两个方向的同一完整系统，仍需付清该同源比较。
另一方面，有限 tame 系统(7)、(29)本身不以该比较为前提。

## 11. 原文与已付接口

- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*,
  J. Inst. Math. Jussieu, doi:10.1017/S1474748023000221：
  [正式刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)。
  本篇逐式使用刊本 p12–13 的 Theorem3.3、Corollary3.6，
  p14–16 的 Definition4.1、Lemma4.2、Definition4.3、Lemma4.4及任意固定 test-vector 映射，
  p17–19 的 Proposition4.5(i)、Theorem4.6。
  (22)、(27)–(29)是本文针对原平凡 nebentypus权2及 K=Q(ω)的自含整修正。
- R831：共同目标、原 q/q⁴ 退化映射、6/12 与 X₀/X₁ 全次数。
- R832：原四维的实际 Chow–CM 分解和最高 λ 投影；不拿任意同表示循环替代端点。
- R885：原四角色、无挠、固定 θ₅/C₅及已单独支付的 n=1 wild 提升。
- Darmon–Rotger, *p-adic families of diagonal cycles*, Astérisque434 (2022),29–75：
  [作者正文](https://arxiv.org/pdf/2207.01314)。
  本篇只用其固定辅助对应规范与 R885 已核的首层解释，
  不在本篇假定两套 Λ-adic 同名类相同。

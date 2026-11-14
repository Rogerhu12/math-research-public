# R261：实际三除法域的 CM 二择一与同一整数迹的模九约束

日期：2026-11-13。

**状态：已证明。** 保留 R258 的 $K=\mathbb Q(\sqrt{-3})$、$\sigma=1$ 及整 $j$ 假设。将实际曲线和其真实六次 CM 参考同时二次扭曲为

$$E_0[p]\simeq A_{d_0}[p],\qquad A_{d_0}:y^2=x^3+d_0,$$

其中 $d_0>0$ 立方自由。本文证明，对每个 $\delta>0$，以下至少一个成立：

$$\boxed{
\begin{aligned}
&\mathcal L_3(E_0)=\mathcal L_3(A_{d_0});\\
\text{或}\quad &c\gg_\delta p^{1/3-\delta}.
\end{aligned}}
\tag{261.1}
$$

常数绝对且有效。第一个分支还准确强迫

$$\boxed{j(E)\in4d_0\,\mathbb Q^3\ \cup\ 2d_0^2\,\mathbb Q^3.} \tag{261.2}$$

这里 $\mathcal L_3$ 指实际模三表示经 $\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3$ 的商域，不是完整三挠点域。证明使用同一个整数 Frobenius 迹的模 $p$、模 $3$ 和模 $9$ 信息。三条乘积角色在每个温和分歧素理想处恰有一条不分歧，这使导子乘积只有 $(pc)^4$，而不是错误的 $(pc)^6$。

同域分支没有在本文被排除；(261.2) 是准确的进一步约束，不能当作有理三同源或整个三挠点表示相同。

## 1. 实际对象

设 $p>37$、实际模 $p$ 像为完整非分裂正规化子、$\rho_{E,p}(I_p)=C^3$，商域为

$$H=\mathbb Q(\zeta_3),$$

并有 R258 的 $\sigma=(\lambda/\psi)^6=1$。假定 $j(E)\in\mathbb Z$。使用 R258 的同一个全局二次扭曲，记

$$A=A_{d_0},\qquad E_0[p]\simeq A[p],\qquad
N(E_0)=N(A)=\kappa p^2c^2,\quad
\kappa\in\{3,9,12,36,192,576\}.
\tag{261.3}
$$

特别，当 $q\nmid6pc$ 时两曲线均有好约化。令 $\Delta_E,\Delta_A$ 为任意有理模型的判别式；变化模型或二次扭曲不改变其立方类。对 $A$ 可用短模型

$$\Delta_A=-432d_0^2.$$

R96 给同一实际商域

$$\mathcal L_3(E_0)=H(\sqrt[3]{\Delta_E}),\qquad
\mathcal L_3(A)=H(\sqrt[3]{\Delta_A}).
\tag{261.4}
$$

两者在 $H$ 上均为非平凡循环三次扩张，因为判别式在 $p$ 的赋值不被三整除。取对应非平凡 Hecke 角色

$$\alpha=\eta_{\Delta_E},\qquad \beta=\eta_{\Delta_A}.$$

每个角色可以选其逆。它们切出的域相同，当且仅当

$$\beta\in\{\alpha,\alpha^2\}. \tag{261.5}$$

若域不同，则 $\alpha,\beta$ 生成一个秩二的 $\mathbb F_3$ 角色群。下文先处理这一情形。

## 2. 一般的三角色 Euler 检测

**引理 261.1。** 固定虚二次域 $H$，令 $\alpha,\beta$ 为线性独立的三次 Hecke 角色。写

$$C_\chi=|D_H|N\mathfrak f_\chi,$$

并设

$$Q\ge\max\left(3,C_\alpha^2,
\prod_{j=0}^2C_{\beta\alpha^j}\right). \tag{261.6}$$

令 $\mathcal B$ 包含 $\alpha,\beta$ 的全部分歧素理想，并满足固定 $A_0>0$ 下的

$$\prod_{\mathfrak q\in\mathcal B}N\mathfrak q\le Q^{A_0}.$$

则对任意 $\epsilon>0$，存在 $\mathfrak q\notin\mathcal B$，使

$$\boxed{\alpha(\mathfrak q)=1,\quad
\beta(\mathfrak q)\ne1,\quad
N\mathfrak q\ll_{H,A_0,\epsilon}Q^{3/8+\epsilon}.}
\tag{261.7}$$

常数有效。

**证明。** 删除 $\mathcal B$ 的全部 Euler 因子，考虑

$$
F_+(s)=\zeta_H^{\mathcal B}(s)
L^{\mathcal B}(s,\alpha)L^{\mathcal B}(s,\alpha^2),
$$

$$
F_-(s)=\prod_{j=0}^2L^{\mathcal B}(s,\beta\alpha^j).
\tag{261.8}
$$

在 $\mathfrak q\notin\mathcal B$ 处，令 $x=(N\mathfrak q)^{-s}$。
若 $\alpha(\mathfrak q)\ne1$，则

$$\{1,\alpha(\mathfrak q),\alpha(\mathfrak q)^2\}
=\{\beta(\mathfrak q),\beta(\mathfrak q)\alpha(\mathfrak q),
\beta(\mathfrak q)\alpha(\mathfrak q)^2\}=\mu_3,$$

所以两侧完整局部因子都等于 $(1-x^3)^{-1}$。
若 $\beta(\mathfrak q)=1$，两侧也显然相同。
因此，如果 (261.7) 的角色值组合在范数 $X$ 以内不存在，两侧范数至多 $X$ 的全部理想系数完全相同。

使用 R251 的紧支撑权 $w(t)=(1-t)^8$（$0\le t\le1$），Mellin 变换为

$$\widehat w(s)=\frac{8!}{s(s+1)\cdots(s+8)},\qquad
\widehat w(1)=\frac19.$$

线性独立性保证 $\beta,\beta\alpha,\beta\alpha^2$ 全部非平凡，所以 $F_-$ 整；$F_+$ 在一有一个简单极点。Yang 的固定域 GL(1) Burgess 界给每条竖线因子

$$|L(1/2+it,\chi)|\ll_{H,u}
C_\chi^{3/16+u}(1+|t|)^{3/8+2u}.$$

利用 (261.6)，对 $F_-$ 的三个因子相乘后误差导子项至多 $Q^{3/16+u}$。对 $F_+$ 的两个非平凡因子使用 $C_\alpha^2\le Q$，其余固定 zeta 因子只增加 $t$ 的固定幂。

每个删去的 Euler 多项式在 $\Re s\ge1/2$ 上绝对值为 $O_{H,A_0,u}(Q^u)$，证明与 R251 §4.2 完全相同：大范数处用 $1+n^{-1/2}\le n^{u/A_0}$，小范数只给固定有限积。三个因子并不引入依赖于变化坏集合的新常数。

因此 Mellin 移线给

$$S_-(X)=O_{H,A_0,u}(Q^{3/16+u}X^{1/2}),$$

$$S_+(X)=\frac{\mathcal R X}{9}
+O_{H,A_0,u}(Q^{3/16+u}X^{1/2}). \tag{261.9}
$$

准确留数为

$$
\mathcal R=
\operatorname{Res}_{s=1}\zeta_H(s)\,|L(1,\alpha)|^2
\prod_{\mathfrak q\in\mathcal B}
\left(1-\frac1{N\mathfrak q}\right)
\left(1-\frac{\alpha(\mathfrak q)}{N\mathfrak q}\right)
\left(1-\frac{\alpha^2(\mathfrak q)}{N\mathfrak q}\right).
\tag{261.10}
$$

分歧处置角色值为零。该留数为正。
R251 引理 251.2 的证明对非实三次角色原样成立：将切出的循环六次扩张换成循环三次扩张，Thorner–Zaman 的无零区仍排除其例外实零点；同一 Borel–Carathéodory 论证给有效的

$$|L(1,\alpha)|\gg_{H,u}C_\alpha^{-u}.$$

留数中的有限乘积至少是 $\prod_{\mathfrak q\in\mathcal B}(1-(N\mathfrak q)^{-1})^3$，故

$$\mathcal R\gg_{H,A_0,u}Q^{-u}.$$

若目标素理想在 $X$ 以内不存在，紧支撑保证 $S_+(X)=S_-(X)$，遂由 (261.9) 得 $X\ll Q^{3/8+4u}$。取足够小的 $u$ 即证明 (261.7)。全过程只用固定 $H$ 的有效常数，不含实二次 $L(1)$ 的分母。证毕。

## 3. 实际温和分歧使导子乘积降低

令 $R=c/3^{v_3(c)}$。由 R96，$\alpha,\beta$ 在所有 $q\ne3$ 上方具有完全相同的分歧支撑：

$$q=p\quad\text{或}\quad q\mid R.$$

每个这样的位置均为温和三次角色，导子指数为一。
对任一 $\mathfrak q$ 在此支撑中，温和惯性的三次商循环，所以存在 $e\in\{1,2\}$ 使

$$\beta|_{I_{\mathfrak q}}=\alpha^e|_{I_{\mathfrak q}}.$$

于是 $\beta,\beta\alpha,\beta\alpha^2$ 中恰有一条在该位置不分歧，另两条导子指数为一。这里的 $e$ 可以随素理想变化，证明并不假设一个全局相位。对每个有理 $q$，其上方全部素理想范数的积为 $q^2$，故

$$\prod_{j=0}^2N\mathfrak f_{\beta\alpha^j}^{(3)}
=(pR)^4, \tag{261.11}$$

其中上标 $(3)$ 表示删除三处的因子。

在三处，每个三次局部角色都杀掉 $U_4=(U_2)^3$，所以导子指数至多四；这个 R251 §2.1 的单位群论证也适用于所有乘积角色。因此

$$C_\alpha^2\le3^{10}(pR)^4,\qquad
\prod_{j=0}^2C_{\beta\alpha^j}\le3^{15}(pR)^4.
\tag{261.12}
$$

取

$$Q=3^{15}(pc)^4,$$

并让 $\mathcal B$ 包含 $6pc$ 上方全部素理想，则

$$\prod_{\mathfrak q\in\mathcal B}N\mathfrak q
\le(6pc)^2\le Q.$$

引理 261.1 给 $\alpha(\mathfrak q)=1$、$\beta(\mathfrak q)\ne1$，并且重新命名任意小的 $\epsilon$ 后

$$N\mathfrak q\ll_\epsilon(pc)^{3/2+\epsilon}. \tag{261.13}$$

如果有理素数 $q$ 在 $H$ 中惰性，则它在每个实际 $S_3$ 商中的 Frobenius 是外侧二阶元；其平方，即 $H$ 上方素理想的 Frobenius，恒为一。因此 $\beta(\mathfrak q)\ne1$ 排除了剩余次数二的素理想。于是

$$N\mathfrak q=q,\qquad q\equiv1\pmod3,\qquad q\nmid6pc.
\tag{261.14}$$

这也是两曲线共同的好约化素数。

## 4. 同一个整数迹的模九障碍

**引理 261.2。** 设 $q\nmid6pc$、$q\equiv1\pmod3$，且

$$\alpha(\mathfrak q)=1,\qquad\beta(\mathfrak q)\ne1.$$

则

$$\boxed{q\ge p^2/16.} \tag{261.15}$$

**证明。** 令 $a_E,a_A$ 为两个好约化的整数迹。实际同余 (261.3) 给 $a_E\equiv a_A\pmod p$，而 Hasse 界给

$$|a_E-a_A|\le4\sqrt q.$$

若 $q<p^2/16$，则两个整数迹完全相等，记其共同值为 $a$。

因为 $q$ 在 $H$ 分裂，$A$ 的全部极大序 CM 端同态在 $\mathbb Q_q$ 定义，约化后也在 $\mathbb F_q$ 定义。Frobenius 与 $H$ 交换；$H$ 在特殊纤维端同态代数中的中心化子是 $H$，且 Frobenius 是代数整数。因此它是

$$\pi\in\mathcal O_H,\qquad \pi\bar\pi=q,\qquad
\pi+\bar\pi=a.$$

$T_3(A)$ 是 $\mathcal O_H\otimes\mathbb Z_3$ 上的秩一自由模：
后者是 DVR，而前者是其上秩一的无挠有限模。
故 $A[3]$ 上的 Frobenius 是在 $\mathcal O_H/3$ 上乘以 $\pi$。

环 $\mathcal O_H/3$ 的单位群阶为六；其与 $Q_8$ 的交恰为 $\{\pm1\}$。因此

$$\beta(\mathfrak q)\ne1
\quad\Longleftrightarrow\quad
\pi\not\equiv\pm1\pmod{3\mathcal O_H}.$$

令 $\varpi=\sqrt{-3}$，选 $s\in\{1,-1\}$ 使 $\pi\equiv s\pmod\varpi$。因为 $3\mathcal O_H=\varpi^2\mathcal O_H$，上式给

$$v_\varpi(\pi-s)=1.$$

其有理范数为

$$N_{H/\mathbb Q}(\pi-s)=q+1-sa,$$

并且 $H/\mathbb Q$ 在三的剩余次数为一，所以准确有

$$\boxed{v_3(q+1-sa)=1.} \tag{261.16}$$

另一方面，$\alpha(\mathfrak q)=1$ 表示 $E_0[3]$ 的 Frobenius 矩阵 $M$ 落在 $Q_8$ 中。
由 $\pi\equiv s\pmod\varpi$ 可得整数 $a\equiv2s\pmod3$；
$Q_8$ 的六个四阶元素迹为零，只有 $\pm I$ 分别具有迹 $\pm2$。
因此

$$M=sI.$$

于是 $E_0[3]$ 的全部九个几何点都在 Frobenius 端同态减 $s$ 的核中。
该端同态的次数为 $q+1-sa$，所以

$$9\mid q+1-sa,$$

与 (261.16) 矛盾。这里 $s=-1$ 的情形也已包括；它对应 Frobenius 加一，或者等价地对有限域上的二次扭曲计点。证毕。

仅使用迹模三无法证明这个引理：标量 $\pm I$ 与非平凡三阶 Jordan 元具有相同迹。准确的模九整除正是补上的信息。

## 5. 异域分支的有效下界

若两个实际商域不同，§2–§3 给出满足 (261.13)–(261.14) 的检测素数；§4 给其下界。因此

$$p^2/16\ll_\epsilon(pc)^{3/2+\epsilon},$$

从而

$$c\gg_\epsilon p^{2/(3/2+\epsilon)-1}.$$

令 $\epsilon$ 足够小，对每个 $\delta>0$ 得到

$$\boxed{c\gg_\delta p^{1/3-\delta}.} \tag{261.17}$$

所有解析估计始终在固定 $H$ 上，所有坏素数和乘积导子均已显式计入，所以常数绝对有效。这证明 (261.1)。

## 6. 同域分支的准确立方类与局部后果

若两个商域相同，Kummer 理论给

$$\Delta_E\in\Delta_AH^{\times3}
\quad\text{或}\quad
\Delta_E\in\Delta_A^2H^{\times3}.$$

有理数的立方类映入 $H$ 后仍然单射：若 $r\in\mathbb Q^\times$ 在 $H$ 中为立方，取范数给 $r^2\in\mathbb Q^{\times3}$，因 $(2,3)=1$ 得 $r\in\mathbb Q^{\times3}$。因此上述关系已经在 $\mathbb Q^\times/\mathbb Q^{\times3}$ 中成立。

又有

$$\Delta_A=-432d_0^2=(-6)^3\,(2d_0^2),$$

所以

$$\boxed{\Delta_E\in2d_0^2\,\mathbb Q^{\times3}
\ \cup\ 4d_0\,\mathbb Q^{\times3}.} \tag{261.18}$$

当 $j(E)\ne0$ 时，$j=c_4^3/\Delta_E$ 使其立方类为判别式立方类的逆；$(2d_0^2)(4d_0)=(2d_0)^3$，故得到 (261.2)。$j=0$ 则可在 (261.2) 中取零，亦符合陈述。

若记 $\operatorname{cf}_3(n)$ 为正整数的立方自由部分，则整性进一步把有理立方改成整数立方：

$$j(E)\in
\operatorname{cf}_3(4d_0)\,\mathbb Z^3
\ \cup\
\operatorname{cf}_3(2d_0^2)\,\mathbb Z^3.
\tag{261.19}$$

原因是乘子已经立方自由，其每个素因子的指数至多二；若有理立方根有任何分母，该处的总赋值为负。这是同一全局立方类的两个选择，不能逐个素数独立改变指数。

另有一个直接可用的三处后果。若 $v_3(c)=1$，R258 的准确表迫 $v_3(d_0)=0$，故 $3\mid v_3(\Delta_A)=3$。于是同域情形必有

$$3\mid v_3(\Delta_E). \tag{261.20}$$

因此

$$v_3(c)=1,\quad3\nmid v_3(\Delta_E)
\quad\Longrightarrow\quad c\gg_\delta p^{1/3-\delta}.
\tag{261.21}$$

这涵盖 R96 中 $c=6$、$v_3(\Delta_E)\equiv2\pmod3$ 的局部整基分支。固定 $c$ 后，(261.21) 给有效的 $p$ 上界；它不是对剩余有限素数的自动排除。判别式赋值模三在本题使用的全局二次扭曲下不变。

## 7. 尚未闭合的同域分支

(261.18)–(261.19) 不使 $j$ 或 $c$ 有界。整个模三表示仍可能不同：相同的是 $Q_8$ 商，不能据此声称 $E_0[3]\simeq A[3]$，更不能推出 $E_0$ 有有理三同源。

在 $c=6$ 的同域分支，(261.20) 只保留 R96 允许的 $v_3(\Delta_E)\equiv0\pmod3$ 情形；它没有产生矛盾。在一般变化支撑下，需要继续处理这一共同 Kummer 域与同一个模 $p$ 表示的共同实现，或者得到与 (261.17) 相反的导子/高度控制。

## 8. 依赖与来源

- [R258：六次 CM 扭曲标准形](../results/R258-sextic-cm-normal-form-and-exact-integral-j-level.md)：同一个真实 $A_{d_0}$、二次扭曲、全部导子相等、$b=1$ 及三处表。
- [R96](../results/R96-actual-cubic-discriminant-support-and-local-three-branches.md)：实际 $\operatorname{GL}_2(\mathbb F_3)/Q_8$ 商、全部非三处分歧与 $p$ 的非立方赋值。
- [R251](../results/R251-joint-euler-detector-and-uniform-integral-j-conductor-growth.md)：紧支撑 Mellin、全部坏 Euler 乘子、$U_4=(U_2)^3$、非实有限阶角色的有效 $L(1)$ 下界。本文重新证明三角色局部恒等式和每个温和位置的导子取消。
- Liyang Yang，*Relative trace formula and twisted L-functions: the Burgess bound*，Compositio Mathematica **162** (2026), 2591–2641，Corollary 1.2 (1.3)，[DOI](https://doi.org/10.1017/S0010437X26103327)、[作者稿](https://arxiv.org/abs/2305.10719)。所用固定域 Eisenstein 特化有效性见 R229 §2。
- Jesse Thorner、Asif Zaman，*A unified and improved Chebotarev density theorem*，Algebra & Number Theory **13** (2019), 1039–1068，Theorem 3.1，[出版者全文](https://msp.org/ant/2019/13-5/ant-v13-n5-p02-p.pdf)。本文对非实三次角色使用同一个有效无零区，不引入实角色的 Siegel 常数。

本文为纯证明稿，无脚本或计算数据依赖。

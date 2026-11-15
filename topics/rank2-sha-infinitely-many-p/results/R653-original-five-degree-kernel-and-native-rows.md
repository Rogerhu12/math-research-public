# R653 — 原两个冻结门的完整 S5 分离、真实三标量行与全部 W 失败支

日期：2026-11-15。**状态：已证明。**

本篇把 R645/R650 的四个实际中央系数在原两个 sigma 的
$Q_5/L_5$ 框架中完整分离。所得五项是整个标准 odd
$\mathcal S_5\boxtimes\mathcal S_5$ 身份，包含全部角型。
因此四个系数准确回到三个固定的 degree 五标量行和显示的
五输入积分；负一行仍是原 $\sigma_{17}^5$ 的负一单位矩，
没有用正五矩代替它。

这个分离只在原冻结门上直接张量化。
R650 的两个 W 失败支移动 $Q_5$，故在它们上须保留全部五项
及真实角型测试转置。文末还给同一 R594 未加帽多项式的准确
零基准，明确实际四行完全来自真实 carry/单位差，
而不能把这些差逐支删除。

## 1. 同一五变量系数与原 Q5/L5 joint

保持 R645/R650 的全部规范、ray、固定坏集及 $N\ge1$，
特别
$$
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2,\quad\Omega=\Omega_p,\quad
\chi=\chi_{65}\in\{1,-1\}.
\tag{1}
$$
原四个第一输入上的测度记为
$$
\nu_4=-\frac1{84}\mathcal P_{6,C}
  (\nu_\sigma^{\otimes4})(\xi_1,\xi_2,\xi_3,x).
$$
于是同一个完整六输入来源是
$$
\boxed{\mu_0=\nu_4\otimes(Q,L)_*(\nu_\sigma(c)\otimes\nu_\sigma(d)),
\qquad Q=c+2d,\quad L=2c-d.}
\tag{2}
$$
$C$ 平均只作用原前四输入，未碰 $c,d$。
这个框架行列式为 $-5$，是普通单位；
其生成函数的最后两变量准确为
$$
\mathcal F(q,l)=\sigma(q+2l)\sigma(2q-l).
\tag{3}
$$
两轴范数均为五，交叉 Gaussian 为零，各有一个 odd 系数，
故 (3) 在完整标准 odd $\mathcal S_5\boxtimes\mathcal S_5$，
没有新增 flat twist、覆盖倍数或周期归一。

沿用 R650 的
$$
a=-(5+6\omega)/29,\quad b_F=(5+6\omega)/5,\quad g=3-2\omega,
$$
$$
F_0=F-aA-b_FQ,\quad F_1=F-b_FQ,\quad
G_0=G-gaA-gb_FQ,\quad G_1=G-gb_FQ .
$$
它们全部与 $Q$ 正交；更直接地，在原坐标中
$$
F_1=D_4+C-\frac{3\omega}{5}L,\qquad
F_0=D_4+C-aA-\frac{3\omega}{5}L,\qquad
G_i=13H_1+gF_i,
\tag{4}
$$
其中 $D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3$，
$H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x$。

记
$$
D_i=F_i-C,\quad E_i=F_i+13C,\quad
\mathcal G_i=\{C\ {\rm unit},D_i\in p^N\},
$$
$$
X_i=(D_i/\kappa^N,E_i,G_i),\qquad
p_i=\frac{\widehat P_p(X_i)}{b\Omega^6},\qquad
e_i=\frac{(\kappa^{-N}\partial_D+\partial_E+g\partial_G)
                 \widehat P_p(X_i)}{b\Omega^6}.
\tag{5}
$$
$\widehat P_p$ 仍包括 R594 的全部实际 $\lambda,\kappa$ 与整右逆。
$A,C,F_i,G_i,\mathcal G_i,p_i,e_i$ 都独立于 $Q$，
但依赖原其余五输入，特别一般依赖 $L$。
R650 的 $p_i^{[1]}$ 正是 $b_FQe_i$。

## 2. 全部五项 theta 身份

取标准 odd degree 五的完整基
$$
\begin{aligned}
D_5&=-xy\sigma^5,& \operatorname{type}D_5&=0,&D_5(0)&=1,\\
Z_5&=x^2\sigma^5,& \operatorname{type}Z_5&=1,&Z_5(z)&=z+O(z^7),\\
F_{12}&=-2y\sigma^5=\sigma(z)\sigma(2z),
 &\operatorname{type}F_{12}&=2,&F_{12}(z)&=2z^2+O(z^8),\\
X_5&=x\sigma^5,&\operatorname{type}X_5&=3,&X_5(z)&=z^3+O(z^9),\\
\Sigma_5&=\sigma^5,&\operatorname{type}\Sigma_5&=5,
 &\Sigma_5(z)&=z^5+O(z^{11}).
\end{aligned}
\tag{6}
$$
这里的 $\Sigma_5$ 不指 R533 的 $\Sigma=\sigma^2$。

**完整身份为**
$$
\boxed{
\begin{aligned}
\mathcal F(q,l)={}&F_{12}(q)D_5(l)-D_5(q)F_{12}(l)
     +3Z_5(q)Z_5(l)\\
 &+6b\{X_5(q)\Sigma_5(l)+\Sigma_5(q)X_5(l)\}.
\end{aligned}}
\tag{7}
$$

证明不依赖采样。空间 $\mathcal S_5$ 的五个角型在 (6) 中各一维。
(3) 在同时 $\mu_6$ 作用下型为二，因此允许的型对只有
$(2,0),(0,2),(1,1),(3,5),(5,3)$。
令 $l=0$、$q=0$ 给前两系数 $1,-1$；
原二次项
$(q+2l)(2q-l)=2q^2+3ql-2l^2$ 给第三系数三。
最后用原规范
$$
\sigma(z)=z+\frac b{210}z^7+O(z^{13}).
$$
其八次项中 $q^3l^5$ 和 $q^5l^3$ 的整数系数都是 $1260$，
故另两系数均为 $6b$。前面三型在这两单项式没有贡献。
五个角型已穷尽完整张量格，所以这支付全函数身份。
原 Amice 唯一性把 (7) 传成同一物理 $Q,L$ 的完整测度式。

特别
$$
\boxed{
(\mathrm{forget}\ Q)_*(Q,L)_*\nu_\sigma^{\otimes2}
=-\nu_{F_{12}}(L),\qquad
(\mathrm{forget}\ Q)_*(Q\,d\nu_{\rm pair})
=3\Omega\,\nu_{Z_5}(L).
}
\tag{8}
$$
第二式是完整总一阶矩，不是单位矩；
因此其系数是 $3\Omega$，没有额外 Euler 因子。

## 3. 三条真实标量行及其准确范围

在同一未缩放物理变量 $Q$ 上定义
$$
\boxed{
\ell_D=\int_{\mathbf Z_p^\times}\log\langle Q\rangle\,d\nu_{D_5},\quad
I_{\Sigma,-1}=\int_{\mathbf Z_p^\times}Q^{-1}\,d\nu_{\Sigma_5},\quad
\ell_{Z,1}=\int_{\mathbf Z_p^\times}Q\log\langle Q\rangle\,d\nu_{Z_5}.
}
\tag{9}
$$
第二条就是原 $\sigma_{17}(z)^5$ 的负一单位矩。
$\Omega_{p,0}=17^{1/6}\Omega_p$ 的原比较保持不变；
没有改成双覆盖来源，也没有将其重认成 R540 的
$f_1=-xy\sigma^6$ 负五矩。

当前 whole odd5 核是 $\chi I$，故三条来源各有实际核心
$\chi\lambda$。由 (6) 的整个总矩可得
$$
\boxed{
\nu_{D_5}(\mathbf Z_p^\times)=1-\chi\lambda,\qquad
\int_{\mathbf Z_p^\times}Q\,d\nu_{Z_5}
=\Omega(1-\chi\lambda\kappa).
}
\tag{10}
$$
两者为单位；第一条使用原偶迹/Hasse 的 $1\pm\lambda$ 单位界。
同样
$$
\int_{\mathbf Z_p^\times}Q^5\,d\nu_{\Sigma_5}
=120\Omega^5(1-\chi\lambda\kappa^5)
$$
为单位，但这不是 (9) 的负一矩。本文没有给
$I_{\Sigma,-1}$ 非零或零，也没有由一个角型单重识别新曲线。

因为 principal 单位权对 $\mu_6$ 不变，(7) 的第一 $Q$
角型在测试 $1_{\rm unit}\log\langle Q\rangle$ 下只保 $D_5$；
在 $1_{\rm unit}Q^{-1}$ 下只保 $\Sigma_5$；
在 $1_{\rm unit}Q\log\langle Q\rangle$ 下只保 $Z_5$。
这些消去使用的是 (5) 对 $Q$ 的完整独立性。

## 4. 原四个 K 系数的完整五输入表达

以下每个积分都在原五变量 $(\xi_1,\xi_2,\xi_3,x,L)$ 上，
各自显示的 $\mathcal G_i$、$A$ 单位条件全部保持。定义
$$
\begin{aligned}
M_0&=\int_{\mathcal G_0}p_0\,d(\nu_4\otimes\nu_{F_{12}}),\\
H_-&=\int_{\mathcal G_0}Ap_0\,d(\nu_4\otimes\nu_{X_5}),\\
H_+&=\int_{\mathcal G_0}e_0\,d(\nu_4\otimes\nu_{Z_5}),\\
A_0&=\int_{\mathcal G_1,A\ {\rm unit}}
            p_1\log\langle A\rangle\,d(\nu_4\otimes\nu_{F_{12}}),\\
A_1&=\int_{\mathcal G_1,A\ {\rm unit}}
 [p_1/A+b_Fe_1\log\langle A\rangle]\,d(\nu_4\otimes\nu_{Z_5}).
\end{aligned}
\tag{11}
$$
这些是实际积分，不是将伴随换成其质量的符号。
由 (7)–(9)，R645/R650 的整个向量准确为
$$
\boxed{
\begin{aligned}
K_{Y,0}&=-M_0\ell_D,\\
K_{Y,1}&=6b\,H_-I_{\Sigma,-1}+3b_FH_+\ell_{Z,1},\\
K_{A,0}&=-A_0,\\
K_{A,1}&=3\Omega A_1 .
\end{aligned}}
\tag{12}
$$
所有符号和 $-1/84$ 已包含在原 $\nu_4$ 中。

例如 $K_{A,1}$ 的两项都恰含一个 $Q$，而其余因子和门不含
$Q$，所以使用 (8) 的总一阶矩。$K_{Y,1}$ 第一项含
$Q^{-1}$，准确选 (7) 的 $\Sigma_5(Q)\otimes X_5(L)$；
第二项含 $Q\log\langle Q\rangle$，准确选
$3Z_5(Q)\otimes Z_5(L)$。
这同时解释了为何不能把两条未知标量或两个不同五输入系数合并。

## 5. 同一门内的真实非齐次参考环带

为记录质量而不遗漏尺度，定义原完整行
$$
\mathcal K_m=
\int_{\mathcal G_0,\ Q\in p^m\mathbf Z_p^\times}
       p_0\log\langle Q/p^m\rangle\,d\mu_0,\qquad m\ge0 .
\tag{13}
$$
整个 $\mathcal G_0,p_0$ 保持不变，仍不依赖 $Q$。
使用原 whole odd5 核及 (7)，得到
$$
\boxed{
\mathcal K_m=-(\chi\lambda)^m M_0
 \{\ell_D+m\log\langle\lambda^2\rangle(1-\chi\lambda)\}.}
\tag{14}
$$
这里 $\kappa/p=\lambda^2$，所以显示的 log 质量必须存在。
$K_{Y,0}=\mathcal K_0$，故
$$
\boxed{
(\chi\lambda)^{-m}\mathcal K_m-K_{Y,0}
=-m\,M_0(1-\chi\lambda)\log\langle\lambda^2\rangle .}
\tag{15}
$$
$\log\langle\lambda^2\rangle\ne0$：
否则代数数 $\lambda^2$ 在此普通处是根单位，继而其同一个
代数数为根单位，与 $N_{K/\mathbf Q}(\lambda^2)=p^{-2}$ 矛盾。
但 $M_0$ 本身尚未付非零；(15) 不把这一遗漏补成结论。
这条非齐次差在同一真实五输入权上成立，
没有把一个独立 rank-zero 参考换入原域。

若按 $Q/\kappa^m$ 归一，(14) 的 log 质量项消失。
这两种归一不能在 R645 的外部补偿中混用。
原完整 Mellin 中央导数还要乘 $d_p=p-1$，
与 R645(34)、R650(23) 的规范一致。

## 6. W 失败支必须使用整个五项式

R650 的实际 $P_z=P_{W,z}$，$z=\kappa^{2m}$，满足
$$
W=A+b_QQ+b_LL,\quad b_Q=(11+6\omega)/5,\quad b_L=(2+12\omega)/5,
$$
$$
D_i\circ P_z=D_i+(z-1)\gamma_iW,\qquad
\gamma_0=-(6+\omega)/60,\quad
\gamma_1=-(61+36\omega)/360 .
\tag{16}
$$
因此移动门有非零且当前为单位的 $Q$ 系数
$(z-1)\gamma_i b_Q$。它一般不在 $Q$ 的 $\mu_6$ 作用下不变。
原 $A/Q$ 单位 cut 和有理、log 观察也按 R650(8) 一起移动。

对这些支上的任意完整测试 $\Psi$，唯一可直接使用的是
$$
\boxed{
\begin{aligned}
\int\Psi\,d\mu_0={}&
 \int\Psi\,d(\nu_4\otimes\nu_{F_{12},Q}\otimes\nu_{D_5,L})
-\int\Psi\,d(\nu_4\otimes\nu_{D_5,Q}\otimes\nu_{F_{12},L})\\
&+3\int\Psi\,d(\nu_4\otimes\nu_{Z_5,Q}\otimes\nu_{Z_5,L})\\
&+6b\int\Psi\,d(\nu_4\otimes\nu_{X_5,Q}\otimes\nu_{\Sigma_5,L})
+6b\int\Psi\,d(\nu_4\otimes\nu_{\Sigma_5,Q}\otimes\nu_{X_5,L}).
\end{aligned}}
\tag{17}
$$
这里每一项保同一个 $\Psi$，包含 R650 两条失败支的整个指示。
不能在 (17) 中先删掉三个 odd $Q$ 项。

若希望逐个使用角型 $k$，真实测试转置准确是
$$
\Pi_k^{\rm test}\Psi
=\frac16\sum_{\zeta\in\mu_6}\zeta^{-k}
       \Psi(\xi_1,\xi_2,\xi_3,x,\zeta Q,L).
\tag{18}
$$
例如移动门逐支变成
$$
D_i+(z-1)\gamma_i(A+b_Q\zeta Q+b_LL)\in p^N .
\tag{19}
$$
R650 的所有其他观察同样换成其 $\zeta Q$ 支。
(18)–(19) 保含中心的真实测度角型；没有以“原 $T$ 为
principal”将一个不变性尚未成立的 $Q$ cut 删除。

## 7. 同一未加帽多项式的准确零基准

写 R594 原多项式为
$$
\widetilde Q_p(C,F,G)=-C^6/8+
 \sum_{1\le i\le5,\ 0\le j\le6-i}x_{ij,p}C^iF^jG^{6-i-j}.
$$
定义不同于实际 carry 权的无 cut 测试
$$
r_i=\widetilde Q_p(C,F_i,G_i)/(b\Omega^6).
\tag{20}
$$
这是使用同一个已付二十列的另一明确测试；
不是直接把 $\widehat P_p$ 中的 $u_j$、$\kappa^{-N}$ 和门删去后
假装积分不变。

R590 的完整分离为 $\mu_0=\nu_{B_C}\otimes\nu^\flat$，且
$$
m_{B_C}(0)=1,\quad m_{B_C}(1)=\cdots=m_{B_C}(5)=0,\quad
m_{B_C}(6)=-8b\Omega^6 .
$$
$A,Q,L,F_i,G_i$ 都与 $C$ 正交，所以对任意其余五输入测试
$\varphi$，准确有
$$
\boxed{\int r_i\varphi\,d\mu_0=\int\varphi\,d\mu_0.}
\tag{21}
$$
沿 $F_i,G_i$ 的实际共同方向微分时，
$-C^6/8$ 不变，其余每项仍含 $C^1,\ldots,C^5$，故
$$
\boxed{
\int
 \frac{b_FQ}{b\Omega^6}
 (\partial_F+g\partial_G)\widetilde Q_p(C,F_i,G_i)\,
 \varphi\,d\mu_0=0 .}
\tag{22}
$$

把 R645 的两条完整 $t$ 变化中的 carry 权改为 (20)，使用其
真正的一阶变化 (22)，得到四个无 cut 系数
$\overline{\mathbf K}$。它们全部严格为零：
$$
\boxed{\overline{\mathbf K}=0 .}
\tag{23}
$$
证明如下。$A$ log 的全行乘原最后两 sigma 的零质量；
$Q$ principal log 在忘 $L$ 后只见 type-two 的 $F_{12}(Q)$，
因此为零。$A/Q$ 行同样在 $Q^{-1}$ 测试下杀掉该 type-two 来源；
$Q/A$ 行用 $F_{12}$ 的总一阶矩零。余下一阶多项式项由 (22)
整条消去。所有理由均是完整来源身份，而非局部质量猜测。

于是实际 $\mathbf K$ 完全等于真实 carry/单位权与 (20)–(22)
的差所得积分。在 R650 的 W 两层式中可准确替换
$\mathbf f$ 为 $\mathbf f-\overline{\mathbf f}$。
但 $\overline{\mathbf f}$ 不带原 $\mathcal G_i$ 支撑：
门外的 $-\overline{\mathbf f}$ 是完整补项，必须保留。
(23) 不使它在每个 W 环带或每条失败支上单独为零。

## 8. 当前原算术关系中的准确位置

R645 的两个原 $S/T$ 总行保持不变，R650 的整个四行补偿仍成立。
本篇将它们里面的四个系数准确化成 (12)，给同一门中的
非齐次参考差 (15)，并把 W 失败支保成完整的 (17)–(19)。
若后续独立支付 $\Sigma_5$ 的全有限角色或负一值，
只能用于 (12) 中显示的那一项，不能同时删除
$\ell_D,\ell_{Z,1}$、$H_\pm$ 或任一 W 失败支。

尤其原 $M_0,A_0,A_1,H_-,H_+$ 仍是五输入带门积分；
原三个 degree 五标量行也没有被未经证明地赋值。
它们没有改变已经付清的原两曲线归一或全部补域。
整个中央非零及主目标尚未完成。

## 精确证书与依赖

- [精确脚本](../scripts/check-r653-original-five-degree-kernel-and-native-rows.js)
- [完整证书](../scripts/check-r653-original-five-degree-kernel-and-native-rows.json)
- [R645：两个真实门及四条原系数](R645-original-ya-intersection-and-carry-transpose.md)
- [R650：完整 W 两层补偿和实际 odd1755 门](R650-fixed-carry-gates-and-whole-odd1755.md)
- [R594：同一个二十列多项式及实际整右逆](R594-two-source-six-carry-compensation.md)
- [R590：完整 B_C 分离和六个矩](R590-original-six-carry-branches-and-sole-b-fibre.md)
- [R370：整个 odd5 joint 与绝对规范](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)
- [R513：当前 odd5/odd65 的同一标量](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)

证书核原 Q/L Gram、全部允许型对、两个真实八阶系数、
五条规范首项、原冻结行的 Q/C 独立性，以及 W 失败支中
不为零的 Q 系数。全函数、原测度、无限环带及所有 cut 的量词
由正文证明。

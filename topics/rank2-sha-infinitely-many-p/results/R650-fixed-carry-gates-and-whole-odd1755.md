# R650 — 两个固定 q 门的真实 W 补偿与原 A 门的 odd1755 返回

日期：2026-11-15。**状态：已证明。**

本篇继续 R645 的同一个 $\mu_0$、同一个 $q$ 及四个实际中央系数。
两个固定门在原 $W$ 操作下的位移均为已知单位乘 $W$，所以它们的
交叠与两条失败支可以准确列出。整个四行向量有一条保全源的
$W$ 两层补偿式；不能只把其中的多项式项或 log 质量置零。

另一个新增支付直接作用于 R645 的实际 $A$ 门：
其深轴 $D_1=F-C-b_FQ_5$ 在同一完整来源上有绝对标量
$\chi_{65}\lambda$。证明逐支保留六个 $C$ 旋转的 odd 半特征，
并用已付的原 odd65 锚确定 whole odd1755 的标量。
它将整个 $K_{A,0}$ 及 $K_{A,1}$ 返回到显示的两个单位条件，
仍保原多项式、原周期、真实 log 与全部其他输入。
没有新增辅助中央零，也没有把本篇边界积分当成原 $T$ 的裸中央。

## 1. 同一来源与两条固定门

沿用 R645 的全部对象、普通 ray 与坏集，记
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad b=17,\quad
\mu_0=\mathcal P_{6,C}\rho_0,\quad
Q=Q_5=c+2d,\quad L=2c-d .
\tag{1}
$$
原 $A,Y,W,C,F,G$ 的完整六行均为 R645(3)、(13)，不改变输入。
为清楚起见，置
$$
a=-\frac{5+6\omega}{29},\quad b_F=\frac{5+6\omega}{5},
\quad g=3-2\omega,
$$
$$
F_0=F-aA-b_FQ,\quad F_1=F-b_FQ,\qquad
G_0=G-gaA-gb_FQ,\quad G_1=G-gb_FQ ,
\tag{2}
$$
$$
D_i=F_i-C,\quad E_i=F_i+13C,\qquad
\mathcal G_i=\{C\ {\rm unit},D_i\in p^N\},\quad i=0,1 .
\tag{3}
$$
$N\ge1$ 是原固定 carry 深度。
R645 的 $K_{Y,\bullet}$ 使用 $\mathcal G_0$，
$K_{A,\bullet}$ 使用 $\mathcal G_1$。
在各门内 $F_i$ 自动为单位。

设
$$
X_i=(D_i/\kappa^N,E_i,G_i),\qquad
p_i=\widehat P_p(X_i)/(b\Omega^6),
$$
$$
p_i^{[1]}=\frac{b_FQ}{b\Omega^6}
(\kappa^{-N}\partial_D+\partial_E+g\partial_G)
                         \widehat P_p(X_i).
\tag{4}
$$
$\widehat P_p$ 仍是 R594 的整个九行整右逆。
四个实际行按有序列写成
$$
\mathbf f=
\begin{pmatrix}
\mathbf1_{\mathcal G_0,Q\ {\rm unit}}p_0\log\langle Q\rangle\\
\mathbf1_{\mathcal G_0,Q\ {\rm unit}}
 [p_0A/Q+p_0^{[1]}\log\langle Q\rangle]\\
\mathbf1_{\mathcal G_1,A\ {\rm unit}}p_1\log\langle A\rangle\\
\mathbf1_{\mathcal G_1,A\ {\rm unit}}
 [p_1Q/A+p_1^{[1]}\log\langle A\rangle]
\end{pmatrix}.
\tag{5}
$$
门外各函数按零延拓；它们是原紧整域上的连续有界函数。
允许的固定分母包括 $\kappa^{-N}$，没有令它等于一。
准确地
$$
\mathbf K:=\int\mathbf f\,d\mu_0
=(K_{Y,0},K_{Y,1},K_{A,0},K_{A,1})^t .
\tag{6}
$$

## 2. 原 W 的全部真实转置

对 $P_z=P_{W,z}$，原 $C,F,G$ 逐个固定，故 R645 的原 $q$
逐点固定。但是 (2) 的冻结行不固定。精确计算给
$$
\alpha=\frac{29}{72},\qquad q_W=\frac{5-6\omega}{72},
$$
$$
\boxed{
\gamma_0=-\frac{6+\omega}{60},\qquad
\gamma_1=-\frac{61+36\omega}{360}.}
\tag{7}
$$
完整变化为
$$
\boxed{
\begin{aligned}
A\circ P_z&=A+(z-1)\alpha W,&
Q\circ P_z&=Q+(z-1)q_WW,\\
D_i\circ P_z&=D_i+(z-1)\gamma_iW,&
E_i\circ P_z&=E_i+(z-1)\gamma_iW,\\
G_i\circ P_z&=G_i+(z-1)g\gamma_iW,&
C\circ P_z&=C .
\end{aligned}}
\tag{8}
$$
(8) 给 (5) 的每一个因子，包含 $p_i^{[1]}$ 前面的 $Q$、
两个有理分母，以及所有单位 cut；不能只运输 log。

这些位移系数都是当前单位。所需分子范数除已有小素数外
只出现 $31$，而 $p\equiv7\bmod64$ 排除 $p=31$。
尤其 $N(61+36\omega)=2821=7\cdot13\cdot31$。

取任一 $m\ge1$、$z=\kappa^{2m}$，令
$\mathcal G_i^{z}=P_z^{-1}\mathcal G_i$。
因为 $(z-1)\gamma_i$ 为单位，
$$
\boxed{
\mathcal G_i\cap\mathcal G_i^z
=\mathcal G_i\cap\{W\in p^N\}
=\mathcal G_i^z\cap\{W\in p^N\}.}
\tag{9}
$$
两条差支 $\mathcal G_i\setminus\mathcal G_i^z$、
$\mathcal G_i^z\setminus\mathcal G_i$ 都要求 $W\notin p^N$。
当 $N=1$ 时它们确实都在原 $W$ 单位域；
当 $N>1$ 时只可写成 $v_p(W)<N$，不能擅改成单位域。

在共同门 (9) 内，(8) 也保持 $A$ 和 $Q$ 各自的单位条件。
所以每对原单位指示在共同门准确相同；
在两条差支仍使用它们各自的真实指示。

## 3. 完整四行的 W 两层补偿

R638 的同源 $K_W^2=I$ 给
$$
\mu_0|_{W\in p^{2m}}=\lambda^{2m}(P_{\kappa^{2m}})_*\mu_0 .
\tag{10}
$$
(10) 对所有伴随测试成立，故对整个 (5) 同时得到
$$
\boxed{
(1-\lambda^{2m})\mathbf K
=\int_{W\notin p^{2m}}\mathbf f\,d\mu_0
+\lambda^{2m}\int(\mathbf f\circ P_{\kappa^{2m}}-\mathbf f)\,d\mu_0 .}
\tag{11}
$$
这里不把任何单行质量、log 行或单位补域分开赋零。

为写全第二项，令
$\mathbf f_i=\mathbf1_{\mathcal G_i}\mathbf u_i$ 为 (5) 中对应的
两行，$\mathbf u_i$ 包含其真实 $A/Q$ 单位指示。
对 $z=\kappa^{2m}$，准确有三支分解
$$
\boxed{
\begin{aligned}
\int(\mathbf f_i\circ P_z-\mathbf f_i)\,d\mu_0
={}&\int_{\mathcal G_i\cap\mathcal G_i^z}
       (\mathbf u_i\circ P_z-\mathbf u_i)\,d\mu_0\\
&+\int_{\mathcal G_i^z\setminus\mathcal G_i}
                              \mathbf u_i\circ P_z\,d\mu_0
-\int_{\mathcal G_i\setminus\mathcal G_i^z}
                              \mathbf u_i\,d\mu_0 .
\end{aligned}}
\tag{12}
$$
第一支中两个单位 cut 相同，但函数仍有完整差。
具体若 $v_i=(z-1)\gamma_iW$，多项式差准确是
$$
\sum_{r=1}^6\frac{v_i^r}{r!}
(\kappa^{-N}\partial_D+\partial_E+g\partial_G)^r
                      \widehat P_p(X_i).
\tag{13}
$$
每一项整，因为共同门中 $v_i\in p^N$。
相应 log 差分别是
$$
\log\left(1+\frac{(z-1)q_WW}{Q}\right),\qquad
\log\left(1+\frac{(z-1)\alpha W}{A}\right),
\tag{14}
$$
且 (5) 的有理项还保两个实际移动分母。
(13)、(14) 的乘积和交叉项都属于 (12)，不以一阶近似替代它。

可固定 $m=1$。已有 R410 的单位界给
$1-\lambda^2\in\mathcal O^\times$，于是 (11) 真正在原整系数域中
解出整个 $\mathbf K$；不需要新增射线。
但解出的右边仍是显示的一个低 $W$ 环带加两个门各自的三支。
“能够除以 $1-\lambda^2$”不使这些真实积分为零。

## 4. 实际 A 门的完整 odd1755 标量核心

现在直接处理 (3) 中的 $D_1$，而不新增无关辅助轴。
其整行是
$$
\boxed{
5D_1=(5,\ 5\omega^2,\ -10\omega,\ 0,\ -6\omega,\ 3\omega),\qquad
N(5D_1)=195 .}
\tag{15}
$$
并且
$$
D_1\perp Q,\qquad N(D_1)=39/5 .
$$
在原未平均来源上，(15) 有三个 odd 系数，故为标准 odd195
半特征。仍须支付全部六个 $C$ 旋转。

对原 $R_\zeta=I+(\zeta-1)\bar C^{\,t}C$，
$D_1R_\zeta=F_1-\zeta C$。每个
$$
15(F_1-\zeta C),\qquad \zeta\in\mu_6,
\tag{16}
$$
都是原六输入的整行，范数 $1755$。六个非零模二系数的数目
依次为 $3,5,5,3,5,5$，全为 odd。
完整行和每个模二系数均在证书中列出。
在固定全部正交伴随的生成变量上，交叉 Gaussian 恰为零，
所以这是真正 whole 标准 odd1755，而非只忘伴随后的一变量式。

现有 ray 已使 $g_\pi\equiv1\bmod27,5,13,2$，故
$$
g_\pi\equiv1\pmod{3510}=1\pmod{2\cdot1755}.
\tag{17}
$$
R370 的奇中心唯一化证明因而给整个 odd1755 核为一个实际标量。
用原非零固定拉回
$$
[3\delta]^*\mathcal S_{65}^{\rm odd}
                 \subset\mathcal S_{1755}^{\rm odd},\qquad
N(3\delta)=27,
\tag{18}
$$
与真实普通核心严格交换，结合 R504/R513 的
$K_{65}=\chi_{65}I$，绝对确定该标量恰为 $\chi_{65}$。
乘子范数 odd，保持原标准 odd 半特征。
没有从项目交织猜一个新符号。

$15$ 为普通单位，各支 (16) 都在同一个实际物理 $D_1$ 上
给相同核心。平均后得到整联合
$$
\boxed{
\mu_0|_{D_1\in p^r}
=(\chi_{65}\lambda)^r(P_{D_1,\kappa^r})_*\mu_0,\qquad r\ge0.}
\tag{19}
$$
所有其余五输出和实际隐藏 cut 保留。
本篇没有据 (19) 自动给 $\mu_W$ 或 $h_W$ 同一个单层标量；
(11) 使用的是独立已付的 W 两层式 (10)。

## 5. 原 K_A,0 的整条门返回

定义真实正交伴随
$$
\widehat E=F_1+\frac{34}{5}C,\qquad
A_\perp=A-\frac{5(1+6\omega)}{39}D_1,\qquad
G_\perp^{(1)}=G_1+\frac{31g}{39}D_1 .
\tag{20}
$$
它们都与 $D_1$ 正交；准确 Gram 为
$$
N(\widehat E)=1326/25,\qquad N(A_\perp)=976/39 .
$$
这里没有为这些范数另赋未经证明的单轴核心。

原变量的完整回代是
$$
\boxed{
C=\frac5{39}(\widehat E-D_1),\qquad
E_1=\frac{70\widehat E-31D_1}{39},\qquad
G_1=G_\perp^{(1)}-\frac{31g}{39}D_1,\qquad
A=A_\perp+\frac{5(1+6\omega)}{39}D_1 .}
\tag{21}
$$
因此在 $D_1\in p^N$ 内，
$C$ 单位等价于 $\widehat E$ 单位，
$A$ 单位等价于 $A_\perp$ 单位。
对 (6) 的整个第三行使用 (19)，严格得到
$$
\boxed{
\begin{aligned}
K_{A,0}
={}&\frac{(\chi_{65}\lambda)^N}{b\Omega^6}
 \int_{\{\widehat E,A_\perp\ {\rm unit}\}}
 \widehat P_p\left(
 D_1,\frac{70\widehat E-31\kappa^ND_1}{39},
 G_\perp^{(1)}-\frac{31g\kappa^ND_1}{39}
 \right)\\
&\hspace{27mm}\cdot
 \log\left\langle A_\perp+
       \frac{5(1+6\omega)\kappa^N}{39}D_1\right\rangle\,d\mu_0 .
\end{aligned}}
\tag{22}
$$
这仍是同一个原六变量来源；原其余变量都在同一六维联合中积分。
$Q$ 在 (19) 中固定。

$K_{A,1}$ 也有同一个完整返回：在 (5) 第四行按 (21)
把 $D_1$ 换成 $\kappa^ND_1$，保原 $Q$，并取消门
$D_1\in p^N$，其余两 cut 变为
$\widehat E,A_\perp$ 单位，整体乘 $(\chi_{65}\lambda)^N$。
尤其 $p_1^{[1]}$ 中的原
$\kappa^{-N}\partial_D+\partial_E+g\partial_G$ 保持原定义；
它不是对变换后权任意重取一个导数。

(22) 中 $\kappa^N D_1$ 出现在 $E$、$G$ 以及 log 中。
删掉其中任一项都会改变原 $K_{A,0}$。
把 log 换成一给对应的完整质量式；该质量没有零理由。
也不能把显示的 $\widehat E$ 单位条件取成一个伴随质量，
更不能把 (22) 认成新 $A_\perp$ 裸中央。

## 6. 与原算术补偿的准确联立

R645 对每个 $n\ge N$ 已付原真实外部部分
$\mathcal O_{Y,n}^{Y},\mathcal O_{A,n}^{Y}$ 的完整比较。
在原 $J'_S=J'_T=0$ 的反证条件下，
$$
-\frac{(\mathcal O_{j,n}^{Y})'(0)}
 {d_p\chi_{65}^n\lambda^{3n}}
 =K_{j,0}+\kappa^nK_{j,1}
     +p^{\,2(n-N)+1}\mathcal O,\qquad j=Y,A .
\tag{23}
$$
现在 (11)–(14) 给 (23) 右边四条系数的同源 W 两层补偿，
(19)–(22) 又把实际 $A$ 门的两条行按真实深轴完整返回。
这些式子可同时代入 (23)，所有全域及 log 质量保持一致。

尚未支付的是 (12) 两条失败支及共同门中的完整混合测试，
与原 $S/T$ 纯中央之间的进一步关系。
失败支即使在 $N=1$ 时位于 $W$ 单位域，测试仍含
$A/Q$ 单位、原 $D_i$ 门和 $A/Q$ 的 log，不能由
$J'_T=0$ 单独删除。另一方面，原 $q$ 的
$\pi_4$ 中性不能替代冻结后的 $p_i$，其准确差已在 R645(28)–(30)
和本篇 (8)、(12) 中完整显示。

所以本篇新增的是对实际未控补偿的一条确定 odd 核、
一条保全四行的 W 补偿和完整门运输，而不是另一个独立非零
见证。原全中央非零及主目标仍未完成。

## 精确证书与依赖

- [精确脚本](../scripts/check-r650-fixed-carry-gates-and-whole-odd1755.js)
- [完整六支及 Gram 证书](../scripts/check-r650-fixed-carry-gates-and-whole-odd1755.json)
- [R645：原 Y/A 交域及四个实际系数](R645-original-ya-intersection-and-carry-transpose.md)
- [R638：完整 W 三态与全部真实词](R638-original-yw-three-state-and-word-compensation.md)
- [R594：同一个原 q、完整九行右逆](R594-two-source-six-carry-compensation.md)
- [R370：odd Heisenberg 中心规范](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)
- [R504：原 odd65 的绝对标量](R504-original-two-axis65-core-and-complete-rectangles.md)
- [R513：同一 odd 标量的合法拉回比较](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)

证书只用自含 BigInt $\mathbf Q(\omega)$ 精确算术，核全六支整行、
odd 半特征、所有 Gram、原 W 位移及 (20)–(21) 的完整回代。
实际 trace 的绝对标量、整联合核心、全部深度与边界积分由正文支付。

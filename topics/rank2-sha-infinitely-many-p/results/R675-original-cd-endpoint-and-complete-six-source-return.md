# R675 — 原未切第二 Y 的 cd 端点：完整六系数及实际非 S 来源

**状态：已证明。** 本文固定 R594 的原 $\widehat P_p$，不另选十一维核中的测试。
在 R671 的 $j=N,n=N$ 端点，未附第二个 Y 条件的 cd 门与 R669 的共同 E 深门
是同一个真实集合。本文恢复它的整条 principal degree34 来源，给出保全部
$\lambda,\kappa,\kappa^N$ 的六系数公式，以及原右逆的完整模 p 表。

该来源一般不在原 S 线上。删去当前 ray 内相对密度零的一族素数后，
对所有 $N\in4\mathbf Z_{>0}$ 同时，其完整质量和 Y-unit 质量均为单位；
第二观察准确为第一观察的负号。这不证明其中央导数非零，
也不把原算术总行的外部或浅域赋零。

## 1. 真正的同域端点

保 R664、R668、R671 的全部原六输入、周期及物理行：
$$
Y_0=A+Q,\quad Y_1=A+L,\quad Q=c+2d,\quad L=2c-d,\quad
\mathcal E=5A-29(Q+L).
$$
$N$ 总是正的四倍数。因 $2,5,29,63$ 在当前 ray 为单位，
$$
\boxed{
\{c,d\in p^N,\ Y_i\in p^N\}
=\{A,Q,L\in p^N\}
=\Gamma_N\cap\{\mathcal E\in p^N\},\qquad i=0,1.
}
\tag{1}
$$
其中 $\Gamma_N=\{Y_0,Y_1\in p^N\}$。左边先给 Q、L 深，再给 A 深；
右边由 R664 的完整三轴反演，其行列式 126 是单位。

(1) 只用于 $n=N$。$n>N$ 时的单 Y cd 门并未要求另一 Y 深，
不可互换。R669 正式参数为
$$
u=\kappa^N,\qquad t=\kappa^{n-N}=1,
$$
不是旧的未归一 $\kappa^n$。

令 $\mathcal A^S_{i,N}$ 为 R671 的 $j=N$ 完整 cd 返回行，
即该篇付清所有实际 core 后剩下的 $Y_i$-unit Mellin 行。
用 R669 的固定实际观察 $M_{j,p}$，准确有
$$
\boxed{
\mathcal A^S_{i,N}(w)
=\epsilon_i\sum_{j=0}^5c_{j,p}(u)M_{j,p}(w),\qquad
\epsilon_i=(-1)^i,
}
\tag{2}
$$
$$
c_{j,p}(u)=C_{0,j,p}(u,1)=C_{1,j,p}(u,1).
\tag{3}
$$
从共同域到 (2) 的因子是 $\lambda^{-4N}$，没有新增周期。
(3) 也直接来自原整数旋转 $(c,d)\mapsto(d,-c)$：
它将 $Y_0,F_0$ 送到 $Y_1,F_1$，固定原四输入及下面全部伴随，
而 $\sigma(c)\sigma(d)$ 得到负号。因此未归一两来源整条相反；
这里保全部隐藏变量、门和 canonical phase，不只比较质量。

## 2. 完整 C 单位补项和实际 S34 来源

置
$$
g=3-2\omega,\quad D=D_*,\quad C^\perp=C+\frac{29}{143}D,\quad
E_\perp=14C^\perp,
$$
$$
G_{00}=G_\perp-
 \left(-\frac{263}{38}+\frac{263}{57}\omega\right)C^\perp,
\qquad H_i=F_i-C,\quad K_i=H_i-\frac{406}{143}D .
$$
R671 的 $M=N-j=0$ 已没有剩余 H 深条件；其确切权为
$$
\frac{1_{C^\perp\ {\rm unit}}}{b\Omega^6}
 \widehat P_p(H_i,E_\perp+uK_i,G_\perp+guK_i).
\tag{4}
$$
R665 的 whole $C^\perp$ 核为 $\eta\lambda$，$\eta^2=1$；
$H_i,K_i,D,Y_i$ 均与 $C^\perp$ 正交。所以完整来源正是
$$
\boxed{\begin{aligned}
\mathscr F_{i,p}(Z;u)=\frac1{b\Omega^6}\int e^{Y_iZ/\Omega}
\bigl\{&
\widehat P_p(H_i,E_\perp+uK_i,G_\perp+guK_i)\\
&-\eta\lambda\widehat P_p(H_i,\kappa E_\perp+uK_i,\,
G_{00}+\kappa(G_\perp-G_{00})+guK_i)
\bigr\}\,d\mu_0 .
\end{aligned}}
\tag{5}
$$
这完整保 C 深补域，没有把原第六矩换成四次质量近似。

微分方向与实际 $Y_i$ 正交，原完整 theta lift 及 R669 的线丛论证给
$$
\mathscr F_{i,p}\in\mathcal S_{34}^{(0)},\qquad
\mathscr F_{1,p}=-\mathscr F_{0,p}.
\tag{6}
$$
此空间恰以
$$
\Xi_j=\sigma^{34}x^{17-3j},\qquad 0\le j\le5
\tag{7}
$$
为基。先付 (6)，再用六个 jet 恢复已知六维空间；
没有从有限 jet 外推全函数身份。

## 3. 完整六系数的有限公式

以下公式无未定测度矩。写同一个原多项式为
$\widehat P_p=\sum_{a+b+c=6}p_{abc}D^aE^bG^c$。
这些系数始终由 R594 的固定整右逆
$$
x_p=B(\tau)(A_pB(\tau))^{-1}b_p,\qquad \tau=(1+\lambda)^{-1}
$$
及原 E 次数整逆确定；本文不改变其中任何一列或目标。

先用 $b=1$ 的正式级数计算一个固定有限表。
R590 的原五 flat 输入生成函数是
$$
\mathcal F_5(z_f,q_f,r,c,d)=
\frac{f_1(z_f)\Sigma(q_f)-f_3(z_f)\Theta(q_f)}{42}
 \sigma(r)\sigma(c)\sigma(d),
\tag{8}
$$
$$
f_1=-xy\sigma^6,\quad f_3=-y\sigma^6,\quad
\Sigma=\sigma^2,\quad\Theta=x\sigma^2.
$$
独立原 C 输入还给整因子
$$
B_C(s)=B(s/\delta),\quad B=-y\sigma^3,\qquad
B_C(s)=1-\frac{s^6}{90}+O(s^{12}).
\tag{9}
$$
即原第六矩为 $-8b\Omega^6$，以下完整保留。

下列三维行均在后面补两个零，得到五维行：
$$
\begin{aligned}
a&=(-1+\omega/2,\ 2+3\omega/2,\ 2+4\omega),\\
d&=((-19+19\omega)/174,\ (31-37\omega)/58,\ (-43-21\omega)/29),\\
e&=((-133+133\omega)/429,\ (217-259\omega)/143,\ (-602-294\omega)/143),\\
v&=((-5843-3715\omega)/858,\ (-1593-1599\omega)/286,\ (1324-266\omega)/143),\\
v_0&=((-247-143\omega)/36,\ (-65-91\omega)/12,\ (39-13\omega)/6).
\end{aligned}
\tag{10}
$$
实际观察和第一权方向是
$$
o_0=(a_1,a_2,a_3,1,2),\qquad o_1=(a_1,a_2,a_3,2,-1),
$$
$$
h_0=(\delta/6,1/2-\omega,-1-\omega,1,2+3\omega),\qquad
h_1=(\delta/6,1/2-\omega,-1-\omega,2+3\omega,-1),
\qquad k_i=h_i-\frac{406}{143}d.
\tag{11}
$$
$s,t,r_0$ 是三个独立微分变量，Z 是观察变量。置
$$
\begin{aligned}
\mathbf z_i^+&=o_iZ+h_i s+(e+uk_i)t+(v+guk_i)r_0,\\
\mathbf z_i^-&=o_iZ+h_i s+(\kappa e+uk_i)t+
 (v_0+\kappa(v-v_0)+guk_i)r_0 ,
\end{aligned}
\tag{12}
$$
$$
\begin{aligned}
\ell_+&=-s+\frac{1596+263u}{143}t+
 \frac{-789+526\omega+263gu}{143}r_0,\\
\ell_-&=-s+\frac{1596\kappa+263u}{143}t+
 \frac{(-789+526\omega)\kappa+263gu}{143}r_0 .
\end{aligned}
\tag{13}
$$
于是
$\mathcal G_i^\pm=(1-\ell_\pm^6/90)\mathcal F_5(\mathbf z_i^\pm)$
在伴随总次数不超过 6 时，是原完整生成函数的准确截断。
定义
$$
m_j=\sum_{a+b+c=6}p_{abc}a!b!c!\,
 [s^at^br_0^cZ^{6j}]
 (\mathcal G_0^+-\eta\lambda\mathcal G_0^-),
\qquad 0\le j\le5 .
\tag{14}
$$
(8)–(14) 是固定 $6\times28$ 的实际有限映射，最高原总次数 36。
它保全部 $u,\kappa$，不是以六个未定新常数代替系数。

原 $b=17$ 的六个 theta 系数完整为
$$
\boxed{\begin{aligned}
c_0={}&b^{-1}m_0,\\
c_1={}&\frac{34}{15}m_0+m_1,\\
c_2={}&b\left(\frac{4318}{2475}m_0+\frac{193}{105}m_1+m_2\right),\\
c_3={}&b^2\left(\frac{58492}{111375}m_0+
 \frac{1612561}{1576575}m_1+\frac{148}{105}m_2+m_3\right),\\
c_4={}&b^3\left(\frac{22301806}{422668125}m_0+
 \frac{1655663467}{9435801375}m_1+
 \frac{764131}{1576575}m_2+\frac{103}{105}m_3+m_4\right),\\
c_5={}&b^4\left(\frac{903658796}{919303171875}m_0+
 \frac{17663600217706}{3258606825849375}m_1+
 \frac{265417402}{9435801375}m_2+
 \frac{205276}{1576575}m_3+\frac{58}{105}m_4+m_5\right).
\end{aligned}}
\tag{15}
$$
全部参数和原右逆依赖均在 (12)–(14) 中，没有高次参数余项。

证明 (15)：写 $w=Z^6$、$x=Z^{-2}X(w)$、$\sigma=Zh(w)$。
原方程给
$$
X_0=1,\quad X_1=-1/7,\quad
X_n=\frac{\sum_{i=1}^{n-1}X_iX_{n-i}}{(6n+1)(n-1)}\quad(n\ge2),
\qquad
\log h=-\sum_{n\ge1}\frac{X_nw^n}{6n(6n-1)}.
$$
$\Xi_j=Z^{6j}h^{34}X^{17-3j}$ 的前六 jet 矩阵为单位三角。
其精确逆就是 (15)。恢复 b 后，(14) 的第 j 项乘 $b^j$，
原权另有 $1/b$，故各 b 次数如显示。
这些固定分母在当前好素数及原固定坏集外均为单位。

## 4. 原 S 线的精确判据

原 S 为
$$
S=\sigma^{34}x^2\frac{(X+b)(X-8b)(7X^2-4bX+16b^2)}7,\qquad X=x^3.
$$
所以其同一实际基向量是
$$
s=(0,1,-53b/7,-12b^2/7,-80b^3/7,-128b^4/7).
\tag{16}
$$
端点来源在 S 线上当且仅当以下五个表达式分别为零：
$$
\boxed{
c_0,\quad 7c_2+53bc_1,\quad 7c_3+12b^2c_1,\quad
7c_4+80b^3c_1,\quad 7c_5+128b^4c_1 .
}
\tag{17}
$$
下一节直接支付原固定测试的第一个表达式为单位的实际素数子族。

## 5. 原右逆的全部六行留数与非 S 判据

令 $P_{-1},P_0$ 为 R659 原数据中的完整 Pres、Pconst。
原右逆在 $\kappa=0$ 的准确表达为
$$
\overline{\widehat P}_L
=L^{-1}P_{-1}+P_0-
 \frac{P_{-1}^{[0]}+L P_0^{[0]}}{1+L},\qquad P^{[0]}=P(D,0,G).
\tag{18}
$$
原两表逐系数准确满足
$$
P_{-1}^{[0]}=P_0^{[0]}.
\tag{19}
$$
$u=\kappa=0$ 时补项的 E 输入为零。因此整个 $(1+L)$ 分母严格约去，
并给全部六个真实模 p 系数
$$
\boxed{
c_j\equiv b^{j-1}(A_j/\lambda+B_{j,\eta})\pmod p,\qquad 0\le j\le5 .
}
\tag{20}
$$
随附 JSON 的 reduced_residue 列出两种 $\eta$ 下全部 12 对
固定有理 CM 坐标。其完整定义是把 (18) 代入 (12)–(15)；
脚本从原 Pres/Pconst 重建全部表，不用素数采样或新测试。

尤其
$$
\boxed{
A_0=
\frac{
13397935849776258729526441354882155182177788347685155974
-7370090169156038523688747385665797822424677907483793849\,\omega
}{
809698546184498543351088767745116124498735185549856960
}\ne0 .
}
\tag{21}
$$
这个质量还可直接由原第六齐次矩
$(z_fq_f^2-z_f^3)rcd/42$ 计算。
另外五行的恢复仍保 (9) 全 C 第六矩，未用质量代替整源。

记 $\pi_0$ 的整数迹为 $a_p$。在所选 $\mathfrak p$ 处，
$$
\lambda=-1/\bar\pi_0\equiv-a_p^{-1}\pmod{\mathfrak p},
\qquad
b c_0\equiv-A_0a_p+B_{0,\eta}\pmod{\mathfrak p}.
\tag{22}
$$
清除固定分母后只涉及两个固定非零的二次范数多项式
$\operatorname{Norm}_{K/\mathbf Q}(-A_0T+B_{0,\eta})$。
$p\le X$ 时 Hasse 界给 $|a_p|\le2\sqrt X$，
每个非零范数值为 $O(X)$，至多有 $O(\log X)$ 个不同素因子。
故 (22) 为零的素数至多 $O(\sqrt X\log X)$。
若某个整数迹使范数准确为零，这样的迹只有有限个；
CM 范数式 $4p=a_p^2+3v^2$ 对每个迹仍给 $O(\sqrt X)$ 个可能 p。
固定分母另排有限集。此计数同时覆盖实际 $\eta=\pm1$。

当前 ray 有正密度，因而：

**定理。** 在其相对密度 1 子族中，所有 $N\in4\mathbf Z_{>0}$ 同时满足
$$
\boxed{
c_{0,p}(\kappa^N)\in\mathcal O^\times,\qquad
\mathscr F_{0,p}\notin K_{\mathfrak p}S .
}
\tag{23}
$$
一致性来自 $u=\kappa^N\equiv0\pmod p$ 和原实际整右逆的模 p 返回，
不是逐 N 再删坏集。

whole S34 核在 principal 偶空间上是 $\lambda$，故
$$
\boxed{
\mathcal A^S_{0,N}(0)=(1-\lambda)c_{0,p}(\kappa^N),\qquad
\mathcal A^S_{1,N}(0)=-(1-\lambda)c_{0,p}(\kappa^N).
}
\tag{24}
$$
R410 已付 $1-\lambda$ 单位，因此两个原 unit 质量也均为单位。

## 6. 原中央行和完整补域仍全部保留

(2) 保六个实际同 p 的 Mellin 观察，原 S 只给
$J_S=\sum_{j=1}^5s_jM_{j,p}$。
(23)–(24) 不证明任何 $M'_{j,p}$ 或 $\mathcal A^{S\prime}_{i,N}$ 非零。

R671 的未切 cd 完整式仍是
$$
\mathcal X^S_{i;n,N}
+\lambda^{n+3N}\mathcal A^S_{i,N}
=\epsilon_i\lambda^{n+N}J_S .
\tag{25}
$$
所有原外部、质量及 log 项继续存在。
尺度移权时，(24) 产生的非零质量乘 log 常数必须完整保留。
R674 可在原核中另选不同测试，使其 $t=0$ 共同来源回 S；
那是另一测试和另一端点，不改变本篇原固定 $\widehat P_p$ 的结论。

本篇新增 (1) 的实际端点、(12)–(15) 全六系数、
原固定右逆的全 (20) 表，以及 (23)–(24) 的实际非 S/单位质量判据。
主目标仍未完成：仍须控制 (25) 的完整外部，
或支付这六个观察之间真正的算术关系。

## 7. 复核文件

- scripts/check-r675-original-cd-endpoint-six-source.js
- scripts/check-r675-original-cd-endpoint-six-source.json

默认脚本读取已发表的 check-r659-frozen-gate-mass-and-full-compensation.json，
重建原右逆全部留数、完整补项和六维表。
它还导出 completeCoefficients(P,lambda,kappa,u,eta,b)，
对原 R594 完整 HatP 及准确 Q(omega) 参数直接求全部 (15)，
不把高次参数截成留数。证书保 155 条完整 quarter 归一恒等式、
两种 eta、C 第六矩、固定三角逆和全部有理系数。

主要依赖：

- [R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)：固定原右逆。
- [R659 原数据](../scripts/check-r659-frozen-gate-mass-and-full-compensation.json)：Pres/Pconst。
- [R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)：完整 Cperp core。
- [R666](R666-original-conditional-a-sources-and-exact-depth-recurrence.md)：原条件来源。
- [R669](R669-original-double-s-six-dimensional-source-return.md)：完整 S34 线丛和六基。
- [R671](R671-fixed-depth-cd-return-and-original-exterior-filters.md)：未切 cd 域与原外部。

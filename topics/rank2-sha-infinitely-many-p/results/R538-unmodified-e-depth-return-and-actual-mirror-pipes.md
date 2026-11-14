# R538 — 未移动测试的 E 深返回与实际镜管消去

日期：2026-11-14。**状态：已证明。** R529 的原 $K$ 单位测试在另附
$E$ 深条件时，不必改成 $E/\kappa^n$。整个四输出推前准确乘一个
显示的单位多项式。它与真正改变 $Y$ 的 $J$ 核配合后，把原非零管
所在的已知 $S$ 中央行收缩到三个伴随都深的同一个实际域。

R535 的 $\mathcal N$ 分量还有一个真正的输入交换：原 $R_3$ 深、
独立 sigma 单位管与其镜管完整相消，保 native $Y$ 权及全部另外
四个条件。这个消去只针对显示的分量；它不把整个来源的补域赋零，
也不保持旧 $W$ 的 native 权。主目标仍未闭合。

## 1. 同一来源、同一测试、同一四输出

用 R529–R535 的原规范
$$
a=2+\omega,\quad\eta=2/a,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad b=17,\quad d=p-1.
$$
仍取原六 sigma 来源 $\rho_0=-\nu_\sigma^{\otimes6}/84$，
实际行
$$
J=(R-ax)/2,\quad K=(R+ax)/2,\quad
R=R_3,\quad E=E_K,\quad H_0=E+\eta K.
\tag{1}
$$
保 R532 的完整正交框架
$(J,A_5,K,E,B_2,C_{30})$ 及
$$
\boxed{
\Pi=(J,A_5,B_2,C_{30}),\qquad
Y=\frac{2(-1+4\omega)}3J+2A_5.
}
\tag{2}
$$
四个输出与 $K,E,H_0$ 全正交。$\Pi$ 逐个被原 $\mathcal T$ 固定。

本篇一直使用同一个未移动的测试
$$
\boxed{
\widehat P_K=
\frac1{216b\Omega^6}\sum_{j=0}^6\binom6j
 \frac{\eta^jE^{6-j}K^j}{D_j},\qquad
D_j=1+\lambda\kappa^j .
}
\tag{3}
$$
所有分母为 R529 已付的单位。

## 2. 七个整条四输出矩，而非仅三个 Taylor 系数

定义完整四输出来源
$$
\mathcal F_j=
\frac{\binom6j\eta^j}{216b\Omega^6}
 \Pi_*\{E^{6-j}K^j\,d\rho_0\}.
\tag{4}
$$
准确有
$$
\boxed{
(\mathcal F_0,\ldots,\mathcal F_6)
=\frac1{27}(-1,0,0,20,0,0,8)\,\Pi_*\rho_0 .
}
\tag{5}
$$
这里没有先取第一 $Y$ principal 块；(5) 保所有四个输出及任意
依赖它们的连续测试。

以下给全函数证明。R535 的全 Hesse 张量表明，第
$2,4,5$ 个 $E$ 矩在保其他五输出时恒零，因此
$\mathcal F_1=\mathcal F_2=\mathcal F_4=0$。
同一整个偶线给
$$
E^6\text{ 行}=-8b\Omega^6\cdot E^0\text{ 行},
$$
故 $\mathcal F_0=-\Pi_*\rho_0/27$。

对于 $\mathcal F_5$，R535 的第一个 $E$ 矩只含
$\mathsf Q(R)\mathsf Q(Q)$，其中
$\mathsf Q(z)=x_\wp(z)\sigma(z)^3=\sigma(\delta z)/\delta$。
在保 $Q,\xi_2,d_0$ 时，相关的 $(R,x)$ 联合是
$\nu_{\mathsf Q}(R)\otimes\nu_\sigma(x)$。
用输出 $U=2J$、$V=2K$，其生成函数为
$$
\mathsf Q(s+t)\sigma(a(t-s)).
$$
由于 $a=-\omega\delta$，该函数关于 $t$ 是偶函数。故整个第五
$K$ 矩为零，$\mathcal F_5=0$，并非只在零点核一个数值。

剩下的 $\mathcal F_6$ 可在两个原 primitive 来源上精确支付。
令
$$
F_{\mathsf B}(s,t)=B_3(s+t)\sigma(a(t-s)),\qquad
F_{\mathsf P}(s,t)=\sigma(s+t)^3\sigma(a(t-s)).
$$
它们在 $s$ 方向属于整个 even $\mathcal S_6$，分别是型 $1,4$。
这两个型子空间各只有一维，基为
$-x_\wp y_\wp\sigma^6$、$x_\wp\sigma^6$。
第六 $K$ 矩保持这些型。由
$$
B_3(z)=1+\frac{3b}{10}z^6+\cdots,\quad
\sigma(z)=z+\frac b{210}z^7+\cdots,\quad a^6=-27
$$
直接得
$$
[s\,t^6]F_{\mathsf B}
=[s^4t^6]F_{\mathsf P}=\frac{12ab}{5}.
$$
物理 $K=V/2$ 的矩因子是 $6!/2^6$，而两条原 $U$ 边际首项分别为
$-as,-as^4$。由整个单重型空间，准确得到
$$
\boxed{
U_*(K^6\,d(\nu_{\mathsf B}\otimes\nu_\sigma))
=-27b\Omega^6\,U_*(\nu_{\mathsf B}\otimes\nu_\sigma),
}
$$
$$
\boxed{
U_*(K^6\,d(\nu_{\mathsf P}\otimes\nu_\sigma))
=-27b\Omega^6\,U_*(\nu_{\mathsf P}\otimes\nu_\sigma).
}
\tag{6}
$$
R535 的第零 $E$ 行恰是这两个真实来源与另外 $Q$ 因子的和，
故 (6) 给 $\mathcal F_6=8\Pi_*\rho_0/27$。
最后 R522 的整个 $H_0^6$ 身份给
$\sum_j\mathcal F_j=\Pi_*\rho_0$，于是
$\mathcal F_3=20\Pi_*\rho_0/27$。这完成 (5)。

作为独立证书，还可以在原四 sigma 上直接抽全部六次系数。
它们的第一 $Y$ 来源共有原
$G_{16}=\sigma(2z)\sigma(2\delta z)/(4\delta)$；
其余属于整个三维
$\sigma^{18}\operatorname{span}\{x_\wp^7,bx_\wp^4,b^2x_\wp\}$。
该完整空间中重建得到的七行恰为 (5) 乘
$(1,-4/7,16/7)$。这只是第二次核查，不替代上述整条四输出证明。

## 3. E 深度无需再移动正测试

由实际 $E$ 核 $\beta$，在 (4) 中限制 $E\in p^n$，
准确再乘 $\beta^n\kappa^{(6-j)n}$。$K$ 核同为 $\beta$，
且固定 $E,\Pi$；限制 $K$ 单位准确乘 $D_j$，
与 (3) 的分母逐项相消。

所以对每个 $n\ge0$ 有整个四变量测度身份
$$
\boxed{
\Pi_*\{{\bf1}_{E\in p^n,\ K\ {\rm unit}}\widehat P_K\,d\rho_0\}
=\beta^n P(\kappa^{3n})\,\Pi_*\rho_0,
\qquad P(t)=\frac{8+20t-t^2}{27}.
}
\tag{7}
$$
$P(1)=1$；对于 $n\ge1$，
$P(\kappa^{3n})\equiv8/27\bmod p$，故是当前处单位。
没有新增射线或大素数门。

(7) 真正使用未改动的 $\widehat P_K(E,K)$，
并非先改成 $\widehat P_K(E/\kappa^n,K)$ 再把记号省去。
它支付了 R532 中该额外移权的实际区别。

原 $h=\omega^2\mathcal T_*\rho_0$ 也满足同式：
$\mathcal T$ 固定 $\Pi$，把 $E,K$ 同乘 $\omega^2$；
(3) 的总次数是六，所有显示深度/单位条件均保持。
这里没有增加一个独立的曲线中央条件。

对于任意 $n\ge1$，(7) 相邻相减还保真实
$v_p(E)=n$ 环带，其系数为
$$
\beta^n\{P(\kappa^{3n})-\beta P(\kappa^{3n+3})\}.
\tag{8}
$$
模 $p$ 为 $\beta^n(8/27)(1+\lambda)$，同样是单位。
只声明这些真实紧开深度与环带，不作不必要的任意 Borel 延伸。

## 4. 与真正混 Y 的 J 核合用

取非负 $(n,\ell,m)$ 和 $r\ge1$，在同一个原来源中定义
$$
\boxed{
\mathcal C_{r;n,\ell,m}
=\{J\in p^r,\ K\ {\rm unit},\
      E\in p^n,\ B_2\in p^\ell,\ C_{30}\in p^m\}.
}
\tag{9}
$$
R532 的实际核心表给 $B_2:\beta$、$C_{30}:\chi\lambda$，
其中 $\chi=\chi_{65}$。这两轴和 $J$ 均正交于 $K,E$，
故 (3) 原样保留。

取完整逆输出
$$
\Pi_{r,\ell,m}=
(J/\kappa^r,\ A_5,\ B_2/\kappa^\ell,\ C_{30}/\kappa^m).
$$
由 (7) 和真实三个核心，
$$
\boxed{
(\Pi_{r,\ell,m})_*
\{{\bf1}_{\mathcal C_{r;n,\ell,m}}\widehat P_K\,d\rho_0\}
=\beta^{r+n+\ell}(\chi\lambda)^mP(\kappa^{3n})\,
 \Pi_*\rho_0.
}
\tag{10}
$$
全部逆尺度只在 (9) 的实际像使用。

第一算术观察必须用
$$
\boxed{
Y_r=\frac{2(-1+4\omega)}3\,J/\kappa^r+2A_5,
}
\tag{11}
$$
这正是原非零管已经采用的真实 $J$ 移权。
于是对全部 Mellin 变量，
$$
\boxed{
\int_{\mathcal C_{r;n,\ell,m},\ Y_r\ {\rm unit}}
 \langle Y_r\rangle^{du}\widehat P_K\,d\rho_0
=\beta^{r+n+\ell}(\chi\lambda)^m
 P(\kappa^{3n})J_S(u).
}
\tag{12}
$$
因此原 $J'_S(0)=0$ 确实控制 (12) 的完整中央。
这个结论不是把纯伴随边际误认为新算术来源：
其右侧仍是同一条原 $S$，左侧则已付显示的实际混 $Y$ 返回。

特别取 $\ell=m=n$。R529/R532 的原非零管
$$
\mathcal D_{n,r}=
\{A_5,B_2,C_{30},E\in p^n,\ K\ {\rm unit},\
                          J/\kappa^r+K\in p^n\}
\tag{13}
$$
包含于 (12)，且仍使用完全相同的测试与 $Y_r$。
其局部中央赋值仍为 $5n$。
已控制的外域现在可准确收缩为
$$
\boxed{
\{\mathcal C_{r;n,n,n},\ Y_r\ {\rm unit}\}
       \setminus\mathcal D_{n,r}.
}
\tag{14}
$$
尚未处理的是 $A_5$ 深条件和 $J/\kappa^r+K$ 的真实近相消，
而非再把 $E,B_2,C_{30}$ 放回全域。

## 5. 一个真实来源分量的绝对镜面对称

R535 的完整 Hesse 中，
$$
\boxed{
\rho_{\mathcal N}=
-\frac{\omega^2}{28}
 \nu_{\mathsf Q}(R)\otimes\nu_{\mathsf Q}(Q)
 \otimes\nu_{\mathsf Q}(Z)
 \otimes\nu_\sigma(x)\otimes\nu_\sigma(\xi_2)
 \otimes\nu_\sigma(d_0)
}
\tag{15}
$$
是原整个来源中的一个明确有符号分量，非另认的算术零线。

定义真实物理反射
$$
\boxed{
\mathcal R_K:\quad
(R,x)\longmapsto(-ax,-R/a),
\quad (Q,Z,\xi_2,d_0)\text{ 固定}.
}
\tag{16}
$$
它固定 $J,A_5,E,B_2,C_{30}$，使 $K\mapsto-K$，
因此固定整个 native $Y$ 与 (11) 的 $Y_r$。
它与 $P_{J,r}$ 交换。

原分量的绝对相位也恰为一。因为
$\mathsf Q(z)=\sigma(\delta z)/\delta$、$\delta/a=-\omega^2$、
$\omega^2a=-\delta$，
$$
\mathsf Q(-v/a)\sigma(-ar)
=-\frac{\omega^2a}{\delta}\mathsf Q(r)\sigma(v)
=\mathsf Q(r)\sigma(v).
$$
因此
$$
\boxed{(\mathcal R_K)_*\rho_{\mathcal N}=\rho_{\mathcal N}.}
\tag{17}
$$
这个身份使用原 sigma 的实际 CM 缩放，包含完整规范；
不从一个投影矩阵猜反射标量。

对于 (13) 一类 $E$ 深条件和不再依赖 $E$ 的其余测试，
$\rho_{\mathcal N}$ 的 (3) 只有 $j=5$ 项能贡献。
这是 R535 的整个第 $1$ 个 $E$ 矩；其余 $0\le6-j\le6$ 全零。
所以在这些实际域中，该分量的完整积分恰是一个
$K^5$ 奇测试。将 (16) 作用于域，native $Y_r$ 不变，积分严格取负。

## 6. 两条原近相消管的完整配对

置
$$
\boxed{
\begin{aligned}
\mathcal D^+_{n,r}&=
 \{A_5,B_2,C_{30},E\in p^n,\ K\ {\rm unit},\
                      J/\kappa^r+K\in p^n\},\\
\mathcal D^-_{n,r}&=
 \{A_5,B_2,C_{30},E\in p^n,\ K\ {\rm unit},\
                      J/\kappa^r-K\in p^n\}.
\end{aligned}}
\tag{18}
$$
这里 $J\in p^r$，两条件均迫使 $J/\kappa^r$ 为单位。
当 $n\ge1$ 时两管不交，且
$$
\boxed{\mathcal R_K\mathcal D^+_{n,r}=\mathcal D^-_{n,r}.}
\tag{19}
$$
在未作 $J$ 压缩前，它们分别就是
$\{R\in p^n,x\ {\rm unit}\}$ 与
$\{x\in p^n,R\ {\rm unit}\}$，连同其余显示深条件。
全部四个原隐藏条件都保留。

由 (17) 及前节的整个奇测试，对任意只依赖
$(J/\kappa^r,A_5,B_2,C_{30})$ 的连续权，
特别是 native 单位 Mellin 权，准确有
$$
\boxed{
\begin{aligned}
&\int_{\mathcal D^+_{n,r}}
 d\log\langle Y_r\rangle\,\widehat P_K\,d\rho_{\mathcal N}\\
&\qquad+
\int_{\mathcal D^-_{n,r}}
 d\log\langle Y_r\rangle\,\widehat P_K\,d\rho_{\mathcal N}=0.
\end{aligned}}
\tag{20}
$$
这消掉了一个真正的补域分量，不只是它的第一个 Taylor 系数。

该分量两边都非零。R535 的原全函数核给其第一管首五系数
$$
q_5=-\frac{80}{64827}-\frac{8\delta}{7203},
\qquad
\boxed{Nq_5=\frac{64}{3^6\,7^5}.}
\tag{21}
$$
整个局部第五阶为
$(d/b)(1+\lambda\kappa)q_5/D_5$，是当前处单位。
其五个深 primitive 输入仍是实际 sigma 类型，全部高尾严格更深。
该分量的 $(U,V)$ 来源也在同一个 whole $\mathcal S_6\otimes\mathcal S_6$
中；所以其真实 $J$ 核仍为 $\beta$，保全部其他输入。
因此 (20) 两个积分的赋值都准确为 $5n$；
$J$ 深度仅再乘实际单位 $\beta^r$。

局部质量以及所有固定尺度 log 项由独立 $\xi_2,d_0$ 的零质量
准确消去，且 (16) 本来就固定 $Y_r$。
这里没有从质量不明的另一个测试借用零质量。

## 7. 哪些补项仍须保留

(20) 仅针对 (15) 这一实际分量。Hesse 的
$\mathcal L,\mathcal M$ 项不因此变成同一个反射不变来源，
故不能把整个 $\rho_0$ 的两管积分宣称为零。
(14) 中除这两个管及其 $\mathcal N$ 分量外的其余部分仍未控制。

另外旧 $W$ 在 (16) 下准确变化为
$$
\boxed{W\longmapsto W-2(1/3-\delta)K.}
\tag{22}
$$
同样公式用于原 $J$ 转置后的 $W_r$。
所以 (20) 不保持旧 $T$ 的 native 权。
若比较该曲线，必须运输 (22)，并在含 $W$ 的测试中保整个 $E$
来源，不能先按七个低矩忘去它。R529 的两项 $W$ 补偿仍然存在。

本篇新增的控制是 (7) 的未移动测试完整返回、(10)–(14) 的
真实混 $Y$ 收缩，以及 (18)–(21) 的一条完整补域配对。
没有增加未经证明的独立中央条件，也没有完成主目标。

## 精确证书与依赖

- [完整四输出矩、未移动深度系数与实际镜管](../scripts/check-r538-unmodified-e-depth-and-actual-mirror-pipes.mjs)；
  [全部精确数据与独立 S18 重建](../scripts/check-r538-unmodified-e-depth-and-actual-mirror-pipes.json)。
  同一 BigInt/CM 主体已在 V8 执行。独立验证了两个 whole S6
  primitive 第六矩、七个比例、绝对镜面相位、真实 $J/Y$ 不变、
  $q_5$ 范数以及原四 sigma 的完整三维重建。
- [R535：原 Hesse 五项与整个 E 深核](R535-original-hesse-tensor-and-complete-mixed-kernel.md)。
- [R532：全部六轴与原真实深域](R532-original-j-a5-full-frame-and-rank-two-source.md)。
- [R529：同一测试、原非零管及 W 补偿](R529-original-low-j-k-core-and-complete-st-carry.md)。
- [R522：原 H0 的完整正六次来源身份](R522-common-degree3-even-factor-and-same-st-positive-test.md)。

# R737 — 同一负一首行的全部共同深层消元与原四单位、双返回条带

日期：2026-11-15。**状态：已证明。**

本篇保持 R734 的同一个实际测试 $q_N^*$，不重新适配来源。
R735 已证明的负一首项可以沿原完整 E/Z 两轴核心，
准确移到一个**有限的 primitive 条带组合**：
它只使用 $Y,Z,E$ 同为单位的两斜门差，
以及这个域中真正的四-unit部分和 W/V 两个深支。
全部 $Z,E$ 共同正深层由显示的三十一阶整算子消去。
两次有限过滤只给首项再乘单位，不新增射线条件。

这个非零仍是原 T 的实际内/外补偿。
原两个单独 $\mathcal O_i^T$ 的完整端点项、全部条件质量、
两条第二态的不同有理观察及移动门在下文同时保留。
并未把某一返回条带认成原 T 中央。

## 1. 同一个 cd 来源与 E 的有限次数

固定原 ordinary 子族和
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad
N\in4\mathbf Z_{>0},\qquad q_N=q_N^* .
\tag{1}
$$
固定 p、N 后，整个测试及其系数不随下面 n 的移位改变。
令
$$
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
\alpha=17-3\omega,\quad \bar\alpha=20+3\omega,\quad
b_Y=\bar\alpha/17,
$$
$$
Z=W-b_YY,\qquad V=36Y-\alpha W,\qquad
E=E_{YW}=(5+6\omega)A-29c-(58+87\omega)d.
\tag{2}
$$
所有三个 A 伙伴仍保留。

令 $\rho_{0,N}=\Phi_N\mu_0$ 为 R715(3) 的**完整 cd 返回来源**。
$\Phi_N$ 包含 R734 的同一整逆、C-unit、E-test 单位逆，
以及将 C 单位条件返回时的两项；它不是只取其中第一项。
使用 R686(10) 的原未删 C-unit 表示，可将其唯一写成
$$
\boxed{\Phi_N=\sum_{a=0}^{30}E^a\phi_{a,N}.}
\tag{3}
$$
每个 $\phi_{a,N}$ 是原有界整测试，
只依赖同时正交于 $Y,Z,E$ 的三个伙伴。
若用 R715 的两个 C 分支展开，(3) 对两个分支分别展开后相加。

确实，实际多项式中的 E 只经
$$
H=D_*-\frac E{29},\qquad K=H-\frac{406}{143}D_*
$$
进入；$C^\perp,E_\perp,G_\perp,G_{00},D_*$ 均与 E 正交。
C-unit 指示也与 E 正交。每个混次块仍保原
$b^{d/6}\Omega^d$ 归一，固定这些单位后 (3) 的系数整。
最高次数30来自已付的 G 幂及 C12 家族；R734 没有增加 B 列或新次数。

原三态记为 $e_0=\mu_0,e_1,e_2$，列像矩阵 R、K 如 R692。
令 $\rho_{i,N}=\Phi_N e_i$。R734 的完整来源保持
$$
Y_*\rho_{0,N}=S,\qquad W_*(\rho_{0,N},\rho_{1,N},\rho_{2,N})
 =6\delta(T,T,-T),\qquad
\Omega^{-1}Y_*(Z\rho_{0,N})=0 .
\tag{4}
$$
第二、三态的 Y 来源仍为
$\omega^2S/2\pm[1/2]_*S_{\rm new}$。
上述都是完整来源等式，不在其后凭空添加本篇条带。

## 2. 同一两斜门及真实 native 行

用已发表斜门 note 的准确系数
$$
\begin{array}{c|cc}
i&b_i&e_i\\ \hline
1&-(170+117\omega)/526&-(4+9\omega)/263\\
3&(170+291\omega)/526&(2-3\omega)/263 .
\end{array}
\tag{5}
$$
记
$$
B_i=b_iZ+e_iE,\qquad
\Delta_\ell=1_{B_1\in p^\ell}-1_{B_3\in p^\ell},\qquad \ell\ge0.
\tag{6}
$$
这里 $34B_i=34Y_i-29Y$ 是原与 Y 正交的实际斜轴，
并非换了一个同范数轴。$\Delta_0=0$。
沿原固定坏集，四个 $b_i,e_i$ 及
$b_1e_3-b_3e_1=-5/263$ 都是单位。

对任意整坐标点，$\Delta_\ell\ne0$ 只可能在
$$
v_p(Z)=v_p(E)=j<\ell
\tag{7}
$$
上。若两个赋值不同，两个 B 都有相同的较小赋值，
不能恰有一条深；若两者都至少为 $\ell$，差也为零。
所以所有共同深层的以下分解是完整的，未丢一条“单位补域”。

令 $n>N,\ell=n-N$。R713 的整数旋转换元、
原共同 cd 返回及 Y 核给同一完整权上的 native 配对式
$$
\begin{aligned}
\mathcal R_{N,n}(w)
={}&\lambda^{n+3N}
 \int_{Y\ {\rm unit}}\Delta_\ell\Phi_N\\
&\quad\cdot\{\langle b_YY+uZ\rangle^{d_pw}
        -\langle b_Y\rangle^{d_pw}\langle Y\rangle^{d_pw}\}\,d\mu_0,
\qquad d_p=p-1 .
\end{aligned}
\tag{8}
$$
它等于原 $\mathcal I^T_{\rm pair}
-\langle b_Y\rangle^{d_pw}\mathcal I^S_{\rm pair}$。
(8) 的 E 是已付 cd 返回坐标，两个 C 分支按 (3) 保留；
不是在原坐标忘 E 后重新加门。
因 $u\in p\mathcal O$，两个 unit cut 准确同为 Y-unit，
故 (8) 的相对质量逐点为零。

对 $k\ge1$ 定义
$$
M_{a,k}(\ell)=
 \int_{Y\ {\rm unit}}\Delta_\ell\,Z^kY^{-k}
       E^a\phi_{a,N}\,d\mu_0,\qquad M_{a,k}(0)=0.
\tag{9}
$$
全部真实负矩只在显示的单位域上读取。于是
$$
\mathcal R'_{N,n}(0)=d_p
 \sum_{k\ge1}\frac{(-1)^{k+1}u^k}{k b_Y^k}F_k(n),
\quad
F_k(n)=\sum_{a=0}^{30}F_{a,k}(n),\quad
F_{a,k}(n)=\lambda^{n+3N}M_{a,k}(n-N).
\tag{10}
$$
所有 $1/k$、混次系数和完整 C 补偿保留。
$k\ge2$ 的尾在 $p^{2N}\mathcal O$ 中；本文所有有限移位算子均整，
所以此尾界以后仍成立。

## 3. whole E 核在原三态上的范围

R686 §2 已支付 standard odd7627 的全核
$\chi_E\lambda$，$\chi_E^2=1$。
这是同一 E 输出、全部伙伴保持的身份。
E 与 W 正交，故其完整 restriction、缩放和 canonical W 四挠算子
逐项交换；因此它在原 $e_0,e_1,e_2$ 上均为同一个标量，
不需从某条边际重新定号。

同时 R692 的 Z 核为 $\gamma\lambda R_YR$，
其中 $\gamma=\chi_A\chi_E$、$\chi_A=\chi_{29,p}\in\{\pm1\}$。
由于 $Re_0=e_0$，两个正交轴在原第一态给
$$
\boxed{
\mu_0|_{\{E,Z\in p^j\}}
=\chi_A^j\lambda^{2j}
 \bigl(P_{E,\kappa^j}P_{Z,\kappa^j}R_Y^j\bigr)_*\mu_0 .
}
\tag{11}
$$
C 角平均逐项固定 E/Z，故也在这个完整身份中。
(3) 的系数 $\phi_{a,N}$ 被 (11) 逐点固定；
仅显示的 $E^a$ 产生 $\kappa^{aj}$。
不存在一个漏记的移动 C-unit 或 E-test 指示。

## 4. 全部共同深层的精确一阶递推

令
$$
P_{a,k}(\ell)=
 \int_{\{Y,Z,E\ {\rm unit}\}}\Delta_\ell\,Z^kY^{-k}
                 E^a\phi_{a,N}\,d\mu_0 .
\tag{12}
$$
这里的 P 是原 primitive 条带积分，不是新的 theta 投影。
按 (7) 把 (9) 分成 $Z,E$ 同为单位和同为非单位。
在后一部分用 (11) 的 $j=1$：
$Y\mapsto-Y$、$Z,E\mapsto\kappa Z,\kappa E$，
$\Delta_\ell\mapsto\Delta_{\ell-1}$。
得到完全准确的关系
$$
\boxed{
M_{a,k}(\ell)
=P_{a,k}(\ell)+r_{a,k}M_{a,k}(\ell-1),
\qquad
r_{a,k}=(-1)^k\chi_A\lambda^2\kappa^{a+k}.
}
\tag{13}
$$
迭代后也是有限恒等式
$$
M_{a,k}(\ell)=\sum_{j=0}^{\ell-1}r_{a,k}^{\,j}P_{a,k}(\ell-j).
\tag{14}
$$
特别每个旧共同深层都在 (14) 中；没有极限冻结。
$k\ge1$ 时 $v_p(r_{a,k})=a+k>0$，
所以相应无限卷积在需要时也是真有界收敛。
这里不将 $q_N$ 换成 $q_{N+j}$。

令
$$
c_{a,k}=\lambda r_{a,k}
=(-1)^k\chi_A\lambda^3\kappa^{a+k},\qquad
P^F_{a,k}(n)=\lambda^{n+3N}P_{a,k}(n-N).
$$
若 $\mathsf T_2$ 表示同一实际序列的 $n\mapsto n+2$，(13) 给
$$
\boxed{
(\mathsf T_2-c_{a,k}^2)F_{a,k}(n)
=P^F_{a,k}(n+2)+c_{a,k}P^F_{a,k}(n+1).
}
\tag{15}
$$
右边的 $n+1$ 项保它自己的实际门和反射奇偶，
不是把奇一步冒作偶一步。

定义有限整算子
$$
\boxed{
\mathscr Q_k^{(2)}
=\prod_{a=0}^{30}(\mathsf T_2-\lambda^6\kappa^{2(a+k)}).
}
\tag{16}
$$
设 $\mathscr Q_{k,\ne a}^{(2)}$ 删除对应 a 因子，
则对整个 (10) 的第 k 系数有
$$
\boxed{
\mathscr Q_k^{(2)}F_k(n)
=\sum_{a=0}^{30}\mathscr Q_{k,\ne a}^{(2)}
 \{P^F_{a,k}(n+2)+c_{a,k}P^F_{a,k}(n+1)\}.
}
\tag{17}
$$
最高31次偶步、实际共62层。
这是原31个 E 次数的有界有限消元，未引入新的高次来源。
某个 $\phi_{a,N}$ 为零时，该项自动为零；
可统一保30这一原次数上界。

## 5. 原 rank-one 负矩的非零转移到 primitive 条带

保 R734 的原算子
$$
\mathscr P_{31}^{(2)}
=\prod_{j=1}^{31}(\mathsf T_2-\lambda^4\kappa^{2j}),\quad
U_{31}=\prod_{j=1}^{31}(1-\kappa^{2j}),\quad
V_{31}=\prod_{j=1}^{31}(1-\lambda^2\kappa^{2j}).
\tag{18}
$$
全部单位性来自 $\kappa\in p\mathcal O$。
它与 (16) 交换，因为 p、N、测试均固定。

R734 的原冻结差为
$$
\mathcal D_N(0)=\frac caD_{\omega,17}+\frac1aD_{-,17},\qquad
\mathfrak I_N=\Omega\int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{\mathcal D_N(0)}.
\tag{19}
$$
a、c 是该篇实际完整整逆的代数单位，不能用有限域读数替代。
R735 已证明 $\mathfrak I_N\ne0$；
固定合格 p、充分大 $N\in4\mathbf Z$ 时，
$v_p(\mathfrak I_N)=v_p(\mathfrak I_\infty)<N$。

在 R734 已提取的 k=1 常数模态上，
$\mathsf T_2$ 的特征值为 $\lambda^4$。
因此 $\mathscr Q_1^{(2)}$ 的准确乘数为
$$
\prod_{j=1}^{31}(\lambda^4-\lambda^6\kappa^{2j})
=\lambda^{124}V_{31}.
$$
结合原全部尾，严格得到
$$
\boxed{
\mathscr Q_1^{(2)}\mathscr P_{31}^{(2)}
  (\mathcal I^T_{\rm pair})'(0)
=\frac{d_p\,s\,u}{b_Y}
 \lambda^{2n+2N+248}U_{31}V_{31}\mathfrak I_N
 +p^{2N}\mathcal O,\qquad s=(-1)^{n-N}.
}
\tag{20}
$$
相同两个算子杀掉整个 paired-S Mellin 行，
故其尺度 log 乘质量也被整个消去，未提前删掉。
每个系数整，额外62层实际移位不降低 $p^{2N}$ 尾界。

更具体，定义只含原 primitive 条带的有限组合
$$
\boxed{
\mathcal C_{N,n}=
\frac{d_pu}{b_Y}\,
\mathscr P_{31}^{(2)}
\sum_{a=0}^{30}\mathscr Q_{1,\ne a}^{(2)}
 \{P^F_{a,1}(n+2)+c_{a,1}P^F_{a,1}(n+1)\}.
}
\tag{21}
$$
由 (10)、(17)，(20) 左边恰为
$\mathcal C_{N,n}+p^{2N}\mathcal O$。
故同一个 p、所有充分大的 N 和所有 $n>N$ 上，
$$
\boxed{
v_p(\mathcal C_{N,n})
=N+v_p(\mathfrak I_\infty)<2N.
}
\tag{22}
$$
这是同一个 q 的实际负一值，所有共同正深层已由有限恒等式去掉。
没有用 $I_{\Sigma_5,-1}$ 或另一个来源的单位见证替代 (19)。

## 6. 三个互斥 primitive 部分与真实 W/V 返回

在 (12) 中 $Y,Z,E$ 均为单位。
由原两个框架的单位行列式，
W 与 V 不可能同时深；W 深时 V 单位，V 深时 W 单位。
因此 (12) 准确分为
$$
\mathcal G_{4,E}=\{Y,Z,W,V,E\ {\rm unit}\},
\quad
\{Y,Z,E\ {\rm unit},W\in p\},
\quad
\{Y,Z,E\ {\rm unit},V\in p\}.
\tag{23}
$$
每个部分保同一 $\Delta_\ell$。

写
$$
z_W=\frac{263\kappa W-\bar\alpha V}{612},\qquad
y_W=\frac{V+\alpha\kappa W}{36},
$$
$$
z_V=\frac{263W-\bar\alpha\kappa V}{612},\qquad
y_V=\frac{\kappa V+\alpha W}{36}.
\tag{24}
$$
这些是原 $P_{W,\kappa}$、$P_{V,\kappa}$ 对 Z、Y 的精确拉回。
在前者的 V-unit 域、后者的 W-unit 域，
$y_\bullet,z_\bullet$ 都是单位。
定义移动门
$$
\Delta_\ell^W=
1_{b_1z_W+e_1E\in p^\ell}-1_{b_3z_W+e_3E\in p^\ell},
\quad
\Delta_\ell^V=
1_{b_1z_V+e_1E\in p^\ell}-1_{b_3z_V+e_3E\in p^\ell}.
\tag{25}
$$
q 的三个伙伴、E 和所有 $\phi_{a,N}$ 均由两个物理映射固定。
原 W/V 核却把第一态送到 $e_1$，不可继续使用 $e_0$。

令
$$
\begin{aligned}
G_a(\ell)
 &=\int_{\mathcal G_{4,E}}\Delta_\ell\,\frac ZY
                    E^a\phi_{a,N}\,de_0,\\
H_a^W(\ell)
 &=\int_{\{V,E\ {\rm unit}\}}\Delta_\ell^W\,\frac{z_W}{y_W}
                    E^a\phi_{a,N}\,de_1,\\
H_a^V(\ell)
 &=\int_{\{W,E\ {\rm unit}\}}\Delta_\ell^V\,\frac{z_V}{y_V}
                    E^a\phi_{a,N}\,de_1 .
\end{aligned}
$$
则完整的原来源返回是
$$
\boxed{P_{a,1}(\ell)=G_a(\ell)+\lambda H_a^W(\ell)
                              +\gamma\lambda H_a^V(\ell).}
\tag{26}
$$
这里没有附加不需要的 Y-unit：它已由 (24) 对应的 V/W-unit准确保证。
因此 (21)–(22) 给同一四-unit及两条原返回支的有限非零关系。

尤其两个观察并不相同：
$$
\boxed{
\begin{aligned}
\frac{z_W}{y_W}
 &=-b_Y+\frac{36\kappa W}{V+\alpha\kappa W},\\
\frac{z_V}{y_V}
 &=\frac{263}{17\alpha}
       -\frac{36\kappa V}{\alpha(\kappa V+\alpha W)} .
\end{aligned}}
\tag{27}
$$
前者是 V-unit 上的原负矩展开；后者才有 W-unit 的负矩展开。
例如第二式的第一非恒定项是
$-36\kappa V/(\alpha^2W)$。
只有在完整保留 (25) 时才可将它接到原 W 的型五条件来源；
不能先忘 E 再附斜门。

(27) 的两个常数乘的是实际条件质量，均保留。
同样，$\ell>1$ 时 (25) 的 $\kappa W$、$\kappa V$ 项可能改变深门，
所以不能用 $\kappa=0$ 的门替换它们。
本篇不新增一个未经识别的 S72/V 高度来源来掩盖这些条件。

## 7. 各自 O0/O1 与完整 T 总行的准确比较

令
$$
A_{T,N}(w)=\int f_w(b_YY+uZ)\,d\rho_{0,N},\qquad
f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}.
$$
这是原已缩 Z 的 cd 观察，不是未缩放的 $6\delta J_T(w)$。
同一个整数旋转后的两支严格满足
$$
\boxed{
\mathcal O_{i,n}^T(w)
=\epsilon_i\lambda^{n+3N}A_{T,N}(w)-\mathcal I_{i,n}^T(w),
\qquad i=0,1,\quad \epsilon_i=(-1)^i .
}
\tag{28}
$$
(28) 保 q1 的完整换元，不把同一原角域中的 q1 偷换成 q0。
设
$$
W_{31}=\prod_{j=1}^{31}(1-\lambda^4\kappa^{2j})\in\mathcal O^\times .
$$
在 $\lambda^{n+3N}A_{T,N}$ 这一真实模态上，
$\mathscr P_{31}^{(2)}$ 的乘数是 $\lambda^{62}V_{31}$，
$\mathscr Q_1^{(2)}$ 的乘数是 $\lambda^{62}W_{31}$。
所以两个单独外部全行准确为
$$
\boxed{
\mathscr Q_1^{(2)}\mathscr P_{31}^{(2)}\mathcal O_{i,n}^T
=\epsilon_i\lambda^{n+3N+124}V_{31}W_{31}A_{T,N}
 -\mathscr Q_1^{(2)}\mathscr P_{31}^{(2)}\mathcal I_{i,n}^T .
}
\tag{29}
$$
两条系数除原 $\epsilon_i$ 外相同；
不能从“来源矩阵不同”另造一个不等系数来强迫相消。

由 (4)，原 Y-unit 上完整 Z 一阶来源为零，故
$$
A_{T,N}(w)
=\langle b_Y\rangle^{d_pw}J_S(w)
  +\text{从 }u^2\text{ 起的完整相对行}.
$$
如果原 $J_S'(0)=0$，则 $A_{T,N}'(0)\in p^{2N}\mathcal O$；
这里还使用了原 $J_S(0)=0$，没有删一个未知质量。
于是 (29) 精确显示每个外部的首项如何抵消其对应内部。

将两支相加，不需任何中央假设就有
$$
\boxed{
\begin{aligned}
\mathscr Q_1^{(2)}\mathscr P_{31}^{(2)}
 (\mathcal O_{\rm pair}^T)'(0)
&=-\mathscr Q_1^{(2)}\mathscr P_{31}^{(2)}
 (\mathcal I_{\rm pair}^T)'(0)\\
&=-\mathcal C_{N,n}+p^{2N}\mathcal O .
\end{aligned}}
\tag{30}
$$
故 (22) 的非零同时存在于两个原外部的真实和中。
(26) 把其未闭部分压成同一有限 primitive 条带组合，
而没有把该非零重新命名为原 $J_T'$。
原三中央零仍只适用于已付的完整归一词行。

## 8. 成本、量词和继续使用的接口

- 所有权都是 R734 的同一个 $q_N^*$。完整 $\lambda,\kappa,u$、
  C 两分支、全部高矩及原 $J_2,J_8,J_{14},J_{20},J_{26}$ 不变。
- 新消元只用 E 的既有最高次数30；不新增数值扫描、射线或theta覆盖。
  $\chi_E$ 的绝对号无需猜测；偶步式(16)保其平方，奇一步式(15)仍显示 $\chi_A$。
- 两个31阶偶步算子合计最多124层实际 n 移位，系数整，
  不降低原 $p^{2N}$ 高 k 尾。固定 p、N 后不改测试。
- 精确非零量词是固定合格 p，充分大 $N\in4\mathbf Z$，
  对所有 $n>N$ 成立；没有声称 p 一致的负一赋值界。
- 三个 primitive 部分 (23) 的不同单位轴、第二态和条件质量均在 (24)–(27) 中。
  剩余目标是这些完整原条带与原算术总行的关系，不是再支付一个独立轴核心。

本篇为现有完整来源身份的解析推导，不产生新的可重算输出文件。
依赖：
[R686](R686-original-yz-core-and-same-source-st-unit-failures.md)；
[R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)；
[R713](R713-symmetric-frozen-sources-and-exact-paired-mixed-remainder.md)；
[R715](R715-complete-first-z-source-and-fifty-neutral-returns.md)；
[R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)；
[R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)；
[两原斜门及负一提取](../notes/2026-11-15-two-adjacent-s-slanted-cores-and-native-pair.md)。

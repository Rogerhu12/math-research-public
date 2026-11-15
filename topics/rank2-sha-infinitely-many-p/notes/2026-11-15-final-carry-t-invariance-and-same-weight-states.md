# 原最终 q* 的三阶几何不变性与同权两态

日期：2026-11-15。**状态：已证明。**

R734 的最终实际测试 $q_N^*$ 仍严格被 R493 的物理三阶变换
$\mathcal T$ 固定。这是原六支 carry 的逐点恒等式，
不是从边际返回或辅助矩阵核猜得。
其证明保整个 E 次数逆、全部 $\lambda,\kappa,u$、
两条核修正和 C 的两个返回补项。
它不表示 $q_N^*$ 独立于原第四个 sigma 输入，
也不表示 cd 返回后的 $\Phi_N$ 被同一物理矩阵固定。

## 1. 同一个原矩阵和三个 carry 行

原物理输入是
$$
(\xi_1,\xi_2,\xi_3,x,c,d),\qquad
e_0=-\nu_\sigma^{\otimes6}/84 .
$$
在 $I=(\xi_1,\xi_3,x,c)$ 上，R493/R512 的矩阵是
$$
\mathcal T_I=\frac12
\begin{pmatrix}
-\omega&1&\omega^2&\omega\\
-\omega^2&-\omega&1&-\omega^2\\
-1&-\omega^2&-\omega&1\\
-\omega&1&-\omega^2&-\omega
\end{pmatrix};
\tag{1}
$$
它固定 $\xi_2,d$，并且
$\mathcal T^3=I$、$Y\mathcal T=Y$。
本注没有换用另一个来源空间中的同名三阶算子。

保持 R536 的实际行
$$
\begin{aligned}
C&=(\xi_1-\xi_3+x)/\delta,\\
H_1&=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\\
D&=\xi_1+\omega^2\xi_2-2\omega\xi_3+c+(2+3\omega)d,\\
F&=D+C,\qquad G=13H_1+(3-2\omega)F,\qquad \delta=1+2\omega .
\end{aligned}
\tag{2}
$$
将 (2) 的行乘完整 (1)，准确得到
$$
\boxed{C\mathcal T=\omega^2C,\qquad
F\mathcal T=F,\qquad G\mathcal T=G.}
\tag{3}
$$
这些是六变量线性身份，R536(39) 已逐行支付。
特别不只在某条深管、某个边际或 $u=0$ 时成立。

## 2. 整个六支算子逐点被固定

固定原
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
$$
对每个 $\zeta\in\mu_6$，写
$$
D_\zeta=F-\zeta C,\qquad E_{c,\zeta}=F+13\zeta C.
$$
由 (3)，
$$
D_\zeta\circ\mathcal T=D_{\zeta\omega^2},\qquad
E_{c,\zeta}\circ\mathcal T=E_{c,\zeta\omega^2}.
\tag{4}
$$

令 $P_d(D,E_c,G)$ 为任意实际齐次 d 次多项式，
$d\in6\mathbf Z_{>0}$，允许其系数属于原
$K(\lambda,\kappa,u,\eta)$。
先对**整个**多项式作原次数逆
$$
\widehat P_d=
\sum_{a+e+g=d}
 \frac{[D^aE_c^eG^g]P_d}{1+\lambda\kappa^e}
 D^aE_c^eG^g .
\tag{5}
$$
原六支测试准确为
$$
\mathfrak C_N(P_d)=
\frac1{6b^{d/6}\Omega^d}
\sum_{\zeta\in\mu_6}
1_{\{D_\zeta\in p^N,\ E_{c,\zeta}\ {\rm unit}\}}
\widehat P_d(D_\zeta/\kappa^N,E_{c,\zeta},G).
\tag{6}
$$
这是 R702(13)–(14) 的实际定义。
原 $C$-unit/$F$-unit 条件在该域中等价地保留：
由于 $N\ge1$、$p\nmid14$，
$D_\zeta$ 深且 $E_{c,\zeta}$ unit 正好给 C、F 均为单位。

将 (4) 代入 (6)，再以 $\zeta\mapsto\zeta\omega^2$ 重排同六项，
得到
$$
\boxed{\mathfrak C_N(P_d)\circ\mathcal T=\mathfrak C_N(P_d).}
\tag{7}
$$
这里 $D_\zeta/\kappa^N$ 的真实深域、所有 E-unit 指示、
(5) 的每个分母及各混次周期全部不变。
$\mathcal T$ 不作用于参数 $(\lambda,\kappa,u,\eta)$；
没有把它们冻结为零或换成有限域数值。
特别 (7) 不要求 $P_d$ 对 C 本身不变。

原基准 R594 的六次测试、其九行中性差及所有
$G^{6h}/(b^h\Omega^{6h})$ 倍数均属于 (6) 的线性包。
因为 $G\mathcal T=G$，这些倍乘同样保持 (7)。
它不自动覆盖未选的 $B_0$ 块；下面准确检查实际最终选列。

## 3. R715 的五十列与 R734 的两条完整修正

R715 实际使用的50列只有：

- R702 已选的29条 G 家族，索引
  $0,\ldots,22,25,26,36,37,47,48$；
- 21条十二次 C 列
  $C^iF^jG^{12-i-j}$，其中
  $i=1,j=5,\ldots,11$；
  $i=2,j=5,\ldots,10$；
  $i=3,j=5,\ldots,9$；
  $i=4,j=5,6,7$。

每条 C 列都先按 R702 完整改成 $D,E_c,G$，再用 (5)、(6)。
没有一条 B 列进入这个实际50阶逆。
所以原两个测试
$$
q=q_N^{(715)},\qquad \zeta_N=\zeta_N^{(715)}
$$
都准确满足 (7)。

R734 的额外原列是
$$
v_{140}:\ C^4F^8,\qquad
v_{147}:\ C^5F^6G.
$$
它们同样是 (6) 的十二次列。
用原50阶实际矩阵 $M_{715}$ 定义的两条核修正为
$$
h_j=v_j-\sum_{a\in{\rm Sel}_{715}}v_a
 [M_{715}^{-1}\mathscr T_{50}(v_j)]_a,\qquad j=140,147.
\tag{8}
$$
(8) 中每个系数只依原固定参数，不依六个物理输入。
所以两条 h 也逐点被 $\mathcal T$ 固定，
不需要再计算一个矩阵或一个辅助素数。

最后 R734 的真正测试是
$$
q_N^*=q+\frac{b_0}{a}\zeta_N
          +\frac{r_1}{a}h_{140}+\frac{r_2}{a}h_{147},
\tag{9}
$$
其中 $a,b_0,r_1,r_2$ 是该篇在实际
$(\lambda,\kappa,\kappa^N,\eta)$ 上的完整五阶逆。
于是得到
$$
\boxed{
q_N^*\circ\mathcal T=q_N^*,\qquad
\zeta_N^{(715)}\circ\mathcal T=\zeta_N^{(715)}.
}
\tag{10}
$$
(10) 对原全部合格 p、全部 $N\in4\mathbf Z_{>0}$ 成立。
同一原整逆的单位性、最高次数30和固定坏集完全不变。

## 4. 同一未改权的完整两态

记
$$
h_W=e_1+e_2=\omega^2\mathcal T_*e_0,\qquad
\rho_N=q_N^*e_0,\qquad H_N=q_N^*h_W .
$$
这里的 $h_W$ 是 R493/R702 的原二挠态，
不是旧第三 sigma 核中的另一个同名来源。

(10) 与 R493 的整六变量恒等式给
$$
\boxed{
\mathcal T_*\rho_N=\omega H_N,\qquad
\mathcal T_*H_N=-\omega(\rho_N+H_N),\qquad
(\mathcal T^2)_*\rho_N=-\omega^2(\rho_N+H_N).
}
\tag{11}
$$
因而任意真实紧开域 $\mathcal D$、完整有界测试 f 都有
$$
\boxed{
\int_{\mathcal D}f\,dH_N
=\omega^2\int_{\mathcal T^{-1}\mathcal D}f\circ\mathcal T\,d\rho_N .
}
\tag{12}
$$
两个积分使用同一个 $q_N^*$；原门和观察仍完整转置。
特别 (12) 没有把 $\mathcal T^{-1}\mathcal D$ 换回 $\mathcal D$。

原 $\pi_4=(Y,W,W',G)$ 完整返回和 (11) 给
$$
Y_*(\rho_N,H_N)=\beta^N(S,\omega^2S),\qquad
W_*(\rho_N,H_N)=\beta^N6\delta(T,0),\qquad \beta=-\lambda.
\tag{13}
$$
更完整地，令 $W'=W\mathcal T$、
$W_2=W\mathcal T^2=-\omega^2W-\omega W'$，则
$$
\boxed{
\begin{array}{c|ccc}
 &W&W'&W_2\\ \hline
\rho_N&1&0&-\omega^2\\
H_N&0&-\omega&\omega^2
\end{array}
\quad\text{各项乘 }\beta^N6\delta\,\nu_T .
}
\tag{14}
$$
(14) 是全来源推前，不是只给质量。
对 $\zeta_N^{(715)}$ 替换 $q_N^*$，相同两态公式成立，
而 (13)、(14) 的全部边际为零。
因此仅由这些边际或其同域归一词，仍不能删除该真实中性方向。

## 5. 三个 scalar 深轴仍保全部伙伴

原 C、F、G 同时垂直于 $Y,W,W'$，故也垂直于 $W_2$。
(6) 的整个权被各原 W 轴缩放逐点固定。
R493 的两个完整 scalar 核及其真正 $\mathcal T$ 共轭因而给
$$
\boxed{
\begin{aligned}
\rho_N|_{W'\in p^m}
 &=\beta^m(P_{W',\kappa^m})_*\rho_N,\\
H_N|_{W\in p^m}
 &=\beta^m(P_{W,\kappa^m})_*H_N,\\
(\rho_N+H_N)|_{W_2\in p^m}
 &=\beta^m(P_{W_2,\kappa^m})_*(\rho_N+H_N).
\end{aligned}}
\tag{15}
$$
三个态、三个轴各自配对，不能将 (15) 改成其中一个态在所有轴上
具有同一个标量核。所有另外五个伙伴都在原完整核心中保留。

## 6. 不变性不消掉第四输入或 cd 移动门

原 x 在 (2) 中的三个系数是
$$
C_x=F_x=1/\delta,\qquad G_x=(32+31\omega)/3.
$$
所以一般 $q_N^*$ 仍真正依赖 x；
$C^4F^8,C^5F^6G$ 也没有提供一个“可直接忘 x”的理由。

其次，$\mathcal T$ 虽固定 d，却将 c 变成
$$
c_1=c\circ\mathcal T
=\frac{-\omega\xi_1+\xi_3-\omega^2x-\omega c}{2}.
\tag{16}
$$
故原 $\mathsf{CD}_N=\{c,d\in p^N\}$ 的真实逆像为
$\{c_1,d\in p^N\}$，一般不同。
R715 的 $\Phi_N$ 是对这个指定 cd 域完整返回、并保原两个 C
补项后得到的权。因此 (10) **不**给
$\Phi_N\circ\mathcal T=\Phi_N$。
如果后续继续在返回坐标使用 $\mathcal T$，
必须重新运输该 cd 域和完整正交返回，而不是沿用 (10) 的符号。

原所有 E 浅门、参考、T 外部和 Mellin 质量继续保留。
本注支付的是 (10)–(15) 的同一实际权身份；
原两个外部项是否能据此得到新的独立中央关系，
仍须计算其真实域和完整观察。

## 依赖与执行范围

- [R493](../results/R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)，
  原三阶矩阵、完整相位、两态与 scalar 轴。
- [R536](../results/R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)，
  式(39)–(44)的原 C/F/G 线性转置；本注把它精确扩到实际最终列。
- [R702](../results/R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)，
  式(13)–(18)的完整六支次数逆及所选 G/C 列。
- [R715](../results/R715-complete-first-z-source-and-fifty-neutral-returns.md)，
  实际50列、原两个测试与全部正规返回。
- [R734](../results/R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)，
  两条完整核修正、实际五阶逆和最终 $q_N^*$。

本注是已付完整测试的逐项代数推导，没有新增执行或可重算数据。

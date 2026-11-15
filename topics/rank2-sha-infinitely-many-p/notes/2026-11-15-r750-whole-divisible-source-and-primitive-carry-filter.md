# R750 增补：完整 F-整除来源、实际主部缺额和 primitive carry 筛

日期：2026-11-15。**状态：以下有限来源及实际原矩阵结论已证明；指定非零与主目标仍未完成。**

本篇保 R750 的同一个 $F,B,P_B=qt^rF\widetilde B$、整提升、
原 $M$ 和 $1\le\ell\le r\le13$。
先把 R750(41) 中整个 $\mathcal F_D$ 写成真实逐 charge 基，
再计算实际 $E'$ 主部像的准确维数。
最后用原两条十三行，而不是另换相对矩阵，
在任何可能的 primitive $p^2$ 提升前消掉指定 forcing 中的
$\mathscr B$ 尾。
实际 $\xi$ 和同一个 $R$ 全部保留。

## 1. 全 F-整除空间的准确原基

置
$$
\widehat{\mathcal W}_D=d^{C_D}\overline{\mathcal W}_D,\qquad
b=\deg_YF,\qquad c=C_D=\lfloor D/2\rfloor.
$$
R491 的原 Gauss 双向识别是：对多项式 $\widehat P$，
$\widehat P\in\widehat{\mathcal W}_D$ 当且仅当
$$
\deg_Y\widehat P\le D,\quad
v_\alpha(\widehat P)\ge-2\quad(\alpha=0,h_{7,1},h_{7,2}),
$$
$$
v_1(\widehat P)\ge-1,\qquad
v_d(\widehat P)\ge2c,\qquad
v_\infty(\widehat P)\ge-2c-8.
\tag{1}
$$
这些就是全部原角帽；不是只有一份矩形次数界。

原不可约 $F$ 不等于 $d$。因此
$$
\mathcal F_D=\{R\in\overline{\mathcal W}_D:R|_C=0\}
$$
准确由 $d^cR=FH$ 给出。
Gauss 赋值对乘积严格相加。
定义六个实际整数
$$
\lambda_\alpha=-2-v_\alpha(F)\quad
(\alpha=0,h_{7,1},h_{7,2}),\qquad
\lambda_1=-1-v_1(F),
$$
$$
\lambda_d=2c-v_d(F),\qquad
\lambda_\infty=-2c-8-v_\infty(F).
\tag{2}
$$
对每个 $0\le i\le D-b$，令
$$
m_{\alpha,i}=\max\left(0,\left\lceil\frac{i+\lambda_\alpha}{4}\right\rceil\right),
\quad
m_{1,i}=\max\left(0,\left\lceil\frac{i+\lambda_1}{3}\right\rceil\right),
$$
$$
m_{d,i}=\max\left(0,\left\lceil\frac{\lambda_d-i}{2}\right\rceil\right),
\qquad
v_i=\left\lfloor\frac{9i-\lambda_\infty}{2}\right\rfloor,
$$
$$
a_i(t)=
t^{m_{0,i}}
(t-h_{7,1})^{m_{h_{7,1},i}}
(t-h_{7,2})^{m_{h_{7,2},i}}
(t-1)^{m_{1,i}}d^{m_{d,i}},
$$
$$
n_i=v_i-\deg a_i.
\tag{3}
$$
这里 $h_{7,1},h_{7,2}$ 表示 $h_7$ 的两个根，
不是另加的角点；原域不分裂时整个条件及其 Galois 稳定基下降。

**定理 1。** 完整原 $\mathcal F_D$ 的一个准确基是
$$
\boxed{
d^{-c}F\,Y^i a_i(t)t^j,\qquad
0\le i\le D-b,\quad0\le j\le n_i,
}
\tag{4}
$$
$n_i<0$ 时该组为空。特别
$$
\boxed{
f_D^{\rm div}:=\dim\mathcal F_D
=\sum_{i=0}^{D-b}\max(0,n_i+1).
}
\tag{5}
$$

**证明。** 因 $k[t,Y]$ 中 $F$ 不可约，
$R|_C=0$ 正好是 $F\mid d^cR$。
把 (1) 除去 $F$ 的 Gauss 值，
得到 $H$ 的六个界 (2)。
对 $H=\sum H_i(t)Y^i$，这些界逐系数等价于：

- 在三个四阶角的消失阶至少为 $m_{\alpha,i}$；
- 在 $t=1,d=0$ 的消失阶分别至少为 $m_{1,i},m_{d,i}$；
- $\deg H_i\le v_i$。

原角互异，故 $H_i=a_i A_i$，
且 $\deg A_i\le n_i$。这同时证明必要性、充分性和 (4) 的线性无关。
乘回同一个 $F$ 后满足全部 (1)，所以每条都是原实际列的线性组合。
没有补写自由 normal 值。证毕。

(4) 首先是原约化空间的准确基。
后续使用整提升时，可按原 canonical 自由格提升这些列；
其产生的 $p$ 倍差必须继续进入同一个 $R$。
若使用 R491 已付的同时角保持因子提升，才可把 (4) 按字面逐项整提升。
本定理不从约化因子分解自动推出另一个整格的饱和性。

## 2. 原整个 B_D 的 H1 消失，以及不能省掉的差类 H1

令
$$
N_D=\dim\overline{\mathcal W}_D
=\sum_{n=0}^D(e_{n+1}+1).
$$
对 $D\ge3$，R680 的准确十九角表给
$$
\boxed{-K_X\mathcal B_D=2D+15.}
\tag{6}
$$
同时
$$
\boxed{
N_D=1+\frac{\mathcal B_D^2+2D+15}{2}.
}
\tag{7}
$$

这里可直接给出整数恒等证明。
每条四步链的重数是总和 $D-2$ 的四项平衡分拆；
三步链是总和 $D-1$ 的三项平衡分拆；
两条两步链均为 $(c,c)$。
因此十九项总和为
$3(D-2)+(D-1)+4c=4D-7+4c$。
代入 $u_D=2c+4$ 的原规范公式，即得 (6)。

若 $Q_e(m)$ 为 $m$ 的 $e$ 项平衡分拆的平方和，
则逐层计数给
$$
Q_e(m)+m=2\sum_{j=1}^{m}\left\lceil j/e\right\rceil.
$$
于是
$$
2\sum_{n=0}^D A_n=Q_4(D-2)+D-2,\quad
2\sum_{n=0}^D B_n=Q_3(D-1)+D-1.
$$
另一方面
$$
f_n+C_n+1=5n+5-(n\bmod2).
$$
把这些式子代入 $N_D$，
再用 $D-2c\in\{0,1\}$，
便得 (7) 和 R680 的 $\mathcal B_D^2$ 完全相同的准确整数式；
不需要渐近舍去取整。

由于 $X$ 有理、$\mathcal B_D$ 有非零有效截面，
$H^2(X,\mathcal O_X(\mathcal B_D))=0$：
若 $K_X-\mathcal B_D$ 有截面，乘一个非零 $\mathcal B_D$ 截面
就给非零 $K_X$ 截面，矛盾。
Riemann–Roch 与 (7) 因而证明
$$
\boxed{H^1(X,\mathcal O_X(\mathcal B_D))=0.}
\tag{8}
$$
这是原完整整数表给出的特定消失，不是“nef 即消失”。

记 $\mathcal A=\mathcal B_D-C=2C+E$。
它有效，同理 $H^2(\mathcal O_X(\mathcal A))=0$。
定理1准确计算它的 $H^0$，所以
$$
\boxed{
\delta_C:=h^1(X,\mathcal O_X(\mathcal B_D-C))
=f_D^{\rm div}
-1-\frac{(\mathcal B_D-C)^2-K_X(\mathcal B_D-C)}2.
}
\tag{9}
$$
右侧是由全部原角数据决定的非负整数。
不把它未经计算置零。

也可按根端所指出的准确序列
$$
0\to\mathcal O_X(2C)\to\mathcal O_X(2C+E)
\to\mathcal O_E(2C+E)\to0
$$
和 R495 的 $H^1(2C)=H^2(2C)=0$，
识别
$$
H^1(X,\mathcal O_X(\mathcal B_D-C))
\simeq H^1(E,\mathcal O_E(\mathcal B_D-C)).
\tag{10}
$$
$E$ 的全部实际分量、重数与交点都须保留。
(9) 则给无需假设这些分量分别消失的精确计算。

## 3. R750 实际主部像的准确维数与完整性判据

沿用
$$
E|_C=rP+E',\quad
e'=\deg E'=\mathcal B_D\cdot C-3\kappa-r,
$$
$$
\mathcal U_D\subset H^0(C,N^3(E')),\qquad
\mathcal V_{E'}=\operatorname{pp}_{E'}(\mathcal U_D).
$$
R750 的低 $r$ 个原列给整直和，故
$$
\dim\mathcal U_D=N_D-r-f_D^{\rm div}.
$$
R495 给 $H^1(C,N^3)=0$，
所以 $h^0(C,N^3)=(5\kappa+\chi)/2$。
R750 的准确主部序列因此成为
$$
\boxed{
\dim\mathcal V_{E'}
=N_D-r-f_D^{\rm div}-\frac{5\kappa+\chi}{2}
=e'-\delta_C.
}
\tag{11}
$$
第二个等号也直接来自 (8) 及
$0\to\mathcal O_X(\mathcal B_D-C)\to
\mathcal O_X(\mathcal B_D)\to\mathcal O_C(\mathcal B_D)\to0$。
原 $P$ 的低 $r$ 段已满射，所以施加其消失条件不改变此余核。

**推论 2。** 实际主部像是完整主部空间，当且仅当 (9) 的
$\delta_C=0$。此时
$$
\boxed{
\mathcal U_D=H^0(C,N^3(E')),\quad
\mathcal L_D^{\rm val}
=H^0(C,\omega_C N^{-3}(-E'+TP)).
}
\tag{12}
$$

证明是 (11) 与 R750(26)；
主部全满后，(32) 的残数条件正好要求对偶微分沿整个 Cartier
$E'$ 消去允许的所有极部。
它包含奇点及非约化结构，不能只在 $E'$ 的约化支撑上测试。

若 $\delta_C>0$，则仍使用 R750 的真实主部矩阵，
不是任取一个同维子空间。
在全部原情况下，R750(38) 可精确加强为
$$
\boxed{
\max(0,w_T-e'+\delta_C)\le
\dim\mathcal L_D^{\rm val}\le w_T.
}
\tag{13}
$$
本篇没有由 (9) 或 (13) 得出指定 $\Omega_B$ 非零。

定理1同时把 R750(41)、(44) 中的整个 $\mathcal F_D$
换成了显示的原列 (4)。
这些列的 normal 和下一位仍由同一实际评价读取；
不将它们的曲线值为零误作物理值为零。

## 4. 原两十三行首先迫真正 J 首核

保 R750 的
$$
T_M=s-r-13=2h-k-13,\qquad
T_J=s-r=T_M+13=2h-k,
$$
$$
\eta_0=t^hu,\qquad
\mathscr B=B_0+2\eta_0B_1,\qquad
\operatorname{ord}\mathscr B\ge T_M,
$$
$$
\operatorname{ord}B_0=h+\rho,\qquad
\operatorname{ord}B_1=\rho.
\tag{14}
$$
在同一原相对 $J$ 的约化里，直接展开给
$$
\boxed{
\bar J_0(P_B)=0,\qquad
\bar J_1(P_B)=
a\,t^r q_0e\,\mathscr B\pmod{t^s},\qquad
\bar J_2(P_B)=0.
}
\tag{15}
$$
这里不把 $J(P_B)/p$ 预先认成整向量。

证明如下。普通值的首阶为
$r+2h+\rho=s+k+\rho\ge s$。
Euler 值的最低部分是
$t^r q_0e(B_0+2\eta_0B_1)$；
所有其余项含 $\eta_0B_0$ 或 $\eta_0^2$，
乘 $t^r$ 后从 $s+k$ 或更高起。
第三块仍带原 $t^r$，
因 $r\ge\ell$ 在原相对第三块中消失。
模 $p$ 的普通高值进位带额外 $p$，不另贡献于 (15)。

原 $M$ 的两条十三行是真正的
$\operatorname{diag}(1,p)$ 行缩放。
R449(9) 因而给
$$
M(P_B+pR)\in p^2
\quad\Longrightarrow\quad
P_B\bmod p\in\ker\bar J.
$$
结合 (15)，得到准确必要门
$$
\boxed{
\operatorname{ord}\mathscr B\ge T_J.
}
\tag{16}
$$
这不是对 $R$ 加的任意新规范。

更具体地，第一条 carry 带已经由 (15) 的普通值消失自动通过；
第二条 carry 带由
$$
[t^{T_M}],\ldots,[t^{T_M+12}]\ \mathscr B
$$
经 $a q_0e$ 及原 $t/w$ 的整三角单位变换读取。
如果这十三个数中有非零者，
原 $P_B$ 的 primitive $p^2$ 提升已经被完整 $M$ 排除，
任何同预算 $R$ 都不能把该外带改掉。
若它们全零，才继续真正的可见 forcing 判定。
没有把“未计算的十三个数”说成非零。

## 5. 通过原 carry 后的实际 xi 配对

一旦 (16) 成立，R750 的完整值 forcing 不再含独立的
$\mathscr B$ 尾，因为
$$
\operatorname{ord}(t^{k-r}u^2\mathscr B)
\ge T_M+13-(r-k)\ge T_M
$$
使用的是原 $r-k\le13$。
于是其归一值条件准确简化成
$$
\boxed{
f_B=
-eB_0\left(
\xi-\frac{b_s}{2a}t^{k-r}u^2
\right)\pmod{t^{T_M}}.
}
\tag{17}
$$
括号是允许有限极点的同一个局部表达，
其乘积因 $\operatorname{ord}B_0=h+\rho$ 而仍正则。
这里没有把实际 $\xi$ 改为零，也没有丢掉 $b_s$ 的原高尾。

若写
$$
\Xi_B=\xi-\frac{b_s}{2a}t^{k-r}u^2,
$$
则真正杀全原像的值行必须满足的指定条件是
$$
\boxed{
\operatorname{Res}_P(eB_0\Xi_B\,\omega)=0
\quad(\omega\in\mathcal L_D^{\rm val}).
}
\tag{18}
$$
$\mathcal L_D^{\rm val}$ 仍是 R750 的同一个真实空间；
满足 (12) 的范围才可用其更简洁的完整线束描述。

(16) 之前须使用 R750 的全部原式。
(16) 之后的 (17)、(18) 则是由原两十三行迫出的实际加强，
不是主动改变原 $P_B$、其基准或第一次修正。
通过 (18) 后，还必须在 R750(43)、(44) 的同一来源纤维中处理
所有 normal 行、第三块和真正下一位。
特别，R449 对 primitive $p^3$ 的更强要求是
$P_B\bmod p\in K_2^{\rm red}(J)$；
(16) 只是首核门，不能替代那条完整相对提升。

本篇未证明 (16) 或 (18) 对实际候选必失败；
它把完整原来源和第一 carry 的可计算条件付清，
剩余非零继续取决于实际 $\xi$、原全值左行及同一个 $R$。

依赖：[R449](../results/R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)；
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R680](../results/R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[R741](../results/R741-specified-noncubic-first-forcing-and-necessary-normal-smoothing.md)；
[R750](../results/R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)。

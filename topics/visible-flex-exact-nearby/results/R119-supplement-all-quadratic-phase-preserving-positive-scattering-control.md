# R119：所有对称平方态的真实控制与完整散射的正定方向

2026-11-14，visible-exact / root。

**状态：已证明；32项新的精确门实际全部通过。** 在每个真正未使用的小区间，同一个紧支度量方向
可以使完整二维径向散射的 phase generator 正定。
它保持原两个 phase，且对该区间之外的所有允许控制统一有效。
证明使用全部对称二次型；它比只对某个共振实解给一个非零导数更强。

此处尚未选择全部频率的公共参数，也未反演非径向混模网络。
完整 mean、真实 weak/ordinary 源及外接口仍按已有合同保留。

## 1. 同一实际小区间及所有二次型

沿用
[未用短支集控制](R119-supplement-unused-short-interval-radial-control-and-width.md)
的真实 $j\ge8193$、$\delta,a,\Delta,B,K_j,T,I_n,c_n,L_n$：
\[
 \delta=(2/25)2^{-j},\quad a=\delta^{3/2}/(8\sqrt6),\quad
 B=\Delta/a,\quad K_j=2^{6000}(j+5)^8\delta^{-16},
\]
\[
 \lambda=M^2,\quad M\ge4,\quad
 T=1+\Delta+1+M\sqrt{a(1+\Delta)} .
 \tag{P.1}
\]
$L=L_n\ge13$，$dt=a\,dx$，所有已有控制在 $I_n$ 之外。
区间外 compact 控制的总 $C^4$ norm 取在 $2^{-65}$ 内；加入本篇所有 band 后仍严格在原 $2^{-64}$ 补偿球内。
该区间准确仍为
\[
 Q=7+30Bx^2(1-x)^2,\qquad \mu_t/\mu=-1-Q .
 \tag{P.2}
\]
它之外可为原完整受控 $C^4$ profile，无需解析。

取两条真实基本解 $h_1,h_2$，在 $c=c_n$ 使 wave fundamental matrix
为单位阵：
\[
 Y=(\sqrt k\,\sqrt\mu h,\,
             (\sqrt\mu h)_t/\sqrt k),\qquad
 k=\sqrt{7\lambda-16}.
 \tag{P.3}
\]
归一化的是局部中心的真正 canonical wave state。
常数 $\mu(c)$ 在 $\sqrt\mu h$ 中准确消去；不固定一个会随外部控制
改变的 raw 高度。

对任意实 $A=A^T$，定义对称平方协方差
\[
 \begin{pmatrix}X&Y_b\\Y_b&Z\end{pmatrix}
 =\mu
 \begin{pmatrix}h_1&h_2\\(h_1)_t&(h_2)_t\end{pmatrix}
 A
 \begin{pmatrix}h_1&h_2\\(h_1)_t&(h_2)_t\end{pmatrix}^{T},
\]
\[
 \mathcal K_A=Z-2\lambda Y_b+\lambda X .
 \tag{P.4}
\]
$A$ 可不定，不能使用 $X,Z\ge0$。
若 $A=vv^T$，(P.4) 才还原原实解 $h=v_1h_1+v_2h_2$ 的 kernel。

## 2. 无需正能量的完整三 jet 可观测性

令 $s=1+Q$、$b=2\lambda(\lambda-1)$。
真实对称平方方程准确为
\[
 X_t=-sX+2Y_b,\quad (Y_b)_t=Z-\lambda QX,\quad
 Z_t=sZ-2\lambda QY_b.
 \tag{P.5}
\]
逐项微分给
\[
 (\mathcal K_A)_t=(s-2\lambda)\mathcal K_A-bX_t,
\]
\[
 \boxed{\quad
 (\mathcal K_A)_{tt}+
 [4\lambda Q-s^2-Q_t]\mathcal K_A=bQ_t X .
 \quad}                                                    \tag{P.6}
\]
这是所有 $A$ 的恒等式，包含不定二次型。
若 kernel 恒为零，第一式给 $X_t=0$，第二式和 $Q_t\ne0$ 给
$X=0$，再由 (P.5) 得全部协方差为零。因此映射 $A\mapsto\mathcal K_A$
准确单射；仅仅对 rank-one 态非恒零本来不足以得此结论。

现在量化。在所有保留区间的中心
$113/256\le c\le114/256$，准确有
\[
 B<Q(c)<9B,\qquad B<Q_x(c)<2B,\qquad s(c)<10B .
 \tag{P.7}
\]
从 wave state 到 $(\sqrt\mu h,\sqrt\mu h_t)$ 的真实矩阵是
\[
 R=\begin{pmatrix}k^{-1/2}&0\\
                  s/(2\sqrt k)&\sqrt k\end{pmatrix},
 \quad\det R=1,\quad
 \|R\|^2,\|R^{-1}\|^2\le16B^2\lambda .
 \tag{P.8}
\]
例如 $2\sqrt\lambda<k<3\sqrt\lambda$，其 Frobenius 平方
至多 $3M+13B^2/M\le16B^2\lambda$。

若 $\|A\|_F=1$，(P.8) 给
\[
 \max(|X(c)|,|Y_b(c)|,|Z(c)|)
          \ge(32B^2\lambda K_j^2)^{-1}.
 \tag{P.9}
\]
这里额外 $K_j^{-2}\le1$ 只是向下放宽，适合统一沿用先前常数；
因本篇在 $c$ 归一，本来无需支付它。

记 $\kappa=\sup_{|x-c|\le1}|\mathcal K_A|$，使用真实局部 quartic
的唯一 entire continuation。Cauchy 给
$|\mathcal K_t|\le\kappa/a$、$|\mathcal K_{tt}|\le2\kappa/a^2$。
由 (P.6)、$b\ge\lambda^2$ 及 (P.7)，依次得到
\[
 |X(c)|<2^8a^{-1}B\kappa,\quad
 |X_t(c)|<13a^{-1}B\kappa,
\]
\[
 |Y_b(c)|<2^{11}a^{-1}B^2\kappa,\quad
 |Z(c)|<2^{12}a^{-1}\lambda B^2\kappa.
\]
例如第一行的未取整系数为
$2/(a\lambda^2B)+36a/\lambda+100aB/\lambda^2+2/\lambda^2$，
至多 $140B/a$；其余来自
$2Y_b=X_t+sX$、$Z=\mathcal K_A+\lambda X_t+\lambda QX$。
与 (P.9) 比较，保守得
\[
 \boxed{\quad
 \kappa\ge2^{-20}aB^{-4}\lambda^{-2}K_j^{-2}.
 \quad}                                                    \tag{P.10}
\]
没有假设 $h$ 无零点或某个单独 jet 非零。

## 3. 同一短支集 separation 常数覆盖全部 Sym2

对 $\|A\|_F=1$ 作实正交谱分解，其两个特征值绝对值之和小于2。
原完整平衡复增长因此给
\[
 \|\mathcal K_A\|_{|x-c|\le1024}
 \le\mathcal M:=2^{12}\lambda a^{-2}K_j^2e^{2^{60}T}.
 \tag{P.11}
\]
这只把原 rank-one 的 $2^{10}$ 放宽到 $2^{12}$。
它仍是局部 quartic continuation，不将全 profile 延拓为 quartic。

短区间传播公式 S.6 对 $\mathcal K_A$ 使用 (P.10)，得
\[
 \|\mathcal K_A\|_{I_n}
 \ge2^{-24L}a^LB^{-4L}\lambda^{-2L}K_j^{-2L}
                       \mathcal M^{1-L}.
 \tag{P.12}
\]
其余复根、全部20维 Hermite、平方的九 jet 和
$F=Q^9\mathcal K_A^2-P^2$ 的证明逐字适用，未使用 positivity。
在 S.9 后的新二进制费用只是
\[
             1792L^2+9088L-12<4096L^2\qquad(L\ge13).
\]
全部 $a,B,\lambda,K$ 幂及指数仍由原保守值覆盖。因此
\[
 \operatorname{dist}_{L^\infty(I_n)}
   (\mathcal K_A,\{P/Q^{9/2}:\deg P\le19\})\ge\epsilon_L,
\]
\[
 \epsilon_L=
 2^{-4096L^2}a^{96L^2}B^{-192L^2}
       \lambda^{-96L^2}K_j^{-128L^2}e^{-2^{65}L^2T}.
 \tag{P.13}
\]

完全相同的真实紧支 $C^9$ bump construction 于是给某个
$\psi_A$，满足
\[
 \|\psi_A\|_{C_x^4}:=\sum_{q=0}^4\|\partial_x^q\psi_A\|_\infty\le1,
 \quad \int(P/Q^{9/2})\psi_A\,dx=0\quad(\deg P\le19),
\]
\[
 \int\mathcal K_A\psi_A\,dt\ge d,\qquad
 d=\left[
 2^{-2^{17}}a^{2560}B^{-5120}\lambda^{-2560}K_j^{-3456}
                       e^{-2^{70}T}\right]^{L^2}.
 \tag{P.14}
\]
已把 $\psi_A$ 的号选成正。
这里不除右端 resonant amplitude；不需要存在任何共振。
直接 pairing 的未取整费用是
$26\cdot4096L^2+4436$，
其 $a,B,\lambda,K$ 幂为
$2496L^2+51,4992L^2+130,2496L^2+25,3328L^2+50$，
仍严格落在 (P.14) 内。

(P.14) 的 $d$ 正是原 S.13 所用保守数。
所以在它所属的实际中频 band 及 $L_n\le j+5$ 时，原完整角宽账
继续给
\[
                         -\log d<2^{-803}Mh_j,
 \qquad h_j=8\delta_j^{1/256}.
 \tag{P.15}
\]
所有原 $\zeta,h_j$ 和低频源权不变。

## 4. 一个方向同时控制全部二维态

定义线性映射 $\mathcal L\psi\in{\rm Sym}(2,\mathbb R)$，使
\[
 \operatorname{tr}(A\mathcal L\psi)
                 =\int\mathcal K_A\psi\,dt .
 \tag{P.16}
\]
取单位 $C^4$、紧支于 $I_n$、消去全部19次 phase 多项式的方向集合。
它关于取负对称且凸；有限相加仍为 $C^9$ 紧支。
(P.14) 证明其像在每个 Frobenius 单位方向的 support function
至少为 $d$。

这里可用有限构造，不必假定无限维单位球像为闭集。
实际实 Cauchy 界及 (P.8) 给
\[
                     \|\mathcal L\psi\|_F\le
 L_*:=2^{10}B^2\lambda^2K_j^2 .                         \tag{P.17}
\]
取 Sym2 单位球面的 $\varepsilon=d/(4L_*)$ 有限网。
最大分离网的点数至多 $(1+2/\varepsilon)^3$。
每个网点各取 (P.14) 的一个方向，连同其负方向组成有限集合。
任意单位 $A$ 的 support function 至少 $d-\varepsilon L_*=3d/4$。
有限凸包因而包含半径 $3d/4$ 的 Frobenius 球。

特别 $(d/4)I$ 在该球内。三维有限凸包定理给至多四个顶点的
凸组合，其对应的真实 compact 方向 $\psi$ 满足
\[
 \boxed{\quad
 \|\psi\|_{C_x^4}\le1,\qquad
 \mathcal L\psi=(d/4)I .
 \quad}                                                    \tag{P.18}
\]
仍有全部 phase annihilator 精确为零。
这里的有限存在构造未冒称已数值求出网格或凸系数。

最重要的是，(P.3) 在 $I_n$ 中心归一，(P.2) 在该区间准确固定。
因此 $\psi$ 只依赖该局部实际 quartic、频率和区间；
它不依赖任一区间外解的左/右边界线。
其它所有允许控制、包括其它保留区间的控制，可同时存在。
只要当前 $I_n$ 仍未使用，同一个 (P.18) 对全部这些外部 profile
保持成立。原两 bump 的补偿一阶准确为零（第54束 H.17）。

## 5. 完整复杂 incoming 空间上的正定 generator

取完整负窗的真实酉散射 $S$，端口约定与
[完整径向网络](R119-supplement-complete-radial-unitary-network-and-global-eigenphase.md)
相同。对任意复杂 incoming $x=(a_L,b_R)$，完整变分 Green 恒等式给
\[
 x^*(-iS^*DS[\psi])x
       =\int\mathcal K_h\psi\,dt
       =(d/4)\|Y(c)\|^2 .
 \tag{P.19}
\]
复杂解由实部和虚部的二次型相加读取；不能只证实 incoming 实子空间。

真实双向传递界给
$\|x\|^2\le\|Y_L\|^2+\|Y_R\|^2\le2K_j^2\|Y(c)\|^2$。
故
\[
 \boxed{\quad -iS^*DS[\psi]\ge\frac d{8K_j^2}I .\quad} \tag{P.20}
\]
该式对所有 incoming 状态成立，无需当前 eigenphase 简单，
也不需要它已在1附近。

## 6. 实际有限 band 盒内的统一正定性

这里只对矩阵本身求导，不对单个 eigenphase 二次求导。
在真实固定端口，若 $A_C$、$H_C$ 分别界住完整 $DC,D^2C$，
准确 quotient (U.4) 及 $|\alpha|\ge1$ 给
\[
 \|DS\|\le4A_C,\qquad
 \|D^2S\|\le4H_C+16A_C^2,
\]
\[
 \|D(-iS^*DS[\psi])\|\le4H_C+32A_C^2 .
 \tag{P.21}
\]
所有导数包括真实两 bump 补偿。
第54束的
$A_C=2K_j^2(M+B/M)$、
$H_C=2^{22}K_j^3(M+B/M)^2$
因此被下列统一数覆盖：
\[
 H_G=2^{30}K_j^4(U+B)^2\quad(M\le U,\ M\ge4).
 \tag{P.22}
\]

固定一个实际 dyadic band，其物理频率均在 $[U/2,U]$，
保留编号为 $n$，频率数为 $N\le U$。
以 (P.14) 在 $M=U$ 的数为共同 $d$；所有较小频率的下界不差。
为每个实际频率选 (P.18) 的局部方向 $\psi_m$。
同一窗口该 band 的真实控制为
\[
 \Xi^{(n)}=\frac rN\sum_{m\ {\rm in\ band}}\theta_m\psi_m,
 \quad|\theta_m|\le1,
\]
\[
 r=\min\left(2^{-n-80},
          \frac d{2^{36}K_j^6(U+B)^2}\right).
 \tag{P.23}
\]
它的完整 $C^4$ norm 至多 $r$。
沿把这个 band 的全部控制归零、保持其它区间的控制固定的线段，
(P.22) 给误差至多 $d/(64K_j^2)$。
所以整个盒上、对该 band 每个 $m$，
\[
 -iS_m^*D_{\theta_m}S_m
       \ge D_{j,m}I,\qquad
 D_{j,m}=\frac{rd}{16NK_j^2}>0 ,
\]
\[
 \|D_{\theta_m}S_m\|<2^{-33}/N .
 \tag{P.24}
\]
这两个界对所有其它保留区间的允许控制统一成立；
不需要先选完它们再逐一保护旧 gap。
若对无限 band 使用 (P.23)，其 $C^4$ 总和小于 $2^{-79}$，
严格留在真实 $2^{-64}$ 补偿域内。

对实际中频 band，$n+1<2^{10}(j+5)$、$L_n\le j+5$；
$U$ 至多是当前 $M$ 的两倍。记 $J=j+5$。
由 (P.23)，
\[
 -\log D_{j,m}
 \le2(-\log d)+(n+120)\log2+\log N+8\log K_j+2\log(U+B).
\]
后五项小于 $2^{13}J$，而真实 $M\ge2^{-40}\delta^{-1/8}$ 给
\[
 \frac{2^{13}J}{Mh_j}
 <2^{50-61j/512}<2^{-803}\qquad(j\ge8193).
\]
结合 $-\log d<2^{-803}Uh_j$ 得
\[
                    \boxed{D_{j,m}>e^{-2^{-800}Mh_j}.} \tag{P.25}
\]
原小宽度足以支付完整矩阵正定性和有限盒，未改 source 权。

## 7. 精确范围与继续入口

(P.24) 已是完整二维 complex incoming 的矩阵不等式。
若在一个固定频率的完整网络中，同时沿此频率的坐标改变它的
全部 retained middle windows，而真实左/右允许线和正段对该坐标
固定，则完整 $U=P\bigoplus S_j$ 的 generator 下界是
$\operatorname{diag}(D_{j,m}I_2)$。
其它频率坐标可以改变这些外线；条件求导时它们固定即可。

这为没有邻谱间距假设的 monotone spectral averaging 提供了真实
入口。公共无限参数、good-$t$ 产品选择、全部 weak/ordinary
source 的原加权接线、非径向真实 principal 端图和最终全
$\mathcal F=0$ 仍须继续。没有用径向正定变分宣称非径向矩阵已逆。


## 8. 实际精确执行

源码：[fourfold_all_quadratic_positive_scattering_control.mjs](../scripts/fourfold_all_quadratic_positive_scattering_control.mjs)。
原生报告：[2026-11-14-R119-all-quadratic-positive-scattering-control-rational.json](../notes/2026-11-14-R119-all-quadratic-positive-scattering-control-rational.json)。
完整纯算术函数在V8中执行，32项全部通过。前三阶对称平方式按自由变量的BigInt多项式恒等验证，未采样解、频率或参数。
其余门按有理数核全部新复增长、短支集、凸包、complex incoming归一、真实完整Hessian及whole-layer角宽余量。
源码SHA256：2fbdb150527d4b8f751e1bd79e867bd3eef4d398cfcd03f8d3223a26c7670857。

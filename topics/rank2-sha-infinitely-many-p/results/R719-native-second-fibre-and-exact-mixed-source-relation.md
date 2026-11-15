# R719 — 原二阶纤维的特征零混合关系与真实深浅补偿

日期：2026-11-15。**状态：已证明。**

本文对 R715 的同一个原测试证明固定特征零关系：原二阶规范
$\mathfrak j_2$ 由两冻结、cd-Y、native-W 和五阶以内的完整 Z
混合来源读取。在真实 $\lambda,\kappa,u$ 参数下，边界身份留下显示的
$\kappa,u$ 修正；没有把它们删掉。

因此，保持 R715 已适配正规来源及 $\mathfrak j_2=1$ 时，
第二至第五 Z 来源的一个固定组合为单位。它们不能同时为零而仍保整系数。
本篇在 $\mathbf Q(\omega)$ 验证完整有限身份及其参数次数界，
不把辅助模数的不相容提升成特征零无解。
新混合行支付原 Y-unit 域上的真实 E 深/浅补偿，但仍不代替原条件负矩。

## 1. 同一来源、完整参数与五阶混合来源

保 [R715](R715-complete-first-z-source-and-fifty-neutral-returns.md) 的规范：
$$
\begin{gathered}
K=\mathbf Q(\omega),\quad\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\\
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0},\quad u=\kappa^N,\\
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
b_Y=(20+3\omega)/17,\quad Z=W-b_YY .
\end{gathered}
\tag{1}
$$
原 $\mu_0$ 已含 $-1/84$，其 Y、W 边际为 S、$6\delta T$。
$\rho_{cd,N}(P)$ 总是 R715(3) 的完整 cd 来源：
两条 C 分支、整个 E 单位逆、最高三十次权及每块
$b^{d/6}\Omega^d$ 归一全部保持。

定义
$$
F_k(P)(z)=\Omega^{-k}\int Z^k e^{Yz/\Omega}\,
                            d\rho_{cd,N}(P),\qquad1\le k\le5 .
\tag{2}
$$
因 $Z\perp Y$，它属于整个 $\mathcal S_{34}$ 的角型 $-k$。
完整基所需的首阶为：

| k | 实际首阶 r | 维数 |
|---|---|---:|
| 1 | 5,11,17,23,29 | 5 |
| 2 | 4,10,16,22,28,34 | 6 |
| 3 | 3,9,15,21,27 | 5 |
| 4 | 2,8,14,20,26,32 | 6 |
| 5 | 1,7,13,19,25,31 | 6 |

r 偶时基为 $\sigma^{34}x^{(34-r)/2}$；
r 奇时为 $-\sigma^{34}x^{(31-r)/2}y$，首系数均一。
不存在单极函数，故 r=33 不是 k=3 的新基向量。
所列 jet 经固定单位三角矩阵恢复全来源，不以质量代替这些行。

记
$$
\boxed{
v_{r,k}(P)=b^{\,1-(r+k)/6}[z^r]F_k(P)(z)
=\frac{b^{\,1-(r+k)/6}}{r!\Omega^{r+k}}
       \int Y^rZ^k\,d\rho_{cd,N}(P).
}
\tag{3}
$$
表中 $r+k$ 均为6的倍数。k=0 时用相同规范读取两冻结、
cd-Y 与 native-W。该 b 幂来自
$\sigma_b(z)=\theta^{-1}\sigma_1(\theta z)$、$\theta^6=b$，
以及原每个权块的完整归一；未另选 p 依赖周期。

## 2. 真实149列与固定52行

使用 R702/R715 原算法的同一中性家族，列号从零起：

- R594 的11条完整九行零核差乘 $G^{6h}$，$0\le h\le4$，共55列；
- 同11条差乘实际 $B_0^6G^{6h}$，$0\le h\le3$，共44列；
- 原 $C^iF^jG^{12-i-j}$，$1\le i\le5,\ 0\le j\le12-i$，共50列。

各块保实际周期规范。B 列在 E 单位逆的全分支与 C-zero 分支中
分别运输，不把前一分支的 $B^\perp$ 免费置成 E=0。
R715 的五十条实际选列在此家族内，本身未使用 B 列。

原六次列由
$$
\Pi_p=I-\mathsf B(\tau)[A_p\mathsf B(\tau)]^{-1}A_p,\qquad
\tau=(1+\lambda)^{-1}
\tag{4}
$$
生成；$A_p$ 是 R594 完整九行。在 $\kappa=u=0$ 边界，
$$
\Pi(\tau)=I-\mathsf B(\tau)A(\tau),\quad
A(\tau)=A_++\tau A_0,\quad
\mathsf B(\tau)=\frac{\mathsf B_0+\tau\mathsf B_1}{\tau-1}.
\tag{5}
$$
原仿射基准权按同一右逆返回。所有列的 $\pi_4$ 中性已有来源级证明。

按下列次序组成52行向量 $\mathbf v(P)$，全按 (3) 归一：
$$
\boxed{
\begin{array}{ll}
0,\ldots,5:&\mathscr U_0,\quad r=0,6,\ldots,30,\\
6,\ldots,11:&\mathscr U_1,\quad r=0,6,\ldots,30,\\
12,\ldots,17:&Y_*\rho_{cd,N},\quad r=0,6,\ldots,30,\\
18,\ldots,23:&W_*\rho_{cd,N},\quad r=6,12,\ldots,36,\\
24,\ldots,51:&\text{表中28条混合行，按 k、r 递增。}
\end{array}}
\tag{6}
$$
第二冻结保原 $\mathsf J$ 转置的符号；本篇不用四挠数值生成器。

令 $M_0(\tau,\eta)$ 为52行在149列上的边界矩阵，
$j_0(\tau,\eta)$ 为相同列的原 $\mathfrak j_2$ 行；
$\eta=\pm1$ 是原 C 核实际符号。固定52列为
$$
\boxed{
\begin{gathered}
0,1,\ldots,22,\quad25,26,\quad36,37,\quad47,48,\\
104,\ldots,110,\quad116,\ldots,121,\quad
127,\ldots,131,\quad137,\ldots,140,\quad147 .
\end{gathered}}
\tag{7}
$$
$D=M_0(2,1)_{(7)}$ 是可逆的固定 K 矩阵。定义
$$
\boxed{c=j_0(2,1)_{(7)}D^{-1}\in K^{52}.}
\tag{8}
$$
这是 c 的完整定义，不含 p、N、$\lambda,\kappa,u$ 或任何未知负矩。
脚本从原 sigma 递推重建 D 与 j，不读数值表。

## 3. 完整特征零身份

**定理1。** 对整个边界家族及原仿射基准权，
$$
\boxed{\mathfrak j_{2,0}(P)=c\,\mathbf v_0(P)}
\tag{9}
$$
在 $K(\tau)$ 中对 $\eta=\pm1$ 都准确成立。

**证明。** 先支付有限计算的原来源与截断。以 $b=\Omega=1$ 使用
$$
x(z)=z^{-2}\sum_{n\ge0}x_nz^{6n},\quad x_0=1,\ x_1=-1/7,\qquad
x_n=\frac{\sum_{1\le j<n}x_jx_{n-j}}{(6n+1)(n-1)} ,
$$
$$
[z^{6n}]\log(\sigma(z)/z)=-\frac{x_n}{6n(6n-1)},\qquad
-y(z)z^3=1-\sum_{n\ge1}(3n-1)x_nz^{6n}.
\tag{10}
$$
原完整 C 分离为
$$
\nu_{B_C}\otimes\frac1{42}
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma^{\otimes3},
\quad
f_1=-xy\sigma^6,\ f_3=-y\sigma^6,\ \Sigma=\sigma^2,\ \Theta=x\sigma^2 .
\tag{11}
$$
整个 $B_C$ 的0至30阶保留。逐个 sigma 同时代入隐藏线性形式与
$Yz+Zv$；$v^k$ 系数乘 k! 才是 (2) 的 Z 矩，D/E/G 幂亦乘原阶乘。
最高隐藏次数30、最高观察总次数36，故原总次数至66足够，
并无数值近似。

在齐次级数 $F=F_0\exp(\sum L_n)$ 中，实际递推为
$$
F_n=\frac1n\sum_{j=1}^n jL_jF_{n-j}.
\tag{12}
$$
完整 C-zero 变换在截断前作用于原线性形式，
不丢掉之后会变成 G 幂的 E 项。
原 $\partial_D^2P$ 的四输入矩读取 $\mathfrak j_2$，同两条 C 分支也保持。

在 $\mathbf Q(\omega)$ 解 (8)，再逐项代入，公开执行准确得到
$$
cM_0(\tau,\eta)-j_0(\tau,\eta)=0
\tag{13}
$$
对 $\tau=2,3,4,5$、$\eta=1,-1$ 的全部149列成立。
同一 c 在八种情形的原仿射项余量也全零。
这是1200条特征零等式，不是从模1009结果作有理重构。

还须证明这组有限等式足够。由 (5)，乘 $\tau-1$ 后，
每个中性列及原仿射基准权的系数关于 $\tau$ 至多二次。
边界 E 单位逆与 C 分支准确作用为
$$
\mathcal L_{\tau,\eta}(P)=\mathcal L(P)+(\tau-1)
 \{\mathcal L(P|_{E_c=0})+\eta\mathcal L_0(P|_{E_c=0})\}.
\tag{14}
$$
因此 (13) 及其仿射余量乘 $\tau-1$ 后至多三次。
四个不同有理值的精确消失证明整个多项式恒零；
两种符号各自支付。这证明 (9)。证毕。

(8) 系数的可重算序列化长度为120983 bytes，按根规则不存输出文件。
其 SHA256 为
4a3303c26bfe0f0b86099a81c8fb19752dca5085c67d2edb4ac561a7d72fd8a0。
固定最小公共分母2076 bits，SHA256 为
b371f54e4a532108b1d333536d4d1800b94c679ed435d446873af0ac34f32f3d。
(8)、(10)–(14) 与脚本提供完整重建定义；hash 不替代恒等式证明。

## 4. 实际 lambda/kappa/u 的完整修正

将 $\mathbf x$ 作为149条原中性列的独立系数，
另以 $x_0=0$ 或1表示纯中性或原仿射家族。记完整实际行差
$$
T(L,K_0,U;\mathbf x)
=\mathfrak j_2(L,K_0,U;\mathbf x)
             -c\,\mathbf v(L,K_0,U;\mathbf x).
\tag{15}
$$
$(L,K_0,U)$ 是形式参数，最后才代 $(\lambda,\kappa,\kappa^N)$；
所有行使用 (4) 的实际逆、整个 E 次数和两条 C 分支。

清掉 (8) 与旧生成式的固定分母后，这些行在原单位分母局部环中整。
定理1给 $T(L,0,0;\mathbf x)=0$。明确取
$$
\begin{aligned}
R_\kappa&=
\frac{T(L,K_0,U;\mathbf x)-T(L,0,U;\mathbf x)}{K_0},\\
R_u&=
\frac{T(L,0,U;\mathbf x)-T(L,0,0;\mathbf x)}{U}.
\end{aligned}
\tag{16}
$$
分子含相应因子，(16) 是该整环中的真实有限线性算子，
没有先允许一个 p 分母再称它有界。
依 p、N 的实际系数在构造 (16) 后才代入。准确得到
$$
\boxed{
\mathfrak j_2(P)=c\,\mathbf v(P)+\kappa R_\kappa(P)+uR_u(P).
}
\tag{17}
$$
这保留实际修正，不把边界恒等式冒作全参数恒等式。

再删 (8) 公共分母及第5节固定非零常数的范数分子所含有限素数。
旧高幂射线、M3 和 R715 的相对密度一子族不变。
对实际整系数测试，$R_\kappa,R_u\in\mathcal O$，
所以修正属于 $p\mathcal O$，对全部正 N 四倍数同时成立。
这里不把 p 依赖的 Katz 负矩套入固定 CM 单位密度引理。

## 5. 两个原实际测试强迫的混合单位行

把 c 分成前24条正规行及后28条混合行。
对称目标的固定正规向量是
$$
v_{\rm reg}^{\rm sym}=
(\operatorname{jet}_{0:30}S,\operatorname{jet}_{0:30}S,
 \operatorname{jet}_{0:30}S,\operatorname{jet}_{6:36}(6\delta T)),
\tag{18}
$$
全按 (3) 归一。定义
$$
\Delta_{\rm sym}=1-c_{\rm reg}v_{\rm reg}^{\rm sym}\in K.
\tag{19}
$$
公开特征零执行准确计算了它；其在
$\mathbf F_{1009},\omega=374$ 的余式为400，分母可逆，所以
$$
\boxed{\Delta_{\rm sym}\ne0.}
\tag{20}
$$
这里有限模数只证明已精确定义的固定代数数非零，
没有用于提升矩阵不相容。

对 R715 的 $q_N^{(715)}$，正规来源为 (18)，
$\mathfrak j_2=1$、整个 $F_1=0$；
对 $\zeta_N^{(715)}$，正规来源零、$\mathfrak j_2=1$、整个 $F_1=0$。
(17) 准确给
$$
\boxed{
\begin{aligned}
\sum_{\substack{2\le k\le5\\r\ {\rm in\ table}}}c_{r,k}v_{r,k}
 &=\Delta_{\rm sym}-\kappa R_\kappa-uR_u
                    &&(q_N^{(715)}),\\
\sum_{\substack{2\le k\le5\\r\ {\rm in\ table}}}c_{r,k}v_{r,k}
 &=1-\kappa R_\kappa-uR_u
                    &&(\zeta_N^{(715)}).
\end{aligned}}
\tag{21}
$$
在固定坏集外，两行均为单位。
所以第二至第五个完整混合来源中至少一个有单位 theta 系数；
它们不能同时为零而保这些真实正规目标及整系数。

这只排除同149列家族内的整解。若允许 p 分母，
(17) 迫使至少一个列系数赋值不大于−1；
并没有证明全参数域上无解。
实际 generic rank 可能比边界 rank 大，(21) 不需要否认它。

## 6. 同一 Y-unit 域及 E 深/浅的真实补偿

R686 的全 Y 核与共同隐藏权给
$$
\rho_{cd,N}|_{Y\in p}
=\lambda(R_YP_{Y,\kappa})_*\rho_{cd,N}.
\tag{22}
$$
Z 及所有伙伴不动，因此
$$
\boxed{
v_{r,k}=
\frac{b^{\,1-(r+k)/6}}
 {r!\Omega^{r+k}(1-\lambda(-\kappa)^r)}
 \int_{Y\ {\rm unit}}Y^rZ^k\,d\rho_{cd,N}.
}
\tag{23}
$$
混合表中 r 全为正，分母均为单位。
于是有同一个原 Y-unit 域上的明确测试
$$
\Psi_p(Y,Z)=
\sum_{\substack{2\le k\le5\\r\ {\rm in\ table}}}
\frac{c_{r,k}b^{\,1-(r+k)/6}Y^rZ^k}
 {r!\Omega^{r+k}(1-\lambda(-\kappa)^r)} .
\tag{24}
$$
(21) 正是 $\int_{Y\ {\rm unit}}\Psi_p\,d\rho_{cd,N}$ 为单位。
它不是另换来源得到的独立单位见证。

同一原 $E=E_{YW}$ 的完整平面桥为
$$
\boxed{
(Y,Z)_*(1_{E\in p^N}q_N\mu_0)
=\lambda^{2N}\rho_{cd,N}^{YZ},
}
$$
$$
\boxed{
(Y,Z)_*(1_{E\notin p^N}q_N\mu_0)
=\lambda^N\mu_0^{YZ}-\lambda^{2N}\rho_{cd,N}^{YZ}.
}
\tag{25}
$$
对纯中性差，第二行第一项为零。
完整证明见
[双 S 斜轴 note](../notes/2026-11-15-two-adjacent-s-slanted-cores-and-native-pair.md)
第6节：比较同一 $\{Y,Z,E\in p^N\}$ 的 cd 返回与 Y/Z 矩形，
再约去真实单射推前。没有把边际身份直接升成联合身份。

将 (24) 原样代入，得到
$$
\begin{aligned}
\int_{\{E\in p^N,Y\ {\rm unit}\}}\Psi_pq_N\,d\mu_0
 &=\lambda^{2N}\int_{Y\ {\rm unit}}\Psi_p\,d\rho_{cd,N},\\
\int_{\{E\notin p^N,Y\ {\rm unit}\}}\Psi_pq_N\,d\mu_0
 &=\lambda^N\int_{Y\ {\rm unit}}\Psi_p\,d\mu_0
 -\lambda^{2N}\int_{Y\ {\rm unit}}\Psi_p\,d\rho_{cd,N}.
\end{aligned}
\tag{26}
$$
对 $\zeta_N^{(715)}$，两条真实深/浅行准确相反且均为单位。
这是原总行中必须保留的非零浅补偿，未给其中央赋零。

## 7. 与两斜门及原条件负矩的精确边界

原配对 native 行继续用
$$
L_1=34Y_1-29Y,\quad L_3=34Y_3-29Y,\quad
\ell=n-N,\quad t=\kappa^\ell .
$$
前述 note 在原全六输入证明
$$
\mu_0|_{L_i\in p^\ell}
=\lambda^\ell(R_Y^\ell P_{L_i,\kappa^\ell})_*\mu_0 .
\tag{27}
$$
两斜门已付完整核心，但它们改变原 q 的 E 多项式。
用该 note 的 $\phi_{i,N}(t),Z_i(t)$，
真实配对相对中央准确为
$$
\boxed{
d_p\lambda^{2n+2N}
\sum_{k\ge1}\frac{(-1)^{k+1}(-1)^{k\ell}u^k}{k b_Y^k}
\left\{
\int_{Y\ {\rm unit}}\phi_{1,N}(t)Z_1(t)^kY^{-k}\,d\mu_0
-
\int_{Y\ {\rm unit}}\phi_{3,N}(t)Z_3(t)^kY^{-k}\,d\mu_0
\right\}.
}
\tag{28}
$$
每个固定 k 的括号是次数至多 $30+k$ 的真实 t 多项式；
整个 k 尾、原 $1/k$ 分母及全部 C 分支保持。
配对 S 来源有准确的 $t(t-1)$ 因子；
(28) 的条件负矩目前只已付共同的 $t-1$ 因子。

(24) 的正 Y 次数不替换 (28) 的 $Y^{-k}$，
也不能把 $t=1$ 的 cd 来源零移到 $t=\kappa^\ell$ 的两个移位权。
新增实质是：原正规行不能整消所有低阶混合来源，
其强制部分已成为同源深/浅的明确单位补偿，
而两斜门也已返回同一个完整 Y-unit 域。
主目标剩余为 (28) 与原 T 外部的真实算术比较，
没有从一个子域单位值提前宣布原中央非零。

## 8. 公开执行与重建

完整算法：
[check-r719-exact-boundary-mixed-relation.py](../scripts/check-r719-exact-boundary-mixed-relation.py)。

- command：python3 scripts/check-r719-exact-boundary-mixed-relation.py --workers=4 --taus=2,3,4,5；
- dependencies：python-flint==0.9.0、Node.js；只在内存调用 R594 原算法；
- source commit：ad90f969282811ed8d4499606cb577186e07ec39；
- public run：43694974589；job：132753387780；
- script SHA256：074730c7897224972ac89a6ac4ffddd20d60aaa580a6a2f16e9239413236c5ef；
- stdout：5116 bytes；SHA256：
  a1f1d8322212edebcb74e4de65ac3d418fe4d09061b5ada6a26d81eae8f6ee8c；
- runtime：1154.045秒；全部1200条特征零身份成立；
- 原 R594 输入脚本 SHA256：
  34b630315837c5418d05f6c2984c93c29a680f7802b26dd85391303eee387873。

按根规则只保算法、参数和真实 run/hash，不保存可重算输出。
此前辅助 run43693554672 仅用于寻找52行；
定理1及实际单位结论由本次特征零计算和正文次数界支付。

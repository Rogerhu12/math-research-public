# R666 — 七条原条件 A 来源的完整有限基与准确深度递推

日期：2026-11-15。**状态：已证明。**

本篇继续 R664/R665 的同一个四输入门及同一个原 R594 多项式。
不把 $\Lambda_{2,N}$ 的质量替代整条条件来源。
七条 $\Lambda_{k,N}$ 的完整 Fourier 级数都在原 degree29 theta 空间中；
按角型一共只需 33 个系数，全部由不超过总次数 35 的原四 sigma 矩准确决定。

更强地，作下述明确归一化后，整条来源对深度 $N$ 的依赖是
$t=\kappa^N$ 的至多六次多项式。这给同一测度的七阶深度递推，
而非只给其质量的渐近式。全部 C 单位补项、未知符号 $\eta=\pm1$、
原右逆和所有 $\lambda,\kappa$ 项均保留。

这些有限关系还没有消去 R664/R665 的实际浅补域及 Y 外部；
也没有给新 theta 截面添加算术中央零。

## 1. 完整保留的原四输入和条件来源

固定当前普通 ray 的一个好素数 $p>101$，保持 $b=17$，
$\lambda,\kappa,\Omega$ 及原 R594 的同一个整齐次六次多项式
$$
\widehat P_p(D,E,G)\in\mathcal O[D,E,G].
$$
它依赖当前 $p$ 的 $\lambda,\kappa$，但不依赖深度 $N$。
本文只取 $N\in4\mathbf Z_{\ge1}$，并不重新求这个右逆。

保持 R665 的四输入测度
$$
\nu_4=-\mathcal P_{6,C}\nu_\sigma^{\otimes4}/84
$$
和原 A 轴、三个 A 伴随。以下全部量都与 A 正交：
$$
D=D_*,\qquad C^\perp=C+\frac{29}{143}D,\qquad
E_\perp=14C^\perp,\qquad G_\perp,\qquad G_{00}.
$$
具体常数及回代仍是
$$
\epsilon_D=-\frac{263}{143},\qquad
\gamma_D=\frac{-789+526\omega}{143},\qquad g=3-2\omega,
$$
$$
E_*=E_\perp+\epsilon_D D,\qquad
G_*=G_\perp+\gamma_D D,
$$
$$
G_{00}=G_\perp-
 \left(-\frac{263}{38}+\frac{263}{57}\omega\right)C^\perp .
\tag{1}
$$
这些是原输入的线性行，不是新独立变量。
特别 $D$ 与 C 不正交；原 whole37323/146718 两核和三倍覆盖全部继续使用。

原四输入门和多项式定义为
$$
\mathcal H_N=\{C\ {\rm unit},D\in p^N\},
$$
$$
p_N(z)=\frac1{b\Omega^6}
\widehat P_p(D/\kappa^N+z/\kappa^N,\ E_*+z,\ G_*+gz)
=\sum_{k=0}^6 z^k p_{k,N}.
\tag{2}
$$
所以 R664 的实际条件 A 测度是
$$
\boxed{\Lambda_{k,N}=A_*(1_{\mathcal H_N}p_{k,N}\,d\nu_4).}
\tag{3}
$$
$z$ 在 (2) 只是独立形式参数；后面的 Fourier 变量另用 $Z$。

沿用原 Fourier/周期规范
$$
\mathcal A_\mu(Z)=\int \exp(aZ/\Omega)\,d\mu(a).
\tag{4}
$$
这首先是由全部矩定义的正式级数；在小盘也确实收敛。
原 $\nu_\sigma$ 在该规范中就是同一个 $\sigma(Z)$。
没有改变 $\Omega$ 或物理 A 输出。

## 2. 全部 C 单位补域给出一个准确有限算子

对任意只依 A 伴随的齐次 $r$ 次多项式 $R$，定义线性映射
$$
\boxed{
\mathcal T_r[R](Z)
=\Omega^{-r}\int R(\xi)\exp(A(\xi)Z/\Omega)\,d\nu_4(\xi).
}
\tag{5}
$$
它由原四 sigma 的完整生成函数求 $r$ 次常系数偏导而得；
$\Omega^{-r}$ 准确消掉这 $r$ 次原矩的周期。

置 $t=\kappa^N$，并在原三个形式变量上使用
$$
\mathcal D_t=\partial_D+t\partial_E+tg\partial_G.
$$
定义以下两个齐次 $6-k$ 次的原四输入多项式：
$$
\begin{aligned}
R_{k,p}(t;\xi)
={}&(\mathcal D_t^k\widehat P_p)
 (D,E_\perp+\epsilon_DtD,G_\perp+\gamma_DtD),\\
R^\flat_{k,p}(t;\xi)
={}&(\mathcal D_t^k\widehat P_p)
 (D,\kappa E_\perp+\epsilon_DtD,\,
 G_{00}+\kappa(G_\perp-G_{00})+\gamma_DtD).
\end{aligned}
\tag{6}
$$
微分一律先作，再代入显示的完整线性行。
令 $\eta\in\{1,-1\}$ 为 R665 的实际 whole146718 标量，保两种可能。

**定理 1。** 原完整条件来源准确满足
$$
\boxed{
F_{k,N}(Z):=
\kappa^{kN}\lambda^{-N}\Omega^k\,
\mathcal A_{\Lambda_{k,N}}(Z)
=\frac1{k!\,b}\,
\mathcal T_{6-k}
 \bigl[R_{k,p}(\kappa^N)-\eta\lambda R^\flat_{k,p}(\kappa^N)\bigr](Z).
}
\tag{7}
$$

证明如下。由 (2)，
$$
p_{k,N}=\frac{\kappa^{-kN}}{k!b\Omega^6}
(\mathcal D_t^k\widehat P_p)(D/\kappa^N,E_*,G_*).
$$
先使用 R665 的 whole D 核：
$$
\nu_4|_{D\in p^N}
=(\chi_D\lambda)^N(P_{D,\kappa^N})_*\nu_4
=\lambda^N(P_{D,\kappa^N})_*\nu_4,
$$
其中 $\chi_D^2=1$ 且 $4\mid N$。
D 返回把 $D/\kappa^N$ 变回 D，(1) 的 E/G 两项变成 (6) 的第一行。
它保持 A 与 $C^\perp$。

原 $C=C^\perp-29D/143$；在真实 D 深域上，
C 单位准确等价于 $C^\perp$ 单位。
将它写成全域减 $C^\perp$ 深一层，并使用另一条完整核心
$$
\nu_4|_{C^\perp\in p}
=\eta\lambda(P_{C^\perp,\kappa})_*\nu_4.
$$
这个操作保持 A 和 D，把 $E_\perp$ 乘 $\kappa$，
把 $G_\perp$ 变成 $G_{00}+\kappa(G_\perp-G_{00})$，
因此恰给 (6) 第二行，系数为 $-\eta\lambda$。
最后 (5) 产生的周期为 $\Omega^{6-k}$，与原 $\Omega^{-6}$
及左边 $\Omega^k$ 准确相消，得到 (7)。
全域与补域都使用同一 $\nu_4$；没有把其中一条符号或来源删除。

## 3. 整条来源对深度的精确六次多项式

$\mathcal D_t^k$ 的系数对 t 的次数至多 k。
其作用后 $\widehat P_p$ 的齐次次数为 $6-k$，
(6) 的每个代入行对 t 至多一次。
所以两个多项式对 t 的次数都至多六。

因此存在由 (6)–(7) 明确给出的固定来源 $F_{k,h,p}$，使对全部原 N：
$$
\boxed{
F_{k,N}(Z)=\sum_{h=0}^{6}\kappa^{Nh}F_{k,h,p}(Z).
}
\tag{8}
$$
这里“固定”指当前 p 固定后不依赖 N。
每个系数仍保 $\widehat P_p,\lambda,\kappa,\eta$；
没有把 p 依赖的系数称为全局免费的算术来源。

尤其 $N\to\infty$ 沿正四倍数时，准确极限为
$$
\boxed{
F_{k,0,p}
=\frac1{k!b}\mathcal T_{6-k}
 \left[
 (\partial_D^k\widehat P_p)(D,E_\perp,G_\perp)
 -\eta\lambda(\partial_D^k\widehat P_p)
       (D,\kappa E_\perp,G_{00}+\kappa(G_\perp-G_{00}))
 \right].
}
\tag{9}
$$
这不是只读取 $k=2$ 的质量。所有七条完整来源都在 (9) 中。

## 4. 原 degree29 theta 空间和明确的 33 个系数

R664 已证明 (3) 沿 A 是整个 standard odd $\mathcal S_{29}$ 的真实截面，
角型为 $k-2\bmod6$。这一点也可直接用于 (5)：
A 的原四个 CM 系数范数之和为29，
C 平均固定 A，所有微分方向与 A 正交。
因此原 sigma 准周期公式中的交叉 Gaussian 被正交性逐项消掉；
完整半特征仍为原 odd29，微分没有另添 flat twist。

令
$$
\mathcal I_{29}=\{(a,\beta):a\ge0,\ \beta\in\{0,1\},
                         \ 2a+3\beta\le29\}.
$$
对 $(a,\beta)\in\mathcal I_{29}$，置
$$
r=29-2a-3\beta,\qquad
\Psi_r(Z)=\sigma(Z)^{29}x(Z)^a y(Z)^\beta .
\tag{10}
$$
所有 r 互不相同，且准确遍历
$$
\boxed{\mathcal R_{29}=\{0,1,\ldots,29\}\setminus\{28\}.}
\tag{11}
$$
它们的首项和型为
$$
\Psi_r(Z)=(-1)^\beta Z^r(1+O(Z^6)),\qquad
\Psi_r(\omega_6 Z)=\omega_6^r\Psi_r(Z).
\tag{12}
$$
这是 $\mathcal S_{29}$ 的完整基：
任一截面除以 $\sigma^{29}$ 后，是仅在 O 有至多29阶极的椭圆函数。
在仿射曲线坐标环中，它唯一写为 $P(x)+yQ(x)$，
该极帽恰给 (10) 的全部单项式。
不以首几项相合猜测整个函数相等。

对第 k 条来源，只保
$$
\mathcal R_k=\{r\in\mathcal R_{29}:r\equiv k-2\pmod6\}.
$$
准确列表为：

| k | 原角型 | 完整基的首阶 r | 系数数 |
|---:|---:|---|---:|
| 0 | 4 | 4,10,16,22 | 4 |
| 1 | 5 | 5,11,17,23,29 | 5 |
| 2 | 0 | 0,6,12,18,24 | 5 |
| 3 | 1 | 1,7,13,19,25 | 5 |
| 4 | 2 | 2,8,14,20,26 | 5 |
| 5 | 3 | 3,9,15,21,27 | 5 |
| 6 | 4 | 4,10,16,22 | 4 |

故七条来源共需33个系数，且
$$
\boxed{
F_{k,N}(Z)=\sum_{r\in\mathcal R_k}
              c_{k,r,p}(\kappa^N)\Psi_r(Z),
\qquad c_{k,r,p}(t)\in K[t],\quad\deg_t c_{k,r,p}\le6.
}
\tag{13}
$$
$K$ 可取原所有固定 CM 系数所在的数域；
在本篇 R594/R665 的系数规范下为 $\mathbf Q(\omega)$。

(12) 还给一个完整且无选择的恢复算法。将每个 $\mathcal R_k$ 从小到大排列，
若已恢复较小 r 的系数，则
$$
\boxed{
c_{k,r,p}(t)=(-1)^{\beta(r)}
\left(
 [Z^r]F_{k,p}(t;Z)
 -\sum_{\substack{r'<r\\r'\in\mathcal R_k}}
      c_{k,r',p}(t)[Z^r]\Psi_{r'}(Z)
\right).
}
\tag{14}
$$
这里 $F_{k,p}(t;Z)$ 是 (7) 右端保留独立参数 t 的完整多项式。
对角只有 $\pm1$；缺少的 r=28 不是额外自由系数。
所以至多前30个 Taylor 系数准确决定整条来源。

## 5. 所需原矩只有总次数至多35，且基变换在好 p 处整

(5) 给
$$
\boxed{
[Z^n]\mathcal T_{6-k}[R]
=\frac{\Omega^{-(n+6-k)}}{n!}
       \int A^nR\,d\nu_4 .
}
\tag{15}
$$
R 齐次 $6-k$ 次，恢复 (14) 只用 $n\le29$，
因此每个条目至多使用原四 sigma 的总次数35矩。
所有它们都由同一
$-\mathcal P_{6,C}\sigma^{\otimes4}/84$
的有限 Taylor 展开准确给出。
没有把未计算的条件来源系数当成任意参数。

这些固定低 jet 的分母也已受控。
可直接使用 R660 的原 z 时间整多项式系统：
$$
U'=R,\quad R'=3bU^5,\quad B'=-3bU^5B^2,\quad
V'=3bU^4B^2,\quad A_0'=(V-bU^5B)A_0,
$$
初值 $(0,1,1,0,1)$，其中 $U=u(Z)$、$A_0=\sigma(Z)/U$。
它给全部坐标的 Hurwitz 系数整。
$\sigma=UA_0$，且 (10) 准确为
$$
\Psi_r=(-1)^\beta U^r A_0^{29}R^\beta .
\tag{16}
$$
所以所需 $\sigma$ 的35阶 jet 与 $\Psi_r$ 的29阶 jet
只有不超过35阶阶乘带来的素数分母。
原 C 平均、伴随坐标和 $1/(k!b)$ 另有明确固定分母，
它们均已在当前坏集排除。
原 $\widehat P_p$ 的系数整由原右逆门保证。

因此在当前好 p 处，(14) 的整个三角变换及其逆都整。
令 $\mathscr L_{29,k}$ 为这些 $\Psi_r$ 的 $\mathcal O$ 线性格，
则 (8) 的每个 $F_{k,h,p}$ 都在该格中，且
$$
\boxed{F_{k,N}-F_{k,0,p}\in\kappa^N\mathscr L_{29,k}.}
\tag{17}
$$
(17) 说的是显示有限 theta 基的系数范数；
没有另行声称任意未知 Mellin 值是单位。
固定 p 后，对任何固定线性观察，(8) 都给准确有限式。

## 6. 整条实际测度的七阶深度递推

写 $N=4r$，$r\ge1$，令 $\mathsf S$ 表示 $r\mapsto r+1$ 的移位。
由 (8)，在整个 theta 空间准确有
$$
\boxed{
\prod_{h=0}^6(\mathsf S-\kappa^{4h})F_{k,4r}=0.
}
\tag{18}
$$
若用未归一化的原条件测度，则相应式为
$$
\boxed{
\prod_{h=0}^6
 \left(\mathsf S-\lambda^4\kappa^{4(h-k)}\right)
 \Lambda_{k,4r}=0.
}
\tag{19}
$$
$\Omega^{-k}$ 与 r 无关，故不进根。
有些根有负赋值；(19) 在原 $p$ 进数域上的有界测度向量空间中陈述，
不把这些系数改称整单位。

为说明 (19) 不只是正式 jet 关系，(18) 已使差测度的全部 Fourier 系数、
从而全部多项式矩为零。每个有限组合仍是有界测度。
多项式在 $\mathbf Z_p$ 的连续函数中稠密，
所以这个差测度确实为零。
故 (19) 对任意固定连续测试，包括固定单位 cut 和 principal log，均可积分使用。

但是一个随 N 改变的测试不自动满足同一个递推。
例如 R664 的 T 观察中仍有
$w_i\kappa^N\mathcal E$，
其 unit cut 和 log 必须照原式完整运输。
(19) 没有将这些依 N 的部分冻结。

## 7. 同 J_N 的准确返回和当前范围

令 k=2、Z=0。原 $\Psi_0$ 常数为 $-1$，其余四个基函数常数为零。
于是 (13) 给
$$
F_{2,N}(0)=-c_{2,0,p}(\kappa^N).
$$
另一方面 R664(30) 的准确原质量是
$\Lambda_{2,N}(\mathbf Z_p)=J_N/c_F^2$，$c_F=-3\omega/5$。
因此
$$
\boxed{
J_N=-c_F^2\,\Omega^{-2}\lambda^N\kappa^{-2N}
                         c_{2,0,p}(\kappa^N).
}
\tag{20}
$$
这与 R665 的两 $\eta$ 固定二次多项式和 $v_p(J_N)=-2N$ 相容；
(20) 没有重复其非零证明。
新增的是该常数以外的另外32个实际系数、全条来源及其 N 递推的完整定义和有限恢复。

目前 R664 的 S 共同域可将 (13) 逐项代入，
并以固定 S 测试使用 (18)–(19)；
它的 T 行、真实浅门以及 Y 外部仍须保完整输入。
原11个自由 q 方向若要消某条条件来源，
必须经过 (6)、(14) 的这个实际33系数线性映射；
仅使 (20) 变化或为零，不会使整条 $\Lambda_{2,N}$ 消失。

本篇没有宣称这张33系数映射具有某个尚未计算的秩，
也没有将七条来源视作七个独立算术零。
原固定曲线的无穷不同 p 目标仍需在完整共同/浅/外部关系中完成。

依赖：
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)；
R594 的同一原右逆（准确入口见 R665 及其原证书）。
本篇没有重选任何系数。

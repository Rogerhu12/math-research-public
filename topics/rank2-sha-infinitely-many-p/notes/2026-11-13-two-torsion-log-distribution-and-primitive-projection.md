# 固定二挠除子对数的 CM 分布、二阶角色行及完整 theta 差分

日期：2026-11-13。状态：以下乘法分布、全部常数、二阶移权、非齐次 theta 恒等式和三个固定十七角色质量的非零性均已证明。尚未证明这些新行由原 E17、E34、E136 的三个完整中央导数控制。

本文使用 [E8 参考笔记](2026-11-13-three-curve-central-functional-and-rankzero-connection.md) 的准确截面；不修改 R245 的协变分解。全部分布关系在固定曲线上直接证明，不引用待发表的非零结论。

## 1. 固定函数、单位根和局部对数的规范

仍在 $E_0:y^2=x^3-x$、$dz=dx/(2y)$ 上，置
$$
T_+=(1,0),\quad T_-=(-1,0),\quad T_0=(0,0),\qquad
r(z)=\frac{x(z)-1}{x(z)+1},\quad r(0)=1.
$$
这里 $z=0$ 指无穷远点 $O$。准确有
$$
\operatorname{div}(r)=2(T_+)-2(T_-),\qquad
r(iz)=r(z)^{-1},\qquad r(z+T_0)=-r(z)^{-1}.
\tag{1}
$$
第二式来自 $x(iz)=-x(z)$；第三式来自 $x(z+T_0)=-1/x(z)$。

对固定奇范数 $\alpha\in\mathbb Z[i]$，设 $n=\alpha\bar\alpha$。它在
二挠点上固定 $T_0$，并或固定、或交换 $T_+,T_-$。据此定义
$$
\epsilon_\alpha=
\begin{cases}
1,&\alpha\equiv1\pmod{2\mathbb Z[i]},\\
-1,&\alpha\equiv i\pmod{2\mathbb Z[i]}.
\end{cases}
\tag{2}
$$
符号不随把 $\alpha$ 改为 $-\alpha$ 而改变。

对目标惰性 $p$，排除 $2$ 及本篇固定挠点阶的素因子。固定一个所有
代数系数的 $p$ 进嵌入。所出现的 $r(Q)$ 都是 $p$ 进单位：好约化下
prime-to-$p$ 挠点不能约化到不同阶的二挠点。使用单位群的标准
$p$ 进对数，所有单位根的对数为零。

在原点邻域写
$$
f_Q(z)=\log\frac{r(z+Q)}{r(Q)},\qquad f_Q(0)=0.
\tag{3}
$$
这是一个固定形式支。它与未中心化的 $\log_p r(z+Q)$ 相差明确常数
$\log_p r(Q)$；后文不随意丢掉该常数。

## 2. 奇 CM 范数分布的常数准确为一

**命题 1。** 对每个上述 $\alpha$，有代数函数恒等式
$$
\boxed{\prod_{Q\in E_0[\alpha]}r(z+Q)=r(\alpha z)^{\epsilon_\alpha}.}
\tag{4}
$$

**证明。** 左边的除子是
$2\sum_Q(T_+-Q)-2\sum_Q(T_--Q)$，与右边的除子相同：当 $\alpha$
交换两个二挠点时，需要准确的负指数。因此二者只差一个常数。
在 $z=0$，非零的核点被 $i$ 分成四元轨道。确实 $i-1$ 的范数为二，
而核的阶是奇数，所以 $i$ 或 $-1$ 没有非零不动点。每个轨道由 (1)
给乘积一，$Q=O$ 也给一。右边在原点同样为一，故常数就是一。证毕。

特别地，取本篇的固定
$$
\beta=4-i,\quad \bar\beta=4+i,\qquad
\pi=2+i,\quad\bar\pi=2-i,
$$
四者都满足 $\epsilon=-1$。例如范数十七的式子是
$\prod_Qr(z+Q)=r(\beta z)^{-1}$，不能误写成正指数。

由 (4) 及原点归一，完整局部对数等式为
$$
\boxed{\sum_{Q\in E_0[\alpha]}f_Q(z)
       =\epsilon_\alpha\log r(\alpha z).}
\tag{5}
$$
未中心化时也成立，因为
$\sum_Q\log_p r(Q)=\log_p\prod_Qr(Q)=0$。
这里没有未计入的线性或常数准周期项。

对于偶范数的 $1+i$，相应式子不是 (4)：由 (1) 准确有
$$
r(z)r(z+T_0)=-1.
\tag{6}
$$
其标准 $p$ 进对数范数为零，中心化后也是 $f_O+f_{T_0}=0$。
因此二次覆盖本身不产生额外的 $\log_p2$。theta 尺度变化中另有的
$\log_p2$ 项仍须按 E8 参考笔记的公式保留；它不来自 (6)。

## 3. 两次导数给出明确的非齐次差分

置
$$
B(z)=\frac1{x(z)^2-1},\qquad B(0)=0.
$$
直接使用 $x'=2y,y'=3x^2-1$ 得
$$
(\log r)'=\frac{4x}{y},\qquad
(\log r)''=-4-8B(z).
\tag{7}
$$
对 (5) 求两次导数，准确得到
$$
\boxed{
\sum_{Q\in E_0[\alpha]}B(z+Q)
=\epsilon_\alpha\alpha^2B(\alpha z)
    +c_\alpha,\qquad
c_\alpha=\frac{\epsilon_\alpha\alpha^2-n}{2}.}
\tag{8}
$$
显式常数为
$$
c_\beta=-16+4i=-4\beta,\quad
c_{\bar\beta}=-16-4i=-4\bar\beta,
$$
$$
c_\pi=-4-2i=-2\pi,\quad
c_{\bar\pi}=-4+2i=-2\bar\pi.
\tag{9}
$$
这些常数来自原来的 $-4$ 项及两阶缩放 $\alpha^2$，不是可以任意
调掉的对数积分常数。

### 3.1 把真实 theta 乘子放回去

令
$$
S_8^{\rm b}=-y\vartheta\sigma^3,\quad
F=(S_8^{\rm b})^{17},\quad N=68,\quad H_B=FB.
\tag{10}
$$
$F(0)=1$，$H_B(0)=0$。$F$ 在 $T_+,T_-$ 各有十七阶零，所以 $H_B$
是原 degree-$68$ twist 线丛中的真实全纯截面。
对每个 $Q\in E_0[\alpha]$ 定义
$$
L_{\alpha,Q}(z)=F(\alpha z)B(z+Q).
\tag{11}
$$
它也是真实全纯截面，次数为 $68n$：$B(z+Q)$ 的所有双极点满足
$z+Q=T_+$ 或 $T_-$，其 $\alpha z$ 是某个 $T_\pm$，所以均由
$F(\alpha z)$ 的十七阶零付掉。这里没有使用未付的亚纯参考。

乘以 $F(\alpha z)$ 后，(8) 成为完整 theta 恒等式
$$
\boxed{\sum_QL_{\alpha,Q}(z)
       =\epsilon_\alpha\alpha^2H_B(\alpha z)
         +c_\alpha F(\alpha z).}
\tag{12}
$$
不能把左侧改成未带权的 $\sum_QH(z+Q)$。完整权是 (11) 的
$F(\alpha z)$，不是 $F(z+Q)$。

### 3.2 完整中央行及显式非零 CM 对数

固定惰性 $p$，令 $d=p+1$、$c_0$ 为 R54 的 sigma 临界系数。
沿用 E8 参考笔记的
$$
\mathcal J_{Nc_0}(G;u),\qquad
U_{\alpha,p}=\alpha^d/n\in1+p\mathbb Z_{p^2}.
$$
所有截面都固定，因而在固定有限坏集合外，R54 的整模型及余项
收敛估计适用。由 (12) 及已证完整 CM 缩放公式，
$$
\boxed{\sum_Q\mathcal J_{nNc_0}(L_{\alpha,Q};u)
 =U_{\alpha,p}^{u}\bigl(
   \epsilon_\alpha\alpha^2\mathcal J_{Nc_0}(H_B;u)
       +c_\alpha\mathcal J_{Nc_0}(F;u)\bigr).}
\tag{13}
$$
$\mathcal J_{Nc_0}(F;u)$ 是常数项一的解析单位；这是 $F$ 的 Gauss
估计，不是声称 $\mathcal J(F)=\mathcal J(S_8^{\rm b})^{17}$。

写 $j(G)=\partial_u\mathcal J(G;0)$，并对 (11) 使用同一个单位归一
$$
\widehat j_F(L_{\alpha,Q})
 =j(L_{\alpha,Q})-B(Q)j(F).
$$
由 (8) 在原点的值，$\sum_QB(Q)=c_\alpha$。于是 (13) 求导给
$$
\boxed{\sum_Q\widehat j_F(L_{\alpha,Q})
       =\epsilon_\alpha\alpha^2 j(H_B)
           +c_\alpha\log_pU_{\alpha,p}.}
\tag{14}
$$
这已经是含参考截面 $H_B=F/(U-1)$ 的中央行和明确常数的非齐次闭合恒等式；$H_B$ 不是 R243/R245 的原 rank-two 截面 $H=A_{136}$。

例如把范数五的两个式子相减，全部归一系数保持为 (9)，得
$$
\boxed{
-\frac1{2\pi}\sum_Q\widehat j_F(L_{\pi,Q})
+\frac1{2\bar\pi}\sum_Q\widehat j_F(L_{\bar\pi,Q})
-i\,j(H_B)
=d\log_p\frac{2+i}{2-i}\ne0.}
\tag{15}
$$
相应的范数十七式是
$$
\boxed{
-\frac1{4\beta}\sum_Q\widehat j_F(L_{\beta,Q})
+\frac1{4\bar\beta}\sum_Q\widehat j_F(L_{\bar\beta,Q})
+\frac i2\,j(H_B)
=d\log_p\frac{4-i}{4+i}\ne0.}
\tag{16}
$$
右边非零，因为所列范数一代数数不是根单位。所需局部对数核
结论与 E8 参考笔记相同。特别，这里没有将一个未证明的有限层
非零极限当作已知非零常数。

## 4. 原十七角色的对数常数与二阶行必须分开

固定非零 $P\in E_0[\beta]$，并令 $i$ 在该循环群上取 $4\bmod17$。
对非平凡乘法角色 $\chi:\mathbb F_{17}^{\times}\to\overline{\mathbb Q}^{\times}$，置
$$
\Psi_\chi(z)=\sum_{a\in\mathbb F_{17}^{\times}}
             \chi(a)^{-1}\log_p r(z+aP),
$$
$$
C_\chi=\Psi_\chi(0),\qquad
\Phi_\chi(z)=\Psi_\chi(z)-C_\chi
 =\sum_a\chi(a)^{-1}f_{aP}(z),
$$
$$
B_\chi(z)=\sum_a\chi(a)^{-1}B(z+aP).
\tag{17}
$$
未中心化的 $\Psi_\chi$ 是 $p$ 进解析函数；$\Phi_\chi$ 的 Taylor
系数则直接由固定代数有理函数和形式对数给出。

由 $r(iQ)=r(Q)^{-1}$ 及指标换元，
$$
(1+\chi(i)^{-1})C_\chi=0,
\qquad
\Phi_\chi(iz)=-\chi(i)^{-1}\Phi_\chi(z).
\tag{18}
$$
因 $\chi$ 非平凡，求两阶时 (7) 的常数项相消，给
$$
\boxed{\Phi_\chi''=-8B_\chi,\qquad
B_\chi(iz)=\chi(i)^{-1}B_\chi(z).}
\tag{19}
$$

对仓库固定 $\lambda(3)=-i$，有 $\lambda(4)=1$。所以对
$\chi=\lambda,\lambda^2,\lambda^3$：

- 对数常数 $C_\chi$ 准确为零；
- $\Phi_\chi$ 只含 $z^{4j+2}$；
- 两阶后的 $B_\chi$ 只含 $z^{4j}$，原 $d=p+1$ 中央行仍然保留。

因此 $C_\chi=0$ 绝不意味着二阶中央行被杀掉。
相反，只有 $\chi(i)=-1$ 的 octic 类型可以有非零 $C_\chi$；这些
类型在两阶后取 $i$ 特征 $-1$，不能未经移权就放入原中央行。
这里没有声称所有 octic 常数都非零。

原未加权的 $F\log r$ 也只含 $z^{4j+2}$，所以其未移权中央函数
恒零；但 $z^{-2}F\log r$ 的质量为 $-2$。对它使用 $\nabla_8^2$
时必须保留 R227/R245 的移权和连接项，不能把微分移过 Mellin。

## 5. 固定十七角色的准确范数五分布

设奇范数 $\alpha$ 与 $\beta$ 互素。把 (4) 用在 $z+aP$，再按
$b=\alpha a\bmod\beta$ 换元，得到
$$
\boxed{\operatorname{Tr}_\alpha\Psi_\chi(z)
 :=\sum_{Q\in E_0[\alpha]}\Psi_\chi(z+Q)
 =\epsilon_\alpha\chi(\alpha)\Psi_\chi(\alpha z).}
\tag{20}
$$
这个式子保留全部局部常数；中心化版本准确是
$$
\operatorname{Tr}_\alpha\Phi_\chi(z)
=\mu_{\alpha,\chi}\Phi_\chi(\alpha z)
 +(\mu_{\alpha,\chi}-n)C_\chi,
\quad \mu_{\alpha,\chi}=\epsilon_\alpha\chi(\alpha).
\tag{21}
$$
因而 octic 对数常数若非零，它带的是明确 Euler 型因子
$\mu_{\alpha,\chi}-n$，不能删除后再称为齐次式。

对 (20) 求两阶，得到真正的角色二阶分布
$$
\boxed{\sum_{Q\in E_0[\alpha]}B_\chi(z+Q)
       =\mu_{\alpha,\chi}\alpha^2B_\chi(\alpha z).}
\tag{22}
$$
在 $i\equiv4\bmod\beta$ 的原分量，
$\pi\equiv6=3^{15}$、$\bar\pi\equiv15=3^6\pmod{17}$。
因此范数五的准确标量为

| $\chi$ | $\mu_{\pi,\chi}$ | $\mu_{\bar\pi,\chi}$ |
|---|---:|---:|
| $\lambda$ | $-i$ | $1$ |
| $\lambda^2$ | $1$ | $-1$ |
| $\lambda^3$ | $i$ | $1$ |

这与单纯只用范数一比 $\pi/\bar\pi$ 的算子不同；(20)–(22) 用的是
实际核平移迹。若换到 R231 的平衡 pullback–trace 算子，必须另付
其 theta frame，不能混用两个标量表。

## 6. 三个二阶质量都是明确的非零代数数

令 $U=x(P)^2$。仓库已证的 $\beta=4-i$ 除法多项式是
$$
K(U)=(4-i)U^4+(-12+20i)U^3+(28+10i)U^2
                     +(-20-12i)U-i.
\tag{23}
$$
其四个根是非零核点模 $\mu_4$ 的四个 $x^2$ 值。
它的出处与完整证明见 [R59](../results/R59-fixed-isogeny-normalized-inert-rows.md)
及其固定 CM division note。

三倍公式给
$$
x(3P)^2=U\frac{D(U)^2}{C(U)^4},\quad
C=3U^2-6U-1,\quad D=U^4+12U^3+30U^2-36U+9.
$$
在 $\mathbb Q(i)[U]/K$ 中，它准确约化为
$$
g(U)=\frac{(1+4i)U^3-(20+12i)U^2+(-11+28i)U+14-20i}{4}.
\tag{24}
$$
直接核对 $K(g)=0$、$g^{\circ4}=U$。置 $b=(U-1)^{-1}$，则
$$
B_{\lambda^k}(0)
=\mathcal R_k(U):=4\sum_{j=0}^3i^{kj}b(g^{\circ j}(U)),
\quad k=1,2,3.
\tag{25}
$$
那个因子四来自 $i$ 的四元轨道，不能丢掉。

三个准确的余式为
$$
\begin{aligned}
16\mathcal R_1={}&(-39-3i)U^3+(179-117i)U^2
                   +(-365-185i)U+25+185i,\\
8\mathcal R_2={}&(8+15i)U^3+(-86-21i)U^2
                   +(-76+121i)U+34-51i,\\
16\mathcal R_3={}&(39+37i)U^3+(-311+31i)U^2
                   +(53+263i)U-109-147i.
\end{aligned}
\tag{26}
$$
它们满足 $\mathcal R_k(g)=i^{-k}\mathcal R_k$。对四个根取乘积，给

| $k$ | $\prod_{K(U)=0}\mathcal R_k(U)$ | 再取到 $\mathbb Q$ 的范数 |
|---|---|---|
| $1$ | $256(-89+52i)$ | $2^{16}5^4\cdot17$ |
| $2$ | $256(-15+8i)$ | $2^{16}\cdot17^2$ |
| $3$ | $256(47+52i)$ | $2^{16}\cdot17^3$ |

特别每个 $\mathcal R_k$ 与 $K$ 互素，所以对任意非零 $P\in E[\beta]$
都有 $B_{\lambda^k}(0)\ne0$。这些代数数在 $p>19$ 的所有素位均为
单位。后一结论还用它们是 $S$-整的：$P$ 是固定 prime-to-$p$ 挠点，
$x(P)^2-1$ 在好约化处非零；上述范数不含这样的 $p$。

例如总迹
$\sum_{Q\ne O}B(Q)=4\sum_{K(U)=0}(U-1)^{-1}=-16+4i$
同时复核了 (9) 的常数和方向。

上述有限商环等式及范数均由
[精确脚本](../scripts/check-two-torsion-log-primitive17-resolvents.py)
逐项检验；[输出](../scripts/check-two-torsion-log-primitive17-resolvents.json)
记录全部余式和范数。计算只用高斯有理多项式算术，不选数值根，
不作目标素数扫描。

## 7. 带十七角色的全纯 theta 行与非零范数五对数

为付掉 $B_\chi$ 在 $T_\pm-aP$ 的所有双极，定义
$$
G_\chi(z)=F(\beta z)B_\chi(z),\qquad M=68\cdot17=1156.
\tag{27}
$$
它是真实全纯 degree-$1156$ 截面，因为 $\beta(T_\pm-aP)=T_\mp$，
而 $F$ 在 $T_\mp$ 有十七阶零。
其质量为 (25) 的非零单位 $b_\chi=B_\chi(0)$。

对 $\alpha=\pi,\bar\pi$ 再置
$$
G_{\alpha,Q,\chi}(z)
 =F(\beta\alpha z)B_\chi(z+Q),\qquad Q\in E_0[\alpha].
\tag{28}
$$
同样的零极点检查说明每项全纯，次数为 $5M$。
乘 (22) 以准确 theta frame，得到
$$
\boxed{\sum_QG_{\alpha,Q,\chi}(z)
       =\mu_{\alpha,\chi}\alpha^2G_\chi(\alpha z).}
\tag{29}
$$
于是完整中央函数准确满足
$$
\boxed{\sum_Q\mathcal J_{5Mc_0}(G_{\alpha,Q,\chi};u)
       =\mu_{\alpha,\chi}\alpha^2U_{\alpha,p}^{u}
                              \mathcal J_{Mc_0}(G_\chi;u).}
\tag{30}
$$
特别两个范数五方向求导并消去同一个未知 $j(G_\chi)$，给
$$
\boxed{
\frac{\sum_Qj(G_{\pi,Q,\chi})}{\mu_{\pi,\chi}\pi^2}
-\frac{\sum_Qj(G_{\bar\pi,Q,\chi})}
       {\mu_{\bar\pi,\chi}\bar\pi^2}
=b_\chi d\log_p\frac{2+i}{2-i}\ne0.}
\tag{31}
$$
这里所有固定非零质量、角色标量和 gauge 都已保留。
(31) 不需要假设 $j(G_\chi)$ 非零，也不需要抛弃任何秩零参考的
未知导数。

## 8. 目前还需要实际求出的交织

(17) 的角色作用是除法点 $P\mapsto aP$ 的 ray-scalar 作用。
R231/R239 的原 Yang 行则由固定 Schwartz 模型中的 compact-torus
作用、全部 Haar 相位、二处型和中央权决定。相同的符号
$\lambda$ 不能自行证明两种观察行相同。

本篇已经给出可用于比较的具体全纯源 (27)–(28)、固定有限度数、
准确角色表和中央质量。新参考及新 rank-two 截面属于 degree-$68$
的 twist-$T_0$ 线丛，而旧 $A/B$ 属于无此半特征的线丛；在 $[\beta]$
拉回后的 degree-$1156$ 仍不能把它们直接混作同一块。下一项实际
计算先对全部截面作真实 $[2]$ 拉回，进入共同 degree-$4624=16\cdot17^2$
theta 群模型，保持 $16\times17^2$ 张量或稀疏结构，再用原有限
Weyl/角色矩阵计算投影及额外来源。这个 $[2]$ 拉回的中央变换是
$\mathcal J_{4Mc_0}(G(2z);u)=2^{(p-1)u}\mathcal J_{Mc_0}(G;u)$；
质量非零时须保留其 $(p-1)G(0)\log_p2$ 导数项。随后保留完整中央
行作消元。特别 $b_\chi\ne0$ 而三个原 rank-two 行的质量为零，
说明不能把 (27) 直接认作其中任一原行。

(15)、(16)、(31) 是准确的非零中央关系；它们与原三条导数之间
缺的是上述明确的交织比较，不是一个可以删去的局部对数常数。


# R1054 — 原通常 p 剔除的完整 p² 新来源与真实 flat 张量返回

按根 README 第8条登记完整证明；原 notes 路径保留转向。除本篇明示的已证范围外，课题主目标仍未完成。

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本注消费原固定 weight3 来源，而不再使用已经由 R1052 排除的未剔除
toric flat 族。全部 full2/full9、原 tame 邻点、Artin/Cor 及实际
$g_1,g_2$ 规范保持。以下给出通常剔除中剩余项的真实来源、
逐权 tensor、conductor-$p^2$ 点及完整有限 Schwartz 字；不把
$\flat$ 直接等同通常剔除，也不把一个有限 Schwartz 投影赋成新的
canonical 零。

## 1. 真实 q 归一与 full9 中心号

取原固定
$w_0=\theta(\psi_4^2)$，或已经支付的同一 weight3 CM 来源及其
完整 tame 操作。令
$$
F_0=w_0/\omega_{\rm can}^3,\qquad
g_1=\operatorname{diag}(p,1),\quad
g_2=\operatorname{diag}(1,p).
\tag{1}
$$
$p>211$ 为原好惰性素数。这里
$a_p(w_0)=0$，$\epsilon(p)=-1$；全部 tame 操作与 $p$ 处的
球面 Hecke 作用可交换。原 full2/full9 给
$$
(pI)^*w_0=-p^3w_0,\qquad
(pI)^*F_0=-F_0.
\tag{2}
$$
不能把(2)改成中心作用为1的另一个归一。

以 $Vf(q)=f(q^p)$ 定义通常 $V$。原 Hecke 递推是
$a_{p^2m}=p^2a_m$，故真正除去所有 $p$ 倍 Fourier 项的来源为
$$
w_0^{(p)}=w_0-p^2V^2w_0.
\tag{3}
$$
这个恒等式首先是完整 $q$ 展开恒等式，进而由代数模形式的
$q$ 展开原理成立于同一有限级；这里不使用 supersingular 与
ordinary 两个解析开集之间的延拓。

在 Tate 尖点，$g_2$ 的实际商映射为 $q\mapsto q^p$，
其微分拉回为 $p$，同时把原 tame level 运输为其 $p$ 倍。
两次作用的 tame diamond 是 $\epsilon(p)^2=1$。所以在整个原级
$$
V^2w_0=p^{-6}(g_2^2)^*w_0,\qquad
w_0^{(p)}=w_0-p^{-4}(g_2^2)^*w_0.
\tag{4}
$$
单次 $g_2$ 的 diamond 不能据此删掉。(4)的两次作用与(2)相容。

定义真正的新模形式及其 scalar：
$$
W_p=p^{-4}(g_2^2)^*w_0,\qquad
B_p=W_p/\omega_{\rm can}^3
    =p^2(g_2^2)^*F_0.
\tag{5}
$$
于是 $F_0^{(p)}=F_0-B_p$。$W_p$ 是原 tame level 与
$\Gamma_0(p^2)$ 上的同一个 old modular form；这只是来源身份，
不是说其在本题实际 CM 读者中没有新项。

## 2. 好点有界性、实际坏点和全部 raised 张量

仍取 $y'=yg_1$。好点使用的完整 scalar 是
$$
A_{\rm good}=g_2^*F_0^{(p)}
=g_2^*F_0-p^2(g_2^3)^*F_0.
\tag{6}
$$
两项分别是实际有限级模形式的 completed 结构层 germ，
且 $g_2^*y_{\rm dR}=y_{\rm dR}$。因而原来源返回证明中对
书 Lemma6.16 的使用逐项适用：在同一个好点 $y'$，二者均有
某个有限分母界的有界 $Q_1=q_{\rm dR}^{1/p}$ 展开。
不声称其范数为1。

为记录足够的实际级，$(g_2^3)^*w_0$ 可保在原 tame level
与 $\Gamma_0(p^3)$ 的共同覆盖上；(6)的整个返回均可在该覆盖计算。
此处不需要以书7.18把这个单独来源降回一个较小的级。

因为 $g_1g_2=pI$，实际 $g_1$ 返回为
$$
g_1^*A_{\rm good}=-F_0+B_p.
\tag{7}
$$
同时 $g_1^*Q_1=Q_2$，$\omega_{\rm can}$ 不变，
$g_1^*dz_{\rm dR}=p^{-1}dz_{\rm dR}$。因此(7)是实际有界
$b=2$ Amice 输入，保留其全部系数和有限分母。

令 $\delta^n$ 表示按权 $3,5,\ldots,3+2(n-1)$ 迭代的同一
scalar Maass 算子。原精确变换是
$$
g_1^*\delta_k=p\,\delta_k g_1^*,\qquad
\delta_k g_2^*=p\,g_2^*\delta_k.
\tag{8}
$$
故对每个 $n\ge0$，有不经过任何插值比较的整来源恒等式
$$
\boxed{
g_1^*((p\delta)^n A_{\rm good})
=-p^{2n}\delta^nF_0
+p^{4n+2}(g_2^2)^*(\delta^nF_0).
}
\tag{9}
$$
第二项的 $p^{4n+2}$ 不能减少为 $p^{2n}$。

这里若使用真正拉回的张量 $g_2^*w_0^{(p)}$，它在
$\omega_{\rm can}^3$ 基下的系数是 $p^3A_{\rm good}$。
单纯 $A_{\rm good}\omega_{\rm can}^3$ 则等于
$p^{-3}g_2^*w_0^{(p)}$，没有自行新增 $p^3$。
对前一种真正拉回张量，raise-after-pull 给
$p^{3+2n}g_2^*(\delta^nF_0^{(p)})$；
书7.19的 raise-before-pull tensor 则是
$p^{3+n}g_2^*(\delta^nF_0^{(p)})$。
二者仍相差 $p^n$，不能借(9)恢复尚未支付的7.20/7.22接合。

在完整 toric 和以及原全部外权下，R1052 已证明(9)的第一项所给的
实际 flat 函数恒零。因此对于本注明定的 raise-after-pull flat 读者，
整个值与整个斜率都严格等于实际输入 $B_p$ 所给的读者。
这一步只在已付的完整 toric 和后使用；没有把每一点的
$F_0$ Amice 测度分别断为支撑在 $p\mathbf Z_p$。

## 3. 新点的 conductor 与周期：大 p 幂恰好取消

新项实际评价于
$$
y_2=yg_2^2.
\tag{10}
$$
其商映射 $q_C:E\to E_2$ 的核是原 Tate 直线给出的循环
$p^2$ 子群 $C$，而不是整个 $E[p]$。局部格乘一个
$\mathcal O_{K_p}^{\times}$ 单位后为
$\mathcal O_{K_p}+p^{-2}\mathbf Z_p$；再乘 $p^2$ 后为
$\mathbf Z_p+p^2\mathcal O_{K_p}$。所以目标的局部 CM 阶恰为
$\mathcal O_{p^2}$。所有 full tame level 随实际商映射运输。

选原好整微分 $\omega_0,\omega_2$，写
$$
q_C^*\omega_2=c_C\omega_0.
$$
源高度二形式群的 exact $p$、$p^2$ 挠点参数估值分别为
$1/(p^2-1)$、$1/(p^2(p^2-1))$。用商映射在零点的导数为
全部非零核点参数之积，得到
$$
v_p(c_C)=
\frac{p-1}{p^2-1}
+\frac{p^2-p}{p^2(p^2-1)}
=\frac1p.
\tag{11}
$$
换到指定整微分只乘单位。此证明保留全部厚核；不是只看约化点集。

使用已核定的**书版**周期方向
$\omega_0=\Omega_0\omega_{\rm can}$。
由于 $(g_2^2)^*\omega_{\rm can}=p^2\omega_{\rm can}$，
$$
\boxed{\Omega_2=p^{-2}c_C\Omega_0.}
\tag{12}
$$
原最大阶点的 $v_p(\Omega_0)=-\tau$，
$\tau=p/(p^2-1)$，从而
$$
v_p(\Omega_2)=-2-\frac1{p(p^2-1)}.
\tag{13}
$$
特别，它不是 conductor-$p$ 好点的周期估值
$-1/(p^2-1)$。

令 $r_n^{\rm alg}(E_2,\omega_2)$ 为同一 tame-base 上的
代数 CM Maass 值：即按该微分比较
$\theta(\delta^nF_0)(y_2)=
\Omega_2^{3+2n}r_n^{\rm alg}(E_2,\omega_2)$。
这里不另换高层的 Kodaira--Spencer 归一。于是(9)中新项为
$$
\boxed{
p^{4n+2}\theta(\delta^nF_0)(y_2)
=p^{-4}(c_C\Omega_0)^{3+2n}
r_n^{\rm alg}(E_2,\omega_2).
}
\tag{14}
$$
其显示出来的周期因子估值恰为
$$
-4-\frac{3+2n}{p(p^2-1)}.
\tag{15}
$$
所以原未剔除点上的正线性估值增益已经消失。
(14)没有对剩余的真实邻点代数值作任何原点系数界替换，
也没有由(15)断言非零。

## 4. 同一个 binary theta 的真实局部 annulus

在原固定 binary theta 模型中，$p$ 处原向量为
$\phi_{0,p}={\bf1}_{\mathcal O_{K_p}}$。其全部非 $p$ 分量保持原样。
惰性处 $\psi_4^2((p))=p^2$，原 Fourier 递推与(3)逐项给出
$$
W_p=\Theta(\phi^{\,p}\otimes{\bf1}_{p\mathcal O_{K_p}}),
\qquad
w_0^{(p)}
=\Theta(\phi^{\,p}\otimes{\bf1}_{\mathcal O_{K_p}^{\times}}).
\tag{16}
$$
(16)用原首 Fourier 系数1的同一个 theta normalization。
对原完整 tame 算子先在完整 theta 恒等式上作用；
它们与这个 $p$ 处分量操作可交换。因此(16)不需要把原
2/3/17 Schwartz 向量重新识别或丢掉其相位。

等价地，(16)可以直接由 $x=pz$ 的全局 theta 重标证明：
Hermite degree2给 $p^2$，原 source character 在此有理
缩放上的有限费用正是原 $\psi_4^2((p))$ 归一。
不能单独改变一个 tame 分量而省略该全局重标。

## 5. 新 annulus 的全部 rank-one 有限字

使用已经支付的原双 Hermite 换极化，$a=17/2$。
把原 binary 复坐标写成 $x+\delta Y$，也就是原实坐标
$y=\sqrt3Y$。原生成函数因此成为有理式
$$
S_{\rm alg}(x,Y;r,s)=
-2x^2-6(r-s)x+6(r+s)Y-3r^2+12rs-3s^2.
\tag{17}
$$
原局部 kernel 是 $\psi_p(-aS_{\rm alg})$。这里 $\psi_p$ 是
原全局 additive character 的真实 $p$ 分量，导子为
$\mathbf Z_p$；不擅自改成其共轭。

$p>211$ 时 $2,3,17$ 和这份换极化的交叉矩阵行列式均为单位。
采用自对偶 Haar 使 $\operatorname{vol}(\mathbf Z_p)=1$；
原未分歧 metaplectic splitting 由
$ {\bf1}_{\mathbf Z_p^2}\mapsto{\bf1}_{\mathbf Z_p^2}$ 锚定。
故不存在一个未记出的 $p$ 处根号或自由相位。

在 $x,Y\in p\mathbf Z_p$ 上，$2ax^2$ 的 additive character
恒为1。分别作两个完整积分，线性角色条件准确为
$r-s,r+s\in p^{-1}\mathbf Z_p$，也就是
$r,s\in p^{-1}\mathbf Z_p$。因而
$$
\boxed{
\mathcal W_a({\bf1}_{p\mathbf Z_p^2})(r,s)
=p^{-2}\psi_p\!\left(3a(r^2-4rs+s^2)\right)
 {\bf1}_{p^{-1}\mathbf Z_p^2}(r,s).
}
\tag{18}
$$
体积是两个 $p^{-1}$，所以前面的 $p^{-2}$ 必须保留。
对原整球作同一计算，确实返回原整球，独立核定上述相位规范。

置
$\zeta_{p^2}=\psi_p(1/p^2)$。
(18)在每个 $(p\mathbf Z_p)^2$ coset上为常数，给出全部字：
$$
\boxed{
p^{-2}\!\!\sum_{A,B\bmod p^2}
 \zeta_{p^2}^{(51/2)(A^2-4AB+B^2)}
 {\bf1}_{A/p+p\mathbf Z_p}(r)
 \otimes{\bf1}_{B/p+p\mathbf Z_p}(s).
}
\tag{19}
$$
指数中的 $1/2$ 在 $\mathbf Z/p^2$ 中取逆。
原球在同一字基中是
$\sum_{p\mid A,\ p\mid B}{\bf1}_{A/p+p\mathbf Z_p}
 \otimes{\bf1}_{B/p+p\mathbf Z_p}$。
故通常剔除的整个 finite matrix 为
$$
\boxed{
C_{A,B}={\bf1}_{p\mid A}{\bf1}_{p\mid B}
-p^{-2}\zeta_{p^2}^{(51/2)(A^2-4AB+B^2)}.
}
\tag{20}
$$
这保留原两 rank-one factors 的所有 $p^2$ 字及混合相位
$-102AB$。不能把它改成两份各自的 $p$ 剔除，
也不能先投影其中一条原 canonical 线再丢掉相伴的字。

所有原固定 **prime-to-$p$** finite torus projectors、Artin/Cor
及 Hermite 槽都仍作用在(20)的**整个**张量上；$p$ 处保留
(19)的完整矩阵。任何新增的 compact $p$-torus 平均或角色投影，
必须另行加入其真实全部 cosets 和实际 level 运输，不能默认包含于
原固定54项平均。特别，完整 $p(p+1)$ 个循环 $p^2$ 环类的
imprimitive norm 与固定一条 $p$-level 的原54项是不同读者。
(19)没有断言每个字的 toric 投影都非零，也没有给它们逐字添加
中央零。

## 6. 真实负端点与 proper primitive 的明确接口

令 $\mu_{B_p,a}$ 是(5)经(6)--(7)的实际好点来源给出的
有界 $Q_2$ Amice 测度，$a$ 遍历原完整 toric 字。
保留相同外权及其导数，R1052和(7)给出的实际剩余端点是
$$
\sum_a w_a(-2)\int_{\mathbf Z_p^\times}x^{-2}\,d\mu_{B_p,a}.
\tag{21}
$$
整个斜率则是同一测度的
$x^{-2}\log\langle x\rangle$ 项、原全部
$-(i+1)(i-1)!C_a^i x^{-2-i}$ 修正，以及
$w_a'(-2)$ 乘(21)的完整和。
原实际 Newton 有限 reader 对这个输入逐项适用；
其输入必须由(9)的**第二项**或(19)完整计算，不能沿用原点
$D_{102}\times S_{34}$ 的三个系数前缀。

还有一个 exact proper-source 接口。记
$\mathcal W_0$ 为 $w_0$ 经同一个正号 KS 转成的
$\omega\otimes\Omega^1$ 微分，$G_0$ 为其原归一 Coleman primitive。
KS 在 Hecke 下需 $\det^{-1}$ 费用；准确方向是
$\operatorname{KS}_{\rm src}(\phi^*\omega^2)
 =\deg(\phi)\,\phi^*\operatorname{KS}_{\rm tgt}(\omega^2)$。
因为 $\det(g_2^2)=p^2$，(5)严格给
$$
\mathcal W_p=p^{-2}(g_2^2)^*\mathcal W_0,\qquad
G_p=p^{-2}(g_2^2)^*G_0.
\tag{22}
$$
第二式按原尖点归一；仅局部使用时允许水平差。
这与普通 Fourier primitive 的
$\theta^{-2}(p^2f(q^{p^2}))=p^{-2}(\theta^{-2}f)(q^{p^2})$
逐项吻合。

因此已付的书版正号 Bol 公式把单个(21)写成
$$
p^{-6}\left\langle
 (g_2^2)^*G_0(1)
 -\frac1p\sum_{j=0}^{p-1}(g_2^2)^*G_0(\zeta_p^j),
 \ \omega_{\rm can}(1)\right\rangle.
\tag{23}
$$
这里的根号点只表示同一有界 $Q_2$ 输入所给的 primitive
之 $Q$ 解析延拓值；这是 proper primitive 的同一局部 germ。
水平差的最高分量为 $1,\log Q_2$ 的线性组合，被完整平均准确消掉。

(23)没有把 $Q_2\mapsto\zeta_p^jQ_2$ 认成未重定中心的 CM 图。
将此真实 $Q$ 平均返回原全部 cyclic-$p^2$ 图，
仍须保实际系数运输和规范化；本注不使用旧未支付的
usual/flat 解析接合来完成这一步。

## 7. 本次具体得到的输入

通常剔除中的旧项已由 R1052 在完整 toric 和中严格消去，
剩下的唯一来源是(5)。其实际 CM 点为(10)，周期为(12)，
全部 finite matrix 为(19)，正权输入为(9)第二项，
负端点有(21)--(23)的同一来源表达。

这些是精确来源和读者身份。未证明该剩余读者跨 $p$ 非零，
也未证明它等于原 canonical $J'_S(0)$。书 Def8.7--8.8 本身
没有再除 $\Omega_p^{3+2n}$ 或 $p^{bn}$；
这样的因子出现在其后正权插值比较中，不能据本注把书中整个
$L_p$ 改名为这里的 reader。

### 依赖和原文定位

- [R1052](R1052-original-unmodified-b2-toric-flat-vanishing.md)。
- [真实 good source / bad return](../notes/2026-11-27-original-good-pullback-and-bad-source-return.md)，
  全部 $g_1,g_2$ 和 full9 中心号。
- [实际 flat critical / Bol reader](../notes/2026-11-27-original-flat-amice-critical-slope-and-bol-primitive.md)
  §§1--6.1，使用已校正的书版正号 KS。
- [原双 Hermite 来源](../notes/2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md)
  §§5、10--11，尤其(17)、(32)--(39)；(17)的有理化给本注(17)。
- [原 full p² norm](../notes/2026-11-27-original-inert-p-square-full-norm-and-endpoint-zero.md)，
  原 full tame 中心及全部 proper 图范围。
- D. Kriz, *Supersingular p-adic L-functions, Maass-Shimura Operators and
  Waldspurger Formulas*, AMS212，Lemma6.16、Defs6.17--6.19、
  7.16--7.19及7.19脚注1、Defs8.7--8.8。通常 $p$ 剔除式还见
  §9开头与其(6.28)回引。本文没有以7.20/7.22支付新的接合。

本注没有数学执行，没有新增工作流，也没有改动任何 ref。


## 8. 整个新矩阵的 old 部分与 exact-conductor-$p^2$ 双字

本节只分解同一个(19)，不在原读者中添一个 $p$ 处平均。
令 $R=\mathbf Z/p^2\mathbf Z$，在两条原 rank-one 极化上分别取
$\mathcal S_\pm=\operatorname{Fun}(R,\overline{\mathbf Q})$，
基向量仍为(19)的实际 coset 指示函数。写
$$
v_0(A)={\bf1}_{p\mid A},\qquad
K_{A,B}=p^{-2}\zeta_{p^2}^{(51/2)(A^2-4AB+B^2)},\qquad
P_0f=\frac{v_0}{p}\sum_{A\in pR}f(A).
\tag{24}
$$
这是原整球的一维正交投影，$P_0^2=P_0$；不把它称为原已做过的
$p$ 处 projector。

先做完整有限和。当 $A=pa$ 时，(19)中的混相位为
$\zeta_p^{-102aB}$。$-102$ 为单位，故
$$
(P_0\otimes1)K=(1\otimes P_0)K=p^{-2}v_0\otimes v_0.
\tag{25}
$$
在被留下的 $B\in pR$ 上，其余平方相位也是1。
因此没有 old/new 或 new/old 交叉块。

### 8.1. 两条实际 rank-one 模的完整 torus 字

令
$$
T_2=\{t\in(\mathcal O_K/p^2)^\times:N(t)=1\},\qquad
T_1=\ker(T_2\longrightarrow(\mathcal O_K/p)^1).
$$
其阶分别为 $p(p+1)$ 和 $p$。
使用原两个 Hermitian 系数 $(-17,17)$ 的有限 Weil 表示
$\rho_\pm$。原 $p$ 处 splitting 在 norm-one 单位上平凡；
这两条表示互为对偶，原整球 $v_0$ 固定。
它们的字符均准确为
$$
\operatorname{Tr}\rho_\pm(t)=
\begin{cases}
p^2,&t=1,\\
-p,&t\in T_1\setminus\{1\},\\
1,&t\notin T_1 .
\end{cases}
\tag{26}
$$

以下给(26)的全 Gauss 证明，保实际未分歧相位。
在一个整 symplectic 基中，可把 torus 写为
$t=a+b\delta$、$a^2+3b^2=1$。Hermitian 系数只使两个非对角
矩阵项互乘相反的单位，不改变下面的两个 Gauss 因子的乘积。
对 $t\in T_1\setminus\{1\}$，写
$t=I+p\left(\begin{smallmatrix}0&d b\\b&0\end{smallmatrix}\right)$，
$d=-3$，$b\in\mathbf F_p^\times$。它准确是两个相互交换的
upper/lower transvection 的乘积。原有限 Fourier 归一为 $p^{-1}$
乘全部 $R$-和，故其 trace 是
$$
G(db/2)\,G(-b/2)
=\left(\frac{d}{p}\right)p=-p,\qquad
G(c)=\sum_{x\bmod p}\zeta_p^{cx^2}.
$$
这里 $p$ 惰性使 $d$ 非平方；两个 Hermitian 单位尺度相消，
没有丢掉一个 $\left(\frac{-1}{p}\right)$。

若 $b$ 为单位，原 finite kernel 的 trace 为
$p^{-1}\sum_{x\bmod p^2}\zeta_{p^2}^{u x^2}$，
其中 $u$ 为单位。写 $x=x_0+pk$，先完整求 $k$ 和，只有
$x_0=0$ 留下，故该 trace 为1。
剩下 $t\equiv-1\bmod p$。写 $t=-h$，$h\in T_1$；
$\rho(-1)$ 是原反射 $f(x)\mapsto f(-x)$。
在上述 kernel 中 trace 只允许 $x\in pR$，再完整求这 $p$ 项，
只留下 dual residue $0$，值仍为1。$t=-1$ 本身也只有
$x=0$ 固定，trace 为1。这证明全部情形，且旧整球锚固定了绝对号。

对任意 $\vartheta\in\widehat T_2$，取真实 projector
$$
P_{\pm,\vartheta}
=\frac1{p(p+1)}\sum_{t\in T_2}
 \vartheta(t)^{-1}\rho_\pm(t).
\tag{27}
$$
分母 $p(p+1)$ 保留，未称其为 $p$ 单位。
将(26)与全部字符求和配对，给
$$
\dim P_{\pm,\vartheta}\mathcal S_\pm=
\begin{cases}
1,&\vartheta=1,\\
0,&\vartheta\ne1,\ \vartheta|_{T_1}=1,\\
1,&\vartheta|_{T_1}\ne1 .
\end{cases}
\tag{28}
$$
例如 wild 情形的
$\sum_{T_1\setminus1}\vartheta^{-1}=-1$、
$\sum_{T_2\setminus T_1}\vartheta^{-1}=0$，重数准确为1。
维数 $1+(p^2-1)=p^2$ 回到整个模块，而不是只数已有非零字。

### 8.2. 原双字的准确配对与 whole 来源

原 binary 函数 $ {\bf1}_{p\mathcal O_{K_p}}$ 在乘法 $z\mapsto tz$
下固定。在(16)的两条 eigenspaces 中，同一作用是
$(u,v)\mapsto(tu,tv)$，不是只旋转一条线。
由原换极化的完整 intertwining 和 $p$ 处平凡 splitting，
$$
(\rho_-(t)\otimes\rho_+(t))K=K.
$$
所以(25)、(28)给实际有限分解
$$
K=p^{-2}v_0\otimes v_0+
 \sum_{\substack{\vartheta\in\widehat T_2\\
                  \vartheta|_{T_1}\ne1}}K_\vartheta,
\qquad
K_\vartheta=(P_{-,\vartheta}\otimes1)K
 \in\mathcal S_{-,\vartheta}\otimes
       \mathcal S_{+,\vartheta^{-1}} .
\tag{29}
$$
每个 $K_\vartheta$ 都是用(19)、(27)定义的完整有限和，因此没有
另选根号或未记的 Gauss scalar。

这里每个有限 $K_\vartheta$ 确实非零：
(24)的 $K$ 是两张可逆 diagonal chirp 与
$p^{-2}(\zeta_{p^2}^{-102AB})_{A,B}$ 的乘积。
$-102\in R^\times$，故其整个 $p^2\times p^2$ 矩阵可逆。
它给两个完整 Weil 模之间的非退化配对，结合各字的一维性，
每一对 $\vartheta,\vartheta^{-1}$ 的配对非零。
这只是有限向量非零；后续原全局单位、Hermite、tame torus
投影仍可能杀掉某个全局输出。

将(29)通过原换极化的逆和同一个全局 theta kernel 返回，
定义 $W_\vartheta$ 为 $K_\vartheta$ 的整个来源。则
$$
W_p=p^{-2}w_0+\sum_{\vartheta|_{T_1}\ne1}W_\vartheta .
\tag{30}
$$
所有非 $p$ Schwartz、full2/full9、原 Artin 和 Cor 原样保留。
每个新向量仍属于支撑 $p^{-1}\mathcal O_{K_p}$、在
$p\mathcal O_{K_p}$ cosets 上常值的有限模型；
可在其共同 principal $p^2$ 级及原 tame 级上保留，不能把各个
$W_\vartheta$ 都降回原球面来源。

$\vartheta|_{T_1}\ne1$ 意味着沿 Hilbert90
$z\mapsto z/\bar z$ 得到的两个有限角色都恰有导子 $p^2$：
它们在 $1+p^2\mathcal O_{K_p}$ 上平凡，在
$1+p\mathcal O_{K_p}$ 上非平凡。
这不使用一个导子至少 $p^2$ 的定理于平凡有限字符。

最后对(30)作用本注的同一个 bounded-source 构造与完整 toric
flat 读者。线性性发生在来源恒等式之后；不是把 $P_\vartheta$
擅自移过 $Q$ 读者。R1052 已支付 $p^{-2}w_0$ 的完整 toric
flat 为零，故剩余值和斜率精确为
$$
\mathcal L_{\rm flat}(W_p)
=\sum_{\vartheta|_{T_1}\ne1}
 \mathcal L_{\rm flat}(W_\vartheta).
\tag{31}
$$
两边包含原全部外权和外权导数。
(31)没有声明每个右项分别非零，没有给右项添加原 canonical 零，
也没有将 $Q\mapsto\zeta_pQ$ 与 $T_1$ 作用认同。
真正需要的后继是把(23)的原解析根平均与(27)的实际有限
reciprocity/Heisenberg 作用接合；本节只把这项接合的所有输入
锁为明确的 exact-conductor-$p^2$ 双字，旧字符部分已严格消去。


## 9. 第一输出字、实际 CM 类与同一正权向量

本节把(29)的第一输出投影落实到真实 CM 标记及其微分。
使用 AI2024 的局部 Gauss--Manin/VBMS、marked differential
和 CM splitting 规范，不预认其全局 $L_p$ 定理的 tame-level
假设已经满足。原 $w_0$ 的 tame level 含惰性2及原 full9，
不能直接满足 $ \mathcal O_K/\mathfrak N\simeq\mathbf Z/N $
的 Heegner 条件。全部局部构造在保原 full2/full9 的共同
prime-to-$p$ full-level 有限 étale 模空间上拉回；通用椭圆曲线、
GM连接、极化KS、canonical subgroup 与 marked torsor 均随之
拉回。整数权的本节恒等式因而可在那里逐点使用，不需要丢掉
原 tame 向量，也不需要声称存在符合 AI 全局假设的新 $L_p$。

它不借局部 Hom 的维数猜一个 toric scalar，也不把这些新
exact-$p^2$ 读者命名为原未分歧 canonical $J'$。
临界解析延拓及斜率另按同一实际有界来源处理；这里首先证明
全部非负整数权的精确向量式。

### 9.1 列、行和原换极化的完整共轭

沿原双 Hermite 来源的(13a)--(13c)，以列记原 split plane：
$e_+=(\omega,1)^T$、$e_-=(\bar\omega,1)^T$，
$v_{\rm col}=u e_++v e_-$。取
$t=A+B\delta=a+b\omega$，其中 $a=A+B,b=2B$，
并保留 R1058 的真实 book 矩阵。令
$$
 P=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 g_t=\begin{pmatrix}A+B&2B\\-2B&A-B\end{pmatrix},
 \qquad
 g_{\rm col}=Pg_tP
 =\begin{pmatrix}a-b&-b\\b&a\end{pmatrix}.
 \tag{32}
$$
于是 $g_{\rm col}e_+=t e_+$、$g_{\rm col}e_-=\bar t e_-$。
这也真来自原未缩放列：若
$\tau'=\omega/34$，
$$
 D=\operatorname{diag}(2,1/17),\qquad
 g_{\tau'}=\begin{pmatrix}a-b&-b/34\\34b&a\end{pmatrix},
 \qquad Dg_{\tau'}D^{-1}=g_{\rm col}.
$$
它正是原(13a)的坐标变换；(13c)的固定 $[\omega]$ 换极化
与该 CM torus 交换。原 $a=17/2$、加性角色、Haar 及完整
2/3/17 相位均未更换。

Chan 的(6.12)、(7.1)使用行向量及右作用
$v\mapsto h^{-1}vg$。因此这里必须取
$$
 v_{\rm Ch}=v_{\rm col}^{\,T},\qquad
 g_{\rm Ch}=g_{\rm col}^{\,T}=Pg_t^{\,T}P,\qquad h=\bar t .
 \tag{33}
$$
不是将列矩阵原封不动用于右作用。严格有
$$
 h^{-1}v_{\rm Ch}g_{\rm Ch}
   =(t/\bar t)u\,e_+^{\,T}+v\,e_-^{\,T}.
 \tag{34}
$$
这也与 book 的整 Möbius 式相容。令 $\tau=-z$，则
$$
 -M_{g_t}(z)=
 \frac{(A-B)\tau-2B}{2B\tau+A+B};
$$
右边正是行 $(\tau,1)g_{\rm Ch}$ 的坐标比。
原 $z_0=-\omega$ 遂对应同一个 $\tau_0=\omega$，
不是只在一个点比较两个特征值。

在当前好 $p$，$h$ 是单位，Chan 的 $L(h)$ 之体积因子为1，
原 splitting 与 binary source character 在这些单位上均不分歧。
完整换极化因而给
$$
 \boxed{\;
 \mathcal W_a\,\omega_\psi(\bar t,g_{\rm Ch})\,
      \mathcal W_a^{-1}
       =\rho_-(t/\bar t)\otimes1 .
 \;}
 \tag{35}
$$
本式的标量不是自由选取的。两边在完整 Heisenberg 群上的共轭
相同，故只可能相差常数；原整球在两边都固定，且
$\mathcal W_a$ 将它送到非零的 $v_0\otimes v_0$，
从而该常数严格为1。原球及 $p$ 球均被 $h$ 的单位重标保持，
故(35)适用于实际 $K$ 和通常剔除的整个矩阵(20)。

记
$$
 \mathcal C_2=
 \mathcal O_{K_p}^{\times}/
 \bigl(\mathbf Z_p^{\times}(1+p^2\mathcal O_{K_p})\bigr).
$$
Hilbert90 给
$\mathcal C_2\simeq T_2,\ [t]\mapsto t/\bar t$。
所以(29)的第一输出字正是对真实模 $p^2$ CM 标记作
$$
 \frac1{p(p+1)}
 \sum_{[t]\in\mathcal C_2}
       \theta(t/\bar t)^{-1}\,\omega_\psi(\bar t,g_{\rm Ch}) .
 \tag{36}
$$
全部 $p(p+1)$ 项及分母保持；没有将 $p$ 因子称为单位。

### 9.2 实际循环核和 AI 类的方向

R1058§6已从原 right action 核定
$g_2^2$ 的核为 $\langle\alpha_1\bmod p^2\rangle$。
先作 $g_t$ 再作 $g_2^2$，实际核为
$$
 C_t=\left\langle
 (A+B)\alpha_1-2B\alpha_2\bmod p^2
 \right\rangle=tC_0 .
 \tag{37}
$$
在同一 rational Tate 空间中，目标格是
$T(E)+p^{-2}\mathbf Z_p(t\alpha_1)$。
AI2024§3.4 规定 $a*E$ 的格为 $a^{-1}T(E)$，
故本式对应的局部 idèle 是
$a_{t,p}=t^{-1}$。这里的逆号已经由格计算确定。

若用 prime-to-$p$ integral ideal 代表该类，必须同时保留其
principal scalar、微分与全部 tame level 的改变。
不能把某个方便代表的矩阵重新叫作 $g_t$ 后省掉该 scalar。
下面在固定 rational isocrystal 与实际 CM 准同源中写交换图，
避免这一歧义。

### 9.3 真正的 determinant frame；为何 p² 基准没有多一个 p 幂

先核本篇(14)与 AI 的内在 CM 导数确为同一规范。
原 right action 的 Tate 基定义是
$$
 \alpha'=(\check\phi_*)^{-1}\alpha\,p^\ell g
         =d^{-1}\phi_*\alpha\,p^\ell g,\qquad d=\deg\phi .
 \tag{38}
$$
这里 $p^\ell g$ 是原定义选定的整矩阵。
使用 $\check\phi_*\phi_*=d$ 与 Weil pairing 的同源相容性，
两基的 pairing 比严格为
$$
 \frac{p^{2\ell}\det g}{d}.
 \tag{39}
$$
这可直接从作者2018原稿印页18、(27)之前的基定义推出，
无需把(27)的示意图对任意 determinant 单位作额外解释。

对单位 $g_t$，$d=1,\ell=0$，(39)为 $N(t)$。
对 $g_2^2=\operatorname{diag}(1,p^2)$，
$d=p^2,\ell=0$，则
$\alpha'=(q_C\alpha_1/p^2,q_C\alpha_2)$，(39)严格为1。
因此在原基及其真正 $g_2^2$ 商上，Tate pairing 归一相同；
不能把单位换基的 $N(t)$ 误换成这里的 $p^2$。

为把(39)直接带入 de Rham 账本，令 $e_i$ 为 $\alpha_i$ 经主极化与 Tate 比较所得的水平向量。
由 $\check\phi_*\alpha'=\alpha p^\ell g$，
$\phi^*e_i'=\sum_j(p^\ell g)_{ji}e_j$。
Poincaré 相容性给
$\langle\phi^*e'_1,\phi^*e'_2\rangle=d\langle e'_1,e'_2\rangle$，
左边是 $p^{2\ell}\det(g)\langle e_1,e_2\rangle$，再次得到(39)。
原基的绝对正号及 pairing 一取已经固定的
[R1056(16)](R1056-original-flat-amice-critical-slope-and-bol-primitive.md)，不另重选规范。

更明确地，以原 book 正号基的 pairing 为1，记一般标记的
pairing 单位为 $\kappa_\alpha$。极化给出的内在 KS 满足
$$
 \operatorname{KS}_{\rm pol}(\omega_{\rm can}^{\,2})
       =\kappa_\alpha\,dz_{\rm dR}.
$$
这是由 $\omega_{\rm can}=-z e_1+e_2$ 直接计算
$\langle\omega_{\rm can},\nabla\omega_{\rm can}\rangle
=\kappa_\alpha dz$ 得到的。
内在 KS 逆每次因而比 book 的 $dz$ reader 多 $\kappa_\alpha^{-1}$。
$\kappa_\alpha$ 是水平的，故逐次应用同一个 Gauss--Manin
连接与 CM splitting，得到
$$
 \theta(\delta_3^nF_0)(y_\alpha)
   =\kappa_\alpha^n\,
      \Omega_\alpha^{3+2n}
      (\mathcal D_3^nw_0)(E,\omega_E).
 \tag{40}
$$
$\mathcal D$ 在这里指通用椭圆曲线按极化 KS 定义的内在代数
Maass 算子。因 $(g_2^2)$ 不改 $\kappa_\alpha=1$，
(40)严格支付本篇(14)的内在解释，而非以等式定义一个新的
$r_n^{\rm alg}$。若另用有限层某个余切参数作 trivialization，
仍须连同其真实 frame 比例运输；本段没有把书中(5.75)的
另一个参数常数擅设为1。

改为 $yg_t$ 后，
$\Omega_{0,t}=\Omega_0/\bar t$、$\kappa_{\alpha g_t}=N(t)$。
令 $w=3+2n$，book 的完整 raised tensor 因子为
$$
 j_t(n)=N(t)^{-n}\bar t^{\,w}
       =\bar t^{\,3+n}t^{-n}.
 \tag{41}
$$
因此在全部正权中，完整 pullback 中的三项准确相消：
$N(t)^{-n}\bar t^w\cdot N(t)^n\cdot
(\Omega_0/\bar t)^w=\Omega_0^w$。
原 spherical 来源给独立核对
$\delta^nF_0(yg_t)=N(t)^n\bar t^{-w}\delta^nF_0(y)$。
特别 $t=c\in\mathbf Z_p^\times$ 时，raw 因子是 $c^{-3}$，
返回原 frame 的 scalar $j_t(n)$ 是 $c^3$；两者相消后才下降到 $\mathcal C_2$。
裸 $j_t(n)$ 本身不是该商的 character。

### 9.4 三个微分及同第一层的真实常数

固定第一层 $C_1=C_t[p]$，写
$q_C=q_C'\circ q_1$，其中
$q_1:E_0\to E_1$、$q_C':E_1\to E_C$。
严格区分：

1. 好整 Néron 微分 $\omega_C$，
   $q_C^*\omega_C=c_C\omega_0$；
2. basic AI 微分 $\omega_{2,C}$，由同一 marked dlog lift
   $\omega_{1,C_1}$ 唯一规定
   $(q_C')^*\omega_{2,C}=\omega_{1,C_1}$；
3. 按 AI2024 Remark5.5 公式运输的实际 idelic 标记微分
   $\omega_{a_t}= \iota_p(a_{t,p})^{-1}\omega_{2,a_t}$。

取 AI 的原嵌入，写 $\iota_p(t)=t$。
在固定 $C_1$ 的野轨道上，$t$ 的野部分属于
$\mathcal O_p^\times$，因此保持同一个第一层 conductor-$p$ 格。
这不是说线性乘法 $[t]$ 等于恒等。固定该 block 的一条
$C_{\rm ref}$，在实际准同源范畴取
$\phi_{C,\rm ref}=q_C'(q_{\rm ref}')^{-1}$。
其 degree 为1，且严格有
$\phi_{C,\rm ref}q_{\rm ref}'=q_C'$；
此交换图在共同 $E_1$ 上的箭头是身份，而不是 $[t]$。
这正是固定 rational isocrystal 后的 CM 变格运输。
拉回微分是单射，因此
$\phi_{C,\rm ref}^*\omega_{2,C}=\omega_{2,C_{\rm ref}}$，
未加 $a_{t,p}$ 标记的 $\omega_{2,a_t}$ 正是上面的
$\omega_{2,C}$。
由此，真实 idelic 标记在此坐标中为
$$
 \omega_{a_t}=t\,\omega_{2,C},\qquad
 q_C^*\omega_{2,C}=d_{C_1}\omega_0,\qquad
 u_{C_1}:=\Omega_0d_{C_1}.
 \tag{42}
$$
换 integral ideal 代表时，principal scalar 必须同时作用于
该交换图与微分；(42)的整个式子不改变。

(42)是一个 block 内的准确等式。对不同 $C_1$，
$\omega_{1,C_1}$ 及 $d_{C_1}$ 可以不同，下面保留全部 $p+1$ 个
实际值，不把它们合成一个猜测的 common period。

AI2024 Proposition5.9 给
$\omega_{2,C}=\Omega_{AI,C}\omega_C$，
$v_p(\Omega_{AI,C})=1/(p(p^2-1))$；
本篇(11)给 $v_p(c_C)=1/p$。
于是
$$
 d_{C_1}=\Omega_{AI,C}c_C,\qquad
 v_p(d_{C_1})=\frac p{p^2-1},\qquad
 u_{C_1}\in\mathcal O_{\mathbf C_p}^{\times}.
 \tag{43}
$$
该单位结论不把 $\Omega_{AI,C}$ 本身当成单位。

### 9.5 同一来源的逐点正权等式

记
$$
 A_n(a_t)=
  \delta_3^n(w_0^{[p]})(E_C,\omega_{a_t}),
 \qquad w_0^{[p]}=w_0-p^2V^2w_0,
 \qquad R_{0,n}=p^{2n}\theta(\delta_3^nF_0)(y).
 \tag{44}
$$
$V$ 是 AI Appendix A 的实际 $V_H=\phi^*/p$；
所以 $\mathcal D^nV^2=p^{2n}V^2\mathcal D^n$。
在 canonical conductor-$p^2$ 点，它的第二次 incoming 返回是
$(E_0,q_C^*\omega_{a_t})$。因此这里没有以外向图代替 AI 的
incoming 操作。

用 $\mathfrak R_{\rm new,n}(t)$ 表示本篇(9)第二项在
$yg_t$ 上，按(41)完整拉回到原基后的 scalar。
同样记
$\mathfrak R_{\rm bad,n}(t)
 =\mathfrak R_{\rm new,n}(t)-R_{0,n}$。
由(40)--(43)逐项得到
$$
 \mathfrak R_{\rm new,n}(t)
 =p^{-4}(c_C\Omega_0)^w
       (\mathcal D_3^nw_0)(E_C,\omega_C),
 \tag{45}
$$
以及真正的逐点比较
$$
 \boxed{
 p^{-4}u_{C_1}^{\,w}t^{\,w}A_n(a_t)
  =\mathfrak R_{\rm new,n}(t)-p^{-2}R_{0,n}
  =\mathfrak R_{\rm bad,n}(t)+(1-p^{-2})R_{0,n}.
 }
 \tag{46}
$$
为独立核旧项，$q_C^*\omega_{a_t}=td_{C_1}\omega_0$，
所以 AI 旧项乘左边外因子后为
$$
 p^{-4}(\Omega_0d_{C_1}t)^w
    p^{2n+2}(td_{C_1})^{-w}
       (\mathcal D_3^nw_0)(E_0,\omega_0)
   =p^{-2}R_{0,n}.
$$
这同时锁定 $p^{-2}$ 和通常剔除的负号。
逐点绝不能把 $A_n$ 直接等同 $\mathfrak R_{\rm bad,n}$。

### 9.6 Avatar、中心与 exact-p² 角色

若一个局部 $\theta$ 能同原固定 tame 类型、$\mu_6$ 与当前
无穷分量组成全局 Hecke character，则对应的 $p$ 处有限部分为
$$
 \chi_{{\rm fin},p}
    =\theta^{-1}\circ(t\mapsto t/\bar t),\qquad
 \operatorname{type}(\chi)=(3+n,-n),\qquad
 \chi_n=\chi N_K^n .
 \tag{47}
$$
于是由 $a_{t,p}=t^{-1}$ 和 AI§2.2 的 avatar 定义，
$$
 \widehat\chi_n(a_t)^{-1}
       =\theta(t/\bar t)^{-1}t^{\,3+2n}.
 \tag{48}
$$
这是与(46)实际匹配的权。book 的 $\bar t^{3+n}t^{-n}$
并没有被共轭成 $t^{3+n}\bar t^{-n}$：前者已经在(41)连同
Tate determinant frame 与 $\Omega_{0,t}$ 完整消费，(48)中
的 $t^w$ 来自另一项，即 Remark5.5 的标记微分。

对 $t=c\in\mathbf Z_p^\times$，Hilbert90 和有限 Weil 行动均为1；
在(48)中出现的 $c^w$ 与 $A_n(a_c)$ 的微分缩放 $c^{-w}$
严格抵消。这与(41)的 $c^3c^{-3}=1$ 是同一个来源的两种
trivialization，故整个 covector 真正降商。
同理，深单位改代表时，avatar、marked differential 和系数运输
必须一起变化，整个值不变。

(47)仅在实际 global-units 条件通过时称为全局 Hecke character。
局部每个 $\theta$ 的存在不保证它与原 full2/full9、$\mu_6$
和 infinity component 相容。未作该全局投影前，下面只是完整的
marked CM-evaluation covectors；公式仍逐点成立。
即使上述 global-units 条件通过，也不能据此调用 AI 的全局
$L_p$ 或 Theorem7.1：还须支付该定理的 Heegner tame-moduli、
$(c,N)=1$、实际形式及完整有限来源条件。
本题原惰性2/full9向量没有在这里被改成另一份 Heegner level。

### 9.7 野块旧项准确消去；全部 tame 向量保留

固定非平凡 $\vartheta\in\widehat T_1$，取一个延拓
$\theta_0\in\widehat T_2$。使用未分歧扩张的实际 Teichmüller
子群 $\mathcal T=\mu_{p+1}\subset T_2$，故
$T_2=\mathcal T\times T_1$。取 $\tau\in\mathcal T$ 和
$v\in T_1$，选实际 Hilbert90 lifts
$t_{\tau,v}=t_\tau s_v$，其中 $t_\tau/\bar t_\tau=\tau$，
$s_v\in1+p\mathcal O_{K_p}$ 为 norm-one 的 lift，且
$s_v/\bar s_v\equiv v\bmod p^2$。
不用假设 $\tau\mapsto t_\tau$ 是群截面；
在有限群中严格有
$\theta_0(\tau v)=\theta_0(\tau)\vartheta(v)$。
每个 $\tau$ 正对应一个 $C_1$。
定义原有限 reader
$$
 \mathfrak T_{\theta,n}
  =\frac1{p(p+1)}
      \sum_{[t]\in\mathcal C_2}
          \theta(t/\bar t)^{-1}\mathfrak R_{\rm bad,n}(t),
 \qquad \theta|_{T_1}=\vartheta .
 \tag{49}
$$
根据(35)--(36)，这是第一输出 $K_\theta$ 的同一整体来源读数，
包含其相伴的第二输出字；并非先把任一输出单独赋零。

$R_{0,n}$ 是原 spherical 向量的完整 pullback，故在该局部轨道
为常数。由于 $\sum_{v\in T_1}\vartheta(v)^{-1}=0$，
(46)中的整个旧项在(49)准确为0。因此对所有整数 $n\ge0$，
$$
 \boxed{
 \mathfrak T_{\theta,n}
  =\frac{p^{-4}}{p(p+1)}
     \sum_{\tau,v}
       \theta(\tau v)^{-1}
       u_\tau^{\,3+2n} t_{\tau,v}^{\,3+2n}
       A_n(a_{\tau,v}).
 }
 \tag{50}
$$
此处不需要把单个旧点值称为 flat 零。
若另带原 toric 外权，须先组成其同一 full-avatar 和，
或将该权留在(50)的整个输入里；不能将仅局部未加权的正交
偷移到一个任意加权和。

把实际野和记为
$$
 L_{\tau,n}=\frac1p
   \sum_{v\in T_1}\vartheta(v)^{-1}
      t_{\tau,v}^{\,3+2n}A_n(a_{\tau,v}).
$$
令 $\psi$ 跑遍 $\widehat{\mathcal T}$，并令
$\mathcal F_{\psi,\tau}=(p+1)^{-1}
\theta_0(\tau)^{-1}\psi(\tau)^{-1}$。
取 $\mathfrak A_n=\mathcal F(L_{\tau,n})_\tau$，
则(50)为完整 $p+1$ 维矩阵式
$$
 \boxed{
 (\mathfrak T_{\theta_0\psi,n})_\psi
   =p^{-4}\,
     \mathcal F\operatorname{diag}
          (u_\tau^{\,3+2n})_\tau\mathcal F^{-1}
          \mathfrak A_n .
 }
 \tag{51}
$$
所有 $1/p$ 都仍保留在 $L_{\tau,n}$ 中；
只有 $p+1$ 是单位。因为全部 $u_\tau$ 为单位，
(51)中除显示的 $p^{-4}$ 外的矩阵及其逆均为整单位矩阵。
这不给单条 $\theta$ 一个臆定的共同 scalar，也不由局部矩阵
满秩推出经过原 global projector 后的每个分量非零。

### 9.8 已完成范围及后继输入

本节新付的是(35)的完整 finite intertwiner、(37)的 class 方向、
(38)--(41)的真实 cup/KS 账本、(46)的逐点旧项费用和(50)--(51)
的精确正权向量。原 $p^4$ finite matrix、两输出字、所有 tame
projectors、Artin/Cor 和完整源均保留。

在临界端点使用(51)时，必须选择固定 residue/Teichmüller
分量，并以实际有限单位 $u_\tau$ 和所有 outer weights 支付同一
局部解析延拓；斜率还含 $2\log\langle u_\tau\rangle$、
外权导数及全部 Maass correction。不能仅由正整数同式任意
改造一个解析插值。R1058已付的 root-average 互绕可保这些完整
finite 字的行动，但没有将 root rotation 认成 CM 图。

当前固定曲线的 canonical 坏条件尚未给(49)的新增 ramified
toric covectors 为零。对完整 $p$-torus 再取 trivial average
只回(24)的旧分支，不能用这一平均重造 imprimitive norm 非零。
本节不声称得到课题的最终 forcing。

本节使用的原文位置：Chan,
*Period identities of CM forms on quaternion algebras*,
§6.4(6.12)、§7(7.1)；
Kriz 作者2018原稿 §2.4 的真实 Tate 基定义及书版
§7.3(7.13)、(7.19)的完整 tensor/KS 规范；
AI2024 §3.4、§5.1--5.3（尤其 Remark5.5）、Proposition5.9
及 Appendix A。
固定 classical $k=3$ 时，Definition4.24 的局部整数
$n_k(p)=2$；相应 GM/VBMS 估计在上述同一 tame étale cover
上的拉回保持，故没有使用 two-variable
$n_{\rm univ}\ge3$ 的不同半径断言。
这只支付局部输入的 conductor/半径门；
Definition5.7 的全局求和和 Theorem7.1 的 Heegner 条件仍另保。

原文链接：[Chan §6–7](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A307E84FB65A00F04D142EEAB168B2EE/S2050509420000213a.pdf/period_identities_of_cm_forms_on_quaternion_algebras.pdf)、[Kriz 2018 §2.4](https://arxiv.org/pdf/1805.03605)、[AI2024](https://ems.press/content/serial-article-files/48931)。原双 Hermite 固定坐标与全 tame 来源见[来源证明](../notes/2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md)。


## 10. 原新矩阵的绝对 CM 相位、完整 Weyl 和与真实 Jacobi 字

本节继续使用(19)、(24)的全部实际坐标、加性角色与 Haar。
它将该矩阵识别为一个有绝对相位的有限 Weil 算子，并把其
$p^2$ 项 coevaluation 写成真实 Heisenberg 平移。
这里的平移先发生在原完整 theta kernel 内；不把它称为
原 degree34 line bundle 的自同构，也不对平移后的各字赋予
新的 canonical 中央零。

### 10.1 正线的 CM 矩阵与绝对号

原两条 rank-one 坐标是
$u=A+\delta r$、$v=B+\delta s$；
它们的 canonical momenta 分别为 $-51A$、$+51B$。
在**正线**的列坐标 $(s,51B)^T$ 中，乘 $\delta$ 和乘
$t_0=(1+\delta)/2=1+\omega$ 的矩阵严格为
$$
 D_+=
 \begin{pmatrix}0&1/51\\-153&0\end{pmatrix},
 \qquad
 M_+=\frac{I+D_+}{2}
 =
 \begin{pmatrix}1/2&1/102\\-153/2&1/2\end{pmatrix}.
 \tag{52}
$$
例如 $t_0(B+\delta s)=(B-3s)/2+\delta(B+s)/2$，
直接给(52)。其 determinant 为1，
$M_+^2-M_++I=0$、$M_+^3=-I$；
$t_0^2=\omega$、$t_0^3=-1$。
所有分母均在当前 $R=\mathbf Z/p^2\mathbf Z$ 中可逆。

写 $\zeta=\psi_p(1/p^2)$，
$q(A,B)=51(A^2-4AB+B^2)/2$。
对 $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$
的本题正 Schrödinger 规范，其 unit-$b$ kernel 是
$p^{-1}\zeta^{(dA^2-2AB+aB^2)/(2b)}$。
代入(52)得到
$$
 \boxed{\quad
 \rho_+(t_0)_{A,B}=p^{-1}\zeta^{q(A,B)} .
 \quad}
 \tag{53}
$$
这里的相位已由原模型确定，而非重新选择 Weil 延拓。
确切地，对任意 $u\in R^\times$，
写 $x=x_0+pk$ 并先求全部 $k$ 和，得到
$\sum_{x\bmod p^2}\zeta^{ux^2}=p$；
所以本层 unit quadratic Gauss 归一为 $+1$。
另有不依赖平方根选择的完整旧球核对：
$$
 \begin{aligned}
 (\rho_+(t_0)v_0)(A)
 &=p^{-1}\zeta^{51A^2/2}
       \sum_{b\bmod p}\zeta_p^{-102Ab}\\
 &=v_0(A).
 \end{aligned}
 \tag{54}
$$
当 $p\mid A$ 时平方相位也是1。
这与§5、§8的原未分歧 splitting 和旧球锚完全一致。

以原配对
$\langle e_A^-,e_B^+\rangle=\delta_{A,B}$ 识别
$\mathcal S_-=\mathcal S_+^\vee$。
令
$\mathcal C=\sum_A e_A^-\otimes e_A^+$ 为其 coevaluation。
若 $u^-\otimes v^+$ 对应算子
$w\mapsto\langle u^-,w\rangle v^+$，
tensor 的系数矩阵要转置；由于 $q(A,B)=q(B,A)$，
这里转置不改变(53)，但不能将其改成逆矩阵。准确有
$$
 \boxed{
 K=\frac1p(1\otimes\rho_+(t_0))\mathcal C,\qquad
 K_\vartheta=
 \frac{\vartheta^{-1}(t_0)}p\,\mathcal C_\vartheta ,
 \quad
 \mathcal C_\vartheta
 =(P_{-,\vartheta}\otimes
   P_{+,\vartheta^{-1}})\mathcal C .
 }
 \tag{55}
$$
本式使用(29)的**负线标签** $\vartheta$。
若改用正线标签 $\theta=\vartheta^{-1}$，系数才写为
$p^{-1}\theta(t_0)$。它只依赖 tame 分量。
旧分量
$\mathcal C_0=p^{-1}v_0\otimes v_0$
给 $K_0=p^{-2}v_0\otimes v_0$，准确回(25)。
这给各有限 paired 字的绝对系数，不声称其全局投影非零。

这里还要区分字坐标配对与实际 Haar 配对。
原 $\operatorname{vol}(\mathbf Z_p)=1$，而每个
$A/p+p\mathbf Z_p$ 的体积为 $p^{-1}$，所以
$$
 \langle f_-,f_+\rangle_{\rm Haar}
    =p^{-1}\sum_A f_-(A)f_+(A),\qquad
 \mathcal C_{\rm Haar}=p\mathcal C,\qquad
 K=p^{-2}(1\otimes\rho_+(t_0))\mathcal C_{\rm Haar}.
 \tag{55a}
$$
因而(55)的 $p^{-1}$ 不能不经比较便用于另一种几何或 Serre
配对。下方完整 Weyl 和的 $p^{-2}$ 已使用全部这些费用。

### 10.2 固定正负 Weyl 定义后的全部 p² 项

在同一实际字基上定义
$$
 \begin{aligned}
 W_+(a,b)f(A)&=\zeta^{\,b(A-a/2)}f(A-a),\\
 W_-(a,b)f(A)&=\zeta^{-b(A-a/2)}f(A-a).
 \end{aligned}
 \tag{56}
$$
因此 $W_-(a,b)=W_+(a,b)^{-T}$。
负号来自真实负 Hermitian 模；它不是把两个 physical
Weil pairings 同向认同。正线的参数 $b$ 是 canonical momentum，
而负线相同参数 $b$ 对应 canonical momentum $-b$。

对 $a,b\bmod p$，$W_\pm(a,b)v_0$ 给两组互为对偶、
配对值为 $p$ 的基。完整求和严格给
$$
 \mathcal C=\frac1p\sum_{a,b\bmod p}
 W_-(\widetilde a,\widetilde b)v_0
 \otimes W_+(\widetilde a,\widetilde b)v_0 .
 \tag{57}
$$
两侧须使用同一对实际 lift。
改变 lift 会在两个因子中产生相反的中心相位，完整 tensor
不变。直接核对也很短：两个支撑先迫
$A\equiv B\equiv a\bmod p$，再对 $b$ 求和迫 $A=B\bmod p^2$；
留下的系数恰为1。

原 Egorov 恒等式
$\rho_+(M)W_+(v)\rho_+(M)^{-1}=W_+(Mv)$，
连同(54)，将(55)变成
$$
 \boxed{
 K=\frac1{p^2}\sum_{v\in\mathbf F_p^2}
       W_-(\widetilde v)v_0
       \otimes W_+(M_+\widetilde v)v_0 .
 }
 \tag{58}
$$
$M_+\widetilde v$ 必须先在 $R^2$ 中实际计算；
不能独立约化两个因子的 lift 而删除中心相位。

一个无需留下 lift 费用的精确参数化是：
取 $a,c=0,\ldots,p-1$，在 $R$ 中置
$b_-=51(2c-a)$、$b_+=51(c-2a)$。
于是 $M_+(a,b_-)^T=(c,b_+)^T$，故
$$
 \boxed{
 K=\frac1{p^2}\sum_{a,c\bmod p}
 W_-\bigl(a,51(2c-a)\bigr)v_0
 \otimes
 W_+\bigl(c,51(c-2a)\bigr)v_0 .
 }
 \tag{59}
$$
为固定两个容易混淆的符号，令
$A=a+pu$、$B=c+pv$。
该唯一非零 summand 的总指数为
$$
 \begin{aligned}
 &-b_-(A-a/2)+b_+(B-c/2)\\
 &\quad=
 \frac{51}{2}(a^2-4ac+c^2)
 +51p(a-2c)u+51p(c-2a)v\\
 &\quad=q(A,B)\pmod{p^2}.
 \end{aligned}
 \tag{60}
$$
第一行的负线指数有负号，第二因子仍用正线指数。
常数及 $u,v$ 两个系数分别核回原(19)，所以没有遗漏
一个额外 $\zeta$ 或 $1/p$。
(59)是完整 $p^2$ 项和；它没有把 $p^4$ 个原矩阵坐标删掉，
而是用每项的整个厚支撑同时返回全部这些坐标。

### 10.3 这些字确实是原来源的 Heisenberg/Jacobi 平移

先在原局部 Schwartz 模型中把有限字还原，而不猜一个
sigma 平移常数。基 $e_A$ 对应
$ {\bf1}_{A/p+p\mathbf Z_p}$，$v_0$ 对应
$ {\bf1}_{\mathbf Z_p}$。
对 $\epsilon=\pm1$ 定义完整 Heisenberg 算子
$$
 (\mathsf H_{\epsilon,p}(q,\xi)\phi)(x)
   =\psi_p\!\left(\epsilon\,\xi(x-q/2)\right)\phi(x-q).
 \tag{61}
$$
取 $q=a/p,\xi=b/p$，(61)在每个原 coset 上准确给(56)。
平移、调制和中心 $-\epsilon ab/(2p^2)$ 都保留。
它的乘法律为
$\mathsf H_\epsilon(v)\mathsf H_\epsilon(v')
 =\psi(\epsilon(\xi q'-q\xi')/2)\mathsf H_\epsilon(v+v')$，
所以正负两条中心 character 相反，正是(57)所需配对。
(61)不是只有相同支撑而未定相位的向量识别。

还须保全原 theta 积分中的 $h$。
固定其中一个实际 $h$ 和当前原 CM/tame 字，令
$\Psi_{\epsilon,h}$ 为原整球向量经过该处**全部** Weil 运输后的
全局 Schwartz 函数。
通过原 Egorov 关系，先把(61)的参数运输成
$v_{\epsilon,h}$；不能先穿过 $h$ 后仍使用未运输的参数。
在当前有限层，$v_{\epsilon,h}$ 只涉及实际有限 residue 字。

取一个 rational lift $(q_h,\xi_h)$：
其 $p$ 分量在这个有限模型上实现 $v_{\epsilon,h}$，
其余有限分量属于 $\Psi_{\epsilon,h}$ 的真实 Heisenberg 稳定子。
这样的 lift 由 CRT 给出：先取一个 prime-to-$p$ 整数，
使其倍数的平移和调制都固定原所有非 $p$ Schwartz；
再在模 $p^2$ 指定原参数。
完整有限 $h$ 类型的交仍是开稳定子。
这里没有删除任何非 $p$ 作用，稳定性是在实际原向量上使用的。

全局 theta functional 对 rational Heisenberg 群不变：
平移用 $x\mapsto x+q_h$ 重标整个有理和，
调制和中心用全局加性角色在 $\mathbf Q$ 上平凡。
因而得到准确的 Jacobi 返回
$$
 \boldsymbol\Theta\!\left(
   \mathsf H_{\epsilon,p}(v_{\epsilon,h})\Psi_{\epsilon,h}
 \right)
 =
 \boldsymbol\Theta\!\left(
   \mathsf H_{\epsilon,\infty}(-q_h,-\xi_h)
         \Psi_{\epsilon,h}
 \right).
 \tag{62}
$$
右边在实际无穷 Schwartz 函数上的作用完全显式：
$$
 \bigl(\mathsf H_{\epsilon,\infty}(-q_h,-\xi_h)
            \Psi_{\epsilon,h,\infty}\bigr)(x)
 =
 e^{-2\pi i\epsilon\xi_h(x+q_h/2)}
       \Psi_{\epsilon,h,\infty}(x+q_h).
 \tag{63}
$$
所以平移、Gaussian、coherent 参数及中心相位都在同一个式子中。
若使用原 $(r,s)$ 的 Hermite Gaussian，就将该**整个**
Gaussian/coherent 函数代入(63)，再作原完整 $h$ 积分。
若先改变 arch polarization，则先运输其完整 Schwartz，
不能把任意新 CM 点重新当作原 $\tau=\omega$ 的已分离 Gaussian。
不同 CRT lift 给同一(62)，原因仍是完整 theta automorphy，
不是略去一个可能的符号。

几何上，(62)是原 theta-group/Jacobi 特征的作用。
对原对称刚性化线丛 $\mathcal L_N$，
共同 $p$ 覆盖上的线丛为
$[p]^*\mathcal L_N\simeq\mathcal L_N^{\,p^2}$；
原 $v_0$ 字是 $[p]^*s$。
这里变量按原覆盖写为 $z=pz'$；没有将 $s(pz')$ 的首项
重新归一，其所有真实 $p$ 幂仍保留。
(56)作用在该 degree-$Np^2$ 线丛上，平移点属于实际
$E[p^2]$，其 $[p]$ 像才是底层 $E[p]$ 特征。
在原解析模型中也可直接看到：
把原周期格换成 $p\Lambda$ 后，原 $1/p$ characteristic
在这条覆盖上具有阶 $p^2$。
其 theta-group lift 由(61)--(63)确定，故相应的
Miller/刚性化费用也必须保留。

特别，本题负来源的原三挠平移、$\delta$ 拉回与正来源
不能同向混为一条 degree34 截面。
对负来源中每一条已经支付的实际 section，严格使用
$$
 [p]^*[\delta]^*=[\delta]^*[p]^*,\qquad
 \tau_T^*[\delta]^*
       =[\delta]^*\tau_{[\delta]T}^{\,*}.
 \tag{64}
$$
所以负侧覆盖上的点 $T$ 送回34层时是 $[\delta]T$，
而不是未经转换的同一个 $T$。
原两条三挠字及各自的 Miller 规范先完整运输，再按原来源相加。
(64)没有删掉它们或把 $D_{102}$ 换成一个裸 $D_{34}$。
这里的全局线丛与覆盖身份逐个未取完整无穷圆周投影的实际
$h$ 字及其真实框架使用，再保留原整个 $h$ 积分。
圆周投影后的双核不因此自动成为某个固定椭圆曲面乘积上的
全局 theta 截面；不能据后者的几何非零跳过这个投影。

由于 $p\nmid N$，一般的底层 $E[p]$ 平移并不属于
$\mathcal G(\mathcal L_N)$；
本节从未把(59)当成固定 $\mathcal L_{34}$ 的自同构和。

### 10.4 同一个全局来源的完整返回

记 $\mathfrak T_{\rm orig}$ 为原 binary theta 经已付换极化后的
整个线性 theta 操作：包括全部非 $p$ Schwartz、原 $h$ 积分、
实际 arch 运输、full2/full9、Artin/Cor 和所有原 fixed toric
projectors。其输入仍是两条 rank-one 有限函数的 tensor，
不是两个已经分别取过总 period 的标量。
由(59)--(63)，准确有
$$
 \boxed{
 W_p=\frac1{p^2}\sum_{a,c\bmod p}
 \mathfrak T_{\rm orig}\!\left(
  W_-\bigl(a,51(2c-a)\bigr)v_0
   \otimes
  W_+\bigl(c,51(c-2a)\bigr)v_0
 \right).
 }
 \tag{65}
$$
每个 summand 的真实 theta/Jacobi 输入由(61)--(64)规定。
原 bounded bad 输入则仍为 $-w_0+W_p$；
其旧项的号和所有 $p^{-2}$ 均未改变。

(65)先是完整 finite-Schwartz 恒等式，继而是原 theta 来源的
恒等式。因此可逐个非负整数 Maass 权、逐个 coherent 系数
以及 R1060 的**完整有限**转置使用它。
在这些操作中必须保原 $h$、$\Lambda(-2),\Lambda'(-2)$、
$\Omega_i,\kappa_i$ 和全部 $C_i$ 修正；
不能把冻结外权换成第 $n$ 槽的另一份外权。
同样，本节不从整个来源已知有界推出每个被单独切出的
rank-one factor 在同一圆盘上有界。
负端点和斜率的收敛仍按 R1056/R1059/R1060 的整个实际输入处理。

本节的新结论是(55)的绝对 CM phase、(59)--(60)的完整厚
Weyl 和以及(61)--(65)的实际 theta/Jacobi 来源。
全局 $t_0$ 若要从(55)的一处有限分量移往其它分量，须同时
运输其 arch、tame、source character 与原 $h$；
不能仅因 $t_0\in\mu_6$ 就将 $\vartheta^{-1}(t_0)$ 删除。
coevaluation 的进一步整体 isogeny/addition 返回也须作用在
上述真正 $[p]$ 线丛与全部 Miller 上。
这些后继尚不由(65)产生新的 canonical 坏条件。

本节为同一原矩阵的纸笔恒等式；没有数学执行，也没有重新计算
任何有限谱或原厚交作业。

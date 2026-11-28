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

# $K(Y)$ 全空间闭分式场与未知限制像稠密性之间的精确缺口

日期：2026-11-12（UTC）。作者：literature。独立边界笔记，不另占结果号。

状态：以下实际等价和纯代数模型均已证明。纯代数模型没有 Hilbert 拓扑，不是本课题实际不变子空间的反例，也不否定所有实际限制最终都有稠密像的可能性。

## 1. 实际限制问题可以准确归到一个有界像

沿用 R183 的非首一多项式
$$
P\in\mathcal G[t]\setminus\{0\},\qquad
\mathsf P=\overline{P_{\rm nat}(Y)}.
$$
固定 $R=R(t)$，$p=\deg P$，记
$$
B_P=\sum_{j=0}^p g_j(YR)^jR^{p-j}.
$$
其全空间最大图是
$$
B_Px=R^py.
\tag{1.1}
$$
$B_P$ 与 $R$ 都全空间单射稠密，但当前只有 $R^p$ 已知在全部不变限制及有限放大上稠密。

设 $M\in\operatorname{Lat}A$。
R183 的域保持证明给
$$
\mathsf P(\operatorname{Dom}\mathsf P\cap M)\subseteq M.
$$
所以
$$
\mathcal L_M=\operatorname{Graph}\mathsf P\cap(M\oplus M)
$$
是闭 $A\oplus A$ 不变图。
固定 $(R^p)^{(2)}$ 在它上面稠密，且
$$
(R^px,R^py)=(R^px,B_Px)
$$
是以 $x\in M$ 为参数的图向量。
因此
$$
\boxed{
\mathcal L_M
=\overline{\{(R^ph,B_Ph):h\in M\}}.
}
\tag{1.2}
$$
由两个坐标分别投影，
$$
\boxed{
\overline{\operatorname{Dom}\mathsf P\cap M}=M,\qquad
\overline{\mathsf P(\operatorname{Dom}\mathsf P\cap M)}
=\overline{B_PM}.
}
\tag{1.3}
$$
这与 R140 对第一阶 $Y$ 的固定有界正则化完全相容。

所以目前真正未证的命题是
$$
\overline{B_PM}=M
\qquad
\text{对所有非零 }P\in\mathcal G[t]\text{ 和所有 }M.
\tag{1.4}
$$
$P=t$ 就已包含一般复杂第一阶的未知限制值域问题。

## 2. 不稠密会产生什么实际子商

令
$$
N=\overline{B_PM}\subseteq M.
$$
这是闭 $A$ 不变空间。
如果 $N\ne M$，则非零子商 $Q=M/N$ 上有
$$
(B_P)_Q=0.
\tag{2.1}
$$
通用正则器 $R_Q$ 仍单射且稠密；
所以由同一有界方程定义的最大闭多项式实现
$$
(B_P)_Qx=R_Q^py
$$
变成全域零算子。

这个零算子结论只属于该最大图。
对高次多项式，不能反向声称子商中未经闭包的自然幂已经闭，
也不能由原空间的 $C$ 自伴性给子商补上一个未构造的共轭。

$P=t$ 时情况尤其明确：
该子商的一阶最大闭实现就是全域零算子。
这并不与原空间的 $Y$ 单射矛盾，
因为商中的“$Yx=0$”允许原向量的像落入 $N$。

R23/R140 还使 $A_Q$ 单射、稠密像、拟幂零。
因此这个非零 $Q$ 必须无限维。
所以任何实际失败的限制值域缺陷都自动是无限维，
不能是有限维余核。

## 3. 全空间闭场没有自动给所有限制饱和

R183 证明每个非零 $T_f$ 在全 $H$ 上单射稠密，
并有
$$
\overline{T_fT_{1/f}}=I.
$$
这个闭包是在原空间的自然乘积域上取的。

若只知道 $x\in M\cap\operatorname{Dom}T_{1/f}$，
当前没有证明 $T_{1/f}x\in M$。
因此不能把全空间的逆图逼近限制到 $M$，
再宣称得到 $I_M$ 的强近似。

同样，R183 的有界 gcd 因子在恢复原分母图核心时，
只用了它的全空间稠密像。
在 $M$ 上重复这个步骤，恰好会重新要求未知的
$\overline{B_PM}=M$，形成循环论证。

对于一个既约 Bézout 恒等式，
右边若是 $D R^N$、$0\ne D\in\mathcal G$，
它确实在所有不变图中稠密。
这给有限族的共同关系，
不能把这个强性质分配给其中每一个非零多项式分母。

## 4. 保留全部场运算与半线性作用的纯代数障碍

下面模型专门隔离“全局已是场”仍不推出“一个子模对每个分母饱和”。

取本题相同的代数域 $K$、同一个形式原函数 $\beta_Y$，
以及增量
$$
h_\zeta=\alpha_\zeta\beta_Y-\beta_Y\in K.
$$
R180 给 $\beta_Y$ 超越于 $K$。
令抽象有理函数域
$$
\mathbb F=K(t),\qquad \mathbb M=K[t]\subset\mathbb F.
$$
把 $\mathbb F$ 作为 $\mathbb C$ 向量空间。
每个非零 $f\in\mathbb F$ 在整个 $\mathbb F$ 上的乘法都是双射。
所以全部非零标量多项式乃至全部有理函数，
都在这个全空间上没有核、没有像缺陷，场运算精确成立。

把本题的半线性作用延拓为
$$
\Lambda_\zeta r(t)
=(\alpha_\zeta r)(t+h_\zeta)
\quad(r\in\mathbb F).
\tag{4.1}
$$
它是 $\mathbb C$ 线性可逆变换，并保持 $\mathbb M$。
乘法算子满足准确 gauge 协变
$$
\Lambda_\zeta M_f\Lambda_\zeta^{-1}=M_{\Lambda_\zeta f}.
\tag{4.2}
$$

每个 $0\ne d\in K$ 在 $\mathbb M$ 上也是双射。
所以这个子模已经对全部快基域分母完全饱和。

然而乘以 $t$ 的限制只有像
$$
tK[t]\subsetneq K[t].
\tag{4.3}
$$
例如 $1$ 不在这个像中，尽管全域逆 $1/t$ 在 $\mathbb F$ 上完全存在。
更一般地，对任意正次数多项式 $P$，
$$
P(t)K[t]\subsetneq K[t],
\qquad
\dim_K K[t]/P(t)K[t]=\deg P.
\tag{4.4}
$$

这不与半线性单环结论矛盾。
理想 $(P)$ 通常不被全部 $\Lambda_\zeta$ 固定；
其全部轨道生成的是单位理想。
确实存在有限证书
$$
1=\sum_iU_i(t)\Lambda_{\zeta_i}P(t),
\qquad U_i\in K[t].
\tag{4.5}
$$
(4.5) 在 $\mathbb M$ 上给有限族总像等于 $\mathbb M$，
但 (4.3)—(4.4) 的每个单独像仍是真子模。

## 5. 该模型说明什么、没有说明什么

模型同时保留：

- 全空间上全部非零分式精确可逆；
- 对基域 $K$ 的全部分母饱和；
- 本题相同的加性半线性 gauge 作用；
- 无非零真稳定理想；
- 有限轨道单位证书和有限族总像满。

这些代数性质仍不能推出单个 $t$ 或 $P(t)$ 在子模上的满射性。
所以仅把 R183 的闭场等式或 R166 的轨道证书重复用于未知 $M$，
不足以证明 (1.4)。

本模型没有给 $\mathbb F$ 或 $\mathbb M$ 配置 Hilbert 范数。
它没有证明 $P(t)\mathbb M$ 在某个相关 Hilbert 拓扑中不稠密，
也没有共同 $C$、实际 Haar 表示或正交投影。
特别，$\mathbb M$ 在模型中被全部 gauge 保持；
若把这种性质直接搬进真实 Haar Hilbert 模型，
字符 MASA 与 odometer 遍历性会施加模型所不具有的强限制。

因此这只是严格的形式饱和障碍，
不是实际反例。
实际需要的新输入仍是对未知不变空间的单分母范围控制；
R183 的全空间闭场本身没有提供它。

## 6. 当前可合法使用的实际结论

对每个非零 $P\in\mathcal G[t]$：

1. 原空间的 $\mathsf P$ 已单射、稠密像、$C$ 自伴；
2. 任意闭 $A$ 不变 $M$ 上，其自然最大限制稠密定义、像保持 $M$，并有 (1.2) 的原正则分母图核心；
3. 限制像闭包准确等于 $\overline{B_PM}$；
4. 若它不等于 $M$，就产生 (2.1) 的无限维实际不变子商；
5. 有限 gauge 轨道的快证书控制共同核和总像，仍不控制某个指定成员的单独像。

本笔记不登记新的排核或限制像稠密定理，也不改变 R180/R183 已完成的范围。

# 一个具体的三次指标覆盖：Z = -283

日期：2026-11-12；关联：R37、R42、R46。

**用途与认证边界。** 本例展示 R46 的全局 Mordell–Weil/Sha 筛可以真正非空。类群、三次域、指标形式和局部点的计算在下面展开；唯一未在本文独立重算的输入是 $y^2=x^3-283$ 的秩为零。该输入来自 von Känel–Matschke 作者公布并声明已无条件核实的完整 Mordell–Weil 基数据库；本会话核对了相应条目，但没有取得独立可重放的下降证书。因此下面的“无有理点”结论依赖明确标出的外部秩计算，不应称为本笔记的自含证明。

本例也**不是新增的大素数排除**。它使用的指数剩余类为 $p\equiv1\pmod6$，而 R13 对 $Z=-283$ 的唯一 $p>37$ 候选是 $71\equiv5\pmod6$；此外 R37 的判别式下界早已排除这个小平方自由部分。

## 1. 类群商确实非零

取 R19 族 I 的参数
$$
Z=-283,\qquad c=1,\qquad e=1.
$$
因为 $Z\equiv1\pmod4$，对应二次域为
$$
F=\mathbb Q(\sqrt{-283}),\qquad D_F=-283.
$$

判别式 $-283$ 的全部约化原始正定二元二次型为
$$
(1,1,71),\qquad (7,-5,11),\qquad (7,5,11).
\tag{E.1}
$$
可以通过
$$
|b|\le a\le c,\qquad b^2-4ac=-283,\qquad
a\le\sqrt{283/3}<10
$$
逐项检查；边界情形使用约化型通常的正号约定。因此
$$
\operatorname{Cl}(F)\simeq C_3.
$$

又因 $D_F\equiv5\pmod8$，素数 $2$ 惰性，其上方素理想是主理想 $(2)$。素数 $283$ 在 $F$ 分歧，唯一上方素理想 $\mathfrak q$ 满足
$\mathfrak q^2=(283)$，所以其类的阶整除 $2$；类群阶为 $3$，故此类也平凡。因此 R37 的指定商没有变小：
$$
G_0=\operatorname{Cl}(F)/
\langle[\mathfrak q]:\mathfrak q\mid2\cdot283\rangle
\simeq C_3,
\qquad V_0\simeq\mathbb F_3.
\tag{E.2}
$$

## 2. 三次域和指标形式

取
$$
h(T)=T^3+4T+1.
$$
有
$$
\operatorname{disc}(h)=-4\cdot4^3-27=-283.
$$
由有理根判据，可能的整数根只有 $\pm1$，而两者都不是根，所以 $h$ 不可约。其判别式为平方自由数，故
$$
L=\mathbb Q(\theta),\qquad h(\theta)=0,\qquad
\mathcal O_L=\mathbb Z[\theta],\qquad D_L=-283.
\tag{E.3}
$$

模 $2$，
$$
h(T)\equiv(T+1)(T^2+T+1).
$$
所以 $2$ 的局部分解群为 $C_2$，在二次预解式域上完全分裂。判别式在 $283$ 处的赋值为 $1$，该处只有温和二次分歧；局部分解群正规化这一 $C_2$ 惯性子群，故亦至多为 $C_2$。其余素数未分歧。于是这个 $S_3$ 分裂域给出 (E.2) 的唯一非平凡循环三次类域。

相对于整基 $(1,\theta,\theta^2)$，直接由
$\theta^3=-4\theta-1$ 计算得指标形式
$$
I_L(u,v)=u^3+4uv^2+v^3.
\tag{E.4}
$$
例如，$\theta$ 与 $\theta^2$ 两个坐标列的行列式展开即为右边；它的判别式仍为 $-283$。

## 3. 相应覆盖和全部局部点

R46 在 $e=1$ 给
$$
a=-283,\qquad \mu_1=2,
$$
因此覆盖是
$$
\boxed{
C:\quad u^3+4uv^2+v^3=2t^3
\subset\mathbb P^2.
}
\tag{E.5}
$$
其 Jacobian 为
$$
B:\quad y^2=x^3-283,
$$
三同源目标为
$$
D:\quad V^2=U^3+7641.
$$

R46 已由 (E.2) 证明 $C$ 处处局部可解。本例还可以独立检查：

- 在 $\mathbb R$，取 $(u:v:t)=(\sqrt[3]2:0:1)$。
- 在 $\mathbb Q_2$，固定 $v=t=1$；多项式 $u^3+4u-1$ 在 $u=1$ 处为 $4$，导数为 $7$。其模 $2$ 简单根可 Hensel 提升。
- 在 $\mathbb Q_3$，固定 $v=1,t=-1$；多项式 $u^3+4u+3$ 在 $u=0$ 处为 $3$，导数为 $4$。同样可提升。
- 在 $\mathbb Q_{283}$，$h$ 模 $283$ 的重根为 $35$，另有简单根 $213$，且 $h'(213)\equiv-12\not\equiv0\pmod{283}$。简单根提升给 $I_L(u,1)=0$，即 $C$ 的 $t=0$ 局部点。
- 对其他素数 $\ell$，(E.5) 的射影约化光滑。有限域上 genus $1$ 曲线的点数至少为 $\ell+1-2\sqrt\ell>0$；取一个光滑点并 Hensel 提升即可。

故本例的局部可解不依赖秩数据库。

## 4. 外部完整基数据中的秩零输入

数据来源为 Rafael von Känel 与 Benjamin Matschke 的论文配套页面：

- [作者数据页](https://bmatschke.github.io/solving-classical-diophantine-equations/)，Mordell equation 一节。
- [完整 Mordell–Weil 基数据 mwMordell10000.sobj](https://bmatschke.github.io/solving-classical-diophantine-equations/mordell-weil-bases/mwMordell10000.sobj)。

作者页面说明该文件列出全部 $|a|\le10000$ 的 $y^2=x^3+a$ 的完整有理 Mordell–Weil 基；它基于 Gebel–Pethő–Zimmer 的数据库并补正若干条目，页面明确声明修订后结果已无条件核实。

本会话实际读取并解析了该作者文件，其中
$$
a=-283\quad\longmapsto\quad []
\tag{E.6}
$$
即自由部分的基为空。这里不是从“没有找到小点”推断秩零，也不是把无整数解误当成无有理点。

使用这一作者公开数据输入，得
$$
\operatorname{rank}B(\mathbb Q)
=\operatorname{rank}D(\mathbb Q)=0.
$$
R46 还已证明此参数没有有理 $3$ 挠点，故
$$
D(\mathbb Q)/\phi B(\mathbb Q)=0.
$$
结合 (E.2)，有 $W_1=0$，所以
$$
C(\mathbb Q)=\varnothing,\qquad
0\ne V_0\hookrightarrow\Sha(B/\mathbb Q)[\phi].
\tag{E.7}
$$

这就展示了一个实际候选类域满足全部该类域层面的局部条件，但在有理指标覆盖这一步被全局障碍排除的例子。其无有理点结论的外部计算依赖已在本节完整注明；本文没有声称独立重算或重新认证了 (E.6)。

## 5. 为什么它不增加大 p 的排除范围

R13 对分母素数 $q=283\equiv3\pmod4$ 要求
$$
p\mid q+1=284=4\cdot71.
$$
所以唯一的 $p>37$ 候选是 $p=71$，而
$$
71\equiv5\pmod6.
$$
它对应的 Mordell 曲线是 $B_{-283^5}$，不是本例使用的 $B_{-283}$；不能将后者的秩零转移给前者。

此外，普通虚二次分支的 R37 下界要求
$$
283\ge\pi^2p^4/1024,
$$
对全部素数 $p>37$ 已经不成立。所以这个 $Z$ 本来就已排除。

本例的实质是验证 R46 的三次覆盖/Sha 障碍确会出现，及说明“类群商非零”与“存在有理指标点”之间确有差距。它不声称给出新的统一素数界或一个尚未被其他结果排除的大指数参数。

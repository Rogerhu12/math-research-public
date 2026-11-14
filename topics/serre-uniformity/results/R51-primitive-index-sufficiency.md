# R51：高次指标点的原始性自动恢复与精确充分条件

日期：2026-11-12；会话：serre-uniformity-astra-resume2；分支：cm-denominators。

**状态：已证明的等价归约。** R42、R46 把固定 CM 同余曲线送到三次指标覆盖，但保留了“指标点还须满足原始整数条件”的接口。本篇证明：对于候选最大整环中的原始指标坐标，只要指标右端具有实际要求的高次幂，全部奇素数处的原始性已经自动成立。最终充分条件只额外保留一个模 $3$ 的线性条件及至多一个二进条件。本文没有证明这些原始指标点在所有充分大指数不存在，因此不完成固定 CM 刚性或 Serre 一致性。

## 1. 参数与候选三次域

固定素数 $p>37$、$p\equiv3\pmod4$，以及带符号整数 $Z$，满足
$$
|Z|>1,\qquad (Z,6p)=1.
$$
写
$$
p=6k+e,\qquad e\in\{1,5\},\qquad
d_0=\operatorname{sf}(Z),\qquad Z=d_0z_0^2,\quad z_0>0.
$$
选择 R19 的四个分支之一，并按 R37、R42 取一个真正的候选非 Galois 三次域 $L$。其正规闭包 $H$ 在二次预解式域 $F$ 上为循环三次，具有下表的分歧和分裂性质：

| 分支 | $c$ | $F$ 及 $D_F$ | $D_L$ | $H/F$ 的条件 |
|---|---:|---|---|---|
| I | $1$ | $F=\mathbb Q(\sqrt{d_0})$，$D_F=d_0$，$d_0\equiv1\pmod4$ | $d_0$ | 处处不分歧，$2Z$ 上方全分裂 |
| II | $8$ | $F=\mathbb Q(\sqrt{2d_0})$，$D_F=8d_0$ | $8d_0$ | 处处不分歧，$2Z$ 上方全分裂 |
| III，奇 $X$ | $1$ | $F=\mathbb Q(\sqrt{d_0})$，$D_F=4d_0$，$d_0\equiv3\pmod4$ | $4d_0$ | 处处不分歧，$2Z$ 上方全分裂 |
| III，偶 $X$ | $1$ | $F=\mathbb Q(\sqrt{d_0})$，$D_F=d_0$，$d_0\equiv5\pmod8$ | $4d_0$ | 导子恰为 $(2)$，$Z$ 上方全分裂 |

这里“候选”是指 R42/R46 的实际类群或射线类群字符所给出的域，而非只指定一个形式判别式。特别地，$L$ 是域；普通分支的 $L\otimes\mathbb Q_2$ 有一个 $\mathbb Q_2$ 因子，射线分支的 $L\otimes\mathbb Q_2$ 是温和全分歧三次域。对每个奇 $q\mid Z$，都有
$$
L\otimes\mathbb Q_q\simeq\mathbb Q_q\times F_q
\quad\hbox{或}\quad\mathbb Q_q^3,
\tag{51.1}
$$
其中 $F_q$ 可以是分歧或不分歧二次域。在奇分歧处，$v_q(D_L)=1$。

取最大整环的任意整基 $(1,\omega,\eta)$，令 $I_L(u,v)$ 为 R42 定义的带符号三次指标形式。设
$$
J_e=|Z|^{(e-1)/2}z_0,\qquad
\mu_e=
\begin{cases}
2J_e,&\text{I、II},\\
J_e,&\text{III 两支}.
\end{cases}
\tag{51.2}
$$
由表中判别式直接得到
$$
D_L\mu_e^2=4cZ^e.
\tag{51.3}
$$

## 2. 精确充分条件

**定理 51.1。** 在上述设定下，假定整数 $u,v$ 满足
$$
\gcd(u,v)=1,\qquad
I_L(u,v)=\pm\mu_e|Z|^{3k},
\tag{51.4}
$$
以及一个显式线性条件
$$
u\operatorname{Tr}_{L/\mathbb Q}(\omega)
 +v\operatorname{Tr}_{L/\mathbb Q}(\eta)
\equiv0\pmod3.
\tag{51.5}
$$
令
$$
\theta=u\omega+v\eta
-\frac{u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)}3,
\quad
X=\frac{\operatorname{Tr}(\theta^2)}2,
\quad
W=\frac{N_{L/\mathbb Q}(\theta)}2.
\tag{51.6}
$$
则 $X,W$ 均为整数，而且下表中所列的条件，恰为从 (51.4)、(51.5) 得到相应 R19 原始整数族所剩的全部附加条件：

| 分支 | 仍须单独检查的条件 |
|---|---|
| I | 无 |
| II | $X$ 奇 |
| III，奇 $X$ | 无 |
| III，偶 $X$ | $X\equiv2\pmod4$ |

满足相应条件后，自动有
$$
X^3-27W^2=cZ^p,
\qquad
3\nmid X,
\qquad
\gcd(X,W)=\gcd(X,Z)=\gcd(W,Z)=1,
\tag{51.7}
$$
以及 R19 该行的全部奇偶性和模 $4$ 条件。因此由 R19 的已证充分方向，确实得到一条非 CM 曲线 $E/\mathbb Q$，满足
$$
E[p]\simeq A[p],\qquad A:y^2=x^3-x.
\tag{51.8}
$$

反过来，每个相应 R19 解都在其 R42 三次域和任意上述整基中给出满足 (51.4)、(51.5) 及表中条件的一对 $(u,v)$。因此在每个固定 $Z,p$ 和分支上，这是一组完整的必要且充分的指标点条件，不仅是必要条件。

这里没有把 $C_{L,e}(\mathbb Q)\ne\varnothing$ 当成 (51.4)。式 (51.4) 仍要求**整数**原始坐标和精确的 $|Z|^{3k}$，不能用任意有理覆盖点代替。

## 3. 迹零整元和方程的恢复

由 (51.5)，式 (51.6) 中所减去的数是整数，故 $\theta\in\mathcal O_L$，且 $\operatorname{Tr}(\theta)=0$。

式 (51.4) 右边非零，所以 $1,\theta,\theta^2$ 线性无关，$\theta$ 生成 $L$。因此其首一最小多项式为
$$
g(T)=T^3-XT-N(\theta),
$$
其中 $X\in\mathbb Z$；Newton 恒等式给 $X=\operatorname{Tr}(\theta^2)/2$。

平移不改变指标，故 R42 的指标—判别式恒等式和 (51.3) 给
$$
\operatorname{disc}(g)
=D_LI_L(u,v)^2
=4cZ^e|Z|^{6k}
=4cZ^p.
\tag{51.9}
$$
另一方面
$$
\operatorname{disc}(g)=4X^3-27N(\theta)^2.
$$
其值被 $4$ 整除，故整数 $N(\theta)$ 必为偶数。因此 $W=N(\theta)/2\in\mathbb Z$，且
$$
g(T)=T^3-XT-2W,\qquad X^3-27W^2=cZ^p.
\tag{51.10}
$$
又 $(3,cZ)=1$。对 (51.10) 取模 $3$，立即得到 $3\nmid X$。

注意：不能在未检查 (51.5) 时就把一个整元除以迹的三分之一。此时通常只得到 $L$ 中的有理元素，可能在 $3$ 处有分母。本定理保留该线性条件，未将它隐去。

## 4. 关键局部引理：原始整元的共同因子只能产生三次判别式赋值

**引理 51.2。** 设 $q\ge5$，$L$ 为三次域，且
$$
v_q(D_L)\in\{0,1\}.
$$
当 $v_q(D_L)=1$ 时，另假定
$$
L\otimes\mathbb Q_q\simeq\mathbb Q_q\times K,
$$
其中 $K/\mathbb Q_q$ 为分歧二次域。设 $\theta\in\mathcal O_L$ 迹为零，其在整基 $(1,\omega,\eta)$ 中的两个非平凡坐标 $u,v$ 不同时被 $q$ 整除。将最小多项式写为
$$
T^3-XT-2W.
$$
若 $q\mid X,W$，则必有
$$
v_q(D_L)=1,\qquad
\boxed{v_q(\operatorname{disc}(\theta))=3.}
\tag{51.11}
$$

**证明。** 先设 $v_q(D_L)=0$。此时 $\mathcal O_L/q\mathcal O_L$ 为有限 étale $\mathbb F_q$ 代数，故无非零幂零元。由 $q\mid X,W$，$\theta$ 模 $q$ 满足 $T^3=0$，所以 $\theta\equiv0\pmod{q\mathcal O_L}$。按整基展开即得 $q\mid u,v$，矛盾。

因此只能 $v_q(D_L)=1$。因 $q$ 奇，可写
$$
K=\mathbb Q_q(\pi),\qquad
\pi^2=q\varepsilon,\qquad
\varepsilon\in\mathbb Z_q^\times,
\qquad
\mathcal O_K=\mathbb Z_q\oplus\mathbb Z_q\pi.
$$
在最大整环的局部分解中写
$$
\theta=(r,s+t\pi),\qquad r,s,t\in\mathbb Z_q.
$$
迹为零给 $r=-2s$。直接相乘得
$$
\begin{aligned}
g(T)
 &=(T+2s)\big((T-s)^2-q\varepsilon t^2\big)\\
 &=T^3-(3s^2+q\varepsilon t^2)T
   +2s(s^2-q\varepsilon t^2).
\end{aligned}
\tag{51.12}
$$
所以
$$
X=3s^2+q\varepsilon t^2.
$$
$q\mid X$ 且 $q\ne3$ 强迫 $q\mid s$，故 $q\mid r$。若再有 $q\mid t$，则 $\theta\in q(\mathcal O_L\otimes\mathbb Z_q)$，与 $u,v$ 的局部原始性矛盾。因此 $t$ 为单位。

三个根分别是 $-2s,s+t\pi,s-t\pi$。其差的平方之积为
$$
\operatorname{disc}(\theta)
=4q\varepsilon t^2(9s^2-q\varepsilon t^2)^2.
\tag{51.13}
$$
因为 $q\mid s$ 而 $t,\varepsilon$ 为单位，括号的赋值恰为 $1$；式 (51.13) 的赋值遂为 $1+2=3$。证毕。

本证明明确使用最大整环。若把高指标的 $\mathbb Z[\theta]$ 当作最大整环，便无法得到其中的原始性信息。

## 5. 全部奇素数处的原始性自动成立

假设某个奇素数 $q$ 同时整除 $X,W$。由 $3\nmid X$，有 $q\ge5$。由 (51.10)，$q\mid Z$。候选三次域在该处具有 (51.1) 的结构，奇判别式指数为 $0$ 或 $1$，所以引理 51.2 适用。式 (51.4) 的 $\gcd(u,v)=1$ 给该引理所需的局部原始性。

于是引理强迫
$$
v_q(\operatorname{disc}(g))=3.
$$
然而 (51.9) 给
$$
v_q(\operatorname{disc}(g))=p\,v_q(Z)\ge p>37,
$$
矛盾。因此 $\gcd(X,W)$ 没有奇素因子。

另外，若奇素数 $q\mid Z$ 整除 $X$ 或 $W$ 之一，(51.10) 模 $q$ 和 $q\ne3$ 会迫使它也整除另一个。这已被排除。因此
$$
\gcd(X,Z)=\gcd(W,Z)=1
$$
在全部奇素数处成立。$Z$ 本来就是奇数，所以这两条互素式已完整成立。

这个证明没有给出 $q$ 或 $Z$ 的上界。它只证明：**原始指标坐标加上超过三的判别式赋值，排除了系数端的奇共同因子。**

## 6. 二进条件：只剩两种分支的一位检查

由 (51.10)，当 $c=1$ 时 $X,W$ 奇偶相反；当 $c=8$ 时二者奇偶相同。

### 6.1 普通的 c=1 两支

I 和 III 奇支的 $L\otimes\mathbb Q_2$ 有一个 $\mathbb Q_2$ 因子，因此最小多项式 $g$ 在 $\mathbb Q_2$ 有根。

若 $X$ 偶、$W$ 奇，则
$$
g(T)=T^3-XT-2W
$$
是 $2$-Eisenstein 多项式，在 $\mathbb Q_2$ 不可约，矛盾。因此只能 $X$ 奇、$W$ 偶。由 (51.10) 模 $4$ 得
$$
X\equiv Z^p\equiv Z\pmod4.
$$
在 I 中 $Z\equiv1\pmod4$，在 III 奇支中 $Z\equiv3\pmod4$，所以 R19 所需模 $4$ 条件自动成立。又因 $X$ 奇，$2$ 不是 $X,W$ 的共同因子。

### 6.2 族 II

此处 (51.10) 只说明 $X,W$ 奇偶相同。要满足 R19，必须且只须再要求 $X$ 奇；方程即迫使 $W$ 也奇。于是 $2$ 不再是共同因子，而方程模 $8$ 还自动给 $X\equiv3\pmod8$。

不能把这里的额外条件删掉。最大整环中的原始坐标在二进分歧二次因子上，仍允许 $X,W$ 同为偶数；第 4 节的 $q\ge5$ 引理没有声称覆盖素数 $2$。

### 6.3 族 III 的射线分支

此时 $L\otimes\mathbb Q_2$ 为三次域。如果 $X$ 奇，则 $g(0)$ 为偶数而 $g'(0)=-X$ 为单位，Hensel 引理给 $g$ 的 $\mathbb Q_2$ 根，与该处是三次域矛盾。因此 $X$ 偶，而 $c=1,Z$ 奇进一步强迫 $W$ 奇。

R19 的剩余条件恰为 $X\equiv2\pmod4$。它成立时 $X,W$ 奇偶相反，所以不可能有共同的因子 $2$。

结合第 5 节，全部 (51.7) 和 R19 奇偶条件均已证明。

## 7. 必要方向与真正剩余的整数问题

给定 R19 的实际解，R37、R42 已构造候选域 $L$ 和迹零整元 $\theta$，最小多项式为 $T^3-XT-2W$。按任意整基写
$$
\theta=b+u\omega+v\eta.
$$
迹为零给
$$
3b+u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)=0,
$$
故 (51.5) 成立，且 (51.6) 恢复原来的 $\theta,X,W$。R42 的原始性引理给 $\gcd(u,v)=1$，指标公式给 (51.4)。剩余二进条件就是原数据的一部分。因此必要方向成立。

于是 O6 最后一层可精确写为：对全部充分大 $p$，证明所有候选三次域上不存在满足 (51.4)、(51.5) 及表中二进条件的整数对。与 R46 相比，不再需要把“全部原始整数条件”作为一个未展开的独立谓词。

但最困难的一项仍完整保留：
$$
I_L(u,v)=\pm\mu_e|Z|^{3k},\qquad (u,v)=1,
\qquad k=(p-e)/6,
$$
而 $L,Z$ 同时变化。R46 的 $W_e\ne0$ 只给覆盖的有理点，既不强迫也不排除这个精确的原始幂值条件；R42 的固定形式解数界也仍然不控制最大指数。

本篇新增论证只用有限 étale 代数、二次局部整环、判别式恒等式和 Hensel 引理，并已在文内展开。R19、R37、R42、R46 的已证构造为本篇的仓库内输入；没有引入新的预印本或条件性全局定理。

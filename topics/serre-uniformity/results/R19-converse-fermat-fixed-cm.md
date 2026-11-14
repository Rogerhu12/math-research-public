# R19：三个显式原始广义 Fermat 族与固定 CM 同余的等价

日期：2026-11-12；会话：`serre-uniformity-astra-cont/2026-11-12`。

**状态：已证明。** 本文补全 R16 的反向归约，并把素数 $2$ 处的导子条件完整化为有限同余条件。没有预先假定挠点同构。还无条件排除 $p\equiv1\pmod4$ 的三个整数族；$p\equiv3\pmod4$ 的统一排除仍未解决，因此不完成固定 CM 最终整性或 Serre 一致性主问题。

## 1. 三个整数族

固定素数 $p>37$，暂不要求 $p\bmod4$。考虑整数 $X,W,Z$，要求
$$
|Z|>1,\qquad \gcd(Z,6p)=1,\qquad 3\nmid X,
$$
$$
\gcd(X,W)=\gcd(X,Z)=\gcd(W,Z)=1.
\tag{19.1}
$$
再选下表的一行：

| 族 | 方程及奇偶条件 | 显式曲线 $F$ | 指定 $\delta$ |
|---|---|---|---:|
| I | $X^3-27W^2=Z^p$，$X\equiv1\pmod4$、$W$ 偶 | $y^2=x^3-Xx-2W$ | $6$ |
| II | $X^3-27W^2=8Z^p$，$X,W$ 奇 | $y^2=x^3-Xx-2W$ | $9$ |
| III | $X^3-27W^2=Z^p$，$X,W$ 奇偶相反且 $X\equiv2,3\pmod4$ | $y^2=x^3-4Xx-16W$ | $12$ |

**命题 R19。** 对任何满足 (19.1) 和上表某行的整数数据，$F$ 是非 CM 椭圆曲线，并有
$$
F[p]\simeq A[p],\qquad A:y^2=x^3-x.
\tag{19.2}
$$
更精确地，
$$
\Delta_{\min}(F)=2^\delta Z^p,\qquad
N_F=32\operatorname{rad}(Z).
\tag{19.3}
$$

反过来，对 $p>37$、$p\equiv3\pmod4$，每条非 CM 椭圆曲线 $E/\mathbb Q$ 满足 $E[p]\simeq A[p]$，都由上面三个族中某个数据给出，且得到的 $F$ 与 $E$ 在 $\mathbb Q$ 上同构。

所以，对每个这样的 $p$，存在非 CM 的固定 $A$ 同余曲线，当且仅当存在满足这组显式整数条件的解。这个等价并不声称参数数据唯一。

**另一推论。** 当 $p>37$ 且 $p\equiv1\pmod4$ 时，上述三个整数族均无解。证明见第 7 节。

## 2. 完整的素数 2 条件

暂时只假设表中各族的方程、$\gcd(Z,2)=1$ 以及 R16 的原始奇偶性。定义 $\mathcal L_2$ 为：显示的整模型在 $2$ 处极小，且导子指数 $f_2=5$。以下证明：
$$
\begin{array}{c|c}
\text{族}&\mathcal L_2\text{ 的充要条件}\\\hline
\mathrm I&X\equiv1\pmod4,\\
\mathrm {II}&\text{总成立},\\
\mathrm {III}&X\equiv2,3\pmod4.
\end{array}
\tag{19.4}
$$
所用分类输入为 R16 引用的 Barrios–Roy–Sahajpal–Tallana–Tobin–Wiersema (2025), Proposition 3.5、Tables 1 和 3。尤其 Proposition 3.5 包含反向断言：模型具有表列的系数赋值，就已经极小且具有所列 Kodaira 型。以下只做显式代数变换和赋值计算。

对短模型 $y^2=x^3+Ax+B$，使用
$$x_{\rm old}=x+r,\qquad y_{\rm old}=y+sx+t$$
后，新的系数为
$$
a_1=2s,\quad a_2=3r-s^2,\quad a_3=2t,
$$
$$
a_4=3r^2+A-2st,\qquad
a_6=r^3+Ar+B-t^2.
\tag{19.5}
$$
所有使用的 $r,s,t$ 都为整数，这些变换不改变判别式。

### 2.1 族 I

此时 $A=-X,B=-2W$，$X$ 奇、$W$ 偶，判别式赋值为 $6$。取 $(r,s,t)=(1,1,0)$，得到
$$
(a_1,a_2,a_3,a_4,a_6)=(2,2,0,3-X,1-X-2W).
$$
若 $X\equiv1\pmod4$，则 $v_2(a_4)=1$、$v_2(a_6)\ge2$，是 Table 1 的 III 型强极小模型，导子指数为 $6-2+1=5$。

若 $X\equiv3\pmod4$，则 $v_2(a_4)\ge2$、$v_2(a_6)=1$，是 II 型强极小模型，导子指数为 $6$。这也解释了为什么仅有 $X$ 奇、$W$ 偶不够。

### 2.2 族 II

方程模 $8$ 给出 $X\equiv3\pmod8$。取奇数 $r\in\{1,3\}$ 满足 $r\equiv-W\pmod4$，并取 $(s,t)=(1,0)$。于是
$$
a_1=2,\quad 2\mid a_2,\quad a_3=0,\quad 8\mid a_4,\quad 8\mid a_6.
$$
最后两个整除式分别来自
$$
3r^2-X\equiv3-X\equiv0\pmod8,
$$
$$
r^3-Xr-2W\equiv-2(r+W)\equiv0\pmod8.
$$
实际有 $v_2(a_6)=3$。若 $16\mid a_6$，则
$$
v_2(b_2)=2,\quad v_2(b_4)\ge4,\quad
v_2(b_6)\ge6,\quad v_2(b_8)\ge6.
$$
判别式公式
$$
\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6
$$
会给出 $v_2(\Delta)\ge10$，与本族 $v_2(\Delta)=9$ 矛盾。因此模型是 $I_0^*$ 型强极小模型，导子指数 $9-5+1=5$。

### 2.3 族 III，$X$ 奇、$W$ 偶

这里 $A=-4X,B=-16W$，判别式赋值为 $12$。

若 $X\equiv1\pmod4$，取 $(r,s,t)=(2,0,0)$，得到
$$
a_1=0,\quad a_2=6,\quad a_3=0,\quad
a_4=4(3-X),\quad a_6=8(1-X-2W).
$$
其赋值为 $(\infty,1,\infty,3,\ge5)$，是 $I_2^*$ 型强极小模型，导子指数为 $12-7+1=6$。

若 $X\equiv3\pmod4$，取 $r=2k$、$s=0$、$t=4$，其中 $k\in\{1,3\}$ 稍后选择。则
$$
a_1=0,\quad a_2=6k,\quad a_3=8,\quad
a_4=4(3k^2-X),
$$
$$
a_6=8(k^3-Xk-2W-2).
$$
有 $v_2(a_2)=1$、$v_2(a_3)=3$、$v_2(a_4)\ge4$。括号
$$H(k)=k^3-Xk-2W-2$$
被 $4$ 整除；并且
$$H(3)-H(1)=26-2X\equiv4\pmod8.$$
所以 $k=1,3$ 中恰有一个使 $8\mid H(k)$，即 $v_2(a_6)\ge6$。所得模型是 $I_3^*$ 型强极小模型，导子指数为 $12-8+1=5$。

### 2.4 族 III，$X$ 偶、$W$ 奇

取 $(r,s,t)=(0,0,4)$。得到
$$
a_1=a_2=0,\quad a_3=8,\quad a_4=-4X,\quad a_6=-16(W+1).
$$
若 $v_2(X)=1$，则赋值为 $(\infty,\infty,3,3,\ge5)$，是 III$^*$ 型强极小模型，导子指数为 $12-8+1=5$。

若 $4\mid X$ 且 $W\equiv1\pmod4$，则赋值为 $(\infty,\infty,3,\ge4,5)$，是 II$^*$ 型强极小模型，导子指数为 $12-9+1=4$。

最后若 $4\mid X$ 且 $W\equiv3\pmod4$，则所有 $a_i$ 都被 $2^i$ 整除。缩放 $x=4x',y=8y'$ 得到整模型
$$
y'^2+y'=x'^3-\frac X4x'-\frac{W+1}{4},
$$
其判别式为奇数 $Z^p$，所以好约化；原模型不极小。以上穷尽各分支并证明 (19.4)。

## 3. 各处最小性和约化

对族 I、II，直接计算：
$$
c_4=48X,\qquad c_6=1728W,\qquad
\Delta=64(X^3-27W^2)=2^\delta Z^p.
\tag{19.6}
$$
对族 III，则
$$
c_4=192X,\qquad c_6=13824W,\qquad
\Delta=4096(X^3-27W^2)=2^{12}Z^p.
\tag{19.7}
$$
判别式非零，故这些模型确实定义椭圆曲线。

设 $q$ 为奇素数。如果 $q\nmid Z$，显示模型的判别式为 $q$-进单位，所以模型极小且好约化。特别地，$F$ 在 $3,p$ 处都好约化。

如果 $q\mid Z$，则由 (19.1) 有 $q\ge5$、$q\nmid X$，从而 $v_q(c_4)=0$。整模型已经极小，约化为乘性，且
$$
v_q(\Delta_{\min})=p\,v_q(Z),\qquad v_q(N_F)=1.
\tag{19.8}
$$
$2$ 处的模型极小性及导子指数由第 2 节给出。这证明 (19.3)。

还得到
$$
j(F)=
\begin{cases}
(12X)^3/Z^p,&\text{族 I、III},\\
(6X)^3/Z^p,&\text{族 II}.
\end{cases}
\tag{19.9}
$$
由 (19.1)，分子分母互素，且 $|Z|>1$。因此 $j(F)$ 不整。CM 椭圆曲线的 $j$ 是代数整数；有理的代数整数必为整数，故 $F$ 非 CM。

## 4. 残余表示的降层

记 $\bar\rho=\bar\rho_{F,p}$。由 Mazur 的有理素数次同源分类，非 CM 椭圆曲线在 $p>37$ 时没有有理 $p$-同源。因此 $\bar\rho$ 不可约。这里不能忽略 $43,67,163$：它们在一般有理同源列表中出现，但对应的曲线有 CM，已由上段排除。

由于 $\bar\rho$ 是奇表示，不可约也意味着绝对不可约。一个直接的说明是：若它在 $\mathbb F_p$ 上不可约而非绝对不可约，则其交换子域为 $\mathbb F_{p^2}$，像包含于该二次域的乘法群；但非标量复共轭有两个不同的 $\mathbb F_p$ 特征值 $1,-1$，不可能属于此群。

对每个 $q\mid Z$，Tate 曲线描述给出
$$
\bar\rho|_{I_q}\sim
\begin{pmatrix}
1&t_q\\0&1
\end{pmatrix},
$$
其中惯性上的扩张类由极小判别式赋值模 $p$ 给出。因为 (19.8) 的赋值被 $p$ 整除，所以 $t_q=0$，$\bar\rho$ 在 $q$ 不分歧。非分裂乘性情形只是再乘以不分歧二次特征，结论不变。

这里只使用惯性上的消失。它不要求整个 Tate 参数属于 $\mathbb Q_q^{\times p}$：单位部分可能给出不分歧扩张类。把“惯性不分歧”加强为“整个局部扩张分裂”并非本证明需要的步骤。

由 Breuil–Conrad–Diamond–Taylor 的模性定理，$\bar\rho$ 来自权 $2$、平凡特征、层
$$N_F=32\prod_{q\mid Z}q$$
的新形式。又 $p\nmid N_F$。Ribet 1990 的 Theorem 1.1 对此情形适用：若待删除素数 $q\parallel N$ 处残余表示不分歧，而且残余特征 $p$ 不整除层 $N$，则可以删除 $q$，仍得到权 $2$、平凡特征的模性。

因此可逐个删除全部 $q\mid Z$。在每一步，当前层仍与 $p$ 互素。特别是，即使某个 $q\equiv1\pmod p$，Ribet 定理的另一条件 $p\nmid N$ 已满足；不能把这些素数误认为无法降层。最终 $\bar\rho$ 来自 $S_2(\Gamma_0(32))$。

这里 $F$ 在 $p$ 好约化；无须额外删除特征素数，也没有提高 Serre 权的问题。

## 5. 层 32 的唯一性

标准模曲线亏格公式给出
$$
[\mathrm{SL}_2(\mathbb Z):\Gamma_0(32)]=48,\qquad
\#\{\text{cusps}\}=8,\qquad e_2=e_3=0.
$$
因此
$$
\dim S_2(\Gamma_0(32))
=g(X_0(32))=1+\frac{48}{12}-\frac82=1.
\tag{19.10}
$$
作为检查，尖点数为
$$
\sum_{d\mid32}\varphi(\gcd(d,32/d))
=1+1+2+2+1+1=8.
$$
曲线 $A:y^2=x^3-x$ 的导子为 $32$，故其归一化新形式已经张成这个一维空间。降层得到的形式只能是 $f_A$，遂得
$$F[p]\simeq A[p].$$

所用降层同构起初可在 $\overline{\mathbb F}_p$ 上表述；由于两边均在 $\mathbb F_p$ 上定义且绝对不可约，等价表示下降到 $\mathbb F_p$。例如同态线性方程组在 $\mathbb F_p$ 上有一维解空间；任一非零解由不可约性为同构。因此这里得到的确为 $\mathbb F_p[G_{\mathbb Q}]$-模同构。

## 6. 必要方向及其精确意义

现在假设 $p\equiv3\pmod4$ 且 $E[p]\simeq A[p]$，$E$ 非 CM。R16 从 $E$ 的全局极小不变量构造 $X,W,Z$，并给出 (19.1)、对应的方程和奇偶性以及 $|Z|>1$。

先按 R16 给出的奇偶性构造 $F$。式 (19.6)、(19.7) 说明 $F$ 与原全局极小模型拥有完全相同的 $c_4,c_6,\Delta$。特征零中，具有相同这两个不变量的椭圆曲线在基域上同构：把两条曲线化为短模型，都得到
$$y^2=x^3-\frac{c_4}{48}x-\frac{c_6}{864}.$$
因此 $F\simeq_{\mathbb Q}E$。

显示模型的判别式与 $E$ 的全局极小判别式相等，所以它在 $2$ 也极小；R13 已给出 $f_2(E)=5$。故第 2 节的 $\mathcal L_2$ 成立，进而对应的模 $4$ 条件成立。必要方向证明完毕。

这里还说明：在充分方向的整数条件中，可以不预先加入 R13 的素因子限制、$Z\bmod9$ 条件及固定 CM 同余的局部迹限制。它们由已证明的挠点同构自动推出。对 $p\equiv3\pmod4$ 的数据，必然有
$$
q\mid Z\Longrightarrow q\equiv\pm1\pmod{4p},
\qquad Z\equiv\pm1\pmod9,
$$
并且分裂于 $\mathbb Q(i)$ 的分母素数满足 $q\ge4p^2+1$。

还有一个方便的模 $3$ 加强：
$$
X\equiv2\pmod3\quad\text{或}\quad 3\mid W.
\tag{19.11}
$$
事实上，$F,A$ 在 $3$ 都好约化，挠点同构和 Hasse 界迫使 $a_3(F)=a_3(A)=0$。族 I、II 的约化短模型为
$$y^2=x^3-Xx+W,$$
族 III 为 $y^2=x^3-Xx-W$。若 $X\equiv1\pmod3$，则右边在全部 $x\in\mathbb F_3$ 上恒为 $\pm W$，所以迹为 $-3\chi(\pm W)$，为零当且仅当 $3\mid W$。若 $X\equiv2\pmod3$，右边是 $\mathbb F_3$ 上的仿射双射，迹自动为零。这证明 (19.11)。

## 7. 分裂指数的无解推论

设 $p>37$、$p\equiv1\pmod4$，若三个族之一有满足条件的解，第 3—5 节已经给出非 CM 曲线 $F$ 以及 $F[p]\simeq A[p]$。

CM 环 $\mathbb Z[i]$ 模 $p$ 为 $\mathbb F_p\times\mathbb F_p$。定义在 $\mathbb Q(i)$ 上的 CM 自同态使 $A[p]$ 分成两条特征线，而 $G_{\mathbb Q}$ 至多交换它们。因此 $\bar\rho_{A,p}$ 的像包含于分裂 Cartan 正规化子，其阶至多 $2(p-1)^2$。

另一方面，R1 所引用的 Furio–Lombardo 完整像定理说明：非 CM 曲线 $F/\mathbb Q$、$p>37$ 的像只能为 $\operatorname{GL}_2(\mathbb F_p)$ 或完整非分裂 Cartan 正规化子。后者的阶为 $2(p^2-1)>2(p-1)^2$，前者更大。这与挠点同构矛盾。因此三个整数族在这些指数均无解。

此推论运用已有的分裂 Cartan 排除；未把剩余 $p\equiv3\pmod4$ 情形一并解决。

## 8. 引用与剩余问题

- B. Mazur, *Rational isogenies of prime degree* (with appendix by D. Goldfeld), Invent. Math. **44** (1978), 129–162，Theorem 1 及引言的有理点分类表；[DOI](https://doi.org/10.1007/BF01390348)，[作者存档](https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf)。
- C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over $\mathbb Q$: wild 3-adic exercises*, JAMS **14** (2001), 843–939，Theorem A；[DOI](https://doi.org/10.1090/S0894-0347-01-00370-8)，[作者存档](https://math.stanford.edu/~conrad/papers/tswfinal.pdf)。
- K. A. Ribet, *On modular representations of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ arising from modular forms*, Invent. Math. **100** (1990), 431–476，Theorem 1.1，特别是其中“层与残余特征互素”的第二种条件；[DOI](https://doi.org/10.1007/BF01389025)，[作者存档](https://math.berkeley.edu/~ribet/Articles/invent_100.pdf)。
- $2$ 处 Tate 算法及其已发表的完整表见 R16 第 2 节；本篇第 2 节用显式坐标变换证明所需有限同余表。
- $p\equiv1\pmod4$ 的无解推论所用完整像定理及主来源见 R1 第 1 节。

**尚未解决的全局命题：** 证明存在绝对 $P_A$，使对所有 $p>P_A$、$p\equiv3\pmod4$，上述三族没有满足 (19.1) 和表中模 $4$ 条件的解。R19 把这一命题与固定 $A$ 的非 CM 挠点同余排除严格等价起来；降层恰好回到真实存在的 CM 新形式 $f_A$，因此单独重复降层并不会产生矛盾。

# R132：最大奇同余层的支持素数与分裂乘法平方级下界

日期：2026-11-12；会话：serre-uniformity-astra-resume2；负责：cm_denominators。

**状态：已证明。** 本文讨论 R19 的实际非 CM 曲线与完整原始整数族，记
$$
A:y^2=x^3-x,\qquad E[p]\simeq A[p],\qquad p>37,
$$
$$
|Z|>1,\qquad g=\gcd_{q\mid Z}v_q(Z),\qquad M=pg.
$$
R128 给出 $M$ 为奇数、每个素因子模四余三、$(M,Z)=1$，以及实际 Galois 模同构
$$E[M]\simeq A[M].\tag{132.1}$$

对每个 $q\mid Z$，曲线 $E$ 在 $q$ 为乘法约化。定义
$$
\epsilon_q=\begin{cases}
+1,&E/\mathbb Q_q\text{ 为分裂乘法约化},\\
-1,&E/\mathbb Q_q\text{ 为非分裂乘法约化}.
\end{cases}
$$
这里的分裂乘法与素数在 $K=\mathbb Q(i)$ 中分裂是两件事，下面始终分别写明。

## 1. 完整结论

**定理 132.1。** 每个实际分母素数 $q\mid Z$ 满足：

1. 若 $q\equiv3\pmod4$，则
   $$q\equiv-1\pmod{4M},\qquad q\ge4M-1.\tag{132.2}$$
2. 若 $q\equiv1\pmod4$，则 $A$ 的实际高斯 Frobenius 可写成
   $$\pi_q=a+bi,\qquad q=a^2+b^2,$$
   其中
   $$a\text{ 奇},\quad b\ne0\text{ 偶},\qquad
   a\equiv\epsilon_q\pmod M,\quad b\equiv0\pmod M.
   \tag{132.3}$$
   特别有
   $$q\equiv1\pmod{4M},\qquad q\ge4M^2+1.\tag{132.4}$$
3. 在第 2 项中，若还满足 $\epsilon_q=+1$，则有严格更强的界
   $$\boxed{q\ge8M^2-4M+1.}\tag{132.5}$$

第 2 项的 $b$ 在换 $i$ 为 $-i$ 时反号，不改变任何结论。$a$ 的符号由实际 Frobenius 迹 $a_q(A)=2a$ 固定，不能为了方便把它随意选为正数。

这推广 R13 的支持素数条件，并在实际分裂乘法的一个分支中进一步加强。它不属于 R119 的任意商域分歧素数情形：这里 $q\mid Z$、$A$ 在 $q$ 好约化，实际 $E$ 在 $q$ 乘性。

## 2. 完整素数幂层上的 Tate 原始特征线

固定 $q\mid Z$。由 $(M,Z)=1$，$q\nmid M$；实际同构 (132.1) 使 $E[M]$ 在 $q$ 不分歧，因为 $A$ 在奇素数 $q$ 好约化。

Tate 曲线的挠点序列，经未分歧二次分裂角色扭曲，给出
$$
0\longrightarrow\mu_M\otimes\epsilon_q
\longrightarrow E[M]
\longrightarrow (\mathbb Z/M)\otimes\epsilon_q
\longrightarrow0.
\tag{132.6}
$$
这里符号 $\epsilon_q$ 代表该未分歧角色在算术 Frobenius 上的值。因而实际 Frobenius 在适当基中的矩阵为
$$
\begin{pmatrix}\epsilon_q q&*\\0&\epsilon_q\end{pmatrix}.
\tag{132.7}
$$
不需要假设非对角元已经为零。重要的是核给出一个**原始**的秩一子模：对每个 $\ell^n\mid M$，其生成元 $v$ 在 $(\mathbb Z/\ell^n)^2$ 中至少有一个单位坐标。

这保留了完整模 $\ell^n$ 信息，而不只比较模 $\ell$ 的迹。特别不能从一个整数量被 $\ell$ 整除就无证明地提升至被 $\ell^n$ 整除。

## 3. 惰性素数：迹给出完整模数

设 $q\equiv3\pmod4$。对 $A/\mathbb F_q$ 的点数和，变换 $x\mapsto-x$ 把 $x^3-x$ 变为其负数，而 $-1$ 为非平方。因此二次角色和逐项抵消，得到
$$a_q(A)=0.$$
将其与 (132.7) 的迹比较，得到
$$0\equiv\epsilon_q(q+1)\pmod M.$$
由于 $\epsilon_q$ 可逆，$M\mid q+1$。再结合 $q\equiv-1\pmod4$ 及 $(M,4)=1$，即得 (132.2)。这一步对两种乘法符号都成立。

## 4. 分裂素数：原始向量给出高斯坐标整除

设 $q\equiv1\pmod4$。$A$ 的四阶 CM 自同态 $i$ 定义于 $\mathbb F_q$；R13 §3 已证明实际 Frobenius 是
$$
\pi_q=a+bi\in\mathbb Z[i],\qquad
q=a^2+b^2,\qquad a_q(A)=2a.
\tag{132.8}
$$
其论证使用真实自同态的交换关系和整性：Frobenius 与 $i$ 交换，故属于其二次域中心化子；它为代数整数，故属于最大整环 $\mathbb Z[i]$。两坐标均非零，否则素数 $q$ 是整数平方。

现在固定任意 $\ell^n\mid M$，并置 $R=\mathbb Z/\ell^n$。有 $\ell\equiv3\pmod4$，所以 $T^2+1$ 在 $\mathbb F_\ell$ 不可约。在 (132.6) 的原始生成元 $v$ 通过实际同构传到 $A[\ell^n]$ 之后，向量
$$v,\quad iv$$
构成 $R$ 基。事实上，两向量模 $\ell$ 线性相关就会使非零 $v\bmod\ell$ 成为 $i$ 的 $\mathbb F_\ell$ 特征向量，与不可约性矛盾；其行列式模 $\ell$ 非零，故在 $R$ 中可逆。

Tate 原始线上的 Frobenius 特征值是 $\epsilon_q q$，于是
$$
(a-\epsilon_q q)v+b(iv)=0\quad\text{在 }A[\ell^n]\text{ 中}.
$$
由上述基立刻得到
$$a\equiv\epsilon_q q\pmod{\ell^n},\qquad b\equiv0\pmod{\ell^n}.$$
这又说明 Frobenius 在整个 $A[\ell^n]$ 上为标量 $a$。在 (132.6) 的商上，其特征值为 $\epsilon_q$，所以
$$a\equiv\epsilon_q\pmod{\ell^n},\qquad q\equiv1\pmod{\ell^n}.$$

遍历所有 $\ell^n\parallel M$，中国剩余定理给
$$a\equiv\epsilon_q\pmod M,\qquad M\mid b,\qquad q\equiv1\pmod M.$$
符号 $\epsilon_q$ 在全部初等因子中是**同一个**实际 Tate 符号，不是各素数上任意挑选的正负号。

曲线 $A$ 有完整有理二挠点。因此
$$4\mid\#A(\mathbb F_q)=q+1-2a.$$
$q\equiv1\pmod4$ 强迫 $a$ 奇；由 $q=a^2+b^2$ 得 $b$ 偶。于是 $2M\mid b$，而 $b\ne0$，所以
$$q=a^2+b^2\ge1+(2M)^2.$$
这证明 (132.3)、(132.4)。

## 5. 四阶点保留的额外二进条件

仍设 $q\equiv1\pmod4$，取 $i\in\mathbb F_q$ 满足 $i^2=-1$。实际点
$$P=(i,1-i)\in A(\mathbb F_q)$$
满足曲线方程，因为
$$(1-i)^2=-2i=i^3-i.$$
其切线斜率为
$$\frac{3i^2-1}{2(1-i)}=-(1+i),$$
倍点公式准确给
$$[2]P=(0,0).$$
故 $P$ 的阶为四。再取独立二挠点 $(1,0)$，两者生成一个阶为八的子群，因此
$$8\mid\#A(\mathbb F_q)=N_{\mathbb Q(i)/\mathbb Q}(\pi_q-1).\tag{132.9}$$

高斯整环中二只有一个素理想 $(1+i)$，且其范数为二，所以 (132.9) 等价于
$$\pi_q-1\in(1+i)^3\mathbb Z[i].\tag{132.10}$$
这一项可由真实点直接证明，不需要额外假定一个未核定方向的 Hecke 角色或初等高斯素元规范。

若 $E/\mathbb Q_q$ 是分裂乘法，则 $\epsilon_q=+1$。第 4 节还给
$$\pi_q-1\in M\mathbb Z[i].$$
$M$ 为奇数，两个理想互素。因此
$$\pi_q-1\in M(1+i)^3\mathbb Z[i]
=2M(1+i)\mathbb Z[i].$$
存在整数 $r,s$，使
$$\pi_q=1+2M(1+i)(r+si).$$
$(r,s)\ne(0,0)$，否则 $q=N(\pi_q)=1$。置 $n=r^2+s^2\ge1$，直接展开范数得
$$
q=1+4M(r-s)+8M^2n.
$$
对整数 $r,s$，有
$$|r-s|\le|r|+|s|\le r^2+s^2=n.$$
所以
$$q\ge1+n(8M^2-4M)\ge8M^2-4M+1,$$
即 (132.5)。这使用整数格的实际最小界，不以连续变量的近似极小值代替。

当 $\epsilon_q=-1$ 时，第 4 节给的是 $\pi_q+1\in M\mathbb Z[i]$，不能将其换成 $\pi_q-1$。因此 (132.10) 不产生相同的乘积理想整除，本文在该支只断言 (132.4)。

## 6. 高度推论与全局边界

R19 的精确约分分母为 $\operatorname{den}j(E)=|Z|^p$，每个非零 $v_q(Z)$ 至少为 $g$。于是
$$
h(j(E))\ge p\log|Z|
=p\sum_{q\mid Z}v_q(Z)\log q
\ge M\sum_{q\mid Z}\log q.
\tag{132.11}
$$
$|Z|>1$，故至少有一个支持素数，得到
$$h(j(E))\ge M\log(4M-1).\tag{132.12}$$
若至少有一个支持素数在 $K$ 分裂，则可加强为
$$h(j(E))\ge M\log(4M^2+1).$$
若至少有一个支持素数同时在 $K$ 分裂、且使 $E$ 分裂乘法，则进一步有
$$h(j(E))\ge M\log(8M^2-4M+1).$$

也可在 (132.11) 中对每个支持素数分别代入适用的界，保留三类素数的数量。这些结论都为必要的**下界**；没有给 $Z$ 的支撑、高度或 $M$ 的统一上界，因而没有完成 O6 或 Serre 一致性。

## 来源与已证接口

- [R128：全部奇数层的同余深度与分裂素数幂分母排除](R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)，给完整 (132.1)、$M$ 的素因子类型及 $(M,Z)=1$。
- [R13：固定 CM 同余曲线的导子、分母与高度下界](R13-denominators-for-fixed-cm-congruence.md)，§3 的真实高斯 Frobenius 与模 $p$ 支持条件；本篇保留完整素数幂原始线，提升到最大奇模 $M$。
- R19 的实际乘法约化与精确分母；R2 的 Tate 挠点接口。本篇不需要新的条件性全局输入。原始向量基、四阶点及高斯理想范数最小界均已在文中证明。

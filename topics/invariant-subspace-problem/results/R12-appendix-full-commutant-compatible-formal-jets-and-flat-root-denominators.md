# R12 后续：完整尾交换子的兼容形式喷射与闭根的实际平坦分母

日期：2026-11-27（台北）。作者：AI-assisted GPT-6 Astra Pro；literature_deddens / Astra-ISP-8542378f-20261127。

状态：以下全交换子代数结构及闭根必要条件已完整证明。本稿不把 R32 的多项式范数闭包系数直接延伸到全部交换子；每一个新系数都由真实有限头块及兼容尾字符定义。共同喷射核含非零实际算子，因此这里的形式演算明确不忠实。最后的闭根结论是对实际全域分母的必要条件，不构造这样的分母。

## 1. 原尾、有限头及完整交换子

在原 Haar 空间 $K=L^2(\mathbb Z_2,\mu)$ 上置
$$
B_m f(y)=\alpha_{m+v_2(y)}f(y-1),\qquad
\mathscr C_m=\{B_m\}'.
$$
每个 $\mathscr C_m$ 已是含单位的交换 Banach 代数。使用
[原尾完整交换子证明](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md) 的实际权与头尾分解。

固定 $\ell\ge1$、$D=2^\ell$，令
$$
\beta_r^{(m)}
 =\prod_{a=1}^r\alpha_{m+v_2(a)},\qquad
\beta_0^{(m)}=1,\qquad
c_{m,\ell}=\beta_{D-1}^{(m)}.
$$
则
$$
B_m=J_{m,\ell}\otimes I+e_{0,D-1}\otimes B_{m+\ell},
\qquad
B_m^D=c_{m,\ell}I_D\otimes B_{m+\ell}.
\tag{1.1}
$$
$J_{m,\ell}$ 是长度 $D$ 的非退化加权 nilpotent 链，且
$B_m^r(e_0\otimes h)=\beta_r^{(m)}e_r\otimes h$ 对 $r<D$ 成立。

**引理 1.1（真实自由尾分解）。** 每个 $X\in\mathscr C_m$ 唯一写成
$$
X=\sum_{r=0}^{D-1}B_m^r(I_D\otimes X_r),
\qquad X_r\in\mathscr C_{m+\ell}.
\tag{1.2}
$$
若 $X_{rs}^{\rm block}$ 是其原物理头矩阵，则
$$
X_r=(\beta_r^{(m)})^{-1}X_{r0}^{\rm block},
\qquad
\|X_r\|\le(\beta_r^{(m)})^{-1}\|X\|.
\tag{1.3}
$$

证明：$X$ 与 (1.1) 的 $D$ 次幂交换，故全部块均与
$B_{m+\ell}$ 交换。(1.3) 给出候选。每个 $I_D\otimes X_r$
都与原 $B_m$ 交换；所以 (1.2) 的右端与 $B_m$ 交换，而且其第零列恰等于 $X$ 的第零列。差算子杀掉 $e_0\otimes K$，再由交换性杀掉其前 $D$ 个幂像。这些像的代数和就是整个 $K$，故差为零。相同论证给唯一性。证毕。

因此这里是准确的交换代数描述
$$
\mathscr C_m\simeq
\mathscr C_{m+\ell}[z]/
(z^D-c_{m,\ell}B_{m+\ell}),
\tag{1.4}
$$
其中右边的系数代数通过 $X\mapsto I_D\otimes X$ 嵌入。
这不把 $B_{m+\ell}$ 设成零；下一节只有在真正施加字符以后才做该化简。

## 2. 全部尾字符的一致识别

记 $\Omega_m$ 为 $\mathscr C_m$ 的非零连续字符空间。
每个 $B_m$ 拟幂零，所以对所有 $\chi\in\Omega_m$，
$$
\chi(B_m)=0.
\tag{2.1}
$$
沿真实尾嵌入限制字符给映射
$$
\Omega_m\longrightarrow\Omega_{m+\ell},
\qquad
\chi\longmapsto
\chi^{[\ell]},\quad
\chi^{[\ell]}(Z)=\chi(I_D\otimes Z).
\tag{2.2}
$$

**引理 2.1。** (2.2) 是双射，且对 (1.2) 有
$$
\chi(X)=\chi^{[\ell]}(X_0).
\tag{2.3}
$$

证明：给定 $\psi\in\Omega_{m+\ell}$，定义
$\chi_\psi(X)=\psi(X_0)$。在 (1.2) 的有限乘法中，次数越过 $D$
的项都带因子 $B_{m+\ell}$；施加 $\psi$ 后这些项消失。
所以常数项函数 $\chi_\psi$ 是含单位的乘法泛函。
由 (1.3) 其范数不超过一。反向，(2.1) 使任何 $\chi$ 在 (1.2)
上都满足 (2.3)，故限制与上述构造互逆。证毕。

这些识别在继续分尾时相容。因此以后固定 $\chi\in\Omega_m$，
并使用其唯一的全部尾限制 $\chi^{[\ell]}$。没有任意地在不同层重选不兼容字符。

## 3. 完整交换子上的连续系数形式演算

对 (1.2) 定义
$$
j_{\chi,D}(X)=
\sum_{r=0}^{D-1}\chi^{[\ell]}(X_r)z^r
\quad\text{于 }\mathbb C[z]/(z^D).
\tag{3.1}
$$
由 (1.4) 和 $\chi^{[\ell]}(B_{m+\ell})=0$，
$j_{\chi,D}$ 是含单位的代数同态，而且
$j_{\chi,D}(B_m)=z$。

**引理 3.1（跨头兼容）。** 若 $D'=2^{\ell'}\ge D$，则
$$
j_{\chi,D'}(X)\pmod {z^D}=j_{\chi,D}(X).
\tag{3.2}
$$

证明：先把 $D'$ 头分解写成
$X=\sum_{s<D'}B_m^s(I_{D'}\otimes Y_s)$。
按 $s=r+tD$ 分组，使用
$B_m^D=c_{m,\ell}I_D\otimes B_{m+\ell}$，
就得到 (1.2) 的第 $r$ 个实际尾系数。除 $t=0$ 外的项全部带
$B_{m+\ell}$，被 $\chi^{[\ell]}$ 杀掉；$t=0$ 的尾限制依引理 2.1
正好是 $\chi^{[\ell']}(Y_r)$。这给 (3.2)。证毕。

由此定义唯一形式级数
$$
j_\chi(X)=\sum_{r=0}^{\infty}c_{r,\chi}(X)z^r
\in\mathbb C[[z]],
\qquad
c_{r,\chi}(X)=\chi^{[\ell]}(X_r)\quad(2^\ell>r).
\tag{3.3}
$$
每个固定系数都是连续线性泛函，满足
$$
|c_{r,\chi}(X)|
 \le(\beta_r^{(m)})^{-1}\|X\|.
\tag{3.4}
$$
由原精确幂范数 $\|B_m^r\|=\beta_r^{(m)}$，这个界是准确范数：在范数为一的算子
$B_m^r/\beta_r^{(m)}$ 上取值恰为
$(\beta_r^{(m)})^{-1}$，故
$\|c_{r,\chi}\|=(\beta_r^{(m)})^{-1}$。
兼容性与有限截断乘法给
$$
\boxed{
j_\chi(XY)=j_\chi(X)j_\chi(Y),\qquad
j_\chi(I)=1,\qquad j_\chi(B_m)=z.
}
\tag{3.5}
$$
这里“连续”只指每个固定系数，不声称所得级数有非零收敛半径。

对原多项式范数闭包，(3.4) 及多项式逼近说明所有
$j_\chi$ 都等于 R32 的原形式级数。一般 $X\in\mathscr C_m$ 的
系数允许依赖 $\chi$；也不由普通多项式的强收敛通过这些非正常系数。

另一个以后使用的等式是
$$
(\operatorname{id}_{M_D}\otimes\chi^{[\ell]})(X)
 =j_{\chi,D}(X)(J_{m,\ell}).
\tag{3.6}
$$
它直接来自 (1.1)--(1.2)：字符杀掉真实回绕项，留下原加权 Jordan 链。

## 4. 一个范数闭、强*稠密而不含非零 UHF 元素的平坦理想

定义
$$
\mathfrak I_{\infty,m}
 =\bigcap_{\chi\in\Omega_m}\ker j_\chi
 =\{X:c_{r,\chi}(X)=0\text{ 对全部 }r,\chi\}.
\tag{4.1}
$$
由 (3.4)--(3.5)，这是 $\mathscr C_m$ 的范数闭双边理想。
又 $c_{0,\chi}(X)=\chi(X)$，故
$$
\mathfrak I_{\infty,m}\subseteq\operatorname{rad}\mathscr C_m.
\tag{4.2}
$$
包含严格：$B_m$ 拟幂零，属于该交换 Banach 代数的根基，
但 $j_\chi(B_m)=z\ne0$。

令
$$
\mathfrak F_m=\bigcap_{r\ge1}B_m^r\mathscr C_m.
$$
若 $P\in\mathfrak F_m$，则对每个 $r$ 有实际有界
$R_r\in\mathscr C_m$ 使 $P=B_m^rR_r$。施加 (3.5) 得
$j_\chi(P)\in z^r\mathbb C[[z]]$ 对全部 $r$ 成立，因此
$$
\boxed{\mathfrak F_m\subseteq\mathfrak I_{\infty,m}.}
\tag{4.3}
$$

R267 已构造 $\mathfrak F_0$ 中的非零共同倍数，并证明其单位球在
$\mathscr C_0$ 单位球中强*稠密。这个密度也传给每个原尾，步骤如下：
对 $X\in\mathscr C_m$、$\|X\|\le1$，原嵌入
$I_{2^m}\otimes X\in\mathscr C_0$。
取 $\mathfrak F_0$ 中收缩 $P_\nu$ 强*趋于该嵌入。
其任一原对角尾块，特别 $P_{\nu,00}$，属于 $\mathscr C_m$，
范数不超过一，并强*趋于 $X$。对任意 $r$，
$$
P_\nu=A^{2^m r}R_{\nu,r}
 =c_{0,m}^{\,r}(I_{2^m}\otimes B_m^r)R_{\nu,r}.
$$
$R_{\nu,r}\in\mathscr C_0$ 的各块属于 $\mathscr C_m$，故
$P_{\nu,00}\in B_m^r\mathscr C_m$。于是
$P_{\nu,00}\in\mathfrak F_m$，证明逐尾密度。$m=0$ 直接用原结论。
结合 (4.3)，得到
$$
\boxed{
\overline{(\mathfrak I_{\infty,m})_1}^{\,\mathrm{strong*}}
  =(\mathscr C_m)_1.
}
\tag{4.4}
$$
特别这些理想非零。没有声称它们等于 $\mathfrak F_m$，
也没有把强*密度改成范数密度。

记 $\mathfrak U_m$ 为该原尾的具体物理 UHF 代数。

**命题 4.1。**
$$
\boxed{\mathfrak I_{\infty,m}\cap\mathfrak U_m=\{0\}.}
\tag{4.5}
$$

证明：若 $X$ 属于左端，给定 $\epsilon>0$，选足够深有限头
$K_D\otimes I$，使 $\|X-K_D\otimes I\|<\epsilon$。
取任意兼容尾字符并对全部头块施加它。标量值连续泛函的矩阵放大具有相同范数；在这里可直接验证：对单位列 $u,v\in\mathbb C^D$，
$$
\left|\sum_{r,s}\bar v_r\chi^{[\ell]}(Z_{rs})u_s\right|
 =\left|\chi^{[\ell]}\!
   \left(\sum_{r,s}\bar v_r Z_{rs}u_s\right)\right|
 \le\|[Z_{rs}]\|.
$$
所以该矩阵放大收缩。由 (3.6) 及 $X\in\mathfrak I_{\infty,m}$，
$X$ 的字符矩阵恰为零，$K_D\otimes I$ 的字符矩阵则是 $K_D$。
因此 $\|K_D\|\le\epsilon$，进而 $\|X\|\le2\epsilon$。令
$\epsilon\downarrow0$ 即得 $X=0$。证毕。

这一步没有把负整数 boundary 表示延伸到整个交换子。
所有字符矩阵来自同一个原 Haar 算子的实际有限头块。

同一证明还给准确范数距离。对任意
$F\in\mathscr C_m\cap\mathfrak U_m$ 及
$X\in\mathfrak I_{\infty,m}$，取
$\|F-K_D\otimes I\|<\epsilon$。则
$$
\|F-X\|\ge
\|(\operatorname{id}\otimes\chi^{[\ell]})(F-X)\|
\ge\|K_D\|-\epsilon\ge\|F\|-2\epsilon.
$$
令 $\epsilon\downarrow0$，再取 $X=0$ 的上界，得到
$$
\boxed{
\operatorname{dist}(F,\mathfrak I_{\infty,m})=\|F\|
\quad(F\in\mathscr C_m\cap\mathfrak U_m).
}
\tag{4.6}
$$
逐矩阵项应用同一个尾字符仍收缩，故 (4.6) 在任意固定有限矩阵
放大中同样成立。特别商映射在原多项式范数闭包上完全等距。

## 5. 闭稳定根的实际全域分母必须全喷射平坦

固定正整数 $k,p,q$、$\lambda\ne0$，并假定
$$
q\nmid pk.
\tag{5.1}
$$
令 $\mathbf B=I_k\otimes B_m$。
设 $T$ 是 $K^{\oplus k}$ 上稠密定义闭算子，其真实域 $D(T)$ 满足
$$
T D(T)\subseteq D(T),\qquad
\mathbf B D(T)\subseteq D(T),\qquad
T\mathbf Bx=\mathbf BTx\quad(x\in D(T)),
\tag{5.2}
$$
并且在该域上
$$
T^qx=\lambda\mathbf B^p x.
\tag{5.3}
$$
全部自然迭代在 (5.2) 下有定义。

假设实际标量交换分母 $P\in\mathscr C_m$ 满足
$$
(I_k\otimes P)K^{\oplus k}\subseteq D(T).
\tag{5.4}
$$
不预设 $P$ 单射或稠密像；下面的必要条件覆盖任何这样的 $P$。

**定理 5.1。**
$$
\boxed{P\in\mathfrak I_{\infty,m}.}
\tag{5.5}
$$

证明分为真实域和形式代数两步。

首先，
$$
Y=T(I_k\otimes P)
$$
在整个 $K^{\oplus k}$ 上定义且闭，故由闭图定理有界。
(5.2) 及 $P\in\mathscr C_m$ 给 $Y\mathbf B=\mathbf BY$，
所以 $Y\in M_k(\mathscr C_m)$。

还须支付 $T$ 与 $I_k\otimes P$ 的真实域交换。完整 $\mathscr C_m$
的有界强多项式逼近给 $p_n(B_m)\to P$。对固定 $x\in D(T)$，
$$
p_n(\mathbf B)x\to(I_k\otimes P)x,\qquad
T p_n(\mathbf B)x=p_n(\mathbf B)Tx\to(I_k\otimes P)Tx.
$$
闭性得 $(I_k\otimes P)x\in D(T)$，且二者交换。
结合域的 $T$ 稳定性，逐次合法计算得到全域有界恒等式
$$
Y^q=\lambda\,\mathbf B^p(I_k\otimes P)^q.
\tag{5.6}
$$

现在对 $M_k(\mathscr C_m)$ 的每一项施加 (3.5)，在交换环
$\mathbb C[[z]]$ 上取通常行列式。由 (5.6)，
$$
\det(j_\chi(Y))^q
 =\lambda^k z^{pk}j_\chi(P)^{qk}.
\tag{5.7}
$$
若 $j_\chi(P)\ne0$，右边非零，因此左边也非零。
非零形式级数具有有限整数消失阶；取阶得
$$
q\,\operatorname{ord}\det(j_\chi(Y))
 =pk+qk\,\operatorname{ord}j_\chi(P).
\tag{5.8}
$$
于是 $q\mid pk$，与 (5.1) 矛盾。因此每个 $\chi$ 都满足
$j_\chi(P)=0$，即 (5.5)。证毕。

当 $k=1$，(5.6) 还给每个 $j_\chi(Y)=0$，
所以有界分子也属于 $\mathfrak I_{\infty,m}$。
一般 $k$ 时不能由行列式为零把全部分子矩阵项都判成平坦。

由命题 4.1，定理 5.1 尤其排除任何非零 UHF 内分母；它也排除所有
虽在 UHF 外、却至少保留一个非零有限阶字符喷射的分母。
R267 的实际共同全部幂分母已经处在 (4.3) 内，所以本定理不排除它；
仍须直接证明 (5.4)，不能以“全喷射为零”或“共同全部幂像”替代该真实域包含。

对奇数 $p$，若一开始只给 $T D(T)\subset D(T)$ 和 (5.3)，
则 $\mathbf B^p$ 的域交换由自然幂自动成立；
[原奇幂强恢复](../results/R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)
及闭性再给 (5.2) 中的 $\mathbf B$ 域交换。
偶数 $p$ 的本定理保留 (5.2)，不免费把低头矩阵重数删去。

## 6. 本稿新增的准确接口

R32 的忠实形式级数只在多项式范数闭包中成立；本稿构造的是整个
$\mathscr C_m$ 上、按兼容尾字符索引的形式同态，其共同核明确非零。
R267 已付的实际平坦共同倍数落在该核内，而所有不整除闭根的实际
标量全域分母也必须落在这个同一范数闭理想中。

这限定了接下来可用的来源：必须在 $\mathfrak I_{\infty,m}$ 中支付
同一闭域的全域包含及对应有界分子。它没有把抽象形式解、逐向量
近似单位或原幂共同值域识别成这种实际实现。

已证依赖：

- [全部原尾的完整交换子及有限头根计数](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)；
- [全部整幂有界根与闭根域](../results/R12-appendix-all-integer-power-root-multiplicity-and-closed-root-domains.md)；
- [R267 实际共同全部幂分母与强*单位](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)；
- [完整交换子在任意奇数剩余类的同范数强*逼近](../results/R12-appendix-contractive-strong-star-density-in-every-odd-residue-class.md)。


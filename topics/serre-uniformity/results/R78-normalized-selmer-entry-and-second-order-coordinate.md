# R78：规范 Selmer 矩阵条目与实际二阶奇异坐标

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，并完成有限域配对与坐标换算。**
固定
$$p=43,\qquad r=859,\qquad q=49019,\qquad A:y^2=x^3-x.$$
本文在一组完整指定的全局及局部基下，将 R73 的原始导数值换成
R60 的规范矩阵，得到
$$
\boxed{
M_{\{r,q\}}=
\begin{pmatrix}0&6\\37&0\end{pmatrix},
\qquad \det M_{\{r,q\}}=36\ne0
\quad\text{于 }\mathbb F_{43}.
}
\tag{78.1}
$$
行、列均按 $(r,q)=(859,49019)$ 排序。
此外，同一原始 Euler system 的二阶类在 $q$ 的正下降奇异系数为
$$\boxed{\lambda_q=17,\qquad \lambda_q^{-1}=38.} \tag{78.2}$$
这里并未展开二阶类的巨大根式，也未计算 $p$ 处的三个线性校正系数。
这些未计算量不影响 (78.1)、(78.2)。

有一个必须保留的符号：对 R73 实际采用的
$D_s=\sum_{j=1}^{42}j\sigma_s^j$，
若 $\sigma_s(\Pi)/\Pi$ 的剩余类为 $\zeta_s$，则有限—奇异关系是
**负**的 $\zeta_s$ 对数。§4 用直接 Hilbert 90 推导它，并核对
Rubin 原版的交换图；不能只引用“有限—奇异映射是同构”来决定数值。

## 1. 同一个全局实挠点确能实现两份有限域证书

记
$$
K=\mathbb Q(i),\quad
V=A[43],\quad
\mathbb F=\mathbb F_{43^2},\quad
\mathfrak m=(1+i)^3p,\quad T=K(A[p]).
$$
R70 已证明
$$T=K(\mathfrak m),\qquad
\operatorname{Gal}(T/K)=\mathbb F^\times.$$
其中算术 Artin 元素的标签 $a\in\mathbb F^\times$ 在 $A[p]$ 上
作用为 $[a]$，不是 $[a^{-1}]$。

在一个固定的复嵌入中，选一次
$$P\in A(\mathbb R)[p]\setminus\{O\}.$$
这样的点存在，因为实椭圆曲线的恒等分支是圆群。
记该复嵌入的复共轭为 $\tau$，则
$$
\tau P=P,\qquad \tau([i]P)=-[i]P.
\tag{78.3}
$$
$P,[i]P$ 是 $\mathbb F_p$ 基，因为 $i\notin\mathbb F_p$。

固定下面 §2 的 Weil 配对约定，并令
$$\zeta_0=e_p(P,[i]P). \tag{78.4}$$
它是一个全局原始 $p$ 次单位根，且 $\tau\zeta_0=\zeta_0^{-1}$。

对 $s=r,q$ 分别选择 $T$ 在 $(s)$ 上的素点及剩余域识别，
使 $i$ 约化为证书中形式符号 $i$，并使同一个 $P$ 分别约化为
$$
P_r=(209,268)\in A(\mathbb F_{859}),\qquad
P_q=(11536,29305)\in A(\mathbb F_{49019}).
\tag{78.5}
$$
这两项选择确实能够同时完成。先任取一个相容于 $K$ 的嵌入；
好约化下，素于剩余特征的挠点约化为同构。
再利用整个 Cartan $\mathbb F^\times$ 对非零 $p$ 挠点的自由传递作用，
改变所选素点／嵌入，即可把 $P$ 的像改为指定的 $P_s$。
在两个不同素数上作这样的选择互不冲突；
无需声称有一个全局 Galois 元素同时完成两个不同的局部调整。

因为 $P_s$ 在 $\mathbb F_s$ 上有理，而
$[i]P_s$ 的 $s$ 次 Frobenius 为 $-[i]P_s$，
所选算术 Frobenius 在 $V$ 上恰是 (78.3) 的 $\tau$。
它在 $T/K$ 的平方为一，且其在 $T/\mathbb Q$ 的像等于
固定的 $\tau|T$。
因此两处的正、负特征线都由同一全局 $P,[i]P$ 给出。
Weil 配对与好约化相容，所以 $\zeta_0$ 的两个约化必为
$e_p(P_s,[i]P_s)$；这正是后面需要计算的基变换。

### 1.1 所计算的单位也来自同一个全局族

固定全局点
$$P_2=(i,1-i),\qquad P_{\mathfrak m}=P_2+P.$$
R70 已证明 $P_2$ 的准确湮灭理想为 $(1+i)^3$。
原始 $\mathfrak m$ 挠点的该分量与 $P_2$ 只差一个
$\mathbb Z[i]^\times$ 因子；Robert 函数
$$F_A(X)=\Delta_A^{10}/\psi_{11,A}(X)$$
在 $[i]$ 下不变，而 Cartan 可把非零 $p$ 分量搬到 $P$。
故可以一次选定 R65 原始单位族的一个相容 Cartan 共轭，
以 $P_{\mathfrak m}$ 作为基点。
在所有辅助层用 CRT 取相同 $p$ 分量、固定辅助分量的提升；
这与范数、导数及有限—奇异关系相容。

这一步只是选择同一 Euler system 的全局代表。
非平凡 $\chi_0$ 投影下，统一的 Cartan 共轭是一个非零标量；
最后的唯一单素数 Selmer 类由奇异坐标归一化，故不依赖这个
代表的整体标量。
R70 在 $r,q$ 的公式和 R73 在 $q$ 的公式，都可在 (78.5) 的素点下
看成这一同一全局族的约化。

R73 中用来生成全部 $r$ 核的任意局部 $R\in A[r]\setminus O$
也不造成另一项未知标量：更换 $R$ 只是
$\mathbb F_{r^2}^\times$ 中的共轭，导数下降类在
$\Gamma_r$ 下已经不变。计算复共轭时可以选择一个全局实 $r$ 挠点；
计算有限域范数时则可使用 R73 证书里的方便坐标。

## 2. Weil 配对方向与两处的实际基变换

本文使用 Miller (2004), Proposition 8 的约定：
$$
e_p(X,Y)=(-1)^p\,\frac{f_{p,X}(Y)}{f_{p,Y}(X)},
\qquad \operatorname{div}(f_{p,X})=p(X)-p(O).
\tag{78.6}
$$
其常数按 Miller 函数的相同归一化取定。
Sutherland 的 2025 Lecture 23, Theorem 23.30 使用此配对的倒数，
并在证明中明确解释两者的区别。这里从 (78.6) 到局部 Tate 形式
始终采用同一方向。

保留 R70、R73 的局部单位根
$$
\zeta_s=(2+i)^{(s^2-1)/43}\in\mathbb F_{s^2}.
$$
实际计算得到：

| $s$ | $\zeta_s$ | $e_p(P_s,[i]P_s)$ | $k_s$，即 $e_p(P_s,[i]P_s)=\zeta_s^{k_s}$ |
|---:|---|---|---:|
| $859$ | $97+829i$ | $510+324i$ | $40$ |
| $49019$ | $19416+40301i$ | $40963+2385i$ | $29$ |

因此在所选两个素点上，
$$\boxed{\overline{\zeta_0}=\zeta_r^{40},\qquad
\overline{\zeta_0}=\zeta_q^{29}.} \tag{78.7}$$
两处左边分别表示同一个全局 $\zeta_0$ 的约化，而不是把两个
不同剩余域里的数直接相等。

程序对 (78.6) 另作不依赖函数归一化常数的平移检查。
取 $S=(0,0)=-S$，Miller 的式 (10) 给
$$
e_p(X,Y)=
\frac{f_{p,X}(Y+S)/f_{p,X}(S)}
     {f_{p,Y}(X+S)/f_{p,Y}(S)}.
\tag{78.8}
$$
两种计算结果逐坐标相同，且核对了准确 $43$ 阶、交换两个变量取逆、
将一个变量乘 $2$ 或 $3$ 的双线性，以及 Frobenius 取逆。
这不是只把某个非平凡单位根随意称为全局 Weil 配对。

## 3. Kummer 扭曲、复共轭及两个不同的局部投影

令 $\rho:C\to\mathbb F^\times$ 为 $V$ 的乘法特征。
则圆分特征为 $\omega=\rho^{p+1}$，正确的单位特征为
$$\chi_0=\rho^p.$$
以
$$w=P\otimes\zeta_0^{-1}$$
作为 $V(-1)$ 的 $\mathbb F$ 基。
Cartan 在此基上的特征为
$\rho/\omega=\rho^{-p}=\chi_0^{-1}$，而
$$\tau(w)=-w.$$
因此对 $\chi_0$ 分量 Kummer 数据 $\xi$，下降到 $H^1(K,V)$ 后的
复共轭作用是
$$
\boxed{\tau_V(\xi)=-\bigl(\tau_{\rm units}\otimes\overline{\phantom a}\bigr)\xi,}
\tag{78.9}
$$
其中系数共轭为 $a\mapsto a^p$。这个负号来自 $(-1)$ 扭曲。

在一个所选的 $s$ 处，若 $\xi$ 是局部单位，记
$$
U_s(\xi)=
\log_{\zeta_s}\bigl(\xi^{(s^2-1)/p}\bigr)\in\mathbb F,
\tag{78.10}
$$
对形式线性组合按线性延拓理解。
则对应的 $V$ 不分歧 cocycle 在 $K_{(s)}$ 的算术 Frobenius 上取值为
$$
\frac{U_s(\xi)}{k_s}\,P.
\tag{78.11}
$$
原因是 Kummer cocycle 的 Frobenius 比值正是
$\xi^{(s^2-1)/p}$，而其值要由 $\zeta_s$ 改写到全局 $\zeta_0$ 基。

另一方面，令
$$\nu_s(\xi)=v_{(s)}(\xi)\in\mathbb F,\qquad v_{(s)}(s)=1.$$
它表示奇异商中的 Kummer$(s)$ 系数。
**赋值坐标不除以 $k_s$**：扭曲基已把全局 $\zeta_0$ 送到 $P$；
这里记录的是幂次／赋值，而不是某个剩余单位根的对数。

局部 Frobenius 把 $\zeta_0$ 变为其逆。因此：

- 在不分歧 cocycle 的 $V$ 坐标上，单位剩余对数产生的负号
  与 (78.9) 的负号相消，$\tau$ 作用为 $z\mapsto\bar z$。
- 在奇异赋值坐标上，$\tau$ 保持赋值，故 (78.9) 给
  $z\mapsto-\bar z$。

所以正投影 $\mathcal P^+=(1+\tau)/2$ 分别是
$$
z\longmapsto\frac{z+\bar z}{2}
\quad\text{（不分歧坐标）},\qquad
z\longmapsto\frac{z-\bar z}{2}
\quad\text{（奇异坐标）}.
\tag{78.12}
$$
前者取实部，后者保留纯虚部。不能在这两种坐标上统一使用
同一个未经说明的“取实部”操作。

### 3.1 $P_2$ 的复共轭所产生的因子

这里
$$\tau P_2=[i]P_2,$$
不能在共轭单位时把 $P_2$ 当作有理点。
因为 $F_A([i]X)=F_A(X)$、$\tau P=P$，
$$
\tau F_A(P_2+P)
=F_A([i]P_2+P)
=F_A(P_2-[i]P).
$$
后者是 $p$ 侧 Cartan 元素 $-i$ 的作用。
其单位特征值为
$$\chi_0(-i)=(-i)^{43}=i.$$
在辅助层选实挠点后，对其乘 $-i$ 已包含在范数子群 $H_s$ 中。
此外 $\tau\sigma_s\tau^{-1}=\sigma_s^{-1}$，故
$$\tau D_s\tau^{-1}\equiv-D_s\pmod p.$$
额外 $(7)$ 因子的 Frobenius 在该共轭下保持不变。
与 (78.9) 合并，得到同一原始族的准确关系
$$
\tau\kappa_0=-i\kappa_0,\qquad
\tau\kappa_s=i\kappa_s,\qquad
\tau\kappa_{qr}=-i\kappa_{qr}.
\tag{78.13}
$$
Robert 函数可能的十二次单位根在模 $43$ Kummer 群中为零，
这里没有遗留额外的 $43$ 次单位根修正。

这也解释 R70 的基单位值在 $\mathbb F$ 中呈 $x+xi$，
而 R73 的一阶值为 $17-17i$：它们分别与 (78.13) 的
不分歧局部作用一致。

## 4. 固定 $\Gamma_s$ 后，直接证明有限—奇异映射的负号

### 4.1 Artin 元素与一致化元

在 $s$ 除法域上取
$$
\gamma_s=2+i\bmod s,\qquad
\sigma_s=[\gamma_s]\in
\Gamma_s=\mathbb F_{s^2}^\times/H_s,
\qquad |H_s|=(s^2-1)/p.
$$
这里 $[\gamma_s]$ 是通过 CRT 取 $1\bmod\mathfrak m$、
$\gamma_s\bmod s$ 的**算术** Artin 元素。
它在 $s$ 挠点上作用为 $[\gamma_s]$，方向由 R70 的 primary
生成元证明固定。

在 $K_{(s)}$ 上，$A$ 的 CM 超奇异形式群给全分歧的
$(s^2-1)$ 次 $s$ 挠点扩张。
对一个原始 $s$ 挠点 $R_s$，其形式参数
$t(R_s)=-x(R_s)/y(R_s)$ 是此全分歧扩张的一致化元。
形式 CM 作用的一次项是 $\gamma_s t$，所以
$$
\frac{t([\gamma_s]R_s)}{t(R_s)}
\equiv\gamma_s\pmod{\mathfrak P}.
$$
向次数 $p$ 子扩张取 $H_s$ 范数，得一个一致化元 $\Pi$，并且
$$
\boxed{
\frac{\sigma_s\Pi}{\Pi}\equiv
\gamma_s^{|H_s|}=\zeta_s,\qquad
\Pi^{1-\sigma_s}\equiv\zeta_s^{-1}.
}
\tag{78.14}
$$
这同时确定了导数生成元与局部 tame 根的方向。

### 4.2 Hilbert 90 推导

先看一个循环全分歧 $p$ 次局部扩张 $L/F$，生成元 $\sigma$
满足 $\sigma\Pi/\Pi\equiv\zeta$。
设单位 $u\in L^\times$ 范数为一，并取
$$
D=\sum_{j=1}^{p-1}j\sigma^j,\qquad
(\sigma-1)D=p-N.
$$
Hilbert 90 给 $b$ 满足 $\sigma b/b=u$。
于是
$$k=u^D/b^p\in F^\times,$$
它在 $L^\times/L^{\times p}$ 中代表 $u^D$。
因 $u$ 是单位，
$$v_F(k)=-v_L(b).$$
又因为 $\sigma$ 在剩余域上平凡，
$$\bar u=\overline{\sigma b/b}=\zeta^{v_L(b)}.$$
因此
$$
\boxed{v_F(k)=-\log_\zeta(\bar u).}
\tag{78.15}
$$

在当前 Euler system 中，$s$ 在 $T$ 完全分裂，
所以范数关系给 $Nu_s=1$，且局部同余为
$$u_s\equiv u_0^{(s^2-1)/p}.$$
由 (78.14)、(78.15)，经过 $\chi_0$ 投影与扭曲后，
$$
\boxed{\nu_s(\kappa_s)=-U_s(\kappa_0).}
\tag{78.16}
$$
在 (78.16) 的右边，$U_s$ 仍指先取相应的单位 Kummer 数据，
不是已经除以 $k_s$ 的 $V$ Frobenius 坐标。

对二阶类同样适用。任一不同的候选惰性素数在
$T(t)/T$ 的 Frobenius 是 $\mathbb F_t^\times$ 标量，因而在
$p$ 次商上为一；所以 $s$ 在 $T(t)/T$ 完全分裂。
先施加 $D_t$，再在 $s$ 处使用上述 Hilbert 90，
局部同余及范数一的恒等式都保持。得到
$$
\boxed{\nu_q(\kappa_{qr})=-U_q(\kappa_r),\qquad
\nu_r(\kappa_{qr})=\Phi_r(\operatorname{loc}_r\kappa_q),}
\tag{78.17}
$$
其中 $\Phi_r$ 在这些已固定的坐标下也是负剩余对数。
R65 的 $(7)$ 因子已在 $\kappa_r$ 中乘过一次；
应用 (78.17) 不再另乘 $8/7$。

### 4.3 与原始文献的逐式校验

Rubin (1991), 印刷页 29 定义同一个 $D$ 并给出
$(\sigma-1)D=M-N$；印刷页 31 的 Proposition 2.3
将剩余类 $(x^{1-\sigma})^{1/d}$ 映到
$[N_{L/F}x]$，其中 $d=(N(s)-1)/M$。
取 $x=\Pi$，(78.14) 说明其输入的 $d$ 次幂为 $\zeta_s^{-1}$，
输出赋值为 $+1$。因此该交换图恰给
$\Phi_s=-\log_{\zeta_s}$，与 (78.15) 一致。

Oukhaba–Viguié (2013), 印刷页 156 另以
$\Pi^{1-\sigma}$、$\widehat\varphi$、$\varphi=-\widehat\varphi$
表述相关映射。本文不把这些符号未经整体翻译就代入
R73 已固定的算术 Artin 及正权导数约定；
数值定向完全使用 Rubin 原版交换图及直接推导 (78.15)。
无需在此判断其他文献采用的全部符号。
R65、R73 已使用的同构、支持和非零性结论不依赖这项符号选择。

## 5. 明确归一化局部 Tate 双基

令 $\chi_s:G_{\mathbb Q_s}\to\mathbb F_p$ 为算术 Frobenius 值为 $1$
的不分歧特征。定义
$$a_s=\chi_sP.$$
令 $\delta_s(s)\in H^1(\mathbb Q_s,\mu_p)$ 为 $s$ 的 Kummer 类。
局部映射
$$\mu_p\longrightarrow V_s^-,
\qquad \zeta_0\longmapsto[i]P$$
是 $G_{\mathbb Q_s}$ 等变的：两边的 Frobenius 都作用为 $-1$。
把 $\delta_s(s)$ 沿此映射推前，定义 $e_s$。
于是 $a_s,e_s$ 分别生成 R60 的不分歧与奇异直线。

以 (78.6) 的 Weil 配对取 cup product，再以局部不变量
$j/p\mapsto j\in\mathbb F_p$ 定义 $B_s$。此时
$$\boxed{B_s(a_s,e_s)=1.} \tag{78.18}$$
下面核对这个正号。由 $e_p(P,[i]P)=\zeta_0$，
所需 cup product 为 $\chi_s\cup\delta_s(s)$。
若 $\beta^p=s$，将 $\chi_s$ 的值提升到 $0,\ldots,p-1$，
则一上链 $b(g)=\beta^{\widetilde\chi_s(g)}$ 满足
$$
db(g,h)=
\delta_s(s)(g)^{\widetilde\chi_s(h)}
s^{\lfloor(\widetilde\chi_s(g)+\widetilde\chi_s(h))/p\rfloor}.
$$
利用一次 cup product 的反交换性，
$\chi_s\cup\delta_s(s)$ 正是由上式的进位因子代表的循环代数类。
它来自次数 $p$ 的不分歧扩张、算术 Frobenius 及一致化元 $s$，
其不变量为 $+1/p$。
这也与 Milne, Class Field Theory, III §1 对基本类的标准定义一致。

因此在 $K_{(s)}$ 上，$e_s$ 的奇异赋值坐标为 $i$。
若正投影后的类奇异坐标为 $\lambda i$，它对 R60 的 $e_s$
的系数就是 $\lambda$，无需再乘 $k_s$ 或 $2$。

不分歧部分则不同。对 $\mathbb Q_s$ 的不分歧类，
限制到 $K_{(s)}$ 把算术 Frobenius 换成其平方，故
$$
z(\operatorname{Frob}_{K_{(s)}})
=(1+\tau)z(\operatorname{Frob}_{\mathbb Q_s}).
$$
在正特征线上系数乘 $2$。从 (78.11) 恢复 $\mathbb Q_s$
不分歧系数时，必须除以这个 $2$。

## 6. 从原始值到 $m_{q,r}=37$

记 $p$ 处通常 Kummer 条件为 $L_p$。
R65 的基类 $\kappa_0$ 在
$H^1(K_p,V)/L_p$ 中非零，故对任何原始类定义唯一标量
$$
\alpha_n=
\frac{\operatorname{loc}_p(\kappa_n)\bmod L_p}
     {\operatorname{loc}_p(\kappa_0)\bmod L_p}
\in\mathbb F.
\tag{78.19}
$$
这是同一维 $\mathbb F$ 空间中两个向量的比值，
不依赖为该商空间额外选择基。
定义
$$d_r=\kappa_r-\alpha_r\kappa_0.$$
它属于只松弛 $r$ 的全局群。
从全局通常 Selmer 群为零可知，这个 $p$ 校正投影与 $\tau$ 相容。
结合 (78.13)，有 $\tau d_r=i d_r$。

R70 的 $r$ 处原始基单位值是
$$U_r(\kappa_0)=15+15i.$$
由 (78.16)，
$$\nu_r(\kappa_r)=-15-15i=28+28i.$$
$\kappa_0$ 在 $r$ 是单位，故 $p$ 校正不改变此赋值。
用 (78.12) 的奇异正投影，得到
$$
\nu_r(\mathcal P^+d_r)=28i.
$$
因此
$$
\boxed{\lambda_r=28,\qquad
c_r=20\,\operatorname{desc}_{K/\mathbb Q}
\bigl(\mathcal P^+d_r\bigr),}
\tag{78.20}
$$
其中 $20=28^{-1}\bmod43$。
下降是限制映射到正分量的逆；
R60 的唯一性保证 (78.20) 正是其 $c_r$。

在 $q$，R70 给 $\operatorname{loc}_q\kappa_0=0$，
故 $p$ 校正完全不影响 $d_r$ 的局部值。
R73 的原始数据为
$$U_q(\kappa_r)=17+26i.$$
用 $k_q=29$ 改成全局 $V$ 基，得到
$$
\frac{17+26i}{29}=8+35i.
$$
正投影保留实部 $8$；再从 $K_{(q)}$ 下降到
$\mathbb Q_q$，其 Frobenius 系数为 $8/2=4$。
最后由 (78.20) 归一化：
$$
\boxed{
m_{q,r}=
\frac{17}{2\cdot29\cdot28}
=20\cdot4=37.
}
\tag{78.21}
$$
其中各项分别来自 R73 的原始实部、二次限制、全局 Weil 单位根基、
以及 $r$ 处规范奇异坐标；没有把其中任何一项省略。
$k_r=40$ 不出现在最终分母里，因为 $r$ 处采用赋值坐标，
而 (78.16) 已将局部对数换成该赋值。

R60 的全局互反给
$$m_{r,q}=-m_{q,r}=6,$$
从而得到 (78.1)。反向的 $6$ 是由全局互反证明，
不是声称另外展开并计算了一个尚未算出的导数。
若使用整体相反的 Weil 配对及相应双基，显示的矩阵符号也会改变；
本文的数值都相对于 (78.6)、(78.18) 的明确选择。
零／非零、秩与修改 Selmer 群不受该选择影响。

## 7. 对退化 $q$ 的二阶类给出实际规范化

因为 $\kappa_0|q=0$，由有限—奇异关系，
$\kappa_q$ 在 $q$ 的奇异商为零。
它因此属于只松弛 $p$ 的一维群，故
$$\kappa_q=\alpha_q\kappa_0. \tag{78.22}$$
对同一个原始 $\kappa_{qr}$，(78.17) 给
$$
\nu_q(\kappa_{qr})=-(17+26i)=26+17i,
\tag{78.23}
$$
且在 $r$ 的奇异坐标为 $\alpha_q\nu_r(\kappa_r)$。
因此先消去 $r$，再消去 $p$，得到
$$
\boxed{
d_q=\kappa_{qr}-\alpha_q\kappa_r
+(\alpha_q\alpha_r-\alpha_{qr})\kappa_0.
}
\tag{78.24}
$$
这个类只在 $q$ 松弛。式中使用原始二阶类，
没有把已校正的 $d_r$ 擅自当作 Euler system 的成员。

在 $q$，后两项均无奇异部分；
所以 (78.12)、(78.23) 直接给
$$\nu_q(\mathcal P^+d_q)=17i.$$
由 R60 唯一归一化，
$$
\boxed{
c_q=38\,\operatorname{desc}_{K/\mathbb Q}
\mathcal P^+
\left[
\kappa_{qr}-\alpha_q\kappa_r
+(\alpha_q\alpha_r-\alpha_{qr})\kappa_0
\right],
}
\tag{78.25}
$$
其中 $38=17^{-1}\bmod43$。
这给出 (78.2)，也说明该具体退化素数已经有确定的
辅助素数、确定的二阶奇异系数和确定的规范化倍数。

从 (78.13) 及 $p$ 校正的 $\tau$ 相容性，还可核对
$$
\bar\alpha_r=-\alpha_r,\qquad
\bar\alpha_q=-\alpha_q,\qquad
\bar\alpha_{qr}=\alpha_{qr}.
\tag{78.26}
$$
即前两个系数纯虚，第三个在 $\mathbb F_p$；
式 (78.24) 因而确有 $\tau d_q=-i d_q$。
这些关系没有给出它们的数值。
若要把 (78.25) 展开成完全数值化的全局 Kummer 根式代表，
仍须计算 (78.19) 的三个 $p$ 处商坐标。
本结果不声称已经完成这项 $p$ 进计算。

## 8. 可重复的有限域证书与范围

- [Python 标准库核验程序](../notes/verify_r78_pairing_normalization.py)。
- [配对与规范化完整证书](../notes/r78_pairing_normalization_certificate.json)。
- 原始较大有限域计算仍使用
  [R73 C++ 程序](../notes/verify_r73_derivative_residue.cpp)及
  [其完整证书](../notes/r73_derivative_residue_certificate.json)。

从仓库根目录执行：

~~~bash
python3 topics/serre-uniformity/notes/verify_r78_pairing_normalization.py
~~~

程序重新计算 R70 在 $859,49019$ 的完整基单位投影，
并逐项比较保存的证书；计算两种 Weil 配对公式；
重新生成 R73 的全部 $860$ 个 $\Gamma_r$ 权，
核对每个权恰出现二十次、加权和及无权和，
最后计算 (78.20)、(78.21)、(78.23) 和矩阵行列式。
它读取 R73 的同源求值结果；重算这些同源本身应另运行 R73 的
C++ 入口，不把读取已有结果说成重新完成该大循环。

这个修改 Selmer 群因 (78.1) 为零。
如果实际存在一条同余曲线且其改变条件恰是这两处，
相应实际 Selmer 群才由该矩阵控制。
本文既没有构造这样的非 CM 曲线，也没有对变化 $p$ 给出统一排除。

## 9. 已核对的原始来源

- [R60](R60-selmer-matrix-kummer-residue-symbols.md)：
  规范单素数类、交替性及矩阵核。
- [R65](R65-elliptic-unit-first-second-derivatives.md)、
  [R70](R70-robert-unit-finite-field-certificates.md)、
  [R73](R73-explicit-auxiliary-derivative-residue.md)：
  正确扭曲、同一原始单位族和有限域数据。
- K. Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*,
  Inventiones Mathematicae **103** (1991), 25–68，
  [原刊档案](http://resolver.sub.uni-goettingen.de/purl?PPN356556735_0103)，
  印刷页 29 的导数定义、Propositions 2.2–2.4。
  此处使用原版第 31 页交换图固定有限—奇异符号。
- V. S. Miller, *The Weil pairing, and its efficient calculation*,
  Journal of Cryptology **17** (2004), 235–261，
  [作者公开全文](https://www.researchgate.net/publication/220478991_The_Weil_Pairing_and_Its_Efficient_Calculation)，
  式 (10)、Proposition 8／式 (11)。
  配对倒数约定的区别也核对于
  [Sutherland, 18.783 Lecture 23, Theorem 23.30](https://math.mit.edu/classes/18.783/2025/LectureNotes23.pdf)。
- J. S. Milne, *Class Field Theory*, v4.03 (2020)，
  [作者讲义](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，
  III §1，特别是印刷页 99–102 的不变量和不分歧基本类。
- H. Oukhaba–S. Viguié,
  [*On the Gras conjecture for imaginary quadratic fields*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf),
  Canadian Mathematical Bulletin **56** (2013), 148–160。
  §4 用于原始范数及同余关系；本结果的数值符号由 §4.3 所述
  Rubin 原文及 Hilbert 90 直接固定。

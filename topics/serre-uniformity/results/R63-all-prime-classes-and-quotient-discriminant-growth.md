# R63：全部指数同余类的短关系法与商域判别式增长

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的无条件全局必要条件。** 本文将 R62 的变化商域约束从 $p\equiv1\pmod{12}$ 推广到全部 $p>37$。局部循环总分歧扩张给出剩余域仍为 $\mathbb F_q$ 的实际好约化迹；十二次幂消除惯性而不必假设二次好约化扭曲。对 $h_K>1$，得到
$$
\log p<28\log(8D^{5/2})
\exp\!\left(2\sqrt{\log18\,\log h}\right),
\quad D=|D_K|,\quad h=h_K,
$$
特别地
$$
\boxed{D>\exp\!\left(\frac{(\log\log p)^2}{64}\right).}
$$
这是判别式增长的必要下界，允许 $K$ 随 $p$ 增长。类数一分支仍未解决，本文也不把这一增长下界写成绝对素数界。

## 1. 假设、独立记号与定理

设 $E/\mathbb Q$ 无 CM，$p>37$，且
$$
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).
\tag{63.1}
$$
令 $K$ 为正规化子商 $N/C$ 给出的二次域。由 R5，$K$ 虚二次，$p$ 在 $K$ 中不分歧且惰性。令
$$
\lambda:G_K\twoheadrightarrow\mathbb F_{p^2}^{\times}
$$
为限制到完整 Cartan 后的一维特征。

**本文重新定义并始终使用**
$$
\boxed{\mu=\lambda^{12}.}
\tag{63.2}
$$
因此不沿用 R58、R61、R62 中专属平方分支的 $\mu=\lambda^2$，也不调用它们的二次好约化扭曲结论。

假定 $h=h_K>1$，置
$$
D=|D_K|,\qquad \mathcal B_D=8D^{5/2},
\qquad m_t=\lfloor h^{1/t}\rfloor\quad(t\ge1).
$$
所有对数为实自然对数。非平凡虚二次类群满足 $D\ge15$，其小判别式检查见 R62 §1。

**定理 R63。** 对每个正整数 $t$，都有
$$
\boxed{
\log p<2^{t-1}\log4+
3\cdot2^{t-1}(9^t-1)m_t\log\mathcal B_D.
}
\tag{63.3}
$$
特别地，
$$
\boxed{
\log p<28\log\mathcal B_D\,
\exp\!\left(2\sqrt{\log18\,\log h}\right).
}
\tag{63.4}
$$
消去类数后，有完全显式的
$$
\boxed{
\log p<28\left(\log8+\frac52\log D\right)
\exp\!\left(
2\sqrt{\log18\left(\frac12\log D+\log\log D\right)}
\right).
}
\tag{63.5}
$$
它给出
$$
\boxed{\log\log p<8\sqrt{\log D},}
\tag{63.6}
$$
以及沿任何实际 $h_K>1$、$p\to\infty$ 的异常序列，
$$
\boxed{
\liminf\frac{\log|D_K|}{(\log\log p)^2}
\ge\frac1{2\log18}.
}
\tag{63.7}
$$
等价地，任意 $c<1/(2\log18)$ 最终给出有效必要下界
$D>\exp(c(\log\log p)^2)$。这只是下界的渐近系数，不声称有匹配的异常序列或等价渐近。

## 2. 十二次幂的主理想公式，无类数一假设

[R21](R21-twelfth-power-signature-and-cm-twists.md) 定理 A 已证明
$$
\mu\text{ 在全部 }w\nmid p\text{ 处不分歧},
\qquad
\mu|_{I_p}\in\{\omega_2^{12},\omega_2^{12p}\}.
$$
选择 $\lambda$ 的共轭方向或 $\mathcal O_K/p\simeq\mathbb F_{p^2}$ 的两个嵌入之一，使惯性型为 $\omega_2^{12}$。

使用算术 Frobenius 的 Artin 约定。$K_p/\mathbb Q_p$ 是不分歧二次扩张，其剩余域为 $\mathbb F_{p^2}$；局部互反映射将一个单位 $u$ 在 $\omega_2$ 下送到其剩余元的逆。因此在 $p$ 单位上的 $\mu$ 值为 $\widetilde u^{-12}$。

对 $\alpha\in K^\times$ 且 $v_p(\alpha)=0$，主 idèle 在全局互反映射下平凡。$p$ 外各分量因为 $\mu$ 不分歧，其乘积为主理想 $(\alpha)$ 的 Artin 值；$p$ 单位分量为 $\widetilde\alpha^{-12}$。于是
$$
\boxed{\mu((\alpha))\equiv\alpha^{12}\pmod{p\mathcal O_K}.}
\tag{63.8}
$$
这只使用精确惯性型及全局互反关系，与 $h_K$ 是否等于一无关。这里 $\widetilde\alpha$ 表示剩余元，$\bar\alpha$ 始终表示二次共轭。

## 3. 分裂辅助素数处的实际好约化迹

固定在 $K$ 分裂的有理素数 $q$。因 $p$ 惰性，自动有 $q\ne p$。对选定的 $K$ 上方位，$K_{\mathfrak q}=\mathbb Q_q$，所以
$$
\bar\rho_{E,p}(G_{\mathbb Q_q})\subset C.
\tag{63.9}
$$

### 3.1 潜在乘法约化仍给 q≡1 mod p

一个局部二次扭曲使曲线为分裂 Tate 曲线；这个扭曲只乘标量 $\pm I$，仍保持残余像在 $C$。Frobenius 特征值为 $1,q$。非分裂 Cartan 中有 $\mathbb F_p$ 特征值的元素必为标量，故
$$
q\equiv1\pmod p.
\tag{63.10}
$$
特别地，若 $p>4q$，这个分支不可能。

### 3.2 有限惯性及 Frobenius 交换的特征零提升

假定 $E/\mathbb Q_q$ 潜在好约化。令 $\rho$ 为其在 $T_p(E)$ 上的表示，$I_q$ 为惯性，记
$$
\Gamma=\rho(I_q).
$$
潜在好约化使 $\Gamma$ 有限。模 $p$ 约化在 $\Gamma$ 上忠实：其核包含于 $1+pM_2(\mathbb Z_p)$，而当 $p$ 奇时，$p$ 进对数说明该群没有非平凡有限阶元素。

由 (63.9)，$\Gamma$ 模 $p$ 的像在循环群 $C$ 内，因此 $\Gamma$ 本身循环。它忠实作用在取得好约化后的椭圆曲线特殊纤维上。R21 §5 的自同构次数论证给
$$
e=|\Gamma|\in\{1,2,3,4,6\},\qquad e\mid12.
\tag{63.11}
$$
这个论证也包含 $q=2,3$ 的野惯性：只控制已知为循环的惯性像，不把整个特殊纤维自同构群假定为循环。

对任意 $g\in G_{\mathbb Q_q}$、$\gamma\in\Gamma$，$\rho(g)\gamma\rho(g)^{-1}$ 仍在 $\Gamma$ 内。其模 $p$ 约化与 $\gamma$ 相同，因为整个残余局部像在交换群 $C$ 内。忠实性于是给
$$
\rho(g)\gamma\rho(g)^{-1}=\gamma.
\tag{63.12}
$$
因此特征零的整个局部表示确实交换有限惯性；这不是仅依据“有限惯性循环”就推断 Frobenius 交换。

### 3.3 连续 Frobenius 截面与循环总分歧好约化扩张

局部 Galois 正合列为
$$
1\longrightarrow I_q\longrightarrow G_{\mathbb Q_q}
\longrightarrow\widehat{\mathbb Z}\longrightarrow1.
$$
选择算术 Frobenius 的一个提升 $\phi$。由 $\widehat{\mathbb Z}$ 的自由幂有限循环性质，映射 $1\mapsto\phi$ 延拓为连续同态
$$
s:\widehat{\mathbb Z}\longrightarrow G_{\mathbb Q_q}.
$$
与未分歧商的复合将 $1$ 送到 $1$，故为恒等映射；所以 $s$ 是连续截面，且
$G_{\mathbb Q_q}=I_q\rtimes s(\widehat{\mathbb Z})$。

将惯性满射 $I_q\to\Gamma$ 延拓为
$$
\tau:G_{\mathbb Q_q}\longrightarrow\Gamma,
\qquad \tau(i\,s(z))=\rho(i).
\tag{63.13}
$$
(63.12) 保证其为同态；半直积分解的连续性及 $\Gamma$ 有限保证它连续。它在 $I_q$ 上满射，并在 Frobenius 截面上平凡。

令 $L/\mathbb Q_q$ 为 $\ker\tau$ 的不动域。则 $L/\mathbb Q_q$ 为次数 $e$ 的循环扩张。由于惯性已经映到全部 $\Gamma$，该扩张**全分歧，剩余域仍为 $\mathbb F_q$**。而
$$
\rho(I_L)=1,
$$
故 Néron–Ogg–Shafarevich 判据使 $E_L$ 好约化。

这一步不是对 $E$ 作一个一般 $e$ 次自同构扭曲；它是一个真实的局部基域扩张。即使 $q=2,3$ 且扩张野分歧，上面的有限群及连续截面论证也不变。

### 3.4 剩余域不变给真正的 q 迹

令 $\widetilde E/\mathbb F_q$ 为 $E_L$ 的好约化特殊纤维，则
$$
a_q=q+1-\#\widetilde E(\mathbb F_q)\in\mathbb Z,
\qquad |a_q|\le2\sqrt q.
$$
取 Frobenius 多项式
$$
T^2-a_qT+q.
\tag{63.14}
$$
Frobenius 截面位于 $G_L$，且其在 $L$ 的剩余域上仍为 $q$ 次幂 Frobenius。因此对与选定 $\lambda$ 方向一致的一根 $\beta\in\mathbb F_{p^2}$，
$$
\boxed{\beta^{12}=\mu(\mathfrak q),\qquad
\beta+\beta^p\equiv a_q,\qquad \beta^{p+1}\equiv q.}
\tag{63.15}
$$
改变 Frobenius 提升或好约化扩张可能改变具体根，但惯性阶整除十二，所以第一式保持不变。所用迹始终来自某条实际 $\mathbb F_q$ 椭圆曲线。

## 4. 十二次幂的实迹范数引理

取不同的分裂素数 $q_1,\ldots,q_s$，假定
$$
p>4\max_iq_i.
\tag{63.16}
$$
第 3 节排除潜在乘法分支，给出整数 $a_i$ 及实际 Frobenius 根 $\pi_i$。令
$$
\pi_i^2-a_i\pi_i+q_i=0,
\qquad F_i=\mathbb Q(\pi_i),
\qquad F=F_1\cdots F_s.
$$
$a_i^2<4q_i$，故 $F_i$ 虚二次。非分裂 Cartan 条件及
$0<4q_i-a_i^2<p$ 使该判别式模 $p$ 非平方；所以 $p$ 在各 $F_i$ 惰性。

记 $F^+=F^{\langle c\rangle}$。Frobenius 在每个 $F_i$ 上等于复共轭，故在 $F$ 上等于 $c$，于是 $p$ 在 $F^+$ 完全分裂，且
$$
d=[F^+:\mathbb Q]\le2^{s-1}.
$$

**引理 63.1。** 假定 $K\cap F=\mathbb Q$。对一条非零有向主理想关系，负指数转为共轭后写为
$$
\mathfrak a=
\prod_i\mathfrak q_i^{\max(u_i,0)}
\bar{\mathfrak q}_i^{\max(-u_i,0)}
=(\alpha),
\qquad
N=N\mathfrak a=\prod_iq_i^{|u_i|},
\tag{63.17}
$$
则
$$
\boxed{p<(4N^6)^d.}
\tag{63.18}
$$

**证明。** $\alpha\in\mathcal O_K$，且 $N_{K/\mathbb Q}\alpha=N$。每个有理素数至多取一支，至少一个指数正，因此 $\mathfrak a\ne\bar{\mathfrak a}$。

特别地，**$\alpha^{12}$ 仍非实**：否则其主理想等于共轭，给
$\mathfrak a^{12}=\bar{\mathfrak a}^{12}$，由素理想唯一分解推出 $\mathfrak a=\bar{\mathfrak a}$，矛盾。令
$$
T=\alpha^{12}+\bar\alpha^{12}\in\mathbb Z,
\qquad |T|<2N^6.
\tag{63.19}
$$

在 $KF$ 的一个共同 $p$ 进剩余嵌入下，选择每个 $\pi_i$ 或其共轭，使其约化为对应有向素理想的 $\beta_i$。这是可能的，因为所有生成二次域在 $p$ 不分歧且惰性，剩余域为 $\mathbb F_{p^2}$；先固定在 $K$ 上用于 (63.8) 的识别，再分别选择多项式两根之一。

令
$$
z=\prod_i\pi_i^{|u_i|},\qquad z\bar z=N,
\qquad S=z^{12}+\bar z^{12}\in\mathcal O_{F^+}.
$$
由 (63.8)、(63.15)，
$$
z^{12}\equiv\mu(\mathfrak a)
\equiv\alpha^{12}\pmod p.
$$
施加剩余 Frobenius，它在 $K$、$F_i$ 上同时为复共轭，得到
$$
\boxed{S\equiv T\pmod{\mathfrak P^+},}
\tag{63.20}
$$
其中 $\mathfrak P^+$ 是 $F^+$ 的次数一 $p$ 上方素理想。

若 $S=T$，则两组根具有相同的和及积 $N^{12}$，所以
$$
\{z^{12},\bar z^{12}\}
=\{\alpha^{12},\bar\alpha^{12}\}.
$$
因为 $\alpha^{12}$ 非实，它生成 $K$；同时它或其共轭属于 $F$。故 $K\subseteq F$，与交域假设矛盾。因此 $S-T$ 是非零代数整数，其实域范数是被 $p$ 整除的非零整数。

每个嵌入下 $|z|=\sqrt N$，故 $|S|\le2N^6$。结合 (63.19)，得到
$$
p\le|N_{F^+/\mathbb Q}(S-T)|<(4N^6)^d.
$$
证毕。

**根单位不构成额外障碍。** 本证明直接比较十二次幂后的和与积。零差使 $\alpha^{12}\in F$，已足以推出 $K\subseteq F$；不需要先取十二次根，也不需要将 $\mathbb Q(\zeta_{12})$ 或其平方类预先加入 $F$。因此无需为了排除某个“镜像域”另加 $(3/q)=-1$ 条件。

## 5. 非主分裂素数、平方类选择及短关系

这里调用 [R62](R62-many-prime-relations-and-effective-quotient-bound.md) 中两个只关于虚二次域的引理。它们的证明不使用 $p\equiv1\pmod{12}$：

1. 引理 62.2 用固定非主约化二次型及 CRT，构造任意多个不同的奇非主分裂素数。对其乘积
   $$
   P_k=\prod_{i=1}^kq_i,
   \qquad
   P_k<\mathcal B_D^{(3^k-1)/2}.
   \tag{63.21}
   $$
   二进处 $Q(x,1)$ 可能为零函数的例外，通过固定 $y=2$、$x$ 奇处理；所取素数确为一个非主整理想的素因子。
2. 引理 62.3：从 $2t$ 个与 $K$ 不同的二次域中，可以选择 $t$ 个，使其合成与 $K$ 的交为 $\mathbb Q$。证明在平方类空间中对满足 $\ell(K)=1$ 的线性泛函取平均；允许所列域重复。

固定 $t\ge1$，构造 $2t$ 个素数，令 $P=P_{2t}$，并定义最终比较量
$$
\mathscr V=4^{2^{t-1}}P^{6m_t2^{t-1}}.
\tag{63.22}
$$
显然 $\mathscr V\ge4P$。如果 $p\le4\max q_i$，则 $p<4P\le\mathscr V$，这一分支已经完成。潜在乘法分支也由 (63.10) 落在这里；不能将它与尚未选择的某条关系的较小 $N$ 直接比较。

以下假定 $p>4\max q_i$，利用第 3 节构造所有实际 Frobenius 域 $F_i$。每个 $F_i\ne K$：如果相等，$\pi_i\in\mathcal O_K$ 的范数是 $q_i$，其主理想为 $q_i$ 上方某一素理想，迫使两支都主，与构造矛盾。

平方类选择引理给 $t$ 个指标，使 $K\cap F=\mathbb Q$。对其选定素理想类，
$$
(m_t+1)^t>h
$$
保证有非零有向主关系，其各指数满足 $|u_i|\le m_t$。负指数按
$\mathfrak q_i^{-1}=q_i^{-1}\bar{\mathfrak q}_i$ 转换为 (63.17)，所以
$$
N\le P^{m_t}.
$$
引理 63.1 给
$$
p<(4N^6)^{[F^+:\mathbb Q]}
\le4^{2^{t-1}}P^{6m_t2^{t-1}}
=\mathscr V.
\tag{63.23}
$$
这完成两种分支。由 (63.21)，
$$
\log P<\frac{9^t-1}{2}\log\mathcal B_D,
$$
代入即得 (63.3)。与 R62 相比，范数中的幂次从 $1/2$ 换为 $6$，故相应主项增加十二倍；平方类选择及主理想关系的长度均保持不变。

## 6. 优化数量、消去类数及明确反演

置 $H=\log h>0$、$a_0=\log18$，取
$$
t=\left\lceil\sqrt{H/a_0}\right\rceil\ge1,
\qquad R=18^t h^{1/t}.
$$
从 (63.3) 删除负项，并用 $m_t\le h^{1/t}$，得
$$
\log p<2^{t-1}\log4+\frac32R\log\mathcal B_D.
\tag{63.24}
$$
若 $u=\sqrt{H/a_0}$，则
$$
a_0t+H/t-2\sqrt{a_0H}
=\frac{a_0(t-u)^2}{t}\le a_0,
$$
所以
$$
R\le18e^{2\sqrt{a_0H}},
\qquad \frac{2^t}{R}=9^{-t}h^{-1/t}\le\frac19.
$$
于是
$$
\begin{aligned}
\log p
&<\left(27\log\mathcal B_D+\log4\right)
e^{2\sqrt{\log18\,\log h}}\\
&<28\log\mathcal B_D\,
e^{2\sqrt{\log18\,\log h}}.
\end{aligned}
$$
最后一步只需 $\mathcal B_D>4$，由 $D\ge15$ 满足。证明 (63.4)。

R58 §7 的 Minkowski 理想计数，亦在 R62 §6 使用，给
$$
h<\sqrt D\log D.
\tag{63.25}
$$
这没有 $p$ 的同余条件。将其代入 (63.4)，便得 (63.5)。

为核验粗常数，令 $x=\log D\ge\log15>5/2$。有
$$
\log h<\frac x2+\log x\le x,
\qquad \log\mathcal B_D=\log8+\frac52x<4x.
$$
函数
$$
f(x)=\frac92\sqrt x-\log(112x)
$$
在 $x\ge5/2$ 上导数为正，且起点 $f(5/2)>0$；因此
$\log(112x)<(9/2)\sqrt x$。又 $2\sqrt{\log18}<7/2$，故
$$
\begin{aligned}
\log\log p
&<\log(28\log\mathcal B_D)
 +2\sqrt{\log18\,\log h}\\
&<\frac92\sqrt x+\frac72\sqrt x
=8\sqrt x.
\end{aligned}
$$
这证明 (63.6)，并因两边为正，给出题首的 $D>\exp((\log\log p)^2/64)$。

最后，当 $D\to\infty$，(63.5) 的对数为
$$
\log\log p
<\bigl(\sqrt{2\log18}+o(1)\bigr)\sqrt{\log D}.
$$
粗下界已保证 $p\to\infty$ 时 $D\to\infty$，所以可反演得到 (63.7)。全部函数和误差均由显式表达式给定，任何较小渐近系数的最终阈值可以有效确定。

## 7. 未消除的两个全局瓶颈

本文得到的是对实际曲线及其实际商域的约束；没有假定存在全局 CM 特征零提升，也没有把一维残余特征的有理性提升为新形式的有理系数。

但 $h_K>1$ 时，判别式仍可依 (63.6) 或 (63.7) 增长。这些必要下界没有给 $D_K$ 上界，不能自行排除全部大 $p$。

若 $h_K=1$，非主分裂素理想不存在，本文的避素构造无法开始。在该分支，Frobenius 域可以恰等于 $K$，从而实迹差确实可能为零；这正是需要处理的 CM 比较情形。R21 的有界阶差特征、四次扭曲参数和可能的三次反圆分特征仍需独立控制，其导子或分母并未由本文约束。

R62 的平方分支保留更小常数 $5/2$ 和粗反演常数 $36$；本文以常数 $28$ 和 $64$ 换取全部素数同余类。两者的判别式下界具有相同的领先渐近系数。

## 8. 所用输入

- [R21](R21-twelfth-power-signature-and-cm-twists.md)：精确十二次幂惯性型；$p$ 外包括 $2,3$ 的有限循环自同构阶论证。
- [R61](R61-two-prime-relations-and-discriminant-growth.md)：有向理想关系、共同剩余嵌入和实域范数的基本结构；本篇对十二次幂重新证明非零差，未直接外推其平方公式。
- [R62](R62-many-prime-relations-and-effective-quotient-bound.md)，引理 62.2、62.3：纯数域的 CRT 避素构造和平方类选择。本文已指出它们没有素数同余限制。
- Néron–Ogg–Shafarevich 判据；有限惯性模 $p$ 的忠实性、连续 Frobenius 截面及其延拓步骤已在第 3 节展开。所构造的扩张为总分歧扩张，未把剩余次数的增长隐藏在 $q$ 迹记号中。
- 局部与全局互反映射可参见 J. S. Milne, *Class Field Theory*, v4.03 (2020), Chapters I、V，[作者原文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)；主理想计算已在第 2 节展开。

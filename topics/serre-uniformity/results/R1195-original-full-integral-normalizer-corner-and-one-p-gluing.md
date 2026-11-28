# R1195：原完整正规化子整角与准确的一个 p 拼接模

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126。

## 1. 精确结论

设 $p>3$，$m=(p-1)/2$，并置
$$
G=\operatorname{PGL}_2(\mathbf F_p),\qquad
N=N_{\rm ns}/\mathbf F_p^\times,\qquad
e_N=\frac1{2(p+1)}\sum_{n\in N}n,
\qquad \mathcal A=e_N\mathbf Z_p[G]e_N.
\tag{1195.1}
$$
有限表示的参数保持 [R1029 §2](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)
及 [R1193 §2](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md)：
$V_r$ 是尖点型 $\widetilde\omega_2^{r(p-1)}$，$P_a$ 是主系列
$(\widetilde\omega^a,\widetilde\omega^{-a})$。
令
$$
\mathcal R=\{r:1\le r\le m,\ r\text{ 为奇数}\},
\qquad
\mathcal O_p=\{(x,y)\in\mathbf Z_p^2:x\equiv y\pmod p\}.
$$
原整角的完整答案是
$$
\boxed{\quad
\mathcal A\simeq
\begin{cases}
\displaystyle\prod_{r\in\mathcal R}\mathcal O_p,
 &p\equiv3\pmod4,\\[2mm]
\displaystyle\left(\prod_{r\in\mathcal R}\mathcal O_p\right)\times\mathbf Z_p,
 &p\equiv1\pmod4.
\end{cases}\quad}
\tag{1195.2}
$$
第一个二元因子对应 $(V_1,\mathbf1)$；其余对应 $(V_r,P_{r-1})$。
额外的一元因子对应有限二次 Steinberg 表示 $S_\eta=\operatorname{St}\otimes(\eta\circ\det)$。
因此这不是把不同 finite types 无条件整地拆开；每一对之间的唯一整同余正是模 $p$ 同余。

对任意由这个真实角作用的有限自由 $\mathbf Z_p$-格，§6 进一步给其两种泛纤维子格的准确拼接指数，而不只给一个上界。
在原课题的几何应用中，保留 $p\equiv5\pmod6$ 两行、同一个原 $X_1,J,D_0$ 与六标记下降。
本篇不据有限角证明指定 MW 横截单位。

## 2. 全部球面表示，包含二次退化行

在特征零中，$N$-固定空间非零的不可约表示恰为下表，且每个固定空间均为一维。

| 有限表示 | 参数及出现条件 | 维数 |
|---|---|---:|
| $\mathbf1$ | 总出现 | $1$ |
| $V_r$ | $1\le r\le m$，$r$ 奇 | $p-1$ |
| $P_a$ | $1\le a<m$，$a$ 偶 | $p+1$ |
| $S_\eta$ | 仅 $p\equiv1\pmod4$ | $p$ |

这是 Mercuri–Schoof Proposition 2.1 的完整正规化子判据；原 R1029 已按 Cartan 与其另一陪集的 character 均值分别证明尖点的奇性和主系列的偶性。
两个退化项也可直接核：$N$ 在 $\mathbf P^1(\mathbf F_p)$ 上传递，所以通常 Steinberg 无固定向量。
一维二次 determinant character 无固定向量，因为 $\det N_{\rm ns}=\mathbf F_p^\times$。

对 $S_\eta$，把 Steinberg 写为该置换表示减去常数。点稳定子在 $N$ 中阶为二，其非平凡元的 determinant 模平方为 $-1$。
Frobenius reciprocity 给
$$
\dim S_\eta^N=1\quad\Longleftrightarrow\quad\eta(-1)=1.
\tag{1195.3}
$$
这支付了两行的差别，未将上一行排除二次型的论证挪到下一行。

所有这些表示的 character 值都在 $\mathbf Q_p$：split Teichmüller 值已在该域，nonsplit character 值为 $-z^r-z^{-r}$，未分歧 Frobenius 将两项交换。
它们也确实可定义在 $\mathbf Q_p$ 上。一个自足理由是：置换模 $\mathbf Q_p[G/N]$ 在分裂域上每个球面表示仅出现一次，Schur 指数必须整除这个重数，因而为一。
由此
$$
\mathcal A\otimes\mathbf Q_p
\simeq\prod_{\pi\text{ 在上表中}}\mathbf Q_p,
\tag{1195.4}
$$
坐标是对 $\pi^N$ 的实际标量作用。
特别该角交换，且每个 $\mathcal A$ 元素的所有坐标均在 $\mathbf Z_p$：取稳定整格，再用 $e_N$ 取其秩一固定直和因子即可。

## 3. 每一对的唯一 N 可见剩余因子

对奇 $r>1$，令 $a=r-1$。R1193 (1193.6) 的同一个 Brauer character 计算给
$$
\overline V_r^{\rm ss}=W_a\oplus Z_r,
\qquad
\overline P_a^{\rm ss}=W_a\oplus Z'_a,
$$
$$
W_a=\operatorname{Sym}^{2a}k^2\otimes\det^{-a},\quad
Z_r=\operatorname{Sym}^{p-1-2r}k^2\otimes\det^r,\quad
Z'_a=\operatorname{Sym}^{p-1-2a}k^2\otimes\det^a.
\tag{1195.5}
$$
此处可以先取分裂剩余域 $k$；后文所得标量同余仍在 $\mathbf F_p$ 上。
同一公式在 $r=1$ 时给 $\overline V_1^{\rm ss}=\mathbf1\oplus Z_1$。
所有对称幂的次数均在 $[0,p-1]$ 内。

为明确这些式子不依赖某个已分裂的整格，直接在 $p$-regular 元上核其 Brauer character：split 元的两个对称幂指数和给尖点值零或主系列值 $z^a+z^{-a}$；nonsplit 元上的指数和分别为 $-z^r-z^{-r}$ 或零；中心处维数也准确相加为 $p-1$ 或 $p+1$。
Brauer–Nesbitt 因而给任意稳定格的上述半单化。
在本范围内对称幂不可约，可用两个根子群的有限差分提取全部 divided derivatives 证明；所需阶乘均小于 $p$。

用 Cartan eigenvariables $A,B$。$W_a$ 的 Cartan 固定线为 $kA^aB^a$，正规化子交换元在它上作用为 $(-1)^a=1$，故
$$
\dim W_a^N=1.
$$
在 $Z_r$ 上，固定单项式的指数必须满足
$i\equiv p-r\pmod{p+1}$，但 $0\le i\le p-1-2r$；没有解。
在 $Z'_a$ 上，同样要求 $i\equiv p-a\pmod{p+1}$，但
$0\le i\le p-1-2a$；也没有解。
因此
$$
e_NZ_r=e_NZ'_a=0.
\tag{1195.6}
$$
本结论关于真正的 Cartan 和正规化子，不是只比较惯性指数。

现在取任意 $h\in\mathcal A$。因为 $h=e_Nhe_N$，它在特征零表示上的 trace 正是其 $N$-固定线上的标量。
在稳定格的任意 $G$-稳定组成列上逐因子取 trace，(1195.5)–(1195.6) 说明
$$
h(V_r^N)\equiv h(P_{r-1}^N)\pmod p\quad(r>1),
\qquad h(V_1^N)\equiv h(\mathbf1)\pmod p.
\tag{1195.7}
$$
这给 (1195.2) 所有模 $p$ 同余的必要性；没有只对某一组特殊球面函数检查。

## 4. 真实整幂等元及 p 倍单型投影

令 $e_\pi\in\mathbf Q_p[G]$ 为特征零中央幂等元，并写
$$
\phi_\pi(g)=\operatorname{Tr}(e_Ng\mid\pi)\in\mathbf Z_p.
$$
完整 character 公式为
$$
e_\pi e_N
=\frac{\dim\pi}{p(p^2-1)}
\sum_{g\in G}\phi_\pi(g^{-1})g.
\tag{1195.8}
$$
故对所有球面型均有
$$
\boxed{\quad p\,e_\pi e_N\in\mathcal A.\quad}
\tag{1195.9}
$$
这里的整性逐个群元素系数成立。

定义每一对的和
$$
E_1=(e_{V_1}+e_{\mathbf1})e_N,
\qquad
E_r=(e_{V_r}+e_{P_{r-1}})e_N\quad(r>1\text{ 奇}).
\tag{1195.10}
$$
对 $r>1$，(1195.7) 用在 $e_Nge_N$ 上给
$\phi_{V_r}(g)\equiv\phi_{P_{r-1}}(g)\pmod p$；
所以 (1195.8) 中相加的分子
$$
(p-1)\phi_{V_r}(g^{-1})+(p+1)\phi_{P_{r-1}}(g^{-1})
$$
被 $p$ 整除。对 $r=1$，相同论证给
$1+(p-1)\phi_{V_1}(g^{-1})\equiv0$。
因而全部 $E_r$ 都属于 $\mathcal A$。
它们是相互正交的真正幂等元。

若 $p\equiv1\pmod4$，另置
$$
E_\eta=e_{S_\eta}e_N.
$$
因为 $\dim S_\eta=p$，(1195.8) 已直接给 $E_\eta\in\mathcal A$。
§2 的穷尽表遂给
$$
e_N=\sum_{r\in\mathcal R}E_r
\quad\text{或}\quad
e_N=\sum_{r\in\mathcal R}E_r+E_\eta,
\tag{1195.11}
$$
分别对应两种 $p\bmod4$。

## 5. 充分性：整个整角没有额外高阶同余

固定一对，按 $(V_r,P_{r-1})$ 排坐标；$r=1$ 时第二项改为 $\mathbf1$。
令
$$
U_r=p\,e_{V_r}e_N.
$$
它在这一对的坐标是 $(p,0)$，$E_r$ 的坐标是 $(1,1)$，其余坐标均为零。
于是任意满足 $x\equiv y\pmod p$ 的一对都由实际整元素
$$
yE_r+\frac{x-y}{p}U_r
\tag{1195.12}
$$
实现。额外的一元坐标由 $E_\eta$ 任意实现。
结合必要性 (1195.7)，这证明 (1195.2) 的等号，而不只是一个有限指数包含。

在每一对中进一步有
$$
\boxed{\quad
E_r\mathcal A\simeq\mathbf Z_p[U]/(U^2-pU),
\qquad E_r\overline{\mathcal A}\simeq\mathbf F_p[U]/(U^2).
\quad}
\tag{1195.13}
$$
它的两个泛纤维投影 $U/p$ 与 $1-U/p$ 均不属于这个完整有限角，
因为 $(1,0),(0,1)$ 不满足 (1195.7)。
但这不排除某个特定几何表示上的投影更整；§6 给出准确判据。
本篇也未把有限 $S_\eta$ 角分成两种不同的 Weil–Deligne 单值算子类型。

## 6. 任意实际格的准确拼接模

设 $\Lambda$ 是 $E_r\mathcal A$ 的有限自由 $\mathbf Z_p$-模，
写 $U=U_r|_\Lambda$，于是 $U^2=pU$。
在泛纤维中置
$$
q=U/p,\quad V_c=q(\Lambda\otimes\mathbf Q_p),\quad
V_b=(1-q)(\Lambda\otimes\mathbf Q_p),
$$
$$
\Lambda_c=\Lambda\cap V_c,\qquad
\Lambda_b=\Lambda\cap V_b.
\tag{1195.14}
$$
这两个纯型格都是饱和子格，且
$$
\boxed{\quad p\Lambda\subset\Lambda_c\oplus\Lambda_b\subset\Lambda.\quad}
\tag{1195.15}
$$
证明直接由
$p\lambda=U\lambda+(p-U)\lambda$，其中两项分别属于两个纯型格。

不仅如此，投影、乘 $p$ 与模 $p$ 依次给出准确同构
$$
\begin{aligned}
F_\Lambda
&:=\Lambda/(\Lambda_c\oplus\Lambda_b)\\
&\simeq q\Lambda/\Lambda_c
\simeq U\Lambda/p\Lambda_c
\simeq\operatorname{im}(\overline U:\Lambda/p\Lambda\to\Lambda/p\Lambda).
\end{aligned}
\tag{1195.16}
$$
第一箭头的核恰为两个纯型格之和；第二个箭头是可逆的标量乘法。
最后一个箭头使用准确交集
$$
U\Lambda\cap p\Lambda=p\Lambda_c.
$$
一边由 $U\Lambda\subset V_c$ 给出，另一边由
$U\Lambda_c=p\Lambda_c$ 给出。
因此
$$
\boxed{\quad
[\Lambda:\Lambda_c\oplus\Lambda_b]
=p^{\operatorname{rank}_{\mathbf F_p}\overline U},
\qquad
q\Lambda\subset\Lambda\Longleftrightarrow\overline U=0.
\quad}
\tag{1195.17}
$$
特别损失指数由一个真实的模 $p$ 算子准确测出。
$\overline U^2=0$，故该秩同时计数大小二的 Jordan 块，
并至多为 $\min(\dim V_c,\dim V_b)$。
这个上界也可由两个对称的 Goursat 投影直接看出。

普遍界不能删去这个 $p$：取 $\Lambda=\mathcal O_p$ 自身，
其纯型子格是 $p\mathbf Z_p\oplus p\mathbf Z_p$，
拼接商为 $\mathbf F_p$，$\overline U$ 的秩正为一。
这是完整有限角内的精确例子，不是对原几何格发生损失的先验断言。

## 7. 原曲线上的用法及保留边界

回到本题全部 $p>37,\ p\equiv5\pmod6$。
从同一个 full-$p$ 模型到 $N$ 商的 pull–push 只除以 $|N|$；
原六标记平均及 $\kappa_4$ 下降与该 level 作用交换。
因此 (1195.10)–(1195.11) 的整角元素由原几何对应实现，
作用于实际 Tate 格、Néron Lie/余切格及它们保留的原子格。
这使用 [R1030 §§1、3、5](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md)
的同一个全配对分支实现；双中心行的有限谱与图角色保持
[R1038 §§2–3](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md) 的范围。

原球面旧部因 $S_2(H_6)=0$ 不出现，所以 $E_1$ 在原 holomorphic 空间上确为已登记的单独最低尖点型。这不使其他 $P_{r-1}$ 自动消失。
当 $p\equiv5\pmod{12}$ 时，额外 $E_\eta$ 必须保留；它可同时包含二次 PS 与二次 Steinberg 的有限固定方向，不能用有限角区分其单值算子。

对每个实际 $E_r$-格，先把 $U_r=p e_{V_r}e_N$ 作为完整整对应计算，再读其模 $p$ 作用，(1195.17) 才判断单独尖点投影是否保该格。
在 [R1191](R1191-original-half-rank-factor-all-primitive-inertia-slots.md) 的指定半秩 $C$ 中，各 primitive 槽的整分裂有该篇独立的剩余惯性证明；本篇没有用全 $J$ 的二元角推翻它。
反之，$C$ 上的整分裂也不使全 $J$ 的 $\overline U_r$ 自动为零。

[R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md) 的最高型 normal 计算使用真正整的 $E_m$；本篇说明它为什么须先保相邻主系列，并给进一步拆分的准确一个 $p$ 判据。
这与 [R1190](R1190-original-one-p-Neron-Lie-lattice-bound.md) 的实际子簇 Lie 格界是不同来源，不能把两个界未经比较就相加或相互替代。
指定原 $\beta$ 的高型 log、MW 楔及候选盘排除继续开放。

## 8. 来源与验证

- Pietro Mercuri、René Schoof，*Modular forms invariant under non-split Cartan subgroups*，Math. Comp. 89 (2020), 1969–1991，DOI 10.1090/mcom/3503；[作者正式 offprint](https://reneschoof.github.io/mcom3503.pdf)，§2、Proposition 2.1、§3.2。root 亲读完整四类、正规化子判据和二次退化行。
- R1029、R1030、R1038：原 finite-type 参数、实际几何角及两种约化行，逐项按原范围消费。
- R1193 §2：同一 Brauer 半单化及唯一 N 可见因子；本文扩至全部奇参数，并证明整个整角的充分性及实际格的准确拼接模。

全部为纸面论证；未运行数学程序、未新增素数窗口。


root 完成四类有限表示和两个约化行的核读；o2_high_coefficient 独立纸核整角充分性、Goursat 交集和准确指数公式，均与本文相合。没有把这些核对设为新的授权或停工条件。

# 最小正秩的有界模压缩与逐对共同真空禁阻

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的必要条件。** 本稿使用真正的有限秩正湮灭者，
把最小一般秩与最小正秩相等接到一个准确的有界模压缩公式。
其共同域结论比“全部分母的乘积没有真空原像”更强：
在最小秩至少二的见证中，任意两行都不能有同时正则化它们、
且仍有真空原像的有界交换子。
若这两行各自有广义预解，则两个交叉最小域条件都失败，
两行的实际定义域也不能互相包含。
不要求其余行存在任何预解数据。
后半部进一步给出任意源关系的系数理想湮灭，以及原正循环零商上的
有界低放大因式化：仅这两行的预解数据已足使每个单独分母在该商上作用为零。

这给出真实见证必须满足的共同域限制；
没有证明这样的限制不可能发生，也没有把代数模的稠密闭包当作代数模本身。

## 1. 固定对象与所用最小秩

记
$$
\mathfrak C=A',\qquad
B(u,v)=\langle u,Cv\rangle.
$$
内积对第一变量线性。原模型中 $\mathfrak C$ 交换，
每个 $T\in\mathfrak C$ 都满足
$$
CT^*C=T,\qquad
B(Tu,v)=B(u,Tv).
\tag{1.1}
$$
后一个等式对任意 $u,v\in H$ 成立，因为此处 $T$ 有界。
以下转移算子时使用的是 (1.1)，不把一般无界最大商自动当作双线性对称算子。

固定实际慢算子 $S$。
沿用 [R228A §1](../results/R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md)
及 [逐分母附录 §1](../results/R244-appendix-minimal-rank-individual-denominators-and-positive-koszul-zero-quotient.md)
的最小秩等价。
为说明本稿到底使用何种最小性，简述其完整步骤。

若
$$
\psi(F)=\sum_{\nu=1}^k\langle Fv_\nu,w_\nu\rangle,\qquad
\psi(S\mathfrak C)=0,\qquad \psi(I)\ne0,
$$
令 $v=(v_\nu),w=(w_\nu)$，
$$
M=\overline{\mathfrak C^{(k)}v},\qquad
N=\overline{S^{(k)}M},\qquad Q=M\ominus N.
$$
因 $S\in\mathfrak C$ 且代数交换，$N\subset M$。
$w\perp N$ 及 $\langle v,w\rangle\ne0$ 给 $Q\ne0$。
若 $0\ne q\in Q$，则对所有 $F\in\mathfrak C$，
$$
\langle (SF)^{(k)}q,q\rangle=0.
$$
所以 $\sum_{\nu=1}^kq_\nu\otimes q_\nu$ 是秩至多 $k$ 的非零正见证。
正见证本来也是一般见证，故
$$
\boxed{
\min\operatorname{rank}(\text{一般分离泛函})
=\min\operatorname{rank}(\text{正分离泛函}).
}
\tag{1.2}
$$
原先只对 $\mathcal A$ 给出的条件，可由 R88 的有界强多项式逼近
及有限个向量泛函的强连续性传到 $\mathfrak C$。

现在取达到这个最小值的
$$
\rho=\sum_{i=1}^r f_i\otimes f_i,\qquad
\tau=\sum_i\|f_i\|^2>0,\qquad
\phi(F)=\sum_i\langle Ff_i,f_i\rangle,\qquad
\phi(S\mathfrak C)=0.
\tag{1.3}
$$
选用 $r$ 个线性无关的 $f_i$，于是 $\operatorname{rank}\rho=r$。
置
$$
x_i=Cf_i,\qquad E=\operatorname{span}_{\mathbb C}\{x_1,\ldots,x_r\}.
\tag{1.4}
$$

(1.2) 的准确含义是：
若找到另一个在 $\mathfrak C$ 上等于 $\phi$ 的表达式，
只需 $k<r$ 个一般向量配对项，就已构成矛盾。
新表达式无需在整个 $B(H)$ 上等于原正密度，也无需仍然为正。

## 2. 有界模压缩的准确公式

设一个索引组 $I\subset\{1,\ldots,r\}$ 有 $s$ 个元素，
且存在 $g_1,\ldots,g_k\in H$ 与
$T_{i\ell}\in\mathfrak C$，使
$$
x_i=\sum_{\ell=1}^kT_{i\ell}g_\ell
\qquad(i\in I).
\tag{2.1}
$$
则对全部 $F\in\mathfrak C$，
$$
\begin{aligned}
\sum_{i\in I}\langle Ff_i,f_i\rangle
&=\sum_{i\in I}B(Ff_i,x_i)\\
&=\sum_{i\in I}\sum_{\ell=1}^k
   B(Ff_i,T_{i\ell}g_\ell)\\
&=\sum_{\ell=1}^k
  B\left(F\sum_{i\in I}T_{i\ell}f_i,g_\ell\right).
\end{aligned}
\tag{2.2}
$$
第三行只把**有界** $T_{i\ell}$ 用 (1.1) 移到左边，
再用 $T_{i\ell}F=FT_{i\ell}$。
因此，令
$$
h_\ell=\sum_{i\in I}T_{i\ell}f_i,
$$
便有
$$
\boxed{
\sum_{i\in I}\langle Ff_i,f_i\rangle
=\sum_{\ell=1}^k\langle Fh_\ell,Cg_\ell\rangle.
}
\tag{2.3}
$$

若 $k<s$，在 (1.3) 中以右侧替换这 $s$ 项，
就把整个 $\phi$ 写成至多 $r-s+k<r$ 个一般向量配对项，
同时保留 $\phi(S\mathfrak C)=0$ 及 $\phi(I)=\tau>0$。
由 (1.2)，这不可能。

这里不要求这些 $g_\ell$ 是逆源，不要求任何无界乘积有定义，
也不要求其他 $r-s$ 行具有广义预解。
这是之后所有共同域结论使用的有限秩压缩机制。

## 3. 有限源空间与每个有限生成代数模的交维数

对任意 $g_1,\ldots,g_k\in H$，令
$$
\mathscr M(g_1,\ldots,g_k)
=\mathfrak Cg_1+\cdots+\mathfrak Cg_k
$$
为**代数**和，不取 Hilbert 闭包。
则
$$
\boxed{
\dim\bigl(E\cap\mathscr M(g_1,\ldots,g_k)\bigr)\le k.
}
\tag{3.1}
$$
$k\ge r$ 时显然，故只需 $k<r$。

若交空间维数至少 $k+1$，
用单射线性映射
$$
\Xi:\mathbb C^r\longrightarrow E,\qquad
\Xi(c)=\sum_i c_ix_i
$$
把该交空间拉回 $\mathbb C^r$。
在其原像内取 $k+1$ 个标准内积正交单位向量，
并把它们扩充为一个酉矩阵 $V$ 的行。
置
$$
x'_i=\sum_jV_{ij}x_j,\qquad
f'_i=Cx'_i=\sum_j\overline{V_{ij}}f_j.
$$
酉性准确给
$$
\sum_i f'_i\otimes f'_i=\rho.
$$
前 $k+1$ 个 $x'_i$ 都属于
$\mathscr M(g_1,\ldots,g_k)$，
于是 (2.3) 把这 $k+1$ 项合成至多 $k$ 项，和最小性矛盾。
这证明 (3.1)。

特别，对任意单个 $g\in H$，
$$
\boxed{\dim(E\cap\mathfrak Cg)\le1.}
\tag{3.2}
$$
这是源空间对实际有界交换子轨道的限制，
并非只对某一固定谱分解中的坐标轴成立。
任意酉重选正密度的 $r$ 个源坐标后，同一结论仍成立。

不能在 (3.1) 中加闭包。
例如 $1$ 对 $\mathfrak C$ 循环，所以
$\overline{\mathfrak C1}=H$；
把代数模换成该闭包会直接丢失有界系数因子分解的信息。

## 4. 有真空原像的单个正则子只容纳一个源方向

对任意 $y\in H$，仍以 $X_y$ 表示由原多项式真空核心闭包得到的
最小闭乘子，$X_y1=y$。
它完整交换 $\mathfrak C$：
$$
T\operatorname{Dom}X_y\subset\operatorname{Dom}X_y,\qquad
X_yT=TX_y\quad(T\in\mathfrak C)
\tag{4.1}
$$
于原域成立。这是 [R244 原最小图附录 §1](../results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)
用 R88 的有界强多项式逼近与图闭性证明的性质；
[广义预解附录 §§1–2](../results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)
保留同一原域并给出后文的有界 Bézout 恒等式。

设
$$
P\in\mathfrak C,\qquad Pg=1.
\tag{4.2}
$$
定义
$$
\mathscr D_P
=\{y\in H:PH\subset\operatorname{Dom}X_y\}.
$$
则有准确恒等式
$$
\boxed{\mathscr D_P=\mathfrak Cg.}
\tag{4.3}
$$

先证正向。若 $y\in\mathscr D_P$，
$X_yP$ 是全域闭算子：输入收敛经 $P$ 仍收敛，再用 $X_y$ 闭性即可。
闭图定理给 $T=X_yP$ 有界。
由 (4.1) 与 $P\in\mathfrak C$，$T$ 交换 $A$，所以 $T\in\mathfrak C$。
并且
$$
Tg=X_yPg=X_y1=y.
$$
故 $y\in\mathfrak Cg$。
此处也明确支付了 $X_yP$ 的有界性与 C 对称性。

反向若 $y=Tg$、$T\in\mathfrak C$，
则 $Py=TPg=T1$。
对任意多项式核心向量 $u=p(A)1$，
(4.1) 给
$$
Pu\in\operatorname{Dom}X_y,\qquad
X_yPu=Pp(A)y=Tp(A)1=Tu.
$$
对任意 $u\in H$ 取多项式核心 $u_n\to u$。
$Pu_n\to Pu$、$X_yPu_n=Tu_n\to Tu$，
由 $X_y$ 闭性得到
$$
Pu\in\operatorname{Dom}X_y,\qquad X_yPu=Tu.
$$
故 $y\in\mathscr D_P$，证明 (4.3)。

将 (3.2) 代入：
$$
\boxed{\dim(E\cap\mathscr D_P)\le1
\quad\text{对每个满足 }Pg=1\text{ 的 }P\in\mathfrak C.}
\tag{4.4}
$$
这是实际全域正则化条件的交维数限制；
未将指定有限输入属于某个域替换成 $PH$ 全部属于该域。

## 5. 任意两行的共同真空原像都被排除

设 $r\ge2$，固定任意不同的 $i,j$。
不可能同时有
$$
P\in\mathfrak C,\qquad
PH\subset\operatorname{Dom}M_i\cap\operatorname{Dom}M_j,\qquad
Pg=1,
\tag{5.1}
$$
其中 $M_\nu=X_{Cf_\nu}=X_{x_\nu}$。

这既可直接由 (4.4) 得到，也可不经过维数表述逐式核验。
由闭图定理与域交换，
$$
b_i=M_iP,\qquad b_j=M_jP
$$
都是 $\mathfrak C$ 中的全域有界算子。
故它们具有 (1.1) 的 C 对称性，且
$$
b_i g=x_i,\qquad b_j g=x_j.
$$
因此对全部 $F\in\mathfrak C$，
$$
\boxed{
\langle Ff_i,f_i\rangle+\langle Ff_j,f_j\rangle
=\left\langle F(b_if_i+b_jf_j),Cg\right\rangle.
}
\tag{5.2}
$$
把这两项合为一项后，整个 $\phi$ 至多有 $r-1$ 个一般配对项，
与 (1.2) 矛盾。

注意这里没有声称这两行自身湮灭 $S\mathfrak C$。
被保留的是**整个**原 $\phi$；
其余项完全照旧，故整泛函的湮灭与正的单位值仍然存在。
这正是最小性把全体共同域禁阻加强成逐对禁阻的原因。

## 6. 两个广义预解时的完整交叉域等价

只对所选两行 $\nu=i,j$ 假设有广义预解数据
$$
R_\nu=(M_\nu U_\nu+B_\nu)^{-1}\in\mathfrak C,\qquad
U_\nu\in\mathfrak C^\times,\quad B_\nu\in\mathfrak C.
\tag{6.1}
$$
其余行无需任何此类数据。
原最小域完整交换有界单位，故
$$
R_\nu\text{ 单射},\qquad
\operatorname{Ran}R_\nu=\operatorname{Dom}M_\nu,\qquad
D_\nu=M_\nu R_\nu\in\mathfrak C.
\tag{6.2}
$$
因为 $1\in\operatorname{Dom}M_\nu$，有准确源
$$
g_\nu=(M_\nu U_\nu+B_\nu)1
      =U_\nu x_\nu+B_\nu1,\qquad
R_\nu g_\nu=1.
\tag{6.3}
$$

以下三项严格等价：
$$
\boxed{
1\in\operatorname{Ran}(R_iR_j)
\ \Longleftrightarrow\
x_i\in\operatorname{Dom}M_j
\ \Longleftrightarrow\
x_j\in\operatorname{Dom}M_i.
}
\tag{6.4}
$$

先说明第一个与第二个的两个方向。
由于 $R_i$ 单射，
$$
1\in\operatorname{Ran}(R_iR_j)
\Longleftrightarrow
g_i\in\operatorname{Ran}R_j
=\operatorname{Dom}M_j.
\tag{6.5}
$$
正向确切地说：若 $R_iR_jh=1=R_ig_i$，单射性给 $R_jh=g_i$。
反向若 $g_i=R_jh$，则 $R_iR_jh=R_ig_i=1$。

由 (6.3)，$B_i1\in\operatorname{Dom}M_j$：
这是 $1$ 属于原域及 (4.1) 的结果。
此外 $U_i$ 和 $U_i^{-1}$ 都保持该域。
所以
$$
g_i\in\operatorname{Dom}M_j
\Longleftrightarrow
U_ix_i\in\operatorname{Dom}M_j
\Longleftrightarrow
x_i\in\operatorname{Dom}M_j.
\tag{6.6}
$$
这给第一项与第二项的完整等价。
交换 $i,j$ 并用 $R_iR_j=R_jR_i$，
得到第一项与第三项的完整等价。

另一方面，$P=R_iR_j$ 的全像确实同时属于两个最小域：
它既是 $R_i(R_jH)$，也是 $R_j(R_iH)$；
且
$$
M_iP=D_iR_j,\qquad M_jP=D_jR_i
$$
均有界。
若 (6.4) 中任一项成立，就满足 (5.1)，因而矛盾。
于是
$$
\boxed{
1\notin\operatorname{Ran}(R_iR_j),\qquad
Cf_i\notin\operatorname{Dom}M_j,\qquad
Cf_j\notin\operatorname{Dom}M_i.
}
\tag{6.7}
$$
这不是由某一个必要方向反推的结论；(6.5)--(6.6) 已证明全部方向。

固定两行而改变各自的有界单位、扰动或预解参数，
既有单位类定理给 $R'_\nu=R_\nu V_\nu$，
其中 $V_\nu\in\mathfrak C^\times$。
因此
$$
R'_iR'_jH=R_iR_jH.
$$
(6.7) 的真空失败与参数选择无关。
它也不声称单独的 $R_i$ 或 $R_j$ 没有真空原像；
(6.3) 正好给出了各自的原像。

## 7. 原最小域与分母主理想必须两两不可比较

在 §6 的两行预解前提下，还必有
$$
\boxed{
\operatorname{Dom}M_i\not\subseteq\operatorname{Dom}M_j,
\qquad
\operatorname{Dom}M_j\not\subseteq\operatorname{Dom}M_i.
}
\tag{7.1}
$$
例如，若 $\operatorname{Dom}M_j\subseteq\operatorname{Dom}M_i$，
取 $P=R_j$。
(6.2) 给 $PH\subset\operatorname{Dom}M_i\cap\operatorname{Dom}M_j$，
而 (6.3) 给 $Pg_j=1$。
这又满足 (5.1)，矛盾。另一个方向同理。

这里实际值域包含与代数分母因子化也准确等价：
$$
\boxed{
\operatorname{Ran}R_j\subseteq\operatorname{Ran}R_i
\Longleftrightarrow
R_j=R_iT\quad\text{某个 }T\in\mathfrak C.
}
\tag{7.2}
$$
一向显然。
反向若值域包含，$T=R_i^{-1}R_j$ 在全部 $H$ 上定义。
它是闭算子：$v_n\to v,Tv_n\to w$ 时
$R_iw=\lim R_iTv_n=\lim R_jv_n=R_jv$，
再用 $R_i$ 单射即可。
故 $T$ 有界。
由
$$
R_iTA=R_jA=AR_j=R_iAT
$$
及单射性，$TA=AT$，所以 $T\in\mathfrak C$。

因此 (7.1) 同时给出
$$
R_i\mathfrak C\not\subseteq R_j\mathfrak C,\qquad
R_j\mathfrak C\not\subseteq R_i\mathfrak C.
\tag{7.3}
$$
这是实际主理想，不是强闭包或范数闭包的比较。
特别，两个源乘子不能具有同一个实际定义域，
也不能来自一个已证明这些原域相互包含的预解族。

## 8. 有界系数近似与剩余范围

(3.1) 还排除一种有限预算的“近似共同源”：
固定 $g_1,\ldots,g_k$ 及系数算子范数界 $K<\infty$，
不能有一列含 $k+1$ 个正交系数方向的源框架，
被
$$
\sum_{\ell=1}^k T_{i\ell}^{(n)}g_\ell,\qquad
\|T_{i\ell}^{(n)}\|\le K
$$
同时范数逼近。
否则有限维系数框架取收敛子列，
$\mathfrak C$ 的有界算子球取 WOT 收敛子网；
其 WOT 极限仍属于 $\mathfrak C$。
对固定 $g_\ell$ 取向量弱极限，就得到 §2 中准确的少源因子分解，
矛盾。此处不允许 $g_\ell$ 随近似任意改变，也不提供与 $K$ 无关的正距离。

## 9. 任意有界源关系的各系数理想都被湮灭

设
$$
T_1,\ldots,T_r\in\mathfrak C,\qquad
\sum_{\nu=1}^rT_\nu x_\nu=0.
\tag{9.1}
$$
则对每个 $i$ 及全部 $F\in\mathfrak C$，
$$
\boxed{
\phi(T_iF)
=\sum_{j\ne i}
 \left\langle F(T_if_j-T_jf_i),f_j\right\rangle.
}
\tag{9.2}
$$
确切地，把左侧第 $i$ 项中的 $T_i$ 用有界 C 对称性移到
$x_i$ 上，再用 (9.1)：
$$
\begin{aligned}
B(FT_if_i,x_i)
 &=B(Ff_i,T_ix_i)\\
 &=-\sum_{j\ne i}B(Ff_i,T_jx_j)
 =-\sum_{j\ne i}B(FT_jf_i,x_j).
\end{aligned}
$$
与其他 $r-1$ 项相加就是 (9.2)。

如果存在 $F_0\in\mathfrak C$ 使 $\phi(T_iF_0)\ne0$，
定义
$$
\psi(F)=\phi(T_iF_0F).
$$
由 (9.2)，$\psi$ 至多有 $r-1$ 个一般向量配对项；
又因代数交换，
$$
\psi(SF)=\phi(ST_iF_0F)=0,\qquad
\psi(I)=\phi(T_iF_0)\ne0.
$$
这与 (1.2) 矛盾。
因此得到整个理想的结论
$$
\boxed{\phi(T_i\mathfrak C)=0\qquad(1\le i\le r).}
\tag{9.3}
$$
这里没有仅从单点 $\phi(T_i)=0$ 推出理想湮灭。

另一个直接的低秩公式适用于共同正则子。
若 $P\in\mathfrak C$ 全域正则化一个大小 $s\ge2$ 的索引组 $I$，
令 $b_i=M_iP$。
对所有 $F\in\mathfrak C$，
$$
\boxed{
\phi(PF)
=\left\langle F\sum_{i\in I}b_if_i,1\right\rangle
 +\sum_{j\notin I}\langle FPf_j,f_j\rangle.
}
\tag{9.4}
$$
第一项只需有界算子的双线性对称性。原域交换先给
$$
Px_i=M_iP1=b_i1.
$$
因此
$$
\begin{aligned}
B(PFf_i,x_i)
&=B(Ff_i,Px_i)\\
&=B(Ff_i,b_i1)
=B(Fb_if_i,1).
\end{aligned}
$$
所有跨配对移动的算子都是有界的 $P,b_i,F$。
因 $C1=1$，最后一项正是 (9.4) 中的内积。
整个右侧只有 $r-s+1<r$ 项。
和上一段一样，若 $\phi(PF_0)\ne0$，以 $\phi(PF_0\,\cdot)$
构造较低秩分离泛函便得矛盾。因此
$$
\boxed{\phi(P\mathfrak C)=0
\quad\text{只要 }P\text{ 全域正则化至少两行}.}
\tag{9.5}
$$
这一段没有假设 $1\in\operatorname{Ran}P$。

## 10. 原正循环零商上的低放大因式化

本节另给完整的有界链论证，将 §9 的特定结构提升为商算子零。
不能单凭任意一个泛函理想湮灭就作这种提升。

### 10.1 原正源与低放大的稠密性

先核 $x=(Cf_i)$ 仍表示同一正泛函。
由 $FC=CF^*$，
$$
\langle FCf_i,Cf_i\rangle
=\langle CF^*f_i,Cf_i\rangle
=\langle f_i,F^*f_i\rangle
=\langle Ff_i,f_i\rangle.
$$
所以
$$
\phi(F)=\langle F^{(r)}x,x\rangle,\qquad
\|x\|^2=\tau.
\tag{10.1}
$$
定义原空间中的实际闭旗
$$
M=\overline{\mathfrak C^{(r)}x},\qquad
N=\overline{S^{(r)}M},\qquad Q=M\ominus N.
\tag{10.2}
$$
因 $\phi(SF)=0$，
$x$ 与所有 $S^{(r)}F^{(r)}x$ 正交；
由轨道在 $M$ 中稠密及 $S$ 有界，得到 $x\perp N$。
因而
$$
x\in Q,\qquad Q\ne0.
\tag{10.3}
$$
商表示为
$$
\pi(F)=P_QF^{(r)}|_Q.
$$
闭旗不变性使它是有界代数表示，
$$
\pi(S)=0,\qquad
\phi(F)=\langle\pi(F)x,x\rangle.
\tag{10.4}
$$

若 $k<r$ 且 $Y\subset H^{(k)}$ 是任意闭的对角
$\mathfrak C$ 不变子空间，则
$$
\boxed{\overline{S^{(k)}Y}=Y.}
\tag{10.5}
$$
否则取
$0\ne v\in Y\ominus\overline{S^{(k)}Y}$。
对所有 $F\in\mathfrak C$，
$F^{(k)}v\in Y$，故
$$
\langle (SF)^{(k)}v,v\rangle=0.
$$
于是 $\sum_{\ell=1}^kv_\ell\otimes v_\ell$ 是秩至多 $k<r$
的非零正见证，与最小性矛盾。
(10.5) 是从最小秩得到的真实低放大结论，
不是把全 $H$ 的稠密像未经证明传到不变子空间。

### 10.2 有界矩阵因式化引理

设 $P\in\mathfrak C$，存在 $k<r$、
$y\in H^{(k)}$ 及全域有界矩阵
$$
J:H^{(k)}\longrightarrow H^{(r)}
$$
其每个矩阵项属于 $\mathfrak C$，且
$$
Jy=P^{(r)}x.
\tag{10.6}
$$
则
$$
\boxed{P^{(r)}M\subset N,\qquad \pi(P)=0.}
\tag{10.7}
$$

令 $Y=\overline{\mathfrak C^{(k)}y}$。
矩阵项交换全部 $F$，所以在每个轨道向量上，
$$
JF^{(k)}y=P^{(r)}F^{(r)}x\in M.
$$
由 $J$ 有界、$M$ 闭，先得到 $JY\subset M$。
再由 $JS^{(k)}=S^{(r)}J$，
$$
JS^{(k)}Y\subset S^{(r)}M\subset N.
$$
由 (10.5)，$S^{(k)}Y$ 在 $Y$ 中稠密。
固定 $u\in Y$，取 $S^{(k)}u_n\to u$，则
$JS^{(k)}u_n\to Ju$；
因每项在闭空间 $N$ 中，故 $Ju\in N$。
这证明 $JY\subset N$。
最后，(10.6) 的轨道恒等式及 $P$ 有界给
$$
P^{(r)}M
\subset\overline{JY}\subset N,
$$
从而得到 (10.7)。
论证不需要从 $P^{(r)}M$ 有界反解回 $Y$，也不假设 $JY$ 自身闭。

### 10.3 源关系的删除与插入链

在 (9.1) 的源关系下，令
$E_i:H^{(r)}\to H^{(r-1)}$ 删除第 $i$ 坐标，
并定义有界矩阵
$$
(J_i u)_i=-\sum_{j\ne i}T_ju_j,\qquad
(J_i u)_j=T_i u_j\quad(j\ne i).
\tag{10.8}
$$
原源关系及对角轨道闭包说明
$$
\sum_jT_jm_j=0\qquad(m\in M).
$$
因此
$$
\boxed{J_iE_i m=T_i^{(r)}m\qquad(m\in M).}
\tag{10.9}
$$
此式只在原循环 $M$ 上主张，不在整个 $H^{(r)}$ 上主张。

取 $y=E_ix$，有 $J_iy=T_i^{(r)}x$；
由 §10.2 的 $k=r-1$ 情形，
$$
\boxed{\pi(T_i)=0\qquad(1\le i\le r).}
\tag{10.10}
$$
所以 (9.3) 此时确有更强的算子零解释；
其依据是 (10.8)--(10.9) 的真实有界链。

### 10.4 至少两行的共同正则子

设 $P$ 全域正则化索引组 $I$，$|I|=s\ge2$，
$b_i=M_iP\in\mathfrak C$。
原域交换及 $M_i1=x_i$ 给
$$
Px_i=M_iP1=b_i1\qquad(i\in I).
\tag{10.11}
$$
令
$$
y=\bigl(1,(Px_j)_{j\notin I}\bigr)\in H^{(r-s+1)}
$$
并定义有界矩阵 $J$：
第一项输入记为 $u_0$，其余按 $j\notin I$ 标号，
$$
(Ju)_i=b_iu_0\quad(i\in I),\qquad
(Ju)_j=u_j\quad(j\notin I).
\tag{10.12}
$$
(10.11) 精确给 $Jy=P^{(r)}x$。
因为 $r-s+1<r$，§10.2 适用，得到
$$
\boxed{\pi(P)=0.}
\tag{10.13}
$$
这支付了从共同正则化到原正循环零商上算子零的全部闭包顺序。

## 11. 仅任意两行有广义预解就足以逐分母为零

仍只假设 §6 所选两行 $i,j$ 有广义预解。
取
$$
P=R_iR_j.
$$
它全域正则化这两行，所以 §10.4 给
$$
\pi(R_iR_j)=0.
\tag{11.1}
$$

原真空关系还给
$$
R_ix_i=R_iM_i1=M_iR_i1=D_i1,\qquad
R_jx_j=D_j1.
\tag{11.2}
$$
这里 $1$ 属于原最小域，$R_i$ 保持该域，故每个交换都已付域。
因此有只涉及两坐标的实际有界源关系
$$
(R_iD_j)x_i-(R_jD_i)x_j=0.
\tag{11.3}
$$
§10.3 对其两个非零系数给
$$
\pi(R_iD_j)=0,\qquad
\pi(R_jD_i)=0.
\tag{11.4}
$$

最后只用两个有界 Bézout 恒等式
$$
U_iD_i+B_iR_i=I,\qquad
U_jD_j+B_jR_j=I.
$$
于是
$$
\begin{aligned}
\pi(R_i)
 &=\pi(U_j)\pi(R_iD_j)+\pi(B_j)\pi(R_iR_j)=0,\\
\pi(R_j)
 &=\pi(U_i)\pi(R_jD_i)+\pi(B_i)\pi(R_iR_j)=0.
\end{aligned}
$$
得到
$$
\boxed{
\pi(R_i)=\pi(R_j)=0,\qquad
\pi(D_i)^{-1}=\pi(U_i),\quad
\pi(D_j)^{-1}=\pi(U_j).
}
\tag{11.5}
$$
单位性使用商代数仍交换；有界 Bézout 给双侧逆。

由 (10.4)，自然也有
$$
\boxed{
\phi(R_i\mathfrak C)=\phi(R_j\mathfrak C)=0.
}
\tag{11.6}
$$
若只需要泛函结论，可独立地用 (9.5) 排
$R_iR_j\mathfrak C$，再用 (9.3) 排 (11.3) 的两个系数理想，
最后同样代入 Bézout。
该独立推导也说明，不能把“各 $\phi(R_i)=0$”误当本节的证明。

$Q$ 始终是 (10.2) 中由原正源 $x$ 生成的实际 $r$ 重放大零子商。
(11.5) 未被外推到所有共同交域商、最大比例图或任意其他旗子商。
若所有行都有广义预解且 $r\ge2$，任取配对可知每个 $R_i$
都在这个同一个 $Q$ 上为零；
若只知两行，本节对这两行已经完整成立。

## 12. 剩余共同域边界

本稿没有从正常性推出 (5.1)，也没有给任何两行补上缺失的交叉域。
不同源最小闭乘子的实际域本来就可能不可比较；
上述禁阻目前是最小真见证的必要条件，不是排除它的充分证明。
原正循环零商上每个分母的算子零及分子的单位性，
由 §§10--11 的明确低放大链支付；
它们仍不使原 $Cf_i$ 属于另一个最小乘子的域，
也不使无界逆自动下降到商。
普通 Hilbert ISP 的完成标准尚未达到。

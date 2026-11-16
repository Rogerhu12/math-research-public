# R842 续注：全部非固定负水平残数的实际纤维商与二次 trace 公式

日期：2026-11-16。**状态：以下原纤维商、全部分支 trace、显式二次系数及完整未加前缀的来源满射已证明；指定 $[b_0]$ 在 $\mathscr W_T$ 或更小三长核上的值仍未判定。**

接
[真实负水平的一层行](2026-11-16-r842-negative-horizontal-finite-euler-rows.md)。
本注将该光滑局部计算推进到原 $r=2$ 的全部非固定负水平点，
包括奇点及其 conductor。所用目标是原底纤维在曲线上的实际局部交概形，
不把正规化各支的值作为自由来源。

## 1. 原来源、有限纤维与 Euler 算子

沿 R797/R842 保持
$$
R=q\,t^rG,\qquad q=Y\widetilde q,\qquad
G\in\mathcal H_3,\qquad
F(t,0)=\lambda d^cH(t),\quad \deg H\le2.
\tag{1}
$$
$F$ primitive、几何整；$q$ 仅在原 $d=0$ 有分母。
这里几何整沿 R495 §1(1) 后的原论证：$k$ 完美，$F$ 不可约，
且原 $P=(0,1)$ 是 $k$-有理光滑点。若几何共轭分量多于一个，
Galois 传递性与 $P$ 有理迫它们都经过 $P$，与光滑性冲突。
所以本注没有另加几何整假设。
取 $Q=(t_Q,0)\in C$ 不在任何固定底纤维上。
在 $k_Q$ 上置
$$
T_0=t-t_Q,\qquad x=Y,\qquad
n=\operatorname{ord}_{t_Q}F(t,0)\in\{1,2\},
$$
$$
\ell_Q=\operatorname{ord}_x F(t_Q,x),\qquad
1\le\ell_Q\le b=\deg_YF<p.
\tag{2}
$$
最后的多项式不恒零，因为 $F$ 没有垂直因子。
定义原曲线上的实际 Cartier 交概形
$$
\boxed{
D_Q=V(T_0)\subset C\text{ 的 }Q\text{ 分量},
\qquad
\mathcal O_{D_Q}\simeq k_Q[x]/(x^{\ell_Q}).
}
\tag{3}
$$
它不是两个正规化分支的任意直和。
若 $t_Q$ 非基域有理，在基域取其可分最小多项式的相应局部纤维分量；
扩到 $k_Q$ 后该多项式与 $T_0$ 只差单位。
因此 (3) 及其后按 Galois 合并的除子仍是原曲线上的 Cartier 交。

原 $e=YF_Y$ 在 $T_0=0$ 上等于
$x\,\partial_x F(t_Q,x)$。
若 $F(t_Q,x)=x^{\ell_Q}u(x)$，$u(0)\ne0$，则
$$
x\,\partial_x F(t_Q,x)
=\left(\ell_Q+xu'/u\right)F(t_Q,x).
$$
所以在原完成局部环中 $e\in(F,T_0)$，从而有真实概形包含
$$
\boxed{D_Q\subset Z=(e|_C).}
\tag{4}
$$
原相对 Euler 保 $(F,T_0)$，并在 (3) 上诱导
$$
\boxed{\mathcal E_{D_Q}=D_x=x\partial_x.}
\tag{5}
$$
因此对全部原 $G$，包括 $C$ 在 $Q$ 奇异时，
$$
\boxed{
(D_3(G|_C))|_{D_Q}=D_x(G|_{D_Q}),\qquad
(\mathcal E^2G)|_{D_Q}=D_x^2(G|_{D_Q}).
}
\tag{6}
$$
其正特征值 $1,\ldots,\ell_Q-1$ 均为单位。
这不声称 $D_3$ 在整个 $Z$ 上只依赖一层值；
(6) 只用于显示的原纤维子概形。

## 2. 全部 conductor 分支的 trace 读取

保持原
$$
W=t^{r+1-s}(1-t)^{3s},\qquad c_s=\frac{3(-1)^s}{17},
$$
$$
\mathcal D_R=c_s(\mathcal ER)|_C
\left[
-d\left(\frac{WF_t}{e}\right)
+\frac{W'F_t+WF_{tt}}e\,dt
\right].
\tag{7}
$$
$W$ 在 $Q$ 为单位。
以下残数一律先对该点的全部正规化分支求和，再取原剩余域迹。

在 $k_Q[[x,T_0]]$ 中对 $F$ 作真正 Weierstrass 分解：
$$
F=u(T_0,x)\,\mathcal F(T_0,x),\quad
u(0,0)\ne0,\qquad
\mathcal F=T_0^n+a_1(x)T_0^{n-1}+\cdots+a_n(x).
\tag{8}
$$
$a_i(0)=0$。因 $n\le2<p$，相应的非零分支扩张都是驯分歧；
$\mathcal F$ 在 $k_Q((x))$ 上可分。
用其全部根 $T_i(x)$ 表示分支，重复数包含驯分歧共轭。
若某支的正规参数为 $v$，写
$$
n_i=\operatorname{ord}_v x,\qquad
m_i=\operatorname{ord}_v T_0.
$$
其中 $n_i\le2$、$m_i\le b<p$。
因此每个 $T_i'(x)$ 的首项确实非零，
$$
\operatorname{ord}_xT_i'=\frac{m_i}{n_i}-1.
\tag{9}
$$
这里没有在特征 $p$ 中删除可能的首导数失效；
原两个显示次数界已经将它排除。

定义真实 trace Laurent 级数
$$
\boxed{
S_Q(x)=\operatorname{Tr}_{\,k_Q((x))[T_0]/(\mathcal F)\,/\,k_Q((x))}
\left(\frac1{T_0'(x)}\right)
=\sum_i\frac1{T_i'(x)}.
}
\tag{10}
$$
当 $\mathcal F$ 分裂时取全部因子的 trace。
由原常数项的 Norm，
$$
\ell_Q=\operatorname{ord}_x a_n(x)
=\sum_i\operatorname{ord}_xT_i,
$$
所以 (9) 给
$$
\boxed{S_Q(x)\in x^{1-\ell_Q}k_Q[[x]].}
\tag{11}
$$

**定理。** 对 (1) 中的同一个原来源，
$$
\boxed{
\sum_{\widetilde Q\mapsto Q}
\operatorname{Tr}_{k_{\widetilde Q}/k_Q}
\operatorname{Res}_{\widetilde Q}\mathcal D_R
=
-c_s t_Q^rW(t_Q)\,
\operatorname{CT}_x
\left[
S_Q(x)(D_x+1)^2
\bigl(\widetilde q(t_Q,x)G(t_Q,x)\bigr)
\right].
}
\tag{12}
$$
右侧只读模 $x^{\ell_Q}$ 的原纤维值；
它不读取任选的正规化高 jet，也没有换掉 $q$。

证明先支付两种允许的局部操作。

第一，若 $R$ 改变 $xFL$，$L$ 为原完成局部环的正则元素，
则 $X=(\mathcal E(xFL))|_C=xeL$。
将此直接代入 (7)，得
$$
\mathcal D_{xFL}/c_s
=-xL\,d(WF_t)+xLWF_t\,de/e
+xL(W'F_t+WF_{tt})dt.
\tag{13}
$$
在每个正规化分支上前后两项正则；
$de/e$ 至多简单极，而 $x$ 在每支消失，
故中间项也正则。其全部残数为零。
因此可对 $t^r\widetilde qG$ 作原 Weierstrass 除法而不改边界：
$$
t^r\widetilde qG
=\sum_{j=0}^{n-1}A_j(x)T_0^j+FL.
\tag{14}
$$
并始终取 $R=x\sum_jA_jT_0^j$。

第二，(7) 的后项为
$$
\frac{\mathcal ER}{Y}(W'F_t+WF_{tt})\,\frac{dt}{F_Y}.
\tag{15}
$$
其系数在原平面完整交局部环正则，
$dt/F_Y$ 是其对偶化生成元。
所以 (15) 的全部正规化分支残数和为零。
这是 Gorenstein 留数事实，不是把奇点各支分别赋零。

令 $B_j=(D_x+1)A_j$。
在第 $i$ 个分支，(14) 的实际 Euler 输出是
$x\sum_jB_jT_i^j$，且隐函数式给
$$
WF_t/e=-W(t_Q+T_i)/(xT_i').
$$
将 (7) 第一项分部一次，全部分支 trace 化为
$$
-c_s\operatorname{CT}_x
\sum_{j=0}^{n-1}
(D_x+1)^2A_j\,
\operatorname{Tr}\frac{W(t_Q+T_i)T_i^j}{T_i'}.
\tag{16}
$$
分部时另出现的
$jB_j\operatorname{Tr}(WT_i^{j-1})dx$
为正则微分，残数为零。

若 $j\ge1$，则由 (9)
$$
\operatorname{ord}_x(T_i^j/T_i')
=1+(j-1)m_i/n_i\ge1,
$$
故 (16) 中这些项完全不贡献。
在 $j=0$ 项，$W(t_Q+T_i)-W(t_Q)$ 含 $T_i$，
同样不贡献。因此只剩
$-c_sW(t_Q)\operatorname{CT}(S_Q(D_x+1)^2A_0)$。

最后在 (14) 令 $T_0=0$：
$$
A_0(x)\equiv
t_Q^r\widetilde q(t_Q,x)G(t_Q,x)
\pmod{x^{\ell_Q}}.
$$
$D_x+1$ 保这个理想，结合 (11) 即得 (12)。
全部 trace/残数转换均在同一个实际局部代数中完成，
所以 conductor 条件没有被替换成自由分支条件。证毕。

## 3. 二次分支的完全显式系数

若 $n=1$，写 $\mathcal F=T_0+a_1(x)$，
则准确有
$$
\boxed{S_Q=-1/a_1'(x).}
\tag{17}
$$
$\operatorname{ord}a_1=\ell_Q<p$，
所以其首项是一个非零的 $x^{1-\ell_Q}$ 系数。
当 $\widetilde q(Q)$ 为单位时，(12) 是原纤维商上的非零行；
它的最高 jet 系数为单位，与前注的光滑公式完全一致。

若 $n=2$，写
$$
\mathcal F=T_0^2+a(x)T_0+b(x).
$$
对每个根，
$$
T_i'=-\frac{a'T_i+b'}{2T_i+a}.
$$
求两根的真实 trace，得到
$$
\boxed{
S_Q=
\frac{a'(a^2-4b)}
{(b')^2-aa'b'+b(a')^2}.
}
\tag{18}
$$
分母是 $a'T_0+b'$ 的 Norm，因各实际 $T_i'$ 非零而不恒为零；
允许它在 $x=0$ 消失。
式 (11) 保证该商的所需 Laurent 部分仍只有有限长度。
这同时处理分裂节点、不可分裂节点、尖点、相切多支和光滑水平切点。

当 $\widetilde q(Q)\ne0$，
乘 $\widetilde q(t_Q,x)$ 及 $(D_x+1)^2$ 在
$k_Q[x]/x^{\ell_Q}$ 上都是单位算子。
因此 (12) 在整个原纤维商上恒零，当且仅当
$$
\boxed{S_Q\in xk_Q[[x]].}
\tag{19}
$$
这是可直接由同一个 $F$ 判定的局部条件，
不是由 $\dim Z_-\le2$ 得到的结论。
例如：

- 光滑二重水平切点给 $b'(0)\ne0$，所以 (18) 在 $(x)$ 中，
  与前注的整项消去一致。
- 节点首部 $T_0^2+\alpha xT_0+\beta x^2$，其中
  $\beta\ne0$、$\alpha^2-4\beta\ne0$，给
  $S_Q(0)=-\alpha/\beta$，恢复此前
  $c_s t_Q^rW(t_Q)\alpha/\beta$ 的总残数。
- 若实际二次 Weierstrass 系数满足 $a'=0$，
  则 (18) 恒零；没有据此预设原候选具备该对称性。

## 4. 该有限行确有原全来源，而受限高前缀仍须另判

令 $D_-$ 是全部非固定负水平点的 (3) 之和，
并含原剩余域次数。
由于 $\deg H\le2$，而每个不同底纤维与 $C$ 的总交数至多 $b$，
$$
\deg D_-\le2b.
\tag{20}
$$
原 $r=2$ 曲面几何给
$\kappa\ge6b-9$、$\chi\ge2b+3$，$b\ge3$。
前者准确见 R815 §7(33a)–(33b) 后的结论；后者见
R819 §4(15) 取 $m=3$，亦明列于其 §5.1(17)。因此
故 $\deg D_-<2\kappa+\chi$。
在同一个原 Gorenstein 曲线上，
$$
H^1(C,N^3(-D_-))^\vee
=H^0(C,\omega_CN^{-3}(D_-))=0,
$$
因为其次数为 $\deg D_--2\kappa-\chi<0$。
再用 R495 的原 $\mathcal H_3\to H^0(C,N^3)$ 满射，得到
$$
\boxed{
\mathcal H_3\twoheadrightarrow
H^0(D_-,N^3|_{D_-}).
}
\tag{21}
$$
这里 $D_Q$ 是原 Cartier 局部交，不是正规化任意点值；
所以 (21) 付清全部奇点下降。
若某个局部行 (12) 非零且其余点先指定为零，
(21) 确实提供同预算的全来源实现。
这只说明负水平分量在未加前缀的原来源上是否为零，
不排其它边界对它的补偿。

对高前缀
$\mathscr V_T=H^0(C,N^3(-TP))$，
相同证明仅在额外门
$$
T+\deg D_-<2\kappa+\chi
\tag{22}
$$
成立时给纤维评价满射。
当前一般 $T>2\kappa$ 窗口不能自动使用 (22)。
即使 (22) 成立，仍没有证明兼容核
$$
\mathscr W_T
=\{V_0\in\mathscr V_T:D_3V_0\in\iota_T\mathscr V_T\}
$$
对这些值满射。其唯一 $V_1$ 必须同时满足
(6) 的局部关系和原全部高前缀。
真实第二值、同一个 $cF^3$ 尾、第四短行及整个 $\mathcal W_D$
余列继续原样保留。

本注把实际负水平边界从 $2Z$／正规化高 jet 压到总长度至多 $2b$
的原底纤维商，并给出 (18) 的完全系数式。
剩余全局类仍是 R842 的同一个 $[b_0]$，
物理 $T=s-r-13$、所有原十三行 carry 和同一修正未变。

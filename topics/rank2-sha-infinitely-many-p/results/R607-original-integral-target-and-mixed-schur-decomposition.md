# R607 — 原强化矩阵的无扭整环、完整共振像与九格整 Schur 分块

日期：2026-11-14。**状态：已证明。**

R596 的统一行缩放并非只能逐行使用：它来自同一原有限目标中的一个显示整环。本篇给这个环的三个实际生成元、全部关系和唯一整基；原九来源的完整模 $p$ 像于是可以按真正的环乘法计算。

这个目标把 R589 的全部首极部和 R592 的五个 $\epsilon$ 行放回同一个实际低权环商。七个 Euler 来源中的两个指定 forcing 是显示共振多项式的常数项。最后用 R604 的原单位方阵，对全九格作整的 Schur 分块，完整保留真前缀、首极部及低权观察。目标环的生成元不被添加为新的全局来源。

## 1. 同一物理目标中的加强整基

取
$$
p=6s-1>71,\qquad b=17,\qquad
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p),
\quad w=z^6.
\tag{1}
$$
在 $\mathcal A_p[1/p]$ 中，$w^{ps}=0$，且原物理基为 $1,w,\ldots,w^{ps-1}$。对 $0\le n<ps$ 写 $n=Qs+r$，$0\le r<s$。R596 的真实缩放指数准确化为
$$
\boxed{
t_n=Q+\mathbf1_{Q+6r\ge p}
=\left\lfloor\frac{6n}{p}\right\rfloor .
}
\tag{2}
$$
因为 $6n=Qp+Q+6r$，而 $0\le Q+6r<2p$。

在这个**同一物理目标**中定义
$$
e_n=p^{-t_n}w^n,\qquad
\boxed{\mathcal C_p=\bigoplus_{0\le n<ps}\mathcal O e_n.}
\tag{3}
$$
若 $n+m<ps$，则实际乘法为
$$
\boxed{
e_ne_m
=p^{t_{n+m}-t_n-t_m}e_{n+m},
\qquad t_{n+m}-t_n-t_m\in\{0,1\}.
}
\tag{4}
$$
若 $n+m\ge ps$，乘积为零。因此 $\mathcal C_p$ 是无 $p$ 扭的整环格，含 $\mathcal A_p$。

R589 的全部来源次数界正好说明原九来源多项式代数的真实像
$\mathcal B_p$ 满足
$$
\boxed{\mathcal B_p\subset\mathcal C_p.}
\tag{5}
$$
本篇不声称 $\mathcal B_p=\mathcal C_p$。式 (3) 只是已给原来源的共同整数目标。

## 2. 三生成元、全部关系和基唯一性

令
$$
\upsilon=\frac{w^p}{p^6}=e_p.
\tag{6}
$$
这是有限目标中的实际元素，不是新的固定整函数坐标。三个元素 $w,\epsilon,\upsilon$ 满足
$$
w^s=p\epsilon,\qquad
\epsilon^6=w\upsilon,\qquad
w^{s-1}\epsilon^5=p\upsilon,\qquad
\upsilon^s=0.
\tag{7}
$$

**定理 1。** 有准确的无扭表示
$$
\boxed{
\mathcal C_p\simeq
\mathcal O[w,\epsilon,\upsilon]/
(w^s-p\epsilon,\ \epsilon^6-w\upsilon,\
 w^{s-1}\epsilon^5-p\upsilon,\ \upsilon^s).
}
\tag{8}
$$
其整基为
$$
\boxed{
\upsilon^j w^r\epsilon^t,\quad
0\le j<s,\quad0\le t\le5,\quad0\le r<s,\quad
(t,r)\ne(5,s-1).
}
\tag{9}
$$

证明先保实际物理指数。令 $v=ts+r$。排除的那一个组合恰为 $v=p$；其余组合恰好一次枚举 $0\le v<p$。所以 (9) 对应的物理指标
$$
n=jp+ts+r
$$
恰好一次枚举 $0\le n<ps$，并且
$$
t_n=6j+t,\qquad
\upsilon^j w^r\epsilon^t=e_n.
\tag{10}
$$
这已证明这些像在原目标中整线性独立，数量恰为 $ps$。

另一方面，用 $\epsilon^6=w\upsilon$、$w^s=p\epsilon$，
并在剩下 $(r,t)=(s-1,5)$ 时用第三个关系，可将任意单项式化成 (9) 或零。每次 $\epsilon$ 的六次转移都提高 $\upsilon$ 次数；当它达到 $s$ 即为零。在两次这样的转移之间，$w^s$ 约化严格降低 $w$ 次数，所以过程终止。所有标准项已在 (10) 中独立，因此不存在隐含的 $p$ 扭或额外关系。这证明 (8)。

特别，原 $\epsilon^p=0$ 也保持：
$$
\epsilon^p=\epsilon^{6(s-1)+5}
=w^{s-1}\upsilon^{s-1}\epsilon^5
=p\upsilon^s=0.
\tag{11}
$$

模 $p$ 后得到真正的乘法目标
$$
\boxed{
\overline{\mathcal C}_p
=k[w,\epsilon,\upsilon]/
(w^s,\ \epsilon^6-w\upsilon,\
 w^{s-1}\epsilon^5,\ \upsilon^s).
}
\tag{12}
$$
旧 $\overline{\mathcal A}_p\to\overline{\mathcal C}_p$ 的核准确为 R589 的
$$
J_p=\langle w^r\epsilon^Q:Q+6r\ge p\rangle .
\tag{13}
$$
确实相应原基元素是 $p^{t_n-Q}e_n$，指数为零或一；恰在 (13) 中被杀。不能由 $J_p^2=0$ 推断 (12) 中的原来源乘积为零。

## 3. 原全部来源的完整模 p 像

保持 R586 的同一真实展开
$$
A_4=z^2f_4=w e^{(a/p)w^s}G_4(w),\qquad
A_1=z^5f_1=w e^{(a/p)w^s}G_1(w),
$$
$$
a=6pc,\quad c=[z^{p+1}]\log(\sigma/z),\quad
G_\ell=\sum_{r\ge0}g_{\ell,r}w^r,
\quad \bar a\in k^\times.
\tag{14}
$$
原 Euler 基满足
$$
(6w\partial_w-h)W_{\ell,h}=A_\ell,
\quad
(\ell,h)=(4,0),(4,1),(1,0),\ldots,(1,4).
\tag{15}
$$
在 $r<s$ 的窗口，$g_{\ell,r}$ 是原 $f_\ell$ 的真实整系数。定义未除去 $b$ 尺度的两个指定 forcing
$$
c_{\ell,p}=\bar g_{\ell,s-1}.
\tag{16}
$$

### 3.1 两条原算术来源

对 $X=S,T$，令
$$
a_S=(17/3)a,\qquad a_T=12a,\qquad
L_X(w)=\sum_{u=1}^{s-1}\overline{[w^u]X}\,w^u .
$$
由 R600 及 (13)，在 (12) 中整条原像为
$$
\boxed{
\bar X=L_X(w)
 \sum_{L=0}^{p-1}\frac{\bar a_X^L}{L!}\epsilon^L .
}
\tag{17}
$$
所有 $L+6u\ge p$ 的原单项式在 (12) 中准确为零；这正是原加强行多取一阶 $p$ 的结果，不是删去一个未经估计的尾。

### 3.2 七个原 Euler 来源

定义实际共振多项式
$$
\boxed{
\Gamma_{\ell,h}(\upsilon)=
\sum_{j=j_0}^{s-1}
 \frac{\bar a^{6j+h-1}\bar g_{\ell,s-1-j}}
 {(6j+h)!}\upsilon^j,\qquad
j_0=\begin{cases}1,&h=0,\\0,&h>0.\end{cases}
}
\tag{18}
$$
全部阶乘严格小于 $p$。则七条来源的**完整**像为
$$
\boxed{
\bar W_{\ell,h}
=
\sum_{\substack{1\le u<s,\ L\ge0\\L+6u<p}}
 \frac{\bar a^L\bar g_{\ell,u-1}}
 {L!(L+6u-h)}\,w^u\epsilon^L
+\epsilon^h\Gamma_{\ell,h}(\upsilon).
}
\tag{19}
$$
第一部分的分母都为单位，因为 $6\le L+6u<p$ 而 $0\le h\le4$。

证明直接按原 $k=Ls+u$ 的完整系数分为两类。若 $u<s$ 且 $L+6u<p$，实际分母 $6k-h$ 未共振，得到 (19) 的第一部分。若 $L+6u\ge p$ 而没有
$L+6u=p+h$，加强归一化多给一阶 $p$，该项为零。真正的共振指标唯一写成
$$
k=pj+hs,\qquad 0\le j<s,
$$
而原实际分母是
$$
6k-h=p(6j+h).
$$
代入 R586 的整条首项同余，得到 (18)。$h=0,j=0$ 是原零指标，不产生一项；$h>0,j=0$ 则必须保留。

所以
$$
\boxed{
\Gamma_{\ell,0}(0)=0,\qquad
\Gamma_{\ell,h}(0)
=\frac{\bar a^{h-1}}{h!}\,c_{\ell,p}\quad(h>0).
}
\tag{20}
$$
R589 的首极部恰是 (18) 的 $j\ge1$ 部分；R592 的指定最早行恰是同一个多项式的 $j=0$ 部分。这里没有把后者误作前者的一项。

## 4. 真实 Euler 分解和全部次数的低权环商

原算子 $6w\partial_w$ 保 (3) 的整格，模 $p$ 后在 (12) 上成为
$$
\mathscr D=6w\partial_w+\epsilon\partial_\epsilon,\qquad
\mathscr D(\upsilon)=0.
\tag{21}
$$
在 (9) 的基上，其特征值是 $6r+t\in\{0,\ldots,p-1\}$，每个值恰有 $s$ 个基向量。因此
$$
\mathscr D^p=\mathscr D,
\quad
\ker(\mathscr D-h)=
\epsilon^h k[\upsilon]/(\upsilon^s)\quad(0\le h\le5).
\tag{22}
$$
这是原目标的行算子分解；不把依赖 $p$ 的投影另加成全局来源。

所有权至少六的基向量恰构成理想 $(w)$。故有真实环商
$$
\boxed{
\mathcal Q_p:=\overline{\mathcal C}_p/(w)
\simeq k[\epsilon,\upsilon]/(\epsilon^6,\upsilon^s).
}
\tag{23}
$$
原全来源代数到此的同态准确为
$$
\boxed{
S,T\longmapsto0,\qquad
W_{\ell,h}\longmapsto
 \epsilon^h\Gamma_{\ell,h}(\upsilon).
}
\tag{24}
$$
因此对**所有 $D$ 和全部原多项式**，其真实低权像就是将 (24) 代入原多项式；不需只在一个线性来源空间作投影。

再令 $\upsilon=0$，恰好恢复 R592 的
$k[\epsilon]/(\epsilon^6)$ 真同态及两个 forcing。若两个 $c_{\ell,p}$ 都为零，(24) 的七个像都在理想 $(\upsilon)$ 中；但它们并不为零，因为 (18) 的最高系数由原 $g_{\ell,0}=1$ 给出单位。原首极部秩仍为七。

对实际来源中的 $h\ge1$，显示系数还给
$$
(6\upsilon\partial_\upsilon+h)\Gamma_{\ell,h}
=\bar a\,\Gamma_{\ell,h-1}
 +\mathbf1_{h=1}c_{\ell,p}.
\tag{25}
$$
这里是有限多项式变量 $\upsilon$ 的通常导数，不是把它认作原算子 (21) 或某个普通 core。式 (25) 保留了指定 forcing 作为真实非齐次常数。

例如原二次来源的真正乘法直接给
$$
\boxed{
[\upsilon^2]\,\bar W_{4,0}^{\,2}
=\left(\frac{\bar a^5\bar g_{4,s-2}}{720}\right)^2 .
}
\tag{26}
$$
这就是 R596 的 $p^{12}[w^{2p}]W_{4,0}^2$，在 (12) 中没有被平方零理想误杀。

## 5. 全部原矩阵和真前缀不变

对于任何原 $P\in E_{D,9}$，
$$
\operatorname{ev}_{\mathcal C_p}(P)
=\sum_{n<ps}p^{t_n}[w^n]P(\boldsymbol F)\ e_n .
\tag{27}
$$
所以 R596 的强化矩阵 $\widehat M_{p,D}$ 正是 (27) 的**原代数评价矩阵**。其模 $p$ 全列可以在 (12) 中用 (17)、(19) 的实际环乘法计算。式 (4) 已保所有整数进位，因而与 R596 的完整 Cauchy 公式严格相同。

原全前缀仍是
$$
K_{D,k}=E_{D,9}\cap\ker([w^0],\ldots,[w^{k-1}]),
\tag{28}
$$
不能以 $\ker\overline{\widehat M}$ 替代。目标环的表示没有取消这个提升问题；各个实际 Bockstein 必须仍从同一个 (27) 提取。

## 6. p 大于 7D 时的实际整 Schur 分块

取 $p>7D$，并保 (1) 的好惰性范围。于是 $D<s$。在 R604 的选定原行
$$
n=hs+q,\qquad0\le h\le q\le D,
$$
有
$$
h+6q\le7D<p,\qquad t_n=h.
\tag{29}
$$
因此对**全九格全部列**，真实泛函
$$
\mathcal L_{q,h}=p^h h!\,[w^{hs+q}]
\tag{30}
$$
都整。R604 的纯 $S/T$ 子方阵 $\mathcal V_{p,D}$ 又在
$\operatorname{GL}_{M_D}(\mathcal O)$ 中。

由这些具体原行定义
$$
\boxed{
\mathcal P_{p,D}:E_{D,9}\longrightarrow E_{D,2},
\qquad
\operatorname{coeff}(\mathcal P_{p,D}F)
=\mathcal V_{p,D}^{-1}\mathcal L(F).
}
\tag{31}
$$
这是实际整 retraction，且在原 $E_{D,2}$ 上恒等。若 $B$ 是一个含至少一条 Euler 坐标的原单项式，定义
$$
\widetilde B=B-\mathcal P_{p,D}B .
\tag{32}
$$
纯 $S/T$ 单项式与所有 $\widetilde B$ 构成同一个原局部格的整基；列变换为单位三角，没有改动原整格或附加自由列。

对任意原物理行 $r_n=[w^n]$，新列的实际值是完整 Schur 行
$$
r_n(\widetilde B)
=r_n(B)-r_n|_{E_{D,2}}\,
          \mathcal V_{p,D}^{-1}\mathcal L(B).
\tag{33}
$$
该式保全部 $n$；不是只保被选中的行。

当
$$
k\ge D(s+1)+1,
$$
原真前缀使全部 $\mathcal L(F)$ 精确为零，故 $\mathcal P_{p,D}F=0$。因此
$$
\boxed{
K_{D,k}=
\left\{\sum_B c_B\widetilde B:
 [w^n]\sum_Bc_B\widetilde B=0\quad(0\le n<k)\right\}.
}
\tag{34}
$$
其最后一行仍由 (33) 在同一个核上读取。这个等式与所有模 $p^r$ 提升相容，因为列变换本身整可逆；它不声称约化核自动具有提升。

两种已付原观察在这个分块中保持：

1. 纯 $S/T$ 多项式的实际像属于 $\mathcal A_p$，故
   $$
   \overline{p(F-\mathcal P_{p,D}F)}
   =\overline{pF}\quad\text{于旧 }J_p.
   \tag{35}
   $$
2. 由 (24) 及常数行，$\mathcal P_{p,D}F$ 在 $\mathcal Q_p$ 中恰为 $F(0)$，所以
   $$
   \boxed{
   \rho_{\mathcal Q_p}(F-\mathcal P_{p,D}F)
   =\rho_{\mathcal Q_p}(F)-\overline{F(0)}.
   }
   \tag{36}
   $$
   对原零增广多项式，完整低权共振像及两个 forcing 原样保留。

### 6.1 一次原列的具体系数

在 $D=1$，$W_{\ell,h}(0)=0$，故
$$
\mathcal P_{p,1}W_{\ell,h}
=\alpha_{\ell,h}S+\beta_{\ell,h}T .
$$
系数由原两行 $[w]$ 和 $p[w^{s+1}]$ 精确决定；其模 $p$ 为
$$
\boxed{
\bar\alpha_{\ell,h}
=\frac{234-33h}{19(6-h)(7-h)},\qquad
\bar\beta_{\ell,h}
=\frac{14h-101}{19(6-h)(7-h)}.
}
\tag{37}
$$
确实两行分别要求
$$
\alpha+\beta=\frac1{6-h},\qquad
\frac{17}{3}\alpha+12\beta=\frac1{7-h}.
$$
所有分母是单位。式 (37) 只是精确系数的约化，高精度仍使用 (31)，不将两个 $\ell$ 的高阶项合并。

## 7. 已付范围与后继实际约束

式 (8)、(19)、(23) 同时保留真实乘法、七个完整共振多项式及原低 forcing。$c_{4,p},c_{1,p}$ 可以在公式中同时为零而不使七条来源消失；本篇没有从非零最高系数推断它们的常数项非零。

式 (31)–(36) 保同一全九格和全部真前缀，但只分离纯 $S/T$ 子格，不把其余核赋成中央零，也不证明其高层均整。$\epsilon,\upsilon$ 是依赖 $p$ 的有限目标元素，未作为新固定来源加入全局斜率预算。

后续可在 (23) 的真实低度关系及 (27) 的更高 Bockstein 上继续。原完整算术中央与非空真层之间的缺口仍需单独支付。

## 8. 精确证书

[check-r607-integral-target-and-mixed-schur.mjs](../scripts/check-r607-integral-target-and-mixed-schur.mjs) 给出 20,846 项精确检查：

- 对既有 $p=17,23$ 有限目标，逐一核唯一标准基和全部有序基乘积，包含真实 $p$ 进位与截断；
- 在原解析纤维 $p=23$ 的 $b=1,17$ 两尺度，直接从有理 sigma 系数核七条原 $W$ 在全部 $0\le n<ps=92$ 的完整像，并核原两个被积来源的所有对应行；
- 核还原 forcing 常数项后完整低权七列仍秩七；
- 对 $p=23,b=17,D=3$ 的全部 220 条原九来源单项式，核同一十条选定行整，且真实纯 $S/T$ 子块为单位；
- 核 (37) 的两个实际来源行。

一般 $p,D$ 的无扭、全次数和真前缀结论由正文证明；没有新增素数非消失扫描。原主目标尚未由这些有限目标关系闭合。

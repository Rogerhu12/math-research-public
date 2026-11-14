# R170：局部有限闭乘子的尾分解与 UHF 正则化不可能性

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。
状态：完整证明。第一阶论证及局部有限扩展已由 critical_kernel 独立核对。结论针对实际模型及真实定义域，不从形式除法或未知核的尾速率推出。

## 1. 设置与结论

沿用 $H=L^2(\mathbb Z_2,\mu)$、实际 $A$，以及
$$
N_j=A^{2^j}/d_j,\qquad V_j=(I-N_j)(I+N_j)^{-1}.
$$
记 $\mathscr D$ 为所有有限柱函数，$\mathfrak U$ 为有限物理张量矩阵代数的范数闭包。
每个 $V_j$ 对低于 $j$ 的物理位作用为恒等；这一性质保留真实进位尾。
$\mathfrak U$ 包含 $\mathcal A$，但不是整个 $B(H)$。

对有限柱 $f=\sum_F\widehat f(F)\chi_F$，定义实际有界乘子
$$
X_f=\sum_F\widehat f(F)V_F,\qquad V_F=\prod_{j\in F}V_j.
\tag{1.1}
$$
这是有限和，且 $X_f1=f$、$X_f\in\mathcal A$。
各 $X_f$ 交换且满足 $X_f^*=CX_fC$，其中
$$
(Cu)(y)=\overline{u(-1-y)}.
$$

给定任意 $h\in H$，先在 $\mathscr D$ 上定义
$$
X_{h,0}f=X_fh.
\tag{1.2}
$$
下面证明它可闭，再记 $X_h=\overline{X_{h,0}}$。

称 $h$ 的 Walsh 支撑逐位局部有限，是指
$$
\#\{F:\widehat h(F)\ne0,\ j\in F\}<\infty
\quad\text{对每个 }j.
\tag{1.3}
$$
不要求全局次数有界，不要求实际乘子有界。

**定理1.1。** 若 $h$ 满足 (1.3)，且 $X_h$ 实际无界，则：

1. 对每个 $0\ne E\in\mathfrak U$，$EX_{h,0}$ 在 $\mathscr D$ 上没有通常 Hilbert 范数界。
2. 不存在 $0\ne E\in\mathfrak U$ 满足 $\operatorname{Ran}E\subseteq\operatorname{Dom}X_h$。
3. 不存在 $0\ne E\in\mathfrak U$ 和任意 $F\in B(H)$，使 $EX_{h,0}=F|_{\mathscr D}$。
4. 特别，$X_h$ 不可能是由 $\mathcal A$ 中非零分母和有界分子给出的真实最大闭分式；它不属于 R153 的 $\operatorname{Frac}\mathcal G$。

这里分母排除比只禁止某个已指定分式表示更强：任何非零 UHF 左因子都不能把该乘子在原图核心上有界化。

对无界复杂 $\ell^2$ 第一阶乘子，这些结论全部适用。其任意实际有界预解式在 $\{A\}'\setminus\mathfrak U$ 中，也不属于 $\operatorname{Frac}\mathcal G$。准确证明见 §7。

## 2. 任意 $h$ 的有限柱乘子确实可闭

(1.1) 由有限 Walsh 展开唯一确定。亦可使用有限柱的真有理芽表示 $f=R(A)1$；
两个交换算子若在循环向量1上相同，就在全部多项式轨道上相同，继而在 $H$ 上相同。
因此 (1.2) 没有表示选择的问题。

令
$$
\mathcal B(u,v)=\langle u,Cv\rangle
=\int u(y)v(-1-y)\,d\mu(y).
$$
它是连续对称双线性形式。对 $f,g\in\mathscr D$，
$$
\begin{aligned}
\mathcal B(X_{h,0}f,g)
&=\mathcal B(X_fh,g)
=\mathcal B(h,X_fg)\\
&=\mathcal B(h,X_gf)
=\mathcal B(f,X_gh)
=\mathcal B(f,X_{h,0}g).
\end{aligned}
\tag{2.1}
$$
中间等式使用
$X_fg=X_fX_g1=X_gX_f1=X_gf$。

因为 $C\mathscr D=\mathscr D$，(2.1) 说明
$$
\mathscr D\subseteq\operatorname{Dom}X_{h,0}^*,
\qquad
X_{h,0}^*|_{\mathscr D}=CX_{h,0}C.
\tag{2.2}
$$
伴随稠密定义，故 $X_{h,0}$ 可闭。其闭包 $X_h$ 以 $\mathscr D$ 为图核心，并且
$$
X_h^*=X_{h,0}^*,\qquad
X_h^*|_{\mathscr D}=CX_{h,0}C.
\tag{2.3}
$$
本节没有证明一般 $h$ 的最大 $C$ 自伴性；后文也不需要该加强。

取任意有限 Walsh 截断 $h_n\to h$ 于 $H$。
有限实际乘子的交换性给
$$
X_{h_n}f=X_fh_n\longrightarrow X_fh=X_{h,0}f
\quad(f\in\mathscr D).
\tag{2.4}
$$
这是真实逐向量极限，不是把点态乘法与算子乘法混同。

## 3. 局部有限支撑给出精确尾分解

固定整数 $m\ge1$，写
$$
H=H_m\otimes H^{(m)},
\qquad H_m=L^2(\{0,1\}^{[0,m)}).
$$
把 $h$ 的常数项及所有与 $[0,m)$ 相交的非空 Walsh 支撑项归为 $h^{\rm head}_m$。
由 (1.3)，这一集合是有限集，因此
$$
H_m^{\rm op}:=X_{h^{\rm head}_m}\in\mathcal A
\tag{3.1}
$$
是实际有界算子。它可以包含跨过第 $m$ 位的真实进位；不需要是局部张量矩阵。

其余项 $h^{\rm tail}_m=h-h^{\rm head}_m$ 全部只使用 $j\ge m$ 的位。
每个相应有限单项式 $V_F$ 对头 $H_m$ 为恒等。
由 (2.4) 取逐向量极限，存在尾有限柱域上的算子 $Z_m$，使
$$
\boxed{
X_{h,0}
=H_m^{\rm op}+I_{H_m}\otimes Z_m
\quad\text{于 }\mathscr D.
}
\tag{3.2}
$$
特别对 $v\in H_m$ 和尾有限柱 $g$，
$$
X_{h,0}(v\otimes g)
=H_m^{\rm op}(v\otimes g)+v\otimes Z_mg.
\tag{3.3}
$$

如果某个 $Z_m$ 在尾有限柱域上有一个有限的通常范数界，它就延拓为有界尾算子。
因为 $H_m$ 有限维，(3.2) 将使整个 $X_{h,0}$ 在 $\mathscr D$ 上有界。
其闭包遂为全域有界算子，矛盾。

所以当 $X_h$ 无界时，每个 $m$ 都有尾有限柱单位向量 $g_n$，满足
$$
\boxed{\|Z_mg_n\|\longrightarrow\infty.}
\tag{3.4}
$$
这里不需另行假设一个移位尾模型的最大闭域，也没有把核向量投到一个未证明保持核的柱空间。

实际上，以下证明适用于任何满足 (2.3)、(3.2)、(3.4) 的闭包；局部有限 Walsh 支撑是本模型中可直接核验的充分条件。

## 4. 非零 UHF 算子在某个完整尾扇区上有统一下界

固定 $0\ne E\in\mathfrak U$。
取有限局部算子 $K\otimes I_{H^{(m)}}$，使
$$
\|E-K\otimes I\|<\varepsilon<\frac14\|E\|.
\tag{4.1}
$$
可选 $m\ge1$；$K$ 作用于有限维 $H_m$。
取单位向量 $v\in H_m$，使 $\|Kv\|=\|K\|$。

对所有尾向量 $g$，
$$
\begin{aligned}
\|E(v\otimes g)\|
&\ge\|(K\otimes I)(v\otimes g)\|
-\varepsilon\|g\|\\
&=(\|K\|-\varepsilon)\|g\|\\
&\ge(\|E\|-2\varepsilon)\|g\|.
\end{aligned}
$$
因此
$$
\boxed{\|E(v\otimes g)\|\ge c_E\|g\|,
\qquad c_E:=\|E\|-2\varepsilon>0.}
\tag{4.2}
$$
这是对整个 $v\otimes H^{(m)}$ 的统一下界；不要求 $E$ 本身单射或具有闭值域。

取 §3 的 $g_n$，令 $f_n=v\otimes g_n\in\mathscr D$、$\|f_n\|=1$。
由 (3.3)、(4.2)，
$$
\begin{aligned}
\|EX_{h,0}f_n\|
&\ge\|E(v\otimes Z_mg_n)\|
-\|EH_m^{\rm op}f_n\|\\
&\ge c_E\|Z_mg_n\|-\|E\|\,\|H_m^{\rm op}\|
\longrightarrow\infty.
\end{aligned}
\tag{4.3}
$$
这证明定理1.1的左乘结论。整个证明没有要求 $E$ 与 $A$ 或 $X_h$ 交换。

## 5. 无非零 UHF 算子的整个像落在闭定义域

共轭 $C$ 把每个有限物理张量矩阵映为同样有限的张量矩阵：
它在物理位上作逐位翻转及复共轭。因此
$$
C\mathfrak U C=\mathfrak U.
\tag{5.1}
$$

反设 $0\ne E\in\mathfrak U$ 且
$\operatorname{Ran}E\subseteq\operatorname{Dom}X_h$。
$X_h$ 闭、$E$ 有界，所以全域算子 $X_hE$ 图闭。
闭图定理给
$$
L:=X_hE\in B(H).
\tag{5.2}
$$
对 $g\in\operatorname{Dom}X_h^*$，通常伴随关系给
$$
E^*X_h^*g=L^*g.
\tag{5.3}
$$
特别它在 $\mathscr D$ 上成立。

在 (5.3) 中取 $g=Cf$、$f\in\mathscr D$，并使用 (2.3)，得到
$$
E^*CX_{h,0}f=L^*Cf.
$$
再施加 $C$：
$$
\boxed{
(CE^*C)X_{h,0}f=(CL^*C)f
\quad(f\in\mathscr D).
}
\tag{5.4}
$$
$CE^*C$ 是非零 UHF 算子，右侧有界，与 §4 矛盾。

因此
$$
\boxed{
E\in\mathfrak U,\quad
\operatorname{Ran}E\subseteq\operatorname{Dom}X_h
\quad\Longrightarrow\quad E=0.
}
\tag{5.5}
$$
这个方向只用了有限柱上的准确伴随式，不要求
$\operatorname{Dom}X_h=\operatorname{Dom}X_h^*$ 或最大 $C$ 自伴性。

特别，若非零闭空间 $M\subseteq\operatorname{Dom}X_h$，则
$$
\boxed{P_M\notin\mathfrak U.}
\tag{5.6}
$$
也不存在非零 UHF 算子把整个 $H$ 映入这样的 $M$。
这里不要求 $M$ 不变；用于不变核时该结论当然仍成立。

## 6. 实际分母与快分式场的严格界线

§4 已证明：若 $E\in\mathfrak U\setminus\{0\}$，则不可能有 $F\in B(H)$ 满足
$$
EX_{h,0}=F|_{\mathscr D}.
\tag{6.1}
$$
所以即使一个有界分子不在 UHF 中，也不能用非零 UHF 分母表达这个无界乘子。

特别，若假设 $X_h$ 等于某个实际最大闭商 $E^{-1}F$，其中
$0\ne E\in\mathcal A$ 已具有合法的单值逆，而 $F$ 有界，
则按最大商定义，在 $\operatorname{Dom}X_h$ 上必须有
$$
EX_h=F.
$$
限制到 $\mathscr D$ 就违反 (6.1)。

R153 的每个 $\operatorname{Frac}\mathcal G$ 元素具有
$E,F\in\mathcal G\subseteq\mathcal A\subseteq\mathfrak U$ 的这样的原分母恒等式。
因此
$$
\boxed{X_h\notin\operatorname{Frac}\mathcal G}
\tag{6.2}
$$
作为真实最大闭实现的陈述成立。

这不是说任何形式非负阶商都无界。
R167、R168已经说明形式阶、真实有界性、真实谱各有不同作用；
本节给的是一个实际闭乘子类完全不进入该分式场的机制。

## 7. 全部无界第一阶与明确的有界交换子例子

### 7.1. 第一阶恰在系数不可和时无界

对
$$
h=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
支撑显然逐位局部有限。
R125 的实际闭乘子正是 §2 的有限柱闭包。

若 $a\in\ell^1$，$\sum a_jV_j$ 按算子范数收敛，故乘子有界。
反向可直接在有限柱上验证。
令 $S_j=I-2E_j$，实际与纯第一阶之差有界：
$$
\left\|\sum_j a_j(V_j-S_j)\right\|
\le8\sum_j|a_j|\eta_j<\infty.
\tag{7.1}
$$

在单个物理位可取单位向量 $\phi_j$，使
$$
\langle S_j\phi_j,\phi_j\rangle=1-\omega_j,\qquad|\omega_j|=1.
$$
对前 $n$ 位分别选择 $\omega_j$，可使所有
$-a_j\omega_j$ 具有同一相位，并把该相位与 $\sum_{j<n}a_j$ 对齐。
取这些位的张量积、其余位取常参考向量，得到有限柱单位向量 $f_n$。
纯尾的期望为零，因此
$$
\left|\left\langle
\left(a_*I+\sum_j a_jS_j\right)f_n,f_n
\right\rangle\right|
\ge\sum_{j<n}|a_j|-|a_*|.
\tag{7.2}
$$
(7.1) 只减少一个与 $n$ 无关的常数。
故 $a\notin\ell^1$ 时，实际乘子在有限柱单位向量上的范数无界。

所以本稿的第一阶范围精确是
$$
\boxed{a\in\ell^2\setminus\ell^1.}
\tag{7.3}
$$

### 7.2. 有界预解式在 UHF 与快分式场之外

设 $X$ 是这样的无界第一阶闭乘子，且 $\lambda\in\rho(X)$。
令
$$
R_\lambda=(X-\lambda I)^{-1}.
$$
其像恰为 $\operatorname{Dom}X$，故由 (5.5)
$$
\boxed{R_\lambda\notin\mathfrak U.}
\tag{7.4}
$$
R125 的真实域交换给 $R_\lambda\in\{A\}'$。
因此这是 $\{A\}'\setminus\mathfrak U$ 中的实际算子，不是形式候选。

若 $R_\lambda$ 属于 $\operatorname{Frac}\mathcal G$，R153 的闭逆及原分母图核心将使其真实逆
$$
R_\lambda^{-1}=X-\lambda I,
\qquad
\operatorname{Dom}R_\lambda^{-1}
=\operatorname{Ran}R_\lambda=\operatorname{Dom}X
$$
也属于同一快分式场。
$X-\lambda I$ 仍是无界局部有限第一阶乘子，违反 (6.2)。
故
$$
\boxed{R_\lambda\notin\operatorname{Frac}\mathcal G.}
\tag{7.5}
$$

例如取 $a_j=(j+1)^{-1}$。
R128/R138 已给相应第一阶 $X$ 的空谱，因此每个 $\lambda\in\mathbb C$ 的 $R_\lambda$ 都是上述明确例子。
这里不把有界逆当成 $\mathcal A$ 元素。

### 7.3. 固定共同图正则器也不在 UHF

R128 对任意复杂第一阶给四个非负系数分量的共同预解式乘积 $R(t)$，
满足
$$
R(t)\ne0,\qquad
\operatorname{Ran}R(t)\subseteq\operatorname{Dom}X,\qquad
XR(t)\in B(H).
$$
如果 $X$ 无界，(5.5) 因而给 $R(t)\notin\mathfrak U$。
这一结论不依赖把它对未知不变限制的稠密像再加强。

本稿只对真实单个预解式使用了 (7.5) 的快分式排除；
没有仅凭共同正则器是若干逆的乘积，就无条件断言每个这类乘积都不在该分式场。

## 8. 对局部有限高阶与共振核的准确用途

只要已有闭实现确是局部有限 Walsh 符号的有限柱闭包，
且该实现无界，§§3–6 原样适用。
例如 R131 中已完成闭实现的局部有限二阶，及已核准图核心的独立有限块类，
均可在满足无界性时使用这一准则。
本稿不要求局部有限符号有统一全局次数。

对 R144 的平方共振
$$
M=\ker(X-Y),\qquad Y\in\mathcal A,
$$
已知 $M\subseteq\operatorname{Dom}X$。
如果对应第一阶 $X$ 无界且 $M\ne0$，则必有
$$
P_M\notin\mathfrak U.
\tag{8.1}
$$
R164 仍允许 $P_M$ 属于其更大的高位渐近交换代数。
(8.1) 不与该结论矛盾，也不排除这种投影存在。

若系数在 $\ell^1$ 中，第一阶本来有界，(7.3) 的无界假设不成立；
本稿不因此关闭一般慢可和平方共振。

最后，有限位条件期望是有限秩算子，其整个像确实在有限柱域内。
它并非有限局部矩阵张量尾恒等的 UHF 元素。
因此这类普通图正则化与 (5.5) 相容；也没有由此获得与 $A$ 的精确交织。

## 9. 依赖及未解决部分

本稿使用实际 $V_F1=\chi_F$、共同 $C$ 对称和真实尾张量作用；
R125/R128/R138 用于第一阶已知闭实现、图正则器及明确预解例；
R153 用于快分式的真实逆与原分母恒等式。
局部有限尾分解、UHF 下界、左右正则化排除和无分母结论均在正文完整证明。

一般无限行二阶不自动满足 (3.2) 的有界头分解。
任意未知不变空间上的受限算子也未获得完整尾扇区，
所以全空间证明不能直接传给它们。
完整 Hilbert ISP 与一般慢共振核仍未解决。

# R473 — 三个实际来源的全函数域、规范化与整 conductor 返回

日期：2026-11-14。**状态：已证明。** R468 的第三条来源不仅给第三条
中央必要行；它还把原两生成元的次数 $102$ 函数域覆盖消掉。本篇计算
整个三来源环的规范化、准确 Hilbert 主项，并给一个固定的非零
conductor 乘子，把规范化空间整地返回原三生成元。返回不增加随预算
增长的分母素数，复系数成本至多指数增长。

这是原来源与整格的结论。没有把第三个生成元当成第三个代数独立
坐标，也没有给乘积、conductor 或规范化中的任意元素赋中央零。
R418 的严格全局门尚未由本篇改善。

## 1. 原多项式与固定整模型

在 R468 的共同 $E_1$ 框中，置
$$
t=-x^{-3},\qquad \Theta=x\sigma^2,\qquad
a=t(t-1)(7+4t+16t^2),\quad d=1+8t,\quad f=ad/7,
$$
$$
V=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
$$
三个已识别的实际来源为
$$
S=\Theta^{17}f,\qquad T=\Theta^{36}fV,\qquad
U=\Theta^{68}f_U,\qquad f_U=aH/91.
\tag{1}
$$
这里 $U$ 正是 R466/R469 首项 $z^6$ 的新曲线来源，且
$$
\begin{aligned}
H={}&(8t^2+20t-1)\\
&\cdot(256t^4-1024t^3+1536t^2-52t+13)\\
&\cdot(1792t^4-3136t^3+2112t^2-40t+1)\\
&\cdot(32768t^8-851968t^7+1949696t^6-2111488t^5\\
&\hspace{19mm}+439040t^4-49408t^3+58688t^2+1232t-1).
\end{aligned}
\tag{2}
$$
特别 $\deg H=18$、$H(0)=13$、$f_U=-t+O(t^2)$。
全式来自 R466 的 $P_{21}$，不是仅比较少数局部系数。

以下固定
$$
R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)].
\tag{3}
$$
短证书精确给出
$$
\begin{array}{c|c}
\text{整数}&\text{绝对值}\\ \hline
\operatorname{lc}(H)&2^{34}7\\
\operatorname{lc}(V)&2^{11}\\
\operatorname{disc}(ad)&2^{12}3^{19}7^2\\
\operatorname{Res}(ad,H)&2^{102}3^{109}13\\
\operatorname{Res}(ad,V)&2^{33}3^{32}.
\end{array}
\tag{4}
$$
所以在 $R$ 的每个剩余域中，$ad$ 均平方自由且与 $H,V$ 互素，
所有显示次数不降。允许 $H,V$ 彼此共有因子；证明不要求二者互素。

先将 $t,\vartheta$ 当作独立不定元，再令 $\vartheta=\Theta$。
R418 已证明实际 $\Theta$ 在 $\mathbf Q(t)$ 上超越，因此特征零
的实际来源没有被这个记号引入额外关系。模 $p$ 的来源环在本篇
仍指这个抽象整格，不能未经检验等同于实际截断 jet 的像。

## 2. 第三来源把次数 102 的覆盖消为一

两条权零函数准确为
$$
A(t)=\frac{S^{36}}{T^{17}}=\frac{f^{19}}{V^{17}},
\qquad
B(t)=\frac U{S^4}=\frac{343}{13}\frac H{a^3d^4}.
\tag{5}
$$
由 (4)，它们作为 $\mathbf P^1$ 上映射的次数分别为
$$
\deg A=102,\qquad \deg B=18.
\tag{6}
$$
所有 $A$ 的零点处，赋值对为
$$
\begin{array}{c|c}
\text{点}&(v(A),v(B))\\ \hline
a=0\text{ 的四点}&(19,-3)\\
d=0&(19,-4)\\
\infty&(7,-2).
\end{array}
\tag{7}
$$

**引理 1。** 在特征零及每个 $p\notin\{2,3,7,13,17\}$ 的剩余域中，
$$
k(A,B)=k(t).
\tag{8}
$$

**证明。** 可先作代数闭包，因为所求有限映射的次数不变。令 $P$ 为
$\infty$ 在中间函数域 $k(A,B)$ 所对应的点。其分歧指数同时整除
$7$ 和 $2$，故恰为一，而 $v_P(A)=7,v_P(B)=-2$。
若还有别的点 $Q$ 位于 $P$ 上方，则 $v_Q(A)=7e_Q>0$，故它必须
位于 (7) 的零点表中。有限零点的阶是 $19$，不可能等于
$7e_Q$。所以整个纤维只有 $\infty$，重数一。有限曲线映射的
纤维次数公式给扩张次数一；这也排除了不可分部分。$\square$

又因 $17^2-36\cdot8=1$，
$$
\vartheta=\frac{S^{17}V^8}{T^8f^9}.
\tag{9}
$$
因此
$$
\boxed{\operatorname{Frac}k[S,T,U]=k(t,\vartheta).}
\tag{10}
$$
相比之下，令 $h=S^{17}/T^8=\vartheta f^9/V^8$。整数指数矩阵
的行列式是一，故 $k(S,T)=k(A,h)$；$h$ 对 $k(t)$ 超越，遂有
$$
[k(t,\vartheta):k(S,T)]=102.
\tag{11}
$$
这给新增来源的准确有限覆盖作用，同时仍保超越次数为二。

## 3. 整个规范化环的显示基

给 $\vartheta$ 权一，故 $S,T,U$ 的权依次为 $17,36,68$。定义
$$
\mathcal A=R[S,T,U]\subset R[t,\vartheta],
$$
以及
$$
\boxed{
\mathcal B_m=
\vartheta^m a^{\lceil m/68\rceil}
R[t]_{\le \lfloor11m/34\rfloor-4\lceil m/68\rceil},
\qquad
\mathcal B=\bigoplus_{m\ge0}\mathcal B_m.
}
\tag{12}
$$
负次数上界表示零空间。特别 $\mathcal B_0=R$。分母的 floor/ceiling
是原来源次数强迫的，不能换为自由的角多项式。

**定理 2。** $\mathcal B$ 是 $\mathcal A$ 在其全函数域中的规范化。
对每个 (3) 之外的素数，(12) 的逐项约化同样是对应三来源环的
规范化。

**证明的第一部分：包含与正规性。** (1) 直接给
$\mathcal A\subset\mathcal B$：$S,T,U$ 的角次数分别为 $5,11,22$，
都含 $a$。对 $a$ 的每个不可约因子，赋 Gauss 权
$v(\vartheta)=-1/68$；在无穷远赋
$v_\infty(\vartheta)=11/34$。这些赋值非负的条件恰为
$$
v_{a_i}(q_m)\ge\lceil m/68\rceil,\qquad
\deg q_m\le\lfloor11m/34\rfloor
$$
对每个齐次系数 $\vartheta^m q_m(t)$ 成立。
故 $\mathcal B$ 是正规环 $R[t,\vartheta]$ 与这些赋值环的交，
从而正规；这也保留 $R$ 的所有竖直整性。其乘法封闭性亦可从
ceil 的次可加性和 floor 的超可加性直接核定。

**第二部分：真正有限的整扩张。** 置
$$
\rho=\vartheta^{68}a,\qquad
\mathcal B^{(68)}=\bigoplus_{n\ge0}\rho^nR[t]_{\le18n}.
\tag{13}
$$
这是 $\mathbf P^1_R$ 上 $\mathcal O(18)$ 的完整截面环。同时
$$
S^4=\rho\,a^3d^4/7^4,\qquad U=\rho\,H/91.
\tag{14}
$$
右侧两个十八次齐次式在有限点无公共零点，在无穷远 $H$ 的首项
又为单位。因此它们在 $R$ 上构成无基点 pencil。
在 $\mathbf P^1_R$ 上，对 $n\ge2$ 的 Koszul 序列
$$
0\longrightarrow\mathcal O(18n-36)
\longrightarrow\mathcal O(18n-18)^{\oplus2}
\longrightarrow\mathcal O(18n)\longrightarrow0
\tag{15}
$$
取全局截面是右正合，因为首项的 $H^1$ 为零。这证明 (13) 在
$R[S^4,U]$ 上由权零与权六十八的有限多个元素生成。

还须保留全部六十八个剩余类。写 $m=68n+r$、$0\le r<68$，
令 $\epsilon_r=\mathbf1_{r>0}$、
$q_r=\lfloor11r/34\rfloor-4\epsilon_r$。准确有
$$
\mathcal B_m=
\vartheta^r a^{\epsilon_r}\rho^n
R[t]_{\le18n+q_r}.
\tag{16}
$$
若 $q_r\ge0$，从 $n=0$ 开始；若 $q_r<0$，从 $n=1$ 开始。
之后每次乘 (13) 的完整十八次空间即可填满所有允许次数。
故 $\mathcal B$ 在 $\mathcal B^{(68)}$ 上由权至多 $80$ 的
显示单项式生成。合并 (15)，它在 $R[S^4,U]$、进而在
$R[S,U]$ 和 $\mathcal A$ 上都是有限模。

**第三部分：同一函数域。** (10) 给
$\operatorname{Frac}\mathcal A=\mathbf Q(t,\vartheta)$，而
$\mathcal A\subset\mathcal B\subset\mathbf Q(t,\vartheta)$。
上面已证明有限整性及正规性，所以 $\mathcal B$ 就是规范化。
在任一允许的剩余域中，(4)、(8)、(13)–(16) 逐字有效，得到同一
结论。$\square$

无基点 pencil 的一般截面环论证可参见 Miles Reid，
*Graded Rings and the Main Theorem*（2022 讲义），
[§10.2, pp. 2–3](https://mreid.warwick.ac.uk/MA4L7/Part4B_2022.pdf)；
本题所需的完整序列、整模型及所有剩余权已经在 (13)–(16) 给出。

## 4. 唯一关系、真实 Hilbert 主项与固定 conductor

令 $\mathcal P=R[S,U]$。两个生成元代数独立，且
$$
[k(t,\vartheta):k(S,U)]
=[k(t,S):k(B,S)]\,[k(t,\vartheta):k(t,S)]
=18\cdot17=306.
\tag{17}
$$
第一步使用 $B$ 的实际次数十八以及 $S$ 对 $k(t)$ 超越；第二步
是 $\vartheta^{17}=S/f$，在 $k(t)[S]$ 对素元 $S$ 为 Eisenstein。

定理 2 已给 $T$ 在 $\mathcal P$ 上整，故其最小多项式为唯一
monic 多项式
$$
\Phi(S,U;Z)\in R[S,U][Z],\qquad \deg_Z\Phi=306,\qquad
\Phi(S,U;T)=0.
\tag{18}
$$
整系数也可由 $\mathcal P$ 正规与最小多项式系数的整性直接得到。
由 (10)，$T$ 生成 (17) 的整个扩张，所以此多项式不可约。按原权
伸缩后使用 monic 唯一性，$\Phi$ 的权恰为
$$
306\cdot36=11016.
\tag{19}
$$
因此
$$
\mathcal A\simeq R[s,u,Z]/(\Phi),\qquad
H_{\mathcal A}(q)=\frac{1-q^{11016}}
{(1-q^{17})(1-q^{36})(1-q^{68})}.
\tag{20}
$$
这是可复算的固定多项式定义，不要求把大关系逐项打印。
例如先在 $S=1$ 计算 $B=U$、$z=T^{17}=V^{17}/f^{19}$ 的
十八次最小式，再按 (19) 齐次化，即恢复同一个 $\Phi$。
也可直接用 (13)–(16) 的有限乘法模计算 $T$ 的最小式。

从 (12) 或 (20)，准确得到
$$
\operatorname{rank}_R\mathcal B_m
=\max\{0,\lfloor11m/34\rfloor-4\lceil m/68\rceil+1\},
$$
$$
\dim_k\mathcal A_m=\frac9{34}m+O(1),\qquad
\sum_{j\le m}\dim_k\mathcal A_j=\frac9{68}m^2+O(m).
\tag{21}
$$
式 (20) 的单位根处，除 $q=1$ 外只剩至多简单极点，故这里的
$O(1)$ 确为有界周期项。三来源仍是二次维数增长。

定义实际非零元素
$$
\boxed{\mathfrak c=\Phi_Z(S,U;T)\in\mathcal A_{10980}.}
\tag{22}
$$
它不是任意选择的“足够大乘子”。下面给其在原整格上的完整返回。

**定理 3。** 对所有 $m\ge0$，
$$
\boxed{\mathfrak c\,\mathcal B_m\subset\mathcal A_{m+10980}.}
\tag{23}
$$
此包含在 (3) 上整成立。对每个允许素数，$\mathcal A/p$ 嵌入
$\mathcal B/p$，且 $\mathfrak c\mathcal B$ 是 $\mathcal A$ 中
$p$-饱和子模。

**证明。** 记 $K=\operatorname{Frac}\mathcal P$、
$L=K(T)$。$\mathcal A$ 是 $\mathcal P$ 上基为
$1,T,\ldots,T^{305}$ 的自由模。令 $\ell$ 为这个基中最后一个
系数的泛函。配对
$$
(x,y)\longmapsto\ell(xy)
$$
在此基上反三角，反对角均为一，所以整且完美。Lagrange 插值，
或对 $\Phi$ 全部互异根作部分分式，给
$$
\operatorname{Tr}_{L/K}(x)=\ell(\mathfrak c x),\qquad x\in L.
\tag{24}
$$
这也可先对 $1,T,\ldots,T^{305}$ 核定，再由 $K$ 线性推广。

取 $b\in\mathcal B$、$a_0\in\mathcal A$。因为二者都在正规环
$\mathcal P$ 上整，$\operatorname{Tr}(ba_0)$ 是 $\mathcal P$ 中
的元素。由 (24)，$\ell(\mathfrak c b a_0)\in\mathcal P$ 对所有
$a_0$ 成立；完美配对遂给 $\mathfrak c b\in\mathcal A$。
这证明 (23)，并保全部齐次权。

在允许的剩余域中，(17) 的次数仍为 $306$，且 (18) 仍 monic，
故其约化仍是最小式，$\mathcal A/p\hookrightarrow\mathcal B/p$。
因为 $p\nmid306$，$\Phi_Z$ 的最高项 $306Z^{305}$ 非零，不可能
属于次数 $306$ 的最小式理想。因此 $\overline{\mathfrak c}\ne0$
于整环 $\mathcal B/p$。若 $\mathfrak cb=pa_0$，则先在
$\mathcal B/p$ 得 $\bar b=0$，写 $b=pb_1$ 后有
$a_0=\mathfrak cb_1$；这正是所断言的饱和性。$\square$

这里的标准 different 公式也见 Stacks Project（2026），
[Tag 0BWB, Example 49.12.5](https://stacks.math.columbia.edu/tag/0BWB)。
(24) 已给出本题需要的整 trace-dual 证明；没有假设规范化本身
在 $\mathcal P$ 上先验自由。

## 5. 原全纯来源、整测度与返回成本

(12) 的显示基为
$$
b_{m,j}=\vartheta^m a^{k_m}t^j,\qquad
k_m=\lceil m/68\rceil,\quad
0\le j\le\lfloor11m/34\rfloor-4k_m.
\tag{25}
$$
把其角多项式展开为 $\sum q_nt^n$ 时，始终有
$n\le\lfloor11m/34\rfloor<m/3$（$m>0$）。原函数中
$$
\boxed{\Theta^m t^n=(-1)^n\sigma^{6n}\Theta^{m-3n}.}
\tag{26}
$$
所有指数非负。因此每个 (25) 都是真正全纯的
$\mathcal S_{2m}$ 来源，且直接由已有的 $\sigma,\Theta$ 整测度相乘
得到有界整 Amice 测度；没有取不可控的来源反卷积。
它们在原点至少消失 $6k_m$ 阶。这只给总质量零，不能代 principal
单位质量或中央导数的消失。

返回 (23) 对原三生成元的通常总次数有确定上界
$$
\deg_{S,T,U}(\mathfrak c b)\le
\left\lfloor\frac{m+10980}{17}\right\rfloor
\tag{27}
$$
对每个齐次 $b\in\mathcal B_m$ 成立：所得多项式的每个单项式有
权 $m+10980$，而最小生成元权为十七。这里的线性换算与固定偏移
都必须计入预算，不能按第三个自由坐标计数。

还可选择返回表达，使其系数的复 $\ell^1$ 范数至多
$$
C^{m+1}\|b\|_{\rm coeff}
\tag{28}
$$
对一个固定 $C$ 成立，系数均在 $R$ 中。确切构造如下。
在 (15) 的 $n=2$ 情形，固定选择
$$
R[t]_{\le18}^{\,2}\longrightarrow R[t]_{\le36},
\quad (P,Q)\longmapsto (a^3d^4/7^4)P+(H/91)Q
$$
的一个整右逆；这是两个完整十八次齐次式的版本，确为满射。
该右逆存在于 $R$，因为 (4) 保每个剩余域的无基点性，而 $R$
是 PID。每将两个权六十八单项式相乘，即用同一个固定右逆降低
一个来源次数。迭代至多 $O(m)$ 次，系数范数至多指数增长。
用 (16) 的有限剩余类生成元，最后只需对有限多个
$\mathfrak c$ 乘生成元预选其在 $\mathcal A$ 中的整表达。
这证明 (28)，而不以一个未界定的高次线性方程逆矩阵代替实际成本。

由 (26) 的非负幂以及固定 $a$ 的系数界，同样可取
$$
|b(w)|\le C_1^{m+1}\|b\|_{\rm coeff}
\exp(C_2m|w|^{1/3}),\qquad w=z^6,
\tag{29}
$$
并在原权截面中使用 R418 的 Cauchy 优化。返回只改变其
$O(k+m)$ 项；主项仍是
$-3k\log k+3k\log m$。这没有自动支付惰性包络的严格改进。

### 5.1 抽象饱和与实际 jet 不混同

将 (22) 写为
$$
\mathfrak c=\Theta^{10980}q_{\mathfrak c}(t),\qquad
q_{\mathfrak c}\in a^{162}R[t],\qquad
\deg q_{\mathfrak c}\le3552.
\tag{30}
$$
它非零，故若 $r_{\mathfrak c}=\operatorname{ord}_{t=0}q_{\mathfrak c}$，
则
$$
162\le r_{\mathfrak c}\le3552.
\tag{31}
$$
实际 $w$-jet 的固定首项也是非零有理数。在 $\mathbf Q[[w]]$ 中，
乘 $\mathfrak c$ 是固定 $w^{r_{\mathfrak c}}$ 平移与可逆三角算子。
若使用普通处的原 Amice 参数 $Z$，(26) 还保证
$\mathfrak c(\Omega_p\log(1+Z))$ 整且有界；另删上述固定首项
分子、分母的素因子后，它准确为 $Z^{6r_{\mathfrak c}}$ 乘一个
整形式单位。这里才得到整可逆三角运输。若不删除这些素数，
须保留其实际赋值；这个固定集合不随 $m,k,p$ 变化。

定理 3 的抽象来源饱和本身不声称实际所有截断 jet 的像饱和。
不能把普通 Amice 坐标的整单位直接搬成惰性普通 Taylor 的整单位。
特别在惰性处，Gaussian、阶乘、原 $P_{134}/U_0$、两条十三行 carry
及原 $\pi\beta_J$ 仍要按原矩阵运输；(23) 不能把这些条件删除。

## 6. 对三中央路线的确切贡献

已付清的内容是：原三条已识别曲线来源的全部函数域；规范化的
显示整基和所有剩余权；一个真实固定 conductor 的整返回及
指数范数成本；以及其对实际形式 jet 的固定偏移范围。
这些结论允许在 (12) 中开展计算后，按 (23)、(27) 返回原三源。

仍未付清的是三条完整中央同时失败如何改善同一个原评价映射。
测度乘法是加法卷积；即使 $J'_S(0)=J'_T(0)=J'_U(0)=0$，
也不能把同样的零赋给 $b\in\mathcal B$ 或 $\mathfrak cb$。
需要真实的同域测试转置或原整矩阵关系。二次维数增长 (21)
也没有把 R418 的 $a_I+2b_I<3$ 改成一个已经成立的不等式。

有限多项式数据和全部六十八个剩余类生成元见
[check-r473-three-source-normalization.py](../scripts/check-r473-three-source-normalization.py)
及同名 JSON。它们仅核定本证明显示的固定数据，不通过目标素数
扫描推断任何无穷结论。

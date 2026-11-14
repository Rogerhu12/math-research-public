# R204 附录：树形自适应正逆、共同子商分离与坐标边界

日期：2026-11-12（UTC）。作者：critical_kernel；§F.2 由 root 补充并经 critical_kernel 独立复核。

状态：完整实际算子证明；作为 R204 的独立附录。所有一阶系数均在真实物理位上递归选取，保留实际进位。下文固定同一个有限放大次数 $d$，不声称同一族自动适用于全部未指定不变子商。

## A. 结论与接口

采用 R204 的记号
$$
\mathfrak C=\{A\}',\qquad
\mathfrak U=C^*(I,A),\qquad
J_j=M_{\chi_j},\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad S_j=I-2E_j.
$$
在 $H^{(d)}$ 上所有标量算子按对角方式放大，并记
$$
\mathfrak E_d=
\{T:[T,J_j^{(d)}]\to0,\ [T^*,J_j^{(d)}]\to0
\text{ 于 SOT}\}.
\tag{A.1}
$$

固定范数可分、含单位的 $C^*$ 代数
$\mathfrak B\subseteq\mathfrak E_d$，以及任意可数向量族
$h_1,h_2,\ldots\in H^{(d)}$。若需要固定 UHF，可先把 $\mathfrak B$
换成 $C^*(\mathfrak B,M_d(\mathfrak U))$。

**定理 A.1。**
可同时构造以 Cantor 空间 $\Xi=\{0,1\}^{\mathbb N}$ 为参数的非负系数行
$a^\xi$、闭一阶算子 $X_\xi=X_{a^\xi}$ 及其正逆
$$
a^\xi\in\ell^2\setminus\ell^1,\qquad
L_\xi=(I+X_\xi)^{-1}\in\mathfrak C,
\tag{A.2}
$$
使：

1. 每个 $h_r$ 属于全部 $\operatorname{Dom}X_\xi^{(d)}$，而且
   $\sup_\xi\|X_\xi^{(d)}h_r\|<\infty$；
2. $\|a^\xi\|_2^2=1/7$，$L_\xi$ 单射、稠密像、拟幂零，且
   $$
   \sqrt{7/8}\le\|L_\xi\|\le1;
   \tag{A.3}
   $$
3. 置
   $$
   \mathfrak D=C^*(\mathfrak B,\{L_\eta^{(d)}:\eta\in\Xi\}).
   $$
   对每个 $\xi$ 都存在压缩范数的满射 $*$ 同态
   $$
   \Pi_\xi:\mathfrak D\longrightarrow
   C^*(\mathfrak B,\{L_\eta^{(d)}:\eta\ne\xi\}),
   \tag{A.4}
   $$
   它固定 $\mathfrak B$ 和全部 $\eta\ne\xi$ 的 $L_\eta^{(d)}$，
   并满足 $\Pi_\xi(L_\xi^{(d)})=0$；
4. 对 $\xi\ne\eta$，
   $$
   \|L_\xi-L_\eta\|\ge
   \max(\|L_\xi\|,\|L_\eta\|)\ge\sqrt{7/8};
   \tag{A.5}
   $$
5. 映射 $\xi\mapsto L_\xi$ 在强*拓扑下连续；
6. 若 $\mathfrak B$ 包含预先指定的可数不变旗
   $N_r\subseteq M_r\subseteq H^{(d)}$ 的两个正交投影，
   且把每个非零 $Q_r=M_r\ominus N_r$ 的一个单位代表也列入
   $\{h_s\}$，则同一未经逐个归一化的族在每个 $Q_r$ 上有统一正的
   范数分离常数；其范数闭线性张成还同构于 $\ell^1(\Xi)$。

第 6 项不使用未知分子的限制稠密性。所用每个正逆在子商上的单射、
稠密像由其严格正实部直接给出。

需要的已有实际接口如下：
$$
\sup_j\|V_j\|\le6,\qquad V_j\to0\text{ 于 WOT},\qquad
\|V_j-S_j\|\le8\eta_j,\qquad \eta\in\ell^2.
\tag{A.6}
$$
有限柱同时是每个实际一阶及其通常伴随的图核心。纯模型与实际模型的差
$$
K(a)=\sum_j a_j(V_j-S_j)\in\mathfrak U,\qquad
\|K(a)\|\le8\|a\|_2\|\eta\|_2
\tag{A.7}
$$
按范数收敛。非负且不可和的 $\ell^2$ 一阶为最大增生、空谱闭算子，
因此 $L=(I+X_a)^{-1}$ 为范数至多 $1$ 的有界拟幂零交换子。以上分别来自
R125、R128、R138、R164 及 R194；R204 主文也给出本附录所需的高位边界计算。

## B. 树的质量预算

对每个深度 $n\ge1$ 的二进节点 $s\in\{0,1\}^n$，分配一个有限物理位块
$J_s$。所有块两两不交；按逐层、层内固定字典顺序选择物理位，
使整个选择序列严格递增。

在深度 $n$ 规定
$$
\ell_n=n^2 2^{3n},\qquad
|J_s|=\ell_n,\qquad
\beta_n=\frac{n}{\ell_n}=\frac1{n2^{3n}}.
\tag{B.1}
$$
每块的系数总和与平方和分别为
$$
\ell_n\beta_n=n,\qquad
\ell_n\beta_n^2=2^{-3n}.
\tag{B.2}
$$
整个树全部位的平方质量有限：
$$
\sum_{n\ge1}2^n\ell_n\beta_n^2
=\sum_{n\ge1}2^{-2n}=\frac13.
\tag{B.3}
$$
单条无限路径的平方质量恰为 $1/7$，而其系数总和发散。

把整个树的物理位选择按上述顺序枚举为
$j_1<j_2<\cdots$，对应的规定权重记为 $\beta_k$。
这里 $\beta_k$ 只由所属节点的深度决定；始终 $0<\beta_k\le1$。
此时尚未确定具体 $j_k$。

取 $\mathfrak B$ 单位球的范数稠密序列 $T_1,T_2,\ldots$，
以及 $H^{(d)}$ 单位球的范数稠密测试序列 $v_1,v_2,\ldots$。

## C. 递归同时支付全部交换误差与共同域条件

假设正在选择全树第 $k$ 个物理位，它属于深度 $n$ 的节点 $s$。
令
$$
U_{\rm prev}=\prod_{\substack{\text{本节点中}\\\text{已经选定的 }j}}
J_j^{(d)}.
$$
在此步选择 $j_k$ 足够大，使：

1. 对全部 $r\le k$ 和 $\ell<k$，
   $$
   |\langle V_{j_k}^{(d)}h_r,V_{j_\ell}^{(d)}h_r\rangle|
   \le2^{-k-\ell};
   \tag{C.1}
   $$
2. 对全部 $r,t\le n$，
   $$
   \|[T_t,J_{j_k}^{(d)}]U_{\rm prev}v_r\|
   \le\frac{2^{-n}}{\ell_n},
   \qquad
   \|[T_t^*,J_{j_k}^{(d)}]U_{\rm prev}v_r\|
   \le\frac{2^{-n}}{\ell_n};
   \tag{C.2}
   $$
3. $j_k>j_{k-1}$。

每一步只有有限条件，且 $U_{\rm prev}$ 此时已经固定。
(C.1) 由 $V_j^{(d)}\to0$ 于 WOT 保证；
(C.2) 由 $\mathfrak B\subseteq\mathfrak E_d$ 保证。
各条件都在某个足够大的物理位后成立，故可以同时满足。

对节点 $s$ 定义
$$
U_s=\prod_{j\in J_s}J_j^{(d)}.
$$
恒等式
$$
[T,J_j^{(d)}U]v
=[T,J_j^{(d)}]Uv+J_j^{(d)}[T,U]v
$$
及酉性给出
$$
\|[T_t,U_s]v_r\|\le2^{-n},\qquad
\|[T_t^*,U_s]v_r\|\le2^{-n}
\quad(|s|=n,\ r,t\le n).
\tag{C.3}
$$
因此对任意深度趋于无穷的节点序列 $s_n$，以及每个固定 $T\in\mathfrak B$，
$$
U_{s_n}TU_{s_n}\longrightarrow T
\quad\text{强*}.
\tag{C.4}
$$
先在可数测试集上取极限，再用算子范数统一界延到全部向量，
最后用 $T_t$ 的范数稠密性即可。
这里每个巨大有限块的长度都已在递归中逐位付清；
没有从“固定长度”的渐近交换擅自推出移动长度结论。

### C.1 所有子级数都在给定向量上收敛

固定 $r$，并取任意有限集合 $F\subseteq\{k:k\ge K\}$，其中 $K\ge r$。
由 (A.6)、(C.1) 和 $\beta_k\le1$，
$$
\left\|\sum_{k\in F}\beta_k V_{j_k}^{(d)}h_r\right\|^2
\le
36\|h_r\|^2\sum_{k\ge K}\beta_k^2
+2\sum_{K\le\ell<k}2^{-k-\ell}.
\tag{C.5}
$$
第二项不超过
$$
\left(\sum_{k\ge K}2^{-k}\right)^2=2^{2-2K}.
$$
(B.3) 表明 (C.5) 右侧趋于零，而且与子集 $F$ 无关。
所以整个树级数在每个 $h_r$ 上无条件收敛，所有子级数的尾部也统一趋零。

所有子级数的和还有一个共同界。定义
$$
C_r=
6\|h_r\|\sum_{k<r}\beta_k+
\sqrt{12\|h_r\|^2+2^{2-2r}}.
\tag{C.6}
$$
则任意子级数在 $h_r$ 上的和范数至多 $C_r$。

这一步是实际向量估计，不声称任意一阶域向量的通常系数截断都收敛。
它恰好提供下文所需的共同域资料。

## D. 路径一阶与共同真实域

对路径 $\xi\in\Xi$ 定义
$$
a^\xi_j=
\begin{cases}
\beta_n,&j\in J_{\xi|n},\\
0,&j\text{ 不在该路径上}.
\end{cases}
\tag{D.1}
$$
由 (B.2)，
$$
\|a^\xi\|_2^2=\sum_{n\ge1}2^{-3n}=\frac17,\qquad
\sum_j a^\xi_j=\sum_{n\ge1}n=\infty.
\tag{D.2}
$$

(C.5) 使 $\sum_j a^\xi_j V_j^{(d)}h_r$ 收敛。
令其和为 $y_{\xi,r}$。对任意有限柱测试向量 $v$，
$$
\langle y_{\xi,r},v\rangle
=\langle h_r,(X_\xi^{(d)})^*v\rangle.
$$
有限柱为通常伴随的图核心，所以
$$
h_r\in\operatorname{Dom}X_\xi^{(d)},\qquad
X_\xi^{(d)}h_r=y_{\xi,r},\qquad
\sup_\xi\|X_\xi^{(d)}h_r\|\le C_r.
\tag{D.3}
$$

每个 $L_\xi=(I+X_\xi)^{-1}$ 均为范数至多 $1$ 的有界交换子，单射、
稠密像、拟幂零。对 $y\in H$ 令 $x=L_\xi y$，最大增生性给
$$
\operatorname{Re}\langle L_\xi y,y\rangle
=\operatorname{Re}\langle x,(I+X_\xi)x\rangle
\ge\|x\|^2.
\tag{D.4}
$$
即 $\operatorname{Re}L_\xi\ge L_\xi^*L_\xi$。

还有统一的范数下界。实际恒等式 $V_j1=\chi_j$ 给
$$
X_\xi1=\sum_j a^\xi_j\chi_j,\qquad
\|(I+X_\xi)1\|^2=1+\|a^\xi\|_2^2=\frac87.
$$
因 $L_\xi(I+X_\xi)1=1$，
$$
\|L_\xi\|\ge\sqrt{7/8}.
\tag{D.5}
$$

## E. 一个路径块消去本坐标、固定所有其他坐标

固定 $\xi$，取
$$
U_{\xi,n}=U_{\xi|n}.
$$
其支撑的最小物理指标趋于无穷。
(C.4) 已给它对 $\mathfrak B$ 的固定极限。

### E.1 本路径的真实逆被消去

写
$$
X_\xi=X_\xi^0+K_\xi,\qquad
K_\xi=K(a^\xi)\in\mathfrak U.
$$
本节点的系数总和恰为 $n$，故纯 Walsh 共轭的标量中心为
$$
\lambda_{\xi,n}=2\sum_{j\in J_{\xi|n}}a^\xi_j=2n.
$$
对固定有限柱 $v$，当节点位于其全部支撑之外时，纯局部式
$J_jS_jJ_j=2I-S_j$ 把节点中系数的符号翻转。
翻转后高位创建项仍互相正交，且与低位部分正交。
因此
$$
\|((I+X_\xi)^{(d)}-2n)U_{\xi,n}v\|\le C_{\xi,v},
$$
$$
\|(((I+X_\xi)^{(d)})^*-2n)U_{\xi,n}v\|\le C'_{\xi,v},
\tag{E.1}
$$
常数与 $n$ 无关。实际进位只增加 $\|K_\xi\|\|v\|$。
所有这些向量均为有限柱，处于真实算子及通常伴随的域。

分别左乘 $L_\xi^{(d)}$ 和 $(L_\xi^{(d)})^*$，得到
$$
L_\xi^{(d)}U_{\xi,n}\to0,\qquad
(L_\xi^{(d)})^*U_{\xi,n}\to0
\quad\text{强}.
$$
于是
$$
U_{\xi,n}L_\xi^{(d)}U_{\xi,n}\to0\quad\text{强*}.
\tag{E.2}
$$

### E.2 分叉后的块与其他路径的纯部分严格交换

若 $\eta\ne\xi$，则在分叉深度之后，
$J_{\xi|n}$ 与 $a^\eta$ 的整个支撑不交。
所以纯算子 $X_\eta^0$ 与 $U_{\xi,n}$ 在有限柱核心上严格交换，
由闭包得到完整域的不变性和域交换。

实际差只来自 $K_\eta$：
$$
[I+X_\eta,U_{\xi,n}]=[K_\eta,U_{\xi,n}]
\quad\text{于 }\operatorname{Dom}X_\eta.
\tag{E.3}
$$
由于 $K_\eta\in\mathfrak U$，而这些 Walsh 乘积的全部位整体趋向无穷，
$$
\|[K_\eta,U_{\xi,n}]\|\to0.
\tag{E.4}
$$
证明只需先以有限头 UHF 算子范数逼近 $K_\eta$；
足够远的任意长度 Walsh 乘积都与该有限头算子严格交换。

真实逆的交换子恒等式为
$$
[L_\eta,U_{\xi,n}]
=-L_\eta[K_\eta,U_{\xi,n}]L_\eta.
\tag{E.5}
$$
因此
$$
U_{\xi,n}L_\eta^{(d)}U_{\xi,n}\longrightarrow L_\eta^{(d)}
\quad\text{按范数}\qquad(\eta\ne\xi).
\tag{E.6}
$$
这给出的不是一个只对有限多条路径成立的构造。
固定 $\xi$ 的同一个序列，对每条不同的 $\eta$ 都有 (E.6)；
不要求相对于所有 $\eta$ 一致。

### E.3 坐标边界的完整构造

(C.4)、(E.2)、(E.6) 在 $\mathfrak D$ 的全部生成元上给出强*极限。
每个有限非交换 $*$ 多项式只涉及有限多个生成元，
故其共轭序列仍强*收敛，极限范数不超过原范数。
再按范数延拓，得到 (A.4) 的 $*$ 同态 $\Pi_\xi$。

其像恰为删去本坐标后生成的 $C^*$ 代数：
全部保留的生成元被固定，而任意多项式的像只含这些生成元。
这些 $\Pi_\xi$ 在共同生成元上两两交换，所以作为同态也两两交换。

更一般，对任意路径子集 $I\subseteq\Xi$，可定义一个同时消去 $I$、
固定其余路径与 $\mathfrak B$ 的压缩范数 $*$ 同态。
对一个有限多项式，只组合其涉及的有限多个 $\Pi_\xi$；
收缩性保证不同表达一致，再范数延拓即可。
这里不声称这个一般坐标删除映射由单个序列实现，也不声称它强连续。

## F. 全空间与指定子商上的范数分离

若 $\xi\ne\eta$，应用 $\Pi_\xi$ 与 $\Pi_\eta$ 分别得到
$$
\|L_\xi^{(d)}-L_\eta^{(d)}\|\ge\|L_\eta\|,
\qquad
\|L_\xi^{(d)}-L_\eta^{(d)}\|\ge\|L_\xi\|.
\tag{F.1}
$$
这证明 (A.5)。

又若
$$
B\in C^*(\mathfrak B,\{L_\eta^{(d)}:\eta\ne\xi\}),
$$
则 $\Pi_\xi B=B$，从而
$$
\|L_\xi^{(d)}-B\|\ge\|B\|.
$$
三角不等式给
$$
\operatorname{dist}
\left(L_\xi^{(d)},
C^*(\mathfrak B,\{L_\eta^{(d)}:\eta\ne\xi\})\right)
\ge\frac12\|L_\xi\|.
\tag{F.2}
$$

现在令 $\mathfrak B$ 包含指定旗 $N_r\subseteq M_r$ 的两个投影。
置 $P_r=P_{M_r}-P_{N_r}$，$Q_r=P_rH^{(d)}$，并记
$$
L_{\xi,r}=\left.P_rL_\xi^{(d)}P_r\right|_{Q_r}.
$$
实际交换子保持两端旗，因此它就是相应的子商算子。
对非零 $x\in Q_r$，(D.4) 给
$$
\operatorname{Re}\langle L_{\xi,r}x,x\rangle
\ge\|L_\xi^{(d)}x\|^2>0.
\tag{F.3}
$$
所以 $L_{\xi,r}$ 及其伴随均单射，$L_{\xi,r}$ 稠密像。
它仍拟幂零，因为子商上所有幂的范数不超过全空间的相应幂范数。

每个 $\Pi_\xi$ 固定 $P_r$，故限制到角 $P_r\mathfrak D P_r$，
消去 $L_{\xi,r}$ 并固定全部 $L_{\eta,r}$，$\eta\ne\xi$。
于是
$$
\|L_{\xi,r}-L_{\eta,r}\|
\ge\max(\|L_{\xi,r}\|,\|L_{\eta,r}\|).
\tag{F.4}
$$

### F.1 同一未经归一化的族在每个指定非零子商上统一分离

对每个非零 $Q_r$，把一个单位向量
$h_{s(r)}\in M_r\cap N_r^\perp$ 加入共同域资料。
由 (D.3)，
$$
\sup_\xi\|X_\xi^{(d)}h_{s(r)}\|\le C_{s(r)}.
$$
每个有限部分和都保持 $M_r$，而这里的部分和实际收敛，
故
$$
y_\xi=(I+X_\xi^{(d)})h_{s(r)}\in M_r.
$$
它满足
$$
L_{\xi,r}[y_\xi]=[h_{s(r)}],\qquad
\|[h_{s(r)}]\|=1,\qquad
\|[y_\xi]\|\le1+C_{s(r)}.
$$
所以
$$
\|L_{\xi,r}\|\ge
c_r:=\frac1{1+C_{s(r)}}>0
\quad\text{对全部 }\xi.
\tag{F.5}
$$
结合 (F.4)，得到同一族在每个指定 $Q_r$ 上的 $c_r$-分离。
常数允许依赖于子商，不依赖路径。

也可分别在每个 $Q_r$ 上归一化，此时
$$
\left\|
\frac{L_{\xi,r}}{\|L_{\xi,r}\|}
-\frac{L_{\eta,r}}{\|L_{\eta,r}\|}
\right\|\ge1
\quad(\xi\ne\eta).
\tag{F.6}
$$
因此这些子商的交换子代数都包含连续统大小的范数分离族；
事实上，该族已经来自原空间 $\mathfrak C$ 的实际子商表示。
没有把任意子商交换子都假定能提升到全空间。

### F.2 同一族在每个指定子商张成 $\ell^1(\Xi)$ 的闭副本

仍固定一个非零 $Q_r$，记 $L_\xi=L_{\xi,r}$，
$h=[h_{s(r)}]$，以及 $C=1+C_{s(r)}$。上一节给
$
\|h\|=1,\qquad L_\xi g_\xi=h,\qquad \|g_\xi\|\le C
\quad(\xi\in\Xi).
\tag{F.7}
$
此外压缩 (D.4) 得
$\operatorname{Re}L_\xi\ge L_\xi^*L_\xi$，故
$
(2L_\xi-I)^*(2L_\xi-I)\le I.
$
于是 $2L_\xi-I$ 为收缩，反向次序也满足
$(2L_\xi-I)(2L_\xi-I)^*\le I$，从而
$
\operatorname{Re}L_\xi\ge L_\xi L_\xi^*.
\tag{F.8}
$
令同一个单位向量泛函
$\varphi(T)=\langle Th,h\rangle$。由 (F.7)，
$
1=|\langle L_\xi g_\xi,h\rangle|
\le C\|L_\xi^*h\|,
$
因此
$
\operatorname{Re}\varphi(L_\xi)
\ge\|L_\xi^*h\|^2\ge\delta:=C^{-2}>0
\quad(\xi\in\Xi).
\tag{F.9}
$

现取任意有限集合 $F\subseteq\Xi$ 及复系数 $c_\xi$。
忽略零系数，把非零数 $c_\xi\varphi(L_\xi)$ 的辐角按四个半开扇区分组，
每个扇区角宽 $\pi/2$。至少有一组 $E\subseteq F$ 满足
$
\sum_{\xi\in E}|c_\xi|\ge\frac14\sum_{\xi\in F}|c_\xi|.
$
取该扇区中心的反向相位 $\omega$，则 $|\omega|=1$ 且
$
\operatorname{Re}\bigl(\omega c_\xi\varphi(L_\xi)\bigr)
\ge\frac{|c_\xi\varphi(L_\xi)|}{\sqrt2}
\ge\frac{\delta|c_\xi|}{\sqrt2}
\quad(\xi\in E).
$
§E.3 的坐标删除同态固定 $P_r$，故在此角上仍压缩范数。
删除 $F\setminus E$ 的坐标，并使用 $\|\varphi\|=1$，得到
$
\begin{aligned}
\left\|\sum_{\xi\in F}c_\xi L_\xi\right\|
&\ge\left\|\sum_{\xi\in E}c_\xi L_\xi\right\|\\
&\ge\operatorname{Re}\varphi\left(
\omega\sum_{\xi\in E}c_\xi L_\xi\right)\\
&\ge\frac{\delta}{4\sqrt2}\sum_{\xi\in F}|c_\xi|.
\end{aligned}
$
另一方面，$\|L_\xi\|\le1$ 给相反的直接上界。因此
$
\boxed{
\frac{\delta}{4\sqrt2}\sum_{\xi\in F}|c_\xi|
\le\left\|\sum_{\xi\in F}c_\xi L_{\xi,r}\right\|
\le\sum_{\xi\in F}|c_\xi|.
}
\tag{F.10}
$
有限和按 $\ell^1$ 范数延拓，给有界、下有界的线性映射
$
\Lambda_r:\ell^1(\Xi)\longrightarrow\{A_{Q_r}\}',\qquad
(c_\xi)\longmapsto\sum_\xi c_\xi L_{\xi,r}.
\tag{F.11}
$
每个 $\ell^1(\Xi)$ 元素只有可数支撑，级数绝对范数收敛。
(F.10) 保证其像闭，且恰为 $\{L_{\xi,r}:\xi\in\Xi\}$ 的范数闭线性张成。
该闭副本仍由原 $\mathfrak C$ 中绝对范数收敛的同一线性组合表示。
这里没有使用不可数积分或边界同态的正常性。

## G. 强*连续的 Cantor 族与非正常边界

若路径 $\xi,\eta$ 具有相同的前 $N$ 层节点，则
$$
\|a^\xi-a^\eta\|_2^2
\le2\sum_{n>N}2^{-3n}
=\frac27\,2^{-3N}.
\tag{G.1}
$$
对固定有限柱 $v$，纯一阶的固定次数估计和 (A.7) 给
$$
\|(X_\xi-X_\eta)v\|
\le C_v\|a^\xi-a^\eta\|_2.
\tag{G.2}
$$

固定 $\xi_0$ 和 $y\in H$。
有限柱是 $X_{\xi_0}$ 的图核心，而 $I+X_{\xi_0}$ 满射，
故可选有限柱 $v$，使
$$
\|y-(I+X_{\xi_0})v\|<\varepsilon.
$$
利用 $\|L_\xi\|\le1$，
$$
\begin{aligned}
\|L_\xi y-L_{\xi_0}y\|
&\le2\varepsilon+
\|L_\xi(I+X_{\xi_0})v-v\|\\
&\le2\varepsilon+\|(X_{\xi_0}-X_\xi)v\|.
\end{aligned}
\tag{G.3}
$$
由 (G.1)–(G.2)，$\xi\mapsto L_\xi$ 强连续。
所有实际交换子满足共同 $C$ 对称
$L_\xi^*=C L_\xi C$，故该映射也强*连续。
有限放大以及固定角压缩保留此连续性。

于是同一族在强*拓扑中是紧的，而在算子范数中由 (A.5) 一致分离。
这并不矛盾。
具体地，固定 $\xi$，取不同的路径 $\eta_n\to\xi$：
$$
L_{\eta_n}\to L_\xi\quad\text{强*},\qquad
\Pi_\xi(L_{\eta_n}^{(d)})=L_{\eta_n}^{(d)},\qquad
\Pi_\xi(L_\xi^{(d)})=0.
$$
所以 $\Pi_\xi$ 不是强连续映射。
这也明确阻止从固定一个强稠密可数族推断固定整个强闭包。

## H. 有限坐标的单侧解析独立性

固定有限条不同路径 $\xi_1,\ldots,\xi_m$。
在全空间可取系数于 $\mathfrak B$；
在上述一个非零子商角上，可取系数于 $P_r\mathfrak B P_r$。
以下统一记坐标为 $L_1,\ldots,L_m$，固定系数代数为 $\mathfrak A$。
这些坐标两两交换，单射、稠密像、拟幂零；
每个坐标删除映射固定全部系数与其他坐标。

设 $B_\alpha\in\mathfrak A$，$\alpha\in\mathbb N^m$，
并存在 $\rho>0$ 使
$$
\sum_{\alpha\in\mathbb N^m}\|B_\alpha\|\rho^{|\alpha|}<\infty.
\tag{H.1}
$$
则
$$
\sum_\alpha B_\alpha L_1^{\alpha_1}\cdots L_m^{\alpha_m}=0
\quad\Longrightarrow\quad B_\alpha=0\ \text{对全部 }\alpha.
\tag{H.2}
$$
右侧系数的对应结论也成立。

为核验收敛与取消，先以 $L_1$ 的次数分组：
$$
C_n=\sum_{\beta\in\mathbb N^{m-1}}
B_{(n,\beta)}L_2^{\beta_2}\cdots L_m^{\beta_m}.
$$
各 $L_i$ 拟幂零，故在任意指定正数 $\delta<\rho$ 下有
$\|L_i^k\|\le C_\delta\delta^k$。
(H.1) 因而保证上述分组、原级数及每次有限移位级数均绝对范数收敛。
删除 $L_1$ 的映射给 $C_0=0$，再利用 $L_1$ 的稠密像取消右因子，
逐次得全部 $C_n=0$。
对剩余坐标归纳，得到 (H.2)。
若系数放在右侧，则逐次使用 $L_1$ 的单射性取消左因子。

不要求系数相互交换或与坐标交换。
这里只证明精确关系的系数独立性；不由此推断任意非零多变量表达式在
未知不变子商上单射或限制稠密。
(H.1) 也是必要的使用条件：不能仅凭最初一个级数收敛便假设全部移位级数收敛。

## I. 范围与仍开放的问题

树形构造允许同时固定任意给定的范数可分 $\mathfrak B\subseteq\mathfrak E_d$、
可数旗和可数域向量，但这些资料必须在递归前指定。
连续多个坐标本身是在递归后共同生成的，不被错误地加入最初需要固定的
范数可分代数。

全部真实进位误差通过 UHF 范数收敛的 $K(a^\xi)$ 处理；
不同路径分叉后的严格纯交换只用于推导实际逆交换子 (E.5)。
共同域来自 (C.5) 的明确无条件向量收敛，而非一般域向量的系数截断断言。

本附录没有排除原慢平方共振核，没有证明任意慢符号在所有不变限制中
稠密，也没有构造原 Haar $A$ 的非平凡闭不变子空间。
它补强 R204 的结果为：指定子商中的同一实际连续统正逆族、统一范数分离、
逐坐标 $C^*$ 边界、每个指定子商中的 $\ell^1(\Xi)$ 闭副本及明确的强*与范数拓扑差别。

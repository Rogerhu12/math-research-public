# R925 — 原 y_s 覆盖的306维整基、双图表与完整交除子理想

日期：2026-11-20。

**状态：以下整基、完整乘法、双图表、原函数分母清除及闭点理想算法均已证明；本篇没有把尚未执行的306维整基/乘法或四个大交除子记为 PASS。权重至多4的版本使用 R924§13 已实际通过的 r=29 全核360；没有该回执的素数仍可用本文的无条件权重至多5构造。**

目标是消费 [R883](R883-original-relative-six-shadow-and-complete-boundary.md) 的同一原相对六次源及同一原交除子，避免给次数67680/94752的零维概形建立全维乘法表。本篇的仿射环是原光滑曲线的整环；所有矩阵均保原映射、全部共零、剩余域和非约化长度。它不是从一个短形式前缀猜一个平面模型。

## 1. 原覆盖与一个只在无穷纤维有零的截面

令 $Y=X_0(3468)$，$k=\mathbf F_r$ 或原消费者的 $\mathbf F_{r^2}$，$r=29,41$。保持 R924 的原 $u=q^3$、$S_Y=2S(u^2)$、$L_Y=\Omega_Y(\mathcal C_Y)$，故
$$
g_Y=559,\quad\deg L_Y=1224,\quad
R_m=H^0(Y,L_Y^m),\quad\dim R_m=1224m-558\quad(m\ge1).
\tag{1}
$$
本篇把原 $y_s$ 记作 $\xi$；它不是 R882 的 eta 坐标。原 $Y\to X_0(12)\simeq\mathbf P^1_\xi$ 的次数为306。令
$$
P_\infty=\operatorname{pole}(\xi),\qquad
P_0=\operatorname{zero}(\xi),\qquad\deg P_\infty=\deg P_0=306.
\tag{2}
$$
全部重数包含在这两个除子中；原展开点满足 $\xi=-u^{-1}+O(u)$，所以它在 $P_\infty$ 中的系数恰为1。

R882–R883 的原恒等式直接给
$$
T+27=\frac{(\xi^2+3)^3}{(\xi^2-1)^2}.
\tag{3}
$$
令 $C_Y$ 为原 $D_Y$ 的约化支集，则 R924 给 $D_Y=2C_Y$，而(3)给
$$
\operatorname{div}(\xi^2+3)=C_Y-2P_\infty.
\tag{4}
$$
这里 $Y\to X_0(12)$ 在这两个非 cusp 纤维上 étale，故 $C_Y$ 的612个几何点各为简单零；也可由原 $T+27$ 的三阶零及(3)核定。

因此
$$
w=(\xi^2+3)^2,\qquad\operatorname{div}(w)=D_Y-4P_\infty,
$$
$$
\boxed{J=S_Y/w\in R_1,\qquad\operatorname{div}_{L_Y}(J)=4P_\infty.}
\tag{5}
$$
这是原全局权二截面，不是新引入的 meromorphic frame。以原 $z=u\xi$ 计算时，
$$
J(u)=\frac{u^4S_Y(u)}{(z(u)^2+3u^2)^2}=2u^4+O(u^6).
\tag{6}
$$
原支 $z(0)=-1$，分母为单位。用 R924 的完整666维 $R_1$ 和全部1225个忠实 jet 读取(6)，就得到原 $J$ 的准确全局坐标。

记 $W_n=L(nP_\infty)$。由(5)，对每个 $m\ge1$ 有
$$
\boxed{W_{4m}=R_m/J^m.}
\tag{7}
$$
同时 $J_0=\xi^4J\in R_1$ 的零除子是 $4P_0$。这一第二截面将在后文保留整个无穷边界。

## 2. 完整低阶空间与306个过滤模基

原 $\xi=a/b$ 已按 R924§13 恢复为 $a,b\in R_1$ 的同次分式，$b\ne0$。若 $W_n$ 用 $c/J^m$ 的完整行空间表示，则
$$
\boxed{W_{n-1}=\{f\in W_n:\xi f\in W_n\}.}
\tag{8}
$$
**证明。** 在 $P_\infty$ 的每个闭点 $Q$，设 $e_Q=P_\infty(Q)$。$f\in W_n$ 且 $\xi f\in W_n$ 等价于
$v_Q(f)\ge-ne_Q$ 和 $v_Q(f)-e_Q\ge-ne_Q$，即 $v_Q(f)\ge-(n-1)e_Q$；在其余点上 $\xi$ 没有极，原 $f$ 的正则性保持。这也保留 $e_Q=289$ 的 cusp，不能只对约化支集施加一阶条件。证毕。

在同一个 $R_m$ 中写 $f=c/J^m$、$\xi f=d/J^m$，(8)准确变成
$$
ac=bd\quad\text{于原 }R_{m+1}.
\tag{9}
$$
完整左核的第一投影单射，因为 $b\ne0$；所以保全部核与其投影，直接得到完整 $W_{n-1}$。只选择一条核向量不能代替这个空间。

### 2.1 不使用 h_3 计算值的版本

从完整 $W_8=R_2/J^2$ 维1890出发，连续使用(8)得到 $W_7,\ldots,W_0$。这里(9)是 $R_3$ 的等式，必须检查全部 $u^0,\ldots,u^{3672}$；只需真实乘积行和这个已证明忠实窗，不必先构造完整 $R_3$ 基。

Riemann–Roch 给
$$
h_n:=\dim W_n=306n-558\qquad(n\ge4).
\tag{10}
$$
故 $h_8,h_7,h_6,h_5,h_4$ 分别为1890、1584、1278、972、666；$h_3,h_2,h_1$ 由实际全核读取，不预先猜测，$h_0=1$。

对 $n\ge2$，有准确交式
$$
W_{n-1}\cap\xi W_{n-1}=\xi W_{n-2}.
\tag{11}
$$
理由与(8)相同；所有极点的真实重数均保留。因此 $n\ge6$ 时，
$$
\dim(W_{n-1}+\xi W_{n-1})
=2h_{n-1}-h_{n-2}=h_n,
$$
所以
$$
W_n=W_{n-1}+\xi W_{n-1}\quad(n\ge6).
\tag{12}
$$

### 2.2 r=29 已付的 h_3=360 与较小输入

[R924§13](R924-original-section-divisor-algebras-and-shadow-interface.md) 已实际核完原 $a'-\xi b'$ 的全部1332个未知元、1532行及整个核，核维数恰为360。来源为公开 run `44721065286` / job `136236619274` / source `72187ffc534853a284fb141b6c5214c1761589af`，完整 RESULT hash 为 `f8918b05f72bd16c643547280dd20303237341f9d1d40de19e82fd249fc6f720`。

核的第二投影准确是 $H^0(L_Y(-P_\infty))$。除以(5)的 $J$ 后，正是 $W_3$。所以这个已付全局计算证明
$$
\boxed{h_3=360\quad(r=29).}
\tag{13}
$$
于是 $W_4+\xi W_4$ 的维数为 $2\cdot666-360=972=h_5$，(12)从 $n=5$ 就成立。可以从 $W_4=R_1/J$ 直接起步；$W_3$ 直接使用同一已付核的第二投影，随后只算 $W_3\to W_2\to W_1\to W_0$。这些(9)均为 $R_2$ 的等式，完整窗口只有 $u^0,\ldots,u^{2448}$，不需要先运行完整高权乘积选基。

对 $r=41$，应先读取该素数同一全核。若维数同为360，则相同简化适用；否则按§2.1保留权五版本。本篇不把一个素数的维数自动复制到另一个素数。

### 2.3 自由基的明确选择与完整性

从 $W_0=k$ 取 $b_0=1$，权 $d_0=0$。逐个 $1\le n\le m_0$，在
$$
W_n/(W_{n-1}+\xi W_{n-1})
\tag{14}
$$
中按固定行消元序选完整补基；每条新向量 $b_i$ 的权定义为 $d_i=n$。一般取 $m_0=5$，在(13)已付时取 $m_0=4$。

所选向量总数为
$$
h_{m_0}-h_{m_0-1}=306.
\tag{15}
$$
对每个 $n$，由(11)–(14)递推，准确有
$$
\boxed{\{\xi^j b_i:j\ge0,\ j+d_i\le n\}\text{ 是 }W_n\text{ 的完整 }k\text{ 基}.}
\tag{16}
$$
这里不只证明生成：$n=1$ 时 $W_0\cap\xi W_0=0$，因为 $\xi$ 非恒定，新基数为 $h_1-2$；$n\ge2$ 的新补基数为 $h_n-2h_{n-1}+h_{n-2}$。所以(16)中单项式的总数也恰为 $h_n$；由生成和维数得到全部线性独立性。

实现可保消元选出的非零常数倍 $b_0$，而不重新缩放；此时用完整 $W_0$ 读者求实际 `unit_scalar`，并核它乘 $b_0$ 为1。后文所有单位、乘法和图表均保这个真实单位坐标。

在权四版本中，若保尚未猜测的 $h_1,h_2$，各权的新基数为
$$
1,\quad h_1-2,\quad h_2-2h_1+1,\quad
360-2h_2+h_1,\quad h_2-54.
\tag{17}
$$
各数必须非负，和为306。只有实际核出 $h_2=54$ 后，才可把最大权进一步降为三。

令
$$
\mathcal A=\Gamma(Y\setminus\operatorname{Supp}P_\infty,\mathcal O_Y).
$$
由 $\mathcal A=\bigcup_nW_n$ 和(16)，得到实际整环同构
$$
\boxed{\mathcal A=\bigoplus_{i=0}^{305}k[\xi]\cdot b_i.}
\tag{18}
$$
这同时给原 $k(Y)/k(\xi)$ 的完整306维基。因为原 $Y$ 光滑，(18)就是 $k[\xi]$ 在原 $k(Y)$ 中的整闭包；不需要再对裸306次方程运行正规化，也没有用另一个同亏格曲线代替原源。

## 3. 全部乘法的有限窗口与实际矩阵

按(16)唯一展开
$$
b_i b_j=\sum_k m_{ij}^k(\xi)b_k,
\qquad\deg m_{ij}^k\le d_i+d_j-d_k,
\tag{19}
$$
右边上界为负时该多项式为零。所有系数由同一原 q-jet 读出，因为两边都已知属于 $W_{d_i+d_j}$。

原展开点在 $P_\infty$ 的系数为1，所以 $W_n$ 的完整忠实 Laurent 窗是
$$
u^{-n},u^{-n+1},\ldots,u^{305n},
\quad\text{等价于 }u^n f\text{ 的全部 }0,\ldots,306n.
\tag{20}
$$
若这个窗全零，$f$ 在原无穷点有至少 $305n+1$ 阶零，而其他极点的总极帽最多为 $306n-n=305n$，所以 $f=0$。此证明明确扣除了无穷点自己的极帽，避免把 Laurent 截断错当普通正则窗。

一般权五版本只需 $W_{10}$ 维2502和3061项窗；权四版本只需 $W_8$ 维1890和2449项窗。也可逐对使用更短的 $W_{d_i+d_j}$ 窗；不得缩短其本来完整边界。

### 3.1 权四版本的2453项输入

在权四版本写 $b_i=g_i/J$，$g_i\in R_1$。将 $W_8$ 的目标基乘 $J^2$，得到真实 $R_2$ 截面
$$
\Phi_{j,i}=J\,\xi^j g_i,\qquad j+d_i\le8.
\tag{21}
$$
这1890条截面在完整2449个 jet 上的秩必须为1890；因此它们同时给整个 $R_2$ 的一份实际全局基。产品 $b_i b_l$ 则对应原截面 $g_i g_l$。对所有需要的基对把 $g_i g_l$ 读到(21)的全部窗，再回代，即得到(19)；不必重新遍历原666条 $M_2$ 基的全部候选乘积。

**输入精度必须多留四项。** 若原 $R_1$ 行只保留 $N$ 项，除以 $J=u^4\cdot\text{unit}$ 后，$b_i$ 的绝对精度只有 $O(u^{N-4})$。目标 $\xi^j b_i$ 可能有 $j>4$；一般只能保证精度 $O(u^{N-4-j})$。统一取 $j\le8$，要读到(20)的 $u^{2440}$，须
$$
N-12\ge2441,\qquad\boxed{N\ge2453.}
\tag{22}
$$
等价地，在(21)中 $J\xi^j$ 最多损失四项；2453项输入给全部2449项真实 $R_2$ 输出。仅做 colon 时2449项确实足够，但不能不作说明就把它用于所有高 $\xi$ 幂的乘法目标行。原 $z=u\xi$、$J/u^4$ 及每次负阶乘除都保完整精度，记录实际误差阶。

### 3.2 多项式乘法算子

采用行向量，令 $M_i$ 的第 $j$ 行为(19)中 $b_i b_j$ 的多项式坐标。若 $f=\sum_i f_i(\xi)b_i\in\mathcal A$，则
$$
M_f=\sum_i f_i(\xi)M_i,\qquad
\operatorname{coord}(hf)=\operatorname{coord}(h)M_f.
\tag{23}
$$
每个 $M_i$ 只是306×306的 $k[\xi]$ 矩阵，次数由(19)给定。可按实际原函数需要按需计算这些算子；不必为一个六万维交点代数建立全维表。若一次构造所有 $M_i$，共有46971个无序基乘积，每个都仍由(20)或(21)的完整全局身份核定。

交换、结合来自这些真实函数的准确乘法；不能把几个随机三元组测试当作完整代数证明。记录基选择、全部权、目标完整矩阵、真实产品及回代 hash，就把(18)变成可复现的原整环。

## 4. 第二图表与整个原无穷边界

置 $\xi_\infty=1/\xi$、$c_i=\xi^{-d_i}b_i$。则
$$
\boxed{\mathcal A_\infty
=\Gamma(Y\setminus\operatorname{Supp}P_0,\mathcal O_Y)
=\bigoplus_i k[\xi_\infty]c_i.}
\tag{24}
$$
**证明。** 各 $c_i$ 只可能在 $P_0$ 有极。反过来，若 $f\in\mathcal A_\infty$，则 $f\in\mathcal A[1/\xi]$，可取大 $M$ 使 $\xi^M f\in\mathcal A$。因 $f$ 在 $P_\infty$ 正则，准确有 $\xi^M f\in W_M$。用(16)展开并除以 $\xi^M$，每项写成 $\xi_\infty^{M-j-d_i}c_i$，指数非负。因此全部生成。独立性由(18)在函数域中的独立性保持。证毕。

其乘法从第一图表直接得到：
$$
c_i c_j=\sum_k
\xi_\infty^{d_i+d_j-d_k}
m_{ij}^k(1/\xi_\infty)c_k.
\tag{25}
$$
(19)保证各系数是真多项式，没有负幂。两图表在 $\xi\ne0$ 上由 $c_i=\xi^{-d_i}b_i$ 精确胶合。

特别 $\mathcal A_\infty/(\xi_\infty)$ 就是原整个纤维 $P_\infty$ 的有限代数，维数306，包含原全部闭点及宽度重数。这里只对第二图表的 $\xi_\infty=0$ 计算边界；第一图表已经包含其余全部有限点，不能在两个图表上各算一遍同一有限点。

原六个 cusp 纤维为 $\xi=0,\pm1,\pm3,\infty$。由 R883 的完整 cusp 分支表，每个纤维有18个几何点：一处阶289，其余17处阶1，故总长度306。特别“纤维维数306”不等于306个几何 cusp；六个纤维的约化支集总数仍为108。基域 $\mathbf F_r$ 上的全部 cusp 域形状仍是 R924 的12个有理点和六个次数16闭点；扩到原 $k=\mathbf F_{r^2}$ 后仍须按真实嵌入读取剩余次数。

如果只计算 $\det M_f$ 在第一图表的零点，就会漏掉此整个 $P_\infty$。本篇的第二图表是具体的已正规化输入，不以一个“无穷处之后补算”的口头约定代替它。

### 4.1 原有限判别式及仅六处的高分歧参数

底 $X_0(12)$ 无椭圆稳定子；在所选好素数处，忘去17平方级结构的覆盖在非 cusp 开集 étale。上一节的每个 cusp 纤维恰有一个有理点的分歧指数289，其余17个几何点的指数为1。因 $r\nmid289$，全部分歧 tame。在局部 $v=u\varpi^e$ 中，$dv/d\varpi$ 的阶为 $e-1$；所以每个重 cusp 的 different 指数恰为288，其余点为零。

因此完整第一图表的判别式理想准确为
$$
\boxed{\operatorname{disc}(\mathcal A/k[\xi])
=\bigl(\xi(\xi^2-1)(\xi^2-9)\bigr)^{288}k[\xi].}
\tag{25a}
$$
有限部分次数为1440；无穷纤维再贡献288，合计1728，正好等于 $2g_Y-2+2\cdot306$。任何完整整基的 trace Gram 行列式只相差 $k^\times$，故将其首一化后必须准确等于(25a)，不能有额外指数或额外不可约因子。

过滤基还满足 $\sum_i d_i=g_Y+306-1=864$，由(16)对大 $n$ 的维数直接比较得出。trace Gram 每个项的次数上界为 $d_i+d_j$，故行列式的初步上界为1728；(25a)准确支付其少掉的无穷贡献。实际计算全部 trace Gram 行列式是可以独立运行的检验，本篇没有把它写作已完成的回执。

由(25a)，只要 $\pi$ 不整除五个有限 cusp 因子，$\mathcal A/(\pi)$ 就是 étale，且 $\pi(\xi)$ 在每个 $Q|\pi$ 都是原参数。此时交除子的非约化长度全部来自交重本身，局部读出可直接用 $\pi$ 的幂。五个有限重 cusp 和第二图表的唯一重 cusp 仍必须用§7.3的真实参数；不能在它们上把289阶的基参数当作一阶参数。

## 5. 每个原函数的准确分母清除

### 5.1 从原完整 M2 及退化截面进入整环

任何 $F\in R_1$ 都有 $F/J\in W_4$。由(16)在 $n=4$ 的666条基，读取完整坐标，即
$$
F/J=\sum_i p_{F,i}(\xi)b_i,
\qquad\deg p_{F,i}\le4-d_i.
\tag{26}
$$
将这些目标基乘 $J$，就是 $\xi^j g_i\in R_1$；所以此坐标变换直接在同一完整666维空间中完成，不需要新的高权函数域恢复。

R924 中的原三个退化 $\pi_j$，$j=1,2,4$，给已认证的 $jF(u^j)\in R_1$。把这些真实拉回截面送进(26)；权 $m$ 乘积仍保原 $j^m$。若原函数最初为不同分次之比，先按 R924 保留全部 $S$ 因子、$\rho_j$ 和真实同次化，再进入本节。

一般同次分式 $f=A/B$、$A,B\in R_m$ 在第一图表准确写成
$$
\boxed{f=\frac{A/J^m}{B/J^m},\qquad A/J^m,B/J^m\in W_{4m}\subset\mathcal A.}
\tag{27}
$$
对于原坐标恢复的实际乘积 recipes，逐个用(26)和(23)相乘，即得这两个306维多项式向量。不能把同次化时已有的 $S$ 零点省去；(27)只是同时除以同一个真实截面 $J^m$，保持整个原有理函数。

更一般地，给定 $N,D\in\mathcal A$、$D\ne0$，保存函数为有序对 $(N,D)$。加、乘、取逆和正整数幂都在这个分式对中准确执行；除法只交换非零分子分母，不先求一个大函数域逆元。可删除明确的共同标量多项式因子；不能仅因两个 norm 有相同因子就删除原分子分母在不同地方的零点。

### 5.2 第二图表的同一个函数

写 $N=\sum_i n_i(\xi)b_i$、$D=\sum_i d_i'(\xi)b_i$，选
$$
M\ge\max_i\{\deg n_i+d_i,\deg d_i'+d_i\}.
$$
由过滤基，$\xi^{-M}N,\xi^{-M}D$ 都在 $\mathcal A_\infty$，其坐标直接为
$$
\xi_\infty^{M-d_i}n_i(1/\xi_\infty),\qquad
\xi_\infty^{M-d_i}d_i'(1/\xi_\infty).
\tag{28}
$$
它们是真多项式，且两边用了同一 $M$，所以其比仍是原 $f$。对(27)取 $M=4m$，等价于同时除以 $J_0^m$。这给全部 $P_\infty$ 点的实际函数输入，没有依靠在原无穷单一分支上的数值猜其他 cusp 的值。

常数基始终保持原 $k\hookrightarrow k(Y)$。从 $\mathbf F_r$ 建出的 $b_i,\xi,J$ 在常数共轭下固定；原 $c\mapsto c^r$ 只作用系数。消费者的 $f^r$ 则按整环/分式的真正幂计算，包含变量的 Frobenius；原 Artin 置换仍按 R924 的独立标签执行。

## 6. 真正的零、极与交除子理想

令 $R=k[\xi]$，以(18)识别 $\mathcal A$ 的底模为 $R^{306}$。下述所有核和 Hermite 形式都在这个多项式环中计算，而非在有限 q-窗中猜理想。环结构和全部乘法矩阵已经由§3的全局身份给出。

### 6.1 一次完整核同时处理全部共零

设 $f=N/D\ne0$，$N,D\in\mathcal A$。$M_N,M_D$ 在 $k(\xi)$ 上可逆，因为 $\mathcal A$ 是整环。计算
$$
K_f=\{(x,y)\in R^{306}\oplus R^{306}:xM_D=yM_N\}.
\tag{29}
$$
它可由612×306矩阵 $\binom{M_D}{-M_N}$ 的完整多项式左核得到。具体可求带完整 unimodular 变换的 Hermite 形式，并保留所有零行对应的变换行；由于其非零行在分式域上线性独立，这些零行给全部多项式核，不只是一个有限指数子模。

两个投影的行模分别为
$$
I_+(f)=\{x\in\mathcal A:xD\in N\mathcal A\},\qquad
I_-(f)=\{y\in\mathcal A:yN\in D\mathcal A\}.
\tag{30}
$$
在第一图表任一闭点 $Q$ 的 DVR 中，写 $a=v_Q(N)$、$b=v_Q(D)$。条件 $xD=yN$ 给
$$
v_Q(I_+(f))=\max(a-b,0),\qquad
v_Q(I_-(f))=\max(b-a,0).
\tag{31}
$$
因为 $\mathcal A$ 是原光滑仿射曲线的 Dedekind 环，(31)确定整个理想。于是
$$
\boxed{I_+(f)=I_{\operatorname{zero}(f)|_{\operatorname{Spec}\mathcal A}},\qquad
I_-(f)=I_{\operatorname{pole}(f)|_{\operatorname{Spec}\mathcal A}}.}
\tag{32}
$$
两投影都单射且秩306；非零 $N,D$ 排除零投影。对投影分别作 Hermite 形式，得到完整零、极理想的306行多项式基。

这一步已经准确约去每个原点的共零，包含任意高重数。没有先把分母在约化域的零当成极点，也没有只约去标量 norm 的 gcd。若 $H_+,H_-$ 为所得完整行基，则
$$
\dim_k\mathcal A/I_\pm=\deg\det H_\pm
\tag{33}
$$
分别是第一图表真实零、极除子的次数。

### 6.2 理想乘积的有界行数实现

若 $I,J$ 的完整行基为 $H_I,H_J$，对 $J$ 的每条基元 $v_j$，$H_IM_{v_j}$ 是 $I v_j$ 的完整 $R$-基；这些行模之和恰为 $IJ$。逐个把这306行与当前306行 Hermite 基合并，保持整个和的 Hermite 形式即可。每一步至多612行、306列，不需一次保存306²条乘积行。理想幂用同一准确乘积和平方完成；任一步都保存完整模，而非按“看起来相同”的行数截断。

### 6.2.1 由全 norm 和包含认证理想积早停

设 $I,J\subset\mathcal A$ 为已认证的非零整理想，$v_1,\ldots,v_{306}$ 是 $J$ 的完整 $k[\xi]$ 基。算法按固定顺序构造
$$
K_j=\sum_{i=1}^j I v_i\subset IJ.
$$
每个 $Iv_i$ 都是实际 $\mathcal A$-理想，所以 $K_j$ 也是，且 Hermite 返回式和双包含给其完整多项式行模。令 $N(I)=\det H_I$ 取首一规范。由于 $\mathcal A$ 是已认证的 Dedekind 整环，有
$$
N(IJ)=N(I)N(J),\qquad N(IJ)\mid N(K_j).
$$
若在任一步实际得到完整多项式等式
$$
N(K_j)=N(I)N(J),
$$
则 $IJ/K_j$ 是有限 $k[\xi]$-模，且
$$
\dim_k(IJ/K_j)=\deg N(K_j)-\deg N(IJ)=0.
$$
故 $K_j=IJ$，可以立即结束后续生成块；此为整个理想相等的证书。若前面均不满足，继续到全部 306 块必得 $IJ$。实现必须记录实际读取的 `tested_basis_blocks`、可用的 `total_available_basis_blocks`、完整 norm 等式及包含理由，不能把提前结束记成已经执行所有生成块。

### 6.3 直接构造原有效交除子

仍使用 R883/R924 的同一循环呈现、同一输入 $y_1,y_p$ 和同一输出。令
$$
g=y_1-y_p^r\ne0,\qquad
\mathfrak I=I_-(y_1)\,I_-(y_p)^r.
$$
对第一图表每点，$v_Q(g)+\operatorname{pole}_Q(y_1)+r\operatorname{pole}_Q(y_p)\ge0$，所以
$$
\boxed{\mathfrak I_E=g\mathfrak I\subset\mathcal A}
\tag{34}
$$
恰为原有效交除子
$$
E=\operatorname{div}(g)+\operatorname{pole}(y_1)+r\operatorname{pole}(y_p)
\tag{35}
$$
在第一图表的理想。这里的 $r$ 次理想幂保留真实重数；它不是常数共轭或 Artin 平均。

若 $g=N/D$，$H_I$ 为 $\mathfrak I$ 的行基，计算完整核
$$
uH_IM_N=vM_D.
\tag{36}
$$
这仍是612×306多项式矩阵的核。由(34)，每个 $u\in R^{306}$ 都有唯一多项式 $v$；故完整核的 $u$ 投影为整个 $R^{306}$，其基矩阵为 unimodular。$v$ 投影准确给 $\mathfrak I_E$，再作 Hermite 形式即可。必须核 $u$ 投影确为全模及(36)的完整回代；若不通过，不得用一个少维图表理想代替原 $E$。

同一过程在 $\mathcal A_\infty$ 中给 $\mathfrak I_{E,\infty}$。后者只保 $\xi_\infty=0$ 的 primary 部分。于是完整次数核为
$$
\boxed{\deg\det H_E+
v_{\xi_\infty}(\det H_{E,\infty})
=\begin{cases}
2256+r d_F,&d_F<2256,\\
2256(r+1),&d_F\ge2256,
\end{cases}}
\tag{37}
$$
其中原 $d_F$ 仍由实际完整 $y_F$ 极除子读取。左边第二项已经按全部剩余域次数计重；不是只数原展开点。

## 7. 分块读取全部闭点与非约化长度

本节的有限对象以306行多项式模表示；不要求把一个次数六万以上的商展开成同样大小的全乘法矩阵。

### 7.1 完整支持，不能只用约分后的 norm

对 $h\in\mathcal A\setminus\{0\}$，
$$
N_{k(Y)/k(\xi)}(h)=\det M_h\in k[\xi]\setminus\{0\}.
\tag{38}
$$
因此函数 $N/D$ 的第一图表零极支集包含在 $\det M_N\det M_D$ 的所有素因子上。必须分别保两份支持；约分后的函数 norm 可能把不同原地方的相反赋值抵消，不能用它单独判定支持。若已经构造完整有效理想 $I$，则用 $\det H_I$ 的完整因式分解即可，它包含恰好那些有非零局部长度的基素点。

把 $F=\det H_I$ 首一化并分解为 $\prod_\pi\pi^{e_\pi}$。$F$ 湮灭 $\mathcal A/I$，因为 $H_I$ 的 adjugate 给该包含。因此可以按这个标量因式分解作完整 CRT 分块；对每一因子，
$$
I_\pi=I+(\pi^{e_\pi})\mathcal A
\tag{39}
$$
的商正是该 primary 块。两个完整理想基的堆叠及 Hermite 形式给(39)。多余的指数上界不丢点：每个 $Q|\pi$ 的局部长度至多 $e_\pi$，而 $v_Q(\pi)\ge1$。

每个商一直保存为 $R^{306}/\operatorname{row}(H)$。Hermite 余式或带变换的 Smith 形式给规范代表；元素乘法由(23)之后模 $H$ 约化，单位和常数嵌入均保留。其总系数长度是除子次数，而非该次数的平方或立方。

### 7.2 至多306维的残余支集代数

对一个 $\pi$，置 $k_\pi=k[\xi]/\pi$。把同一完整乘法矩阵模 $\pi$，再除以 $I$ 的实际像，得到
$$
B_\pi=\mathcal A/(I+\pi\mathcal A),
\qquad\dim_{k_\pi}B_\pi\le306.
\tag{40}
$$
在这个小代数中求 nilradical、约化商及全部 primitive idempotent，方法就是 R924 的实际 Frobenius/乘法分解。不能先假定其 étale：在 $\xi=0,\pm1,\pm3$ 的 ramified cusp 纤维中，它确实可能有非约化长度。

每个约化局部因子给实际剩余域 $\kappa(Q)$、固定嵌入 $k\to k_\pi\to\kappa(Q)$，以及
$$
d_Q=[\kappa(Q):k]=\deg(\pi)[\kappa(Q):k_\pi].
\tag{41}
$$
原 $\omega$ 的像由此嵌入决定。不得在做椭圆曲线迹之前独立换根，也不能把 $\mathbf F_r$ 的一个闭点在扩到 $\mathbf F_{r^2}$ 后仍当作同一未分裂点。

把(40)中的 primitive idempotent 提升到完整 $\mathcal A/I_\pi$。提升唯一；可迭代 $e\mapsto3e^2-2e^3$，每次把幂等误差提高到其平方的理想中，直至误差精确为零。原误差在有限代数的 nilradical 中，所以此过程有限终止。最后核全部幂等元互相正交、和为1，不能只保某个约化投影。

若提升为 $e_Q$，局部因子为
$$
\mathcal A/(I_\pi+(1-e_Q)\mathcal A).
\tag{42}
$$
其理想仍由306行多项式模给出；用其 Hermite 行列式次数求完整 $k$-维数 $\lambda_Q$。因为原局部环是 DVR，准确交重为
$$
\boxed{I(Q)=\lambda_Q/d_Q.}
\tag{43}
$$
核此商为正整数及 $\sum_Q\lambda_Q=\deg\det H_I$。这样读到任意高交重，不需要把整个商的每个乘法算子变成六万维矩阵。

第二图表仅对 $\pi=\xi_\infty$ 重复(39)–(43)，即得所有 $P_\infty$ 上的真实闭点和重数。

### 7.3 全局点标签、真实参数和共零后的值

对第一图表，$J$ 在整个开集为单位截面；原666条完整 $R_1$ 基 $F_i$ 的坐标 $F_i/J\in\mathcal A$ 给原很充足嵌入的实际射影坐标。在第二图表边界，用 $F_i/J_0$。它们在重叠处相差同一个非零标量，所以归一化后的完整射影坐标及原底域 Frobenius 轨道给可跨切割比较的实际点标签；相同次数或相同最小多项式不是相同原点的判据。

从(40)的剩余映射可把原最大理想 $\mathfrak q_Q\subset\mathcal A$ 写成完整多项式模：取剩余映射的全部核行提升，再加 $\pi\mathcal A$，作 Hermite 形式。必须核 $\dim_k\mathcal A/\mathfrak q_Q=d_Q$。用§6.2求 $\mathfrak q_Q^2$，实际选一条 $\varpi_Q\in\mathfrak q_Q\setminus\mathfrak q_Q^2$，它就是原 DVR 中的参数。ramified cusp 处不能以 $\pi(\xi)$ 自动替代它；后者可能有289阶零。

为了在 $Q$ 读取一个正则函数 $a/b$，先保其真实阶 $v_Q(a),v_Q(b)$。在 $\mathcal A/\mathfrak q_Q^M$ 中取 $M>\max(v_Q(a),v_Q(b))$，逐个约去相同的 $\varpi_Q$ 次幂，然后在实际 $\kappa(Q)$ 中相除首项。约除可解
$$
\varpi_Q^v x\equiv a\pmod{\mathfrak q_Q^M}
\tag{44}
$$
的完整多项式模方程；不同解的剩余首项相同。有限剩余域的系数域也可按 R924 的 $X^{\#\kappa(Q)}-X$ 唯一提升固定。

需要一个明确终止上界时，对整元素 $a$ 有
$$
v_Q(a)\le v_\pi\det M_a,
\tag{45}
$$
因为 $v_\pi\det M_a=\sum_{Q'|\pi}[\kappa(Q'):k_\pi]v_{Q'}(a)$。所以 $1+\max(v_\pi\det M_a,v_\pi\det M_b)$ 已足够作为 $M$。第二图表对 $\pi=\xi_\infty$ 同理。该界可保守但有限；不能以固定短 jet 失败就删掉高阶共零点。

### 7.4 同一原整环中的最大理想给精确点身份

固定原 $k=\mathbf F_{r^2}$（含同一个 $\omega$）、同一原 $\mathcal A$ 的有序完整整基及其已认证乘法。对第一图表的闭点 $Q$，§7.3 的剩余映射核给实际最大理想 $\mathfrak q_Q\subset\mathcal A$。它作为 $k[\xi]$ 的满秩子模具有唯一的首一上三角 Hermite 行基 $H_Q$。因此对同一图表中的两个闭点，
$$
Q=Q'\quad\Longleftrightarrow\quad
\mathfrak q_Q=\mathfrak q_{Q'}
\quad\Longleftrightarrow\quad H_Q=H_{Q'}.
$$
据此可用“原有序整基的身份、原常数字段表示、图表、完整 $H_Q$”的规范序列作为点键；hash 只是该完整序列的索引。若只存 hash，消费时遇到相同 hash 仍应比较完整 $H_Q$，不把 hash 无碰撞当数学假设。原常数字段的有限域系数按既定 $\omega$ 基编码。不同切割或不同残域生成元选择产生同一个核时，Hermite 基相同，所以这种点身份不依赖任意选择的残余域多项式。

第二图表同理用 $\mathcal A_\infty$ 的同一有序基及 $k[s]$ 最大理想，只保 $s=0$ 的点。它们全在 $\operatorname{Supp}(P_\infty)$，与第一图表的点集不交；图表标记即可避免重复计算，无须把两张图表中整个重叠区域都列出。

这种键之所以代表原点，依据是 R925 已证明的实际整环恒等 $\mathcal A=\Gamma(Y-\operatorname{Supp}(P_\infty),\mathcal O_Y)$，不是剩余域次数、剩余多项式或一个投影点集。剩余域中的原 $\omega$ 嵌入仍须按 §7.2 的实际映射保存；不能由这个键推断椭圆曲线输出值或迹。§7.3 的完整 666 个射影坐标继续提供独立的几何回代与跨不同整基比较入口。消费者在固定同一整基内对各切割求交、合并点和读取重数时，可以直接使用上述完整最大理想键。

## 8. 原 consumer 的完整接口和当前执行门

由§5–7得到现有消费者所需的准确 `function_divisor`、`poles`、`Divisor.list/degree/multiplicity`、`Q.degree/residue_field`、`valuation` 和 `reduce`。第一图表加第二图表的零纤维给全部原点，且所有比较都经§7.3的原射影坐标。

原 $F/P$ 的特征零完整认证、R924 的同次化和三个退化仍是前置输入。把它们构造为§5的分式对象后，直接使用 R883/R924 的原 $v=\xi^2-1$、$\varepsilon$、$(v+4)/v$、$\theta_{17}$、$d_{\rm new}$、Artin 顺序、双端点和常数反射；本篇没有改变其中任何一项。

对实际四组交除子，先按(37)核完整次数及有效性，再对每个闭点使用 R883 的原 $m_Q$、$k_Q=E(Q)-3m_Q$ 和原输出比值。分歧三挠点仍计入次数，只在真实乘6后消去；极点用原射影延拓；全迹仍是
$$
[6]\operatorname{Tr}_{\kappa(Q)/\mathbf F_{r^2}}P_Q
=\left[\frac{1-(-r)^{d_Q}}{(r+1)/6}\right]P_Q.
\tag{46}
$$
保留完整 $d_Q$ 和真实重数到最后，才在原5挠或7挠目标上约化，并交给原18×9与双轴读者。306维环或一个 norm 多项式本身不证明该 Artin 组合非零。

可执行阶段应分别留回执：原完整 $R_1$ 和 $\xi$；$J$ 及全部 colon；过滤基与全部权；每条所用完整乘法、两个图表和同一函数嵌入；所有零/极/交理想的完整多项式模核；所有基素因子、闭点、重数和实际剩余嵌入；最后原完整 shadow 读数。前一个阶段成功不替后一个阶段预填 PASS。

本篇将后续核、理想和局部支集的矩阵行列数限制在覆盖次数306或其固定倍数；总次数仍出现在一元多项式和有限模的系数长度中。矩阵 Hermite/Smith、因式分解、全部局部读数的实际时间还须由公开 Actions 支付；没有宣称高次数交除子因换了表示就已经便宜或已经完成。

### 原始来源和实现依据

- [R924](R924-original-section-divisor-algebras-and-shadow-interface.md)：原完整格、原 $Y$ 与三个退化、已付 $r=29$ 的原全核360及全部原映射身份；本篇(4)–(46)给新整环和消费算法的完整证明。
- [R882](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)、[R883](R883-original-relative-six-shadow-and-complete-boundary.md)：原 $\xi=y_s$、次数306、原全部 cusp/分支和同一完整交除子/迹公式。
- Kamal Khuri-Makdisi, *Linear algebra algorithms for divisors on an algebraic curve*, Math. Comp. 73 (2004), 333–357，[原文](https://arxiv.org/pdf/math/0105182)；*Asymptotically fast group operations on Jacobians of general curves*, Math. Comp. 76 (2007), 2213–2239，[原文](https://arxiv.org/pdf/math/0409209)，§1区分完整 RR 乘法表示与算术整环表示。本篇具体给出两者之间的原306维转换，不以一般 Jacobian 群算法替代实际点因子。
- Sage 官方 [Dense matrices over univariate polynomials over fields](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_polynomial_dense.html)：`hermite_form(transformation=True, include_zero_rows=True)` 给完整变换 $UA=H$；`minimal_kernel_basis` 返回整个多项式核，`is_minimal_kernel_basis` 除 rank 和零积外还核 saturation；`reduce` 的完整多项式余式保留原行模。本文数学要求是全部核/全模及完整返回式；若运行版本的具体接口不同，应调整实现并验证该语义，不能把分式域核误当未饱和的多项式核。


## 9. 首个公开完整环请求

`rank2-sha-original-y-affine-normalization.yml` 请求同固定Sage10.6镜像的r=29、q2453、batch64。`produce-original-y-colon-apery.py` 重用同原ys全核的W3投影，再核三条完整colon及所有W0–W8；`original_affine_multiplication.py` 核全部46971个真实基对，再按(25)给两张完整正规化图表。包装器先打印独立的Apéry回执，再打印完整双图表乘法回执；失败后不把后一阶段记成PASS。

root与两名独立审阅者已静态逐行核原J单位精度、全部2449项colon、真306基及2453输入到全Laurent窗口、完整乘法回代和图表权。这里只做AST/YAML等静态检查，实际数学仍只由公开Actions执行；目前未声明这个新任务成功。其余闭点、完整理想、原函数和原shadow接受门仍按§8逐项执行。

| 源文件 | SHA256 |
|---|---|
| `produce-original-y-colon-apery.py` | `a72b9e5c316fc7a8208e8c23a32236ae76a56d5a773ada315699fee0d04d1fc4` |
| `original_affine_multiplication.py` | `ff55083ab0e25d6b44991b64fa9cdc63d397842add1c474459e42986437e65a2` |
| `produce-original-y-affine-normalization.py` | `22b2a9566485c542f375e15c9b41ae05054124f2cd0f5efba71244a0f39d2ed3` |

首实际请求为[run44724912327](https://github.com/Rogerhu12/math-research-public/actions/runs/44724912327) / job136249752863 / source `fea36d7d86dc6229b23f5af13bd7ba53e0b362d1`，首请求时运行中；其完整成功回执现见§12。

## 10. 六个完整厚cusp纤维的实际读取门

状态：本说明的几何与代数形状已证明；对应实现只做了静态/语法检查，
尚未据此登记任何公开数学执行 PASS。

### 10.1. 同一个原覆盖及全部纤维

沿用 R883、R924、R925 的原 $Y=X_0(3468)$、
$\xi=y_s:Y\to X_0(12)\simeq\mathbf P^1$、次数306。
取 $k_0=\mathbf F_r$，$r=29,41$。
原 $X_0(12)$ 的六个 cusp 在这个坐标中是

$$
\xi=0,\ 1,\ -1,\ 3,\ -3,\ \infty.
$$

每个纤维有18个几何点：一个原有理 cusp 的分歧指数为289，
另外17个点的分歧指数为1。这可由 R883 的 $T$ cusp 阶289和1，
$Y\to X_0(867)$ 在每个 cusp 的指数2，以及 $T(\xi)$ 在六个显示值的局部阶2核定。
它也直接等于忘去 $17^2$ 结构时的 cusp 宽度比。

这17个简单点包括一个有理点和一个由 $\mathbf Q(\zeta_{17})$ 给出的16点 packet。
在两个原素位上，$29\bmod17=12$、$41\bmod17=7$ 都有阶16，
所以该 packet 是一个次数16的闭点。

因此每个完整纤维的有限代数准确为

$$
\boxed{k_0[\nu]/(\nu^{289})\ \times\ k_0\ \times\ \mathbf F_{r^{16}}.}\tag{1}
$$

这里的厚分量同构使用原光滑曲线在有理 cusp 的 DVR 及其真实参数；
不假定 $\xi-a$ 是那个参数。事实上在厚点它的阶是289。
六个完整纤维的 scheme 长度之和是1836，约化支集的几何点数是108，
在 $k_0$ 上有12个有理闭点和6个次数16闭点。
不能把这些三种计数混为一谈。

### 10.2. 全 Frobenius 的准确形状

令 $F$ 是整个306维代数上的实际 $r$ 次 Frobenius，按行向量约定表示。
在厚分量上，它把 $\nu^j$ 送至 $\nu^{rj}$，故

$$
\operatorname{rank}F
=17+1+\left\lfloor\frac{288}{r}\right\rfloor
=\begin{cases}27,&r=29,\\25,&r=41.\end{cases}
$$

因 $r^2>289$，$F^2$ 杀掉全部288维 nilradical，并且
$\operatorname{rank}F^2=18$。但是 $F^2$ 在次数16残域上仍有阶8，
所以它不是约化投影。真正的规范约化投影可取

$$
\boxed{P_{\rm red}=F^{16},\quad P_{\rm red}^2=P_{\rm red},
\quad\operatorname{rank}P_{\rm red}=18.}\tag{2}
$$

同样有 $F^{18}=F^2$。完整特征多项式与固定空间维数是

$$
\det(X-F)=X^{288}(X-1)^2(X^{16}-1),
$$
$$
\dim\ker(F^d-1)=2+\gcd(d,16)\qquad(d\ge1).\tag{3}
$$

其中次数16残域的特征多项式是 $X^{16}-1$，可由有限域正规基定理得到。
厚分量只贡献一个固定常数方向，其余288个特征根为零。
这些公式在实现中均用整个实际 Frobenius 算子检查，不由维数直接预填。

### 10.3. 真实厚局部代数的认证

先用完整固定代数 $\ker(F-1)$ 的实际乘法分裂三个 primitive idempotent，
再以(2)计算每个局部分量的约化域。必须实际得到

$$
(\text{局部长度},\text{剩余次数})=(289,1),(1,1),(16,16).
$$

在289维分量中，取完整 nilradical 的任意基。
因为原局部环是 DVR，某个基元 $\nu$ 必不在最大理想平方中。
程序通过全乘法算子的秩288找到这样的原参数，并准确验证

$$
1,\nu,\ldots,\nu^{288}\text{ 的秩为289},\qquad
\nu^{288}\ne0,\quad\nu^{289}=0.\tag{4}
$$

这完整认证(1)的厚分量，保留全部高阶信息。
只核 $\nu^{r^2}=0$ 或只核 nilradical 维数288均不够替代(4)。
每个参数向量保留在同一原图表的基坐标中，因而也给原局部参数的实际全局提升。

### 10.4. 同一全局曲线的全部点标签

第一图表使用 R925 的原 $J$，第二图表使用 $J_0=\xi^4J$。
完整666条原权二基 $F_i$ 在有限纤维的坐标是 $F_i/J$，
在无穷纤维的坐标是 $F_i/J_0$。
两者都先在整个有限代数中读取，不先投到约化支集。

为了形成闭点的规范标签，才使用(2)投到真实残域，
在固定的次数16 cyclotomic 域模型中对全部666个实际射影坐标归一化，
并对完整 $r$-Frobenius 轨道取规范代表。
全局线丛次数1224大于 $2g+1=1119$，故它很充足；
这些全部坐标区分原曲线的几何点。
实际还核18个原 $k_0$ 闭点标签互不重复。

标签基域是 $k_0$。后续原消费者扩到 $k=\mathbf F_{r^2}$ 时，
每个次数16闭点会分成两个次数8闭点；须按原 $\omega$ 嵌入使用 $r^2$ 轨道，
不能继续把完整 $r$ 轨道当作一个 $k$ 点。
全部未约化坐标仍与标签一起留在进程中。

### 10.5. 与完整 different 的核对

$\Gamma_0(12)$ 没有椭圆稳定子；在这些好素数处，忘去 $17^2$ 结构在非 cusp 开集上 étale。
六个厚 cusp 的指数289与 $r$ 互素，各贡献 different 次数288，
总数为1728，恰是

$$
(2g_Y-2)+2\cdot306=1116+612.
$$

所以原仿射整闭包相对 $k_0[\xi]$ 的判别式理想是

$$
\bigl(\xi(\xi^2-1)(\xi^2-9)\bigr)^{288}.
$$

这里全局几何证明不等于已经实际算出 trace Gram determinant。
本次代码读取的具体有限证据是六个真实完整局部代数及其全部点标签；
不把它扩写为四个大交除子或原 shadow 已计算。

实现：`original_ys_cusp_fibers.py`；
前端：`produce-original-y-cusp-fibers.py`。
前置输入为实际完整两图表正规化与同一666条原全局截面的环坐标。

## 11. 精确整环接口与新公开请求

`original_section_ring_embedding.py` 在完整W4的1225个Laurent项上将全部666条原M2/J读到同一306整基，并以同权反转给M2/J0。原map入口另核两个R917源的完整QQ205基、同有理饱和变换、全部共同M2/RR/S前缀；原三退化各j^m、F分母B2*S³和调用者原ω不变。此处返回的是同一原函数在两图表的分式，尚未把它的分母当作极除子。

`original_ys_divisor_ideal_tools.py` 只消费该真实整环。它使用完整多项式minimal kernel及明确检查饱和性的verifier；Hermite返回式加反向完整余式核两包含。§6.2.1的完整norm早停保全理想；零极、真实交理想与无穷s-primary都保全部共零/长度。根代理已亲读Sage官方kernel/Hermite接口定义；另由 `rank2-sha-original-polynomial-module-api.yml` 在固定Sage10.6镜像检查两原特征及其二次常数域的实际API语义，包含同秩但非饱和假核被拒和删零行后的完整变换。这个小检查只确认后端语义，不认证原曲线除子。

`rank2-sha-original-y-cusp-fibers.yml` 为新六纤维在同进程重建原完整格和全乘法表，再读取§10的六个306维真实纤维、全289局部幂基及666原射影标签。所有输出对象保在进程内，只打印来源/参数/hash与结论。root和两名独立审阅者已核代码/原窗口/两图表/真实单位/全部Frobenius门；本地仅AST/YAML静态检查。两项新请求均待实际回执，四大交除子/shadow尚未计算。

| 新源文件 | SHA256 |
|---|---|
| `original_section_ring_embedding.py` | `d43d5c31bf6b0ac69bbc80a532efbb458349299f6229c2dfa70f4b2952274687` |
| `original_ys_divisor_ideal_tools.py` | `661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7` |
| `original_ys_cusp_fibers.py` | `f52462aef8786928b5ad827b9351fee510273b5a3ae8c802201b95b790aea2cd` |
| `produce-original-y-cusp-fibers.py` | `3ee7a55cb4e90f23357ef8e5219c42cf95235b86703dbc3bfe19825e5981d313` |
| `check-original-polynomial-module-api.py` | `5180a0acfc0fa622540569f21f8fbd4bd41281e318a03230da621dd04f0d307a` |


## 12. 原306完整整环和两图表的实际回执

2026-11-20 11:17:46 UTC，公开 [run44724912327/job136249752863](https://github.com/Rogerhu12/math-research-public/actions/runs/44724912327/job/136249752863) 在 source `fea36d7d86dc6229b23f5af13bd7ba53e0b362d1` 完成。参数为 r=29、同原M2精度2453、乘法batch64、固定Sage10.6镜像；整个原Y格、ys、colon、306基和两图表在同一进程从原始公式重建，耗时592.378733806秒。root已读取完整日志并独立计算完整result和log的SHA256。

实际低阶维数及自由基权重为

| n | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| h_n | 1 | 2 | 68 | 360 | 666 |
| 新生成元数 | 1 | 0 | 65 | 226 | 14 |

总数306、权重总和864。这里 h2=68 是实际核的结果，不能由Riemann–Roch的下界54代入；14个权4生成元确实存在，所以先前保留到完整W8及2453输入精度是必要的。本项只认证r29，不外推r41。

从已有完整W3出发，三个新colon在全部2449个系数上依次得到：未知数/秩/核维数为720/652/68、136/134/2、4/3/1。所有完整核、两投影、同分式恒等回代均成功。实际单位不是默认第一基元本身；所选权0基元的标量为14，程序核了真实单位对每个基元的作用。

W0到W8的所有带权单项式均实际达到完整维数与秩，完整M4=J²W8有1890条基，全部2449系数已知并回代。全部46971个对称基乘积按真正权界核完，分布如下。

| 总权 | 乘积数 | 完整目标空间维数 |
|---|---:|---:|
| 0 | 1 | 1 |
| 2 | 65 | 68 |
| 3 | 226 | 360 |
| 4 | 2159 | 666 |
| 5 | 14690 | 972 |
| 6 | 26561 | 1278 |
| 7 | 3164 | 1584 |
| 8 | 105 | 1890 |

每个乘积都核完整全局零界，全部系数次数帽和反向权重变换均成功。因此本次已实际认证原A和原B的完整乘法及其真实单位。未把此事记为尖点局部分解、四大交除子或原shadow已经完成。

| 回执对象 | SHA256 |
|---|---|
| 完整最终result | `473e35bc9bdf73e488ad231fc51f54e49caea71ae1755035ddc1aedb6b37188c` |
| 完整中间Apéry result | `b6cc51a57019c59950017e19045d1db40d9d042e481c8e0c5c350de65f7b47f5` |
| 完整job日志 | `0208b18fff4bdace97173daf7bc43d2d165ee5e22e4e81818a028ef9eabcd913` |
| 完整乘法签名 | `5ce8e795af0de19ba3471f3a83e6202564f66fc527678dec09c4518a9e54aed8` |
| 原J坐标 | `0aed7bc402cc413558491a70605d80a5e4a4f9193ae972d3de4f0185ddd20120` |
| 完整Apéry坐标 | `37a12d2b35e086ea6746cdb5babb48393c14e7207bd49b6791605c5dc997e7f3` |
| 同原M4完整基 | `ef802e657d1c21cabd9a46283e9c3865ceae6cc22df8cc3faea202ba19736a8b` |
| producer | `22b2a9566485c542f375e15c9b41ae05054124f2cd0f5efba71244a0f39d2ed3` |
| colon源码 | `a72b9e5c316fc7a8208e8c23a32236ae76a56d5a773ada315699fee0d04d1fc4` |
| 完整乘法helper | `ff55083ab0e25d6b44991b64fa9cdc63d397842add1c474459e42986437e65a2` |

### 12.1. 固定Sage的多项式整核与Hermite语义

[run44726729229/job136255921243](https://github.com/Rogerhu12/math-research-public/actions/runs/44726729229/job/136255921243) 在 source `155a07fd16deb83bc20a98a84eac54e8ea17ae22`、2026-11-20 11:20:54 UTC 完成，耗时0.104388202秒。实际固定Sage10.6分别核r29、r41及常数扩张次数1、2：真正完整多项式minimal kernel通过饱和性验证；乘以变量后虽同秩且乘积为零的非饱和假核被拒；Hermite完整零行核通过；删零行所得2×3变换的完整返回与反向包含都通过。

result SHA256为 `ae4f08c8d1df87379823430b3b348a475bb1319f8e934553973e708868a68e12`；完整日志为 `d3e26108a8bb4995f26fb8ede58f79b974dec5f65b502703dd3e87346846f2db`。脚本/helper hash仍为§11所列 `5180a0ac…307a` / `661075ee…226d7`。这付清了所用后端的实际接口语义；原曲线真实理想及其全局值仍须以原输入另行通过。


## 13. 原参数、准确赋值及任意阶共零后的剩余值

本补充对应 `original_ys_local_value_tools.py`，只消费 R925 已认证的同一整环、完整最大理想和实际剩余映射。代码的本地状态仅为 AST/静态检查；所有数学执行仍须公开 Actions。它不自行构造另一条曲线、改变原常数嵌入或宣称已经计算椭圆迹。

### 13.1. 完整最大理想的幂就是原地方赋值条件

令 $\mathcal A$ 是 R925 的第一或第二原图表，$R=k[\xi]$ 或 $k[s]$，$Q$ 是其闭点，$\mathfrak q=\mathfrak q_Q$ 是原剩余映射 $\mathcal A\to\kappa(Q)$ 的完整核。由于 $\mathcal A$ 是 Dedekind 整环，对每个整元素 $a$ 和 $n\ge0$，
$$
a\in\mathfrak q^n\quad\Longleftrightarrow\quad v_Q(a)\ge n.
\tag{L1}
$$
其他地方的整性由 $a\in\mathcal A$ 已经保证。所有 $\mathfrak q^n$ 都用原理想乘法和完整 Hermite 行基表示；§6.2 的 norm 等式早停仍只在已证明整个理想相等时使用。

完整 $\mathfrak q/\mathfrak q^2$ 是一维 $\kappa(Q)$-空间，特别是非零。故 $\mathfrak q$ 的306条 $R$-基行中至少一条 $\varpi$ 不属于 $\mathfrak q^2$。实际核
$$
\varpi\in\mathfrak q,\qquad \varpi\notin\mathfrak q^2
\tag{L2}
$$
即证 $v_Q(\varpi)=1$，得到原 DVR 的真实参数。即使 $Q$ 是覆盖的289重 cusp，(L2)仍有效；算法不把基函数 $\pi(\xi)$ 的一个高阶零自动当参数。

### 13.2. Norm 提供有限终止界，完整理想成员关系给准确值

对非零整元素 $a$，由完整乘法矩阵 $M_a$ 的 Hermite 行模读取整个主理想 $(a)$，并取其首一 norm $N(a)\in R$。若基素多项式为 $\pi$，令
$$
e_\pi=v_\pi N(a),\qquad
f_Q=[\kappa(Q):k_\pi].
$$
原有限覆盖的 norm 赋值式给
$$
e_\pi=\sum_{Q'\mid\pi}
[\kappa(Q'):k_\pi]v_{Q'}(a).
\tag{L3}
$$
各项都非负，故
$$
0\le v_Q(a)\le\left\lfloor e_\pi/f_Q\right\rfloor.
\tag{L4}
$$
当实际剩余值不为0时，直接得 $v_Q(a)=0$。否则在(L4)的有限区间内，对完整理想 $\mathfrak q^n$ 的 Hermite 余式做二分判定，并最终实际核
$$
a\in\mathfrak q^v,\qquad a\notin\mathfrak q^{v+1}.
\tag{L5}
$$
这样得到准确 $v_Q(a)=v$；norm 只提供终止界，不能替代按原闭点的成员关系。代码的 cache 以 hash 分桶后继续比较完整元素，避免把 hash 的无碰撞性当数学假设。

### 13.3. 共零后的首项由完整多项式模方程唯一确定

给定非零 $a\in\mathcal A$，准确赋值为 $v>0$，取 $M=v+1$。在完整商 $\mathcal A/\mathfrak q^M$ 内逐步相乘并约化，得到 $\varpi^v$ 的准确代表 $p_v$。因为 $M>v$，
$$
v_Q(p_v)=v,
\qquad (p_v)+\mathfrak q^M=\mathfrak q^v.
\tag{L6}
$$
第二式可逐地方核：在 $Q$ 上取两赋值的较小者 $v$；在其他地方 $\mathfrak q^M$ 为单位理想。

令 $H_M$ 是 $\mathfrak q^M$ 的完整 $R$-行基。构造612×306多项式矩阵
$$
S=\begin{pmatrix}M_{p_v}\\H_M\end{pmatrix}.
\tag{L7}
$$
用完整 Hermite 变换 $H=US$，并核全部输入行对 $H$ 的余式为0，认证其与 $S$ 是同一整个多项式行模。算法额外要求
$$
H=H_{\mathfrak q^v},
\tag{L8}
$$
这直接核(L6)在同一原整基中的完整实现。随后以 $H$ 的首一上三角主元作准确多项式除法，解 $cH=a$。令 $(x,y)=cU$，则完整回代为
$$
xM_{p_v}+yH_M=a.
\tag{L9}
$$
从而 $p_vx\equiv a\pmod{\mathfrak q^M}$。所有系数都在 $R$ 内；没有在分式域求解后清分母冒充全模。

若 $x'$ 是另一解，则 $\varpi^v(x-x')\in\mathfrak q^M$，所以 $v_Q(x-x')\ge M-v=1$。故 $x$ 的剩余值与解的选择无关，恰是 $a/\varpi^v$ 的实际首项。由准确赋值 $v_Q(a)=v$，它非零，程序也实际验证非零。

### 13.4. 原分式读取和消费者接口

对同一原分式 $a/b$，先保持 $b\ne0$。若 $b(Q)\ne0$，直接在原 $\kappa(Q)$ 中取 $a(Q)/b(Q)$。否则读取准确 $v_a,v_b$：$v_a>v_b$ 时值为0；$v_a<v_b$ 时是原函数的真正极点，接口报带准确极阶的 `OriginalLocalPoleError`，留给消费者原有射影延拓。

当 $v_a=v_b=v>0$ 时，用同一个原参数 $\varpi$、同一个完整 $\mathfrak q^{v+1}$ 和同一个(L7)同时解两个目标 $a,b$。各自首项为 $\bar x_a,\bar x_b\ne0$，得到
$$
(a/b)(Q)=\bar x_a/\bar x_b\in\kappa(Q).
\tag{L10}
$$
因此任意高共同零阶都会被准确消去；不存在固定短 jet 失败就删除原点的路径。原 $k\hookrightarrow\kappa(Q)$ 的实际嵌入沿用闭点 helper，入口重新检查原常数域生成元的像；这固定了原 $\omega$，不会独立更换其根。

可用接口为 `OriginalAffineLocalReader(engine, original_basis_identity=None)`，方法 `uniformizer(point)`、`valuation(point,a)`、`fraction_valuation(point,(a,b))`、`leading_coefficient(point,a)` 和 `reduce_fraction(point,(a,b))`。同一原 engine 可直接消费；若使用另一个操作适配器对象，必须给完全相同的原有序整基身份，并比较原最大理想完整矩阵。两张图表分别调用各自 reader，第二图表仍只消费 $s=0$。

此层把 R925 的地方求值入口做成有限多项式模算法。后续消费者仍须保原全部 $m_Q,k_Q$、原常数反射和 Artin 顺序、原射影极点规则及完整椭圆曲线迹；局部值接口本身不推断任何 shadow 非零。


### 13.5. 完整剩余域和原最大理想的实现认证

`original_ys_closed_point_tools.py` 实现§7的全部基素因子、完整primary块、实际闭点、剩余映射和原最大理想。root已全文审阅，另由global独审；局部值层经deep独审。这里给两个不能省略的算法细节。

令B为(40)的真实小代数，维数D≤306，底域大小q≥29。实际q次幂算子F满足F²杀死全部nilradical，因为q²>D；其像U恰为唯一有限étale系数子代数。**F²本身一般不是投影。** 在U的全基中读F²限制的可逆矩阵T，若C为F²全行在U中的坐标，则实际约化投影是P=C T⁻¹ U。代码核P²=P、rank(P)=dim(U)、P F²=F² P=F²及原单位返回。F首先由实际p次幂矩阵及完整半线性复合得到，原常数嵌入不变。

完整固定代数ker(F−1)为kπ的有限直积。逐个使用其全部基元的真实乘法矩阵，按全部线性特征因子分裂，得到所有primitive idempotent；不枚举可能很大的整个kπ。每个实际剩余因子中，按Frobenius避开全部最大真子域得到生成元α，再实际核完整幂基满秩、最小多项式不可约及全部原环基到该残域的映射。选择α只改变原残域的内部坐标；多项式商与原生有限域的正反同构在生成元和原底域生成元上均回代，原ω像沿原嵌入保留。Sage官方 [field_extension接口](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_quotient_ring.html#sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing_domain.field_extension) 明确给出域、商到域、域到商三个返回对象；固定版本的实际使用仍由新原输入公开门核验。

对完整norm中π的指数e，π^e湮灭整个primary商，所以小纤维幂等元的初始误差在(π)内，经e↦3e²−2e³至多ceil(log2(e))次必变成精确零。程序检查完整误差为零才接受，之后构造全部局部primary理想并按真实norm次数读重数；所有分量总长必须返回原理想长度。原点身份用完整最大理想HNF，重复hash后继续比较完整矩阵。

| 新源文件 | SHA256 |
|---|---|
| `original_ys_closed_point_tools.py` | `705edc3584e74d295473940178282ff734c765a73dfbd2789ce74c2a32ed561a` |
| `original_ys_local_value_tools.py` | `a954fdaf928bda3d731ecd88eecf6d418aa11bd77d7f17f03dde1683a9f3a21b` |

本节完整证明与源码已接入；没有把静审写成实际原闭点、共同零首项或原shadow的计算PASS。

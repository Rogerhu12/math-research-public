# R620 — 全原来源的准确带权 Hilbert 函数与十三阶边界 Smith 窗

日期：2026-11-15。**状态：已证明。**

本篇继续 R612 的同一个完整有限目标 $\mathcal C_p$。
对整个原 $\mathcal W_D$，带权核不再只由一个理想描述：
以下给出其准确维数、全部初始系数空间、同帽整基和实际单位 Smith 因子的准确数目。
核心是约束数每一普通 $t$ 阶减六，而新来源列数每阶至多减一，
故整个消元只有一个转换点。原 $q_n$ 的全部高尾由后续真实列逐阶支付。

进一步，在最高原 $t$ 帽距 $s-13$ 不超过十二的边界窗，
整个模 $p$ 核就是实际 $t^{s-13}$ 尾列。
这些列的首 Bockstein 在原十三阶低带上单射，
因此这个**完整大目标**的全部非单位 Smith 因子恰为 $p$。
原 $P_{134}/U_0$、charge 四十及 $\epsilon^6=w\Upsilon$ 均保留。

本篇不计算旧三块的 $d_2$。
R597 同一个 $R$ 的剩余前两块 forcing 仍未判为非零；
也没有由本篇给任何新增来源赋中央零。

## 1. 同一个有限来源与完整物理矩阵

保
$$
p=6s-1>101,\qquad 0\le D<p,\qquad n_0=s-13,\qquad m=p-78=6n_0-1.
\tag{1}
$$
仍取
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^n q_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=\frac{\{t h_7\}^{A_n}(t-1)^{B_n}}{d^{C_n}},
\quad h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4,\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{2}
$$
定义每个电荷的最大普通首阶
$$
\boxed{b_n=A_n+e_{n+1}=f_n-2A_n-B_n+C_n.}
\tag{3}
$$
原来源的一组重排整基是
$$
C_{n,r}=Y^nq_n(t)t^{r-A_n},
\qquad A_n\le r\le b_n.
\tag{4}
$$
这只是重排原列，不增加任何角或次数帽。

完整评价仍为
$$
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon}),\qquad
a\in\mathcal O^\times,\quad \epsilon=w^s/p,
\tag{5}
$$
其中 $t=\tau_0w+O(w^2)$、$\tau_0\in\mathcal O^\times$，
$g(0)=1$，全部普通高尾和 $P_{134}$ 均是原对象。
目标是 R607/R612 的
$$
\mathcal C_p=
\bigoplus_{0\le j<ps}\mathcal O\,p^{-\lfloor6j/p\rfloor}w^j
$$
及其准确呈示
$$
\mathcal O[w,\epsilon,\Upsilon]/
(w^s-p\epsilon,\epsilon^6-w\Upsilon,
w^{s-1}\epsilon^5-p\Upsilon,\Upsilon^s).
\tag{6}
$$
记此实际整矩阵为 $M_D^{\mathcal C}$。
R612 已支付 (5) 对每条原列的整性，而不只支付来源格的整性。

令
$$
I_m(t,v)=\langle t^r v^h:6r+h\ge m\rangle,\qquad v=Y-1.
$$
R612 的完整坐标运输准确给
$$
\boxed{
\ker\overline M_D^{\mathcal C}
=\{\bar P\in\overline{\mathcal W}_D:
\bar P(t,1+v)\in I_m(t,v)\}.}
\tag{7}
$$
在原点 $d$ 是单位，故 (7) 与乘回原 $d^{C_D}$ 的版本相同。
(7) 已保 $w^{13}$ 的准确权 $78$；
不能把阈值改为 $p$。

## 2. 每阶的真实列与唯一转换点

对 $r\ge0$，置
$$
\rho(r)=\min\{n\ge0:b_n\ge r\},
$$
$$
I_r=\{0\le n\le D:A_n\le r\le b_n\},
\qquad m_r=|I_r|,
\qquad h_r=(m-6r)_+.
\tag{8}
$$
若 $I_r$ 非空，它是准确连续区间
$$
\boxed{I_r=[\rho(r),\,\min(D,4r+2)]\cap\mathbf Z.}
\tag{9}
$$
因此 $m_r$ 完全是可直接计算的原列数。
原来源总维数为
$$
N_D=\sum_r m_r=\sum_{n=0}^D(e_{n+1}+1).
\tag{10}
$$

**引理 1。** $b_n$ 严格递增，且
$$
b_{n+12}=b_n+50,
$$
$$
(b_0,\ldots,b_{12})=(4,8,13,15,21,24,30,32,37,41,47,48,54).
\tag{11}
$$
其十二个循环增量是
$$
(4,5,2,6,3,6,2,5,4,6,1,6).
$$
故
$$
\rho(r+1)-\rho(r)\in\{0,1\},\qquad
\boxed{m_{r+1}\ge m_r-1.}
\tag{12}
$$

**证明。** (11) 由 (2)–(3) 按十二余类计算。
严格递增的整数序列在相邻两个整数阈值之间至多失去一个指标。
(9) 的上端随 $r$ 不减，而下端至多加一，得到 (12)。
这里不要求每个 $b$ 增量至少为二；其中确有一个增量为一。证毕。

当 $h_r>0$ 时，$h_{r+1}=\max(0,h_r-6)$。
结合 (12)，一旦 $h_r\le m_r$，
以后每阶仍有 $h_{r'}\le m_{r'}$。
因此不存在“先有自由列、稍后又出现列数不足”的第二转换点。

若核非零，定义
$$
r_*=\min\{r:h_r<m_r\}.
\tag{13}
$$
若此集合为空，以下核为零。
另外
$$
m_r-1\le b_D-r\quad(0\le r\le b_D),
\tag{14}
$$
因为 $m_r$ 个不同整数 $b_n$ 都位于 $[r,b_D]$。
所以 $h_{b_D}\ge1$ 时，
$h_r\ge1+6(b_D-r)\ge m_r$ 对全部 $r$ 成立。
这说明自由列一旦存在，必有 $h_{b_D}=0$；
于是所有有约束的目标阶都不超过 $b_D$。
这一步排除了在原列最大首阶以后由 $q_n$ 高尾产生隐藏约束的可能。

## 3. 原角 jet 矩阵的完整整消元

先在固定环 $\mathbf Z[1/7]$ 上形成
$$
\mathcal T_m=\mathbf Z[1/7][t,v]/I_m(t,v),
\qquad
E_m:P\longmapsto P(t,1+v).
\tag{15}
$$
$d=1+8t$ 在该有限环中可逆。
每条 (4) 在 $t^r$ 的首系数为
$$
\chi_n(1+v)^n,\qquad \chi_n=7^{A_n}(-1)^{B_n}.
\tag{16}
$$
故第 $r$ 个对角块准确为
$$
\bigl(\chi_n\binom nh\bigr)_
{0\le h<h_r,\ n\in I_r}.
\tag{17}
$$

对任何连续电荷 $n=c,c+1,\ldots,c+q-1$，
$$
\boxed{
\det\bigl(\binom{c+j}{i}\bigr)_{0\le i,j<q}=1.}
\tag{18}
$$
这可由逐列差分
$\binom{n+1}{i}-\binom ni=\binom n{i-1}$ 归纳证明。
因此 (17) 的前 $\mu_r=\min(m_r,h_r)$ 行及前 $\mu_r$ 个实际电荷，
组成行列式 $\prod\chi_n$ 的整单位块。
不需要把非连续电荷差的可逆性当作额外假设。

**定理 1（完整核与秩）。**
$$
\boxed{
\begin{aligned}
K_D(p)&:=\dim_k\ker\overline M_D^{\mathcal C}
=\sum_{r=0}^{b_D}(m_r-h_r)_+,\\
R_D(p)&:=\operatorname{rank}_k\overline M_D^{\mathcal C}
=\sum_{r=0}^{b_D}\min(m_r,h_r)
=N_D-K_D(p).
\end{aligned}}
\tag{19}
$$
而且 (15) 在 $\mathbf Z[1/7]$ 上的核、像和余核均自由，
其非零 Smith 因子全部为单位。

**证明。** 按 $t$ 阶从小到大处理真实来源系数。

在 $r<r_*$ 时，$h_r\ge m_r$。
此前没有自由来源系数；在核方程中，(18) 迫本阶全部 $m_r$ 个新系数为零。
其余 $h_r-m_r$ 行不增加新的来源关系。
这不是假设高尾不存在：此前来源系数已经整归零，
因而其全部高尾也确实为零。

在 $r\ge r_*$ 且 $h_r>0$ 时，$h_r\le m_r$。
将本阶最后 $m_r-h_r$ 个实际电荷系数作为自由坐标。
此前自由列和本阶自由坐标在第 $r$ 阶产生的全部 $h_r$ 个值已知；
用 (18) 的前 $h_r$ 个原列一次整解，恰好消去这些值。
先前列的 $q_n$ 高尾全部进入这一右端。
本次使用的是 (4) 中首阶恰为 $r$ 的原列，因此不改变任何更低阶。

唯一转换点保证此过程以后不会缺列。
当 $h_r=0$ 时，该阶及其后的所有实际来源坐标自由。
引理1后的观察保证：有自由列时，整个约束窗口已在 $b_D$ 前结束。
于是每个显示自由坐标都延拓为一个完整同帽来源，而不是只解局部系数。

这给出恰有 $\sum(m_r-h_r)_+$ 个自由核坐标，
且每个核元素由这些坐标唯一确定。
另一方面，把每阶前 $\mu_r$ 个电荷列及前 $\mu_r$ 行合在一起，
得到块下三角方阵，其对角块为 (18) 乘 (16)。
其行列式恰是若干 $\chi_n$ 的乘积，是 $\mathbf Z[1/7]$ 单位。
因此像和余核也均为自由直和因子，秩为所列 $R_D(p)$。
最后通过 (7) 得到实际物理矩阵的 (19)。证毕。

这里 (15) 的整饱和与 $M_D^{\mathcal C}$ 的整饱和是不同断言。
对实际物理矩阵，(19) 准确给出的是
$$
\boxed{\text{单位 Smith 因子的数目恰为 }R_D(p).}
\tag{20}
$$
余下 $K_D(p)$ 个来源方向可能产生非单位因子或特征零核，
尚不能仅由 (15) 的整消元分类。

## 4. 全部初始系数、实际整提升与高度成本

取 (13) 存在的情形。
定理1同时给
$$
\boxed{t^{r_*}\mid P\quad
\text{对每个 }P\in\ker E_m.}
\tag{21}
$$
这个全局 $t$ 下界是锐的。
更完整地，在全局 $t$ 过滤的第 $r$ 个分次层，真实核的初始多项式空间准确为
$$
\boxed{
t^rY^{\rho(r)}(Y-1)^{h_r}
\mathbf Z[1/7][Y]_{\le m_r-h_r-1}}
\quad(m_r>h_r).
\tag{22}
$$
其他阶为零。

确实，本阶所有首项是
$t^rY^{\rho(r)}\mathbf Z[1/7][Y]_{\le m_r-1}$；
在 $Y=1$ 消到 $h_r$ 恰给 (22)。
定理1的后续整解说明 (22) 中每一项都能延拓，
而不只是一份必要的环境空间。
取第一个自由坐标便得到 $t$ 阶恰为 $r_*$ 的真实来源。

特别，每个 $\ker\overline M_D^{\mathcal C}$ 元素都有
一个保持全部十九角、原 $q_n$ 和原次数帽的整提升，
该提升还**准确**满足 $E_m(P)=0$。
这些提升组成有限自由格，约化满射到实际模 $p$ 核。
它们只为下一 Bockstein 固定了合法基准；
没有使其物理评价自动被 $p^2$ 整除。

本构造也不给提升引入随 $p$ 增长的新分母素数：
可取核基的全部坐标在 $\mathbf Z[1/7]$ 中。
还存在绝对常数 $C$，使非空核的一组上述基满足
$$
\boxed{
\text{共同分母}\mid7^{C(D+1)^2},\qquad
\max|\text{来源坐标}|\le \exp(C(D+1)^2).}
\tag{23}
$$
理由如下。非空核迫 $m\le6b_D$，所以整解只经过 $O(D+1)$ 个普通阶。
$q_n/t^{A_n}$ 到这些阶的整数系数由 (2) 的固定因子展开给出
$\exp(O(D+1))$ 界。
(18) 的逆可分成移位 Pascal 矩阵及普通 Pascal 矩阵之逆，
其整数系数同样为 $\exp(O(D+1))$；
再除 (16) 时每一步只增加至多 $A_D$ 个七分母。
逐阶右端是至多 $N_D=O((D+1)^2)$ 项之和，
因此 $O(D+1)$ 步给 (23)。
这只是该显示实际提升的成本，
不是把不连续子式的行号换成全局真饱和旗标成本。

(19) 也恢复 R612 的准确单射门
$$
K_D(p)=0\quad\Longleftrightarrow\quad p>6(b_D+13).
\tag{24}
$$
反向的实际见证仍是最高原列的 $t^{b_D}$ 首项；
本篇的新内容是门内全部核及真实单位数，而非再次登记 (24)。

## 5. 全 D/p 主阶的准确分段函数

令 $D\to\infty$、$p/D\to\alpha$，并保 (1)，所以 $\alpha\ge1$。
由 (3)、(9)，一致有
$$
N_D=\frac{47}{24}D^2+O(D),\qquad
b_n=\frac{25}{6}n+O(1),
$$
$$
m_r=D\left(\min(1,4x)-\frac{6x}{25}\right)_++O(1),
\quad x=r/D,
$$
$$
h_r=D(\alpha-6x)_++O(1).
\tag{25}
$$
代入准确求和 (19)，得到
$$
\boxed{R_D(p)=D^2\mathcal R(\alpha)+o(D^2),\qquad
K_D(p)=D^2\left(\frac{47}{24}-\mathcal R(\alpha)\right)+o(D^2),}
\tag{26}
$$
其中
$$
\boxed{
\mathcal R(\alpha)=
\begin{cases}
\displaystyle\frac{47\alpha^2}{1464},
&1\le\alpha\le61/25,\\[4pt]
\displaystyle\frac{-\alpha^2+50\alpha-61}{288},
&61/25\le\alpha\le25,\\[4pt]
\displaystyle\frac{47}{24},&\alpha\ge25 .
\end{cases}}
\tag{27}
$$
若 $p=\alpha D+O(1)$ 且 $\alpha$ 位于固定有界范围，余项为 $O(D)$。

**计算。** $m(x)$ 在 $x=1/4$ 换斜率。
当 $\alpha\le61/25$ 时，唯一交点是
$x_*=25\alpha/244\le1/4$；
在此前积 $m(x)$、此后至 $\alpha/6$ 积 $\alpha-6x$，
得到第一行。
当 $61/25\le\alpha\le25$ 时，
$x_*=25(\alpha-1)/144$ 位于 $[1/4,25/6]$。
核面积是两块三角形之和
$$
\frac{(25-\alpha)^2}{7200}
+\frac{(25-\alpha)^2}{300}
=\frac{(25-\alpha)^2}{288},
$$
从 $47/24$ 减去它给第二行。
$\alpha\ge25$ 时用 (24) 或取零面积。证毕。

在原连接常用的 $f_D<p$ 范围，极限有 $\alpha\ge9/2$，
故只需 (27) 的后两段。
这些系数描述的是同一个完整有限物理矩阵的单位容量；
并未把它转成旧三块的首像缺陷或中央非零。

## 6. 十三阶边界窗：整个模 p 核就是原尾列

以下再假设
$$
\boxed{0\le u:=b_D-n_0\le12.}
\tag{28}
$$
由 (11)，任意四个连续 $b$ 增量之和至少为十六。
因此区间 $[b_D-13,b_D]$ 中至多有四个 $b_n$。
特别
$$
m_{n_0-1}\le4,\qquad h_{n_0-1}=5.
\tag{29}
$$
由 (12)，对 $r<n_0-1$ 有
$m_r\le4+(n_0-1-r)$，而 $h_r=5+6(n_0-1-r)$。
所以之前每阶均无自由坐标。
从 $r=n_0$ 起 $h_r=0$。
定理1遂给准确整识别
$$
\boxed{
\ker E_m=\mathcal W_D^{(n_0)}
:=\{P\in\mathcal W_D:t^{n_0}\mid P\}.}
\tag{30}
$$

当前范围内 $n_0\ge A_D$。
对 $D\ge2$，这是
$n_0\ge b_D-12=A_D+e_{D+1}-12>A_D$
及 $e_{D+1}\ge13$；
$D=0,1$ 则直接由 $n_0\ge5$ 核定。
故 (30) 的实际整基就是
$$
\boxed{
C_{n,n_0+j},\qquad
0\le j\le u,\quad b_n\ge n_0+j.}
\tag{31}
$$
令
$$
m_j^\circ=\#\{n\le D:b_n\ge n_0+j\}\le4,\qquad
K=\sum_{j=0}^{u}m_j^\circ=K_D(p).
\tag{32}
$$
每个集合都是原连续电荷的尾区间。

## 7. 原完整首 Bockstein 在低十三阶中单射

对 (30) 中的实际 $P$，写 $P=t^{n_0}\widetilde P$。
这是计算同一个原列的商，不把 $\widetilde P$ 当新增来源。
由 $n_0+13=s$ 及原 $w^s=p\epsilon$，(5) 给准确恒等
$$
\boxed{
\frac{\Phi(P)}p=
U_{\mathcal C}\epsilon\,
\widetilde P(t(w),g(w)e^{a\epsilon}),}
$$
$$
U_{\mathcal C}=c_*U_0(w)e^{40a\epsilon}
                    (t(w)/w)^{n_0}\in\mathcal C_p^\times .
\tag{33}
$$
右端确实整。
(31) 除去共同 $t^{n_0}$ 后，每列的普通部分是
$$
t^j h_7^{A_n}(t-1)^{B_n}d^{-C_n},
$$
不含负 $t$ 幂。
R612 的同一 regularized 范数证明对这些固定因子仍适用，
给其在 $\mathcal C_p$ 内的整性；
原单位及其逆也完整保留。

所有原 $\overline M_D^{\mathcal C}$ 像都在
$w^{13}\overline{\mathcal C}_p$ 中。
乘完整单位 $\overline U_{\mathcal C}^{-1}$ 后仍在该理想中。
因此读原标准基里
$$
w^j\epsilon^{h+1},\qquad
0\le j\le u\le12,\quad
0\le h<m_j^\circ\le4
\tag{34}
$$
的系数，全部杀掉原模 $p$ 像。

(34) 是真正合法行：
$\epsilon$ 次数至多四，$j<s$，
并且 $6j+h+1\le76<p$。
没有将 $\epsilon^6=w\Upsilon$ 当零。
在 (6) 的标准基中，乘 $w^{13}$ 不能产生这些普通 $w$ 阶小于十三、
$\Upsilon$ 次数为零且 $\epsilon$ 次数至多四的单项式。

按 $j$ 排列尾列 (31)。
(33) 在 (34) 上的矩阵按普通阶为块下三角；
第 $j$ 个对角块准确为
$$
\boxed{
\left(\chi_n\tau_0^j\frac{(an)^h}{h!}\right)_
{0\le h<m_j^\circ,\ b_n\ge n_0+j}.}
\tag{35}
$$
$g(0)=1$，而所有 $q_n$ 和换参的更高普通项只进入后续块。
连续电荷不同，$m_j^\circ\le4$，所以 (35) 是单位 Vandermonde 块。
原 $a,\tau_0,\chi_n$ 也全部为单位。

因此原实际首 Bockstein
$$
\beta_{\mathcal C}:\ker\overline M_D^{\mathcal C}
\longrightarrow\operatorname{coker}\overline M_D^{\mathcal C},
\qquad
\bar P\longmapsto[\overline{\Phi(P)/p}]
\tag{36}
$$
在 (28) 中单射。
这次注入确实经过原像的余核：
显示行 (34) 已杀掉全部原模 $p$ 像，
不只是证明 $\Phi(P)/p$ 作为环境向量非零。

**定理 2（完整大目标的准确 Smith 形式）。**
在 (1)、(28) 下，
$$
\boxed{
M_D^{\mathcal C}
\text{ 有 }N_D-K\text{ 个单位因子、}
K\text{ 个恰为 }p\text{ 的因子，且没有零列因子。}}
\tag{37}
$$
相应整余核的自由秩为 $ps-N_D$。
原 $P_{134}/U_0$、十三阶、charge 四十均未改变。

**证明。** 定理1已给模 $p$ 核维数 $K$ 和单位数 $N_D-K$。
对有限自由整矩阵，首 Bockstein 在这个核上单射，
准确排除所有赋值至少为二的 Smith 因子及特征零核。
(36) 支付了这一步，得到 (37)。证毕。

## 8. 原旧截止、真前缀和完整中央保持

(19)、(27)、(37) 全属于 R607/R612 的同一个完整 $\mathcal C_p$。
旧 $M=c_*U_0m_{13}J$ 是另一个真实截断。
特别 (34) 可以读到 $\epsilon^3,\epsilon^4$，
它们不都在旧三块中。
故 (36) 不能不经原投影就当作旧 $d_2$ 的单射。

同样，(7) 的加权坐标变换保持权 $(6,1)$ 的理想，
却不保持任意按普通物理 $w$ 次数截取的前缀：
$v$ 的像同时含 $a\epsilon$ 和 $g(w)-1$。
因此不能将 (19) 的不连续实际行集直接换成
每个真饱和层的行集，或据 (23) 宣称全局 Bost 主成本已经改善。

R597 的指定 $P+pR+p^2T$ 仍必须在旧截止内保同一个 $R$、
完整两条十三行、两块实际续段和下一位。
此前实际 Euler 列消去第三尾后留下的第二块 $B$ 倍数，
尚未由本篇判为原像或非零余类。
原三条完整中央条件也仍只属于已经付清身份的固定来源，
未传播到本篇的核基或任意乘积。

## 依赖

- [R612](R612-original-full-source-weighted-kernel-and-fixed-nodal-exit.md)：
  全原来源的整性、完整加权核、实际 $w^{13}/U_0$ 运输及准确单射门。
- [R607](R607-original-integral-target-and-mixed-schur-decomposition.md)：
  $\mathcal C_p$ 的整呈示、标准基和真正混合边界。
- [R434](R434-original-angular-high-coordinates-and-carry-unit-schur-transport.md)：
  原 $\mathscr R$、$g$、$t$、Gaussian 常数及固定高尾规范。
- [R597](R597-original-nodal-critical-lift-and-complete-low-ell-second-class.md)：
  旧截止内同一个修正和完整第二类的准确范围。

本篇为全参数有限整消元与物理 Bockstein 证明；
没有新增素数扫描，没有以来源饱和替代物理余核。

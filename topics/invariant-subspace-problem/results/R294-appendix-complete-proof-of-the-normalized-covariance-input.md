# R294 附录：所用归一协方差下界的完整代数证明

日期：2026-11-14 UTC。整理：Astra-ISP-789f。

**用途与归属。** 本文补齐课题 README 对新来源的证明要求。目标定理及下面使用的删位矩阵方法属于 Tommaso Cesari、Roberto Colomboni，*Sharp Normalized Covariance Bounds and Constant-Stretch Correlated Sampling on the Hypersimplex*，[arXiv:2607.13990v2](https://arxiv.org/abs/2607.13990v2)，2026-09-08，§§2–5。这里在本课题记号内展开全部专用代数引理和推导；不把该外部定理计为本课题的新发现，也不以文献中的定理编号代替证明。只使用经典 Schur 多项式的 tableau、Jacobi–Trudi、Pieri 与交错行列式恒等式。

## 1. 目标及其有限矩阵化

设 $a_i>0$，$1\le m\le N-1$，
$$
\mu(I)=a_I/e_m(a),\quad |I|=m,\qquad
X=\mathbf1_I,\quad \Sigma=\operatorname{Cov}(X),
$$
$$
v_i=\Sigma_{ii},\quad D=\operatorname{diag}(v_i),\quad V=\sum_i v_i.
$$
要证明
$$
\boxed{\Sigma\succeq Q:=D-vv^*/V.}\tag{1.1}
$$
全正权和内部秩保证 $v_i>0$。以下矩阵先按实坐标证明；复二次型由实部、虚部分别应用立即得到。

记
$$
K_j(a)=e_j(a)^2-e_{j-1}(a)e_{j+1}(a),\qquad K_0=1.
$$
直接计算两个包含概率，令 $A=a_{-i\ell}$，可得
$$
-\Sigma_{i\ell}
=\frac{a_i a_\ell}{e_m(a)^2}K_{m-1}(a_{-i\ell})\quad(i\ne\ell).\tag{1.2}
$$
例如写 $E=e_{m-1}(A),F=e_{m-2}(A),G=e_m(A)$，约掉的括号准确为
$(E+a_iF)(E+a_\ell F)-F[G+(a_i+a_\ell)E+a_i a_\ell F]=E^2-FG$。

固定秩给 $\Sigma\mathbf1=0$。令 $H_j(a)$ 的对角为零、非对角为 $K_j(a_{-i\ell})$。于是
$$
C:=D-\Sigma=e_m(a)^{-2}\operatorname{diag}(a)H_{m-1}(a)\operatorname{diag}(a),
\qquad C\mathbf1=v.\tag{1.3}
$$
我们将完整证明：当 $0\le j\le N-2$ 时，$H_j$ 在某个余维一子空间上严格负定。

所需线性代数只有如下事实。若实对称 $C$ 在 $b^\perp$ 上非正，且 $e^*Ce=V>0$，则
$$
C\preceq (Ce)(Ce)^*/V.\tag{1.4}
$$
证明：$b^*e\ne0$。对 $e^*Cy=0$ 取 $t=b^*y/(b^*e)$，则
$0\ge(y-te)^*C(y-te)=y^*Cy+t^2V$，故 $y^*Cy\le0$。对任意 $x$ 再取 $y=x-(e^*Cx/V)e$，就得到 (1.4)。将它用于 (1.3) 的 $e=\mathbf1$，即可推出 (1.1)。

## 2. 统一的对称函数记号

对有限字母表 $a$，以生成式定义 $e_r,h_r$：
$$
\sum e_r t^r=\prod_i(1+a_it),\qquad
\sum h_r t^r=\prod_i(1-a_it)^{-1}.
$$
负下标为零，$e_0=h_0=1$；空字母表和空行列式也依此约定。写 $R_{q,h}=s_{(q^h)}$。经典恒等式为
$$
s_\lambda=\det(h_{\lambda_i-i+j})
=\det(e_{\lambda'_i-i+j}),\qquad
R_{q,h}=\det(e_{h-i+j})_{i,j=1}^{q},\tag{2.1}
$$
$$
e_t s_\lambda=\sum_{\nu:\nu/\lambda\text{ 每行至多一格、共 }t\text{ 格}}s_\nu.\tag{2.2}
$$
Schur 多项式也是所有行弱增、列严格增的 tableau 单项式之和；因此在非负字母表上非负。在全正 $N$ 字母表上，行数不超过 $N$ 时严格正，否则为零。特别地 $K_j=R_{2,j}$。

以下两个变换也在此证明。对单个删除字母 $x$，生成式给 $h_r[a-x]=h_r(a)-xh_{r-1}(a)$，于是
$$
R_{q,h}[a-x]=\sum_{t=0}^h(-x)^t s_{(q^{h-t},(q-1)^t)}(a).\tag{2.3}
$$
把 (2.1) 的行写为 $U_i-xU_{i+1}$ 并展开：若选移位行后紧接未移位行，就产生重复行。故非零选择只能是最后 $t$ 行一起移位，恰得 (2.3)。当 $x=a_i$，这就是删去实际第 $i$ 个字母。

若 $\Pi_a=\prod_i a_i$、$\lambda\subseteq(q^N)$，补齐 $N$ 行后定义 $\lambda^c=(q-\lambda_N,\ldots,q-\lambda_1)$，则
$$
\Pi_a^q s_\lambda(a^{-1})=s_{\lambda^c}(a).\tag{2.4}
$$
对互异字母，在交错行列式商
$s_\lambda(a)=\det(a_i^{\lambda_j+N-j})/\det(a_i^{N-j})$
中取倒数，各行分别乘 $a_i^{q+N-1}$ 和 $a_i^{N-1}$，再同时反转两组列，就得到 (2.4)。多项式恒等性将它延到重复的正字母。尤其
$R_{q,h}(a)=\Pi_a^qR_{q,N-h}(a^{-1})$。

## 3. 删位和的完整正性引理

令
$$
F_h(a)=\sum_i a_i^2R_{4,h}(a_{-i}),
$$
$$
\mathcal B_h=R_{3,h}R_{2,h+1}-e_hF_h,
\qquad
\mathcal A_h=R_{2,h}R_{3,h+1}-e_{h+1}F_h.\tag{3.1}
$$
核心是以下明确的 Schur 系数公式。若
$\lambda=(5^\alpha,4^\beta,3^\gamma,2^\delta,1^\epsilon)$、$|\lambda|=5h+2$，则
$$
[s_\lambda]\mathcal B_h=
\begin{cases}
\beta+1,&\alpha+\beta+\gamma=h,\ \delta=0,\\
\epsilon+1,&\alpha+\beta+\gamma=h+1,\ \gamma=0,\\
0,&\text{其他情况}.
\end{cases}\tag{3.2}
$$
不是上述形状的分拆系数也为零。下面给出全部系数的推导。

### 3.1 删位和的带符号展开

当 $h=0$，$F_0=p_2$，$\mathcal B_0=h_2-p_2=e_2$，与 (3.2) 一致。设 $h\ge1$，定义
$$
P_t=s_{(4^{h-t},3^t,2,1^t)},\quad
Q_t=s_{(4^{h-t},3^t,1^{t+2})},\quad
Z_t=s_{(4^{h-t-1},3^{t+2},1^t)}.
$$
由 (2.3)，
$$
F_h=\sum_{t=0}^h(-1)^t p_{t+2}s_{(4^{h-t},3^t)}
=\sum_{t=0}^h(P_t-Q_t)-\sum_{t=0}^{h-1}Z_t.\tag{3.3}
$$
第二个等号可以逐个交错指数证明，过程如下。先取字母数 $L\ge2h+3$。对分拆 $\mu$，使用指数 $\mu_i-i$ 的交错行列式；乘 $p_d$ 等于把其中一个指数增加 $d$ 后求和。落到已有指数上的项为零，重新降序排列的符号等于跨过指数个数的奇偶号。

对第 $t$ 项，上部指数集为 $I\setminus\{b_t\}$，其中
$$
I=\{3-h,4-h,\ldots,3\},\qquad b_t=3-h+t;
$$
下部为 $-h-1,-h-2,\ldots,-L$。若上部源是 $b_u$，非零落点只能是 $5-h+t+u>3$。它与第 $u$ 项的源 $b_t$ 配对，终态指数集相同；含外部 $(-1)^t$ 后的两个符号指数分别为
$$
t+h-u-\mathbf1_{t>u},\qquad u+h-t-\mathbf1_{u>t}.
$$
差为奇数，所有上部源两两消去。

下部非零源只能落到三个固定空位 $-h+d$，$d=0,1,2$；源为 $-h+d-t-2$，存在条件为 $t\ge d-1$。总符号是 $(-1)^{1-d}$。对应结果依次为 $-Q_t$、$P_t$、$-Z_{t-1}$，且没有遗漏其他落点。这证明 (3.3)；对称函数恒等性再允许将多余字母置零，覆盖任意字母数。

### 3.2 全部 Pieri 系数的两个区间计数

由 $R_{2,h+1}=e_{h+1}^2-e_he_{h+2}$，
$$
\mathcal B_h=R_{3,h}(e_{h+1}^2-e_he_{h+2})
+e_h\sum Q_t-e_h\sum P_t+e_h\sum Z_t.\tag{3.4}
$$
Pieri 的每条竖条带至多改变一行一格，所以目标只能是 (3.2) 的形状，并分成 $\alpha+\beta+\gamma=h$ 或 $h+1$ 两区。

先取第一种。总次数给
$$
\epsilon=\beta+2\gamma+2-2\delta.
$$
初始乘积 $R_{3,h}(e_{h+1}^2-e_he_{h+2})$ 的系数是
$$
N_{\beta,\epsilon}(h+1-\alpha-\delta)-N_{\beta,\epsilon}(h-\alpha-\delta),
$$
其中 $N_{b,e}(u)=\#\{0\le x\le b,\ 0\le y\le e:x+y=u\}$。
两条竖带都要经过最终长五的 $\alpha$ 行和长二的 $\delta$ 新行；第一条在其余长四行与长一行中各选一个初段，正好由 $x,y$ 决定。因此此计数没有重数遗漏。因 $2(h+1-\alpha-\delta)=\beta+\epsilon$，直接使用
$N_{b,e}(u)=\max(0,\min(b,u)-\max(0,u-e)+1)$，其差等于 $\mathbf1_{\delta=\gamma+1}$。

在同一区，$Q_t$ 和 $P_t$ 的贡献分别是
$$
Q=\#([\gamma,\beta+\gamma]\cap[\delta-2,\delta+\epsilon-2]),
$$
$$
P=\mathbf1_{\delta\ge1}\#([\gamma,\beta+\gamma]\cap[\delta-1,\delta+\epsilon-1]).\tag{3.5}
$$
这些区间分别记录旧三／四格行的升格数和旧一格行的升格数；相同长度的行必须选初段，所以每个整数参数只对应一条竖带。$Z$ 在本区无贡献。若 $\delta=0$，$P=0$ 且 $Q=\beta+1$。若 $\delta\ge1$，令 $u=\delta-\gamma-1$；平移后两个交集是
$[0,\beta]\cap[u-1,\beta-u-1]$ 和 $[0,\beta]\cap[u,\beta-u]$。
当 $u<0$ 两者均为全区间，当 $u=0$ 基数差为 $-1$，当 $u>0$ 两者基数相等。它恰好消去初始乘积的 $\mathbf1_{u=0}$，得到 (3.2) 第一行及本区全部零系数。

第二种区满足
$$
\epsilon=\beta+2\gamma-3-2\delta.
$$
初始乘积及 $Q$ 均不贡献；$Z$ 和 $P$ 的贡献是
$$
Z=\#([\gamma-2,\beta+\gamma-2]\cap[\delta,\delta+\epsilon]),
$$
$$
P=\mathbf1_{\gamma\ge1}\#([\gamma-1,\beta+\gamma-1]\cap[\delta,\delta+\epsilon]).\tag{3.6}
$$
若 $\gamma\ge1$，令 $u=\delta-\gamma+1$。分别平移后得到
$[0,\beta]\cap[u+1,\beta-u]$ 与 $[0,\beta]\cap[u,\beta-u-1]$，由 $x\mapsto\beta-x$ 一一对应；两者消去。若 $\gamma=0$，负项不存在，且 $[\delta,\delta+\epsilon]\subset[-2,\beta-2]$，所以 $Z=\epsilon+1$。全部原源下标范围已经被这些交集蕴含；空交集按零计数。这完成 (3.2)。

### 3.3 两个正性结论

由 (3.2) 与 tableau 正性，
$$
\mathcal B_h(a)\ge0,\qquad
\mathcal B_h(a)\ge s_{(5^h,1,1)}(a).\tag{3.7}
$$
对正 $L$ 字母表，令 $\ell=L-h-1$。式 (2.4) 逐项给
$$
F_h(a)=\Pi_a^4F_\ell(a^{-1}),\qquad
\mathcal A_h(a)=\Pi_a^5\mathcal B_\ell(a^{-1}).\tag{3.8}
$$
例如删位后字母数为 $L-1$，其积为 $\Pi_a/a_i$，乘原 $a_i^2$ 就变成 $\Pi_a^4a_i^{-2}$，故第一式没有遗留删位因子。其他三个因子直接用矩形互补即可得到第二式。

若 $h\ge1$ 且 $L\ge h+1$，保留 (3.7) 的指定项，并在 $(5^L)$ 中取补，得到
$$
\boxed{\mathcal A_h(a)\ge s_{(5^{h-1},4,4)}(a)>0.}\tag{3.9}
$$
最后一个分拆有 $h+1\le L$ 行；填第 $i$ 行全为字母 $i$ 就给一个严格正 tableau 项。

## 4. 删位矩阵的显式负超平面

若 $j=0$，$H_j=\mathbf1\mathbf1^*-I$，结论直接成立。以下 $j\ge1$，置 $r=j+1$、$S_r=R_{3,r-1}$，并定义
$$
b_i=K_{r-1}(a_{-i}),\qquad t_i=a_iS_r(a_{-i}),
$$
$$
R=bb^*-K_{r-1}(a)H_j-\frac{e_r(a)}{S_{r+1}(a)}tt^*.\tag{4.1}
$$
$K_{r-1},e_r,S_{r+1}$ 的分母／系数都严格正，因为 $r\le N-1$。我们将由明确条目证明 $R>0$。

### 4.1 两个删位恒等式

对 $A$ 和两个新增字母 $x,y$，有
$$
S_r(x,A)S_r(y,A)-S_{r+1}(x,y,A)S_{r-1}(A)
=K_{r-1}(x,y,A)R_{4,r-1}(A).\tag{4.2}
$$
证明可由一个四阶行列式完成。取 $d=r-1$，$T_{i\ell}=e_{d-i+\ell}(A)$，左右分别乘上对角为一、上副对角为 $x,y$ 的四阶矩阵。整体行列式仍为 $R_{4,d}(A)$。两侧边角三阶子式依次为 $S_r(x,A),S_r(y,A)$；另两角为 $S_{r-1}(A),S_{r+1}(x,y,A)$；中央二阶为 $K_{r-1}(x,y,A)$。这些值由 $e_q(x,A)=e_q(A)+xe_{q-1}(A)$ 逐行／列得到。Desnanot–Jacobi 的“整体×中央＝两正角积−两反角积”即为 (4.2)，包括 $d=1$ 的空矩形。

第二个恒等式是
$$
K_j(x,A)K_j(y,A)-K_j(x,y,A)K_j(A)
=xy\,e_{j+1}(x,y,A)S_j(A).\tag{4.3}
$$
给出其完整有限系数计算。写 $(u,v,w,d,f)=(e_{j+1},e_j,e_{j-1},e_{j-2},e_{j-3})(A)$，
$$
c_0=v^2-uw,\quad c_1=vw-ud,\quad c_2=w^2-vd,
$$
$$
q_0=2vd-w^2-uf,\quad q_1=wd-vf,\quad q_2=d^2-wf,
$$
$$
T_0=\det\begin{pmatrix}w&v&u\\d&w&v\\f&d&w\end{pmatrix}
=w^3-2vwd+v^2f+ud^2-uwf=S_j(A).
$$
令 $s=x+y,p=xy$。单／双字母展开分别为
$$
K_j(x,A)=c_0+xc_1+x^2c_2,
$$
$$
K_j(x,y,A)=c_0+sc_1+s^2c_2+pq_0+spq_1+p^2q_2.
$$
相减后恰为
$$
p\{c_1^2-c_0(2c_2+q_0)+s(c_1c_2-c_0q_1)+p(c_2^2-c_0q_2)\}.
$$
括号的三个系数直接乘开分别为 $uT_0,vT_0,wT_0$，因此等于 $p(u+sv+pw)T_0$，证明 (4.3)。负指标取零的约定覆盖 $j=1$。

将 (4.3) 用于 (4.1) 的非对角条目，再用 (4.2)，得到
$$
\boxed{R_{i\ell}=-\frac{K_{r-1}(a)e_r(a)}{S_{r+1}(a)}
a_i a_\ell R_{4,r-1}(a_{-i\ell})\le0\quad(i\ne\ell).}\tag{4.4}
$$

### 4.2 对角条目的相邻子式计算

写 $a=(x,A)$，设
$$
c=K_{r-1}(A),\quad C_0=K_r(A),\quad T_0=S_r(A),\quad U_0=S_{r+1}(A),
$$
$$
f_0=K_{r-1}(x,A),\quad g=e_r(x,A).
$$
需要两式
$$
f_0U_0=cS_{r+1}(x,A)-xK_r(x,A)T_0,
\qquad cK_r(x,A)-f_0C_0=xgT_0.\tag{4.5}
$$
为明确它们不是额外引用，取四行 $v_i=(e_{r-i},e_{r+1-i},e_{r+2-i})(A)$，$i=0,1,2,3$。令 $L_{ij}$ 为前两列的二阶子式、$\Delta_{ijk}$ 为三阶子式。则
$$
c=L_{12},\quad C_0=L_{01},\quad T_0=\Delta_{123},\quad U_0=\Delta_{012}.
$$
四行交错关系 $v_0\Delta_{123}-v_1\Delta_{023}+v_2\Delta_{013}-v_3\Delta_{012}=0$ 是重复列四阶行列式的展开。对前两坐标分别施加与 $v_1,v_2$ 的二阶行列式，得到
$$
c\Delta_{013}-L_{01}T_0=L_{13}U_0,\qquad
c\Delta_{023}-L_{02}T_0=L_{23}U_0.
$$
一字母展开又给
$$
S_{r+1}(x,A)=U_0+x\Delta_{013}+x^2\Delta_{023}+x^3T_0,
$$
$$
f_0=c+xL_{13}+x^2L_{23},\qquad
K_r(x,A)=L_{01}+xL_{02}+x^2c.
$$
立即得 (4.5) 第一式。第二式只用
$cL_{02}-L_{13}L_{01}=e_r(A)T_0$、
$c^2-L_{23}L_{01}=e_{r-1}(A)T_0$；它们正是 §4.1 的后两个三项乘积系数等式（将指数设为 $r$）。代入上述两条二次展开即得第二式。

第一式乘 $c$，第二式代入消去 $cK_r$，结果是
$$
c^2S_{r+1}(x,A)-x^2gT_0^2=f_0(cU_0+xC_0T_0).
$$
故 (4.1) 的对角条目为
$$
\boxed{R_{ii}=\frac{K_{r-1}(a)}{S_{r+1}(a)}
\{K_{r-1}(a_{-i})S_{r+1}(a_{-i})
+a_iS_r(a_{-i})K_r(a_{-i})\}.}\tag{4.6}
$$

### 4.3 真正正向量与完整平方分解

将 (4.4)、(4.6) 的第 $i$ 行乘实际正向量 $a$，用 $e_r(a)=e_r(a_{-i})+a_ie_{r-1}(a_{-i})$，得到
$$
\boxed{(Ra)_i=\frac{K_{r-1}(a)a_i}{S_{r+1}(a)}
\{\mathcal A_{r-1}(a_{-i})+a_i\mathcal B_{r-1}(a_{-i})\}>0.}\tag{4.7}
$$
严格号由 §3 得到：删位后有 $N-1\ge r$ 个正字母，$h=r-1\ge1$，正好满足 (3.9)。对任意实向量 $z$，逐项展开可得准确平方式
$$
z^*Rz=\sum_{i<\ell}(-R_{i\ell})a_i a_\ell
\left(\frac{z_i}{a_i}-\frac{z_\ell}{a_\ell}\right)^2
+\sum_i\frac{(Ra)_i}{a_i}z_i^2>0\quad(z\ne0).\tag{4.8}
$$
每个交叉系数是 $2R_{i\ell}$；每个平方系数是
$-\sum_{\ell\ne i}R_{i\ell}a_\ell/a_i+(Ra)_i/a_i=R_{ii}$，所以没有隐含余项。

现在若 $b^*z=0$，由 (4.1) 与 (4.8)，
$$
K_{r-1}(a)z^*H_jz
=-\frac{e_r(a)}{S_{r+1}(a)}(t^*z)^2-z^*Rz<0\quad(z\ne0).\tag{4.9}
$$
这正是 §1 所需的负超平面。另有 $\mathbf1^*H_j\mathbf1>0$，因为所有删两位 $K_j$ 都严格正，所以该矩阵确有且仅有一个正特征值；但应用只需要 (4.9)。

## 5. 返回真实协方差和 R294 的全部输入

§4 在 $0\le j\le N-2$ 全部成立，正好覆盖 $j=m-1$。式 (1.3) 的正对角同余保负超平面；再由 (1.4)、$C\mathbf1=v$ 与 $\mathbf1^*C\mathbf1=V>0$ 得
$C\preceq vv^*/V$，即目标 (1.1)。

(1.2) 与行和零也给
$$
x^*\Sigma x=\sum_{i<\ell}c_{i\ell}|x_i-x_\ell|^2,
\quad c_{i\ell}=-\Sigma_{i\ell}>0,\quad\sum_{\ell\ne i}c_{i\ell}=v_i.
$$
所以 $\ker\Sigma=\mathbb C\mathbf1$；对任意常数 $c$，上式不超过
$2\sum_i v_i|x_i-c|^2$，最小化后得到 $\Sigma\preceq2Q$。因此已完全证明
$$
\boxed{Q\preceq\Sigma\preceq2Q.}\tag{5.1}
$$
对 $y\perp\mathbf1$，$QD^{-1}y=y$；把解减去常数投到 $\mathbf1^\perp$ 不改变与 $y$ 的配对，故
$y^*Q^\dagger y=\sum_i|y_i|^2/v_i$。在共同核正交补上反转 (5.1)，得到
$$
\boxed{\frac12\sum_i\frac{|y_i|^2}{v_i}
\le y^*\Sigma^\dagger y\le\sum_i\frac{|y_i|^2}{v_i}.}\tag{5.2}
$$

[R294 主稿](R294-birth-one-uniform-diagonal-gram-comparison-and-common-newton-blocks.md)所用的协方差下界和伪逆界现在全部在仓库内获得证明。其余完整 Schur 字典、实际 $\Gamma_n$ 夹逼、共同代理 Newton 块和无限固定高度极限由该主稿各自给出；[原尾费用附录](R294-appendix-original-tail-coordinate-shift-and-improved-first-return-cost.md)沿用这些已付输入。本文没有从单高度夹逼外推原非交换相邻序，后者的出生一统一有限常数另由不依赖本定理的 [R295](R295-appendix-universal-birth-one-strengthened-s1-by-atomic-splitting.md)支付。

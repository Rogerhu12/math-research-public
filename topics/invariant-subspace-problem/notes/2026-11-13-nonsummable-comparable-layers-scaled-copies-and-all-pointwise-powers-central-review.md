# 非可和幅度的可比层选取与缩放副本：普通多项式及全部固定点态幂

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。
状态：root 全文核验646行，已核自动选层、真实矩阵池、完整域及全部预算。
本文给普通有限矩／矩阵块定理的一个自动选池补充。
新增选取允许任意深的排序跳跃；没有把任意单行自动视为满幂矩阵。
完整 ISP 与一般无副本的重根仍未因此解决。

## 1. 两个准确结论

设
$$
u=a_*+\sum_j a_j\chi_j,\qquad a\in\ell^2,
\qquad
v_\nu=\sum_jc_{\nu j}(\chi_j-1),\quad c_\nu\in\ell^1,
$$
以及
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
给定
$$
F(U,V)=\sum_{k=0}^p f_k(V)U^k,\qquad
p\ge1,\qquad f_p(0)\ne0.
\tag{1.1}
$$

主行中存在一个明确的无限坐标保留集：
$$
j=j(\ell,n),\qquad \ell,n\ge1,
\tag{1.2}
$$
此映射单射，物理顺序任意。
取非增正数列
$$
\rho\in\ell^2\setminus\ell^1,
\tag{1.3}
$$
以及非零缩放序列
$$
\tau\in\ell^2,\qquad \tau_\ell\longrightarrow0.
\tag{1.4}
$$
主行在保留集外仍可为任意 $\ell^2$ 行。

**定理 A（零辅助保留集，任意相位）。**
设存在复数 $z_n$ 满足 $|z_n|=\rho_n$，且
$$
a_{j(\ell,n)}=\tau_\ell z_n,\qquad
c_{\nu,j(\ell,n)}=0
\quad\text{对全部 }\ell,n,\nu.
\tag{1.5}
$$
则对每个 $\lambda\in\mathbb C$ 和每个固定整数 $h\ge1$，
$$
\boxed{[F(u,v)-\lambda]^h e^w\text{ 非零且对原实际 }A\text{ 循环}.}
\tag{1.6}
$$
$\tau_\ell$ 与 $z_n$ 的相位均任意。
辅助在保留集外完全任意，只须可和。

**定理 B（非零幂辅助保留集）。**
设 $\tau_\ell>0$，
$$
a_{j(\ell,n)}=\tau_\ell\rho_n>0,\qquad
c_{\nu,j(\ell,n)}
=(\tau_\ell\rho_n)^{\kappa_\nu},
\tag{1.7}
$$
其中
$$
\kappa_\nu>2,\qquad
1,\kappa_1,\ldots,\kappa_d
\text{ 在 }\mathbb Q\text{ 上线性无关}.
\tag{1.8}
$$
保留集外的辅助仍可为任意可和行。
则 (1.6) 对全部固定 $F,\lambda,h,w$ 成立。

若 $d=0$，定理 B 的无理幂条件为空。
(1.7) 在保留集上确实给可和辅助，因为
$$
\sum_{\ell,n}
(\tau_\ell\rho_n)^{\kappa_\nu}
=
\left(\sum_\ell\tau_\ell^{\kappa_\nu}\right)
\left(\sum_n\rho_n^{\kappa_\nu}\right)<\infty.
\tag{1.9}
$$

结论中的全部点态幂将分别以新多项式
$G=(F-\lambda)^h$ 重新应用证明。
不从单次循环性直接推断点态乘积循环。

## 2. 非可和行自动含有大而近等幅的排序层

**引理 2.1。**
固定 $s>1$ 和 $0<\delta<2^{-s}$。
若正非增 $\rho\notin\ell^1$，
则存在无限多个二进制整数 $N=2^k$，使
$$
\boxed{
\rho_{2N}\ge\delta\rho_N,\qquad
\rho_{2N}\ge(2N)^{-s}.
}
\tag{2.1}
$$

**证明。**
若 $2^{sk}\rho_{2^k}$ 最终有界，
由单调性得 $\rho_n=O(n^{-s})$，与非可和矛盾。
所以
$$
x_k:=2^{sk}\rho_{2^k},\qquad
\limsup_kx_k=\infty.
$$
反设只有有限个 $k$ 满足 (2.1)。
对于充分大 $k$，只要 $x_{k+1}\ge1$，便须有
$$
\rho_{2^{k+1}}<\delta\rho_{2^k},
\qquad
x_{k+1}<q x_k,\qquad q:=2^s\delta<1.
$$
所以对全部充分大 $k$，
$$
x_{k+1}\le\max(1,qx_k).
$$
递归给 $x_k$ 最终有界，矛盾。证毕。

实际上，引理只用
$\limsup_k2^{sk}\rho_{2^k}=\infty$；
非可和是一个无需选择 $s$ 的充分条件。
本文后续仍保 (1.3)，以免扩大表述掩盖主选取。

在 (2.1) 的 $N$ 上，全部 $N<n\le2N$ 满足
$$
\delta\rho_N\le\rho_n\le\rho_N,\qquad
(2N)^{-s}\le\rho_n\le\|\rho\|_2N^{-1/2}.
\tag{2.2}
$$
这里上界来自 $N\rho_N^2\le\|\rho\|_2^2$。

取例如 $s=2,\delta=1/8$ 即可固定整个论证。
后续常数可以依赖这个固定选择。

## 3. 任意有限个缩放副本的真实物理选池

给定任意固定整数 $q\ge1$。
因 $\tau_\ell\to0$ 且每项非零，可先选出互异副本
$$
\ell_1,\ldots,\ell_q
$$
使
$$
|\tau_{\ell_{i+1}}|
\le(\delta/4)|\tau_{\ell_i}|
\quad(1\le i<q).
\tag{3.1}
$$
这些副本一经选定便保持不变，随后才令 $N\to\infty$。
其常数即使很大或很小，也不依赖 $N$。

在每个副本中取 $N<n\le2N$ 的 $N$ 个实际位置，
删去物理编号
$$
j<\lfloor N/4\rfloor.
$$
每个副本最多删去 $\lfloor N/4\rfloor$ 个位置。
所以均可保留恰好
$$
Q_N=\lfloor N/2\rfloor
$$
个位置，记为 $I_{i,N}$。
各池互不相交，且
$$
\min\bigcup_i I_{i,N}\ge\lfloor N/4\rfloor,
\qquad
|a_j|\le C_qN^{-1/2}.
\tag{3.2}
$$
同时
$$
\delta|\tau_{\ell_i}|\rho_N
\le|a_j|\le|\tau_{\ell_i}|\rho_N
\quad(j\in I_{i,N}).
\tag{3.3}
$$

任取每池一个位置，记所得主系数为 $A_1,\ldots,A_q$。
由 (3.1)、(3.3)，当 $i<j$ 时
$$
|A_i-A_j|
\ge\bigl||A_i|-|A_j|\bigr|
\ge\frac{3\delta}{4}|\tau_{\ell_i}|\rho_N.
\tag{3.4}
$$
这对任意复相位都成立。
因此没有将副本内各 $z_n$ 的相位当成相同，也没有要求各池选同一个 $n$。

全部选位只用实际坐标计数。
任意物理排列即使使某些选中坐标极大，也不改变 (3.2)。
后续 carry 预算使用最小选中位，而不使用最大选中位。

## 4. 普通目标的真实有限矩实现

本节列出所用普通矩定理的准确接口。
对固定多项式 $G$，设总次数为 $D$。
原系数向量写为
$$
\xi_j=(a_j,c_{1j},\ldots,c_{dj}).
$$
加入有限个居中可和矩行
$$
\eta_{\omega j}=\xi_j^\omega,\qquad 2\le|\omega|\le D.
$$
因主行属于 $\ell^2$、其余行属于 $\ell^1\subset\ell^2$，
这些二阶以上乘积行都属于 $\ell^1$。

令 $Z_{e_0}$ 表示主变量，$Z_{e_\nu}$ 表示原辅助，
其余 $Z_\omega$ 表示新增矩。
准确有限多项式为
$$
Q_G(Z)=
\left.
G(\partial_t)
\exp\left[
\sum_{\nu=0}^d t_\nu Z_{e_\nu}
+\sum_{2\le|\omega|\le D}
\frac{(-2)^{|\omega|-1}}{\omega!}t^\omega Z_\omega
\right]\right|_{t=0}.
\tag{4.1}
$$
由
$$
\phi(z)=\frac{1-e^{-2z}}2,\qquad
\psi(z)=-\frac12\log(1-2z),\qquad
\psi(\phi(z))=z,
$$
扩展行的准确共振实现 $\mathfrak F_{Q_G}$ 等于普通 $G(u,v)$。
所有被抵消的项至少二阶，均绝对可和；
不要求 $\sum a_j$ 存在。

若 $G$ 关于主变量的次数为 $p_G$，且最高系数字符非零，
实际自然算子
$$
T=P_{Q_G}(X_b,\mathbf Y;\mathbf G)
$$
满足
$$
\operatorname{Dom}T=\operatorname{Dom}X_b^{p_G},
\qquad
Te^w=G(u,v)e^w.
\tag{4.2}
$$
它具有完整闭自然图、原 $C$ 自伴及循环图核心。
核 $M$ 满足
$$
M\subset\mathcal D_\infty(X_b),\qquad
X_b|_M\in B(M).
\tag{4.3}
$$
每个混合修正 $\mathbf G$ 都来自明确的二阶以上局部因子，
属于已证快系数类，并有全部真实导子 jets。

以下使用两个不同的矩阵接口：
一是全部扩展行的满矩阵；
二是选位上只有部分行非零时的真实活跃行子矩阵。
两者不能互相偷换。

## 5. 定理 A：活跃纯主矩阵

先令 $G$ 为任何符合 (4.2) 的固定多项式，
主次数为 $p_G$。
在零辅助保留集上，
所有含原辅助的矩行都准确为零。
在 (4.1) 中，纯主矩 $Z_{ke_0}$ 只需
$$
1\le k\le p_G.
$$
次数更高的纯主矩不出现。
因此活跃行恰可取
$$
a_j,a_j^2,\ldots,a_j^{p_G}.
\tag{5.1}
$$

最高活跃矩导数是一个实际有界交换系数单位。
其字符为
$$
(-2)^{p_G-1}g_{p_G}(0)\ne0,
\tag{5.2}
$$
其中 $g_{p_G}$ 为 $G$ 的主最高系数。
它不要求主字符根简单。

令 $q=p_G$，使用 §3 的 $q$ 个池。
任取一组跨池系数 $A_1,\ldots,A_q$，其活跃矩阵行列式为
$$
\det(A_i^k)_{\substack{1\le k\le q\\1\le i\le q}}
=
\left(\prod_{i=1}^qA_i\right)
\prod_{i<j}(A_j-A_i).
\tag{5.3}
$$
由 (3.3)、(3.4) 与 (2.1)，
$$
\boxed{
|\det(A_i^k)|
\ge C_q\rho_N^{q(q+1)/2}
\ge C_q' N^{-s q(q+1)/2}.
}
\tag{5.4}
$$
所以跨池最小行列式 $\Delta_N$ 满足
$$
\log^+\Delta_N^{-1}=O_q(\log N).
\tag{5.5}
$$

这是实际部分行矩阵，未给零辅助行添加虚构独立性。
结合 §7 的实际矩阵块提升，得到 $G(u,v)e^w$ 循环。

最后取
$$
G(U,V)=[F(U,V)-\lambda]^h.
$$
其主次数为 $hp$，最高主系数字符为 $f_p(0)^h\ne0$。
无限副本提供任何固定数目 $hp$ 所需的池。
于是对每个固定 $h$ 重新应用上述证明，得到定理 A。

## 6. 定理 B：全部幂矩阵

仍先固定 $G$ 及其总次数 $D$。
设
$$
\Omega_D=\{\omega\in\mathbb N_0^{d+1}:1\le|\omega|\le D\},
\qquad
K=|\Omega_D|.
$$
在正主系数保留集上，
全部扩展系数行准确为
$$
\eta_{\omega j}=a_j^{w_\omega},
\qquad
w_\omega=\omega_0+\sum_{\nu=1}^d\kappa_\nu\omega_\nu.
\tag{6.1}
$$
由 (1.8)，这些固定实指数两两不同且全部为正。

令 $q=K$，按 §3 选出 $K$ 个池。
对任意跨池选择写
$$
A_i=\rho_Nx_i,\qquad
x_i\in[\delta\tau_{\ell_i},\tau_{\ell_i}].
\tag{6.2}
$$
这些是固定、互不相交、严格正的紧区间。
故
$$
\det(A_i^{w_\omega})_{\omega,i}
=
\rho_N^{W_D}\det(x_i^{w_\omega})_{\omega,i},
\qquad
W_D:=\sum_{\omega\in\Omega_D}w_\omega.
\tag{6.3}
$$

不同实指数的幂函数构成严格 Chebyshev 系。
为完整说明非零性，按递增顺序列指数
$w_1<\cdots<w_K$。
先考虑实系数。一个非零线性组合 $\sum_{\nu=1}^K b_\nu x^{w_\nu}$
在正轴上至多有 $K-1$ 个互异零点：
除以 $x^{w_1}$ 后，导数成为 $K-1$ 个不同幂的组合，
用 Rolle 定理和归纳即可。
因此在 $K$ 个互异正数上，该实矩阵没有非零实核。若有非零复核向量，其实部或虚部至少一个给非零实核，所以矩阵 $(x_i^{w_\nu})$ 在复数域上也可逆。

行列式连续，各 $x_i$ 所在区间固定紧且彼此分离，
所以其绝对值有严格正下界。
由 (2.1)、(6.3)，
$$
\boxed{
\Delta_N\ge C_D\rho_N^{W_D}
\ge C_D'(2N)^{-sW_D},
\qquad
\log^+\Delta_N^{-1}=O_D(\log N).
}
\tag{6.4}
$$

取 $G$ 的任意非零最高总次项 $g_\omega z^\omega$，
$|\omega|=D$。
有限逆式 (4.1) 给
$$
\frac{\partial Q_G}{\partial Z_\omega}
=(-2)^{D-1}g_\omega\ne0.
\tag{6.5}
$$
这里没有额外 $\omega!$。
它是完整实际实现中的常数单位。
因此无需在主字符根处要求任何原梯度非零。

使用 §7 的全部 $K$ 行矩阵块提升，得到 $G(u,v)e^w$ 循环。
对每个固定 $G=(F-\lambda)^h$，令 $D=\deg G$ 并重新选其 $D$ 阶矩列表与有限个池，
即得定理 B 的全部固定点态幂。

## 7. 实际矩阵块、自然域与四次预算

为明确 §§5–6 不只给形式行列式，列出实际提升的全部接口。
记当前活跃行数为 $q$，每池大小 $Q=Q_N$。
所有所用系数行在全空间上有固定一致幅度上界。
所选主系数满足 (3.2)，辅助系数和由其全局 $\ell^1$ 范数支付。

在任一未知核的根块上，取已给的单位梯度 $D_\star$。
对一个跨池 $q$ 位块 $B$，令 $\Xi_B$ 为真实系数矩阵，
$$
b_B=\frac14\Xi_B^{-1}e_\star.
$$
平方零输入为
$$
P_B=
D_\star^{-1}\sum_{i=1}^q
(b_B)_i\prod_{k\ne i}u_{j_k}.
\tag{7.1}
$$
共因子界与 (5.5) 或 (6.4) 给
$$
\|P_B\|_{\mathrm{abs}}
\le C_M\Delta_N^{-1}.
\tag{7.2}
$$

实际高位差的一次项为
$$
L_j=4\sum_{\nu\text{ 活跃}}
\eta_{\nu j}D_\nu.
$$
所有不活跃行在选中位上准确为零，或该多项式根本不依赖它。
于是
$$
\left(\sum_{j\in B}u_jL_j\right)P_B
=\prod_{j\in B}u_j
$$
在平方零商中成立。

从每池选 $r$ 个位置，以一个固定排序作唯一匹配，得到 $r$ 个互不相交块。
输入总次数为 $(q-1)r$。
$r$ 次差算子的任何一次二阶或更高项，都会令总次数超过 $qr$，
故顶部只能来自每块一次的线性项，准确系数为 $r!$。
这里没有再对所有匹配求和。

取
$$
r=\left\lfloor\sqrt{Q/\theta}\right\rfloor
$$
和固定 $\theta>0$。
核内先形成 $\prod_BP_B f$，随后才作用最左反射 $J_E$。
真实自然域等式为
$$
T^rJ_E\prod_BP_B f
=
J_E(\gamma_ET)^r\prod_BP_B f.
\tag{7.3}
$$
不把反射当成保核算子。
最左反射作用顶部纯位项给 $(-1)^{qr}$。

采用准确归一化
$$
(-1)^{qr}(r!)^{q-1}(2/Q)^{qr}
$$
对各池的 $r$ 元子集平均。
每池恰有 $\binom Qr$ 个子集，故最后总阶乘为 $(r!)^q$。
有界纯平均在全部固定有限柱上的弱系数为
$$
\left((Q)_r/Q^r\right)^q
\longrightarrow e^{-q/(2\theta)}.
\tag{7.4}
$$

(7.2) 及有限组合数给输入范数上界 $A_N$，满足
$$
\log A_N
\le r\log^+\Delta_N^{-1}+C_Mr+C
=O_M(r\log N).
\tag{7.5}
$$
每个实际输入属于 $\mathcal D_\infty(X_b)$。
选中主系数和满足
$$
\sum_{j\in E}|a_j|\le Cqr/\sqrt N=O_{q,\theta}(1),
$$
全部辅助选中和由可和性控制。
因此所有直到 $4Dr$ 阶的实际 $X_b$ jets 均由固定底数的指数界支付。

R260 的任意跨度壳估计只用
$\min E\ge\lfloor N/4\rfloor$，
给完整重排误差
$$
\varepsilon_N
\le C_D\exp[-385\,16^{\lfloor N/4\rfloor-1}].
$$
重复位 carry、全部矩系数和混合快修正的误差
最多乘 $A_Ne^{C_Dr\log(r+2)}$，因而趋零。
所以真实
$$
T^r\mathcal V_Nf\rightharpoonup e^{-q/(2\theta)}f,
$$
且输出有一致范数界。

对固定局部全矩阵 $D_*$，
真实有限头分解每次提出一个 $A$，
剩余主次数至多当前固定 $p_G$。
全部 $4Dr$ jets 给
$$
\|(\operatorname{ad}_T^rD_*)\mathcal V_N f\|
\le
2\|D_*\|A_N C^r
e^{-5r^4/6+105r^3}\|f\|.
\tag{7.6}
$$
由 (7.5)，$\log A_N=O(\sqrt N\log N)=o(r^4)$，
故 (7.6) 趋零。

原完整 $C$ 配对与 $Tg=0$ 给
$\mathcal B(D_*f,g)=0$ 对全部局部矩阵成立，
局部不可约性排除非零核。
完整 $C$ 自伴和循环图核心随后给目标循环。
这同时支付 §§5–6 的实际域、有限头、符号、阶乘与弱平均。

## 8. 与旧空谱范围的关系

若所有主系数同射线，某些上述例子本来已经落在旧空谱锚范围内。
不将这部分重计为新增。

可以明确保持没有这样的锚：
取正 $\rho$，在定理 B 的正保留集外，再放入一条
$$
a_{j_-(n)}=-\rho_n
$$
的非可和负副本，并令这些位上的全部辅助为零。
主行的正、负质量均为无穷，仍属于 $\ell^2$。
任意非零常数倍主行加上有限个可和辅助，
都不能消除两个相反相位上的无限质量。
因此不能通过原主／辅助的常数线性组合取得
“单射线加可和相位缺陷”的旧空谱锚。

例如可取一个辅助指数 $\kappa=\sqrt5$，
有限低头另置
$$
a_0=1,\qquad c_0=2^{-1/3},
$$
然后将全部副本放在剩余位置。
对普通多项式
$$
F(U,V)=U^2+V^3
$$
及其全部固定点态幂，定理 B 均适用。
其 $\lambda=0$ 字符根 $(0,0)$ 是原双梯度同时为零的真实 cusp；
原首位切片为
$$
p_0(z)=z^2,\qquad
p_1(z)=(z-2)^2+(-2c_0)^3=z^2-4z,
$$
确有共同根。
这里说的是原切片保留候选，不是假设未知共同根实际存在。

## 9. 允许深排序跳跃的明确幅度

为说明引理不暗含全局负幂或对数下界，可取
$$
L_1\ge10,\qquad L_{k+1}=e^{3L_k},
$$
并将
$$
e^{-L_k}
$$
重复
$$
m_k=\left\lceil e^{L_k}/k\right\rceil
$$
次组成非增 $\rho$。
则
$$
\sum_n\rho_n=\infty,\qquad
\sum_n\rho_n^2<\infty.
$$
第一式来自每层质量至少 $1/k$；
第二式由 $\sum_ke^{-L_k}/k<\infty$ 得到。

令 $M_k=\sum_{\nu\le k}m_\nu$。
有 $M_k\asymp e^{L_k}/k$，
故在下一层起点
$$
\frac{-\log\rho_{M_k+1}}{(M_k+1)^{3/2}}
=
\frac{L_{k+1}}{(M_k+1)^{3/2}}
\longrightarrow\infty.
$$
所以不存在全局 $\log\rho_n^{-1}=O(n^{3/2})$。
同时 $n\rho_n\to0$，仍然非可和。

若还希望复制后的主行保留这样的巨大排序缺口，
可取 $\tau_\ell=e^{-L_\ell}$，
而不是几何缩放。
截至指数 $2L_k$ 的正副本项仅来自
$\ell\le k$、基行层号 $\le k$，总数为 $kM_k$；
再加入一条负副本也只有 $(k+1)M_k$ 项。
下一指数至少 $L_{k+1}$，所以同样违反全局
$O(n^{3/2})$ 对数界。
各固定次数的证明只选有限个副本；
它们的极小缩放因子仅进入固定常数，
随后让引理 2.1 的 $N$ 继续趋于无穷即可。

这个例子展示自动选池的范围，不产生任何核存在断言。

## 10. 范围边界与来源

本文没有证明任意单个非可和行都满足满幂矩阵条件。
同幅大平台若没有所需相位或缩放副本，
仍可能缺乏多个独立矩方向。
简单根好集定理只给一个主梯度单位，也不能替代这里的矩阵。

居中可和超指数主行、迟首辅助及旧实际预算边界，
均未被本文的非可和副本条件自动关闭。
一般不具最高主系数字符单位的自然多项式、
多个独立无界方向及完整 Hilbert ISP 仍未完成。

所用完整来源：

- [普通点态有限矩展开](2026-11-13-ordinary-pointwise-moment-expansion-veronese-pools-and-reserve-sites-central-review.md)：
  准确 $\phi/\psi$ 逆、最高矩常数、完整自然图及部分活跃行版本。
- [多辅助矩阵块](2026-11-13-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages-central-review.md)：
  实际余子式输入、$(-1)^{qr}$、唯一匹配及全部组合归一化。
- [任意非可和好集简单纤维](2026-11-13-nonsummable-main-good-sets-and-simple-character-fibers-central-review.md)：
  非可和子集的多项式种子与简单根范围；本文没有把该单池结论外推到重根。
- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  自然闭图、核内有界 first 与深域、原完整 $C$ 配对。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意跨度实际壳估计与真实高阶导子。
- [旧空谱范围审计](2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)：
  应扣除的同射线／可和相位缺陷范围。

新增的实质输入为引理 2.1 的非可和近等幅层、
任意相位下经缩放获得的真正分离，
以及任意物理排列中仍能保留固定比例的完整矩阵池。

# R150 附录：临界对数双模式的全部普通多项式、零参数与真实矩阵池

日期：2026-11-13（UTC）。normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；root 与 kernel 全文独立核查。
关键新增输入是已独立审查并发布的
[变化正预解幂与实际核内混合 jets](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)。
本稿将它与准确普通点态矩逆及真实矩阵池相接，不预设未知核上的 first 有界。

## 1. 同一原临界双模式的结论

固定整数 $k\ge2$，置
$$
\alpha=\frac{k-1}{k},\qquad
a_j=\frac1{j+2},\qquad
b_j=\frac1{k(j+2)(\log(j+2))^\alpha}.
\tag{1.1}
$$
保留原前缀所确定的固定实常数 $\kappa_a,\kappa_b$：
$$
\sum_{j<n}a_j=\log(n+2)+\kappa_a+O(n^{-1}),
$$
$$
\sum_{j<n}b_j=(\log(n+2))^{1/k}+\kappa_b
+O\!\left(\frac1{n(\log(n+2))^\alpha}\right).
$$
原模式始终是
$$
\boxed{
u=-\kappa_a+\sum_ja_j\chi_j,\qquad
z=-\kappa_b+\sum_jb_j\chi_j.
}
\tag{1.2}
$$
没有重新选择物理排列、中心常数或相位来把零参数变成非零参数。

**定理。** 对任意非零有限标量多项式 $F\in\mathbb C[x,y]$，以及任意
$$
w=w_*+\sum_jw_j\chi_j,\qquad (w_j)\in\ell^2(\mathbb C),
$$
都有
$$
\boxed{F(u,z)e^w\ne0,\qquad [F(u,z)e^w]_A=H.}
\tag{1.3}
$$
特别，对全部 $\lambda\in\mathbb C$、整数 $r\ge1$，
$$
\boxed{[z^k-u-\lambda]^r e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.4}
$$
这里包括此前尚未得到的 $\lambda=0$。

更一般，任何原非恒定 $F$ 与任意非零一变量多项式 $Q$ 的
$Q(F(u,z))e^w$ 都由 (1.3) 处理。
每次对整个有限多项式 $Q\circ F$ 重新构造其矩变量和 Bell；不使用“循环向量可以点乘”的规则。

结论仍只针对这些明确的有限多项式与指数权，不给任意 $L^2$ 向量循环性，也不解决普通 Hilbert 不变子空间主问题。

## 2. 把普通点态多项式准确送入有限矩变量

常数多项式由 $e^w$ 循环处理。
以下固定总次数 $D=\deg F\ge1$，所有维数在令池大小 $N\to\infty$ 之前固定。

取
$$
\Omega_D=\{(i,j)\in\mathbb N_0^2:1\le i+j\le D\},
\qquad K=|\Omega_D|=\frac{D(D+3)}2.
\tag{2.1}
$$
每个物理位 $p$ 的实际系数列为
$$
\xi_p=(a_p^i b_p^j)_{(i,j)\in\Omega_D}\in\mathbb R^K.
\tag{2.2}
$$
对应的点态模式定义为
$$
v_{10}=u,\qquad v_{01}=z,\qquad
v_{ij}=\sum_pa_p^ib_p^j(\chi_p-1)\quad(i+j\ge2).
\tag{2.3}
$$
只有前两条可能无界；其余行都在 $\ell^1$，因为总幂至少2而 $a,b\in\ell^2$。
它们是真正可和且已居中的高矩，没有把 $\sum a_p$ 或 $\sum b_p$ 当作收敛量使用。

将 $Z=(Z_{ij})_{\Omega_D}$ 暂作独立的有限标量变量，定义
$$
\boxed{
Q_F(Z)=
\left.
F(\partial_t,\partial_s)
\exp\left[
tZ_{10}+sZ_{01}
+\sum_{2\le i+j\le D}
\frac{(-2)^{i+j-1}}{i!j!}\,t^is^jZ_{ij}
\right]\right|_{t=s=0}.
}
\tag{2.4}
$$
只取到总参数次数 $D$；所以这是有限多项式。
给 $Z_{ij}$ 权 $i+j$，则 $Q_F$ 的权次及普通次数都不超过 $D$。

令
$$
\phi(t)=\frac{1-e^{-2t}}2,\qquad
\psi(t)=-\frac12\log(1-2t),
\qquad \psi(\phi(t))=t
\tag{2.5}
$$
于零点解析分支。
在扩展行的共振生成式中代入参数
$$
s_{10}=t,\quad s_{01}=s,\quad
s_{ij}=\frac{(-2)^{i+j-1}}{i!j!}t^is^j.
$$
第 $p$ 位的组合参数准确为
$$
\sum_{(i,j)\in\Omega_D}s_{ij}a_p^ib_p^j
=\phi(ta_p+sb_p)\quad\text{到总次数 }D.
$$
额外的线性高矩部分与二次以上共振部分合并后，余下
$$
\sum_p[\psi(\phi(ta_p+sb_p))-(ta_p+sb_p)](\chi_p-1)=0
$$
到全部所需次数。
所有和的非线性系数至少含两个 $\ell^2$ 因子，绝对收敛。
这就证明
$$
\boxed{\mathfrak F^{\mathrm{exp}}_{Q_F}=F(u,z)}
\tag{2.6}
$$
作为原实际点态有限多项式恒等式。

这是
[R236 普通点态矩逆 §§3—4](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)
的同一有限 $\phi/\psi$ 计算。
该计算本身允许两条 $\ell^2$ 线性行；旧证明后续只留一条无界行的限制，将在本稿用变化正则器单独替换，而不是偷偷删去。

### 2.1 全空间的常数偏导方向

写
$$
F_D(x,y)=\sum_{i+j=D}f_{ij}x^iy^j.
$$
选一个 $\omega_*=(i_*,j_*)$ 满足 $f_{i_*j_*}\ne0$。
变量 $Z_{\omega_*}$ 权为 $D$，在 (2.4) 中只能线性出现且不能与任何其他正权变量同乘。
准确有
$$
\boxed{
\partial_{Z_{\omega_*}}Q_F
=(-2)^{D-1}f_{i_*j_*}=:c_*\ne0.
}
\tag{2.7}
$$
参数阶乘 $i_*!j_*!$ 已准确抵消，没有额外阶乘。
$D=1$ 时就是原非零线性系数。
此方向是整个有限多项式中的标量常数；不要求核内选根，不要求某个无界 first 在核内有界。

## 3. 原 Bell、最大闭图及正则化核输入

记
$$
t_p=e^{-2w_p},\qquad R_p=V(t_pN_p).
$$
两条实际倾斜 first 为
$$
Z_{10}=X_+-\kappa_a I+H_{a,w},\qquad
Z_{01}=Y_+-\kappa_b I+H_{b,w},
\tag{3.1}
$$
其中
$$
X_+=X_{\sum a_p\chi_p},\quad
Y_+=X_{\sum b_p\chi_p}
$$
是未居中的最大增生 first；$H_{a,w},H_{b,w}\in\mathcal A$ 是 R186 §10 的固定有界交换扰动。
对 $i+j\ge2$，实际高矩模式是
$$
Z_{ij}=\sum_pa_p^ib_p^j(R_p-I)\in\mathcal A.
\tag{3.2}
$$

对扩展指标的多重指数 $\beta=(\beta_\omega)_{\Omega_D}$，$2\le|\beta|\le D$，令
$$
G_\beta
=(-1)^{|\beta|-1}(|\beta|-1)!
\sum_p\left(\prod_{\omega\in\Omega_D}\xi_{\omega p}^{\beta_\omega}\right)
(R_p-I)^{|\beta|}.
\tag{3.3}
$$
全部系数行绝对可和，故按范数收敛；局部至少二阶消去还给原已证快类性质。
本稿只用其真实有界性、局部公式及至少二阶的 $N_p$ 因子。

实际有限共振多项式为
$$
P(Z;\mathbf G)=
\exp\left(\sum_{2\le|\beta|\le D}
\frac{G_\beta}{\beta!}\partial_Z^\beta\right)Q_F(Z).
\tag{3.4}
$$
只作有限次求导。
其关于原两无界 first 的总次数至多 $D$。
R186 的共同自然词图、完整有限 jets 与规范闭包给
$$
\mathsf T=\overline{P|_{\mathcal D_D}},\qquad
\mathsf T^*=C\mathsf TC,\qquad
\mathsf Te^w=F(u,z)e^w.
\tag{3.5}
$$
这里 $\mathcal D_s$ 包含两条正 first 的全部长度至多 $s$ 的自然词；固定有界交换倾斜不改变它。
没有声称原自然多项式在 $\mathcal D_D$ 上已经闭。

在 (3.4) 中把 $\mathbf G$ 作为已经定义的系数保持固定，(2.7) 给
$$
\boxed{\partial_{Z_{\omega_*}}P=c_*I.}
\tag{3.6}
$$
所有更高导数作用于常数均为零。
该式是在全空间共同自然域上成立的真实方向单位。

令 $M=\ker\mathsf T$。
使用已发布
[正预解幂引理 §§1—6](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)，取
$$
q_r=(8D+8)r,\quad\epsilon_r=r^{-2},\quad
\mathcal R_r=
(I+\epsilon_rX_+)^{-q_r}(I+\epsilon_rY_+)^{-q_r}.
\tag{3.7}
$$
准确有
$$
\boxed{
\|\mathcal R_r\|\le1,\quad
\mathcal R_r\to I\ {\rm SOT},\quad
\mathcal R_rM\subset M\cap\mathcal D_{q_r}.
}
\tag{3.8}
$$
长度 $s\le q_r$ 的任意实际倾斜混合词满足
$$
\|W(Z_{10},Z_{01})\mathcal R_r\|
\le(C_w+2r^2)^s.
\tag{3.9}
$$
核保持直接来自 R186 的有界最大图方程，不先假定 $M$ 有任何自然域正则性。
$\mathcal R_r$ 从始至终只放在右侧核输入，不使用 $\mathcal R_r^*$ 保持 $M$。

## 4. 全部固定阶矩的统一跨池行列式

本节给 (2.2) 的全部 $K$ 行，不能只检查原两行的 $2\times2$ 行列式。

取固定两两分离的正整数倍数，例如
$$
I_{\ell,N}=\{(3\ell+1)N+s:0\le s<N\},
\qquad 1\le\ell\le K.
\tag{4.1}
$$
每池 $N$ 位，最小物理位至少 $4N$。
对任意跨池取点 $p_\ell\in I_{\ell,N}$，置
$$
t_\ell=\frac{p_\ell+2}{N},\qquad L=\log N.
$$
全部 $t_\ell$ 落在固定正紧区间，且这些区间两两分离。

按总次数 $d=i+j$ 排列矩行。
准确有
$$
a_p^{d-j}b_p^j
=k^{-j}N^{-d}L^{-\alpha j}\,
t^{-d}\left(1+\frac{\log t}{L}\right)^{-\alpha j},
\qquad 0\le j\le d.
\tag{4.2}
$$
先从第 $(d,j)$ 行抽出 $k^{-j}N^{-d}L^{-\alpha j}$。

固定 $d$，定义 $(d+1)\times(d+1)$ 常数矩阵
$$
B^{(d)}_{j,h}=\binom{-\alpha j}{h},
\qquad 0\le j,h\le d.
\tag{4.3}
$$
这是把不同节点 $-\alpha j$ 代入次数 $h$、最高系数 $1/h!$ 的多项式所得的 Vandermonde 型矩阵，因 $\alpha\ne0$ 而可逆。
用 $(B^{(d)})^{-1}$ 线性组合该组行，再把第 $h$ 个新行乘 $L^h$。
有限 Taylor 展开在上述所有紧区间上一致给
$$
L^h\sum_{j=0}^d
((B^{(d)})^{-1})_{h,j}
\left(1+\frac{\log t}{L}\right)^{-\alpha j}
\longrightarrow(\log t)^h.
\tag{4.4}
$$
因此经过全部固定块变换后，矩阵一致趋于以函数
$$
\boxed{t^{-d}(\log t)^h,\quad
1\le d\le D,\quad0\le h\le d}
\tag{4.5}
$$
为行、以各 $t_\ell$ 为节点的矩阵。

### 4.1 极限矩阵的全部跨池选择都非退化

置 $x=\log t$，(4.5) 成为
$$
e^{-dx}x^h,\qquad 1\le d\le D,\quad0\le h\le d.
$$
它们构成实指数的合流 Chebyshev 系统。
这里给出所需的自含零点证明：
一个含这些指数多项式、总维数 $K$ 的非零实线性组合至多有 $K-1$ 个不同实零点。
对维数归纳，先除以其中一个指数 $e^{\lambda x}$ 再求导；
该指数组的常数维度消失，而其他不同指数组上的“求导＋非零常数”在有限多项式空间中可逆。
维数准确减少1，Rolle 定理完成归纳。
复线性关系取一个非零实部或虚部即可归约。

故任意 $K$ 个不同正节点处的矩阵行列式都非零。
各节点分处固定不交紧区间，行列式连续，所以模有统一正下界。
再用 (4.4) 的一致收敛，实际变换矩阵在全部跨池选择上也有统一正下界。

计入所有抽出的行因子及块变换行列式，令
$$
A_D=\sum_{d=1}^D d(d+1)
=\frac{D(D+1)(D+2)}3,\qquad
B_D=\sum_{d=1}^D\frac{d(d+1)}2=\frac{A_D}2,
$$
便得到
$$
\boxed{
\Delta_N:=
\min_{p_\ell\in I_{\ell,N}}
\left|\det[\xi_{p_1}\ \cdots\ \xi_{p_K}]\right|
\ge C_DN^{-A_D}(\log N)^{-(\alpha+1)B_D}.
}
\tag{4.6}
$$
所有 $k^{-j}$ 和固定 $B^{(d)}$ 行列式只进入正的常数。
所以
$$
\boxed{\log^+\Delta_N^{-1}=O_D(\log N).}
\tag{4.7}
$$
原 first 的选位幅度为 $O(N^{-1})$，故从这些池每池选 $r\asymp\sqrt N$ 位时，两行绝对选位和都一致有界，实际甚至趋零。
这些是原物理位集合，未重排原算子或原常数。

## 5. 常数单位方向的真正矩阵块输入

以下是
[R236 多辅助矩阵 §§5—8](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)
的有限顶部恒等式，但不再引用其中“核内 first 有界”的步骤。
自然域和增长一律使用 (3.7)—(3.9) 及已发布的正则引理。

取一块 $B=(p_1,\ldots,p_K)$，每池一个位，记
$$
\Xi_B=[\xi_{p_1}\ \cdots\ \xi_{p_K}],\qquad
\beta_B=\frac14\Xi_B^{-1}e_{\omega_*}.
\tag{5.1}
$$
令 $u_p=t_pN_p$。
原高位符号差的一次系数准确为
$$
L_p=4\sum_{\omega\in\Omega_D}
\xi_{\omega p}\,\partial_{Z_\omega}P.
\tag{5.2}
$$
每个 (3.3) 的局部修正包含至少二阶 $u_p$，故没有平方零一次项。
定义有界交换块输入
$$
\boxed{
Q_B=c_*^{-1}
\sum_{\ell=1}^K\beta_{B,\ell}
\prod_{\substack{1\le h\le K\\h\ne\ell}}u_{p_h}\in A'.
}
\tag{5.3}
$$
其位次数为 $K-1$；没有任何未支付的无界偏导逆。

在这块的平方零商中，
$$
\left(\sum_{\ell=1}^K u_{p_\ell}L_{p_\ell}\right)Q_B
=c_*^{-1}\left(\sum_{\ell=1}^K\beta_{B,\ell}L_{p_\ell}\right)
\prod_{\ell=1}^Ku_{p_\ell}
=\prod_{\ell=1}^Ku_{p_\ell}.
\tag{5.4}
$$
最后一步是 (5.1)、(5.2)、(3.6) 的全空间常数恒等式。
这里暂用平方零商只为列出唯一顶部；下一节会把重复位还原成真实 carry。

取
$$
r=r_N=\lfloor\sqrt N\rfloor.
$$
从每池选 $r$ 位，按原物理顺序作一个固定匹配，组成 $r$ 个块；
不额外计算所有匹配。
记其总位集为 $E$，$|E|=Kr$，以及
$$
Q_E=\prod_{\text{固定 }r\text{ 块}}Q_B.
\tag{5.5}
$$
全部行系数全局有界，$|t_p|$ 与其倒数一致有界，有限余子式给实际绝对输入成本
$$
\boxed{
H_N\le(C_{D,k,w,F}\Delta_N^{-1})^r,\qquad
\log H_N=O(r\log N).
}
\tag{5.6}
$$
该量控制完整 $N_p$ 单项式展开，不用可能相消后的算子范数代替它。
$Q_E$ 是有界交换子，故
$$
Q_E\mathcal R_rf\in M\cap\mathcal D_{q_r}\quad(f\in M).
\tag{5.7}
$$

## 6. 从平方零顶部返回实际算子和准确域

令 $J_E=\prod_{p\in E}M_{\chi_p}$。
取带帽变量为在原实际局部公式中仅把选中位 $t_pN_p$ 变成 $-t_pN_p$。
完整反射与带帽公式的差由正则引理 §4 的最高物理位壳支付：
$$
\varepsilon_N\le C e^{-c16^{4N-1}}.
\tag{6.1}
$$
联合导数先按两正未居中 first 计算，再用真正的
$\operatorname{ad}_{H_{a,w}},\operatorname{ad}_{H_{b,w}}$
卷积转到倾斜 first；并未假设误差壳与这些扰动交换。

在核内深输入 (5.7) 上，带帽 $P$ 的常数项是原 $P$，作用为零。
每次差分至少一次，$r$ 次提升与次数 $(K-1)r$ 的输入相乘：
任何一个提升若使用二次以上项，或者同一块收到两次，都会出现重复位。
只有每块恰好得到一次时存活，(5.4) 给唯一顶部
$$
r!\,t_EN_E,\qquad
t_E=\prod_{p\in E}t_p,\quad N_E=\prod_{p\in E}N_p.
\tag{6.2}
$$
$r!$ 是提升各块的次序数，与匹配数无关。

对实际算子，重复位用
$$
N_p^2=\eta_pN_{p+1},\qquad
\eta_p\le e^{-770\,16^p}
$$
支付。
实际有理局部因子的二阶余项也有同一个因子，余下的逆统一有界。
所有有限系数多项式的无界 first 总次数至多 $Dr$。
反射和正规排序的每个原 first 字或者留在右侧，或者变成一次系数导数，故不增加这个总数。
统一 $4Dr$ 的预算小于 $q_r$；
(3.9) 和正则引理 §5 给额外费用至多 $\exp[Cr\log(r+2)]$。

原自然作用次序严格为
$$
\mathsf T^r J_EQ_E\mathcal R_rf
=J_E(\gamma_E\mathsf T)^r Q_E\mathcal R_rf.
\tag{6.3}
$$
其每个中间向量都由上述有限词预算属于所需自然域；
自然 $P$ 在这些输入上等于原最大 $\mathsf T$。
先在核内消去原常数项及 (5.4) 的单位，再作用最左 $J_E$。
由 $J_EE_E=(-1)^{Kr}E_E$，最终得到
$$
\boxed{
\mathsf T^r J_EQ_E\mathcal R_rf
=(-1)^{Kr}r!t_EE_E\mathcal R_rf+\mathcal E_{E,N}f.
}
\tag{6.4}
$$
误差由
$$
\|\mathcal E_{E,N}f\|
\le
(\varepsilon_N+\eta_{4N})
e^{Cr\log(r+2)}H_N\|f\|
+C r!|t_E|Kr\,\eta_{4N}\|f\|
\tag{6.5}
$$
主控；放宽固定常数无碍。
前项含所有反射导数、重复位及原系数多项式费用，后项是把实际 $N_E$ 与纯 $E_E$ 比较的费用。
不把纯位模型的恒等式直接当作原算子等式。

### 6.1 全部池阶乘与弱极限

定义实际有界输入平均
$$
\boxed{
\mathcal V_N=(-1)^{Kr}(r!)^{K-1}(2/N)^{Kr}
\sum_{\substack{J_\ell\subset I_{\ell,N}\\|J_\ell|=r\ (1\le\ell\le K)}}
t_E^{-1}J_EQ_E.
}
\tag{6.6}
$$
$K$ 个组合数及该前因子准确给
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=\max\left(1,\frac{C^{Kr}}{r!}H_N\right),\qquad
\boxed{\log A_N=O(r\log N)=o(r^4).}
\tag{6.7}
$$
顶部分别再得到一个 $r!$，总计为 $(r!)^K$，恰好是每个池各自的 $r$ 次平均。
置
$$
C_{\ell,N}=\frac2N\sum_{p\in I_{\ell,N}}E_p,\qquad
\mathcal C_N=\prod_{\ell=1}^KC_{\ell,N}^{\,r}.
$$
于是 (6.4)—(6.7) 给
$$
\boxed{
\|\mathsf T^r\mathcal V_N\mathcal R_rf
-\mathcal C_N\mathcal R_rf\|\longrightarrow0
\quad(f\in M).
}
\tag{6.8}
$$
双指数 carry 足以支付完整平均的绝对费用，不要求 $\mathcal V_N$ 一致有界。

纯池平均满足
$$
\|\mathcal C_N\|\le(1+1/N)^{Kr},
$$
且在固定有限柱之间，其矩阵系数准确为
$$
\left(\frac{(N)_r}{N^r}\right)^K\longrightarrow e^{-K/2}.
$$
全部池移向原物理高位，因此有限柱稠密及一致范数界给
$$
\mathcal C_N\rightharpoonup e^{-K/2}I.
\tag{6.9}
$$
由 $\mathcal R_rf\to f$ 和 $\sup\|\mathcal C_N\|<\infty$，
(6.8) 得到真正非零的弱极限
$$
\boxed{
\mathsf T^r\mathcal V_N\mathcal R_rf
\rightharpoonup e^{-K/2}f.
}
\tag{6.10}
$$
这里没有将越来越强的固定预解幂当作强单位，也没有让未正则化的核向量免费进入高阶自然域。

## 7. 固定局部四次界排除原规范核

固定任意局部全矩阵 $D_0$。
原实际有限低头差可准确提出一个 $A$，所以正则引理 §6 给共同自然域上的
$$
P=P_{\mathrm{tail},h}+A\,U_h(Z_{10},Z_{01}),
\qquad \deg U_h\le D.
$$
全部系数为实际有界交换子，尾与 $D_0$ 完整域交换。
在 $\operatorname{ad}_P^rD_0$ 的展开中保留两侧 $A$ 幂，再逐项把 first 字移过固定 $D_0$；
R109 的原四次幂界及 (3.9) 给
$$
\boxed{
\|(\operatorname{ad}_{P}^{r}D_0)
\mathcal V_N\mathcal R_rf\|
\le
A_N
e^{-5r^4/6+105r^3+C_{D,D_0}r\log(r+2)}
\|f\|\longrightarrow0.
}
\tag{7.1}
$$
(6.7) 支付新增的全部矩阵逆成本。
这里的估计针对实际深域输入，不声称整个无界交换子在全空间有界。

对任意 $f,g\in M$，全部自然中间词已由 $q_r$ 预算支付。
使用原全空间的完整 $C$ 自伴性及 $\mathsf Tg=0$，得
$$
B(D_0\mathsf T^r\mathcal V_N\mathcal R_rf,g)
=(-1)^r
B((\operatorname{ad}_P^rD_0)\mathcal V_N\mathcal R_rf,g).
\tag{7.2}
$$
不要求 $CM=M$，不把 $D_0$ 当作保核，也不把任何正则器的伴随移入未知核。
右侧由 (7.1) 趋零，左侧由 (6.10) 趋于
$$
e^{-K/2}B(D_0f,g).
$$
所以
$$
B(D_0f,g)=0\qquad(f,g\in M,\ D_0\text{ 任意局部全矩阵}).
\tag{7.3}
$$
实际 Haar 局部全矩阵代数不可约。
若 $f\ne0$，其局部轨道线性张成稠密；(7.3) 迫 $Cg=0$ 对所有 $g\in M$，矛盾。
因此
$$
\boxed{\ker\mathsf T=0.}
$$

R186 的完整 $C$ 自伴性给 $\overline{\operatorname{Ran}\mathsf T}=H$。
$e^w$ 循环且其多项式轨道是 $\mathsf T$ 的实际图核心，
由 (3.5) 得 $F(u,z)e^w$ 循环。
若它为零，则非零 $e^w\in\ker\mathsf T$，同样矛盾。
定理全部得证。

## 8. 与旧零中心障碍的准确关系

[完全居中梯度尾稿](R150-appendix-centered-critical-powers-gradient-tail-cancellation-and-nonzero-parameters.md)
已经处理全部非零参数，并证明：在指定梯度／二阶尾预算下，任意合法物理位集的中心仍趋零。
本稿不改变那条证明，也不声称在相同柱预算内找到了非零中心。

新测试改变了输入和配对：
先在原规范核中用真正强趋单位的变化正预解幂取得 $O(r)$ 层自然域，
再用全部有限矩池的全空间常数偏导方向提升；
最后以原局部双侧 $A$ 四次成本配对。
原 first 在核内可以仍无界。
因此无需以非零标量中心或端点多圆盘单位作为前提。

原端点稿对
$z^L+\epsilon z^{L+k}(z^k-u)$ 的小 $\epsilon$ 全参数范围，
及外盘结论，在这同一两行上现在都由 (1.3) 完整覆盖；
多于两个独立模式、一般无矩阵池的原行及无限模式不由此自动覆盖。
本稿没有从这些有限多项式向量的稠密性推到任意向量循环，也没有把实际正常见证源预算或普通 ISP 主目标写成已经完成。

## 9. 依赖与可复核接口

- [变化正预解幂与实际核内混合 jets](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)：未居中正 first、实际倾斜、原最大核保持、线性词深度、联合导数壳及原 $C$ 配对。
- [R236 普通点态矩逆](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md) §§3—4：有限 $\phi/\psi$ 逆、准确最高矩常数偏导；本稿另付其原来缺少的第二无界方向。
- [R236 多辅助矩阵](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md) §§5—9：每块缺位输入、固定匹配、全部阶乘与反射符号；本稿用变化正则器替换核内有界 first。
- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §§2—6、10：共同自然词、规范最大图、完整 $C$ 自伴、任意复 $\ell^2$ 权下的实际 Bell 与图核心。
- [R260](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) §§2—4、9：真实最高物理位壳与原局部两侧 $A$ 因子。

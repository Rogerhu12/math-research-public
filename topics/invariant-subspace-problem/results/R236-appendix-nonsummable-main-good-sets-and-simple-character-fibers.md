# R236 附录：任意非可和主行的简单字符纤维与普通二次循环性

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
状态：已证明。
主行只须 $\ell^2\setminus\ell^1$，全部有限个辅助只须 $\ell^1$。
本稿不要求主／辅助逐位比较、排序正则性或矩阵行列式。
结论针对简单主字符根；一般重数根与完整 Hilbert ISP 仍需继续。

## 1. 准确目标

取
$$
a,b\in\ell^2,\qquad a\notin\ell^1,\qquad
c_\nu\in\ell^1\quad(1\le\nu\le d),
$$
其中允许 $d=0$。
令
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v_\nu=\sum_jc_{\nu j}(\chi_j-1),\qquad
w=b_*+\sum_jb_j\chi_j.
$$
给定
$$
F(U,V)=\sum_{k=0}^p f_k(V)U^k,\qquad
p\ge1,\qquad f_p(0)\ne0.
\tag{1.1}
$$
记
$$
q_0(z)=F(z,0).
$$
它的次数恰为 $p$。

**定理 1（普通点态简单纤维）。**
若 $q_0(z)-\lambda$ 的全部根都是简单根，则
$$
\boxed{
[F(u,v)-\lambda]e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{1.2}
$$
全部相位、物理排列和有限低头均任意。
没有假设辅助在主行零位消失。

**定理 2（准确共振简单纤维）。**
若 $\mathfrak F_F$ 为同一有限行列表的准确多行共振变换，
在相同简单根假设下也有
$$
\boxed{
(\mathfrak F_F-\lambda)e^w\text{ 非零且循环}.
}
\tag{1.3}
$$

两个结论使用同一个自动好集。
普通结论通过已证有限矩逆变换进入真实共振实现，
没有删除普通 Bell 修正。

## 2. 删除任意相对大辅助后，主行仍不可和

固定 $\varepsilon>0$。
置
$$
b_j^{\rm aux}=\sum_{\nu=1}^d|c_{\nu j}|,
$$
$$
G_\varepsilon=
\{j:a_j\ne0,\ b_j^{\rm aux}\le\varepsilon|a_j|\}.
\tag{2.1}
$$
在坏集 $a_j\ne0$、$b_j^{\rm aux}>\varepsilon|a_j|$ 上，
$$
\sum_{\rm bad}|a_j|
\le\varepsilon^{-1}\sum_{\nu=1}^d\|c_\nu\|_1<\infty.
\tag{2.2}
$$
所以
$$
\boxed{\sum_{j\in G_\varepsilon}|a_j|=\infty.}
\tag{2.3}
$$
主行零位上的辅助不需要估计，也不会入选。

把好集上的非零主幅度递减排序，记为
$\rho_n^{(\varepsilon)}$。
对任意固定 $s>1$，有无穷多个整数 $N$ 满足
$$
\boxed{\rho_N^{(\varepsilon)}\ge N^{-s}.}
\tag{2.4}
$$
否则最终 $\rho_n^{(\varepsilon)}<n^{-s}$，
会使 (2.3) 中的和有限。
这里不仅有一个种子，而有任意大的种子。

## 3. 对角选取和真实双删除

固定任意 $\varepsilon_k\downarrow0$，例如 $1/k$。
依次在每个 $G_{\varepsilon_k}$ 上选一个满足 (2.4) 的
$$
N_k>N_{k-1},\qquad N_k\to\infty.
$$
还可以要求 $N_k$ 超过任何此前已指定的有限阈值。
每一步的好集不同，但 $s>1$ 在全部步骤中固定。

从该好集的前 $N_k$ 个主排序位开始，删除：

- 整个主行的最大 $\lfloor N_k/4\rfloor$ 个非零幅度所在物理位；
- 原物理位小于 $m_k=\lfloor N_k/4\rfloor$ 的项。

两次合计最多删去 $N_k/2$ 项。
在余项中保留
$$
Q_k=\lfloor N_k/2\rfloor
$$
位，组成真实集合 $I_k$。
有
$$
\boxed{
\begin{gathered}
\min I_k\ge m_k,\qquad
N_k^{-s}\le|a_j|\le3\|a\|_2N_k^{-1/2}\quad(j\in I_k),\\
\sup_{j\in I_k}\frac{\sum_\nu|c_{\nu j}|}{|a_j|}
\le\varepsilon_k\longrightarrow0.
\end{gathered}
}
\tag{3.1}
$$
幅度下界来自好集排序，幅度上界来自整个主行的排序，
两者没有混为同一种重排。
删除保持全部相对辅助界。

固定 $\theta>0$ 并置
$$
r_k=\lceil\sqrt{N_k/\theta}\rceil.
$$
任意 $E\subset I_k$、$|E|=r_k$ 都满足
$$
\sum_E|a_j|\le C_\theta,
\qquad
\sum_E|c_{\nu j}|\le\|c_\nu\|_1.
\tag{3.2}
$$

## 4. 普通目标的准确有限矩实现

令 $D$ 为 $F$ 的总次数。
把全部有限矩行
$$
a_j^{\omega_0}\prod_{\nu=1}^d c_{\nu j}^{\omega_\nu},
\qquad 2\le|\omega|\le D,
$$
加入为居中可和辅助。
主行之外的所有行都可和。

沿用普通矩展开稿的准确有限多项式
$$
Q_F=
\left.
F(\partial_t)
\exp\left[
\sum_{\nu=0}^dt_\nu Z_{e_\nu}
+\sum_{2\le|\omega|\le D}
\frac{(-2)^{|\omega|-1}}{\omega!}t^\omega Z_\omega
\right]\right|_{t=0}.
\tag{4.1}
$$
由
$$
\phi(z)=(1-e^{-2z})/2,\qquad
\psi(z)=-\tfrac12\log(1-2z),\qquad \psi\circ\phi=z,
$$
其扩展行共振变换准确等于普通点态 $F(u,v)$。
所有补偿至少二阶，均绝对可和，未使用 $\sum a_j$。

相应实际自然算子写作
$$
T_\lambda=P_Q(X,\mathbf Y;\mathbf G)-\lambda I,
\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p,
\tag{4.2}
$$
其中所有新增 first 辅助 $\mathbf Y$ 有界，
所有明确的二阶以上混合修正 $\mathbf G$ 属于 $\mathcal G$。
真实最高主系数的字符仍为 $f_p(0)\ne0$，因为
$$
Q_F(U,0)=F(U,0).
\tag{4.3}
$$
R176/R186 给完整闭自然图、原 $C$ 自伴和 $e^w$ 的循环图核心，
并有真正域等式
$$
T_\lambda e^w=[F(u,v)-\lambda]e^w.
\tag{4.4}
$$

对准确共振目标则直接取其原多行实现；
不需加入额外矩。
以下统一把所用的有限多项式记为 $P$、
主外所有可和系数行记为 $\eta_{\ell j}$。
两种实现的字符多项式均为 $q_0$。

## 5. 所有非主行在好集上都相对趋零

原辅助行已经由 (3.1) 给出这一性质。
对新增矩行 $|\omega|=n\ge2$，在 $j\in I_k$ 上，
$$
\begin{aligned}
\frac{
|a_j|^{\omega_0}\prod_\nu|c_{\nu j}|^{\omega_\nu}
}{|a_j|}
&=
|a_j|^{n-1}
\prod_\nu\left|\frac{c_{\nu j}}{a_j}\right|^{\omega_\nu}\\
&\le
|a_j|^{n-1}
\max(1,\varepsilon_k^D).
\end{aligned}
\tag{5.1}
$$
因此全部有限个非主系数行满足
$$
\boxed{
\delta_k:=
\max_\ell\sup_{j\in I_k}
|\eta_{\ell j}/a_j|
\longrightarrow0.
}
\tag{5.2}
$$
这里各个高矩至少多出一个主幅度因子
$O(N_k^{-1/2})$。
无需知道好集在整个排序中的密度，
也无需知道原主行的任何全局衰减下界。

## 6. 简单根块上的固定真实 Neumann 逆

反设 $M=\ker T_\lambda\ne0$。
原最大图定理给
$$
M\subset\mathcal D_\infty(X),\qquad X_M\in B(M),
$$
$$
\sigma(X_M)\subset\{z:q_0(z)=\lambda\}.
$$
按有限根作 Riesz 分块。
固定任意非零块 $M_\mu$，其主谱为 $\{\mu\}$。

令
$$
D_0=P_X(X_{M_\mu},\mathbf Y;\mathbf G),\qquad
D_\ell=P_{Y_\ell}(X_{M_\mu},\mathbf Y;\mathbf G).
\tag{6.1}
$$
所有这些算子都在该块上有界并相互交换。
简单根假设给
$$
\chi_\mu(D_0)=q_0'(\mu)\ne0.
$$
由于其余零字符系数与 $X_M-\mu I$ 都交换拟幂零，
$$
\boxed{D_0\in B(M_\mu)^\times.}
\tag{6.2}
$$

准确高位一次系数为
$$
L_j
=4a_jD_0+4\sum_\ell\eta_{\ell j}D_\ell
=4a_j
\left(D_0+\sum_\ell(\eta_{\ell j}/a_j)D_\ell\right).
\tag{6.3}
$$
这个式子对普通目标成立，是因为它已经被实际转成了共振实现；
所有混合 $G$ 的符号差至少二次，不贡献这里的一次系数。

由 (5.2)，对于充分大的 $k$，
$$
\left\|
D_0^{-1}\sum_\ell(\eta_{\ell j}/a_j)D_\ell
\right\|\le\frac12
\quad(j\in I_k).
$$
所以真正的核内 Neumann 逆满足
$$
\boxed{\|L_j^{-1}\|\le C_{M_\mu}|a_j|^{-1}
\le C_{M_\mu}N_k^s.}
\tag{6.4}
$$
选池在知道未知块之前已固定；
只是“充分大”的起点可以依赖固定块的逆范数。
没有在全空间假设这些系数具有同一逆。

对 $|E|=r_k$，定义准确乘积逆
$$
\mathfrak R_E=\prod_{j\in E}L_j^{-1}:M_\mu\to M_\mu.
$$
它保持核、全部深域和全部交换系数，并且
$$
\boxed{
\log^+\|\mathfrak R_E\|
\le s r_k\log N_k+C_{M_\mu}r_k.
}
\tag{6.5}
$$
这里既没有全空间预解成本，也没有结果式或矩阵行列式成本。

## 7. 实际提升与单池有界弱平均

先令 $h_E=\mathfrak R_Ef\in M_\mu$，再作用
$$
J_E=\prod_{j\in E}M_{\chi_j}.
$$
全部自然 jets 先由核内有界 $X_M$ 支付。
(3.2) 与任意跨度的真实导子估计再给
$$
\|X^nJ_Eh_E\|
\le2R_{D,M_\mu,\theta}^n\|h_E\|
\qquad(0\le n\le4Dr_k).
\tag{7.1}
$$
所有混合系数来自有限个可和矩行与明确局部多项式，
完整壳误差为
$$
\mathfrak e_k\le C_D e^{-385\,16^{m_k-1}},
$$
有限词重排最多付
$e^{C_{D,\theta}r_k\log(r_k+2)}$。

平方零顶部恒等式和实际 carry 给
$$
T_\lambda^{r_k}J_E\mathfrak R_Ef
=(-1)^{r_k}r_k!t_EE_Ef+\mathcal E_Ef.
\tag{7.2}
$$
准确顺序仍为
$$
T_\lambda^{r_k}J_E\mathfrak R_Ef
=
J_E(\gamma_ET_\lambda)^{r_k}\mathfrak R_Ef.
$$
先在原核内取消 $\prod L_j$，再施最左反射；
不假设反射保持核。

令
$$
\mathcal V_k=
(-1)^{r_k}(2/Q_k)^{r_k}
\sum_{\substack{E\subset I_k\\|E|=r_k}}
t_E^{-1}J_E\mathfrak R_E.
\tag{7.3}
$$
组合数与 (6.5) 给
$$
\|\mathcal V_k\|\le A_k,\qquad
\log A_k\le s r_k\log N_k+C_{M_\mu}'r_k+C.
\tag{7.4}
$$
实际误差至多为
$$
\mathfrak e_k e^{C_{D,\theta}r_k\log(r_k+2)}A_k
+C2^{r_k}r_k\eta_{m_k},
$$
故趋零。
纯单池平均具有一致范数界，固定有限柱系数为
$$
(Q_k)_{r_k}/Q_k^{r_k}\longrightarrow e^{-1/\theta}.
$$
于是
$$
\boxed{
T_\lambda^{r_k}\mathcal V_kf
\rightharpoonup e^{-1/\theta}f.
}
\tag{7.5}
$$

对固定局部全矩阵 $D_*$，真实有限头分解每次提出一个 $A$，
其余多项式主阶至多 $p$。
(7.1) 给
$$
\|(\operatorname{ad}_{T_\lambda}^{r_k}D_*)\mathcal V_kf\|
\le
2\|D_*\|A_k C_{D,D_*,M_\mu,\theta}^{r_k}
e^{-5r_k^4/6+105r_k^3}\|f\|.
\tag{7.6}
$$
由 (7.4)，
$$
\log A_k=O(\sqrt{N_k}\log N_k)=o(r_k^4).
$$
所以任意固定 $\theta>0$ 都足以使 (7.6) 趋零。

原完整 $C$ 配对、$T_\lambda g=0$ 与 (7.5) 给
$$
\mathcal B(D_*f,g)=0
$$
对同一块中全部 $f,g$ 和全部局部矩阵成立。
局部不可约性迫 $M_\mu=0$。
各有限根块逐一排除，遂有 $\ker T_\lambda=0$。

完整 $C$ 自伴给稠密像，真实循环图核心给 (1.2) 和 (1.3)。
两定理得证。

## 8. 与共同例外根结合后的准确约束

共同例外根定理说明：
若同一非可和主 first 的某个有限谱部分存在，
全部非零自然多项式核共享一个标量 $r_X$。
对于本稿的普通或准确共振目标，
任何实际坏位移仍必须满足
$$
\lambda=q_0(r_X).
$$
本稿进一步给必要条件
$$
\boxed{q_0'(r_X)=0.}
\tag{8.1}
$$
确实，如果这个实际根为简单根，
只在对应根块使用 §§2–7 即可排掉它；
不需要其他标量根也是简单的。

对普通目标，另有原首位切片碰撞条件；
对共振目标，另有对应的共振首位条件。
(8.1) 不取代这些已证条件，也不把共同根的存在当作已知。

## 9. 普通二次多项式对全部非可和主行闭合

取任意非恒定二次标量多项式
$$
q(z)=Az^2+Bz+C,\qquad A\ne0,
$$
以及任意 $\lambda$。

如果 $q(z)-\lambda$ 有两个不同根，
定理 1（无辅助）立即给
$$
(q(u)-\lambda)e^w\text{ 循环}.
$$
如果它只有一个二重根 $r$，则
$$
q(z)-\lambda=A(z-r)^2.
$$
主行有非零首系数 $\alpha=a_{j_a}$；
旧 R144/R147 的两个切片
$(z-r)^2$ 与 $(z-r-2\alpha)^2$ 没有共同根，
因此这个情形早已关闭。

所以
$$
\boxed{
(q(u)-\lambda)e^w
\text{ 对任意 }a\in\ell^2\setminus\ell^1,
\text{全部二次 }q,\lambda,w\text{ 循环}.
}
\tag{9.1}
$$
特别，先前的普通临界二次
$$
(u^2-\alpha^2)e^w
$$
在任意非可和主行上都闭合。
这里扣除了旧单根平移幂部分；
新增范围是无需规则排序或熵假设的一般非可和简单两根部分。

对于已有 R259/R268/R269 覆盖的规律主行，
不把该重叠范围重新登记为新增。

## 10. 没有自动得到的内容

本稿不把
$$
(F(u,v)-\lambda)^m e^w,\qquad m>1,
$$
从单次循环直接推出。
该点态幂的字符根通常具有重数，
其主偏导在根上为零，(6.2) 的固定单位不再存在。

虽然有限矩展开给更高阶的常数矩方向，
要使用多个方向仍须真实兼容的矩阵池或另一个明确输入；
单池中的不同小主幅度不能自动称为满幂矩阵。

可和主行不保证 (2.3)，
所以这里的自动好集种子不能外推到所有 $\ell^1$ 行。
此前可和超指数族的实际预算边界仍然有效。

一般最高系数字符为零的自然多项式、
多个独立无界慢方向、任意非解析闭包及完整 ISP 均未由此关闭。

## 11. 来源

- [普通矩展开源](../notes/2026-11-13-ordinary-pointwise-moment-expansion-veronese-pools-and-reserve-sites-central-review.md)：
  准确 $\phi/\psi$ 有限逆、全部多变量阶乘、主最高字符与真实普通目标。
- [多辅助矩阵块源](../notes/2026-11-13-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages-central-review.md)：
  多行实际混合 jets、固定低头 $A$ 因子与完整自然域配对。
- [辅助公共半径源](../notes/2026-11-13-auxiliary-scale-joint-resolvent-arbitrary-l2-main-and-tail-gaps-central-review.md)：
  单池核内乘积逆的正确左反射次序及精确有界弱平均。
- [R176](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  核内有界 first、Riesz 根块、原完整 $C$ 自伴及循环图核心。
- [共同例外根定理](R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)：
  不同自然核和权共享同一个可能根。
- [R144](R144-first-mode-shift-resultant-cyclicity.md)、
  [R147](R147-exponential-weighted-first-mode-polynomial-cyclicity.md)：
  已闭的单根平移幂与原首位切片范围。
- [R260](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意跨度实际导子与四次局部预算。

本稿新增的是任意有限可和辅助下仍保非可和的好集、
任意大多项式种子的对角选择及全部新矩比值的一致趋零，
由此得到真正固定的核内 Neumann 逆。

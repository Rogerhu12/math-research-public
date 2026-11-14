# R150 附录：复对数模式的合并矩池、最高齐次符号与所有高阶共振零参数

日期：2026-11-13（UTC）。normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；root 与 boundary 全文独立核查。
本稿只使用原 Haar 上的实际 first、原复中心常数、完整普通 Bell 与正分量预解。
它不要求未合并的全 Veronese 矩列满秩。

## 1. 原复对数模式及结论

固定有限个两两不同复数
$$
\rho_1,\ldots,\rho_q,\qquad \operatorname{Re}\rho_\nu>0.
$$
全部复幂采用正实对数底：
$x^\rho=\exp(\rho\log x)$，$x>0$。
定义原系数行
$$
a_{\nu p}=
\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2},
\qquad
u_{\rho_\nu}=-\kappa_{\rho_\nu}
+\sum_{p\ge0}a_{\nu p}\chi_p.
\tag{1.1}
$$
这里的固定复常数由原行准确确定：
$$
\sum_{p<n}a_{\nu p}
=S^{\rho_\nu}+\kappa_{\rho_\nu}
+O(n^{-1}S^{\operatorname{Re}\rho_\nu-1}),
\qquad S=\log(n+2).
\tag{1.2}
$$
它来自 $f_\rho(x)=\rho(\log x)^{\rho-1}/x$ 的导数绝对积分误差；不对复行声称单调，也不使用实指数的中心常数。

取非恒定标量多项式 $F\in\mathbb C[x_1,\ldots,x_q]$，普通总次数为 $D\ge1$，最高普通齐次部分记作 $F_D$。
定义有限指数多项式
$$
\boxed{
H_F(t)=F_D(\rho_1t^{\rho_1},\ldots,\rho_qt^{\rho_q}),
\qquad t>0.
}
\tag{1.3}
$$

**定理。** 若 $H_F$ 不恒为零，则对任意非零一变量多项式 $Q$、任意复 $\ell^2$ 指数权
$$
w=w_*+\sum_pw_p\chi_p
$$
都有
$$
\boxed{
Q(F(u_{\rho_1},\ldots,u_{\rho_q}))e^w
\ne0,\qquad
[Q(F(u_{\rho_1},\ldots,u_{\rho_q}))e^w]_A=H.
}
\tag{1.4}
$$
因此包含全部 $[F(u)-\lambda]^r e^w$，$\lambda\in\mathbb C$、$r\ge1$。
对非零常数目标直接使用 $e^w$ 循环；不把常数 $F=\lambda$ 的零向量纳入全参数量词。

条件 (1.3) 是有限可核验条件：在最高齐次部分中按相同复指数 $\rho\cdot\omega$ 分组，然后检查各组的有限系数和是否全为零。
本稿不把这个充分条件称为必要条件。

## 2. 真实相同矩行的准确合并

令
$$
\Omega_D=\{\omega\in\mathbb N_0^q:1\le|\omega|\le D\},
\qquad
c_\omega=\prod_{\nu=1}^q\rho_\nu^{\omega_\nu},
$$
$$
d_\omega=|\omega|,\qquad
s_\omega=\rho\cdot\omega-d_\omega.
\tag{2.1}
$$
实际矩行准确满足
$$
\prod_\nu a_{\nu p}^{\omega_\nu}
=c_\omega\,m_{d_\omega,s_\omega}(p),
\qquad
m_{d,s}(p)=\frac{(\log(p+2))^s}{(p+2)^d}.
\tag{2.2}
$$
所以只按相同的键 $(d,s)$ 合并；不同 $d$ 不能因为部分渐近相同而合并。
设全部不同键构成有限集合 $\mathcal I_D$。

对 $d=1$，不同 $\rho_\nu$ 保证每组只有一个原 first，定义
$$
v_{1,\rho_\nu-1}=\rho_\nu^{-1}u_{\rho_\nu}.
\tag{2.3}
$$
它的真实常数项是 $-\kappa_{\rho_\nu}/\rho_\nu$，保留而不重置。
对 $d\ge2$，定义真正有界的居中模式
$$
v_{d,s}=\sum_pm_{d,s}(p)(\chi_p-1).
\tag{2.4}
$$
因为 $d\ge2$，该行绝对可和，不论 $s$ 的虚部和固定实部大小。
未合并的一阶模式另定义为 $v_{e_\nu}=u_{\rho_\nu}$；以下求和式只用于 $|\omega|\ge2$。若原扩展高矩为
$$
v_\omega=\sum_p\left(\prod_\nu a_{\nu p}^{\omega_\nu}\right)(\chi_p-1),
$$
则
$$
\boxed{
v_\omega=c_\omega v_{d_\omega,s_\omega}.
}
\tag{2.5}
$$
对 $|\omega|=1$，同一式由 (2.3) 准确成立。
这些是原函数的精确等式，不只是中心或尾等价。

### 2.1 倾斜和实际算子中的比例仍准确

令 $t_p=e^{-2w_p}$、$R_p=V(t_pN_p)$。
合并后的高矩实现为
$$
Z_{d,s}=\sum_pm_{d,s}(p)(R_p-I)\in\mathcal A
\quad(d\ge2).
\tag{2.6}
$$
它与每个未合并矩的倾斜实现仍准确相差标量 $c_\omega$。
$d=1$ 时，$Z_{1,\rho_\nu-1}$ 是 $u_{\rho_\nu}/\rho_\nu$ 的完整倾斜闭 first，等于原 $X_{u_{\rho_\nu},w}/\rho_\nu$。
非零标量倍、固定原常数和 $\ell^2\times\ell^2$ 的实际有界倾斜全部保留。

不能只在点态函数中合并矩，却在后续 Bell 中仍把原重复系数当成独立模式。
下面直接对合并后的列表重新构造完整生成式及全部系数。

## 3. 普通多项式的有限逆与合并后的完整 Bell

先在未合并的形式矩变量 $Y_\omega$ 中定义
$$
Q_F(Y)=
\left.
F(\partial_{t_1},\ldots,\partial_{t_q})
\exp\left[
\sum_{|\omega|=1}t^\omega Y_\omega+
\sum_{2\le|\omega|\le D}
\frac{(-2)^{|\omega|-1}}{\omega!}t^\omega Y_\omega
\right]\right|_{t=0}.
\tag{3.1}
$$
给 $Y_\omega$ 权 $|\omega|$，此多项式的权次及普通次数至多 $D$。
原
$$
\phi(z)=(1-e^{-2z})/2,\qquad
\psi(z)=-\tfrac12\log(1-2z),\qquad
\psi(\phi(z))=z
$$
有限 jets 计算给
$$
\mathfrak F^{\mathrm{ext}}_{Q_F}=F(u_{\rho_1},\ldots,u_{\rho_q}).
\tag{3.2}
$$
所有非线性系数至少含两个 $\ell^2$ 因子，所以绝对收敛。
本步没有出现可能发散的 $\sum_pa_{\nu p}$。

现在作准确有限线性代入
$$
\boxed{
\overline Q_F(W)=
Q_F\bigl((c_\omega W_{d_\omega,s_\omega})_{\omega\in\Omega_D}\bigr).
}
\tag{3.3}
$$
用 $W_{d,s}$ 的权 $d$，代入仍保持全部有限权次。

为核完整共振变换，给未合并列表参数 $z_\omega$。
它的实际线性项与每个位的参数和分别是
$$
\sum_\omega z_\omega v_\omega
=\sum_{g\in\mathcal I_D}\theta_g v_g,\qquad
\sum_\omega z_\omega\xi_{\omega p}
=\sum_{g\in\mathcal I_D}\theta_g m_g(p),
$$
$$
\theta_g=\sum_{\omega:(d_\omega,s_\omega)=g}c_\omega z_\omega.
\tag{3.4}
$$
因此其整个有限共振生成式恰为合并列表生成式对 $\theta(z)$ 的复合。
有限链式法则使 $\partial_{z_\omega}$ 准确变为
$c_\omega\partial_{\theta_{g(\omega)}}$。
由 (3.2)—(3.4)，得到
$$
\boxed{
\mathfrak F^{\mathrm{group}}_{\overline Q_F}
=F(u_{\rho_1},\ldots,u_{\rho_q}).
}
\tag{3.5}
$$

对合并列表直接定义实际混合系数
$$
G_\beta=
(-1)^{|\beta|-1}(|\beta|-1)!
\sum_p\left(\prod_{g\in\mathcal I_D}m_g(p)^{\beta_g}\right)
(R_p-I)^{|\beta|},
\qquad 2\le|\beta|\le D.
\tag{3.6}
$$
合并列表的每条行属于 $\ell^2$，故这些和按范数绝对收敛；每项包含至少二阶实际 $N_p$。
令
$$
\boxed{
P(W;\mathbf G)=
\exp\left(\sum_{2\le|\beta|\le D}
\frac{G_\beta}{\beta!}\partial_W^\beta\right)
\overline Q_F(W).
}
\tag{3.7}
$$
这是合并后重新构造的完整实际 Bell。
R186 的共同自然域与图核心给其规范最大实现 $\mathsf T$，并准确有
$$
\mathsf T^*=C\mathsf TC,\qquad
\mathsf Te^w=F(u_\rho)e^w.
\tag{3.8}
$$
若与未合并构造比较，两者在共同循环向量 $e^w$ 的整个多项式图核心上相同，故规范闭图也相同。
不从只在一个向量上的形式相等直接猜测最大域相等。

## 4. 合并后最高矩方向与条件 (1.3)

写
$$
F_D(x)=\sum_{|\omega|=D}f_\omega x^\omega.
$$
未合并的最高矩变量只有线性项，系数为
$(-2)^{D-1}f_\omega$。
因此对键 $g=(D,s)$，准确有
$$
\boxed{
\partial_{W_{D,s}}\overline Q_F
=(-2)^{D-1}
\sum_{\substack{|\omega|=D\\\rho\cdot\omega-D=s}}
f_\omega c_\omega
=:C_{D,s}.
}
\tag{4.1}
$$
该偏导是全局标量常数，而非某个未知字符根上的值。

另一方面
$$
H_F(t)=t^D\sum_{s:(D,s)\in\mathcal I_D}
\left(\sum_{\omega\text{ 同组}}f_\omega c_\omega\right)t^s.
\tag{4.2}
$$
不同复指数的函数 $t^s$ 在 $t>0$ 上线性无关：
置 $x=\log t$，对有限指数和 $\sum d_se^{sx}$ 在一个点取前若干阶导数，Vandermonde 矩阵可逆。
所以 (1.3) 等价于至少一个
$$
C_{D,s_*}\ne0.
$$
(3.7) 的正阶微分作用于常数均为零，故
$$
\boxed{\partial_{W_{D,s_*}}P=C_{D,s_*}I.}
\tag{4.3}
$$
这就是用于原矩阵提升的实际全空间单位方向。
无须让重复的矩行拥有虚假的独立逆。

## 5. 合并矩列表的实际跨池下界

对每个 $1\le d\le D$，把其不同指数记为
$$
s_{d,1},\ldots,s_{d,m_d},\qquad
K=\sum_{d=1}^Dm_d=|\mathcal I_D|.
$$
取 $K$ 个固定分离倍数的原物理池，例如
$$
I_{\ell,N}=\{(3\ell+1)N+j:0\le j<N\},
\qquad1\le\ell\le K.
\tag{5.1}
$$
每池 $N$ 位，最小物理位至少 $4N$。

令 $p_\ell\in I_{\ell,N}$ 任意，$t_\ell=(p_\ell+2)/N$、$L=\log N$。
全部节点分处固定不交正紧区间。
实际矩行是
$$
m_{d,s}(p)=
N^{-d}L^s\,t^{-d}
\left(1+\frac{\log t}{L}\right)^s.
\tag{5.2}
$$
先抽出完整复数行因子 $N^{-d}L^s$，不是只抽其模长。

固定 $d$，矩阵
$$
B^{(d)}_{j,h}=\binom{s_{d,j}}h,\qquad
1\le j\le m_d,\quad0\le h<m_d
\tag{5.3}
$$
可逆：各列是次数为 $h$、最高系数为 $1/h!$ 的多项式，在不同复节点 $s_{d,j}$ 求值。
用该矩阵的逆组合行，再把第 $h$ 行乘 $L^h$。
固定复杂指数的 Taylor 余项在所有节点紧区间上一致，得到
$$
L^h\sum_{j=1}^{m_d}
((B^{(d)})^{-1})_{h,j}
\left(1+\frac{\log t}{L}\right)^{s_{d,j}}
\longrightarrow(\log t)^h.
\tag{5.4}
$$
最大 $h=m_d-1$ 的余项仍为 $O(L^{-1})$。
这里的复变换不会把极限基函数变成复指数：
最终基恰为
$$
\boxed{t^{-d}(\log t)^h,\quad
1\le d\le D,\quad0\le h<m_d.}
\tag{5.5}
$$

置 $x=\log t$，这些函数成为实指数 $e^{-dx}x^h$。
逐次“除以一个指数、求导、Rolle 归纳”证明其任意非零实线性组合至多有 $K-1$ 个不同实零点；复关系取非零实部或虚部。
故任意跨池节点的极限矩阵都可逆。
分离紧区间上的连续性给统一正下界；(5.4) 的一致收敛把它传到真实矩阵。

准确计入行因子和块变换，令
$$
A=\sum_d d\,m_d,\quad
B=\sum_d\frac{m_d(m_d-1)}2,\quad
\Sigma=\sum_{(d,s)\in\mathcal I_D}\operatorname{Re}s.
$$
便有
$$
\boxed{
\Delta_N:=
\min_{p_\ell\in I_{\ell,N}}
\left|\det[m_g(p_\ell)]_{g,\ell}\right|
\ge c\,N^{-A}(\log N)^{\Sigma-B}.
}
\tag{5.6}
$$
特别
$$
\boxed{\log^+\Delta_N^{-1}=O(\log N).}
\tag{5.7}
$$

各 $d=1$ 行在池上的幅度为 $O(N^{-1}(\log N)^C)$，所以对充分大 $N$ 也是 $O(N^{-1/2})$。
每池选 $r=\lfloor\sqrt N\rfloor$ 位时，有限个 first 的选位绝对和均一致有界，实际趋零。
$d\ge2$ 的全部行另有固定全局 $\ell^1$ 界。
这些是完整矩阵池所需要的真实费用。

## 6. 多条复 first 的正分量预解，准确限定域

这里把临界双模式的正则引理写成所用的有限复行形式。
它直接来自 R186 §2 的正分量构造，不假定每条复 first 自己有预解。

把全部 $d=1$ 行的实部、虚部分别拆为正负部，删去零行，得到有限个非负 $\ell^2$ 行及其真实最大增生 first
$$
T_1,\ldots,T_J.
$$
$J$ 在 $N,r$ 之前固定。
原每条合并 first 在这些正分量的共同域上是它们的固定复线性组合，加原常数及固定有界倾斜。
不声称原共同域等于正分量的共同域。

令
$$
R(\epsilon)=\prod_{\nu=1}^J(I+\epsilon T_\nu)^{-1}\in A',
\qquad
q_r=(8D+8)r,\quad\epsilon_r=r^{-2},
$$
$$
\boxed{\mathcal R_r=R(\epsilon_r)^{q_r}.}
\tag{6.1}
$$
全部因子为交换收缩。
R186 (3.5) 的逐因子域支付给
$\mathcal R_rH$ 属于全部正分量长度至多 $q_r$ 的自然词域，且其词范数不超过 $(2/\epsilon_r)^s$。
因此每个原倾斜 first 词也真实有定义，满足
$$
\boxed{\|W(Z)\mathcal R_r\|\le(C+Cr^2)^s
\quad(s\le q_r).}
\tag{6.2}
$$
所有有界合并模式和 Bell 系数在 $A'$ 中，保持这些正分量共同域。

在稠密的正分量共同一阶域上，
$$
\|(\mathcal R_r-I)f\|
\le q_r\epsilon_r\sum_{\nu=1}^J\|T_\nu f\|\to0;
$$
收缩性将其延到全部 $H$。
规范核 $M=\ker\mathsf T$ 是 R186 有界核方程的核，故
$$
\boxed{
\mathcal R_r\to I\ {\rm SOT},\qquad
\mathcal R_rM\subset M
}
\tag{6.3}
$$
并同时支付所有所需有限正分量及原 first 词域。

对原高位反射误差，在这 $J$ 个正分量下使用联合导数范数
$$
\|B\|_\partial=
\sum_{\gamma\in\mathbb N_0^J}
\frac{\|\operatorname{ad}_{T_1}^{\gamma_1}\cdots
\operatorname{ad}_{T_J}^{\gamma_J}B\|}{\gamma!}.
$$
每个最高物理位为 $\ell$ 的真实误差壳仍为局部矩阵，
其模不超过 $C\eta_{\ell-1}$；
全部正分量头范数和至多 $C\sqrt{\ell+1}$。
所以同一实际壳证明给
$$
\|E_{E}\|_\partial
\le C\sum_{\ell\ge\min E}\eta_{\ell-1}e^{C\sqrt{\ell+1}}
\le C'e^{-c16^{\min E-1}}.
\tag{6.4}
$$
原复 first 的有限线性组合只增加固定几何常数；
有界倾斜的 $\operatorname{ad}_H$ 与这些正分量导数交换，但不必与误差壳交换，真正的二项式卷积仍给固定因子和阶乘界。

长度 $s$ 的反射词中，每个 first 字只会留在右侧或变成一次系数导数。
故 $r$ 次固定次数 $D$ 的提升、全部正规排序和局部配对只需要 $O(Dr)$ 个正分量字。
(6.2) 与联合阶乘预算给新增费用
$$
\exp[Cr\log(r+2)].
\tag{6.5}
$$
这里没有从未知核正则性推断 first 有界，也没有以每个原复 first 的空谱为前提。

## 7. 合并矩的顶部提升与原 C 排核

固定 $r=\lfloor\sqrt N\rfloor$。
每个跨池 $K$ 位块的实际矩阵是
$$
\Xi=[m_g(p_\ell)]_{g,\ell}.
$$
取目标方向 $g_*=(D,s_*)$，令
$$
b=\tfrac14\Xi^{-1}e_{g_*},\qquad u_p=t_pN_p.
$$
原差分一次系数为
$$
L_p=4\sum_g m_g(p)\partial_{W_g}P.
$$
由 (4.3)，有界交换块输入
$$
Q_B=C_{D,s_*}^{-1}
\sum_{\ell=1}^Kb_\ell\prod_{h\ne\ell}u_{p_h}
$$
在平方零商中准确满足
$$
\left(\sum_{\ell=1}^Ku_{p_\ell}L_{p_\ell}\right)Q_B
=\prod_{\ell=1}^Ku_{p_\ell}.
\tag{7.1}
$$
输入单位是一个非零标量；其余因子都在 $A'$。
$r$ 个固定匹配块的输入 $Q_E$ 先施于 $\mathcal R_rf\in M$，再在最左侧作物理反射 $J_E$。

全部输入绝对系数费用由 (5.7) 给
$$
H_N\le(C\Delta_N^{-1})^r,\qquad \log H_N=O(r\log N).
$$
$K$ 池平均的准确前因子仍为
$$
(-1)^{Kr}(r!)^{K-1}(2/N)^{Kr},
$$
且逐项另乘 $t_E^{-1}$。
原顶部是 $(-1)^{Kr}r!t_EE_E$；只有每块恰好收到一次提升才能达到平方零顶部。
其余项由真实 $N_p^2=\eta_pN_{p+1}$、(6.4) 和 (6.5) 处理。
这给有界输入平均 $\mathcal V_N$，其预算
$$
\log A_N=O(r\log N)=o(r^4),
$$
以及真正的弱极限
$$
\boxed{
\mathsf T^r\mathcal V_N\mathcal R_rf
\rightharpoonup e^{-K/2}f\qquad(f\in M).
}
\tag{7.2}
$$
原纯池平均一致有界，故 $\mathcal R_rf\to f$ 不被增长的输入费用放大。
自然 $P$ 与原最大 $\mathsf T$ 的每一步识别都在 (6.1) 已付的有限深域上进行。

对固定局部全矩阵 $D_0$，真实有限低头差提出一个 $A$：
$$
P=P_{\mathrm{tail},h}+A\,U_h(T_1,\ldots,T_J),
\qquad\deg U_h\le D
$$
于已付正分量共同词域上成立。
只对明确实际有限低头这样除以 $A$，不除完整慢系数。
原两侧 $A$ 四次幂界保留，(6.2)—(6.5) 给
$$
\|(\operatorname{ad}_P^rD_0)\mathcal V_N\mathcal R_rf\|
\le
A_N e^{-5r^4/6+105r^3+Cr\log(r+2)}\|f\|\to0.
\tag{7.3}
$$
由原全 $H$ 上的完整 $C$ 自伴性，
$$
B(D_0\mathsf T^r\mathcal V_N\mathcal R_rf,g)
=(-1)^rB((\operatorname{ad}_P^rD_0)
\mathcal V_N\mathcal R_rf,g),\qquad f,g\in M.
$$
没有使用 $\mathcal R_r^*$ 保核，也不要求 $CM=M$。
结合 (7.2)—(7.3)，得到 $B(D_0f,g)=0$ 对全部局部全矩阵。
其不可约性迫 $M=0$。
R186 的原图核心与 (3.8) 遂给 $F(u_\rho)e^w$ 非零且循环。

上述顶部、全部阶乘和真实反射顺序与
[临界双模式全多项式稿](R150-appendix-critical-logarithmic-two-mode-full-polynomials-and-zero-parameters.md)
§§5—7 相同；本稿新增的是原重复矩的准确合并、复指数池以及所需的有限正分量域。
它不是把一般满矩条件直接用于一个秩亏矩阵。

### 7.1 外层复合保条件，故全部位移与点态幂都包括

若 $Q$ 非恒定、次数为 $h$、最高系数为 $q_h$，则
$$
(Q\circ F)_{hD}=q_h F_D^h.
$$
因此
$$
H_{Q\circ F}(t)=q_hH_F(t)^h
$$
不恒零。
对整个 $Q\circ F$ 重新使用以上有限矩构造，证明 (1.4)。
非零常数 $Q$ 直接处理。
有限多个满足条件的 $F_i$ 的乘积也可同样对其整个最高部分应用；不通过点乘循环向量来推论。

## 8. 所有高阶简单零点共振族：零参数和全部复合，无次数阈值

固定整数 $R\ge2$，任意复数 $\mathfrak D$ 满足
$$
\operatorname{Re}\mathfrak D>0.
$$
取
$$
\rho_p=\mathfrak D/p,\qquad
c_p=\left[\prod_{\substack{1\le q\le R\\q\ne p}}
(1/p-1/q)\right]^{-1},
\qquad
G_R(x)=\sum_{p=1}^Rc_px_p^p.
\tag{8.1}
$$
$c_p\ne0$，所有 $\rho_p$ 两两不同。
该多项式的最高普通次数为 $R$，最高普通齐次部分只有
$$
(G_R)_R=c_Rx_R^R.
$$
所以
$$
\boxed{
H_{G_R}(t)=c_R(\mathfrak D/R)^R t^{\mathfrak D}\ne0.
}
\tag{8.2}
$$
合并后即使许多其他矩行相同，这个有限最高组系数仍非零。

定理给
$$
\boxed{
Q\left(\sum_{p=1}^Rc_p(u_{\mathfrak D/p})^p\right)e^w
\text{ 对任意非零 }Q\text{ 非零且循环}.
}
\tag{8.3}
$$
特别包含全部 $\lambda\in\mathbb C$、$r\ge1$ 的点态幂，**也包含零参数**。
不再需要旧严格条件 $\operatorname{Re}\mathfrak D<R$，
也不要求避开临界外盘；
$R$ 与 $\mathfrak D$ 只须固定有限，原每个模式和中心常数不变。

例如 $R=3$，除去共同非零系数后得到
$$
\boxed{
\left[
u_{\mathfrak D}
-4u_{\mathfrak D/2}^{\,2}
+3u_{\mathfrak D/3}^{\,3}
-\lambda
\right]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环},
\qquad \operatorname{Re}\mathfrak D>0.
}
\tag{8.4}
$$
这是对同一个原普通点态多项式重新构造完整 Bell 的结论。

若 $\operatorname{Im}\mathfrak D\ne0$，每个参与的原 first 都是全复平面连续谱。
确实对 $\rho=\mathfrak D/p$、$\sigma=\operatorname{Re}\rho>0$，
$$
\sum_{j<n}\bigl(|a_j^{(\rho)}|
-\operatorname{Re}(e^{-i\theta}a_j^{(\rho)})\bigr)
\ge\left(\frac{|\rho|}{\sigma}-1\right)S^\sigma+O(1)\to\infty
$$
对每个固定 $\theta$ 成立；用
[R138 完整分类](R138-first-chaos-complete-spectrum-classification.md)
即可。
本证明并未借用这些 first 的空谱预解；用的是各行正分量的真实预解。

## 9. 仿射独立指数时的全部多项式与范围边界

若原指数满足
$$
\sum_{\nu=1}^q n_\nu=0,\quad
\sum_{\nu=1}^q n_\nu\rho_\nu=0,\quad n_\nu\in\mathbb Z
\quad\Longrightarrow\quad n_1=\cdots=n_q=0,
\tag{9.1}
$$
则相同普通总度下没有不同矩的指数碰撞。
任意非零最高齐次部分至少有一个独立非零组，故条件 (1.3) 对所有非恒定 $F$ 自动成立。
因此该固定列表的全部非零普通多项式乘 $e^w$ 均循环。

两模式时 (9.1) 只要求 $\rho_1\ne\rho_2$；
这给同一方法下的全部复双对数模式。
对于三个或更多模式，合并矩定理比 (9.1) 更宽：
(8.1) 的指数有许多精确有理关系，却仍满足目标多项式的非零最高组条件。

条件可以失败。例如正实指数 $(1,2,3,4,5)$ 和
$$
F(x)=x_1x_5-4x_2x_4+3x_3^2
$$
满足
$$
F_D(\rho_\nu t^{\rho_\nu})
=(5-32+27)t^6=0.
$$
本稿的最高矩常数方向在此确实消失，不能把一个零的合并系数当作单位。
这只表明本判据不适用，不说明该向量不循环或原算子存在非零核；其他实际方向逆必须另证。

本稿没有处理无限个模式、任意原系数行或任意正常见证源，
也没有由这些循环多项式的稠密性宣称全部 $L^2$ 向量循环。
普通复 Hilbert 不变子空间问题仍未完成。

## 10. 完整依赖

- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §§2—6、10：原复行正分量共同正则器、真实自然词和最大图、全 $C$ 自伴及普通 Bell。
- [变化正预解幂引理](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)：随 $r$ 的强单位、线性深度、联合反射导数及两侧四次预算；本稿 §6 完整列出有限正分量扩展的域范围。
- [临界双模式全多项式稿](R150-appendix-critical-logarithmic-two-mode-full-polynomials-and-zero-parameters.md)：全部实际池阶乘、反射顺序、强单位核输入和原 $C$ 配对。
- [R236 普通矩逆](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md) 与 [多辅助矩阵](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)：有限生成逆与常数方向矩阵块。
- [有限 jet 主稿](R150-appendix-finite-logarithmic-jets-vandermonde-tail-cancellation-and-polynomial-cyclicity.md) §11：原复 $\kappa_\rho$ 及复杂指数旧严格范围；本稿不重新定义这些常数。

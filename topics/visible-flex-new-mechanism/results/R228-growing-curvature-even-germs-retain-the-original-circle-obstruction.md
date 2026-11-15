# R228：增长曲率偶端口仍保留原八包的第四 ruling 障碍

日期：2026-11-15。**完整纸面推导；未执行新的符号研究、profile 积分或几何试验。**

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的真实分子恢复、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 的点态八矩及 chain 项、[R193](R193-full-width-positive-obstruction-for-frozen-eight-derivative-packets.md) 的原八包正系数、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md) 的任意 gauge 配对及 [R224](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md) 的同锚历史消去。

本稿检验一个确实改变三矩空间的共同偶端口。其三矩空间准确包含 $\sigma^2$，不能直接套 R216 的平点门或 R224 的常 $k,\omega$ 计算。结果是：只要曲率中一个明确的指数系数非零，完整最高项仍回到同一个 $\mathsf T$ 四次泛函。在下述 $b=0$ 子类，R193 的 $c_6>0$ 再给严格障碍。消掉该指数系数的例外留作不同的未决问题。

## 1. 相容偶端口及参数分叉

令 $\sigma=s-s_*$、$t=\sigma^2$，固定 $h_e>0,\varepsilon>0$ 和 $k_e,\omega_e,a\in\mathbb R$，置
$$
b=\omega_e-\frac{k_e}{h_e},\quad
C=k_e-\frac{a}{2\varepsilon},\quad c=\frac C{h_e^2}.
\tag{1}
$$
考虑准确解析端口
$$
h=h_e e^{\varepsilon t},\quad
k=\frac a{2\varepsilon}-at+C e^{2\varepsilon t},\quad
\omega=b+\frac a{2\varepsilon h_e}e^{-\varepsilon t}
+\frac C{h_e}e^{\varepsilon t}.
\tag{2}
$$
直接求导给
$$
\boxed{\omega_s=\frac{k_s}{2h},\qquad d=h\omega-k=bh+at.}
\tag{3}
$$
没有把 $\omega$ 当成独立自由函数。三者均偶，中心速度零。本文假设实际几何在某个双侧开邻域具有该端口，并在该邻域及固定共同 profile 区间 $I$ 上满足物理条件 $z=\xi+\omega\ne0$。全局低阶词、frame 与闭合的实现须另付。

主要分支是
$$\boxed{C\ne0.}\tag{4}$$
此时 $k=ch^2+O(1+t)$。若 $C=0,a\ne0$，则
$$
a=2\varepsilon k_e,\quad k_e\ne0,\qquad
k=k_e(1-2\varepsilon t),\quad
\omega=b+\frac{k_e}{h_e}e^{-\varepsilon t}.
\tag{5}
$$
下文不把 (5) 一并排除。

## 2. 完整偶部商及新的三矩空间

固定同一个合法三矩第一圆
$$
\phi_\theta=\cos\theta f+\sin\theta g,\quad
D_\theta=f^2-\phi_\theta^2,\quad \mathbf m(D_\theta)=0,
\tag{6}
$$
保原共同零 collar 与唯一右积分 $Jv(\xi)=\int_\xi^r v(\eta)d\eta$，假设 canonical 二、三阶已过其全部 range 条件。R221 的三矩系数为
$$
\mathbf w=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{7}
$$
当 $a\ne0$，$d=bh+at$ 准确给
$$
\boxed{\mathcal W_e=\operatorname{span}
\left\{h,t,\frac{1+a^2t^2}{h}\right\}.}
\tag{8}
$$
例如 $\mathbf w_1-2b\mathbf w_2=at/2$。$a=0$ 时降为 $\operatorname{span}\{h,h^{-1}\}$。两种情形均有 $W=O(hP(\sigma))$，其中 $P$ 是有限多项式界。

R224 偶部商证明实际只需 $h,k,\omega$ 为偶且满足原相容式。在本端口，$h,d,k,z$ 偶，$\gamma=h_s,d_s,e_s$ 奇。R73 六项式每个速度项均含两个奇因子，所以整个 $M_{\rm raw}$ 偶；R221 局部三线性 ruling 项只含一个 $\gamma$ 或 $e_s$，所以为奇。因此对任意固定同 collar 的 $w$，
$$\operatorname{Ev}\mathcal B_\theta(w)\in\mathcal W_e.\tag{9}$$
平方项及第三齐次改动也在 $\mathcal W_e$。该式先于第三合法性行，故覆盖全部允许 gauge。

真实累计八矩写为 $\mathsf m=\mathsf m_*+\mathsf o$，其中 $\mathsf o$ 奇且 $\mathsf o(0)=0$。由 (6)，$w^*=\Phi_{\mathsf m_*}D$ 的全部左尾准确零。同锚中心模型满足
$$
Z=\widehat Z-Y_{w^*},\qquad
U=\widehat U+2\widehat Z_B(\phi,w^*)+Y_{\chi^*}.
\tag{10}
$$
$\chi^*$ 保真实第三初值，不必宣称为合法全局 gauge。R221 单紧槽配对支付其端项，R224 完整代入给
$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e}.
\tag{11}
$$
中心模型的 parity 包含 $\Omega(k)$；$k$ 偶使中心第四 ruling 自身为偶。因此可解的必要条件是
$$
\boxed{\widehat{\mathscr K}_\theta\in\mathcal W_e
\text{ 于整个 germ、对全部相位成立。}}
\tag{12}
$$

## 3. 准确最高二阶算子

令 $q=\xi+b$，定义固定平移算子
$$
\mathsf T_b(u,v)
=q^2u'v'+qJ\big((\eta+b)^2u''v''+2u'v'\big).
\tag{13}
$$
下文 $O(h^jP)$ 是在固定紧 $I$ 的每个所需有限 $C^m_\xi$ 范数的界；多项式、常数可随 $m$ 与固定参数改变。固定 $\varepsilon>0$ 时任何多项式除以 $h$ 都趋零，不需 $\varepsilon\downarrow0$ 一致。

从 (2)–(3)，
$$
k=ch^2+O(P),\quad e=hq+at,\quad z=(e+k)/h,\quad
K_0=(e+k)(ke-1)/h^2.
\tag{14}
$$
R73 原六项式
$$
r_s(u,v)=A_0uv+\tfrac12A_1(uv'+u'v)+A_2u'v'
+B_0J_0+B_1J_1+B_2J_2^*
\tag{15}
$$
的系数准确满足
$$
A_0,A_1=O(h^3P),\quad A_2=\frac{c^2h^4q^2}{8}+O(h^3P),
\tag{16}
$$
$$
B_0=\frac{c^2h^4qb^2}{8}+O(h^3P),\quad
B_1=\frac{c^2h^4qb}{4}+O(h^3P),\quad
B_2=\frac{c^2h^4q}{8}+O(h^3P).
\tag{17}
$$
核对只需 $K_{0,\xi}=(2ke+k^2-1)/h$ 的最高项 $c^2h^3$，以及 $K_0$ 的最高项 $c^2h^3q$。所有速度项低于 $h^4$ 层，仍留在原余项。故
$$
\boxed{r_s=\beta\mathsf T_b+\mathsf R_s,\quad
\beta=c^2h^4/8,\quad \mathsf R_s=O(h^3P).}
\tag{18}
$$
令 $B(\sigma)=\int_0^\sigma\beta$，基本导数比较给
$$
\boxed{B(\sigma)\sim c^2h(\sigma)^4/(64\varepsilon\sigma).}
\tag{19}
$$
对任意固定多项式，$\int_0^\sigma h^jP=O(h^j\widetilde P)$，$j>0$。所以真实中心第二 history
$$
\mathsf o=B\mathsf T_b+O(h^3P)=B\mathsf T_b+o(B).
\tag{20}
$$
全部 $J_0,J_1,J_2^*$ 保同一右锚，没有分包重置。

## 4. 完整第三动态及局部恢复

使用 R56 的分子，不用含 $z^{-1}$ 的物理分量。第一场分子
$$
V_Y=(-\phi'/2,0,h\phi-e\phi'/2)=(O(1),0,O(hP)).
\tag{21}
$$
静态二阶输入的 $P_{uv}=J_e/(8h)+eu'v'/8$ 与 R56 的 $\mathcal B_{uv}=J/(2h)$ 均为 $O(hP)$。R221 准确 $\eta$ 式只含 $h,d$ 及一阶导数，给 $\eta=O(hP)$，所以局部分子
$$
V_K=(\eta/h,zP+\mathcal B,e\eta/h)
=(O(P),O(h^2P),O(hP)).
\tag{22}
$$
真实协变导数给充分界
$$
\nabla_sV_Y=(0,O(h^2P),O(hP)),\quad
\nabla_sV_K=(O(h^4P),O(h^2P),O(h^2P)).
\tag{23}
$$
因此 $\ell_s=R[H(Y,K)]$ 的 R56(5) 各项中，
$T_s/(2h^2)=O(h^2P)$、$K_0P=O(h^4P)$，其余均不超过 $O(h^4P)$。这里使用准确关系
$$
kz-(k^2+1)/h=(ke-1)/h,\qquad \lambda=e_s/h^2.
\tag{24}
$$
得到 $\ell_s=O(h^4P)$。

变化 profile 的 chain 项也保留。其首系数准确消去看似很大的部分：
$$
\nu-\gamma k/h^2=-(d/h)_s=-(at/h)_s=O(P/h).
\tag{25}
$$
R73 的其余两个系数与相应右积分组合后为 $O(P)$，故整个固定 profile 算子 $\Psi_s=O(P)$。

令 $O_D=\mathsf o(D)$。完整第三 history 满足
$$
(\widehat W_3)_s=-2\ell_s(\phi;D)
+2r_s(\phi,O_D)+2\Psi_s(\phi,(O_D)_s).
\tag{26}
$$
唯一 $B\beta$ 主项为
$$
2B\beta\,\mathsf T_b(\phi,\mathsf T_bD)
=(B^2)_s\mathsf T_b(\phi,\mathsf T_bD).
\tag{27}
$$
其余乘积至多 $O(h^7P)$；局部及 chain 项至多 $O(h^4P)$。从中心零初值积分，得
$$
\boxed{\widehat W_3
=B^2\mathsf T_b(\phi,\mathsf T_bD)+O(h^7P)
=B^2\mathsf T_b(\phi,\mathsf T_bD)+o(B^2).}
\tag{28}
$$

第三局部恢复不能省。完整第二分子为
$$V_Z=(O(BP),O(h^2P),O(hBP)).\tag{29}$$
R56 三阶 $P,\mathcal B=O(hBP)$，而 $T_{s\xi}=O(h^2BP)$。这里 $\nabla_sV_Z$ 的 N 分量确可达 $O(h^2BP)$；第一场 N 分量及其 $\xi$ 导数为零，才使该项不额外进入所需的 $T_{s\xi}$ 配对。其余分量直接用 (21)、(23)、(29) 得该界。R56(6) 给
$$\eta_3=O(hBP).\tag{30}$$
第三局部场与第一场的 ruling 配对为 $O(hBP)$，相对于 $hB^2$ 趋零。它的 N 分量无需为零，只与第一场相应导数正交。

## 5. 完整 ruling 极限

定义
$$
E_b(u,v)=\frac14\int_I
\big((\xi+b)^2u''v''+2u'v'\big)\,d\xi.
\tag{31}
$$
由 (7)，原配对准确满足 $\mathcal E_s(u,v)/h\to E_b(u,v)$。其余系数来自 $d=bh+at$，至多为多项式乘 $h^0,h^{-1}$。一槽有真实尾、另一槽紧支撑时仍按 R221 真端项身份处理。

二阶局部平方为 $O(h^3P)$，它与 $Y_{O_D}$ 的交叉项为 $O(hBP)$；除以 $hB^2$ 都趋零。结合 (28)、(30)，从完整 forcing $-H(Z,Z)-2H(Y_\phi,U)$ 得
$$
\boxed{
\frac{\widehat{\mathscr K}_\theta}{hB^2}
\longrightarrow\mathscr C_{b,\theta}
=-E_b(\mathsf T_bD,\mathsf T_bD)
+2E_b(\phi,\mathsf T_b(\phi,\mathsf T_bD)).
}
\tag{32}
$$
同时对任意固定 $W\in\mathcal W_e$，
$$W/(hB^2)\longrightarrow0.\tag{33}$$
若 (12) 在真 germ 上成立，解析身份遂迫 $\mathscr C_{b,\theta}=0$ 对所有相位成立。

此处延拓完全针对消去 $z$ 分母后的有限分子/ruling 公式：R56(5)–(7)、R73、R221 只剩正的 $h$ 的负幂与整解析系数，故在整个实 $\sigma$ 轴可延拓。实际 $z$ 远处可能变号；这不授权延长物理路径，也不妨碍解析函数身份检验。没有通过物理奇点来构造实际曲面。

## 6. 原八包在 b=0、C非零时严格失败

设 $Q=f+ig$，普通复双线性延拓。相位代数给
$$
(\mathscr C_b)_4=-\frac18\left[
E_b(\mathsf T_b(Q,Q),\mathsf T_b(Q,Q))
+2E_b(Q,\mathsf T_b(Q,\mathsf T_b(Q,Q)))
\right].
\tag{34}
$$
这是 $\operatorname{Re}(e^{-4i\theta}(\mathscr C_b)_4)$ 的复幅，不是单个复 Fourier 系数。

当 $b=0,C\ne0$ 时，(34) 正是 R224 已与 R193 严格对齐的 $\mathsf T,E_\infty$ 泛函。对原八包宽度 $\lambda>0$ 及已付同三矩光滑邻域，
$$
\boxed{\operatorname{Re}(\mathscr C_0)_4=-8c_6/\lambda<0.}
\tag{35}
$$
与 (32)–(33) 的必要零值矛盾。

**定理。** 对 R193 原八包或已付光滑邻域，包含 (2) 双侧 germ、满足 $b=0,C\ne0$ 的任何实际几何，都不能通过完整第四 ruling。覆盖全部合法二阶与第三齐次 gauge、任意真实传入历史，以及每个能放入共同物理区间的正宽度。

特别地，若仍保原中心 $k_e=\omega_e=0$，则 $b=0,C=-a/(2\varepsilon)$。所有 $a\ne0$ 的新端口仍被排除，尽管 $\sigma^2$ 已准确进入三矩空间。$a=0$ 则回到 R224 已排的原标准端口。

## 7. 未决范围

1. 例外 (5) 的 $h^4\mathsf T_b$ 层准确消失，须另付下一完整算子及全部局部/chain 动态，不能再使用 (35)。
2. $b\ne0$ 时 (34) 是准确必要门，但本稿不移植 R193 的 $c_6$ 符号，须对实际平移算子与圆核实。
3. 改变圆会改变 (34)；R199 任意 faithful 修改不自动继承符号。只有另外证明保持该严格符号的固定支撑高阶邻域才继承排除。
4. 即使新局部偶门通过，完整 period、odd ruling、同一个 gauge 的 R221 联合像、高阶收敛以及嵌入/reach/幅度仍须各自证据。

本稿消去一个确有新增三矩自由度、却仍受原四次泛函限制的端口子族；不宣称一般等距机制不存在，不重算已完成的 R193 积分。


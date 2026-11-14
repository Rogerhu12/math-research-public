# R150 附录：真实偏导的有界逆、实二次对数共振及全部普通点态幂

日期：2026-11-13（UTC）。normal_resume_1cf / Astra-ISP-1cf8c51d；根提出最高实指数的唯一矩方向与全复合延伸，逐项独立核验。
状态：已证明；Astra-ISP-1cf8c51d 与 kernel_resume_1cf 独立复核全部原域、矩系数及真实偏导逆。
本稿使用原规范最大图、完整 ordinary Bell 和原 $C$ 配对。
其全点态幂结论不是从一次循环性继承，也不把普通点态幂换成某个自然算子幂。

## 1. 设置与主结论

取两两不同正实数
$$
0<\rho_1<\cdots<\rho_q,
$$
以及同一原对数模式
$$
a_{\nu p}=\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2},
\qquad
u_\nu=-\kappa_{\rho_\nu}+\sum_pa_{\nu p}\chi_p.
\tag{1.1}
$$
$\kappa_{\rho_\nu}$ 保留原前缀积分比较所确定的常数。
指数权为任意固定复 $\ell^2$ 行
$$
w=w_*+\sum_pw_p\chi_p.
$$

令
$$
F(x)=x^{\mathsf T}Bx+\ell^{\mathsf T}x+c,
\qquad B=B^{\mathsf T}\in M_q(\mathbb R),\quad B\ne0,
\quad \ell\in\mathbb C^q,\quad c\in\mathbb C.
\tag{1.2}
$$
只要求二次系数为实；仿射部分和指数权可以是复数。

**定理。** 对任意非零一变量多项式 $Q$，
$$
\boxed{
Q(F(u_1,\ldots,u_q))e^w\ne0,\qquad
[Q(F(u_1,\ldots,u_q))e^w]_A=H.
}
\tag{1.3}
$$
特别包括全部
$$
[F(u)-\lambda]^h e^w,\qquad
\lambda\in\mathbb C,\quad h\ge1.
\tag{1.4}
$$
对非恒定仿射 $F$，结论已由合并矩定理的最高组条件给出；非零常数目标仍单独处理。
本稿不包含恒等为零的目标多项式。

## 2. 实际偏导有全域有界逆时的矩阵块接口

先记录一个准确扩展。
设 $P(W;\mathbf G)$ 是实际完整多模式 Bell 多项式，最大闭实现为 $\mathsf T$；
原有限矩池及共同正则器已经如前稿支付。
假设某个显示模式的偏导在共同深域上等于一个真实闭算子 $\mathsf D$，并且
$$
\boxed{
\mathsf D:\operatorname{Dom}\mathsf D\longrightarrow H
\text{ 双射},\qquad
L=\mathsf D^{-1}\in A'\cap B(H).
}
\tag{2.1}
$$
这里 $\mathsf D$ 可以无界；不把它称作 $B(H)$ 中的有界单位。

对一个跨池块，记实际行矩阵 $\Xi$，取
$$
b=\tfrac14\Xi^{-1}e_*.
$$
仍有一次差分系数
$$
L_p=4\sum_\gamma \xi_{\gamma p}\partial_{W_\gamma}P.
$$
把原常数单位块输入改为
$$
\boxed{
Q_B=L\sum_i b_i\prod_{j\ne i}t_{p_j}N_{p_j}.
}
\tag{2.2}
$$
它是有界交换子。
在已付共同深域上，$\sum_i b_iL_{p_i}=\mathsf D$，故平方零顶部准确取消为
$$
\left(\sum_i t_{p_i}N_{p_i}L_{p_i}\right)Q_B
=\prod_i t_{p_i}N_{p_i}
\quad\text{模重复位}.
\tag{2.3}
$$
每个 $A'$ 元保持原 first 及全部正分量自然词域；
因此 $L$ 的出现不损失已有深度。
$L$ 也保持 $\ker\mathsf T$，来自 R186 的有界核方程。

形成 $r$ 个块时，实际绝对输入预算只另乘
$$
\|L\|^r.
\tag{2.4}
$$
这是固定几何费用，低于原四次成本。
全部输入先在核内形成，$J_E$ 始终在最左侧；
从不把 $L$ 穿过反射，也不把 $L^*$ 施于未知核。
其联合 first 导数为零，因为 $L\in A'$ 与全部 first 完整域交换；
真实反射误差仍按原顺序作用于这个有界右输入。

因此，原全部阶乘、carry、变化正预解深度以及
$$
\mathsf T^r\mathcal V_N\mathcal R_rf\rightharpoonup c f,
\quad c\ne0,
$$
和两侧 $A$ 四次配对逐项保持成立。
这个接口要求 (2.1) 的真实全域逆和完整域一致性，不接受一个形式分式或仅有稠密像的代替物。

## 3. 实对数线性 first 的全平面实际逆

设
$$
v=d_0+\sum_{\nu=1}^q d_\nu u_\nu,
\qquad d_\nu\in\mathbb R,
$$
且不全为零，允许 $d_0\in\mathbb C$。
其原行是
$$
c_p=\sum_\nu d_\nu a_{\nu p}
=\frac1{p+2}\sum_\nu d_\nu\rho_\nu(\log(p+2))^{\rho_\nu-1}.
\tag{3.1}
$$
取最大满足 $d_\nu\ne0$ 的指数 $\rho_{\nu_*}$。
由于所有指数为不同实数，该项在实轴尾部严格支配其他项。
故 $c_p$ 从某个有限位起具有固定符号 $\sigma\in\{1,-1\}$，并且
$$
|c_p|\sim |d_{\nu_*}|\rho_{\nu_*}
\frac{(\log(p+2))^{\rho_{\nu_*}-1}}{p+2}.
$$
所以正尾 $c_p^+=\sigma c_p\mathbf1_{p\ge p_0}$ 属于
$\ell^2\setminus\ell^1$。

令 $X_+=X_{\sum c_p^+\chi_p}$。
R128/R134 给 $X_+$ 最大增生、空谱，且其全平面预解在 $A'$ 中。
原线性 first 的实际复倾斜满足
$$
D=X_{v,w}=\sigma X_++H,\qquad H\in A'\cap B(H),
\tag{3.2}
$$
同域闭实现准确成立。
$H$ 包括有限低头、原固定常数和
$\sum_pc_p(R_p(w)-V_p)$；后者由 $\ell^2\times\ell^2$ 按范数绝对收敛。

下面明确支付有界交换扰动的逆，不只声称“有界扰动保持空谱”。
令
$$
L_0=(\sigma X_+)^{-1}\in A'.
$$
它是拟幂零有界算子。
确实，空谱给对每个 $\mu\ne0$，$I-\mu^{-1}L_0$ 有实际有界逆，故
$\sigma(L_0)\subset\{0\}$。
又 $H$ 与 $L_0$ 交换，所以
$$
r(HL_0)\le\|H\|r(L_0)=0.
$$
因此 $I+HL_0$ 是真实有界单位，其 Neumann 级数在范数中收敛，逆仍在 $A'$。
在原 first 域上逐项核验得
$$
\boxed{
D^{-1}=L_0(I+HL_0)^{-1}\in A'.
}
\tag{3.3}
$$
该逆的像在 $\operatorname{Dom}X_+$，左右逆等式均实际成立。
把任意复标量位移并入 $H$ 后，同一证明给 $\sigma(D)=\varnothing$。
所以 $L=D^{-1}$ 本身也拟幂零。

若 $v$ 的行全为零而 $v=d_0\ne0$，则另作常数情形：$D=d_0I$，逆为 $d_0^{-1}I$。
不在这个常数情形声称其逆拟幂零。

## 4. 一个空谱 first 的完整普通点态幂都有有界逆

保持上一节非零实线性行，$D=X_{v,w}$，$L=D^{-1}$。
对固定整数 $h\ge1$，原目标是 $v^h e^w$。
R186 §10 的完整 ordinary Bell 在同一个闭 first 上给
$$
\mathsf B_h=
D^h+\sum_{j=0}^{h-1}C_jD^j,
\qquad C_j\in A'\cap B(H),
\tag{4.1}
$$
其中各 $C_j$ 是该原行及同一 $w$ 的真实 Bell 系数。
这里不把 $\mathsf B_h$ 换成 $D^h$；
$h\ge2$ 时这些系数通常不为零。

在 $\operatorname{Dom}D^h=\operatorname{Ran}L^h$ 上，
$$
\mathsf B_h=
\left(I+\sum_{j<h}C_jL^{h-j}\right)D^h.
\tag{4.2}
$$
所有 $C_j$ 与 $L$ 交换。
每个 $C_jL^{h-j}$ 拟幂零，有限个彼此交换的拟幂零元之和仍拟幂零；
可直接由多项式展开和谱半径公式证明。
故括号为 $A'$ 中的真实有界单位，得到
$$
\boxed{
\mathsf B_h^{-1}
=L^h\left(I+\sum_{j<h}C_jL^{h-j}\right)^{-1}
\in A'\cap B(H).
}
\tag{4.3}
$$

域也由此完整确定：
$D^h$ 是有界单射 $L^h$ 的闭逆，故闭；
(4.2) 左乘有界单位后仍闭，定义域仍是 $\operatorname{Dom}D^h$。
R186 的单模式自然闭包与循环图核心把它识别为 $v^h e^w$ 的原规范实现。
若在较大多模式共同域上先得到同一目标，其 $e^w$ 多项式图核心给同一个最大闭图。

常数 $v=d_0\ne0$ 时，完整 Bell 恰为 $d_0^hI$，逆另行显然成立。
因此本节准确覆盖“非零实 first 加复常数”以及“非零复常数”两类，而不假设后者的逆拟幂零。

## 5. 单一最高实指数矩的偏导公式

本节给把外层 $Q$ 全部次数付清的关键等式。
对任意原多项式 $G$，其未合并的 ordinary-to-resonant 有限逆记作 $Q_G(Y)$。
由完整指数生成式直接求导，
$$
\boxed{
\partial_{Y_\omega}Q_G
=\frac{(-2)^{|\omega|-1}}{\omega!}\,
Q_{\partial^\omega G}.
}
\tag{5.1}
$$
证明只用
$$
\partial^\beta_t(t^\omega E(t))\big|_{0}
=\frac{\beta!}{(\beta-\omega)!}
\partial^{\beta-\omega}_tE(0)
\quad(\beta\ge\omega),
$$
及原有限多项式系数；$\beta\not\ge\omega$ 的项为零。
所以 (5.1) 包括完整多变量阶乘，没有省掉较低 Bell 系数。

从 $F$ 中删去实际不参与的变量，然后把剩余最大实指数仍记为 $\rho_q$。
若
$$
F(x)=x_q d(x_1,\ldots,x_{q-1})+e(x_1,\ldots,x_{q-1})
\tag{5.2}
$$
且 $d\ne0$，令外层 $Q$ 的次数为 $h\ge1$、最高系数为 $q_h$。
那么
$$
\partial_{x_q}^{h}Q(F)=h!q_h d^h.
\tag{5.3}
$$
在 $|\omega|=h$ 的所有矩中，$\omega=he_q$ 的键
$$
(h,h\rho_q-h)
$$
唯一。
因为任何另一个多重指标使用了严格更小的实指数，其加权和严格小于 $h\rho_q$。
不同总度的物理行也不被合并。
删去未使用的更大指数，正是保证这一论证对应实际原变量列表所需的步骤。

在合并矩构造中 $Y_{he_q}=\rho_q^hW_{h,h\rho_q-h}$。
所以 (5.1)—(5.3) 准确给
$$
\boxed{
\partial_{W_{h,h\rho_q-h}}\overline Q_{Q\circ F}
=\rho_q^h(-2)^{h-1}q_h\,\overline Q_{d^h}.
}
\tag{5.4}
$$
随后对合并列表施完整实际 Bell 修正：
系数保持固定，求导与该有限微分修正交换。
因此真实偏导的规范实现恰为
$$
\boxed{
\rho_q^h(-2)^{h-1}q_h\,
\bigl[d(u)^h e^w\text{ 的完整 ordinary Bell}\bigr].
}
\tag{5.5}
$$
其完整域相同可由 R186 的共同 $e^w$ 多项式图核心识别。
此处绝不是将右侧替换为 $(X_{d,w})^h$。

若 $d$ 是上一节允许的实线性 first 加复常数，或非零复常数，
(4.3) 使 (5.5) 有全域有界 $A'$ 逆。
于是它满足 §2 的实际矩阵提升接口。

## 6. 实二次定理的证明

记最高普通部分
$$
F_2(x)=x^{\mathsf T}Bx
$$
及合并矩的曲线符号
$$
H_F(t)=F_2(\rho_1t^{\rho_1},\ldots,\rho_qt^{\rho_q}).
$$

若 $H_F\not\equiv0$，
[合并复对数矩池定理](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)
已经给任意非零 $Q$ 的完整结论，无须本节再作处理。

以下考虑此前那个定理不能直接支付的
$$
H_F\equiv0.
\tag{6.1}
$$
先删去原 $F$ 中不参与的模式，再取剩余的最大 $\rho_q$。
在 $H_F$ 中，指数 $2\rho_q$ 的项只有
$B_{qq}\rho_q^2t^{2\rho_q}$；
因此 (6.1) 强迫
$$
B_{qq}=0.
$$
所以原 $F$ 对 $x_q$ 准确为一次：
$$
F=x_q d(x_{<q})+e(x_{<q}),\qquad
d=2\sum_{\nu<q}B_{q\nu}x_\nu+\ell_q.
\tag{6.2}
$$
由于 $F$ 实际依赖 $x_q$，$d$ 非零。
若该行 $B_{q\nu}$ 不全为零，$d(u)$ 是一条非零实线性原 log 行加复常数，
§§3—4 付其完整 ordinary 幂的全域有界逆。
若该行全为零，则 $\ell_q\ne0$，是同样已付的常数情形。

对每个固定外层 $Q$，取整个 $G=Q\circ F$，
重新建立其全部有限矩、合并键、完整 Bell 及规范最大图。
§5 的唯一矩偏导给一个具有全域有界 $A'$ 逆的真实方向。
全部不同合并矩的跨池下界仍由前稿 §5 给
$$
\log^+\Delta_N^{-1}=O(\log N).
$$
取 $r_N=\lfloor\sqrt N\rfloor$，输入中新增的固定方向逆只付
$\|\mathsf D^{-1}\|^{r_N}$。
所以全部输入仍有
$$
\log A_N=O(r_N\log N)=o(r_N^4).
$$
变化正预解先把原核输入送入 $O(D_G r_N)$ 层真实自然词域；
矩阵顶部和纯池非零弱极限、两侧 $A$ 四次界及原 $C$ 配对照 §2 全部成立。
于是整个 $G$ 的原规范核为零，原图核心给 $Q(F(u))e^w$ 非零且循环。

每个外层多项式均重新执行这套完整构造。
这证明 (1.3)，包括所有零参数和全部点态幂。

### 6.1 一次普通 Bell 的确消失，但全幂证明没有停在这一步

(6.1) 还给每个实际物理位的准确等式
$$
F_2(a_{1p},\ldots,a_{qp})=0,
$$
因为该值为
$H_F(\log(p+2))/[(p+2)^2(\log(p+2))^2]$。
原二次 ordinary Bell 校正因此严格为
$$
\sum_pF_2(a_{1p},\ldots,a_{qp})(I-R_p(w)^2)=0
$$
对任意复 $w$ 成立。
所以一次原目标的实现确为 $F(Z_w)$。
但这不使 $Q(F)$ 的全部高阶校正自动为零。
全幂结论使用的是 (5.1)—(5.5) 的真实偏导和完整单 first Bell 逆；
没有以 $[F(Z_w)]^h$ 代替普通 $F(u)^h$。

## 7. 最高矩完全抵消的五模式原零参数例

取原正实指数
$$
(\rho_1,\ldots,\rho_5)=(1,2,3,4,5)
$$
及
$$
F(x)=x_1x_5-4x_2x_4+3x_3^2.
\tag{7.1}
$$
原中心曲线满足 $F(\mathbf1)=0$，
最高普通矩曲线也准确满足
$$
H_F(t)=(5-32+27)t^6=0.
$$
所以前稿的最高矩常数方向在此确实失效，不能靠不合法拆开重复矩挽救。

最大变量 $x_5$ 的系数恰为 $d=x_1$。
原 $X_{u_1,w}$ 是正空谱 first 加有界交换扰动，§3 给其实际逆。
对任意外层 $Q$、$h=\deg Q$，
矩键 $(h,4h)$ 只有 $he_5$ 一个原指标，
相应真实偏导是
$$
5^h(-2)^{h-1}q_h
\bigl[u_1^h e^w\text{ 的完整 ordinary Bell}\bigr],
$$
由 §4 有全域有界 $A'$ 逆。

因此
$$
\boxed{
\left[
u_1u_5-4u_2u_4+3u_3^2-\lambda
\right]^h e^w
\text{ 对全部 }\lambda\in\mathbb C,\ h\ge1,\ w
\text{ 非零且循环}.
}
\tag{7.2}
$$
五个原中心常数、物理位及指数权全都保持原定义。

一次的五条原 first 池还可直接核验：
其矩阵为
$$
\left[\frac{\nu(\log(p_\ell+2))^{\nu-1}}{p_\ell+2}\right]_{\nu,\ell=1}^5,
$$
行列式是 $5!$、五个分母及 $\log(p_\ell+2)$ 的准确 Vandermonde 之积。
固定分离倍数 $N$ 池给 $\Delta_N\ge cN^{-5}$。
高次 $Q$ 则使用全部合并矩池，而不冒称一次五行预算已经覆盖任意次数。

## 8. 一个直接范围注及仍须保留的限制

同一唯一矩公式也给：
若原有限正实 log 列表中，$F$ 关于其实际参与的最大指数变量的次数至少为一，且关于该变量的最高系数为非零常数，
则取外层次数乘原该变量次数的纯矩偏导，得到非零标量方向；
全部非零 $Q(F)e^w$ 同样循环。
这是 (5.1) 和唯一矩键的直接常数特例，不要求最高普通曲线非零。

实二次证明的非恒定系数情形则实质使用：
最高实指数使 $F$ 对该变量一次；
其系数是一条尾部最终定号的真实 first；
该 first 的每个完整普通幂有实际有界逆。
一般复杂梯度行不必具有这个性质。
本稿没有把这些原正实指数模式替换成旋转的复指数后仍宣称所有实二次结论，也不把通常有界扰动当作任意无界图的谱保持原则。

未知原不变空间的 $C$ 不变性、first 有界性及一般源上界仍未假定。
任意无限模式、任意原行、一般多项式及普通 Hilbert ISP 不由此完成。

## 9. 依赖

- [合并矩池与全部高阶共振](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)：准确原中心、完整生成式合并、所有不同矩的实际池和原 $C$ 配对。
- [变化正预解幂与核内 jets](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)：变化强单位及线性深度预算。
- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §§2—6、10：全部自然域、最大图及完整普通 Bell。
- [R134 空谱 first](R134-empty-spectrum-first-chaos-polynomial-cyclicity.md) 与 [实际计数半群](R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)：真实正尾的全平面逆。
- [R236 普通矩逆](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)：有限生成式与准确多重指标阶乘。

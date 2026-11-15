# R776 — 原 S174 的三处绝对 Weil 谱、完整半特征与精确 δ² 导子

日期：2026-11-15。**状态：已证明。**

本篇支付 R772 的原 degree174 来源在三处的全部三个方向及其绝对相位。所用的是原加性角色、原 Hermitian 参数 α=87 和 Yang 的实际 Hecke splitting。结论不是把一个抽象三维有限 Weil 模接到原来源，也不把全 S174 误作全偶空间。

三个原三处方向的环面特征，在生成元 (ω,−1) 上准确为
$$
(1,+1),\qquad(\omega,+1),\qquad(\omega,-1).
\tag{1}
$$
没有遗漏的共同 metaplectic 标量。两个新增方向对应的真实 Hecke 角色在三处有精确导子 δ²，而不是 δ³。它们在 uniformizer δ 上的值不同，必须保留。

本篇没有单独从 (1) 推出原全部负一矩的点公式；二处、二十九处、全局单位相容及原完整 theta–Katz 平方仍须与这张三处表一起使用。R774 的一般点公式已付，不能代替这个来源识别步骤。

## 1. 原参数、加性角色和整局部模型

固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\qquad\delta^2=-3,\qquad\operatorname{Im}\delta>0.
$$
R772 的真实整行是 P0=δP，范数174。其标准线丛准确为
$$
\mathcal L=\mathcal O_{E_0}(174[0]),\qquad
E_0:y^2=x^3+1.
\tag{2}
$$
原 b=17 到 E0 的代数微分缩放与全部实际有限 p 门按 R772 保持。

沿 R290 的 Yang 极化 X=Qδ，degree 2α 的模型在此取
$$
\alpha=87,\qquad
\psi_3(x)=e^{-2\pi i\{x\}_3},\qquad
\psi'_3(z)=\psi_3\!\left(\operatorname{Tr}_{K_3/\mathbf Q_3}
                               \frac{87\delta z}{4}\right).
\tag{3}
$$
三处 different 是 (δ)。因此 ψ3∘Tr 的 conductor 指数为 −1；
87δ 的 δ-adic 赋值为3，故
$$
n(\psi'_3)=-4=2(-2),\qquad
L=\delta^{-2}\mathcal O_{K_3}.
\tag{4}
$$
这里 conductor 指数是使 ψ′ 在 δ^n O 上平凡的最小整数。

原 lattice model 是
$$
\mathscr S(L)=
\{f:\ f(z+l)=\psi'_3(z\bar l)f(z),\ l\in L;\quad f
       \text{ 局部常值且支撑紧}\}.
\tag{5}
$$
对 w∈K3，取原刚性化的余类向量
$$
f_w(z)=
\begin{cases}
\psi'_3(w\bar z),&z\in w+L,\\
0,&z\notin w+L.
\end{cases}
\tag{6}
$$
特别 f_w(w)=1，因为 ψ′ 在 Q3 上平凡。相位在这里已固定，不能再任意改变一个余类的符号。

令
$$
v=\delta^{-3}=\delta/9,\qquad
\mathscr V_3=\mathbf C f_0\oplus\mathbf C f_v\oplus\mathbf C f_{-v}.
\tag{7}
$$
这正是支撑在 δ^-3 O 上的全部三维子空间：δ^-3 O/L 有且仅有0、v、−v三个余类。

## 2. 真实 splitting：为何 −1 没有额外共同负号

记 G=K3^1。为区分两个常被混用的规范，先固定三处 Hecke 角色
$$
\chi_3^0(u)=u\bmod\delta\in\{\pm1\}\quad
(u\in\mathcal O_{K_3}^{\times}),\qquad
\chi_3^0(\delta)=-i.
\tag{8}
$$
它限制到 Q3× 等于 ε_{K3/Q3}。例如
3=−δ²，故 χ3^0(3)=(-1)(-i)^2=1，正是 ε(3)。

在原 ψK/2 规范下，R290 的三处二次 Gauss 计算给
$$
\epsilon(1/2,\chi_3^0,\psi_{K,3}/2)=-i,\qquad
\epsilon(1/2,\chi_3^0,\psi_{K,3}/2)\chi_3^0(\delta)=-1.
\tag{9}
$$
另一方面 3=N(δ)，而29≡−1 mod3不是局部范数单位，所以
$$
\epsilon_{K_3/\mathbf Q_3}(87)
 =\epsilon(3)\epsilon(29)=-1.
\tag{10}
$$
Yang 1999 Proposition1.2(1)、式(1.9)因此给：从 (5) 到原
Schrödinger Hecke 模型的 splitting 比 ξ **严格为平凡角色**。

Yang 1998 Theorem0.1(1) 对偶 conductor (4) 的结论于是直接适用：
$$
\boxed{
\omega_{87,\chi_3^0}(g)f(z)=f(zg),\qquad g\in G,
}
\tag{11}
$$
其中已通过实际 lattice–Schrödinger intertwiner 认同两模型。
这不是只核一个范数一有限商。尤其 g=−1 在原 Hecke splitting
中就是反射；没有可以事后添加的共同 −1 或 i。

若改用未注明 splitting 的有限 Sp(2,F3) 表，其中心值可能带
quadratic 标量；那张表不能直接替换 (11)。

## 3. 三维矩阵与绝对 ω 相位

对 g=ω，三个余类都被固定，因为 ω−1 的 δ-adic 赋值为1。
在 fv 的中心 z=v 直接读取：
$$
\begin{aligned}
(\omega_{87,\chi_3^0}(\omega)f_v)(v)
 &=f_v(v\omega)
 =\psi'_3(v\overline{v\omega})\\
 &=\psi_3\!\left(
       \operatorname{Tr}\frac{87\delta\bar\omega}{108}\right)
 =\psi_3(29/12)=\omega .
\end{aligned}
\tag{12}
$$
这里 N(v)=1/27，Tr(δ barω)=3，且29/12−2/3=7/4∈Z3。
使用原负有限加性角色后，e^{-4πi/3}=ω；相反的加性角色会给共轭值，
不能在本篇改用它。

fv 与 f−v 的相位相同，因为两者范数相同。f0 在整个 G 下固定。
对 −1，
$$
f_v(-z)=f_{-v}(z),\qquad f_{-v}(-z)=f_v(z),\qquad f_0(-z)=f_0(z),
\tag{13}
$$
中心值均为1。因此在按 (f0,fv,f−v) 排列的基上，
$$
\boxed{
W_3(\omega)=
 \begin{pmatrix}1&0&0\\0&\omega&0\\0&0&\omega\end{pmatrix},
\qquad
W_3(-1)=
 \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
}
\tag{14}
$$

写
$$
G_j=\{g\in G:g\equiv1\bmod\delta^j\}.
$$
范数一条件给 G2=G3；G/G2 的完整阶数为6，并由 ω、−1 生成。
G2 在 (7) 上平凡。可直接验证：g−1∈δ³O，
所以它不移动三个余类，而余类相位的参数
N(v)(bar g−1) 的赋值至少 −3，大于 ψ′ 的 conductor 指数 −4。
于是 (14) 核定了整个 G 的作用，而非只两次样本检查。

三个一维本征空间为
$$
F_0=f_0,\qquad F_{\mathrm e}=f_v+f_{-v},\qquad
F_{\mathrm o}=f_v-f_{-v}.
\tag{15}
$$
它们的特征 τ0、τe、τo 完整由
$$
\begin{array}{c|ccc}
 &\tau_0&\tau_{\mathrm e}&\tau_{\mathrm o}\\ \hline
\omega&1&\omega&\omega\\
-1&1&1&-1\\
G_2&1&1&1
\end{array}
\tag{16}
$$
给出。维数相加为3，故没有第四个遗留 sector。

## 4. 原 Schrödinger 函数与有限范数

采用 Yang 1999 式(1.6)、Appendix(A11) 的实际 intertwiner，
并用 ρ(f0)(0)=1 固定其唯一共同尺度。对
w=R(w)+I(w)δ，其公式为
$$
\rho(f_w)(x)=
 \psi_3\!\left(\frac{\Delta\alpha}{2}R(w)I(w)\right)
 \psi_3(-\Delta\alpha R(w)x)\,
 \mathbf1_{I(w)+\Delta^{-1}\mathbf Z_3}(x).
\tag{17}
$$
这里 Δ=−3，n=−2，所以 floor(n/2)=−1。由于 v=δ/9 的实部为0，
本篇没有一个隐藏的 modulation 或根单位：
$$
\boxed{
\begin{aligned}
\phi_0&=\mathbf1_{\frac13\mathbf Z_3},\\
\phi_{\mathrm e}
 &=\mathbf1_{\frac19+\frac13\mathbf Z_3}
   +\mathbf1_{-\frac19+\frac13\mathbf Z_3},\\
\phi_{\mathrm o}
 &=\mathbf1_{\frac19+\frac13\mathbf Z_3}
   -\mathbf1_{-\frac19+\frac13\mathbf Z_3}.
\end{aligned}}
\tag{18}
$$
相对于 vol(Z3)=1 的原自对偶加法测度，
$$
\boxed{\|\phi_0\|^2=3,\qquad
       \|\phi_{\mathrm e}\|^2=\|\phi_{\mathrm o}\|^2=6.}
\tag{19}
$$
它们两两正交。新增方向的范数不能沿用旧球的3，也不能统一约成1；
后续 Yang 全权平方必须逐条保留 (19)。

## 5. 这些确是原全部 S174 的三因子

这里把局部模型与原 degree174 的完整 theta 池接齐，避免只得到
一个与原来源无关的三维表示。

二处取原四陪集
$$
e_j=\mathbf1_{j/2+2\mathbf Z_2},\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,
$$
其完整原半特征子空间为 span(fA,fB)，系数写成
$$
v_2=(a,b,-a,b).
$$
本节只用该空间与半特征，不预先指定它的二处 torus 本征基。
二十九处取全部29个原陪集
$$
e_c^{(29)}=\mathbf1_{c/29+\mathbf Z_{29}},\qquad c\in\mathbf F_{29}.
$$
三处取 (7)、(18) 的全部三维空间。其他有限处取原球。

全部有理支撑准确为 x=n/522。三个有限坐标依次为
$$
2x\bmod4\mathbf Z_2\longleftrightarrow n\bmod4,\qquad
9x\bmod3\mathbf Z_3\longleftrightarrow n\bmod3,\qquad
29x\bmod29\mathbf Z_{29}\longleftrightarrow21n\bmod29.
\tag{20}
$$
这些使用261≡1 mod4、58≡1 mod3和18^-1≡21 mod29。
所以任一纯张量的实际系数为
$$
a_n=v_2(n\bmod4)\,v_3(n\bmod3)\,v_{29}(21n\bmod29).
\tag{21}
$$
一般向量为这些纯张量的有限和。全系数空间维数是
2·3·29=174。

令 s0=(1−ω)^-1=(1+δ/3)/2。原 Hermite Gaussian 的尺度为
|δ³α|=261√3，故 theta 写成
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\!\left(\pi i\frac{\delta}{3}\frac{n^2}{348}
                 +2\pi inZ\right).
\tag{22}
$$
由 (21)，
$$
a_{n+348}=a_n,\qquad
(-1)^n a_{n+174}=-a_n.
\tag{23}
$$
于是原半周期计算逐项给
$$
F(Z+1)=F(Z),\qquad
F(Z+s_0)=e^{-174\pi i s_0-348\pi iZ}F(Z).
\tag{24}
$$
所以
$$
S_\Lambda(Z)=e^{174\sqrt3\pi Z^2}F(Z)
 \in H^0(\mathbf C/\Lambda,\mathcal O(174[0])),
\quad \Lambda=\mathbf Z+s_0\mathbf Z.
\tag{25}
$$
所有 Fourier 序列的映射是单射：一个恒零的 (22) 的每个 Fourier
系数都为零，继而 (21) 的原有限向量为零。两侧维数均为174，
因此 (25) 覆盖整个原标准空间，而不是58维 δ-pullback 子空间。

这也精确解释 −1 的符号：二处 fA、fB 均偶，三处 φo 为奇，
二十九处还可取偶或奇向量。全截面的 z↦−z 特征是三个因子的乘积。
“原线丛次数174为偶”不意味着其所有截面都偶，更不能删掉 φo。
式(14)的三处反射号无需由另外一个因子补偿才能成立。

R772 的全部 finite-p 平移和正交伙伴 jets 只给这个174维池的
代数线性组合及其实际 p-primary 平移；它们没有扩大 (18) 的三处范围。

## 6. Hilbert90 转置与真实 Hecke 角色表

令 τ 为 (16) 的任一个环面特征，定义
$$
\widetilde{\tau}^{-1}(z)=\tau(z/\bar z)^{-1},\qquad
\chi_{3,\tau}=\chi_3^0\,\widetilde{\tau}^{-1}.
\tag{26}
$$
Yang 的 splitting 对这个有限扭曲的变化准确为 τ(g)^-1。
确实
$$
\frac{\delta(g-1)}{\overline{\delta(g-1)}}=g,
\tag{27}
$$
所以原 splitting 公式中的 twisting multiplier 就是 τ(g)^-1。
因此 (18) 中的对应向量在真正的 ω_{87,χ3,τ} 下固定。
这个方向不是根据一个有限素理想的 CM 特征反猜的。

在三处，每个单位 modδ² 唯一写成 εω^a，
ε∈{±1}、a∈{0,1,2}。因
ω/barω=ω²、δ/barδ=−1，完整表为
$$
\boxed{
\begin{array}{c|c|c|c|c}
\text{向量}&\chi_{3,\tau}(\epsilon\omega^a)&
 \widetilde{\tau}^{-1}(\delta)&
 \chi_{3,\tau}(\delta)&a(\chi_{3,\tau})\\ \hline
\phi_0&\epsilon&1&-i&1\\
\phi_{\mathrm e}&\epsilon\omega^a&1&-i&2\\
\phi_{\mathrm o}&\epsilon\omega^a&-1&+i&2
\end{array}}
\tag{28}
$$
a(χ) 是 δ-adic conductor 指数。新增单位角色在
1+δO 上非平凡，在1+δ²O上平凡，所以最后两行的2是精确值，
不是一个粗上界。

三条角色在 Q3× 上都严格为 ε_{K3/Q3}：
Hilbert90 比 z/bar z 对 z∈Q3× 为1。
特别两个 uniformizer 符号都满足
χ(3)=χ(−1)χ(δ)^2=1；不能因 χ(δ)=+i 就误认为中心角色改变。

(28) 中的 χ 是 Yang 全权正来源在三处的实际 unitary 分量。
组装某条全局 type-(1,0) 目标或负一 finite-χ 分支时，
仍须同二处、二十九处及无穷权满足主 μ6 的积关系。
本篇不把单独的三处表当作已经定义好的全局 Hecke 角色。
特别 φe 与 φo 虽有相同单位角色，uniformizer 相差未分歧二次；
全局组装时不能合并它们。

## 7. 与原点公式及算术域的接口

R774 已对满足其完整假设的已识别 type-(1,0)、root-negative
自对偶角色支付一般3导子的 good pair、真正临界 companion、
全部有限 Hom 和同一 point-eigensector 公式。
因此本篇新出现的 δ² 本身不再是该定理的禁区。

剩余的准确来源任务是：把 (21) 在二处和二十九处一并分解，
付全局有限角色和全权 theta–Katz 平方，再逐个应用 R774。
下列事项没有由 (28) 自动完成：

1. 某个任意有限 p 门只保裸 type5 来源；其它角型可由 physical χ 补偿。
2. 每个有限方向的负一单位值非零。
3. 原 JS′、JT′ 或第三中央为零会使这些条件行分别为零。
4. 点因子幂等元可与任意 N、n 的无限 p-adic 极限交换。

原 R772 的 P58/P0 缩放、全部有限门与完整补域不变；
本篇只把其中的三处局部范围由未定界限收紧为 (18)、(28) 的精确表。

## 文献、依赖及计算范围

- T. Yang, *Eigenfunctions of the Weil representation of unitary group of one variable*,
  Trans. Amer. Math. Soc.350 (1998), 2393–2407：
  §0、Theorem0.1、原 lattice model 与 fw。
  作者全文：<https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*,
  Compositio Math.117 (1999), 337–359：
  §1 式(1.6)–(1.9)、Proposition1.2、Corollary1.4、Appendix(A11)。
  作者全文：<https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)：
  原加性角色、极化、三处二次 Gauss 及完整半周期规范。
- [R772](R772-original-p58-orthogonal-weight-and-full-finite-schwartz-source.md)：
  原 P0 整行、全部174维来源、17处整分裂、有限门和共同周期。
- [R774](R774-ramified-discriminant-good-pairs-and-exact-point-factors.md)：
  已识别完整角色的一般3导子点公式。

本篇所有矩阵与相位均由显示的三个余类、原局部公式和原半周期直接证明。
没有新增数值扫描、辅助素数实验或需存储的重算数据。

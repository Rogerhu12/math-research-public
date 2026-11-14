# R112：非保圈度量修复的模态投影与稳定后验界

2026-11-12，Astra-visible-flex-fd2d / root。

**状态：本文的线性恒等式、有限维投影、精确后验界及保像集定理均已证明。**
它允许径向位移依赖角度，故不受 R109 的保圈重标下界直接排除。
**尚没有用本方法得到达到原容差的新完整图。**
尤其线性最小二乘或采样小残差不是原 g 的完整度量证书；下述正则性、可逆性、接口及精确后验必须实际支付。

本文不改变当前固定物理 g、参数或时间范围，不把重新拟合一个目标度量叫作修复。

## 1. 固定旋转度量上的全部一阶应变

在一个材料环带上取

$$g=ds^2+f(s)^2\,d\theta^2,\qquad f>0,\quad f\in C^2.$$

设当前实际图为 $X$，其诱导度量 $h=X^*e=g+E$。
$X\in C^2$ 给 $h,E\in C^1$；不要求曲面为 $C^3$。
这里 $E$ 是实际 Cartesian 导数形成的差，不能以源方程右端的代数约束代替。

令材料位移为

$$v=a(s,\theta)\partial_s+b(s,\theta)\partial_\theta.$$

直接微分坐标拉回，得到完整 Lie 导数

$$
(\mathcal L_vg)_{ss}=2a_s,\qquad
(\mathcal L_vg)_{s\theta}=a_\theta+f^2b_s,
$$
$$
(\mathcal L_vg)_{\theta\theta}=2ff'a+2f^2b_\theta.
\tag{1}
$$

在目标正交框架 $(\partial_s,f^{-1}\partial_\theta)$ 中，归一化形式为

$$
S_f(a,b)=
\begin{pmatrix}
2a_s&fb_s+a_\theta/f\\
fb_s+a_\theta/f&2(f'/f)a+2b_\theta
\end{pmatrix}.
\tag{2}
$$

证明只需对 $\Phi_t=(s+ta,\theta+tb)$ 的
$D\Phi_t^Tg(\Phi_t)D\Phi_t$ 在 $t=0$ 求导。
式 (1) 包含径向位移造成的圆周目标半径变化；漏掉 $2ff'a$ 会得到错误的修复方程。

## 2. 半测地清除的准确范围与终端漂移

若先规定 $a(0,\theta)=b(0,\theta)=0$，要求一阶 $ss,s\theta$ 分量全部为零，
则解被唯一确定为

$$a(s,\theta)=-\frac12\int_0^s E_{ss}(t,\theta)\,dt,$$
$$b(s,\theta)=-\int_0^s
\frac{E_{s\theta}(t,\theta)+a_\theta(t,\theta)}{f(t)^2}\,dt.
\tag{3}
$$

剩下的角分量恰为

$$R=E_{\theta\theta}+2ff'a+2f^2b_\theta.\tag{4}$$

式 (3) 并不使 (4) 自动变小。角微分可能放大高 Fourier 模，
因此强行消去原本很小的两个分量也可能使第三个分量更坏。
这是一种确定的线性构造，不是任何非保圈重标都必须遵从的约束。

若还要求终端 $a(L,\theta)=b(L,\theta)=0$，则 (3) 必须满足两项积分条件

$$\int_0^L E_{ss}\,ds=0,\qquad
\int_0^L\frac{E_{s\theta}+a_\theta}{f^2}\,ds=0.
\tag{5}$$

不满足时不能把终端漂移直接删掉。若改用截断函数 $\chi(s)$，实际线性残差增加

$$
S_f(\chi a,\chi b)-\chi S_f(a,b)
=\begin{pmatrix}2\chi'a&f\chi'b\\f\chi'b&0\end{pmatrix}.
\tag{6}
$$

因此窄截断段有明确的导数代价，必须与原应变一起计入。

式 (3) 的 C² 正则性也不是仅由任意 $E\in C^1$ 自动得到。
例如 $b_{\theta\theta}$ 需要其积分被积函数有相应的角正则性。
后续定理直接要求实际采用的 $a,b\in C^2$；在本题可用有限 Fourier、共享两 jet 的径向 Hermite 字段明确满足它。
把仅逐段线性的采样位移画出来不支付这个条件。

## 3. 同时分担三项误差的逐模投影

写归一化误差为

$$B=\begin{pmatrix}e&z\\z&\gamma\end{pmatrix}
=\operatorname{diag}(1,f^{-1})E\operatorname{diag}(1,f^{-1}).$$

考虑一组常见的实对称 Fourier 模

$$e=e_k(s)\cos k\theta,\quad z=z_k(s)\sin k\theta,
\quad\gamma=\gamma_k(s)\cos k\theta,$$
$$a=A(s)\cos k\theta,\qquad b=C(s)\sin k\theta,\qquad k\ge1.$$

式 (2) 给三个残差系数

$$u=e_k+2A',\quad
v=z_k+fC'-kA/f,\quad
w=\gamma_k+2(f'/f)A+2kC.\tag{7}$$

给定正径向权 $\omega(s)>0$，Frobenius 应变平方的角积分除以常数 $\pi$ 后为

$$J_k(A,C)=\int_0^L\omega f\{u^2+2v^2+w^2\}\,ds.\tag{8}$$

完整三项共同进入，而不是把前两项设为绝对零。
相反奇偶的实模同理；不同 $k$ 由三角正交性完全解耦。
$k=0$ 直接由 (2) 处理，不能凭空保留不存在的 $\sin0\theta$ 项。

### 命题 1：有限维投影确实存在且唯一

在任意线性无关的有限维 C² 径向基中求 $A,C$，其中终端位移为零，
并加所需的镜像或接口约束。假设这些约束至少排除非零常量 $A$ 和非零常量 $C$ 同时作为零应变字段，
例如 $A(0)=0$、$A(L)=C(L)=0$。则 (8) 的 Hessian 正定，存在唯一全局极小点。

**证明。** Hessian 二次型就是去掉 $e_k,z_k,\gamma_k$ 后的同一积分。
若它为零，正权给 $2A'=0$，所以 $A$ 为常量；$A(0)=0$ 得 $A=0$。
第二项随后给 $fC'=0$，所以 $C$ 为常量；$C(L)=0$ 得 $C=0$。
线性无关基于是排除一切非零系数核。有限维严格凸二次函数存在唯一极小点。证毕。

若基字段为 $v_j$，正规方程准确写成

$$\sum_j\left\langle S_f(v_i),S_f(v_j)\right\rangle_\omega c_j
=-\left\langle S_f(v_i),B\right\rangle_\omega.\tag{9}$$

增大同一可行有限维子空间不会提高最小的这个 $L^2$ 值。
但它**不保证**最大误差下降，也不保证未表示的高 Fourier 模、真实接口或非线性余项小。
改变数值权 $\omega$ 只是选取修复字段的方法，目标 g 本身仍是原来那个。
离散 FFT 或少量径向点只能筛选；连续结果要另包围全部区间和全部角度。

## 4. 只用 C¹ 度量误差的稳定精确后验恒等式

设实际选定的位移 $v=(a,b)$ 为 C²，令

$$\Phi=\operatorname{Id}+v,\quad K=Dv,\quad
\Delta g=g\circ\Phi-g,\quad E_\Phi=E\circ\Phi.$$

这是坐标加法定义的映射；不把线性化字段直接当作测地指数映射。
精确拉回误差为

$$\mathcal R=(I+K)^T(g\circ\Phi+E_\Phi)(I+K)-g.$$

把同阶项准确消去后得到

$$\begin{aligned}
\mathcal R={}&E+\mathcal L_vg\\
&+[\Delta g-a\,g_s]+[E_\Phi-E]\\
&+K^T(\Delta g+E_\Phi)+(\Delta g+E_\Phi)K\\
&+K^T(g\circ\Phi+E_\Phi)K.
\end{aligned}\tag{10}
$$

**证明。** 展开两个 $I+K$，再用
$\mathcal L_vg=a g_s+K^Tg+gK$ 逐项归并。没有丢掉任何二阶或更高阶项。证毕。

式 (10) 的优势是先消去已知接近的系数，不必对两个 O(1) Gram 矩阵各自取大区间后相减。
其中

$$\|\Delta g-a g_s\|
\le\tfrac12|a|^2\sup\|g_{ss}\|,\qquad
\|E_\Phi-E\|
\le |a|\sup\|E_s\|+|b|\sup\|E_\theta\|,
\tag{11}$$

上确界只需覆盖连接 $p$ 与 $\Phi(p)$ 的短坐标线段。
第一式用 $g\in C^2$；第二式只用 $E\in C^1$ 的微积分基本定理。
$E_s,E_\theta$ 可由实际 $X$ 的一、二阶导数形成，不需要曲面的三阶导数。

为给一个完全明确的保守数值预算，假设在所需区间上

$$|a|\le A_0,\quad |b|\le B_0,\quad\|K\|\le\kappa,$$
$$\|g_s\|\le G_1,\quad\|g_{ss}\|\le G_2,
\quad\|g\circ\Phi\|\le G_0,$$
$$\|E_s\|\le L_s,\quad\|E_\theta\|\le L_\theta,
\quad\|E_\Phi\|\le E_0.$$

则 (10) 除线性残差外的坐标算子范数至多

$$N=\tfrac12G_2A_0^2+L_sA_0+L_\theta B_0
 +2\kappa(G_1A_0+E_0)+\kappa^2(G_0+E_0).\tag{12}$$

若 $f\ge f_*>0$，完整相对误差满足

$$\|g^{-1/2}\mathcal Rg^{-1/2}\|
\le\|g^{-1/2}(E+\mathcal L_vg)g^{-1/2}\|
+\max(1,f_*^{-2})N.\tag{13}$$

可逐区间使用自己的 $f_*$ 和上界，或直接对 (10) 的各矩阵乘积作区间包围，避免不必要的全局最小半径损失。
若某一展开跨越径向 Hermite 接口，$E\in C^1$ 仍使 (11) 有效；只需覆盖短线段两侧的实际导数。

### 4.1 改在移位点使用线性残差：可完全省去 E 的导数

还有一个更适合当前小位移的精确恒等式。令
$\mathcal L=E+\mathcal L_vg$，$y=\Phi(x)$，下标 $x,y$ 表示在对应点求值，则

$$\begin{aligned}
\mathcal R(x)={}&\mathcal L(y)
 +[g(y)-g(x)-a(y)g_s(y)]\\
&+[K(x)-K(y)]^Tg(y)+g(y)[K(x)-K(y)]\\
&+K(x)^TE(y)+E(y)K(x)+K(x)^Th(y)K(x).
\end{aligned}\tag{14a}
$$

**证明。** 从 $\mathcal R=(I+K_x)^Th_y(I+K_x)-g_x$ 展开；
减去 $\mathcal L_y=E_y+a_y(g_s)_y+K_y^Tg_y+g_yK_y$ 后，余项逐一就是上式。证毕。

假设在字段支撑及连接线段上

$$|v|\le d,\quad |a|\le A_0,\quad\|Dv\|\le\kappa,\quad
\|D^2v\|_{\rm bilinear}\le H_0,$$

并有 $\|g\|\le G_0$、$\|g_s\|\le G_1$、$\|g_{ss}\|\le G_2$、$f\ge f_*>0$。
旧图若已有相对误差 $\delta$，则 $\|E(y)\|\le\delta G_0$。
微积分基本定理给

$$\|K(x)-K(y)\|\le H_0d,\qquad |a(y)-a(x)|\le\kappa d,$$

而从 y 向 x 作一阶 Taylor 展开得

$$\|g(y)-g(x)-a(y)g_s(y)\|
\le\tfrac12G_2A_0^2+G_1\kappa d.$$

故 (14a) 的全部非线性余项坐标范数至多

$$N_*=\tfrac12G_2A_0^2+G_1\kappa d+2G_0H_0d
 +2\kappa\delta G_0+\kappa^2(1+\delta)G_0.\tag{14b}$$

若已经连续证明 $\|g^{-1/2}\mathcal Lg^{-1/2}\|\le U$，
在移位点 y 仍可使用同一个 U。目标框架转回 x 只增加因子

$$\gamma=\sup\max\{1,f(y)^2/f(x)^2\}
\le1+G_1A_0/f_*^2.$$

于是一个完全不需要 $E_s,E_\theta$ 的实际后验界是

$$\boxed{\|g(x)^{-1/2}\mathcal R(x)g(x)^{-1/2}\|
\le\gamma U+\max(1,f_*^{-2})N_*.}\tag{14c}$$

这里的 $D^2v$ 只作用于选定的 C² 修复字段；没有要求原 C² 曲面的三阶导数。
已定义的有限 Fourier/Hermite 字段可直接给这个上界。
若某个闭子环带上字段恒为零，$\Phi$ 在那里就是恒等，旧误差可直接复用。
在已证明 $\Phi$ 是全局微分同胚后，固定子环带的边界还阻止活动点被映射穿过它；
因此对只支撑在 $f\ge.4$ 的字段，不必把深 cuff 的最小半径代入 (14c)。

以上也允许先对一个已经严格包围原固定目标的 supplier 度量 $g_0$ 作计算。
若 $\|g^{-1/2}(g_0-g)g^{-1/2}\|\le\epsilon_0$ 且相对 $g_0$ 的完整后验为 $U_0$，
则相对原 g 的上界为 $\epsilon_0+(1+\epsilon_0)U_0$。
这由 $g_0\le(1+\epsilon_0)g$ 及三角不等式直接得到；必须计入实际已证明的 $\epsilon_0$，而不是换目标。

## 5. 真正的材料微分同胚和固定接口

### 命题 2：一个足够的全局可逆条件

设 $a,b$ 为周期 C² 字段，$a(0,\theta)=a(L,\theta)=0$，
并且在整个材料圆柱的提升条带上

$$\|D(a,b)\|_{\mathbb R^2\to\mathbb R^2}\le\kappa<1.\tag{14}$$

则 $\Phi(s,\theta)=(s+a,\theta+b)$ 是这个闭材料环带的 C² 微分同胚。

**证明。** $\partial_s(s+a)>0$，固定 $\theta$ 时径向两端保持，所以像仍在同一径向区间。
对提升条带内任意两点 $p,q$，沿直线积分给

$$|\Phi(p)-\Phi(q)|\ge(1-\kappa)|p-q|.$$

因此提升映射一一；它与 $2\pi$ 平移等变，故圆柱上的映射也一一。
$I+Dv$ 处处可逆，边界上的角映射严格递增且次数为一。
内部局部微分同胚、紧性和边界对应给整个环带上的满射；也可用
$\Phi_t=\operatorname{Id}+tv$ 的次数一同伦直接得到。逆映射由逆函数定理为 C²。证毕。

式 (14) 是充分条件，不要求它是最优条件。
若不同坐标尺度造成它过严，可在固定的线性坐标缩放后验证同一证明；不能只检查有限点的 Jacobian 为正。

要接上固定帽，令 $a,b$ 在 cuff 的完整两 jet 为零，或者在 cuff 的一个开邻域恒零。
这样 $\Phi$ 可向帽延为恒等映射，仍全局 C²。
若上、下半图以中央镜像拼接，令径向位移 $a$ 对有符号 $s$ 为奇函数、角位移 $b$ 为偶函数；
相应端点条件是 $a(0,\theta)=a_{ss}(0,\theta)=b_s(0,\theta)=0$。
这明确支付镜像的 C² 接合，不以半图上的连续位移代替全局材料映射。

## 6. 相位族的所有像集几何准确保留

现假设上述 $\Phi$ 已全局 C² 可逆，并向固定帽延为恒等。
置 $Y=X\circ\Phi$。其像集与 X **完全相同**，没有小量近似。
在活动部分用物理材料角的相位作用定义

$$Y_\alpha=R_\alpha\circ Y\circ\tau_{-\alpha},$$

帽保持逐点不动，公共圆领两 jet 仍是同一个旋转背景。
由于 $g$ 对材料角平移不变，(13) 的全域上界自动对所有 $\alpha$ 相同。
这里不能把 $X_\alpha\circ\Phi$ 与上式混为一谈：一般非保圈 $\Phi$ 不与材料角平移交换。

每个相位活动像集仍是 $R_\alpha X(A)$，固定帽像集也原封不动。
所以整个相位族的直径、固定 H、held 距离、含反射的刚体商距离、嵌入性和 reach 全部准确保留。
不需要重新估计这些几何量，也不需要 R110 的小差几何转移。
仍必须给出自己的全域 (13)、C² 字段和可逆性；线性 screen 并不因此升级为等距解。

## 7. 与当前主线的关系

R109 排除了旧 M12/M14 仅作保圈径向与角向重标就达到原 $2\cdot10^{-9}$；
本文允许 $a_\theta\ne0$，所以提供一个不同而可实际检验的后处理空间。
它不保证这个空间中存在足够好的修复。

当前实际 M12 common 的半测地 screen 已显示强制清除 E/F 会放大 G，因此这条具体字段不登记为候选。
逐模平衡投影仍只能产生待核实字段。若无法通过连续后验，就继续原 M15/W22 的真实联解，
不把纯参数变化降低射击范数当作完整 g 误差下降。
原 fixed-g refinement 比较链、共同 exact bridge 和所有失败数据仍保留。

## 8. 本题 flat17 的已实算充分数值门

`scripts/fd2d-noncircle-pullback-budget.py` 从旧M12自己的冻结target和精确二进物理参数出发，
对14段flat-ramp的径向一、二阶导作准确有理Bernstein包围；桥段的角多项式Bernstein值
在[0,3)内，故向内桥半径不增，二阶导由其明确三次系数包围。尾的实际旋转背景曲率≤6
给|f_ss|≤6。因此在字段活动区f≥.4，可使用
G0=1.21、G1=2.2、G2=1000（计算所得G2已有理上界小于94）。

取充分字段门 |p|,|q|≤1e−10、||Dv||≤1e−6、||D²v||≤.01，
旧误差保守δ=3e−8、连续linear U≤1.9e−9、已知目标转移≤1e−12。
代入(14b)–(14c)，向外区间算术实际给
非线性坐标余项≤4.705312984226618e−12，
原fixed-g完整相对误差≤1.930408208765848e−9<2e−9。

结果在 `2026-11-12-fd2d-noncircle-pullback-budget.json`。
这是已证明的**充分box**；实际字段的全域导数、线性残差、接口、可逆性仍须逐项支付。
初步projection的采样读数不填写这些前提，当前不登记完成。

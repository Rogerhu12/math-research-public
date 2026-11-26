# 好二辅助输入的 I9/I3 曲面：实际三同源、自同构商的限制与剩余比较

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

本注记录继续 R990 时实际使用的曲面，并证明两项范围明确的事实：该曲面有平方为纤维乘负三的真实次数三有理自映射；但其任何有限自同构群商的解消都不是 K3。后者只排除直接自同构商，不排除另一个曲面的共同覆盖、非 Galois 有理映射或一般代数对应。新辅助输入的完整有限角色和实际检验向量另在 R991；本注不把 Hodge 型或相同新形式当作已经构造了 Chow 对应。

## 1. 同一个有理模型

固定 $K=\mathbf Q(\delta)$、$\delta^2=-3$、$\omega=(-1+\delta)/2$。考虑 Tate 三挠曲线及它的三次基变换
$$
 \mathcal E_t:\quad y^2+xy+ty=x^3,
 \qquad B:\quad v^3=t(1-27t).
 \tag{1}
$$
令 $S\to B$ 为相应相对极小光滑椭圆曲面。这里 $B$ 的光滑完备化通过
$$
 X=-12v,\qquad Y=4-216t
 \tag{2}
$$
与 $Y^2=X^3+16$ 同构。进一步 $X=4x_0,Y=8y_0+4$ 给 $y_0^2+y_0=x_0^3$。

式 (1) 的原有理椭圆曲面在 $t=0,1/27,\infty$ 分别有 $I_3,I_1,IV^*$。三分支均全分歧；相对极小基变换后纤维分别为 $I_9,I_3$、光滑纤维。这是 François Greer–Yilong Zhang，*Elliptic-elliptic surfaces and the Hesse pencil*（2024），[arXiv:2409.18927](https://arxiv.org/abs/2409.18927)，Proposition 4.9、Propositions 11.1–11.2 的极限曲面（其基参数经线性换元）。原文 Remark 5.6 明确包含此极限，给 $\mathrm{MW}_{\rm tors}=\mathbf Z/3$ 和 $|\det\mathrm{NS}|=3$；Proposition 5.9 付其 $\mathbf Q$ 模型。不是把该文另一个 $I_6+2I_3$ 曲面的结论搬来。

直接从 (1) 也得 $e(S)=12$、$\chi(\mathcal O_S)=1$、$q=p_g=1$。无多重纤维，基本线丛在 $B$ 上次数一，故 $K_S$ 是它的拉回，$\kappa(S)=1$，Iitaka 纤维化就是 $S\to B$。$I_9,I_3$ 的平凡格秩为 $2+8+2=12=h^{1,1}$，从而 $\rho=12$、几何 Mordell–Weil 秩为零、$T(S)$ 秩为二。

记两个坏纤维基点为
$$
 P=(0,4),\qquad -P=(0,-4)\quad\text{在式 (2) 上}.
 \tag{3}
$$
切线 $Y=4$ 与该三次曲线在 $P$ 的交数为三，所以 $P$ 恰为三阶点。两个纤维类型不同，不能在自同构下互换。

## 2. 真实次数三自映射及准确的负三

令 $Q=(0,0)\in\mathcal E_t[3]$。按 Jacques Vélu，*Isogénies entre courbes elliptiques*，C. R. Acad. Sci. Paris 273 (1971), A238–A241，公式 (7)–(11)（[Ghitza 英译原文](https://aghitza.github.io/publications/translation-velu.pdf)），以 $\{O,Q,-Q\}$ 为核的规范商 $\phi_t$ 是
$$
 \mathcal E'_t:\quad y'^2+x'y'+ty'
   =x'^3-5t x'-t-7t^2.
 \tag{4}
$$
其完整有理映射由原加法法则给出
$$
 x'(R)=x(R)+\sum_{A=Q,-Q}(x(R+A)-x(A)),
$$
$$
 y'(R)=y(R)+\sum_{A=Q,-Q}(y(R+A)-y(A)).
 \tag{5}
$$
尤其 $x'=x+t/x+t^2/x^2$。规范微分满足 $\phi_t^*\omega'_t=\omega_t$，其中 $\omega_t=dx/(2y+x+t)$。

为核所有缩放常数，原曲线和商曲线的完整不变量为
$$
 \begin{array}{c|ccc}
  &c_4&c_6&\Delta\\\hline
 \mathcal E_t&1-24t&-1+36t-216t^2&t^3(1-27t)\\
 \mathcal E'_t&1+216t&-1+540t+5832t^2&t(1-27t)^3.
 \end{array}
 \tag{6}
$$
取
$$
 t'=1/27-t.
 \tag{7}
$$
在 $B$ 上 $(t,v)\mapsto(t',v)$ 是真实对合。直接代入 (6) 给
$$
 c_4(\mathcal E_{t'})=c_4(\mathcal E'_t)/9,\qquad
 c_6(\mathcal E_{t'})=-c_6(\mathcal E'_t)/27.
 \tag{8}
$$
在短 Weierstrass 坐标 $u=x+b_2/12$、$w=y+(a_1x+a_3)/2$ 中，方程是
$w^2=u^3-c_4u/48-c_6/864$。所以 (8) 给完全指定的 $K$ 同构
$$
 \iota_t:\mathcal E'_t\longrightarrow\mathcal E_{t'},
 \qquad (u',w')\longmapsto(u'/\delta^2,w'/\delta^3),
 \quad \iota_t^*\omega_{t'}=\delta\omega'_t.
 \tag{9}
$$
因此 $F_t=\iota_t\phi_t$ 与基对合 (7) 一起给 $S$ 的次数三有理自映射 $F$，且 $F_t^*\omega_{t'}=\delta\omega_t$。再做一次，在一般纤维上得到保原点的次数九同源，微分乘数是 $\delta^2=-3$。特征零中同源的微分表示单射：微分为零的群同态只能是零。因此准确有
$$
 \boxed{F^2=[-3]_{S/B}}
 \tag{10}
$$
作为有理映射的恒等式。这里的 $F$ 不是一个对合；$[{-3}]$ 的纤维次数为九，不能把它抹成恒等映射后取商。

下面的全局二形式同时固定符号：
$$
 \Omega=\frac{dt}{v^2}\wedge\frac{dx}{2y+x+t}.
 \tag{11}
$$
$dt/v^2$ 是 $B$ 的正则无零一形式；在 $t=0,1/27$ 的全分歧点，$dt$ 的二阶零与 $v^2$ 抵消。在无穷处取 $r$ 使 $t\sim r^{-3},v\sim c r^{-2}$；消去三重基变换的 $IV^*$ 后，原纤维微分是 $r$ 乘极小模型微分。因此 (11) 在该纤维恰有一阶零，别处无极，生成 $H^0(S,K_S)$。由 (7)、(9)，
$$
 \boxed{F^*\Omega=-\delta\Omega.}
 \tag{12}
$$
图闭包因而给实际的代数自对应；在秩二超越上同调上它的特征值是 $-\delta,\delta$。本注不从 (12) 推出 $t_2(S)$ 与 CM 椭圆平方的 Chow 同构，也不未经论证把一个上同调关系提升为已指定的 Chow 双逆。

## 3. 任何有限自同构商均不是 K3

这是对实际曲面 (1) 的证明，不是对所有 $p_g=q=1$ 曲面的断言。

任一 $g\in\mathrm{Aut}(S_{\overline K})$ 保持 Iitaka 纤维化，所以诱导 $\alpha\in\mathrm{Aut}(B)$。它必须分别固定 (3) 的两点。以无穷点为群原点，写 $\alpha(b)=u b+c$，其中 $u\in\mu_6$。同时固定 $P,-P$ 给
$$
 (u-1)(2P)=0,\qquad c=P-uP.
 \tag{13}
$$
在模型 (2) 上 $[\omega]$ 固定 $P$，而 $[-1]P=-P\ne P$。所以 (13) 恰迫 $u\in\mu_3$、$c=0$。所有可能基作用均由
$$
 d:(t,v,x,y)\longmapsto(t,\omega v,x,y)
 \tag{14}
$$
生成；由 (11)，$d^*\Omega=\omega\Omega$。

将 $g$ 与某个 $d^{-j}$ 复合后，得到一般纤维上的自同构。一般纤维的 $j$ 非常数，故其保原点自同构仅为 $\pm1$；任意自同构是截面平移再复合这两个保原点自同构之一。截面平移保持纤维微分，反演使其变号。因此
$$
 g^*\Omega=\varepsilon\omega^j\Omega,
 \qquad \varepsilon\in\{1,-1\},\ j\in\{0,1,2\}.
 \tag{15}
$$
式 (15) 等于 $\Omega$ 当且仅当 $j=0,\varepsilon=1$，即 $g$ 是纤维平移。

现令 $G$ 为任意有限自同构群，$Y$ 为 $S/G$ 的光滑解消。商奇点在特征零为有理奇点；二形式的下拉/不变量描述给
$$
 H^0(Y,K_Y)=H^0(S,K_S)^G.
$$
若 $p_g(Y)=1$，则每个 $g\in G$ 都须固定 $\Omega$，故每个都是纤维平移。此时商仍有映射 $Y\to B$，而 $B$ 的非零一形式拉回非零，故 $q(Y)\ge1$。若某个 $g$ 不固定 $\Omega$，则 $p_g(Y)=0$。两种情形都排除 K3 的 $p_g=1,q=0$。所以
$$
 \boxed{\text{任何有限 }G\subset\mathrm{Aut}(S_{\overline K}),
   \text{其商的光滑解消都不是 K3。}}
 \tag{16}
$$
这特别排除了寻找本曲面的 Nikulin 型对合来直接套 R988 的路线。也不能从 CM 椭圆曲线乘积直接 generically finite 支配 $S$：前者 Kodaira 维数零，后者为一；消解不定点后的 canonical 拉回公式在特征零给 generically finite 映射的 Kodaira 维数不等式，方向与此相反。

## 4. 已检查的实际平面模型与仍未支付的比较

式 (1) 的原有理曲面有双有理参数
$$
 a+b+c=1,\qquad t=abc,\qquad x=-ab,\quad y=ab^2.
 \tag{17}
$$
在相应开集，逆式是 $b=-y/x$、$a=x^2/y$、$c=1-a-b$；将原方程代入即得 $abc=t$。因此 $S$ 与下面的循环三重平面覆盖双有理：
$$
 \boxed{V^3=abc\bigl((a+b+c)^3-27abc\bigr),\qquad
 \deg V=2.}
 \tag{18}
$$
该式的第二个因子是有结点三次曲线，不是把 $a^3+b^3+c^3-3abc$ 误写成 $(a+b+c)^3-27abc$ 后得到的三条直线。此前尝试将 Hesse 的三组三角形对应成 Fermat/Ceva 九线安排也不成立：实际交点为九个三重点及九个双点，并非 Ceva 九线的十二个三重点。故这些形式目前不支付 Fermat 曲面支配或有限维 Chow 动机。

已读而不能替代本比较的原始文献还包括：

- Arapura–Greer–Zhang，[arXiv:2602.07302v1](https://arxiv.org/html/2602.07302v1)，Proposition 9.1 的对应来自其两个实际二重覆盖的共同 Kummer 曲面。该文纤维含 $IV/IV^*$ 的另一族不能无图套到本 $I_9/I_3$ 曲面。
- Shioda–Schütt，*An interesting elliptic surface over an elliptic curve*，[arXiv:math/0611103](https://arxiv.org/abs/math/0611103)，§6 的次数三 K3 基变换确实存在，但其曲面有唯一 $I_6^*$，超越 CM 域为 $\mathbf Q(i)$；不是本曲面。

继续工作的数学门仍是实际新输入的最高 $\lambda$ 分量非零/互反律，或者能计算该分量的一般代数对应。严格全 $G_K$ 模同构若已付，可以直接运输 Galois 上同调及相应局部条件；这不自动等同新旧循环，不自动给跨 $p$ 非零，也不要求先证明一个与所用非零定理无关的 Chow 逆。上述排除不会关闭这两条真正的路线。

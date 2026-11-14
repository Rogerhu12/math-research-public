# 完整 Cartier、固定单位的次数界与移动 Hasse 留数

日期：2026-11-12。状态：本文的局部次数界、实际双留数公式、
固定挠点 Wronskian、cusp 首项和移动支撑下界均已证明。
本文只检验一种具体的有限维化途径：对实际 Kummer 输入施完整
Cartier 后，是否仅因极点阶下降便落入一个固定极点除子的空间。
答案是否定的；这不排除其他 Frobenius、Hecke 或 cohomology 比较，
更不否定本课题的 Sha 无穷素数目标。

全篇固定实际的 $N=68$ 全级 Legendre 族
\[
 E_\lambda:y^2=x(x-1)(x-\lambda),\qquad
 t=\lambda-\tfrac12,\qquad s=1-4t^2,\qquad Z=-x/y.
\]
所用 $256$ 标签 $\mathcal S$、旋转标签
$\mathcal S^{\rm rot}$、单位 $R_{\mathcal S},R_{\rm rot}$ 及常数 $c_e$
均为[实际除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)
中的原对象。令
\[
 h_e=-\frac{c_e}{2N^2}
       (\log R_{\mathcal S}-i\log R_{\rm rot}).
 \tag{1}
\]
$h_e$ 在 $Z=0$ 规范为零；在整个代数曲面上只使用其准确的绝对微分
\[
 dh_e=-\frac{c_e}{2N^2}
       (d\log R_{\mathcal S}-i\,d\log R_{\rm rot}).
 \tag{2}
\]
因此 (2) 是固定代数一形式，不需要把形式对数本身当作有理函数。

## 1. 固定单位确实给出一个统一的 Cartier 次数界

先说明该途径中成立的部分。取一个固定光滑曲面的 étale 坐标图，
以 $(t,Z)$ 为两个坐标，其他坐标 $\mathbf y$ 满足固定方程
$\mathbf F(t,Z,\mathbf y)=0$，并反转固定 Jacobian 行列式 $J$。
删去一个固定有限坏位集合后，所有方程及有关固定单位都有整模型。
对坐标幂次 lift $\phi(t)=t^p,\phi(Z)=Z^p$，étale 性给唯一 lift。
模 $p^2$ 写
\[
 \phi(\mathbf y)=\mathbf y^p+p\mathbf v.
\]
若 $\mathsf J=\partial\mathbf F/\partial\mathbf y$，则
\[
 \mathbf v=-(\mathsf J^{[p]})^{-1}\mathbf E,\qquad
 \mathbf E=
 \frac{\mathbf F^\sigma(t^p,Z^p,\mathbf y^p)
                    -\mathbf F(t,Z,\mathbf y)^p}{p}\pmod p.
 \tag{3}
\]
分子确实可逐系数除以 $p$。其次数为 $O(p)$，常数只取决于固定方程；
$\det(\mathsf J^{[p]})=J^p$。这里没有声称系数的 Fermat 商有
一个统一的赋值上界。

若固定单位 $r=a/b$，置
\[
 B_r=\frac1p\log\frac{\phi(r)}{r^p}.
\]
用 $\phi(a)=a^p+p\delta a$ 等式展开，准确得到
\[
 B_r\bmod p=\frac{\delta a}{a^p}-\frac{\delta b}{b^p}
       =\frac{P_{r,p}}{(abJ)^p},
 \qquad \deg P_{r,p}\le C_rp.
 \tag{4}
\]
最后一个分母允许补上固定幂；$C_r$ 与 $p$ 无关。
这同[真实 Kummer cochain](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
的形式盘规范相容，绝非任意改变 lift 后仍保持次数界的断言。

在一个固定光滑紧化上，(4) 的极点除子因此不超过
$pD+D_0$，其中 $D,D_0$ 固定。对有理顶次二形式 $\alpha$，
完整 Cartier 的局部公式是
\[
 \mathscr C_2\!\left(\sum a_{ij}t^iZ^j\,dt\wedge dZ\right)
 =
 \sum a_{pi+p-1,pj+p-1}^{1/p}t^iZ^j\,dt\wedge dZ.
 \tag{5}
\]
系数及目标曲面带相应 Frobenius twist；在完美系数域上可作通常识别。
特别，一个素除子处极阶 $M$ 变成至多 $\lceil M/p\rceil$。
这是对局部一致化参数直接应用 (5) 的结果。

所以固定 $B_r$ 乘固定有理二形式后施 $\mathscr C_2$，
的确落入某个固定极点除子的有限维空间。没有 GM 权重时，
(2) 与 $d\log Z$ 的乘积甚至是固定对数二形式；
Cartier 保持这种对数形式，但必须对 $c_e,i$ 同时作系数 Frobenius，
不能把这些常数全当成 $\mathbb F_p$ 元素。

**这个结论本身不提供非零性。** 例如固定整数 $a\in\mathbb Z$、
$r=1-at$ 有
\[
 [t^p]B_r=\frac{a^p-a}{p}.
 \tag{6}
\]
统一极点阶与系数的统一浅赋值，是两种不同信息。

## 2. 实际临界行所增加的权重

以下取 $p\equiv3\pmod4$、$p\ge7$。沿用实际整 GM Frobenius 的
$U,V$，并置
\[
 \zeta_p=U/V,\qquad B=t\zeta_p.
\]
[完整 Wronskian 与导数行](2026-11-12-exact-gm-wronskian-and-kummer-derivative-row.md)
的式 (11)、(16)、(18) 给
\[
 \mathcal P_p(f)=
 \frac{[t^{p+1}]f'B^{p+2}}{p+2}
 -\frac ba f_1+p^2\frac ab\{f_3-(p+3)f_1\},
 \tag{7}
\]
\[
 \mathcal P_p(f)\equiv
 \tfrac12[t^{p-1}]f'\zeta_p^2-\frac ba f_1\pmod p,
 \qquad
 f'=\eta t^{p-1}M_o'(t^p)-[Z^p]\partial_t h_e.
 \tag{8}
\]
因此真正新增的代数二形式是
\[
 \boxed{\quad
 \Omega_p=\zeta_p^2\,dh_e\wedge d\log Z
          =\zeta_p^2(\partial_t h_e)\,dt\wedge\frac{dZ}{Z}.
 \quad}
 \tag{9}
\]
例如 (5) 在原点的常数项恰提取
$[t^{p-1}Z^p]\zeta_p^2\partial_t h_e$，带系数 Frobenius。
$1/Z$ 不能删掉。

已知的 $M_o$ 单位首项不会单独解决 (7)。
该 Wronskian 笔记式 (19) 中的显式 $-\eta$，
与[一阶模数](2026-11-12-first-modulus-vectorial-extension-and-critical-projection.md)
式 (26) 的 Kummer 修正中 $+\eta$ 准确相消。
本文不把这个已消去的常数再次当作非零输入。
另外，(9) 只是一层 Cartier 输入；求最终的除 $p$ 值仍须保留
(7) 的完整精度或同一笔记的模 $p^2$ 修正。

## 3. 实际 $\zeta_p$ 在所有 Hasse 根处有真简单极点

令
\[
 H_p(t)=P_{(p-1)/2}(2t),\qquad h_p=H_p'(0).
\]
[固定规范的 $p$-curvature](2026-11-12-legendre-p-curvature-with-fixed-normalization.md)
式 (4)、(18) 已证明 $h_p\ne0$，$H_p$ 的根全简单，且
\[
 \boxed{\quad V\equiv\frac{H_p}{h_p s^p}\pmod p.\quad}
 \tag{10}
\]
这里采用其原 $P_n(1)=1$ 规范。

为把这个形式盘等式用于全基，不能任取一个同 jet 的有理函数。
实际 proper Legendre 晶体也定义在
\[
 R_0=\mathbb Z_p[t,s^{-1}]
\]
的 $p$-adic 完成上。基 $(\omega,\nabla_t\omega)$ 在此仍是整基：
前述整 GM 笔记式 (2) 的基变换分母只有 $2,\lambda,1-\lambda$。
$\phi(t)=t^p$ 在这个完成环上合法，因为
$s(t^p)\equiv s(t)^p\pmod p$ 为单位。
同一个 crystalline–de Rham 整比较及 Hodge 拉回模 $p$ 为零，
使实际 Frobenius 矩阵的第一行在整个 $R_0^\wedge$ 上被 $p$ 整除。
所以定义 $U,V$ 的两个条目除 $p$ 后仍属于 $R_0^\wedge$，
从而
\[
 \bar U,\bar V\in\mathbb F_p[t,s^{-1}].
 \tag{11}
\]
限制到 $t=0$ 就是原来的实际矩阵，并非另选的比较。
(10) 因而也是这些有理函数的等式。

完整 Wronskian 模 $p$ 给
\[
 UV'-U'V=
 \frac1{s^{p+1}}+\frac ba\,t^{p-1}V^2.
 \tag{12}
\]
若 $H_p(\alpha)=0$，则 $s(\alpha)\ne0$，而 (10) 给 $V'(\alpha)\ne0$。
(12) 随即给
\[
 U(\alpha)V'(\alpha)=s(\alpha)^{-p-1}\ne0.
\]
因此
\[
 \zeta_p=\frac{A_\alpha}{t-\alpha}+B_\alpha+O(t-\alpha),
 \qquad A_\alpha\ne0.
 \tag{13}
\]
共有 $(p-1)/2$ 个这样的几何 Hasse 根。
这一步使用真实全局整 Frobenius；没有从一个形式 $p$ 次幂余项
猜测全局极点。

## 4. 真正的两次对数留数

在全级基曲线上固定一个实际截面 $R=-P$，令
\[
 z_P(t)=Z(-P_t).
\]
所用 $P$ 有准确阶 $68$。故 $z_P$ 在光滑基上既不为零也不为无穷；
$Z$ 在该点是 étale 坐标。具体地，$Z=-x/y$ 是度二映射，
其非平凡 involution 是 $R\mapsto T_0-R$；
分歧点满足 $2R=T_0$，均为四挠点，不能等于 $R$。
也可不使用 involution 而直接计算
\[
 \frac{dZ}{dx}=\frac{x(x^2-\lambda)}{2y^3}.
\]
在非二挠点处，临界条件是 $x^2=\lambda$；
倍点公式随即给 $2R=(0,0)$。因此实际阶 $68$ 的点
在所有目标特殊纤维中都保留这个局部坐标。

若 $dh_e$ 在该截面处的对数 residue 为常数 $m_P$，则局部写
\[
 h_e=m_P\log(Z-z_P(t))+\text{正则部分}.
\]
在 (13) 的一个基点附近，对 (9) 先取基方向 residue，
再取纤维方向的对数 residue，准确得到
\[
 \boxed{\quad
 \operatorname{Res}_{(\alpha,-P)}\Omega_p
 =
 -m_PA_\alpha^2
 \left\{(\log z_P)''+
               2\frac{B_\alpha}{A_\alpha}(\log z_P)'\right\}_{t=\alpha}.
 \quad}
 \tag{14}
\]
此处双 residue 按 $d(t-\alpha)\wedge d(Z-z_P(\alpha))$ 排序。
改变排序只改变整体符号，不影响非零性。

为核对最易漏的项，记 $\partial_t h_e=\gamma$，则
\[
 \gamma=-\frac{m_Pz_P'}{Z-z_P}+\cdots,\qquad
 \gamma'=-\frac{m_Pz_P''}{Z-z_P}
         -\frac{m_P(z_P')^2}{(Z-z_P)^2}+\cdots.
\]
基 residue 是 $(A_\alpha^2\gamma'+2A_\alpha B_\alpha\gamma)dZ/Z$。
二阶纤维极项与 $1/Z$ 相乘，贡献
$+m_P(z_P'/z_P)^2$，恰将 $z_P''/z_P$ 改成 $(\log z_P)''$。
只看到二阶极点后说 Cartier 将其杀掉，会漏掉这个简单留数。

也可用横截坐标 $v=Z-z_P(t)$ 一步核验：
(9) 的对数 $dv/v$ 系数是 $-m_P\zeta_p^2d\log z_P$。
Cartier 的局部公式保证双对数 residue 变为其 $p$ 次方根。
所以 (14) 非零时，$\mathscr C_2(\Omega_p)$ 在
$t=\alpha$ 上有真对数极点。二阶极点被降到一阶，不会将这个
非零 residue 降为零。

## 5. 两个原轨道标签与准确的 $m_P$

取原种子
\[
 P=(1,-1)/68,\qquad Q=-3P.
 \tag{15}
\]
两者都在原 $\mathcal S$ 中；$-3$ 是其生成元。
$\mathcal S$ 与 $\mathcal S^{\rm rot}$ 不交。
一个不依赖数值近似的核对如下。令
$f=34(1+i)$，在 $(\mathbb Z[i]/f)^\times$ 上，
$\epsilon(u)$ 是满足 $u\equiv\epsilon(u)\pmod{(1+i)^3}$ 的
唯一 $\mu_4$ 元素；令 $\lambda(3)=-i$ 定义
$\mathbb F_{17}^\times$ 上的四次角色。则
\[
 \chi(a+bi)=\epsilon(a+bi)
       \lambda\!\left(\frac{a+4b}{a-4b}\right)
\]
满足
\[
 \chi(-3)=\chi(-2+i)=1,\qquad \chi(-i)=-i\ne1.
\]
例如 $\epsilon(-2+i)=-i$，$(a+4b)/(a-4b)=11=3^7$，
所以第二个生成元的值确为一。
$P$ 的 annihilator 是 $(f)$，故这个角色已排除两个轨道相交。

固定除法单位的完整除子为
\[
 \operatorname{div}r_R=D_N-N^2(-R),\qquad
 D_N=\sum_{T\in E[N]\setminus O}(T)-T_0+T_1+T_\lambda.
\]
在 $-P$ 或 $-Q$ 处，$D_N$ 的系数都是一。
保留两组 $256$ 项的共同 $D_N$ 贡献，(1) 给
\[
 \boxed{\quad
 m_P=m_Q
 =-\frac{c_e}{2N^2}\{256(1-i)-N^2\}
 =\frac{c_e(273+16i)}{578}.
 \quad}
 \tag{16}
\]
所以不是只取 $c_e/2$。
对每个惰性 $p\ge7$，(16) 是单位：
若这样的 $p$ 整除 $273^2+16^2$，
则 $-1$ 在 $\mathbb F_p$ 为非平方迫使 $p$ 同时整除 $273,16$，
矛盾。其余分母和 $c_e$ 的坏位只在 $\{2,3,5,17\}$。

定义两个固定有理函数及其 Wronskian
\[
 f_P=\frac{d\log z_P}{dt},\qquad
 f_Q=\frac{d\log z_Q}{dt},\qquad
 \Delta=f_P'f_Q-f_Q'f_P.
 \tag{17}
\]
若在某个 Hasse 点 $\Delta\ne0$，(14) 对 $P,Q$ 不可能同时为零：
消去同一个 $2B_\alpha/A_\alpha$ 就会给 $\Delta=0$。
这也涵盖其中一个 $f_P,f_Q$ 为零的情形，不需要除以它们。

## 6. 一个 cusp 的准确首项：$\Delta$ 对全部目标素数均非零

使用与原周期完全一致的约定
$\tau=\omega_2/\omega_1$。
若 $\tau=\gamma\tau'$，
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，
标签 $r+s\tau$ 在新格上变成
\[
 (dr+bs)+(cr+as)\tau'.
 \tag{18}
\]
这不是把标签列向量直接乘以 $\gamma^{-1}$。

取 $\gamma=S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$
对应的 cusp，令
\[
 q=e^{2\pi i\tau'},\qquad w=q^{1/68},\qquad
 \varepsilon=e^{2\pi i/68}.
\]
此处确是实际 Legendre 族的参数，而不只是抽象 coarse 模曲线的参数：
$\lambda=1$ 的 Legendre 纤维为 split multiplicative $I_2$ 型，
其 Tate 参数的阶为二。实际 $68$ 级点只需加入
$\mu_{68}$ 及 $q^{1/68}$，故该 cusp 的惯性阶准确为
$68/\gcd(68,2)=34$；形式单位的 $68$ 次根在目标特征均可提取。
所以所选实际连通分量上 $w$ 是一致化参数。
(18) 把 $P=(1,-1)/68$ 送为 $(1,1)/68$，
其 Tate 参数为 $u=\varepsilon w$。
$Q=-3P$ 的 $Z$ 与 $3P$ 只差负号，故其对数导数可用 $u^3$ 计算。

由 $\lambda(-1/\tau')=1-\lambda(\tau')$ 及
$\lambda(\tau')=\vartheta_2^4/\vartheta_3^4$ 的定义级数，
\[
 t=\tfrac12-16w^{34}+O(w^{68}),\qquad
 \frac{dt}{dw}=-544w^{33}(1+O(w^{34})).
 \tag{19}
\]
系数在 $\mathbb Z[\varepsilon,1/2]$ 中。
Tate 曲线的标准坐标为
\[
 X(u)=\sum_{n\in\mathbb Z}\frac{q^nu}{(1-q^nu)^2}
       -2\sum_{n\ge1}\frac{nq^n}{(1-q^n)^2},
\]
\[
 Y(u)=\sum_{n\in\mathbb Z}\frac{(q^nu)^2}{(1-q^nu)^3}
       +\sum_{n\ge1}\frac{nq^n}{(1-q^n)^2}.
 \tag{20}
\]
当 $u=\varepsilon^a w^a$、$a=1$ 或 $3$ 时，
\[
 X=\frac{u}{(1-u)^2}+O(q/u),\qquad
 Y+\tfrac12X=\frac{u(1+u)}{2(1-u)^3}+O(q/u).
\]
在 $\lambda=1$ 的节点模型中，
$x=1+4X$、$y=\pm8(Y+X/2)$；
在整个 Tate 邻域，此坐标变换的系数与该极限相差 $O(q^{1/2})$。
理由是 Legendre 三个二挠点的 Tate 坐标在
$\mathbb Z[1/2][[q^{1/2}]]$ 中，且相应非消失根差为单位。
对 $Z=-x/y$ 的相对误差因此至少为
\[
 \min(34,68-2a)=34.
\]
由节点上的准确式 $Z=\pm(1-u^2)/(4u)$，得到
\[
 z_P=C_Pw^{-1}(1-\varepsilon^2w^2+O(w^{34})),\qquad
 z_Q=C_Qw^{-3}(1-\varepsilon^6w^6+O(w^{34})),
 \tag{21}
\]
其中 $C_P,C_Q$ 是只含 $2$ 和单位根的非零常数。
用 $Z(-P)$ 或 $Z(P)$ 只改变这些常数的符号。

写 $\ell_P=\log z_P,\ell_Q=\log z_Q$，但只对它们求导。
(21) 给
\[
 \ell_{P,w}=-w^{-1}-2\varepsilon^2w+O(w^3),\qquad
 \ell_{Q,w}=-3w^{-1}+O(w^5),
\]
\[
 \ell_{P,ww}\ell_{Q,w}-\ell_{Q,ww}\ell_{P,w}
       =12\varepsilon^2w^{-1}+O(w).
\]
换成 $t$ 导数时共同的 $t_{ww}$ 项准确消掉，故
\[
 \boxed{\quad
 \Delta=\frac{12\varepsilon^2}{(-544)^3}w^{-100}
                           +O(w^{-98}).
 \quad}
 \tag{22}
\]
首系数在每个 $p\notin\{2,3,17\}$ 都是单位。
因此这里不仅有特征零的 $\Delta\ne0$，
而且其全部目标素数约化都非零；无需再引入一个未计算的判别式例外。

作为标签变换的独立核对，另取
$\gamma=\left(\begin{smallmatrix}2&1\\21&11\end{smallmatrix}\right)$。
它仍在 $\lambda=1$ 上方，(18) 给 $P$ 的新标签 $(10,19)/68$；
$P,Q$ 的 Tate 距离分别为 $19,11$。
在这两个 cusp，$z_P,z_Q$ 的赋值向量是
$(-1,-19)$、$(-3,-11)$，也足以在特征零证明 (17) 非零。
真正保证模 $p$ 不退化的是更强的 (22)。

## 7. 固定零点数界与线性多个残留 Hasse 极点

令 $C^\circ$ 为**实际 Legendre 族全 $68$ 级点 torsor**
中容纳原标签的一条几何连通分量，
$C$ 为其在 $\lambda$ 直线上的正规紧化，
$d=\deg(C\to\mathbb P^1_\lambda)$。
这里不把 $C$ 无条件认定为 coarse 模曲线 $X(68)$：
Legendre 族的带符号 monodromy 与 $-I$ 必须保留。
以下证明也不需要这个认定。
两个点 $P,Q$ 的准确阶都是 $68$，
所以 $z_P,z_Q$ 在光滑基上为单位；其零极点只在 cusp。
因此 $d\log z_P,d\log z_Q$ 在每个 cusp 至多有简单极点。

还须核紧化及连通性在约化后保持，不能只用开放部分的 étale 性。
在每个目标 $p$ 的严格 henselian 基上，
整个 torsor 的群是 $\mathrm{GL}_2(\mathbb Z/68)$ 的子群；
后者的阶只有 $2,3,17$ 为素因子，故为 prime-to-$p$。
应用 SGA 1 (1971), Exposé XIII, Corollaire 2.9、§2.10
及 Lemma 2.11 的 tame specialization，
固定连通分量及各 cusp 惯性在几何特殊纤维中保持。
同一 Exposé 的 Proposition 5.4–5.5、Corollaire 5.6
给相对 Abhyankar/Kummer 局部式：
在一个 cusp 的严格局部环中，cover 由
$w^e=v$ 后的 étale cover 得到，其中 $v$ 是该 cusp 的基参数，
$e$ 与 $p$ 互素。一个分支的正规化完成环因而是
$\mathcal O[[w]]$。这同时证明紧化光滑、几何连通、
次数 $d$ 及各 cusp 指数的保持；开放部分由 $E[68]$ 的 étale 性处理。
这是对实际 torsor 的适用性论证，不依赖 coarse 模曲线的通用族。

以下用各 cusp 自己的 ramification index $e$ 来计数，
不要求先计算它们全都相等。

在 $\lambda=0$ 或 $1$ 上方，$dt$ 阶数为 $e-1$，于是
\[
 \operatorname{ord} f_P,\operatorname{ord} f_Q\ge-e,\qquad
 \operatorname{ord} f_P',\operatorname{ord} f_Q'\ge-2e.
\]
故 $\Delta$ 在这些 cusp 极阶至多 $3e$。
在 $\lambda=\infty$ 上方，$dt$ 阶数为 $-e-1$，
相应四个阶数分别至少为 $e,e,2e,2e$，没有极点。
非 cusp 处 $dt$ 非消失，两个对数微分也正则，仍无极点。
因此对每个 $p\notin\{2,3,17\}$，
\[
 \deg\operatorname{div}_\infty(\bar\Delta)
 \le3\sum_{c\mid\lambda=0}e_c+
     3\sum_{c\mid\lambda=1}e_c=6d.
 \tag{23}
\]
(22) 保证 $\bar\Delta$ 不为零，故其零点总数含重数也至多 $6d$。

一个 Hasse 底点上有 $d$ 个几何全级点。
若该底点在每个全级点处都使 (17) 为零，就至少消耗 $d$ 个零点。
所以至多六个 Hasse 底点能全部例外。对其他每个 Hasse 底点，
至少在一个全级点和 $-P,-Q$ 中至少一个截面处，
(14) 的双留数非零。

结合 (10)–(16)，得到本篇的准确结论：
\[
 \boxed{\quad
 \mathscr C_2(\Omega_p)\text{ 在至少 }
       \frac{p-1}{2}-6
 \text{ 个不同的 Hasse 底点上有真对数极点。}
 \quad}
 \tag{24}
\]
当右端为负时只取零下界；对惰性 $p\ge19$ 已给非空的移动支撑。
若数全级点，则至少有
$d((p-1)/2-6)$ 个非例外点。
(24) 的零数计算只使用每个 cusp 底点上
$\sum e_c=d$；只有 (22) 的非零首项用到指定 cusp 的 $e=34$。

这里的“真极点”不能仅靠加一个 rational exact 二形式去掉：
在横截局部参数的 Laurent 展开中，
任意 $d\alpha$ 的双对数 residue 都是零。
所以 (14) 也是对这种局部 exact 改写的障碍。
这并不声称任意更大的有限秩系数系统或其他投影都必须保留这些极点。

## 8. 对下一步的实际含义

(4)–(5) 证明固定 Kummer 单位的完整 Cartier 确有固定次数控制。
(24) 则证明，在当前真实临界行中乘上 $\zeta_p^2$ 后，
不能把这个控制直接转述为“极点支撑也固定”。
极点阶从二降到一，移动极点的个数仍随 $p$ 线性增长，
而且已经在实际两挠点和真实 $m_P$ 上检测到非零对数留数。

故要从这一接口继续建立固定有限维 Frobenius 比较，
需要新的、实际配对所强迫的消去或一个能保留这些 moving-residue
数据的额外结构。本文没有以“没有这种直接消去”替代主课题结论，
也没有把模 $p$ 的二形式与最终除 $p$ 后的中央标量混为一谈。

### 已核原始来源

- N. Katz (1970), *Nilpotent connections and the monodromy theorem:
  applications of a result of Turrittin*, Publ. Math. IHÉS **39**,
  175–232，Theorem 7.2，pp.200–202。
  [作者原文](https://web.math.princeton.edu/~nmk/old/nilpconn.pdf)。
  原文的普通/对数 Cartier、乘法性及 étale 坐标证明均已核对；
  (5) 和双留数保留是其局部坐标公式的直接推论。
- A. Grothendieck 等 (1971), *Revêtements étales et groupe fondamental*
  (SGA 1)，Exposé XIII，Corollaire 2.9、§2.10、Lemma 2.11，
  以及 Proposition 5.4–5.5、Corollaire 5.6。
  已核 [SMF 重排原文](https://arxiv.org/pdf/math/0206203)
  的 pp.288–290、317–318（原版边栏 pp.389–392、431–433）。
  §7 逐项核 prime-to-$p$ 群、三条互不相交 cusp、
  相对光滑基与 Kummer 局部正规化的适用性。
- G. Everest (1999), *Explicit Local Heights*, New York J. Math. **5**,
  115–120，p.118，式 (12)–(14)。
  [正式全文](https://nyjm.albany.edu/j/1999/5-9.pdf)。
  这里只引用 Tate 曲线及其两个坐标级数；(21)–(23) 为本文直接计算。
- NIST DLMF（2026 年查阅），
  [20.2.2–20.2.3](https://dlmf.nist.gov/20.2) 的 theta 定义级数、
  [23.15.6](https://dlmf.nist.gov/23.15.E6) 的 $\lambda$ 规范、
  [23.18.1–23.18.2](https://dlmf.nist.gov/23.18) 的模变换。
  它们固定 (18)–(19) 的 cusp、nome 和符号。
- 实际全基 crystalline Frobenius 使用
  [整 GM 原证明](2026-11-12-integral-gm-frobenius-critical-row.md)
  中已核的 Stacks Project（2026 年）Tags
  [07MW](https://stacks.math.columbia.edu/tag/07MW)、
  [07MZ](https://stacks.math.columbia.edu/tag/07MZ)、
  [07N0](https://stacks.math.columbia.edu/tag/07N0)；
  §3 说明相同整比较为何适用于 $R_0^\wedge$。
- $p$-curvature 的准确常数、简单 Hasse 根及 (10)：
  [固定规范原证明](2026-11-12-legendre-p-curvature-with-fixed-normalization.md)。
  本篇在使用之前已独立通读，根端亦已复核。

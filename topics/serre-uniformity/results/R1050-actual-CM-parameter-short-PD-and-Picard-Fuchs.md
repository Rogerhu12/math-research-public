# R1050：原 CM target 参数的短 PD 比较与完整所需 Picard–Fuchs 截断

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；o1_theta / global_route / root。

**已证明：原 target fine eigenparameter 与同一椭圆族的实际 Hodge period graph，在所需首 $p$ 精度内只差一个保留的单位。** 因而原 coarse CM 参数可以由明确的超几何比值反演，确定到整个原深盘轮廓所需的阶数。本文没有将节点自身返回误作单纯坐标项，也没有把完整原 Abel-log 轮廓直接写成一个未付清的 Taylor 复合。

## 1. 原对象、精度与结论

令
$$
p=6N+5\ge41,\qquad \ell=(p+1)/3=2N+2,
\qquad k=\overline{\mathbf F}_p.
$$
保留 R1021、R1032、R1039 的同一个普通 quotient-isogeny、trace-zero $Q$ 和实际 target fine eigenparameter $u'$。在所选原 CM 标记处，coarse 坐标为 $b=1$；fine 参数取
$$
t=(b-1)^{1/3},\qquad b=1+t^3,\qquad r=1-b^3.
\tag{1050.1}
$$
这里取原辅助 fine 盖上的一个根；后文的 coarse 公式不依赖此根。$u'$ 与 $t$ 均是实际 fine 变形环的参数。$b-1$ 在二者中恰有三次零，不能把普通 $s\in S$ 处 $b-s$ 的一次坐标关系沿用到 CM 点。

定义只取所需项的原有理级数
$$
q(r)={}_2F_1\left(\frac56,\frac56;\frac43;r\right),\qquad
j(r)={}_2F_1\left(\frac12,\frac12;\frac23;r\right).
\tag{1050.2}
$$
使用它们的 $r^i$ 系数时仅取 $i<\ell$。这些系数在 $p$ 处全整，$j(0)=q(0)=1$。

在原实际 Hodge crystal 的固定特征基中，可将 period graph 归一为 $\Xi=t+O(t^4)$。存在一个原单位 $d\in k^\times$，使
$$
\boxed{\quad
\Xi=d u'\pmod{(u')^p}.
\quad}
\tag{1050.3}
$$
其所需截断准确由 (1050.2) 给出；立方后是
$$
\boxed{\quad
Z=\Xi^3
=-\frac r3\left(\frac{q(r)}{j(r)}\right)^3
\pmod{(b-1)^{\ell+1}}.
\quad}
\tag{1050.4}
$$
式 (1050.4) 按有限截断解释，不在特征 $p$ 中任意定义带坏分母的无限超几何级数。

其一次项是 $Z=b-1+O((b-1)^2)$，故有唯一反演
$$
\boxed{\quad
b=B_{\rm CM}(Z)\pmod{Z^{\ell+1}},\qquad
B_{\rm CM}(Z)=1+Z+\frac5{16}Z^2+\cdots.
\quad}
\tag{1050.5}
$$
更准确地，(1050.3) 结合实际 $\mu_3$ 角色给
$$
b=B_{\rm CM}(d^3(u')^3)\pmod{(u')^{3\ell+3}}.
\tag{1050.6}
$$
因此 $B_{\rm CM}$ 的全部 $Z^i$ 系数，$0\le i\le\ell$，由 (1050.4) 严格确定。

R1021 在实际仿射尾上给
$$
u'=\varepsilon(c_Q\psi+pR_Q),\qquad
\psi=\beta^{p-1},\qquad \varepsilon^{p+1}=p.
$$
所以同一个原尺度是
$$
\boxed{\quad
\kappa_1=d^3c_Q^3,\qquad
b_{\rm lift}
=B_{\rm CM}(\kappa_1\varepsilon^3\psi^3)
\quad\text{在原仿射尾模 }p\text{ 的所需精度内}.
\quad}
\tag{1050.7}
$$
$\kappa_1$ 正是 R1032、R1039 的实际首三次比较单位，不能把它设成一。本文也不将 $R_Q$ 在仿射尾上的正则性扩张成节点处的正则性。
在 $p\equiv5\bmod12$ 的两个 incidence 上，分别使用 R1038、R1039 的原 $c_{Q,\pm}$ 与 $\psi_\pm$；其已核的运输给同一个 $\kappa_1$，而 $\psi_\pm^3$ 在两个无穷端仍保留原相反首符号。式 (1050.7) 分别应用于这两条实际支，不省去第二个节点，也不独立重选其相位。

## 2. 同一椭圆族在 CM 点的好模型

原 Gauss–Manin 来源是
$$
E_b:y^2=x^3+3brx+r(1-2b^3),\qquad
\omega=dx/(2y),\quad r=1-b^3.
\tag{1050.8}
$$
这个 Weierstrass 标架在 $r=0$ 不是好标架。作实际坐标变换
$$
x=r^{1/3}X,\qquad y=r^{1/2}Y
$$
后得到
$$
\mathcal E_t:Y^2=X^3+3b r^{1/3}X+(1-2b^3).
\tag{1050.9}
$$
其中 $r^{1/3}=t(-3-3t^3-t^6)^{1/3}$。它是 $k[[t]]$ 上的好模型，特殊纤维为 $Y^2=X^3-1$。原变换所需的平方根可在辅助二次盖上取；其作用只是共同乘 period，下面的 ratio 下降，(1050.9) 本身已在 $k[[t]]$ 上定义。

$t$ 的一次变形只改变 $X$ 项，其导数 $3(-3)^{1/3}$ 非零，而常数项没有一次变化。因 $p>3$，这是 j-zero 点的实际 fine 椭圆变形参数，Kodaira–Spencer 为单位。也可先取原点值一的六次单位根将常数项归一为 $-1$，得到同一个结论。

这个模型与原带辅助标记的 target 椭圆变形来自同一 fine moduli 盘；Serre–Tate 等价所给的是它的实际 $p$-divisible group，而非另选的抽象同高度形式群。

## 3. 短 PD 理想及实际 Fil graph

在
$$
S=k[[t]]/(t^p),\qquad I=(t)
\tag{1050.10}
$$
上使用
$$
\gamma_n(x)=
\begin{cases}
x^n/n!,&0\le n<p,\\
0,&n\ge p.
\end{cases}
\tag{1050.11}
$$
这是一个真正的 nilpotent PD 结构：小于 $p$ 的阶乘可逆，而在加法、乘法和复合公理中越过 $p$ 的项总次数至少 $p$，由 $I^p=0$ 消失。它与基环的 canonical PD 相容。任何保持 $I$ 的 $k$-代数自同构都保持这一个 PD 结构。

令 $G_0=\mathcal E_0[p^\infty]$，$M=\mathbb D(G_0)(W(k))$。使用与 R1035 相同的实际协变 Dieudonné crystal。合法 PD 基变换给
$$
\mathbb D(G_0)(S)=M\otimes_{W(k)}S.
\tag{1050.12}
$$
原变形 $\mathcal E_t[p^\infty]/S$ 的 Hodge 子模是一条实际 direct-summand 直线。它约化为 $M/pM$ 的原 Hodge 特征线，故在这条线附近唯一写成 graph。Zink 的对象和态射比较确保这个 graph 描述的是实际变形，并与原 framing 作用相容。

原 framing torus 是 $\mu_{p^2-1}\subset\mathbf Z_{p^2}^{\times}$ 在 $G_0$ 上的真实作用。它不必由整个椭圆曲线的全局自同构给出；此处使用的是 R1021 已固定的 special BT framing 及 Serre–Tate 变形作用。它在 $M$ 上分成两个特征线，角色相差第 $p$ 次幂。它固定特殊 Hodge 线，所以在该线附近的 graph coordinate 上按两个角色的比值作用。

采用 R1021 的 target 方向，原 $u'$ 满足
$$
g_\zeta(u')=\zeta^{p-1}u'.
\tag{1050.13}
$$
graph 的 tangent character 与实际变形切空间的角色相同，也是 $\zeta^{p-1}$。因此，在选定特征基后的原 graph coordinate $\Xi$ 满足
$$
g_\zeta(\Xi)=\zeta^{p-1}\Xi\quad\text{于 }S.
\tag{1050.14}
$$
写 $\Xi=\sum_{1\le n<p}c_n(u')^n$。因 (1050.14)，非零项必须满足
$$
(p-1)n\equiv p-1\pmod{p^2-1},\quad\text{即 }n\equiv1\pmod{p+1}.
$$
在 $1\le n<p$ 内只有 $n=1$。Kodaira–Spencer 为单位，故 $c_1=d\ne0$。这证明 (1050.3)。这里未假设实际变形为常数；固定的是 crystal 的 PD 评价，Hodge 直线仍移动。

## 4. 与原 Picard–Fuchs 比值的实际比较

R1023 (1023.19) 已直接从 (1050.8) 的代数 de Rham reduction 得到
$$
\nabla\omega=\frac{b^2}{2r}\omega+\frac1{2r}\eta,
\qquad
\nabla\eta=\frac b2\omega-\frac{b^2}{2r}\eta,
\qquad \eta=x\omega.
\tag{1050.15}
$$
相应原 period 的标量方程为
$$
h''-\frac{3b^2}{r}h'
-\frac{b(5-4b^3)}{4r^2}h=0.
\tag{1050.16}
$$
这同一个 de Rham crystal，在好模型 (1050.9) 的标架中，于短 PD 厚化 (1050.10) 上与 (1050.12) 比较。

这里的精度可以直接说明。晶体在 PD 对角线上的 Taylor 同构，确定次数 $n<p$ 的系数时只除以 $n!$；用普通 connection 写出来，就是逐次解到导数的 $t^{p-2}dt$ 系数。由此得到的固定特征基就是 §3 的实际晶体基。无需、也未声称整个普通 connection 在 $k[t]/(t^p)$ 上有一个完全水平基：顶层 $t^{p-1}dt$ 可有 $p$-curvature 障碍，本文没有使用它。

将 (1050.16) 的自变量换成 $r$，再写 $h=(1-r)^{1/3}r^\nu F(r)$，可直接得到
$$
r(1-r)F''+
\left(1+2\nu-(7/3+2\nu)r\right)F'
-(\nu+2/3)^2F=0,
\tag{1050.17}
$$
其中 $\nu=\pm1/6$。故原两个解为
$$
h_+=b r^{1/6}q(r),\qquad
h_-=b r^{-1/6}j(r).
\tag{1050.18}
$$
好模型的微分是 $r^{1/6}\omega$，所以同一两个 period 在好标架中是
$$
b r^{1/3}q(r),\qquad b j(r).
\tag{1050.19}
$$
一项在 $t=0$ 有一次零，另一项为单位。这两项分别处在原几何 $\mu_3$ 的两个特征方向；它们不能被任意互加而仍保留特征基。因而与 §3 的实际 graph 相比，只剩一个乘法常数。将线性项定为 $\Xi=t+O(t^4)$ 后，准确得到
$$
\Xi=(-1/3)^{1/3}r^{1/3}\frac{q(r)}{j(r)}
\quad\text{至次数 }p-1,
\tag{1050.20}
$$
其中根的选择使 $(-1/3)^{1/3}r^{1/3}/t$ 的原点值为一。于是立方即为 (1050.4)。本步骤比较的是同一实际 Hodge crystal 的 period graph，强于仅仅比较 Schwarzian。

## 5. 所有分母和末端精度

$j$ 的 $i$ 次系数为
$$
\frac{(1/2)_i^2}{(2/3)_i\,i!}.
$$
在 $(2/3)_i$ 中首次出现 $p$ 倍因子的位置是 $i=\ell$，因为 $2+3(\ell-1)=p$。因此本文所用的 $0\le i<\ell$ 全整。$q$ 的下参数 $(4/3)_i$ 首次出现 $p$ 倍因子的位置是 $i=2\ell-1$，亦在本范围外；所有 $i!$ 都是单位。

在 (1050.20) 中，$r^i$ 项对应 fine 次数 $1+3i$。最大所用 $i=\ell-1$ 对应 $p-1$，正好落在短 PD 已付范围内。为了得到 $Z$ 的 $r^\ell$ 系数，外面的 $r$ 表明只需 $q/j$ 到 $r^{\ell-1}$，没有越界使用 $j$ 的第一个坏分母。

取 (1050.20) 的 $t$ 次数 $<p$ 截断作为一个 $k[t]$ 多项式 $\Xi_{<p}$。它的次数均为 $1\bmod3$；实际 $u'(t)$ 在同一个几何 $\mu_3$ 下也有这个角色。由 (1050.3)，
$$
\Xi_{<p}-d u'\in(t^p).
$$
而 $p\equiv2\bmod3$，最早可能的 $1\bmod3$ 误差次数是 $p+2$，所以
$$
\Xi_{<p}-d u'=O(t^{p+2}),\qquad
\Xi_{<p}^3-d^3(u')^3=O(t^{p+4}).
\tag{1050.21}
$$
$p+4=3(\ell+1)$，故立方作为 $t^3=b-1$ 的级数，在 $\ell$ 次以内准确；这证明 (1050.6) 的末端范围。

前两项可直接纸算：
$$
q=1+25r/48+O(r^2),\qquad
j=1+3r/8+O(r^2),
$$
$$
Z=-r/3-7r^2/48+O(r^3).
$$
代 $r=-3(b-1)-3(b-1)^2-(b-1)^3$ 得
$$
Z=(b-1)-5(b-1)^2/16+O((b-1)^3),
$$
于是 (1050.5) 的 $5/16$ 和 (1050.20) 的
$$
\Xi=t-5t^4/48+O(t^7)
$$
均保原尺度。

## 6. 原尾上可使用的范围

R1021 的 $u'=\varepsilon(c_Q\psi+pR_Q)$ 是实际仿射尾的等式。将其代入 (1050.6)，对 $\varepsilon$ 次数 $<p+1$ 的全部项，$pR_Q$ 不贡献；而 (1050.6) 的余项在代入后始于 $\varepsilon^{p+4}$，也在所需范围之外。原 full CM 旗标使用 $1\le k\le\ell-1$，对应 $3k\le p-2$，所以 (1050.7) 严格覆盖这些 coarse 参数项。
在 $p\equiv5\bmod12$ 行，此代入对两条原 incidence 各自作一次，保留 $c_{Q,\pm}$、$\psi_\pm$、已识别的共同 $\kappa_1$ 以及第 $k$ 次幂的 $(\pm1)^k$ 双端首符号。

这是一条关于实际 target coordinate 的结论。原 CM 微分的更早 normal 层可能在节点有极，并经真实 Dickson 消去及 $1/\psi$ 返回中心，再返回同一尾。本文没有断言这些项为零，也没有仅凭 (1050.7) 把原完整轮廓等同于 $R_L(B_{\rm CM})$ 的 Taylor 级数。两条 $p\bmod12$ 行的图、一个或两个无穷端、精确零留数与中心反馈仍使用 R1044、R1046 已付的实际模型；未将其替换成一个抽象单尾模型。

## 来源

- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)，*Actual full-p affine tail rigidity and quotient parameter*，§§1–4：真实 framing、target eigenparameter、同一 quotient 及 $pR_Q$ 的准确仿射范围。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)，*Original CM divisor complete first log vector*，§4、(1023.19)–(1023.22)：同一原族的 de Rham 矩阵及三阶比较；本文将实际 PD 比较推进到所需首 $p$ 截断。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md) §5、[R1039](R1039-original-p5-complete-CM-normal-jet-and-rational-disc-scale.md)：同一 CM fine/coarse 三次零及原 $\kappa_1$，不换 quotient 或标记。
- [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)，*Original lowest-type integral Lie comparison by two PD thickenings*：本课题已采用的协变晶体、实际 Fil graph 和态射自然性；本文另逐项验证 (1050.10) 的短 PD 理想，不沿用一个未经验证的大分歧 PD 理想。
- Thomas Zink, *The display of a formal p-divisible group*, Astérisque 278 (2002), 127–248，[作者全文](https://www.math.uni-bielefeld.de/~zink/display.pdf)，Definition 47、(74)–(76)、Theorem 48，及 Theorem 94 / Corollary 95：晶体基变换、Hodge 子模、实际 formal BT 与对象/态射比较。对应作者 PDF 第43–44及88–89页。本轮已实读这些段落。

全文为纸面推导，没有执行数学计算、没有重算旧窗口。实际 period source 与初项经 o1_theta / global_route 相互核对；root 独立核短 PD 公理、实际 framing、Gauss–Manin 方程和末端分母精度。全 self-return 仍是后继问题，Serre 主目标仍 OPEN。

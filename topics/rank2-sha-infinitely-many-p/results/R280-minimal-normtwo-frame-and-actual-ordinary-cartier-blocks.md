# R280 — 真实范数二最小 frame、普通 Cartier 的 $18+17$ 分块及原相邻十七维图

日期：2026-11-13。**状态：以下原三源的范数二拉回、整空间同构、与 R266 旧格的准确等价、两个原十七维模的实际普通 Cartier 公式，以及 R277 新组合的完整分块与质量接口均已证明。没有增加来源维数或免费改进深度预算；主中央非零仍待证明。**

本篇使用 R266 的同一个真实测度算子
$$
T_p=b_{17}[b_0^2]_*\psi_p.
\tag{1}
$$
其 theta 迹、原整格闭合、与 $i$ 及归一二挠平移的交换都已支付。
下面给出与 R264/R265 原十七维正／相邻模直接对接的较小 frame。

## 1. 真实范数二拉回同时支付角参数与两个周期函数

令
$$
\alpha=1+i,\quad \bar\alpha=1-i,\quad
U=x^2,\quad v=U^{-1},\quad t=\sqrt{1-v}.
$$
实际加法与 sigma 公式给
$$
x(\alpha z)=-\frac{i(U-1)}{2x},\qquad
\sigma(\alpha z)^2=2ix\sigma(z)^4,\qquad
\vartheta(\alpha z)^2=(U-1)\sigma(z)^4.
\tag{2}
$$
平方根均取原点支；这些是原 theta 函数的恒等式。

设
$$
w=v(\alpha z)=-\frac{4v}{(1-v)^2}.
$$
准确有
$$
\boxed{
t(w)=\frac{1+v}{1-v},\qquad
u(\alpha z)=\frac{\alpha u}{t},\qquad
F(w)=tF(v),
}
\tag{3}
$$
以及
$$
\boxed{
\mathfrak H(w)=\frac{t^2}{2}\bigl(1-t\mathfrak H(v)\bigr).
}
\tag{4}
$$

**证明。** (2) 的 $x$ 式来自点 $P$ 与 $iP$ 的实际加法。
sigma 加法给
$\sigma(\alpha z)\sigma(\bar\alpha z)=2x\sigma^4$，
而 $\sigma(\bar\alpha z)=-i\sigma(\alpha z)$，得到第二式；
再乘 $x(\alpha z)$ 得第三式。

(3) 的前两式直接由 (2) 和原点首项得到。
比较 $\alpha z=u(\alpha z)F(w)$ 与 $z=uF(v)$，得到 $F(w)=tF(v)$。
最后对
$2\log\Theta(w)=4\log\Theta(v)+\log(1-v)$
求 $v$ 导数，使用 $\Theta'/\Theta=\mathfrak H/(4t)$，
并代入 $w'=-4(1+v)/(1-v)^3$，得到 (4)。$\square$

因此运输 R277 的 forcing 时，$F$ 和 $\mathfrak H$ 也有已经付清的真实变换；
不需只搬角多项式而留下未知周期因子。

## 2. 原三源已经在 $136$ 次的正 theta 空间中

仍用 R270 的固定 $Q_A,Q_B,Q_H$。由
$\vartheta(\alpha z)^{68}=\vartheta(z)^{136}(1-v)^{34}$，
原拉回准确为
$$
\boxed{
\begin{aligned}
S_A(\alpha z)&=\vartheta^{136}P_A(v),&
P_A(v)&=(1-v)^{34}Q_A(w),\\
S_B(\alpha z)&=\vartheta^{136}P_B(v),&
P_B(v)&=(1-v)^{34}Q_B(w),\\
S_H(\alpha z)&=\vartheta^{136}P_H(v),&
P_H(v)&=(1-v)^{33}(1+v)Q_H(w).
\end{aligned}}
\tag{5}
$$
它们都是次数至多三十四的实际多项式。
由于 $w(1/v)=w(v)$，有准确的不同二挠符号
$$
\boxed{
P_A(v)=v^{34}P_A(1/v),\quad
P_B(v)=v^{34}P_B(1/v),\quad
P_H(v)=-v^{34}P_H(1/v).
}
\tag{6}
$$
第三源的平方根被真实 $\alpha$ 拉回消去；(6) 保留了它与前两源不同的作用符号。

写
$$
\mathcal S_N=\sigma^N L(NO).
$$
在 $\mathcal S_{136}$ 中，$i$ 不变部分准确为
$$
\mathcal E=\sigma^{136}\mathcal O[U]_{\le34},\qquad \dim\mathcal E=35.
\tag{7}
$$
这是因为 $x(iz)=-x$、$y(iz)=iy$，而 $\sigma(iz)^{136}=\sigma^{136}$。
归一二挠平移 $T_0=(0,0)$ 在此部分作用为
$$
\mathcal J(f)(U)=U^{34}f(1/U).
$$
故有原整直和
$$
\boxed{
\mathcal E=\mathcal E^+\oplus\mathcal E^-,
\qquad \dim\mathcal E^+=18,\quad\dim\mathcal E^-=17.
}
\tag{8}
$$
投影 $(1\pm\mathcal J)/2$ 在奇素位整。
由 (5)–(6)，原 $A,B$ 在 $\mathcal E^+$，第三原 $H$ 在 $\mathcal E^-$。

对普通 $p$，$\alpha\in\mathbb Z_p^\times$。
实际 $\psi_p$ 与按 $\alpha$ 缩放交换，因而
$$
T_p(G(\alpha z))=(T_pG)(\alpha z).
\tag{9}
$$
R266 又给 $T_p$ 与 $i,\mathcal J$ 交换。
所以 (8) 是**真实测度 Cartier 的整稳定分块**，不是仅按角函数猜出的维数。

完整普通 Mellin 同时满足
$$
M_{G(\alpha z)}(u)=(\alpha^{p-1})^uM_G(u).
\tag{10}
$$
因此，对原质量为零的三个来源，完整中央导数零在 (5) 下保持。
这里使用的是实际单位缩放，不是来源乘法。

## 3. 它与 R266 旧 $34m+1$ 维格完全整等价

对任意 $m\ge1$，令
$$
\mathcal E_m=\sigma^{136m}\mathcal O[U]_{\le34m}.
$$
R266 的旧空间为
$$
\mathcal V_m=\Xi^m\mathcal O[t_0]_{\le34m},\qquad
\Xi=\sigma^{272}(U+1)^{68},
\quad t_0=\frac{U^2-6U+1}{(U+1)^2}.
$$
真实 $\bar\alpha$ 拉回给同构
$$
\boxed{
[\bar\alpha]^*:\mathcal E_m\xrightarrow{\ \sim\ }\mathcal V_m.
}
\tag{11}
$$
若输入为 $\sigma^{136m}P(U)$，在右侧 $\Xi^m$ frame 下，它准确成为
$$
\boxed{
2^{-34m}(1-t_0)^{34m}
 P\!\left(-\frac{1+t_0}{1-t_0}\right).
}
\tag{12}
$$

**证明。** (2) 的共轭式给
$$
\sigma(\bar\alpha z)^{136m}
=2^{68m}\sigma^{272m}U^{34m},\qquad
U(\bar\alpha z)=-\frac{(U-1)^2}{4U}.
$$
设 $q=U/(U+1)^2=(1-t_0)/8$，
则 $U(\bar\alpha z)=-(1+t_0)/(1-t_0)$；
除以 $\Xi^m$ 得到 (12)。
这是齐次三十四 $m$ 次多项式上的二元线性变量变换，
其底层 $2\times2$ 矩阵行列式为 $\pm2$。
因此在 $\mathbb Z[i,1/2]$ 上连同逆变换都整，证明 (11)。$\square$

在 (12) 中，原 $\mathcal J$ 的作用准确变成
$$
t_0\longmapsto-t_0.
\tag{13}
$$
所以 R266 旧空间中的这个角反射，现在有了完整的真实 theta 作用与
$T_p$ 交换证明。$m=1$ 的偶／奇部分恰为 (8) 的 $18/17$ 两块。

(11) 不增加 Hilbert 主阶、深 Smith 数或新中央约束；
它只是把同一个原整格与原十七维连接放在更直接的共同坐标里。

## 4. R264 的两个原十七维模准确就是实际块

记 R264/R265 的正、相邻来源
$$
W=-y\vartheta\sigma^{67}
=\vartheta^{68}t\,v^{16},
$$
$$
\mathcal H_+=W\,\mathcal O[U]_{\le16},\qquad
\mathcal H_-=(W/x)\,\mathcal O[U]_{\le16}.
\tag{14}
$$
它们在特征零具有相同的原 charge；相邻模保留 $1/x$ 和不同的 $i$ 型。

**定理 1。** 实际 $\alpha$ 拉回给整同构
$$
\boxed{
\Phi_+:\mathcal H_+\xrightarrow{\sim}
 \mathcal S_{136}^{\,i=+1,\mathcal J=-1},
}
\tag{15}
$$
$$
\boxed{
\Phi_-:\mathcal H_-\xrightarrow{\sim}
 \mathcal S_{136}^{\,i=-1,\mathcal J=-1}.
}
\tag{16}
$$
两边各为十七维。具体地，对 $\deg Q\le16$，
$$
\boxed{
\begin{aligned}
\Phi_+(WQ)
&=2^{32}\sigma^{136}U^{16}(U^2-1)
 Q\!\left(-\frac{(U-1)^2}{4U}\right),\\
\Phi_-((W/x)Q)
&=2^{33}i\,\sigma^{136}xU^{16}(U+1)
 Q\!\left(-\frac{(U-1)^2}{4U}\right).
\end{aligned}}
\tag{17}
$$
这些公式只有二的幂分母，全部奇素位保持原 primitive 格。

**证明。** 第一式由 (3)、(14) 逐项代入；
第二式再乘 $1/x(\alpha z)=2ix/(U-1)$。

$\mathcal S_{136}$ 的 $i=-1$ 部分为
$\sigma^{136}x\mathcal O[U]_{\le33}$。
归一二挠作用在其多项式上为 $P(U)\mapsto-U^{33}P(1/U)$，
因此 $\mathcal J=-1$ 部分恰为 $P$ 的三十三次 palindromic 条件，维数十七。
(17) 的两式分别满足所列符号。

反过来，三十四次 anti-palindromic 多项式唯一写为
$$
(U^2-1)U^{16}R(U+U^{-1}),\qquad \deg R\le16;
$$
三十三次 palindromic 多项式唯一写为
$$
(U+1)U^{16}R(U+U^{-1}),\qquad \deg R\le16.
$$
因为 $(U-1)^2/U=U+U^{-1}-2$，这与 (17) 只差仿射变量
$U+U^{-1}=2-4s$ 及二的幂单位。
上述表示在 $\mathbb Z$ 的逐次首项三角基中也整，
所以 (17) 是所述整同构。$\square$

由 (9)、R266 的实际正 theta 闭合及符号交换，得到
$$
\boxed{
T_p\mathcal H_\pm(\mathcal O)\subset\mathcal H_\pm(\mathcal O)
}
\tag{18}
$$
对全部普通允许素位成立。这把原十七维模的普通有限闭合与原测度直接接上，
没有把 R264 的裸 de Rham Cartier 冒充原算子。

## 5. 两个实际 Cartier 矩阵有不同的首对角

为把 (18) 写成可直接计算的公式，令
$$
r_{\bar\pi}(z)=\frac{\sigma(\bar\pi z)}{\sigma(z)^p}
=B(U),\quad \deg B=r,\quad B^*(U)=U^rB(1/U).
$$
$\bar\pi=b_0$ 采用原 CM 规范，故 $B(0)=1$，最高系数 $b_0$；
这里的 $B$ 是**普通 $p$ 的实际 division 多项式**，不是固定 $K_\beta$。
准确有
$$
x(\bar\pi z)=x(B^*/B)^2,\qquad
U(\bar\pi z)=U(B^*/B)^4.
\tag{19}
$$

对 $\sigma^{136}P(U)$ 定义
$$
H_+(U)=B(U)^{136}P\!\left(U(B^*/B)^4\right);
$$
对 $\sigma^{136}xP(U)$ 定义
$$
H_-(U)=B(U)^{134}B^*(U)^2
 P\!\left(U(B^*/B)^4\right).
\tag{20}
$$
它们均为真正的整多项式，负幂已被原有限次数界支付。
原 Cartier 公式是
$$
\boxed{
T_p(\sigma^{136}P)\equiv
\frac{b_{17}}{b_0}\sigma^{136}
 \sum_{j=0}^{34}
 [U^{jp+r}](U-1)^{2r}H_+(U)\;U^j
\pmod p,
}
\tag{21}
$$
$$
\boxed{
T_p(\sigma^{136}xP)\equiv
\frac{b_{17}}{b_0}\sigma^{136}x
 \sum_{j=0}^{33}
 [U^{jp+3r}](U-1)^{2r}H_-(U)\;U^j
\pmod p.
}
\tag{22}
$$
如系数不在所选 $\mathbb F_p$，求系数后照常施加逆 Frobenius；
原 Gaussian 系数在普通素位的剩余域中由原嵌入读取。

**证明。** R266 已证明完整权的归一公式
$$
\left(\frac{\mathcal C(\sigma^{136}f\,dz)}{dz}\right)\circ[\bar\pi]
=\sigma^{136}\frac{\mathcal C(r_{\bar\pi}^{136}(f\circ[\bar\pi])\,dz)}{dz}.
$$
若写成未归一的一形式拉回，两边须同时保留 $\bar\pi$ 的微分因子；
这里已经准确除以它。
再乘原 $b_{17}/b_0$ 规范，得到 $T_p$ 的模 $p$ 表达。
对 $E_0$，
$y^{p-1}=(x^3-x)^{2r}=x^{2r}(U-1)^{2r}$。
偶 $x$ 幂的 Cartier 抽取条件给 $U$ 指数 $jp+r$；
多一个 $x$ 时，条件准确变成 $jp+3r$。
这证明 (21)–(22)，并保留了相邻模不同的 tame 型。$\square$

把 (21)、(22) 限制到 (15)、(16)，再使用 (17) 的原整逆，
便得到两个真正的 $17\times17$ 模 $p$ 矩阵。
它们是 (18) 的特征零原矩阵的约化，而不是另外构造的检测器。
特别地，普通裸 $\mathcal C(x\,dz)=0$ 并不会令 (22) 消失：
实际 $H_-$ 和其全部 division 权仍在。

也不能把相邻模的 principal Mellin 当作正权中央行。
其 $i=-1$ 对称性会使未移权 principal 行为零；
实际 Stokes 运输必须保留相应的二次角因子和移权，
正如 R245/R265 的完整转置所要求。

## 6. R277 新组合在这张整图中的实际位置

沿用 R277 的
$$
\kappa=\frac{32869400496960896}{60295968781641855},\quad
K_*=B_+(v)-\kappa tR_H(v),\quad
Y=\vartheta^{68}.
$$
其两个有限 theta 分量是
$$
G_{\mathrm e}=YB_+(v),\qquad
G_{\mathrm o}=YtR_H(v).
\tag{23}
$$
在真实 $\alpha$ 拉回后，前者在 $\mathcal E^+$，后者在
$\mathcal E^-=\Phi_+(\mathcal H_+)$。
具体地
$$
G_{\mathrm o}=WP_R(U),\qquad
P_R(U)=U^{16}R_H(1/U)\in\mathbb Q[U]_{\le16}.
\tag{24}
$$
这给出原正十七维连接中一个完全明确的实际输入。

它的原点系数与 R264 的原余核为
$$
\boxed{
P_{R,16}=\frac{3410630213}{44924880},\qquad
\ell(P_R)=-\frac{23433376750893848}{4679675}.
}
\tag{25}
$$
(25) 由 R277 证书的十七个 $R_H$ 系数与 R264 已列出的整数 $\ell$ 向量
逐项作反序点积得到；没有省略其非零质量。
前一偶分量的质量为
$$
G_{\mathrm e}(0)=\frac{186757957369096}{4512611027925}
=\kappa P_{R,16},
$$
故
$$
YK_*=G_{\mathrm e}-\kappa G_{\mathrm o}
$$
的原点常数准确相消。
原角原函数仍是 $\mathcal Z_*=tK_*$；两者都从 $v^2$ 起。
这不把“常数项零”扩大为完整单位测度质量零。

在固定 $\beta$ theta frame 中，$B_+$ 为十五次，所以其商严格 proper。
$R_H$ 的最高系数为 $-1/935$，于是
$$
\boxed{
\frac{K_*}{K_\beta^4}
=\frac{\kappa}{935\beta^4}t+\text{完整四层 proper 部分}.
}
\tag{26}
$$
原来源 $S_A+S_B+\kappa S_H$ 的对应多项式部分是
$-\kappa t/(55\beta^4)$；两者准确相差 $-1/17$。
这只是原十七次角积分的已付首项，不能删除这个剩余奇方向。

若把 (18) 的正块矩阵记为 $\mathsf T_{p,+}$，以 $Q_{16}$ 为原质量行，
R266 的真正单位质量公式在此为
$$
\boxed{
M_{WQ}(0)=Q_{16}
 -b_{17}^{-1}e_{16}^{\,T}\mathsf T_{p,+}Q.
}
\tag{27}
$$
因此 (25) 给出的输入质量和其 $p$-core 修正都有明确位置；
没有凭 $\ell(P_R)\ne0$ 或 $P_{R,16}\ne0$ 宣称原中央导数非零。
偶块有同样的十八维真实质量行，比较 $G_{\mathrm e}$ 与
$\kappa G_{\mathrm o}$ 必须同时保留两个 core 项。

本篇把 R277 消分歧极后的 forcing 接到了真实 $18+17$ 格和
R264/R278 的原十七维域；所需下一步是对这些具体输入的完整连接／移权聚合，
而不是再次证明抽象有限空间存在。


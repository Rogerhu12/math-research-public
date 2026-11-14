# R259 — norm-two 补极、导子十七处的真秩一迹与完整对数运输

日期：2026-11-13。**状态：下述补极、真实 CM2 迹、全部相邻权投影、导子十七处的秩一结构及完整 $\Phi,\Phi',\Phi''$ 运输均已证明。基本 CM2 行确有非零 E34 分量；其实际 $\beta$ 拉回再共轭十七次迹后，常数行只剩 CM 方向，原 primitive 投影为零。主问题未完成。**

本篇接续 [R251](R251-adjacent-companion-lambda2-and-log-free-central-loop.md)、
[R253](R253-four-octic-ray-logarithms-and-norm2-constants.md) 和
[R254](R254-octic-ray-original-companions-and-full-fourth-order-transport.md)。
原 $\Phi_k$ 及其非零常数 $C_k$ 始终使用 R253 的实际对象。

## 1. 两个实际 frame 和准确的极补偿

置
$$
\alpha=1+i,\qquad \beta=4-i,\qquad
S=S_8=-y\vartheta\sigma^3,\qquad F=S^{17},
$$
并仍取 $E_0:y^2=x^3-x$、$dz=dx/(2y)$、$U=x^2$。
原 CM2 恒等式为
$$
\sigma(\alpha z)=\alpha\sigma(z)\vartheta(z),\qquad
\vartheta(\alpha z)=-y(z)\sigma(z)^3/\vartheta(z).
$$
两式由原除子、自动因子及原点首项分别确定；再用
$y(\alpha z)=-iy(z)(U+1)/(2\alpha x^2)$，逐项代入得到
$$
S(\alpha z)=(1+x(z)^{-2})S(z)^2.
$$
因此下面两个次数为 $136$ 的真实 frame 有明确比值：
$$
G=F^2,\qquad H=F(\alpha z),\qquad
R=H/G=(1+x^{-2})^{17}.                                   \tag{1}
$$
两者的线丛相同，但连接不同，不能把 $H/G$ 当常数。

用 $x'=2y$、$y'=3x^2-1$ 直接计算，
$$
q_1:=\frac{R'}R=-\frac{68y}{x(U+1)},\qquad
q_2:=\frac{R''}R=
\frac{68(3U^2+62U-69)}{x(U+1)^2}.                        \tag{2}
$$
在 $T_0=(1+i)\Omega_0/2$ 的局部坐标 $h=z-T_0$ 中，
$x=-h^2+O(h^6)$，而 $H$ 非零。于是 $G R''=Hq_2$ 确有
$4692H(T_0)/h^2$ 的极项。
加入原系数 $4692H/x$ 后，准确得到
$$
\boxed{
C_{\rm n}:=G R''+\frac{4692H}{x}
=544H\,\frac{x(9U+25)}{(U+1)^2}.
}                                                               \tag{3}
$$
这个来源全局全纯。其余分母在 $x=\pm i$，但这些点在 $\alpha$
下落到 $T_\pm$，$H$ 的十七阶零足以支付双极点；
在 $T_0$ 则已由 (3) 明确消极。在原点
$$
C_{\rm n}(z)=4896z^2+O(z^6).                             \tag{4}
$$

## 2. CM2 迹的完整线丛规范

$F$ 的原整周期半特征是
$(-1)^{m+n}$，$\omega=(m+ni)\Omega_0$。
因为 $\alpha T_0=i\Omega_0$，次数 $136$ 的标准 Mumford lift 满足
$$
\mathcal T_{T_0}^{136}H=-H.
$$
所以 $H=[\alpha]^*F$ 的 canonical deck lift 是
$-\mathcal T_{T_0}^{136}$，不是正号的标准平移。
对任意原 meromorphic 函数 $h$，实际有限平坦迹的投影公式为
$$
\boxed{
[\alpha]_*(Hh)=F(w)\bigl(h(z)+h(z+T_0)\bigr),
\qquad w=\alpha z.
}                                                               \tag{5}
$$
该式已经包含完整 Gaussian 和半特征：
其拉回是 $(1-\mathcal T_{T_0}^{136})(Hh)$。
特别 $[\alpha]_*H=2F$，没有额外的 $1/2$。

令目标坐标 $X=x(w)$，则原加法公式给
$$
x(z+T_0)=-1/x(z),\qquad
X=-\frac{i(U-1)}{2x}.
$$
将 (3) 的完整有理因子在二点纤维上相加，得到
$$
\boxed{
[\alpha]_*C_{\rm n}
=4352i\,F(w)\frac{X}{X^2-1}.
}                                                               \tag{6}
$$
从此在目标重新写 $x=x(w),U=x^2$。使用 R251 的
$W=-y\vartheta\sigma^{67}$、$F=WU^8(U-1)^8$，(6) 正是
$$
[\alpha]_*C_{\rm n}=4352i\,\frac W x P_{\rm n}(U),
\qquad P_{\rm n}=U^9(U-1)^7.                             \tag{7}
$$

## 3. 基本相邻权行的全部实际投影

令 $N$ 为 R251 的真实 CM5 矩阵除以 $2+i$，作用于
$(W/x)\mathbf Q(i)[U]_{\le16}$。
记该篇首项 $z^2=1$ 的三个实际相邻权来源为 $H_1^-,H_2^-,H_3^-$，
特征值分别 $i,-1,-i$。对 (7) 中未乘 $4352i$ 的基本来源，
准确分量如下：

| 实际来源 | 系数 |
|---|---:|
| $H_1^-$ | $38789/2^{22}$ |
| $H_2^-$ | $5377525/2^{26}$ |
| $H_3^-$ | $688441/2^{25}$ |
| $S(\beta z)/x(\beta z)$ | $(314359+214386i)/2^{27}$ |
| $S(\bar\beta z)/x(\bar\beta z)$ | $(314359-214386i)/2^{27}$ |

其余十二个实际角色分量和各自的 $z^2$ 系数均在证书中完整列出；
十二个系数全部非零，没有把它们当成新的椭圆曲线来源。
连同上表，证书给出整个十七维分解。

特别，R251 的真实运输
$Q_{+,w}H_2^-(2z)=128i\kappa_4 B(2z)/5$ 给出
$$
\boxed{
Q_{+,w}\bigl((E_2^-[\alpha]_*C_{\rm n})(2z)\bigr)
=-\frac{18283585}{2048}\kappa_4 B(2z),
\qquad \kappa_4=2^{-1/4}.
}                                                               \tag{8}
$$
这里 $E_2^-=(1/16)\sum_{j=0}^{15}(-1)^jN^j$。
所以基本来源确有非零的原 E34 分量。
它还不是原十七处对数来源产生的高次常数项；后者必须经过下节的
另一个实际 correspondence。

## 4. 导子十七处的真实迹不是可逆的 norm-five 算子

设
$$
\mathcal C_{17}=[\bar\beta]_*[\beta]^*
$$
作用于次数 $68$、twist-$T_0$ 的原 theta 截面。
两个拉回具有同一次数 $1156=4\cdot17^2$ 的自动因子，
使用 R248 的同一实际同构。

**结构定理。** $\mathcal C_{17}$ 的完整像包含于
$$
\boxed{
[\beta]^*\left\langle
S,\quad S/x,\quad Sx/y,\quad S/y
\right\rangle.
}                                                               \tag{9}
$$
因此在全次数 $68$ 空间中秩至多四，在每个全局 $i$ 特征空间中
秩至多一。四个基的 $i$ 特征依次是 $1,-1,i,-i$。

证明保留原 lift 相位。取 $T\in E_0[\beta]$，写
$\beta T=\gamma=(m+ni)\Omega_0$。在源次数 $1156$ 上，
$$
\mathcal T_T^{1156}([\beta]^*f)
=(-1)^{m+n}[\beta]^*f.                                   \tag{10}
$$
这通常不是特征 $+1$。
与 $E_0[\bar\beta]$ 的 canonical deck lifts 交换是合法的：
两个群都在 $E_0[17]$ 内，次数 $1156$ 被 $17^2$ 整除，
其 theta 群交换子恰为一。
把 (10) 经实际迹传到输出，在 $\bar\beta T$ 上得到同一特征。

另一方面，对次数四的任一 $s$，
$$
[\bar\beta]^*[\beta]^*s=[17]^*s.
$$
其在 $\mathcal T_T^{1156}$ 下的特征为
$\chi_4(17T)=\chi_4(\bar\beta\gamma)$。
因为 $\bar\beta\equiv i\pmod2$，这准确等于
$(-1)^{m+n}$。所以候选像 $[\beta]^*s$ 与真实输出使用同一
kernel 特征，而非只具有相同维数。

用非零参考 $S(\beta z)$ 除输出，所得 meromorphic 函数对整个
$E_0[\beta]$ 不变，因而下降为 $h(\beta z)$。
由于 $[\beta]$ 是非分歧映射，输出全纯等价于 $Sh$ 在次数四
线丛上全纯。这证明输出恰落在 (9) 所述空间内。

最后，
$$
\operatorname{div}S=2(T_0)+(T_+)+(T_-).
$$
由 $x,y$ 的实际零极阶，(9) 中四个基本截面都全纯；
它们的四个不同 $i$ 特征使其线性独立。次数四线丛的全纯截面
维数为四，故它们给出完整基。这也证明各特征像的准确上界。

## 5. 相邻行的高次像只剩一个 CM 方向

在正权 $(WP(U))$ 与相邻权 $((W/x)P(U))$ 两个十七维空间中，
精确证书分别给出 (9) 的完整秩一算子：
$$
\mathcal C_{17}^{+}=P_\beta\otimes\ell_+,\qquad
\mathcal C_{17}^{-}=(D_\beta K_\beta^2)\otimes\ell_-.
                                                               \tag{11}
$$
$P_\beta,D_\beta,K_\beta$ 都是 R248 的原 CM division 多项式。
两条线性泛函 $\ell_\pm$ 的全部十七项系数在证书中列出。
其计算使用真实十七次纤维
$$
UQ_{\bar\beta}(U)^4-tK_{\bar\beta}(U)^4=0.
$$
在相邻型中保留必要的
$x(\bar\beta z)/x(\beta z)$ frame 因子。
结构定理使一个非零纤维足以确定各条泛函；证书另在第二个准确纤维
同时核对所有十七个输入坐标。
两型都非零，且其唯一非零特征值准确为
$$
\ell_+(P_\beta)=\ell_-(D_\beta K_\beta^2)=-1+4i.
                                                               \tag{12}
$$

对本篇的基本来源，具体得到
$$
\boxed{
\mathcal C_{17}\left(F\frac{x}{U-1}\right)
=\frac{521525-325189i}{2^{24}}\,
                  \frac{S(\beta z)}{x(\beta z)}.
}                                                               \tag{13}
$$
证书以 (11) 的完整泛函回乘 $P_{\rm n}$，输出的全部十七个坐标
与 (13) 相等；所用全部输入坐标已由第二个纤维核验。

右端属于 $N=1$ 的真实 CM 线。因此
$$
\boxed{
E_2^-\mathcal C_{17}\left(F\frac{x}{U-1}\right)=0.
}                                                               \tag{14}
$$
R254 在相邻全局 $i=-1$ 空间的原 $\Pi_v$ 是
$(1-N^4+N^8-N^{12})/4$，它也准确杀掉 (13)。
所以高次常数行在原四个八次伴随上的投影同样为零。
这和 (8) 同时成立：中间确实插入了一个非可逆的、导子整除次数的
实际 correspondence。

为供正权的配对计算使用，同一 $\ell_+$ 还给出
$$
\begin{aligned}
\mathcal C_{17}\left(F\left[-4488-\frac{4352}{U-1}\right]\right)
&=\left(-\frac{584661059}{131072}
+       \frac{2075649i}{262144}\right)S(\beta z),\\
\mathcal C_{17}\left(F\left[4896-\frac{4352}{U-1}\right]\right)
&=\left(\frac{319380173}{65536}
-       \frac{59007i}{4096}\right)S(\beta z).
\end{aligned}                                                   \tag{15}
$$
没有为这些正权行重新选择十七处角色或归一。

## 6. 保留原对数的完整 norm-two 一阶、二阶式

先在基础尺度写出全部项。取 R253 的任一八次角色，
$$
\Psi(z+T_0)=-\Psi(z),\qquad C=\Psi(0)\ne0,\qquad
\Phi=\Psi-C.
$$
所以
$$
\Phi(z+T_0)=-\Phi(z)-2C,\quad
\Phi'(z+T_0)=-\Phi'(z),\quad
\Phi''(z+T_0)=-\Phi''(z).                                \tag{16}
$$
令 $\nabla_G=\partial-G'/G$。
由 $\nabla_G(H\Phi)=H(\Phi'+q_1\Phi)$，准确有
$$
\nabla_G^2(H\Phi)
=H\bigl(\Phi''+2q_1\Phi'+q_2\Phi\bigr).                  \tag{17}
$$
这一步没有混同 $G$、$H$ 两个连接。

用 (5)、(16) 作实际迹。写 $w=\alpha z$，
$X=x(w),Y=y(w),V=X^2$，并定义真正下降的对数来源
$$
\Upsilon(w)=\frac{y(z)}{x(z)}\Psi(z).
                                                               \tag{18}
$$
其下降合法，因为两个因子在 $T_0$ 下都反号。
直接计算给
$$
[\alpha]_*(H\Phi)=-2CF,
$$
$$
\boxed{
[\alpha]_*(\nabla_G(H\Phi))
=-68F\Upsilon-68\alpha C F\frac{YX}{V-1}.
}                                                               \tag{19}
$$

二阶补极式的非恒定部分也有一个明确的一阶表达。
由 (2)–(3)，
$$
q(z)-q(z+T_0)=\frac{18496x}{U+1},\qquad
q_1(z)-q_1(z+T_0)=-68\,\frac yx,
$$
其中 $q=C_{\rm n}/H=q_2+4692/x$。
设 $B_0=y/x$，则 $B_0'=(U+1)/x$。
结合实际 CM2 坐标变换，得到
$$
\frac{18496x}{U+1}\Psi-136\frac yx\Psi'
=-136\alpha\left(\Upsilon'
                    +\frac{35-X^2}{Y}\Upsilon\right).
                                                               \tag{20}
$$
右端还有原非恒定对数，未被替换成 $C$。

这一连接系数有准确的代数 gauge：
$$
M=\frac{y^{17}}{x^{26}},\qquad
\frac{M'}M=\frac{35-x^2}{y},\qquad
\mathcal A:=F/M=-\frac{\vartheta^{69}}{\sigma}.
                                                               \tag{21}
$$
$\mathcal A$ 在 $O$ 有一个简单极，在 $T_0$ 有六十九阶零。
于是 (20) 给出完整公式
$$
\boxed{
[\alpha]_*\left(\nabla_G^2(H\Phi)
                     +\frac{4692H\Phi}{x}\right)
=-136\alpha\,\nabla_{\mathcal A}(F\Upsilon)
-4352i\,C F\frac{x}{U-1}.
}                                                               \tag{22}
$$
(22) 同时保留了 $\Phi$、$\Phi'$、$\Phi''$ 的全部贡献和极补偿。

## 7. 真正接到原十七处来源的 $\beta$ 拉回

R254 使用的来源是 $F(\beta z)\Phi(z)$。
裸 $F(\alpha z)\Phi(z)$ 在原十七平移的对数点没有同样的零阶，
所以不能用基础 (22) 直接替代它。
正确置
$$
F_\beta(w)=F(\beta w),\quad
G_\beta(z)=F(\beta z)^2,\quad
H_\beta(z)=F(\alpha\beta z),\quad
\mathcal A_\beta(w)=\mathcal A(\beta w).
$$
定义实际下降来源
$$
\Upsilon_\beta(\alpha z)
=\frac{y(\beta z)}{x(\beta z)}\Psi(z).                    \tag{23}
$$
因为 $\beta T_0=T_0$，(16) 和反号仍准确成立。
导数的每个链式因子保留后，三条完整迹是
$$
L_0:=[\alpha]_*(H_\beta\Phi)=-2CF_\beta,
$$
$$
\boxed{
L_1:=[\alpha]_*(\nabla_{G_\beta}(H_\beta\Phi))
=-68\beta F_\beta\Upsilon_\beta
-68\alpha\beta C F_\beta\frac{YX}{V-1},
}                                                               \tag{24}
$$
其中现在 $X=x(\beta w),Y=y(\beta w),V=X^2$，以及
$$
\boxed{
\begin{aligned}
L_{2,\rm reg}
&:=[\alpha]_*\left(
\nabla_{G_\beta}^2(H_\beta\Phi)
+\frac{4692\beta^2H_\beta\Phi}{x(\beta z)}\right)\\
&=-136\alpha\beta\,
      \nabla_{\mathcal A_\beta}(F_\beta\Upsilon_\beta)
-4352i\beta^2 C F_\beta\frac{X}{V-1}.
\end{aligned}
}                                                               \tag{25}
$$
尤其两个 $\beta$ 因子和 $4692$ 项都没有消失。

最后一个常数来源正是
$4352i\beta^2[\beta]^*(Fx/(U-1))$。
因此再接 R254 的真实 $[\bar\beta]_*$ 时，必须使用 (13)，得到
$$
4352i\beta^2\mathcal C_{17}\left(F\frac{x}{U-1}\right)
=\gamma\,\frac{S(\beta z)}{x(\beta z)},
\qquad
\gamma=\frac{153850595+88763171i}{65536}.
                                                               \tag{26}
$$
随后 (14) 使它的原 E34 primitive 行为零；
R254 的四条八次 primitive 行也为零。
这是原来源上的准确消去，不是预设非零常数没有用处。

若不作 primitive 投影，实际 CM 行仍可保留。
R251、R250 的原相位给
$$
Q_{+,w}\left(\frac{S(2\beta z)}{x(2\beta z)}\right)
=-2\kappa_4F_0(2\beta z).
$$
所以在 R54 的完整中央函数中，(25) 的常数项贡献准确为
$$
2\kappa_4\gamma\,C\,q_2^uU_{\beta,p}^{\,u}J_0(u),
\quad
q_2=2^{p-1},\quad U_{\beta,p}=\beta^{p+1}/17.
                                                               \tag{27}
$$
求导必须保留 $J_0'$ 及 $\log_pU_{\beta,p}$；没有把 $C$ 与这些量的
乘积当成新的对数线性型。

## 8. 完整非恒定剩余行与下一种实际插入

(25) 的第一项不是未知的自由常数，而是已经指定的
$\Upsilon_\beta$ 及 meromorphic frame
$-\vartheta(\beta w)^{69}/\sigma(\beta w)$ 的一阶协变导数。
将它接 R254 的实际有限 trace、dyadic 和 norm-five 投影时，
可逐分支使用
$$
T_\nu\nabla_{\mathcal A_\beta}f
=r_\nu^{-1}\left(
\nabla_{\Theta}T_\nu f
-a_\nu T_\nu f\right),
\qquad
a_\nu=\partial_z\log\frac{T_\nu\mathcal A_\beta}{\Theta}.
                                                               \tag{28}
$$
$r_\nu$ 是该真实分支的斜率，所有 $a_\nu$ 和原极项必须保留。
这里还可明确写出一阶完整中央转置。取
$\mathcal O=Q_{+,w}E_2^-[\bar\beta]_*$ 并在输出作 $[2]$，
令 $f=F_\beta\Upsilon_\beta$、$\Theta=\vartheta(4z)^{17}$。
按原有限分支定义
$$
\widetilde f=\sum_\nu c_\nu r_\nu^{-1}T_\nu f,\qquad
\mathscr E=-\sum_\nu c_\nu r_\nu^{-1}a_\nu T_\nu f.
$$
于是 $\mathcal O(\nabla_{\mathcal A_\beta}f)
=\nabla_\Theta\widetilde f+\mathscr E$。
这里 $f$ 的极点只在 $E_0[\beta]$；原 $Q_{+,w}$ 分支具有非零的
十六原二处平移，奇 CM5 不改变该二处阶数。因此没有分支把这些极点
送到原点。$\widetilde f$ 的全局 $i$ 特征为 $i$，所以
$g=\widetilde f/z$ 在原点正则且 $i$ 不变。

置 $c=272c_0,d=p+1$，
$W_0=z\Theta'/\Theta-dcz^d$，
$f_M=J_c(g)$、$g_M=J_c(W_0g)$。用原准确规则
$J_c(Eg)=duJ_c(g)$、
$J_c(z^dg)=uJ_c(g;u-1)/c$，得到
$$
\boxed{
J_c(\mathcal O\nabla_{\mathcal A_\beta}f;u)
=(du+1)f_M(u)-duf_M(u-1)-g_M(u)+J_c(\mathscr E;u).
}                                                               \tag{29}
$$
因而其中央导数是
$$
f_M'(0)+df_M(0)-df_M(-1)-g_M'(0)+J_c(\mathscr E)'(0).
                                                               \tag{30}
$$
所有对数常数、连接项及实际移权都保留。
这些是固定 prime-to-$p$ 分支；原极点与二处平移在好约化后仍分离，
所以按 R254 同一半径估计支付固定阶导数和对数成本即可。
$E_2^-$ 在含对数空间上只表示其固定有限算子公式，不无证延长有限
全纯空间上的幂等性。式 (29) 不声称 Mellin 泛函与任何原算子交换。

本次结论清楚地区分两种已计算的行为：(8) 的基本相邻行非零，
而 (26) 的实际高次常数行在 primitive 部分准确为零。
要改变后者，插入必须破坏其纯 $[\beta]^*$ 来源；
仅把 (8) 的非零系数重复用于高次迹不能做到这一点。
原非恒定剩余、完整常数 CM 行 (27) 及其参考归一都保留在
(24)–(28)，可继续与新的实际乘子比较。

## 精确证书

[脚本](../scripts/check-normtwo-compensation-and-conductor17-trace.py) 与
[输出](../scripts/check-normtwo-compensation-and-conductor17-trace.json)
包含 (2)–(8) 的全部有理恒等式、十六个完整相邻权投影及质量、
(11) 的两条完整十七项秩一泛函、(13)、(15) 的准确标量。
第二个固定纤维同时检验两型的所有输入坐标。
所用结构、线丛及真实 lift 的证明在 §4；没有用 norm-five
的可逆性推导导子十七处的行为。


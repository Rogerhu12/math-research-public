# R334：原中央参数的单秩提升作用与固定 Miller 单位进位

日期：2026-11-13。**状态：以下均已证明。R331 扩展后的实际首提升类对高轴、原中央首参数及真实下一位的依赖均已明确；原完整中央失败的第二个必要聚合式保留两项。实际 theta 首 carry 给出统一调和数公式，并化成原固定 genus-two 双覆盖上的明确单位。没有把该单位对数或某个单独中央权视为原完整中央非零。**

## 1. 已付原来源与提升商

固定 R331 的 $p=6s-1>7,p\ne17$、$s>13$、
$1\le\ell<s-13$，$L=2s+\ell$，以及同一原目标
$$\Gamma_L=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2).$$
沿用 $b=17,t=-b/x^3,a=t(t-1)h_7,h_7=16t^2+4t+7$，
$$g=e^{-\kappa w^s}\rho,\qquad a_p=p\kappa\in\mathcal O^\times.$$
原 primitive 来源为 R331 的
$$\mathcal F_D=G_0\mathcal N_{\le D}\oplus\mathcal O K_0
\oplus\mathcal O K_1\oplus\mathcal O K_2,\qquad D\ge3.$$
除去已经支付的共同 $G_0$ 后，用形式径向变量 $R$ 表示相对来源：
$$
\Phi(R,t)=\Phi_N(R,t)+c_0v_0(t)
 +c_1v_0(t)R u(t)+c_2v_0(t)R^2u(t)^2,
\tag{1}
$$
其中 $v_0=(t-1)(1+8t)h_7$、$u=(t-1)h_7$；
$\Phi_N$ 是原归一化的实际有限列。它们均在 $t=0$ 正规，正次数列在那里为零。
记 $\mathcal E=R\partial_R$、
$$W_i(\Phi)=(\mathcal E^i\Phi)(g(w),t(w)).$$
三个整数块仍准确为
$$
J_0=[W_0]_{<s},\quad
J_1=[a_pW_1+p\mathscr S W_0]_{<s},\quad
J_2=[a_p^2W_2/2+pa_p\mathscr S W_1+p^2\mathscr S^2W_0]_{<\ell},
\tag{2}
$$
其中 $\mathscr S$ 是普通系数移去 $s$ 次的算子。

令 $K$ 为 (1) 实际来源的模 $p$ 首核。R331 的准确提升商为
$$
\mathcal C_D^+=\frac{\Gamma_L/p}
 {I_{N,D}+\mathcal B_{13}+\operatorname{span}(\bar W_0^{\rm corr},
                 \bar W_1^{\rm corr},\bar W_2^{\rm corr})},
\tag{3}
$$
这里 $W_i^{\rm corr}=v_0(gue_2(a_p\epsilon))^i$ 是三条已付修正列，
$\mathcal B_{13}$ 是 R328 的两个各十三行跨界带。
对 $\bar\Phi\in K$ 取整提升，原首 Bockstein 类是
$$\beta_g(\bar\Phi)=[\mathcal J_g^+(\Phi)/p]\in\mathcal C_D^+.\tag{4}$$
更换来源提升只加一个实际像，故此类有定义。
下文始终在 (3) 中计算，未退回已经被 R331 扩大的单乘子商。

## 2. 首核可取物理常数兼容的原提升

因为 $v_0(0)=u(0)=-7$，(1) 在 $t=0$ 是
$$\Phi(R,0)=c-7c_0+49c_1R-343c_2R^2,$$
其中 $c$ 是 $\Phi_N$ 的常数。首核的三个径向常数给
$$c-7c_0+49c_1-343c_2=0,\quad49c_1-686c_2=0,
\quad49c_1-1372c_2=0\pmod p.$$
所以 $c_1=c_2=0$、$c=7c_0$ 在剩余域中成立。
因此每个首核向量都有一个仍在同一原来源中的整提升，满足
$$\boxed{\Phi(R,0)=0\text{ 恒等成立，故 }W_i(0)=0\quad(i\ge0).}\tag{5}$$
做法是将 $c_1,c_2$ 的提升取为零，并使 $c=7c_0$ 严格成立。
这只改变来源的一个 $p$ 倍，(4) 的余核类不变。
这里的 $W_i(0)$ 是物理轴常数；(2) 的径向常数行仍可能含真实 $p$ 进位。

以下论证也适用于整个已付原导子的任意有限分次部分除去 $G_0$ 后的实际列。
R329 的最低阶公式表明，相对次数 $n\ge3$ 时这些列至少有一阶物理零；
因此只有相对 charge0、1、2可能有常数。三个首核常数仍使该次数二多项式恒为零，
可按原分次部分作同样的兼容提升。后面的结论依赖这个确切事实，
不依赖单乘子归一化是否已经穷尽全部原导子。

## 3. 高轴不改变首提升，原中央参数只给一个末行类

**定理1。** 固定 $t(w)$ 与低轴，其余规范保持不变。

1. 将 $g$ 改为 $g+w^sH(w)$，$H\in\mathcal O[w]$，不改变首核，也不改变 (4)。
2. 将 $a_p$ 改为 $a_p+p\nu$ 不改变 (4)。
3. 将 $g$ 改为 $g+\tau w^{s-1}$ 时，首核有相同的自然识别，(3) 的像商也有相同的自然识别，且
$$
\boxed{\beta_{g+\tau w^{s-1}}(\bar\Phi)-\beta_g(\bar\Phi)
=\bar a_p\bar\tau\,\lambda_\ell(\bar\Phi)\,\eta_\ell,}
\tag{6}
$$
其中
$$\lambda_\ell(\bar\Phi)=[w^\ell]\bar W_2(\Phi),\qquad
\eta_\ell=[\epsilon^2w^{\ell-1}]\in\mathcal C_D^+.$$
因此原末个低轴系数的作用是一个准确的单秩映射。尤其 $g_{s-1}$ 的 $p$ 倍变化不改变首 Bockstein。

**证明。** 取 (5) 的提升。若 $\widetilde g=g e^z$，则在所需有限窗口内
$$\widetilde W_i=\sum_{j\ge0}z^jW_{i+j}/j!.\tag{7}$$
所需阶乘小于 $p$。首核条件正是
$W_0=W_1=0\bmod(p,w^s)$、$W_2=0\bmod(p,w^\ell)$。

当 $z\in w^s\mathcal O[[w]]$ 时，(2) 中被除以 $p$ 的三个低前缀完全不变。
第一移块的变化是 $(z/w^s)W_1$，模 $p$ 在其前 $s$ 项为零；
第三块第一次移块的变化是 $a_p(z/w^s)W_2$，模 $p$ 在其前 $\ell$ 项为零。
第二次移块在除一个 $p$ 后仍带 $p$，所以没有剩余项。这证明第一条。
第二条代入 (2) 后，所有变化分别含首核的 $W_1$ 或 $W_2$ 低前缀，亦为零。

对第三条，$z=\tau w^{s-1}+O(w^s)$；高部分已经由第一条处理。
由 (5)，所有 $\widetilde W_i-W_i$ 从 $w^s$ 才开始，故首核条件不变。
对来源的全部列，可能仍出现的低阶改变，只在两条修正列的前两块末行，
因而属于 $\mathcal B_{13}$；第三块长度小于 $s-13$，不读到这些改变。
这给 (3) 的同一个像商。

现在计算首提升的变化。第一块没有变化。第二块的移块变化是
$$\tau w^{-1}W_1+(\tau^2/2)w^{s-2}W_2+\cdots.$$
首核条件使它只可能在第一、第二块的末带留下项，均已由
$\mathcal B_{13}$ 支付。第三块的变化准确为
$$a_p\tau w^{-1}W_2\pmod{p,w^\ell}.$$
二次项含 $w^{s-2}W_3$，而 (5) 使它的阶至少 $s-1>\ell$。
因 $W_2=0\bmod(p,w^\ell)$，最后只剩
$a_p\tau[w^\ell]W_2\,w^{\ell-1}$，得到 (6)。$\square$

式 (6) 保留 R331 的全部修正尾。若先消三个径向常数，$\ell>1$ 时
$\eta_\ell$ 本身没有常数坐标；若 $\ell=1$，其准确常数消去代表为
$$
\boxed{\epsilon^2+
\frac{\bar W_0^{\rm corr}}{7\bar a_p^2}
+\frac{2\bar W_1^{\rm corr}}{49\bar a_p^2}
+\frac{\bar W_2^{\rm corr}}{343\bar a_p^2}.}
\tag{8}
$$
三个常数虽为零，式 (8) 的其余高行仍必须保留。对 R331 的后续实际 Schur 投影 $\Pi$，
式 (6) 的末行应写为 $\Pi(\eta_\ell)$；不能把一个主元坐标的消去当作其整个类为零。

## 4. 原中央首参数及完整下一位聚合

令
$$\widehat S=e^{-\kappa w^s}S=g(w)a(t(w))/(7b),\qquad
c_1=[w^s]\widehat S=s_{p+1},\quad c_2=[w^{2s}]\widehat S.$$
这里 $a(t(w))=7bw+\cdots$，所以
$$\boxed{g\mapsto g+\tau w^{s-1}\quad\Longrightarrow\quad c_1\mapsto c_1+\tau.}\tag{9}$$
定义用于精确矩阵分解的辅助低轴
$$g^\circ=g-c_1w^{s-1}.$$
它只是一种把实际参数写开的计算记号，不是另一条 theta 来源，也不赋予它新的中央条件。
定理1给出原数据的准确分解
$$
\boxed{\beta_g=\beta_{g^\circ}
 +\bar a_p\bar c_1\,\lambda_\ell\otimes\eta_\ell.}
\tag{10}
$$
R301 的完整中央失败首先迫 $c_1\equiv0\pmod p$，所以确实去掉 (10) 中显示的这一项。
它没有把剩余的 $\beta_{g^\circ}$ 置零。

这里还可以严格付出完整中央的下一位。R324 证明
$\widehat U,\widehat U^{-1}$ 在 $w^p$ 之前整；$S/U$ 是同一整形式参数的原有理函数，
所以 $\widehat S$ 在 $w^p$ 之前也整。特别 $3s<p$，故
$$a_3=\kappa^{-3}[w^{3s}]\widehat S\in p^3\mathcal O.$$
R301 的完整 Newton 尾使所有 $h\ge4$ 的中央导数项都在 $p^3\mathcal O$ 中。
因此
$$
\boxed{J'_S(0)\equiv\frac{p}{a_p}c_1
              -\frac{p^2}{a_p^2}c_2\pmod{p^3}.}
\tag{11}
$$
完整失败于是迫
$$
\boxed{a_pc_1-pc_2\equiv0\pmod{p^2},\qquad
c_1/p\equiv c_2/a_p\pmod p.}
\tag{12}
$$
第二式同时使用已知的 $c_1\equiv0\pmod p$。不能把 $c_1/p$ 和 $c_2$ 分别置零。

$c_2$ 以系数一读取 $g_{2s-1}$，而定理1第一条表明该高轴不会单独改变首 Bockstein。
$g_{s-1}$ 的 $p$ 倍变化也不改变首 Bockstein。因此 (12) 是真实的下一精度输入，
须通过原 theta 的确定方程继续运输；不能仅凭这一个聚合式宣称 (3) 的高行已被消去。

## 5. 同一原 theta 的首 carry：完整统一系数

下面给该确定方程与其第一高块，供下一提升使用；所有表达都在原 $t=-b/x^3$ 规范。
置
$$\mathcal L(t)=\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n.$$
由 $x'=2y,y'=3x^2,\zeta'=-x$，
$(\log\Theta)''=-4b/x^2$。又
$$t'=6by/x^4,\qquad t''=-6bx^{-2}(5-8t),\qquad
(t')^2=-36bx^{-2}t(1-t),$$
所以原方程准确为
$$
\boxed{6t(1-t)\mathcal L''+(5-8t)\mathcal L'=34/3,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.}
\tag{13}
$$
初值 $\mathcal L(0)=0,\mathcal L'(0)=34/15$ 确定全部系数。

记
$$h(t)=\sum_{n\ge0}h_nt^n,\qquad
h_n=\frac{(1/2)_n}{n!(6n+1)},\qquad z=u h(t),\quad u=x^{-1/2}.$$
对 $0\le n<2s$，有精确有理比值
$$
\frac{\ell_{s+n}}{\ell_s}
=\frac{p+1}{p+1+6n}
  \frac{(1/2+p/6)_n}{(1+p/6)_n}.
\tag{14}
$$
此窗口中的每个展开分母均为 $p$ 单位。令 $\mathsf H_n=\sum_{j=1}^n1/j$、$\mathsf H_0=0$，
则乘积的一次展开给
$$
\boxed{\frac{\ell_{s+n}}{\ell_s}
\equiv h_n(1+pD_n)\pmod{p^2},\qquad
D_n=1-\frac1{6n+1}+\frac{\mathsf H_{2n}-\mathsf H_n}{3}.}
\tag{15}
$$
这里 $p\ell_s$ 为单位；没有把首坏系数当作整系数。

定义固定有理级数
$$\mathcal H(t)=\sum_{n\ge0}h_nD_nt^n,\qquad
\mathcal T(t)=\mathcal H(t)-h(t)\log h(t).$$
再置真实的两个原常数
$$\alpha_p=p\ell_s,\qquad d_p=\ell_s-\kappa(-1/b)^s\in\mathcal O.$$
最后的整性来自原 Gaussian 消去，亦可由 (14) 的模 $p$ 首项核定。
因为
$$w^s=(-t/b)^s h(t)^{p+1},$$
原高块
$$\mathcal R_p(t)=t^{-s}\left(
\log g(w(t))-\log(1+8t)-\sum_{n<s}\ell_nt^n\right)$$
满足
$$
\boxed{\mathcal R_p(t)\equiv d_p h(t)+\alpha_p\mathcal T(t)
                  \pmod{p,t^{2s}}.}
\tag{16}
$$

**证明。** 对 (14) 的每个因子取对数一次导数，得到
$$1-\frac1{6n+1}+\frac16\sum_{j=0}^{n-1}
\left(\frac1{j+1/2}-\frac1{j+1}\right)=D_n,$$
即 (15)。在次数 $<2s<p$ 中，$h,\log h$ 都整，并且
$h^{p+1}\equiv h+p h\log h\pmod{p^2}$。
将 $\ell_s=\alpha_p/p$、$\kappa(-1/b)^s=\alpha_p/p-d_p$ 代回原式，
准确相消一层 $p$ 分母，剩余即 (16)。$\square$

(16) 中的 $d_p$ 是由原系数确定的常数，不是一个可自由选取的对数提升。
定理1说明这整个高块不会直接改变首 Bockstein；它是下一层仍须保留的实际数据。

## 6. 调和数 forcing 的原固定代数单位

记 $G(t)=(1-t)^{-1/2}$。有固定生成式
$$
\sum_{n\ge0}\frac{(1/2)_n}{n!}
(\mathsf H_{2n}-\mathsf H_n)t^n
=-G(t)\log\frac{1+\sqrt{1-t}}2.
\tag{17}
$$
例如可先对 $(1-t)^{-a}$ 在 $a=1/2$ 求参数导数，再用
$$\sum\frac{(1/2)_n}{n!}\mathsf H_nt^n
=2G(t)\log\frac{1+\sqrt{1-t}}{2\sqrt{1-t}}.$$
后一式由其初值零及
$(1-t)Y'-Y/2=(G-1)/t$ 直接验证，所以 (17) 是全形式恒等式。

由 $(1+6t\partial_t)h=G$，(15)、(17) 给
$$
\boxed{(1+6t\partial_t)\mathcal T
=-G(t)\left(\log h(t)+\frac13
                  \log\frac{1+\sqrt{1-t}}2\right).}
\tag{18}
$$
这并非两个无关的形式对数。取原固定双覆盖
$$\mathscr C:\ y^2=v^6+b,\qquad x=v^2,\qquad
v\sim z^{-1},\quad y\sim-z^{-3},\quad dz=v\,dv/y.$$
令 $f=v^3-y$。则
$$
\boxed{f(v^3+y)=-b,\qquad
\operatorname{div}(f)=3(P_+-P_-),\qquad d\log f=-3v\,dz,}
\tag{19}
$$
其中 $P_\pm$ 是 $y/v^3\to\pm1$ 的两个无穷点。
第一式是曲线方程；对 $f$ 求导给第三式。两无穷处的展开分别是
$f=-b/(2v^3)+\cdots$、$f=2v^3+\cdots$，证明中间的确切除子，没有其他零极。

在原物理分支，$\sqrt{1-t}=-y/v^3$、$h=zv$，所以 (18) 的对数准确为
$$
\boxed{\mathcal F(t):=\log h+\frac13\log\frac{1+\sqrt{1-t}}2
      =\frac13\log\frac{z^3(v^3-y)}2,\qquad
\frac{d\mathcal F}{dz}=\frac1z-\sqrt x.}
\tag{20}
$$
右端的括号在该原点分支为一，故是准确的正规形式对数。
$f$ 是固定曲线上的真正 Miller 单位，其支撑和阶数由 (19) 给全；
同时 $z^3$ 是原椭圆对数的 frame，仍必须保留。
本篇没有把 $\mathcal F$ 改成单独的 $\log f$，也没有把这条固定双覆盖免费作为原有限来源。

## 7. 目前已得到的实际约束

原完整失败给出 (10) 中 $\bar c_1=0$，并给出保留两项的真实下一精度 (12)。
R331 修正后的首提升问题因此准确落在确定的 $\beta_{g^\circ}$，其实际 Schur 高行仍须计算。
(16)、(18)、(20) 进一步提供了一个与原 theta、原椭圆对数及固定代数单位同时兼容的
下一层 forcing，不能用任意高对数替换。

尚未证明的是：原完整失败是否使这个确定 forcing 的实际配对落入 R331 的原像，
或是否迫某个高行成为单位矛盾。需要控制的是同一个实际像商；
来源导子、已付常数修正、单独的 Miller 单位非平凡性都不代替该配对。

## 固定精确证书

- `scripts/check-jzero-central-rank-one-and-fixed-harmonic-carry.py/.json`：核实际 theta 方程、固定调和数生成式、两次中央聚合、三条常数修正及原 genus-two 单位微分。

依赖：R301 完整 Newton 尾；R322 原三块及下一障碍；R324 至 $w^p$ 的真实整性；
R328 完整十三行运输；R331 扩展来源及其完整 Schur 余块。

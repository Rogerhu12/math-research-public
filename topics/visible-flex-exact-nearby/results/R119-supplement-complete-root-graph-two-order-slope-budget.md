# R119 续篇：真实根图的完整二阶余项与斜率费用

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在[原真实根图](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
的同一小球、同一物理切口和完整密度标签空间中，把第51束为 graph
宽放的 $b^4$ 二阶费用收回到 $b^2$。令 $\mathcal T_g$ 为第1节
定义的完整图传递，$\mathcal P_g^{(1)}$ 为保留真实 principal 两角、
完整高度恢复及同支首相位的模型。则 $|s|\le1$ 时

$$
\boxed{\quad
\|\mathcal T_g-\mathcal P_g^{(1)}:
      \mathcal W_s\to\mathcal W_{s+2}\|<2^{1024}b^2,
\qquad
\|\mathcal T_g-\mathcal P_g^{(1)}:
      \mathcal W_s\to\mathcal W_{s+4/3}\|<2^{700}b^{4/3}.
\quad}
\tag{G.1}
$$

正逆方向均成立。$\mathcal W_s$ 保留两个独立 mean；它是在实际
strict density waves 中的完整状态，见 (G.8)，不是裸 raw 高度范数。
物理 height、conormal、端图和 weak 端点荷在第6节准确恢复。
这里不据此将整个负段或全网络的新阈值写成已经成立。

## 1. 实际图、精确 principal 流和完整 mean

沿用原根图篇的 $H=1/64$、$g(\phi)$、$b>1$、$n=n_i$：

$$
|g-H|<2^{13}n,\qquad b^2n\le2^{-512},\qquad
c(\xi)=\sqrt{\xi}/b,\qquad
\kappa(\xi,\phi)=b\left({5\over16\xi^{5/2}}
                           +{V(\xi,\phi)\over\sqrt\xi}\right).
\tag{G.2}
$$

所有图都在 $H/2<\xi<2H$ 的同一实际解析 germ 内；
$|V|<17,\ |V_\xi|<129,\ |V-V_0|<2^{32}n$。
图高差记为 $q(\phi)=g(\phi)-H$，中间图为
$g_s=H+sq,\ 0\le s\le1$。它可以变号，也可以在任何点为0。

先取齐次源。原完整密度高度和两态满足

$$
y_\sigma={w_\phi+\sigma w_\xi/c\over2},\qquad
(y_\sigma)_\xi-\sigma c(y_\sigma)_\phi
                =-\sigma\kappa w/2.
\tag{G.3}
$$

在中间图上取实际密度迹

$$
W_s=w(g_s,\phi),\qquad
Y_{\sigma,s}=(1+\sigma c(g_s)g_s')y_\sigma(g_s,\phi).
\tag{G.4}
$$

准确有 $(W_s)_\phi=Y_{+,s}+Y_{-,s}$。对 $s$ 求导、用 (G.3)，
并把图密度因子的导数保留，直接得到

$$
\partial_sY_{\sigma,s}
 -\sigma\partial_\phi\left({q\,c(g_s)\over1+\sigma c(g_s)g_s'}
                                     Y_{\sigma,s}\right)
           =-\sigma q\kappa(g_s,\phi)W_s/2.
\tag{G.5}
$$

两支准确标签是

$$
L_{\sigma,s}(\phi)=\phi+\sigma\int_H^{g_s(\phi)}c(\xi)\,d\xi,
\quad L_{\sigma,s}'=1+\sigma c(g_s)g_s',
\quad H_{\sigma,s}=L_{\sigma,s}^{-1}.
\tag{G.6}
$$

设 $\mathcal D_H=M_{H'}C_H$，
$X_\sigma=\mathcal D_{H_{\sigma,s}}Y_{\sigma,s}$，
$\alpha=\langle X_+\rangle=-\langle X_-\rangle$、
$Z_\sigma=X_\sigma-\sigma\alpha$。完整周期高度恰为

$$
W_s=c_0+\alpha(L_{+,s}-L_{-,s})
       -i\sum_\sigma C_{L_{\sigma,s}}D_\phi^{-1}Z_\sigma,
\qquad D_\phi=-i\partial_\phi .
\tag{G.7}
$$

此处 $c_0$ 是实际独立积分常数，通常不等于输出的物理平均。
$D_\phi^{-1}$ 只在 mean 为0。高度的 mean 和通量的 mean 均在
$(c_0,\alpha)$ 中，未再添加一个把其中之一设零的条件。
定义平衡状态和范数

$$
\mathcal W_r=\mathbb C^2\oplus(H^r_0)^2,\qquad
\mathcal Y=(c_0,\alpha,|D_\phi|^{-1/2}Z_+,
                            |D_\phi|^{-1/2}Z_-).
\tag{G.8}
$$

使用 Hilbert 直和范数。与原有限个分量的和范数互换只需固定因子2，
下列余量均已包含。

## 2. 没有图高差分母的跨支原函数

为使 (G.5) 与第51束的完整密度系统准确相同，置

$$
C_s=1-c(g_s)^2(g_s')^2,\qquad
\nu_s={q\,c(g_s)\over C_s},\qquad
d_s=-{q\,c(g_s)^2g_s'\over C_s},\qquad
\kappa_s=q\kappa(g_s,\phi).
\tag{G.9}
$$

于是两支速度为 $-d_s-\sigma\nu_s$，
$H_{\sigma,s}$ 正是它们的真实流。
$C_s>1/2$，但 $\nu_s$ 不要求有固定符号。
跨支原函数的系数定义为下式右端：

$$
R_s:={\kappa(g_s,\phi)C_s\over c(g_s)}.
\tag{G.10}
$$

在 $q\ne0$ 时它等于 $\kappa_s/\nu_s$；右端在 $q=0$ 仍光滑，
所以没有除以图高差。
对 $\tau=-\sigma$，先在未作 $|D_\phi|^{-1/2}$ 平衡的标签上写

$$
K_{\sigma\tau}
 ={i\sigma\over2}\Pi_0\mathcal D_{H_\sigma}
              M_{\kappa_s}C_{L_\tau}D_\phi^{-1}\Pi_0,
\qquad
\mathcal L_{\sigma\tau}
 =-\frac14\Pi_0\mathcal D_{H_\sigma}M_{R_s}
                  C_{L_\tau}M_{H_\tau'}D_\phi^{-2}\Pi_0 .
\tag{G.11}
$$

这里乘子 $H_\tau'$ 的变量和投影次序都与第51束 (H.8) 相同。
准确求导得

$$
K_{\sigma\tau}=\partial_s\mathcal L_{\sigma\tau}
                                -\mathcal Z_{\sigma\tau},
\tag{G.12}
$$

$$
\begin{split}
\mathcal Z_{\sigma\tau}
={}&-\frac14\Pi_0\mathcal D_{H_\sigma}
 M_{(R_s)_s+(-d_s-\sigma\nu_s)(R_s)_\phi-2(d_s)_\phi R_s}
 C_{L_\tau}M_{H_\tau'}D_\phi^{-2}\Pi_0\\
&+\frac{\sigma}{2}\Pi_0\mathcal D_{H_\sigma}
 M_{\kappa_s}C_{L_\tau}
 M_{H_\tau''/H_\tau'}D_\phi^{-2}\Pi_0 .
\end{split}
\tag{G.13}
$$

这首先是在 $q\ne0$ 的开集对第51束原恒等式作代入；所有显示系数
均由 (G.10) 光滑延拓。直接乘开后不出现 $q^{-1}$，故恒等式在
$q=0$ 也成立。如果 $q$ 在一个开集恒为0，则该开集上的
$q'$ 及 $s$ 导也为0，等式同样准确成立。
这处理了变号图，不以一个固定符号的假时间变量替代真实图。

## 3. 每个额外斜率因子的实际支付

以下只用有限角导，不跨任何径向接缝作高阶求导。
在原图复域缩到宽 $1/128$ 后，Cauchy、$H/2<g_s<2H$ 和
(G.2) 给可直接代入的宽裕界：

$$
\begin{array}{c|c}
\text{完整系数，含所需至多8阶角导}&\text{上界}\\ \hline
q,\ g_s-H&2^{64}n\\
L_\sigma-\mathrm{id},\ H_\sigma-\mathrm{id}
                         &2^{96}n/b\\
\kappa_s=q\kappa(g_s,\phi)&2^{192}bn\\
R_s&2^{256}b^2\\
(R_s)_s,\ (R_s)_\phi,\ (d_s)_\phi R_s&
                         2^{256}b^2n
\end{array}
\tag{G.14}
$$

第一行由 $2^{13}n$ 的整角域界求8阶导；第二行再用
$|c|<1/b$、$C_s>1/2$ 及逆函数的有限链式公式。
$\kappa_s$ 每项都有 $q$；$R_s$ 的最大固定系数是
$b^2\,5/(16g_s^3)$，只用 $g_s>1/128$。
其 $s$ 导给 $g_{s,s}=q$ 或 $g_{s,s}'=q'$；
其角导给 $g_s'$ 或 $V-V_0$ 的角导，因而都带 $n$。
所需的径向势导仅为 $V_\xi$，由 (G.2) 支付。
例如单次八阶角费小于 $8!\,256^8<2^{80}$；两次有限乘积链式法则
及逆函数的系数和放宽为 $2^{64}$，加固定 $128^3$ 与势的
$2^{32}$ 后仍低于显示的 $2^{256}$。所有行同时在固定较小复角域成立。

在 $|r|\le3$ 所需的两阶输出窗内，原 density pullback 及逆、
乘法和 $|D_\phi|^{\pm1/2}$ 平衡的有限窗口费用可各取 $2^{20}$；
这是原根图篇 (G.16)–(G.23) 的整数链式法则、对偶及插值门。
本处系数的全部8阶界已由 (G.14) 提供。
对 mean 列使用 (G.7) 及其准确两个 mean 行；
其非零 Fourier 输出带完整解析系数，所以两阶权由同一角域支付。
同支的异号 Fourier 锥也是解析远 lag，属于这些平滑项。
于是准确完整 generator 可分为
$K_d+K_{\rm cross}+K_{\rm sm}$，并有

$$
\int_0^1\|K_{\rm all}\|_{\mathcal W_r\to\mathcal W_r}\,ds
 <2^{256}bn,\qquad
\int_0^1\|K_d\|_{H^r\to H^{r+1}}\,ds<2^{256}bn,
\tag{G.15}
$$

$$
\sup_s\|\mathcal L(s):H^r\to H^{r+2}\|
       <2^{384}b^2,\qquad
\int_0^1\|\mathcal Z(s):H^r\to H^{r+2}\|\,ds
       <2^{384}b^2n,
\quad
\int_0^1\|K_{\rm sm}:\mathcal W_r\to\mathcal W_{r+2}\|\,ds
       <2^{256}bn .
\tag{G.16}
$$

这里 $K_{\rm sm}$ 含两个 mean 的完整行、列，不能删除。
在 (G.16) 中 $\mathcal L,\mathcal Z$ 在 mean 上置0，只表示
跨支分部积分不对 mean 使用 $D_\phi^{-1}$。
$|r|\le1$ 时输出最高是 $r+2\le3$，所需平衡前密度指数最高为
$5/2$；全部落在原根图允许窗内。

特别，由 $bn\le b^2n\le2^{-512}$，准确全演化
$U_g'=K_{\rm all}U_g$、同支演化 $U_d$ 及其逆的同阶范数均小于2。
这次可以直接对小图段的完整 generator 作 Gronwall，因为真实
图高本身带 $n$；没有对一整条 strict 段这么做。

## 4. 完整有序 Duhamel 与插值

同支两锥内的平衡 generator 准确为

$$
{i\sigma\epsilon\over2}|D_\phi|^{-1/2}\Pi_\epsilon
 M_{H_\sigma'\kappa_s\circ H_\sigma}
 \Pi_\epsilon|D_\phi|^{-1/2},
\tag{G.17}
$$

故为反自伴。令 $B_g=\int_0^1K_d\,ds$，在两个 mean 上取0；
$e^{B_g}$ 是完整空间上的真正酉模型，两个 mean 仍作为模型的独立
恒等块保留，其实际改变在 $K_{\rm sm}$ 中。

对完整 $U_g-U_d$ 使用 (G.12) 作一次真正分部积分。
端项是 $U_d\mathcal L U_g|_0^1$；积分项的真实次序为

$$
-\int U_d\{\mathcal Z+[\mathcal L,K_d]
                  +\mathcal L K_{\rm cross}
                  +\mathcal L K_{\rm sm}\}U_g
       +\int U_dK_{\rm sm}U_g .
\tag{G.18}
$$

没有把完整 $U_g$ 换成模型。由 (G.15)–(G.16) 和正逆同阶界<2，
两个端项小于 $2^{387}b^2$；$\mathcal Z$ 项小于
$2^{386}b^2n$；至多三个 $\mathcal L K$ 项各小于
$2^{643}b^3n\le2^{131}b^2$。最后的完整平滑行列项小于
$2^{258}bn\le2^{258}b^2$。
这明确指出原粗费用里多出来的一个 $b$ 是怎样由实际 $n$ 支付的，
而不是直接删去它。

同支时间有序传播减去 $I+B_g$，以及 $e^{B_g}-I-B_g$，各自用
两次完整积分，二阶费均小于 $2^{513}b^2n^2$。
因此

$$
\|U_g-e^{B_g}:\mathcal W_s\to\mathcal W_{s+2}\|
 <2^{1020}b^2,\qquad
\|U_g-e^{B_g}:\mathcal W_s\to\mathcal W_s\|<4 .
\tag{G.19}
$$

输出到实际图迹使用 (G.6)–(G.7) 的**完整** principal 恢复算子
$\mathscr P_s$；它的两个 mean 行也随式恢复。
在所需窗上 $\mathscr P_s$ 和逆范数小于2：
所有偏离参考恒等角图的有限导数为 $2^{96}n/b$，
principal 非mean部分的范数用真实 pullback而不是
$\|C_H-I\|$ 估计，mean 恢复的额外有限行列同样小于
$2^{256}n/b$。具体地，在整数 $0,\ldots,4$ 阶使用
$(1+m^2)^k$ 展开的准确二项式能量，对 density transport 作一次
角分部积分；主导数相消，剩余交换子和 Jacobian 项的 log-norm
不超过 $2^{128}n/b$。负阶由真实 density 对偶取得，中间阶由
Hilbert 插值取得。再加上述有限 mean 行列，总能量费用仍小于
$2^{-200}$，故正逆范数严格小于2。定义

$$
\mathcal T_g=\mathscr P_1U_g,\qquad
\mathcal P_g^{(1)}=\mathscr P_1e^{B_g}.
\tag{G.20}
$$

二阶费放宽为 $2^{1024}b^2$，同阶差小于8。
固定输入 $\mathcal W_s$，对输出标度作参数 $2/3$ 的 Hilbert
插值，得到

$$
8^{1/3}(2^{1024}b^2)^{2/3}
       =2^{2051/3}b^{4/3}<2^{700}b^{4/3},
\tag{G.21}
$$

证明 (G.1)。逆向使用同样的小图方程和反向有序积分；
所有小量、端项及恢复的逆界相同。

## 5. 哪个 mean 单位参加估计

本篇 (G.8) 是实际 strict density 的单位，不能在未经转换时等同
于原 Airy root 的裸 mean。原两态转换明确为

$$
c_0=\sqrt{c_*}\,u_0,\qquad
\alpha={u_{\xi,0}+16u_0\over2\sqrt{c_*}},
\qquad c_*={1\over8b}.
\tag{G.22}
$$

从原根图 (G.22)–(G.23) 逐项读取，mean 两方向的有限转换费至多
$2^{20}\sqrt b$。只有与 mean 相连的实际 graph 余项使用这个费；
它们本身带 $bn$：对 mean 输入直接在准确 Duhamel 中使用
$K_{\rm all}$ 的完整 mean 列及输出 $H^{s+2}$ 上的 $U_g$，
对 mean 输出使用其完整 mean 行和输入 $H^s$ 上的 $U_g$，
两者均由 (G.15)–(G.16) 给 $2^{258}bn$ 的宽裕门；
不分别粗估 (G.18) 中会相消的大端项。双向转换合起来最多给
$2^{298}b^2n<2^{-214}$，仍严格位于 (G.1) 的余量内。
非mean的自由 Airy 到 strict wave 两行转换是另一个实际因素；
本篇没有用此 mean 论证免除其全部低频费用。
最终复合必须使用那个因素的真正高输出和低到高门。

## 6. 原单位的全部源和两端口

令 $k=\alpha_{\rm raw}c$ 为原根图的真实判别式密度，
$H(\theta)$ 为固定物理 $t$ 切口的角图，
$s_g=(\partial_\xi+c^2g'\partial_\phi)\log k/(2c)$。
齐次两迹仍准确为

$$
h=(k^{-1/2}W)\circ H,\qquad
p=\varsigma H'\,[\sqrt k(Y_+-Y_--s_gW)]\circ H .
\tag{G.23}
$$

这些真实乘子、normal shear、$\varsigma$ 和 $H'$ 在主项及余项
两侧使用同一准确变换，不被置为1。物理平均仍是
$\langle(H^{-1})'k^{-1/2}W\rangle$ 和
$\varsigma\langle\sqrt k(Y_+-Y_--s_gW)\rangle$。

对原 $Ph=f-\operatorname{div}F$，使用原篇的准确 Piola 后

$$
F_d=k^{-1/2}\widetilde F,\qquad
f_d=k^{-1/2}(\widetilde f-\tfrac12\nabla\log k\cdot\widetilde F).
\tag{G.24}
$$

在图上，完整 weak 两行修正为

$$
\widehat Y_\sigma
=Y_\sigma-\frac{g'}2(cF_d^\xi+\sigma F_d^\phi)|_g,
\quad
W'=\widehat Y_++\widehat Y_-,
\quad
p_{d,g}^{\rm total}=\widehat Y_+-\widehat Y_- .
\tag{G.25}
$$

其平均也必须保留。普通源和 weak 源仍消费原根图 (G.30)–(G.37)
的完整联合路径 norm、ordinary 修正和两端 bare/total 荷；
原预条件源费 $2^{120}\sqrt b\,D_e\mathfrak S_e+2^{40}\sqrt b\|\mathcal B_g\|$ 原样有效。
本篇只改善齐次余项，没有将一般粗 $L^2_tH^s_\theta$ 源免费授予
混合径向—角图的高窗迹。

原材料标签的根内齐次性仍来自实际 Darboux residual=0；
$\Gamma^*$ 两参数列及固定物理半径所产生的尺度/坐标列按原合同
逐项相加。最终全网普通/weak 源映射仍须保留它们，不能由本篇
局部齐次改善宣布这些列为零。

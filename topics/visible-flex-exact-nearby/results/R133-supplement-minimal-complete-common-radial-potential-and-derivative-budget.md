# R133 补篇：common-T 势及两阶 T 导数的完整最小输入预算

2026-11-15，visible-exact / phase_inverse。

**状态：本篇证明准确导数公式、完整尾界及条件数值合同；新的 potential/gap/传播数值门未执行。**
参考对象是同一固定 $\eta_0$、原完整65中心与193方向的显式背景族，
$|\delta|\le10^{-8}$。以下标量代数保复 $\delta$，实际正测度与能量仍须限实参数。

依赖
[共同径向 reference](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md)、
[保留抵消的 c/V](R133-supplement-cancellation-preserving-common-radial-potential-and-ports.md)
和[旧圆 primitive/mean 接口](R133-supplement-common-radial-reference-old-circle-primitive-and-mean-interface.md)。
原 free-Airy 的成功 source bound 不因本篇被改写。
参考两列、选定正侧图、原物理 seam 及完整 high feedback 仍各有独立费用。

## 1. 同一域、同一完整有限背景

取物理坐标 $x=r-r_*$，故旧 $\rho=-x$，$K=xk$。
本节首先在原根片的单一解析延拓内取 $|x|\le H<R_C$。
实际物理身份只在原根片内成立；辅助延拓不将相邻不同 cubic 认作同一背景。
对于本题已有数据，可用原复域 $R_C=1/2000$ 的完整三阶 intrinsic 界，
前提仍是原真实根区间加该圆盘完整包含在已证复矩形中。
这个包含关系已作为run43682479300/1的实际门核过，不能省略根区间的宽度。

全背景写作
$$
 u(r,\phi)=\sum_{p=0}^3U_px^p,\qquad
 v(r,\phi)=s(r)+\sum_{p=0}^3(V_p-S_p)x^p .
 \tag{B.1}
$$
这里 $U_p,V_p$ 是原完整 signed Fourier 多项式，
$S_p=s^{(p)}(r_*)/p!$ 作为完整均值槽加入。
原常数 repair 在 $p=0$ 中准确保留；它的正阶导为0，
但不能因而删除完整 $V_0$ 或方向均值。
原生成记录若按 $\rho$ 保存，必须对第 $p$ 阶系数乘 $(-1)^p$ 后才用于 (B.1)。

设 $m=\langle v\rangle$、$\eta=-\gamma m$、$b=\beta$，
不要混淆特征系数 $\eta$ 与固定 intrinsic 参数 $\eta_0$。
全部 $u_\ell,v_\ell$ 是 bilinear complex-family 系数；
复参数计算不以复共轭替代 $u_{-\ell},v_{-\ell}$。

## 2. 原三阶复域与0--15阶数据足够支付新增4、5阶

设 $f$ 为 $K,\beta,\gamma,s$ 中任一项，原完整数据给
$f^{(j)}(r_*)$，$0\le j\le15$，以及
$$
 \sup_{|x|\le R_C}|f^{(3)}(r_*+x)|\le M_{f,3}.
$$
记 $t=H/R_C<1$，$P_{15,f}(x)=\sum_{j=0}^{15}f^{(j)}(r_*)x^j/j!$。
对 $0\le p\le5$，Cauchy 与完整余项给
$$
 \sup_{|x|\le H}|f^{(p)}-P_{15,f}^{(p)}|
 \le M_{f,3}R_C^{3-p}t^{16-p}C_p(t),
 \tag{B.2}
$$
其中可取
$$
\begin{array}{c|c}
p&C_p(t)\\ \hline
0&[16\cdot15\cdot14(1-t)]^{-1}\\
1&[15\cdot14(1-t)]^{-1}\\
2&[14(1-t)]^{-1}\\
3&(1-t)^{-1}\\
4&13(1-t)^{-1}+t(1-t)^{-2}\\
5&156(1-t)^{-1}+25t(1-t)^{-2}
                    +t(1+t)(1-t)^{-3}
\end{array}
 \tag{B.3}
$$
证明是逐完整遗漏阶 $n\ge16$ 使用
$|f_n|\le M_{f,3}R_C^{3-n}/[n(n-1)(n-2)]$。
对 $p=4,5$，导数比恰分别为 $n-3$ 与 $(n-3)(n-4)$；
令 $n=16+j$ 并求完整几何和即得。
这不是由已存三阶值直接假定高阶为0；新增尾消费仍是新数学。

$K(r_*)=0$ 是原 true-root 精确身份。
设 $P_{14,k}=P_{15,K}/x$，其原根处可去值准确保留。
对 $0\le p\le4$，
$$
 \sup|k^{(p)}-P_{14,k}^{(p)}|
 \le M_{K,3}R_C^{2-p}t^{15-p}D_p(t),
 \tag{B.4}
$$
可取
$$
\begin{array}{c|c}
p&D_p(t)\\ \hline
0&[16\cdot15\cdot14(1-t)]^{-1}\\
1&[16\cdot14(1-t)]^{-1}\\
2&[16(1-t)]^{-1}\\
3&(1-t)^{-1}\\
4&10(1-t)^{-1}+t(1-t)^{-2}
\end{array}.
 \tag{B.5}
$$
第4行的导数比为 $(n-3)/n\le1$；
最后一行用 $(n-3)(n-4)/n\le n-6$，$n\ge16$。
(B.4) 不除小 $x$，在根两侧同时有效。
它还可与 $k^{(p)}=\int_0^1s^pK^{(p+1)}(r_*+sx)\,ds$
的独立完整界取交。
两个完整合法界可以取交或取较小上界，不能相减上界构造缺失部分。

## 3. 必须实际支付的根 gaps 与径向平均

定义
$$
 a_\infty=\eta\sqrt{k},\qquad
 \bar A(x)=\frac32\int_0^1s^{1/2}a_\infty(sx)\,ds,\qquad
 \kappa=\eta\sqrt{k}\,\bar A^{-1/3}.
 \tag{B.6}
$$
所有分支由真实根正数据固定。新 consumer 必须在同一复域支付
$k,\eta,\bar A,\kappa$ 的模下界，不把实轴正下界直接外插到复盘。
例如以下是合法的待核门：
$$
 |k_*|-H\sup|k_r|>0,\qquad
 |\eta_*|-H\sup|\eta_r|>0,\qquad
 |a_{\infty,*}|-\frac35H\sup|(a_\infty)_r|>0 .
 \tag{B.7}
$$
第三式来自 $\bar A(0)=a_{\infty,*}$ 与
$$
 \sup|\bar A^{(p)}|
 \le\frac3{2p+3}\sup|a_\infty^{(p)}|,\qquad0\le p\le4.
 \tag{B.8}
$$
整段 $s x$ 必须落同一已付域；(B.8) 不是跨不同 physical cubic 的公式。

归一化 jets 的乘积与 reciprocal 是有限准确递推。
若 $F_p=f^{(p)}/p!$、$Q_p=(f^{-1})^{(p)}/p!$，则
$$
 Q_0=F_0^{-1},\qquad Q_p=-Q_0\sum_{i=1}^p F_iQ_{p-i}.
 \tag{B.9}
$$
平方根及分数幂可由 $f g_r=\theta f_rg$ 逐阶解出；
每次除法均使用同一完整 ball 与已付下界。
对上包络，分母不能取原量的上端来冒充下界。
在形成 $c$ 与势的 signed 多项式之前，不把这些 jets 变成独立绝对端点。

在严格离根片上，$\bar A$ 改由真实入口及
$$
 2x\bar A_r+3\bar A=3a_\infty,\qquad
 2x\bar A^{(p+1)}+(2p+3)\bar A^{(p)}=3a_\infty^{(p)}
 \tag{B.10}
$$
延续。该入口由根一路累积，不能每片重新归一化。
原 seam 两侧 jets 和实际 reference 匹配矩阵另外保存；
不得以 (B.8) 把不同真实 pieces 拼成同一解析函数。

## 4. 全部 $|j|\ge97$ 的完整有限频率参数

设 $M\le96$，$z=j^{-2}$，$Z=97^{-2}$。
在整个复盘 $|z|\le Z$，
$$
 |1-\ell_0^2z|\ge1-\ell_0^2Z>0,\qquad1\le\ell_0\le M.
 \tag{B.11}
$$
最坏完整 gap 是 $193/9409$。
以下有限和准确保全部 modes，分母不作截断展开：
$$
\begin{aligned}
D_{uu}&=\sum_{\ell_0=1}^M
 {2\ell_0^2z\over1-\ell_0^2z}u_{\ell_0}u_{-\ell_0},\\
D_{vv}&=\sum_{\ell_0=1}^M
 {2\ell_0^2z\over1-\ell_0^2z}v_{\ell_0}v_{-\ell_0},\\
\alpha&={b\over i}\sum_{\ell_0=1}^M
 {\ell_0\over1-\ell_0^2z}u_{\ell_0}v_{-\ell_0},\\
a&=\eta+z\alpha,\qquad \theta={z\alpha\over\eta},\\
E&=\langle-b(1+3u^2+Kv^2)\rangle-2bD_{uu},\\
B&=\langle b(1-u^2-3Kv^2)\rangle-2bKD_{vv},\qquad D=E-B.
\end{aligned}
 \tag{B.12}
$$
$\theta$ 是本节有限频率的 relative coefficient，不是旧圆矩阵逆中的
$y^2V/(n^2B_+)$。
新门还须支付 $1+\theta$ 或等价的 $a$ 的完整模下界。
例如 $\sup|\theta|<1$ 足够，但不能预设它在 $j=97$ 成立。

有限和的径向 jets 逐项使用 Leibniz，$z$ 固定不微分。
完整复系数上的每个 $u_{\ell_0}v_{-\ell_0}$ 先有序相乘再相加。
若使用 joint 系数上界，应实际给 $\sum_\ell\sup_r|\cdot|$；
逐 $r$ 的 Wiener 上界不能直接改写为这个 joint 和。
也可直接在每个共同径向域对完整有限和作 ball 运算，不需要这种互换。

$z=0$ 是无限频率的可去极限，**不是物理 $j=0$**。
物理 independent even mean 始终使用原 (N.7)。
奇偶性给两符号相同的 $a,E,B,V,G$，但源/trace矩阵仍保
$A_j=i\epsilon n a$，$n=4|j|$，$\epsilon=\operatorname{sgn}j$；
这条身份不使用复参数共轭。

## 5. 精确抵消后一次生成 $V,V_T,V_{TT}$

沿同一 physical $r$ 定义
$$
\begin{aligned}
\ell&={\eta_r\over\eta}+{k_r\over2k}-{\bar A_r\over3\bar A},\\
q&=D+{\eta_r\over\eta}+{\theta_r\over1+\theta},\\
c&={k_r\over4k}-{\bar A_r\over6\bar A}
                  -{D\over2}-{\theta_r\over2(1+\theta)},\\
L&=\ell+q,\qquad
F=16K(2\eta\alpha+z\alpha^2),\\
W&=-c_r+\frac12cL-F .
\end{aligned}
 \tag{B.13}
$$
这里 $W$ 是完整 signed 表达式；它不是分别取过绝对值后再相减的两个旧上界。
被消去的只是同一 $\eta_r/\eta$ 的重复项，
$D$ 中完整有限 $b$、原 mean、全部 primitive Fourier 修正均仍在。

共同 reference 势恰为
$$
 \boxed{
 V={W\over\kappa^2},\qquad
 V_T={W_r-2\ell W\over\kappa^3},\qquad
 V_{TT}={W_{rr}-5\ell W_r+(6\ell^2-2\ell_r)W\over\kappa^4}.}
 \tag{B.14}
$$
证明只用 $\partial_T=\kappa^{-1}\partial_r$。
在生成 derivatives 前代入(B.13)，不另外对两份巨大 logarithmic 项取独立界。
所需两个准确中间导数为
$$
\begin{aligned}
W_r&=-c_{rr}+\tfrac12(c_rL+cL_r)-F_r,\\
W_{rr}&=-c_{rrr}+\tfrac12(c_{rr}L+2c_rL_r+cL_{rr})-F_{rr}.
\end{aligned}
 \tag{B.15}
$$
(B.14) 的所有 powers 都是原非零 $\kappa$，没有 $K^{-1}$、$x^{-1}$ 或 $z^{-1}$。

根片的足够最高普通导数要求为：

| 输出 | $k,\bar A,\eta,\alpha$ | $D$ | 根 intrinsic 的足够最高阶 |
| --- | --- | --- | --- |
| $V$ | 至2阶 | 至1阶 | $K$至3阶，其余至2阶 |
| $V_T$ | 至3阶 | 至2阶 | $K$至4阶，其余至3阶 |
| $V_{TT}$ | 至4阶 | 至3阶 | $K$至5阶，其余至4阶 |

(B.2)--(B.5) 因而从原0--15阶与原三阶复域数据覆盖全部需求，
没有请求第16阶 target、FFT 或重新生成原成功 derivatives。
这不意味着新范围内的 reciprocal 或 $V$ 数值门已经成功。

## 6. 真 $T$ 评价域与完整旧圆费用

(B.14) 首先界 $V(z,T_{\rm ref}(r))$。
若要在非径向 $T_{\rm old}(r,\phi)$ 上评价同一参考势，
还必须支付一维 reference 的真实 inverse image。
例如在一个凸复盘上若
$$
 \sup|\kappa/\kappa_*-1|\le\vartheta<1,
$$
则 $T_{\rm ref}/\kappa_*$ 在该盘单叶；
Rouché 给其像包含半径 $(1-\vartheta)|\kappa_*|H$ 的同心盘。
实际 $T_{\rm old}$ 的全像须落入这个已付像域或另一明确认证的同分支像域。
$\kappa\ne0$ 的局部事实本身不保证所需全局像域。

在该合法共同域中，
$$
 V_\phi=V_TT_\phi,\qquad
 V_{\phi\phi}=V_{TT}T_\phi^2+V_TT_{\phi\phi}.
 \tag{B.16}
$$
右端 $V_TT_\phi$ 是 $V_T$ 与 $T_\phi$ 的乘积；
$V_{TT}$ 是势的二阶 $T$ 导数。
真实 mixed/radial 导数同样逐项链式微分，并保
$[\,\partial_r-d\partial_\phi,\partial_\phi\,]=d_\phi\partial_\phi$。

旧圆逆门仍为
$$
 H_j^V=H-\frac{T_\phi V}{n^2}E_{12},\qquad
 \det H_j^V=-B_+\left(1-\frac{T_\phi^2V}{n^2B_+}\right).
 \tag{B.17}
$$
$B_+$ gap 及 $n\ge388$ 只提供一个待检验的 finite-frequency 界；
不能预设其乘积小于1。
二阶角导需(B.14)--(B.16)的完整信息。
只有 strip supremum 时，转到更窄 Wiener 窗仍须支付 Fourier 几何和。
全输出 mean、projection、$J$ 真实奇偶域和有序字一律保留。
若复 $T$ 轨迹穿过真实 reference seam，先使用逐支公式，
再付真实重构列及 $B_jw$ 的分布 jump；
不存在一条自动取消这些 jump 的声明。

## 7. 同一根规范、两源和下一实际消费者的边界

同一 gauge 有
$$
 G_r=(B-c)G,\qquad G(r_*)=1.
 \tag{B.18}
$$
在合法路径上可用 $\exp(\int|B-c|\,|dr|)$ 同时界 $G$ 与 $G^{-1}$。
真 piece 接口继承完整非零 $G$，不重置为1。
需要 derivative 时，$G_{rr}=[(B-c)_r+(B-c)^2]G$ 等准确代数沿同域生成。

两源矩阵仍是
$$
 U_T=P+\frac{g_2}{\kappa G},\qquad
 P_T=(n^2T-V)U+\frac{A_jg_1+cg_2}{\kappa^2G}.
 \tag{B.19}
$$
没有微分 ordinary $g_2$，也没有去掉其第二行贡献。
根数据的完整矩阵仍连接 $(n^{1/3}h_1,h_2)$ 与 $(U,n^{-2/3}P)$；
$r_*$ 两侧使用同一个规范和同一个 signed $A_j$。

以下原数据确切覆盖本篇的待消费输入：

| 原公开 run/记录 | 已完成输入及使用范围 |
| --- | --- |
| 43661471951/1 | $K,\beta,\gamma,s$ 的原普通根导数0--15，$K_0=0$；新高阶部分只追加，旧阶未重算 |
| 43640181602/1，$R_C=1/2000$ 成功 case | 同一 intrinsic 解析延拓的完整复矩形和四项三阶模上界；失败更大域不授 |
| 43664023495/1，complete-background-root-series | 已保存完整 signed 根背景与 repair/direction mean；(B.1)直接复用原系数 |
| 原 ac1/ed42 index 与自然 shard | 原物理 piece 的真实 knots、完整65/193三次系数与接缝；只临时读取，不重做目标 |
| 43682479300/1 的实际 domain gate | 原 true-root 圆盘确在上述复矩形内，固定 $\eta_0$、复系数盒与全mean身份一致 |

上述高根 native SHA256 为
ec702cffb8d1dcb25cdb01eaa89127b1f0044ae1cd3cee9e6e293e8165250480；
整复域 native 为6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f；
完整背景阶段为a6f89d9bf9523d04fd0534f7224b7a8bb3ecc8b0b201ffccf3839585df56b0c8。
它们是历史固定字节输入，依现行规则只在 Actions 临时恢复；
新的消费者只发布脚本、参数、run/SHA与必要的小结论。

即使(B.14)全部新数值门成功，也还没有得到真实参考的两列
$Y_j,n^{-1}Y_{j,T}$、正侧选定 Green/反射图或全部强算子常数。
正侧 growing IVP 的大范数不能代替真实两端图。
完整非径向耦合、实际接缝、两独立源和 physical even mean 均继续保留。

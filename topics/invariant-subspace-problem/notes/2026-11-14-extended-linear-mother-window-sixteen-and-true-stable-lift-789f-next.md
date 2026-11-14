# 原线性有限核的扩展母窗口：到 \(\exp(16d^3)\) 的真实稳定像提升

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：下述实际提升定理已证明。它扩展的是归一化有限物理核的母窗口；原低输出近似及其修复向量的范数不能自动沿用扩大后的参数。本稿未证明实际负图的角度衰减，也未证明 \(N=M\)。

## 0. 定理及与旧量词的区别

仍令

\[
 T=\sum_{i\ge0}(i+1)^{-2}N_i
 \quad\hbox{或}\quad
 T=\sum_{i\ge0}(i+1)^{-2}Y_i,\qquad
 M=\ker T,\quad N=\overline{BM},
\]
\[
 L_m=A_m+D_m,\quad
 D_m=\sum_{i\ge m}(i+1)^{-2}E_i,\quad d=2^m.
\]

全部头与位号均为原物理模型。对 \(m\ge10\) 和任意整数

\[
 1\le Q\le \exp(16d^3)
 \tag{0.1}
\]

存在有界线性映射

\[
 \boxed{
 \Lambda_{m,Q}:
 \ker L_m\cap\mathcal H_{\le Q}^{(m)}
 \longrightarrow N,\qquad
 \|\Lambda_{m,Q}k-k\|
       \le e^{-7d^4}\|k\|.
 }
 \tag{0.2}
\]

这里 \(\mathcal H_{\le Q}^{(m)}\) 只限制第 \(m\) 位之后的孔数；位置可无限，全部原头坐标保留。

[旧原线性逐头提升](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)
§6 的母范围为 \(Q\le e^{d^3/3}\)，误差为 \(e^{-75d^4}\)。
本稿扩大范围并明确换成 (0.2) 的余量，不把旧指数 \(75\) 一并迁移。
[准确稳定像插值](../results/R271-appendix-exact-stable-range-interpolation-and-norm-defect.md)
中别的低输出/修复条件也仍须按其自己的量词使用。

新增点是保留同一实际核的全部导数，并在升级时用两个真实头幂的 Legendre 和：
\[
 \eta_{p-1}R(1+b_pR)H_p(R)H_{p+1}(R).
\]
不再先丢掉实际头幂，再支付粗 \((2R)^{3\cdot2^p}\)。

## 1. 原已证输入与本稿的范数

沿用旧稿的原物理估计：

\[
 A_p^{2^p}=0,\qquad
 \|L_{p+1}-L_p\|\le52\eta_{p-1},
 \qquad \eta_{p-1}\le e^{-80\cdot16^p}\quad(p\ge5),
 \tag{1.1}
\]
\[
 \boxed{
 \|A_p^j\|\le6^j
       \exp[-\gamma(j-p)_+^4],
 \qquad \gamma=770/256.
 }
 \tag{1.2}
\]

差 \(K_p=L_{p+1}-L_p\) 只作用前 \(p+1\) 位，因此

\[
 [K_p,D_{p+1}]=0.
 \tag{1.3}
\]

这是以下合并导数预算的关键，不能把 \(D_p\) 与 \(D_{p+1}\) 混用。

对纯尾 \(D\) 定义

\[
 \mathcal U_R^{D}(f)
 =\sum_{j\ge0}\frac{R^j}{j!}\|D^jf\|,
 \qquad
 H_p(R)=\sum_{j<2^p}\frac{R^j}{j!}\|A_p^j\|.
 \tag{1.4}
\]

完整有限孔输入的相容右逆是旧稿 §2 的同一族 \(R_t'\)：
在新头为 \(p+1\)、输入孔数至多 \(Q'\)、最大阶 \(2^{p+1}\) 时，可取

\[
 R=512\sqrt{Q'+2^{p+1}+1}
      (p+1+Q'+2^{p+1}+2)^{3/2},
 \tag{1.5}
\]
\[
 D_{p+1}R_t'=R_{t-1}',\quad R_0'=I,\qquad
 \|R_t'f\|\le\frac{R^t}{t!}\mathcal U_R^{D_{p+1}}(f).
 \tag{1.6}
\]

它们与原新头 \(A_{p+1}\) 交换，并把尾层 \(\ell\) 送到 \(\ell+t\)。
(1.6) 是完整有限孔层上的已证不等式，没有假设输入只取某个 primitive 分量，也没有改为 bosonic 右逆。

## 2. 一步升级的同源精确导数

设

\[
 k\in\ker(A_p+D_p)\cap\mathcal H_{\le Q'}^{(p)},
 \quad z=2^p,\quad b_p=(p+1)^{-2}.
\]

旧核方程及交换性给

\[
 D_p^j k=(-A_p)^j k.
 \tag{2.1}
\]

又 \(D_{p+1}=D_p-b_pE_p\)，且 \(E_p^2=0\)、\(E_p\) 与 \(D_p,A_p\) 交换。因此对 \(j\ge1\)，

\[
 D_{p+1}^j k
 =(-A_p)^j k-jb_pE_p(-A_p)^{j-1}k.
 \tag{2.2}
\]

对 \(j=0\) 保恒等项并求和，得到

\[
 \boxed{
 \mathcal U_R^{D_{p+1}}(k)
 \le(1+b_pR)H_p(R)\|k\|.
 }
 \tag{2.3}
\]

这里仍是同一个原 \(k\)，没有逐层改选源。也立即有
\(D_{p+1}^{z+1}k=0\)。

置实际新残量

\[
 r=L_{p+1}k=K_pk.
\]

用 (1.3) 的真正交换和 (1.1)，

\[
 \boxed{
 \mathcal U_R^{D_{p+1}}(r)
 \le52\eta_{p-1}(1+b_pR)H_p(R)\|k\|.
 }
 \tag{2.4}
\]

定义完整新线性右逆

\[
 \mathcal R'
 =\sum_{j<2z}(-A_{p+1})^jR_{j+1}'.
 \tag{2.5}
\]

相容性、交换性及 \(A_{p+1}^{2z}=0\) 给
\(L_{p+1}\mathcal R'=I\)。
由 (1.6)，并使用 \(1/(j+1)!\le1/j!\)，

\[
 \|\mathcal R'f\|
 \le R H_{p+1}(R)\mathcal U_R^{D_{p+1}}(f).
\]

于是准确修复 \(k'=k-\mathcal R'r\) 满足

\[
 \boxed{
 L_{p+1}k'=0,\qquad
 \|k'-k\|
 \le52\eta_{p-1}R(1+b_pR)
       H_p(R)H_{p+1}(R)\|k\|.
 }
 \tag{2.6}
\]

归入新头不会增加新尾孔数；修复至多增加 \(2z\) 个新尾孔。因此
\(k'\in\mathcal H_{\le Q'+2z}^{(p+1)}\)。

## 3. 两个真实头幂的完整数值余量

令 \(\Theta=\log(6R)>0\)。由 (1.2)，

\[
 \frac{R^j}{j!}\|A_p^j\|
 \le \exp[j\Theta-\gamma(j-p)_+^4].
\]

精确 Legendre 最大值为

\[
 \sup_{t\ge0}(\Theta t-\gamma t^4)
 =C_\gamma\Theta^{4/3},
 \qquad
 C_\gamma=\frac3{4^{4/3}\gamma^{1/3}}<\frac13.
 \tag{3.1}
\]

故

\[
 \boxed{
 \log H_p(R)\le\log z+p\Theta+C_\gamma\Theta^{4/3},
 }
 \tag{3.2}
\]
\[
 \log H_{p+1}(R)
 \le\log(2z)+(p+1)\Theta+C_\gamma\Theta^{4/3}.
 \tag{3.3}
\]

因 \(R\ge1,b_p\le1\)，
\(\log R+\log(1+b_pR)\le2\Theta+\log2\)。
结合 (1.1)、(2.6) 得修复系数的对数至多

\[
 -80z^4+\log208+2\log z
 +(2p+3)\Theta+2C_\gamma\Theta^{4/3}.
 \tag{3.4}
\]

现在固定初值

\[
 m\ge10,\quad d=2^m,\quad
 1\le Q\le e^{16d^3}
\]

并在第 \(n\) 步取

\[
 p=m+n,\quad z=2^p,\qquad
 Q_n=Q+2z-2d.
 \tag{3.5}
\]

(1.5) 的 \(R\) 满足

\[
 R\le512(Q+5z)^2,
\]
\[
 \Theta\le\log3072+2\log Q+2\log(1+5z)
 \le32d^3+9+2\log(1+5z)
 \le33z^3.
 \tag{3.6}
\]

最后一步对全部 \(z\ge d\ge1024\) 成立。

由 \(C_\gamma<1/3\)，

\[
 2C_\gamma\Theta^{4/3}
 \le\frac23\,33^{4/3}z^4<71z^4.
 \tag{3.7}
\]

该纯数不等式可立方为
\(8\cdot33^4<27\cdot71^3\)。
另外，全部 \(p\ge10\) 都有

\[
 \log208+2\log z+(2p+3)33z^3\le z^4.
 \tag{3.8}
\]

在 \(p=10\)，主比例为 \(33\cdot23/1024<3/4\)，对数余项小于 \(1/4\)；
随着 \(p\) 增加，\((2p+3)/2^p\) 和对数余项与 \(16^p\) 的比都下降。

将 (3.7)、(3.8) 代回 (3.4)，得到完整且统一的一步界

\[
 \boxed{\|k_{n+1}-k_n\|\le e^{-8z^4}\|k_n\|.}
 \tag{3.9}
\]

没有遗漏新头两倍维数、全部输入导数、相容右逆的 factorial 或真实 carry。

## 4. 原 Hilbert 极限及进入稳定像

从任意
\(k_0\in\ker L_m\cap\mathcal H_{\le Q}^{(m)}\)
按 (2.5)–(2.6) 逐步定义 \(k_n\)。
每一步线性，且支撑满足 (3.5)。
由 (3.9)，

\[
 \|k_n\|\le2\|k_0\|,\qquad
 \sum_{n\ge0}\|k_{n+1}-k_n\|
 \le4e^{-8d^4}\|k_0\|
 \le e^{-7d^4}\|k_0\|.
 \tag{4.1}
\]

故有原 Hilbert 强极限 \(k_\infty\)。
因 \(L_{m+n}\to T\) 为算子范数收敛，\(Tk_\infty=0\)。

还必须确认它进入 \(N\)，不能只停在 \(M\)。
第 \(n\) 步差的原全部孔数至多

\[
 (p+1)+(Q_n+2z)\le Q+5z.
 \tag{4.2}
\]

因此对任意固定 \(c>0\)，

\[
 \sum_n\|e^{c\mathcal N}(k_{n+1}-k_n)\|
 \le2\|k_0\|\sum_n
       \exp[c(Q+5z)-8z^4]<\infty.
 \tag{4.3}
\]

初值也只有有限孔数，所以
\(k_\infty\in M\cap\operatorname{Dom}e^{c\mathcal N}\)
对每个 \(c>0\) 成立。
调用原已经证明的
\(M\cap X_3\subseteq N\)
（见
[R239 指数权核饱和](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)），
得到 \(k_\infty\in N\)。
这不依赖本稿待扩展的窗口，也没有循环使用 \(N=M\)。

定义 \(\Lambda_{m,Q}k_0=k_\infty\)，(4.1) 就是 (0.2)。

## 5. 后续可用范围

本定理允许在 \(Q\le e^{16d^3}\) 的完整有限物理核上作同一线性、原范数近恒等的稳定像提升。因而对归一化有限核向量，或仅额外支付 \(e^{O(d^3)}\) 范数的实际来源，(0.2) 仍有趋零余量。

它不自动扩大旧低输出投影定理的所有量词。例如先用一个可能达到 \(e^{c d^4}\) 的非最小高返回修复，再乘本稿 \(e^{-7d^4}\)，必须重新核净指数，不能引用旧 \(e^{-75d^4}\) 的余量。

同样，真实头逆芽半径
\(\rho_m=e^{-110\,8^{m-1}}=e^{-(55/4)d^3}\)
只是一个已证局部解析盘。只有在原 source/Schur 问题中另证实际成本至多一次 \(\rho_m^{-1}\) 时，本稿范围才足以覆盖它；振幅界平方会变成 \(\rho_m^{-2}\)，不能免费改成一次。当前完整高输入先消元后的角度/负图衰减仍未由本稿支付，普通 ISP 与 \(N=M\) 继续开放。


# R271 附录：分割前缀使联合三维块数的失真降为线性

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿优化[低三维块数全模式回缩](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md)的同一个分析/合成算子。先支付一段前缀的精确完整奇异值，再在剩余尾段上支付低块数 shear，得到不含总模式数的
$$
C\le32(1+R/m)
$$
界。原头、同源类、出生区间、真实高旗和闭源空间全部沿用前稿；分割点只用于估计范数。

这并不把 $C$ 变成统一常数，也未支付纯 $S_H^\dagger$ 费用或剩余实际源的高返回。将增长中的 $C$ 用于固定实际来源，还必须按原两费用/整流规则支付它。普通 Hilbert ISP 和原无权 $N=M$ 仍为 OPEN。

## 1. 同一个局部合成的精确完整奇异值

沿用前稿记号。第 $i$ 个原相邻对从
$\mathbb Cp_i\oplus^\perp\mathbb C^3$
到原物理块的合成 $U_i$，把四个外部正交单位向量送到
$h_i,\Omega_i,t_i,|11\rangle_i$。
其中 $h_i,t_i$ 为单位一孔向量且
$\langle h_i,t_i\rangle=-\delta_i$，
$$
\delta_i=\frac{a_i^2-b_i^2}{a_i^2+b_i^2},\qquad
\rho_i=\frac{2a_ib_i}{a_i^2+b_i^2},\qquad
a_i=(m+2i-1)^{-2},\quad b_i=(m+2i)^{-2}.
$$
因此在外部一孔基 $p_i,f_{i,1}$ 中
$$
U_i^*U_i=
\begin{pmatrix}1&-\delta_i\\-\delta_i&1\end{pmatrix};
$$
其余两个方向的 Gram 为 $I$。于是
$$
\boxed{
\|U_i\|=\sqrt{1+\delta_i},\qquad
\|U_i^{-1}\|=(1-\delta_i)^{-1/2},\qquad
\|U_i\|\|U_i^{-1}\|=\frac{a_i}{b_i}.}
\tag{1.1}
$$
这些是全部四维块的准确值，不把斜投影范数误作完整变基范数。

取 $0\le L\le N$，令
$$
A_L=\prod_{i=1}^{L}(1-\delta_i)^{-1/2},\qquad
B_L=\prod_{i=1}^{L}(1+\delta_i)^{1/2},\qquad
\Gamma_L=A_LB_L=\prod_{i=1}^{L}\frac{a_i}{b_i}.
\tag{1.2}
$$
空积取 $1$。前 $L$ 块的完整张量分析/合成范数分别恰为
$A_L,B_L$，没有限制其中的 $Q$ 块数。

原权还给一个简单的望远镜上界。令 $x=m+2i-1>1$，则
$$
\left(\frac{x+1}{x}\right)^2
\le\frac{x+1}{x-1}
$$
等价于 $x^2-1\le x^2$。所以
$$
\boxed{
\Gamma_L
=\prod_{i=1}^L\left(\frac{m+2i}{m+2i-1}\right)^2
\le\prod_{i=1}^L\frac{m+2i}{m+2i-2}
=\frac{m+2L}{m}.}
\tag{1.3}
$$

## 2. 前缀完整、后段低块数的联合估计

前稿的整个外部空间为
$\mathfrak B_N=\bigotimes_{i=1}^{N}(\mathbb Cp_i\oplus^\perp\mathbb C^3)$；
令 $\mathfrak B_{\le R}$ 为全部 $Q$ 块数不超过 $R$ 的闭子空间，
$\Pi_R$ 为其正交投影。
仍然使用同一个
$$
U_N=\bigotimes_{i=1}^{N}U_i,\qquad
\mathcal A_R=\Pi_RU_N^{-1},\qquad
\mathcal U_R=U_N|_{\mathfrak B_{\le R}}.
\tag{2.1}
$$
从未改变这个空间或这两个算子。

对分割点 $L$，记
$$
u_L=\min(R,N-L),\quad
\mathcal R_{>L}=\prod_{i=L+1}^{N}\rho_i^{-1},\quad
\mathcal S_{>L}=\sum_{i=L+1}^{N}\delta_i^2.
$$
前稿 §2 的 shear 证明应用于后 $N-L$ 个块，给出其全部
“$Q$ 块数至多 $u_L$”模式的分析/合成界
$$
\mathcal R_{>L}e^{\sqrt{u_L\mathcal S_{>L}}},
\qquad e^{\sqrt{u_L\mathcal S_{>L}}}.
\tag{2.2}
$$
为避免依赖这个引用的范围，再说明其算子事实：
后段 $K_{>L}=\sum_{i>L}\delta_i|p_i\rangle\langle f_{i,1}|$
降低该段 $Q$ 数，且在该数至多 $u_L$ 时
$\|K_{>L}\|^2\le u_L\mathcal S_{>L}$。
合成在原正交 $h_i,(t_i+\delta_i h_i)/\rho_i$ 基中为
一个收缩对角算子乘 $e^{-K_{>L}}$；
分析在原正交 $g_i,t_i$ 基中为
$e^{K_{>L}^*}$ 乘范数 $\mathcal R_{>L}$ 的对角算子。
取后段低块数行时，用
$\|\Pi_{\le u_L}e^{K_{>L}^*}\|
=\|e^{K_{>L}}\Pi_{\le u_L}\|$。
因此 (2.2) 对任意物理输入及整个所选外部直和成立。

全局 $\mathfrak B_{\le R}$ 是
“前 $L$ 块完全自由，后段 $Q$ 数至多 $u_L$”的闭子空间。
故合成可先在这个较大张量空间估计。
对分析，全局 $\Pi_R$ 的像已经在该后段低块数空间内，所以先取后段
$\Pi_{\le u_L}$ 不改变最终结果。再用完整前缀 (1.2)，得到
$$
\boxed{
\|\mathcal A_R\|
\le A_L\mathcal R_{>L}e^{\sqrt{u_L\mathcal S_{>L}}},
\qquad
\|\mathcal U_R\|
\le B_Le^{\sqrt{u_L\mathcal S_{>L}}}.}
\tag{2.3}
$$
这一推导仍对所有不同位置的低块数模式联合成立，不含 $\binom Nr$。

始终准确有 $\mathcal A_R\mathcal U_R=I$。
对每个 $L$ 的两个界相乘可得
$$
\boxed{
\|\mathcal A_R\|\|\mathcal U_R\|
\le \Gamma_L\mathcal R_{>L}
e^{2\sqrt{u_L\mathcal S_{>L}}}.}
\tag{2.4}
$$
因算子没有改变，可以对右侧取所有分割点的最小值。
这是优化同一个已付映射；不是把不同源空间的好界相加。

## 3. 同一个原远尾回缩的精确优化式

继续前稿参数
$$
q=N+s,\quad J=m+2N,\quad H=T+d+1,\quad P=s+R+d,
$$
$$
\theta=\frac{12HP}{J+1}<\frac12,\qquad
\kappa=\sqrt{\frac{1-\theta}{1-2\theta}}.
$$
仍只保留具有 $r\le R$ 个 $Q$ 块且满足
$$
b\ge0,\qquad \max(0,2r-1)\le t=s+r-b\le T
\tag{3.1}
$$
的整个真实远尾 $K_b(D_J)$。远尾分析范数不超过 $1$，完整短列合成范数不超过
$\kappa$。

对固定 $L$，(2.3) 因而给原组合分析和合成常数
$$
a(L)=A_L\mathcal R_{>L}e^{\sqrt{u_L\mathcal S_{>L}}},
\qquad
b(L)=\kappa B_Le^{\sqrt{u_L\mathcal S_{>L}}}.
$$
两者仍准确交织整个原 $A_m+D_m$，保持所有原左右可行链和高出生旗。
前稿 (3.1) 的有限三维容量 $2r$ 与标量玻色三角矩阵论证没有变化，
所以模型高出生域仍为零，$\widehat\lambda=\widehat\alpha$。

于是前稿的同一个闭原源空间 $\mathscr E_q$ 满足
$$
\boxed{
\lambda(r)\le C_{\rm split}\alpha(r)\quad(r\in\mathscr E_q),}
$$
$$
\boxed{
C_{\rm split}
=\kappa\min_{0\le L\le N}
\left\{\Gamma_L\mathcal R_{>L}
e^{2\sqrt{u_L\mathcal S_{>L}}}\right\}.}
\tag{3.2}
$$
同一个代数回缩 $\mathcal P_q$ 也满足
$$
\lambda(\mathcal P_qr)\le C_{\rm split}\alpha(r)
\quad(r\in\mathscr R_q).
\tag{3.3}
$$
具体地，对每个 $L$，先由分析得到
$\widehat\alpha\le a(L)\alpha$，再由合成得到
$\lambda\le b(L)\widehat\lambda=b(L)\widehat\alpha$，最后对 $L$ 取最小值。
没有假定最优链在各分割点相同。

同源三费用的双向比较、左候选支撑 $[q-T,q]$、真正 $\mathfrak M=B+LGL$
投影以及新 $H_2^\circ$ 能量身份全部继续适用。因此
$$
\boxed{
0\le
\left\langle(H_2^\circ)^{-1}
\mathcal R\mathcal G^\dagger\zeta(r),
\mathcal R\mathcal G^\dagger\zeta(r)\right\rangle
\le(C_{\rm split}^2-1)\alpha(r)^2
\quad(r\in\mathscr E_q).}
\tag{3.4}
$$

## 4. 与总前缀长度无关的线性块数界

取 $L=R$；前稿始终要求 $0\le R\le N$。
后段从原位号 $m+2R$ 开始，故同一个原权平方角度估计给
$$
\mathcal R_{>R}\le e^{2/(m+2R+1)},\qquad
\mathcal S_{>R}\le\frac3{m+2R+1}.
$$
又 $u_R\le R$，所以 (1.3)、(3.2) 得
$$
\boxed{
C_{\rm split}\le
\kappa\left(1+\frac{2R}{m}\right)
\exp\!\left[
\frac2{m+2R+1}
+2\sqrt{\frac{3R}{m+2R+1}}\right].}
\tag{4.1}
$$
这不含 $N$、模式总数或出生总数。

若 $m\ge47$ 且 $\theta\le1/8$，则
$\kappa\le\sqrt{7/6}$。
利用 $\log(7/6)\le1/6$、$2/(m+2R+1)\le1/24$ 及
$2\sqrt{3R/(m+2R+1)}\le\sqrt6<5/2$，前面指数因子的对数至多
$$
\frac1{12}+\frac1{24}+\frac52=\frac{21}{8}<\log16.
$$
最后一个严格不等式也由
$\log2\ge2/3$ 立即验证。
因此
$$
\boxed{
C_{\rm split}<16\left(1+\frac{2R}{m}\right)
\le32\left(1+\frac Rm\right).}
\tag{4.2}
$$
$R=0$ 时 (4.1) 给更好的原纯暗前缀常数；(4.2) 仍合法。

旧界为 $\kappa e^{2/(m+1)+2\sqrt{3R/(m+1)}}$。
(4.1) 在 $R/m$ 增大时改为线性量级，改善来自前缀全变基的精确奇异值和尾段低块数界分开支付。
没有假定整个 $N$ 块均近等距，更没有删除任何跨模式 Gram 项。

## 5. 可直接用于实际来源的范围

若把这一闭源空间用于原 $\mathfrak M$ 投影，
仍准确有
$$
\mu(p)^2\le\frac{C_{\rm split}}2
\bigl(\alpha(p)^2+\lambda_{\rm flat}(p)^2\bigr).
$$
因此在不交未来窗的顶部总度量方法中，可以使用 (4.1) 或 (4.2) 的这个新常数。
但当 $R$ 增长时，必须重新支付顶部左改变量、完整右改变量和同一源流的总费用；
仅有 (4.2) 不自动保证这些量趋零。

每个所选模式仍只有 (3.1) 的活动次数，故原候选左链仍支撑于 $[q-T,q]$。
固定 $w\in W$ 的角度估计也只将原失真替换为 $C_{\rm split}$，不免费删除这个因子。
本稿未将超过 $R$ 的模式、不同配对划分或原余空间中的真实高返回纳入结论。


## 6. 线性阶对这个完整前缀回缩已经不可改进

本节只检验前缀的同一个坐标映射 (2.1)，不把范数下界改写成原最小能量下界。

因为 $R\le N$，$\mathfrak B_{\le R}$ 包含
“前 $R$ 块完全自由、后 $N-R$ 块全取 $p_i$”的整个张量空间。
在这个子空间上，后段合成是单位张量 $\bigotimes_{i>R}h_i$。
取前段合成的最大奇异向量，得到
$$
\|\mathcal U_R\|\ge B_R.
\tag{6.1}
$$

对分析，取一个单位物理输入
$$
x=x_{\le R}\otimes\bigotimes_{i>R}g_i,
$$
其中 $x_{\le R}$ 是前段完整分析的最大奇异向量。
在 $U_i^{-1}g_i=\rho_i^{-1}p_i+
\delta_i\rho_i^{-1}f_{i,1}$ 中，只读取后段全 $p_i$ 的外部正交分量。
这个分量的前段完全自由，故全局 $\Pi_R$ 不删除其中任何部分。
它准确等于
$\mathcal R_{>R}(U_{\le R}^{-1}x_{\le R})
\otimes\bigotimes_{i>R}p_i$，所以
$$
\|\mathcal A_R\|\ge A_R\mathcal R_{>R}.
\tag{6.2}
$$
这给
$$
\|\mathcal A_R\|\|\mathcal U_R\|
\ge\Gamma_R\mathcal R_{>R}\ge\Gamma_R.
\tag{6.3}
$$

与 (1.3) 相反的逐项估计是
$$
\left(\frac{x+1}{x}\right)^2\ge\frac{x+2}{x}.
$$
它等价于 $1\ge0$。因此另一次望远镜给
$$
\boxed{
\Gamma_R\ge
\prod_{i=1}^R\frac{m+2i+1}{m+2i-1}
=\frac{m+2R+1}{m+1},\qquad
\|\mathcal A_R\|\|\mathcal U_R\|
\ge1+\frac{2R}{m+1}.}
\tag{6.4}
$$
与 (4.1) 在 $\kappa=1$ 时的前缀上界比较，$1+R/m$ 正是这个固定完整回缩的失真量级。

(6.4) 使用整个低 $Q$ 模式空间，未要求这些最大奇异向量同时满足
(3.1) 的源出生限制、原头可实现性或实际负图条件。
所以它既不是 $\lambda/\alpha$ 的匹配下界，也不是实际 $W$ 或新高能量的反例。
它排除的只是继续把同一个全模式前缀分析/合成乘积估成与 $R/m$ 无关的常数。

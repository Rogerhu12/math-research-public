# R217：慢 dyadic 符号的精确整函数阶与全方向预解增长

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d。

状态：完整证明。本稿在同轮的统一平方根整函数上界基础上，证明相同阶的全方向下界。包括任意逐位复相位和每位任取 $N_j$ 或 $Y_j$。主问题、正常湮灭态及未知限制上的稠密像仍未解决。

## 1. 陈述

记实际 UHF 代数中的归一化幂及 Cayley 项为
$$
N_j=A^{2^j}/d_j,
\qquad Y_j=N_j(I+N_j)^{-1}.
$$
每位任取 $X_j\in\{N_j,Y_j\}$，并取任意复系数
$$
|c_j|=(j+1)^{-2},\qquad T=\sum_{j\ge0}c_jX_j.
\tag{1.1}
$$
该级数按范数收敛。系数的相位没有任何正则性假设。

**定理。** 同时有以下统一界：
$$
\boxed{
\exp(\sqrt{|z|}/27)
\le\|e^{zT}\|
\le\exp(16\sqrt{|z|})
\quad(|z|\ge16).
}
\tag{1.2}
$$
以及
$$
\boxed{
|\lambda|^{-1}\exp\!\bigl(1/(256|\lambda|)\bigr)
\le\|(\lambda I-T)^{-1}\|
\le2|\lambda|^{-1}\exp\!\bigl(128/|\lambda|\bigr)
\quad(0<|\lambda|\le1/256).
}
\tag{1.3}
$$
下界与上界都对整个圆周统一成立，不是只在某个实射线上成立。

因此，算子值整函数 $z\mapsto e^{zT}$ 的阶恰为 $1/2$，相应型在 $1/27$ 与 $16$ 之间；$w\mapsto(I-wT)^{-1}$ 的整函数阶恰为 $1$，且每个复方向都有严格正的指数型下界。此处只作通常的范数增长陈述，不推断任何特定向量的局部增长率。

## 2. 本稿使用并扩展的统一上界

同轮完整稿
[R215](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md)
已由真实递推
$$
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j}
$$
证明：只要 $|b_j|\le(j+1)^{-2}$，逐位任选 $N_j/Y_j$，则
$$
\left\|\exp\!\left(z\sum_j b_jX_j\right)\right\|
\le e^{16\sqrt{|z|}}.
\tag{2.1}
$$
其单因子输入为
$$
\|X_j\|\le3,
\qquad \|X_j^n\|\le3^n e^{-16^j n^4}
\quad(n\ge2).
\tag{2.2}
$$
证明使用交换因子乘积，低指标取四次幂估计、高指标取普通指数估计；不删除进位。

同一个证明还适用于下文的混合模型：低于某个固定 $k$ 的项使用真实有限头矩阵 $N_j^{[k]}$ 或其 Cayley 项，所有 $j\ge k$ 的项使用纯消灭矩阵 $E_j$。理由如下。

1. 有限头项仍满足 (2.2)，其证明完全来自截断后的同一二进位递推。
2. 纯项满足 $\|E_j\|=1$、$E_j^n=0$ 对 $n\ge2$，故也满足 (2.2)。
3. 有限头项彼此交换，纯尾项彼此交换，头与尾作用于不同张量因子，所以整个族交换。

由此 (2.1) 对这些混合模型仍有同一常数16。对任意 $\lambda\ne0$，将 $T$ 乘单位复数并使用范数 Laplace 积分，得到
$$
\|(\lambda I-T)^{-1}\|
\le 2|\lambda|^{-1}e^{128/|\lambda|}.
\tag{2.3}
$$
同一上界适用于混合模型。积分证明给真实的左右逆，因此也同时证明这些算子的谱为 $\{0\}$。随后才能使用其在任何非零 $\lambda$ 处范数收敛的 Neumann–Laurent 级数。

## 3. 保真低头与纯尾之间的实际算子差

使用 R174 的等距含幺 $*$ 表示
$$
\pi_-:\mathfrak U\longrightarrow B(\ell^2(\mathbb N_0)).
$$
因此只需在孔表示中证明下界。下文省略 $\pi_-$，但始终是在同一 UHF 元素的等距表示中作范数测试；没有把边界向量当成 Haar 向量。

在该表示中，$E_j$ 消灭第 $j$ 位的孔，真空 $\Omega=e_0$ 被所有 $E_j$ 杀掉。有限头 $N_j^{[k]}$ 同样杀掉其低头真空。它的 Cayley 项也如此。

对每个整数 $k\ge1$，定义
$$
H_k=\sum_{j<k}c_jX_j^{[k]},
\qquad D_{\ge k}=\sum_{j\ge k}c_jE_j,
\qquad \widehat T_k=H_k+D_{\ge k}.
\tag{3.1}
$$
头与尾精确交换，$\|H_k\|\le6$、$\|D_{\ge k}\|\le2$，所以
$$
\|T\|\le6,\qquad \|\widehat T_k\|\le8.
\tag{3.2}
$$

真实链展开给
$$
\|N_j-N_j^{[k]}\|\le\alpha_k/\alpha_j\le\eta_{k-1}
\quad(j<k).
$$
逆差恒等式和两个逆的范数界3给
$$
\|Y_j-Y_j^{[k]}\|\le9\eta_{k-1}.
$$
另一方面，$\|N_j-E_j\|\le\eta_j$、$\|Y_j-E_j\|\le4\eta_j$。使用 $\sum_j(j+1)^{-2}<2$，得到
$$
\boxed{
\|T-\widehat T_k\|\le26\eta_{k-1}.
}
\tag{3.3}
$$
这同时覆盖任意相位与逐位混用 $N/Y$。没有假定原实际 $T$ 已是纯张量和。

给定 $r\ge1$，选
$$
k=k(r)=1+\lceil\log_{16}(r+1)\rceil.
$$
则
$$
\delta_r:=\|T-\widehat T_k\|
\le26e^{-770(r+1)}.
\tag{3.4}
$$
这个头长只有 $O(\log r)$。

## 4. 全复方向的半群下界

令 $r=|z|\ge16$、$M=\lceil\sqrt r\rceil$，选择位块
$$
I=\{M,M+1,\ldots,2M-1\}.
$$
有 $k(r)\le M$。例如
$k(r)\le2+\log_{16}(r+1)\le\sqrt r$ 对 $r\ge16$ 成立：在16处可直接检查，右减左的导数为正。

在每个 $j\in I$ 上，令
$$
\zeta_j=\frac{\overline{zc_j}}{|zc_j|},\qquad
\psi_j=\frac{\Omega_j+\zeta_je_j}{\sqrt2}.
$$
取单位张量向量 $\Psi$：块 $I$ 上使用 $\psi_j$，其余位全部使用孔真空。低头 $H_k$ 严格杀掉低头真空；块外的纯尾也杀掉各自真空。又因 $E_j^2=0$，
$$
\begin{aligned}
\langle e^{z\widehat T_k}\Psi,\Psi\rangle
&=\prod_{j\in I}\langle(I+zc_jE_j)\psi_j,\psi_j\rangle\\
&=\prod_{j\in I}\left(1+\frac{r}{2(j+1)^2}\right).
\end{aligned}
\tag{4.1}
$$
这里内积对第一变量线性，故 $\langle E_j\psi_j,\psi_j\rangle=\zeta_j/2$，相位准确抵消。

由于 $M\le\sqrt r+1\le5\sqrt r/4$，有 $j+1\le2M\le5\sqrt r/2$，所以每个因子至少为 $27/25$。利用
$\log(27/25)\ge2/27$，得到
$$
\|e^{z\widehat T_k}\|\ge\exp(2\sqrt r/27).
\tag{4.2}
$$

有界算子的 Duhamel 恒等式及 (3.2)—(3.4) 给
$$
\|e^{zT}-e^{z\widehat T_k}\|
\le r\delta_r e^{8r}
\le e^{-700r}.
\tag{4.3}
$$
最后 $e^{2\sqrt r/27}-e^{\sqrt r/27}\ge\sqrt r/27\ge4/27$，而 (4.3) 小于这个差。因此
$$
\boxed{\|e^{zT}\|\ge e^{\sqrt{|z|}/27}\quad(|z|\ge16).}
$$
结合 (2.1)，证明 (1.2)。

## 5. 全复方向的预解式下界

设 $r=|\lambda|^{-1}\ge256$，仍取 $k=k(r)$，并令
$$
L=\lfloor r/32\rfloor,\qquad I=\{L,L+1,\ldots,2L-1\}.
$$
有 $k\le L$。可由 $2+\log_{16}(r+1)\le r/32$（$r\ge256$）验证，后者在256处成立且差的导数为正。

取输入 $v_I$：块 $I$ 的孔全部占满，其余位全部真空；输出测试为全真空 $\Omega$。低头作用在这两个向量的低头真空上为零；纯尾中只有块 $I$ 的项可以参与从 $v_I$ 到 $\Omega$ 的路径。每个孔必须且只能消灭一次。因此
$$
\langle\widehat T_k^n v_I,\Omega\rangle
=\begin{cases}
L!\prod_{j\in I}c_j,&n=L,\\
0,&n\ne L.
\end{cases}
\tag{5.1}
$$
不同消灭次序都产生同一个复乘积，没有相位抵消。使用 §2 已确立的真实预解式和范数收敛 Laurent 级数，
$$
\left|\langle(\lambda I-\widehat T_k)^{-1}v_I,\Omega\rangle\right|
=r^{L+1}L!\prod_{j=L}^{2L-1}(j+1)^{-2}.
\tag{5.2}
$$
利用 $j+1\le2L$、$L!\ge(L/e)^L\ge(L/3)^L$ 以及 $L\le r/32$，得到
$$
\|(\lambda I-\widehat T_k)^{-1}\|
\ge r\left(\frac r{12L}\right)^L
\ge r2^L.
\tag{5.3}
$$
阶乘下界可直接由 $\sum_{j=1}^L\log j\ge\int_1^L\log x\,dx$ 得出。

两次 (2.3) 和实际逆差恒等式给
$$
\begin{aligned}
\|(\lambda I-T)^{-1}-(\lambda I-\widehat T_k)^{-1}\|
&\le4r^2e^{256r}\delta_r\\
&\le104r^2e^{-514r-770}<1.
\end{aligned}
\tag{5.4}
$$
因此实际预解式范数至少为 $r2^L-1\ge(r/2)2^L$。又 $L\ge r/64$，对 $r\ge256$ 有
$$
\frac r2\exp\!\left(\frac{\log2}{64}r\right)
\ge r e^{r/256}.
$$
这证明 (1.3) 的下界。每一步只使用 $|\lambda|$，所以该下界对所有复方向成立。

## 6. 增长阶与本题的确切含义

记 $F(z)=e^{zT}$，$G(w)=(I-wT)^{-1}$。谱为零保证 $G$ 为整个复平面上的算子值整函数。由 (1.2)，
$$
\limsup_{r\to\infty}\frac{\log\log\max_{|z|=r}\|F(z)\|}{\log r}
=\frac12.
$$
由 $(\lambda I-T)^{-1}=\lambda^{-1}G(1/\lambda)$ 与 (1.3)，
$$
e^{|w|/256}\le\|G(w)\|\le2e^{128|w|}
\quad(|w|\ge256),
$$
所以 $G$ 的阶为1，型严格正且有限。

这些结论比 R190 的逐阶超多项式下界更强，也与 R191 的零四次混合型相容：它们采用不同的增长标度。它们量化了这里指定慢符号的全空间病态逆，而没有证明其在任意未知不变限制上的相同下界。边界等距表示只给全空间 UHF 范数，不能搬运其测试向量到未知 Haar 子空间。

全方向的上下界也不说明每个向量的局部预解增长相同，不能据此排除或构造非零真闭不变子空间。仍需单独处理正常湮灭态、限制值域或实际核方程。

## 7. 依赖

- R174：负整数孔边界的等距含幺 UHF 表示。
- R208 的真实有限头差及同一逆差估计；这里 §3 已重写所需全部范数预算。
- 本轮 [R215](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md) §§2–4：统一整函数上界，其适用于保真头/纯尾混合模型的理由在 §2 完整列出。

本稿所有新下界均来自指定有限向量的精确矩阵元和付清代价的实际算子差，没有使用数值实验或未写出的极限交换。

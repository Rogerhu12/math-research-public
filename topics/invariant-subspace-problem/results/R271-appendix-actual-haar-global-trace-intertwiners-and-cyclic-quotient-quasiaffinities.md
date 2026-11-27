# R271 附录：原 Haar 加权平移到完整边界 T 的同源迹类交织与真实循环商

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本稿把[稀疏真核注入的全空间链](R271-appendix-sparse-kernel-injection-dense-backward-chain-and-global-trace-quasiaffinity.md)用于原 Haar 算子。目标是原完整 $T_N$ 或 $T_Y$，来源是原 Haar 加权平移；未使用 Haar 普通循环性，亦未假设其未知不变子空间被任何额外代数保持。

记目标空间为 $H=\ell^2(\mathbb N_0)$，原 Haar 空间为
$\mathcal H=L^2(\mathbb Z_2,\mu)$。两空间的向量不混同；以下 $e_0$ 始终属于目标 $H$。

## 1. 原 Haar 全整数幂的准确共同范数

在 $\mathcal H$ 上取原
$$
Af(y)=w(y)f(y-1),\qquad w(0)=0,\qquad
w(y)=\alpha_{v_2(y)}\ (y\ne0),
$$
其中
$$
-\log\alpha_j=
\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\quad \alpha_0=e^{-20},
$$
并令 $\eta_j=\alpha_{j+1}/\alpha_j\in(0,1)$。写
$$
\beta_0=1,\qquad
\beta_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)}
=\alpha_0^n\prod_{r\ge1}\eta_{r-1}^{\lfloor n/2^r\rfloor}.
\tag{1.1}
$$
则对每个整数 $n\ge0$
$$
\boxed{\|A^n\|=\beta_n=\|B^n\|.}
\tag{1.2}
$$

证明如下。任意长度 $n$ 的连续 $2$-adic 剩余类中，被 $2^r$ 整除者至少有
$\lfloor n/2^r\rfloor$ 个；每个 $\eta_{r-1}<1$，故 $A^n$ 的乘法权乘积至多
(1.1)。包含实际零点时其乘积为零，也满足该界。在 $y=n$ 处，所乘正整数恰是
$1,\ldots,n$，所有层的最少计数同时达到。选 $2^L>n$，则整个非空 clopen 集
$n+2^L\mathbb Z_2$ 上各因子的赋值与这些正整数相同，故本质上确实取到 $\beta_n$。
原 $B^n$ 的列权来自同样的整数区间，首列 $e_n$ 同时达到这些最少计数，证明其等式。

由已经付清的原 dyadic 公式
$$
-\log\beta_{2^j}
=100\,16^j-105\,8^j+(150j+25)2^j
$$
以及 $\|B\|=\alpha_0<1$，原四次界因此同时给
$$
\boxed{\|A^n\|\le e^{-cn^4}\quad(n\ge2),\qquad c=95/32.}
\tag{1.3}
$$
特别 $A$ 拟幂零。$w>0$ 除了 Haar 零测集 $\{0\}$，乘以 $w$ 单射且像稠密；
平移为酉算子，所以 $A,A^*$ 都单射且像稠密。

## 2. 同一目标链与实际迹类交织

固定前稿一次构造的链 $\{u_n\}_{n\ge0}\subset\mathcal E_\infty\subset H$：
$$
u_0=e_0,\qquad Tu_n=u_{n-1}\ (n\ge1),\qquad
P_0u_n=\mathbf1_{\{n=0\}}e_0,
$$
$$
\overline{\operatorname{span}}\{u_n:n\ge0\}=H,\qquad
\|u_n\|_\kappa\le e^{C_\kappa(n+1)^3}
\quad(\kappa\ge0).
\tag{2.1}
$$
目标 $T$ 和这条链不随来源 $y$ 改变。对 $y\in\mathcal H$ 定义
$$
\boxed{\mathscr K_y=\sum_{n\ge0}u_n\otimes(A^*)^ny:\mathcal H\to H.}
\tag{2.2}
$$
内积对第一变量线性，$(u\otimes v)x=\langle x,v\rangle u$。由 (1.3)、(2.1)，级数按迹范数绝对收敛，且
$$
\|\mathscr K_y\|_1\le C_{\rm tr}\|y\|,
\qquad
\|\mathscr K_y:\mathcal H\to X_\kappa\|\le C_\kappa'\|y\|.
\tag{2.3}
$$
其中常数只依赖已固定的链与尺度。它给出的是实际原物理输出：
$\mathscr K_y\mathcal H\subset\mathcal E_\infty$。

有限和的末项 $-u_N\otimes(A^*)^{N+1}y$ 趋零，因而
$$
\boxed{
T\mathscr K_y=\mathscr K_yA,\qquad
P_0\mathscr K_y=e_0\otimes y,\qquad
\mathscr K_y^*e_0=y.
}
\tag{2.4}
$$
特别
$$
\|y\|\le\|\mathscr K_y\|\le\|\mathscr K_y\|_1
\le C_{\rm tr}\|y\|.
\tag{2.5}
$$
每个非零 $y$ 都给非零实际紧交织。与前稿相同，任意固定 $0<c'<95/32$ 都有
$$
s_{n+1}(\mathscr K_y)\le C(c')e^{-c'n^4}\|y\|,
\tag{2.6}
$$
故它属于全部 Schatten 类 $\mathcal S_p$，$p>0$。

## 3. 不借 Haar 循环性的全 H 稠密像

这是新来源上不能用有限整数列回代代替的一步。

对 $v\in H$ 置
$$
c_n(v)=\langle v,u_n\rangle,\qquad
\Phi_v(A^*)=\sum_{n\ge0}c_n(v)(A^*)^n.
\tag{3.1}
$$
由 (1.3)、(2.1)，这是全 $\mathcal H$ 上按算子范数绝对收敛的真实算子，且
$$
\mathscr K_y^*v=\Phi_v(A^*)y.
\tag{3.2}
$$
若 $v\ne0$，链的全 $H$ 稠密性保证这些系数不全为零。令 $k$ 为最小非零系数的位置。准确因式分解为
$$
\Phi_v(A^*)=(A^*)^kV,\qquad
V=\sum_{n\ge0}c_{n+k}(v)(A^*)^n.
\tag{3.3}
$$
移去固定 $k$ 后仍只有三次系数增长，所以 $V$ 仍按范数绝对收敛，且其常项为非零 $c_k(v)$。

这里必须支付 $V$ 的实际可逆性。$V-c_k(v)I$ 是零常项 $A^*$ 多项式的范数极限。
各多项式因 $A^*$ 拟幂零而谱半径为零，并与极限交换；交换算子的谱半径次可加性给
$$
r(V-c_k(v)I)
\le\|V-c_k(v)I-p_N(A^*)\|\longrightarrow0.
$$
故 $V$ 可逆。(3.3) 中 $(A^*)^k$ 单射，所以 $\Phi_v(A^*)$ 单射。
于是对于每个 $y\ne0$，(3.2) 不可能在 $v\ne0$ 时为零，得到
$$
\boxed{\ker\mathscr K_y^*=\{0\},\qquad
\overline{\operatorname{Ran}\mathscr K_y}=H
\quad(y\ne0).}
\tag{3.4}
$$
没有把一个形式分母当作有界算子，没有使用未知的 $A$ 或 $A^*$ 普通循环性。

另一方面，实际核仍准确为
$$
\boxed{
\ker\mathscr K_y
=\mathcal C_y^\perp,\qquad
\mathcal C_y=\overline{\operatorname{span}}\{(A^*)^ny:n\ge0\}.
}
\tag{3.5}
$$
证明：由 (2.4)
$P_0T^n\mathscr K_yx=e_0\langle x,(A^*)^ny\rangle$；
反向用 (2.2) 的同一个绝对收敛级数。
因此 (3.4) 是无条件的，$\mathscr K_y$ 在整个 $\mathcal H$ 上单射则准确需要
$\mathcal C_y=\mathcal H$，不能倒置这两个范围。

## 4. 每个实际循环商都有单向迹类拟亲和

对 $y\ne0$，$\mathcal C_y$ 是原 $A^*$ 不变闭子空间。令
$$
A_y=P_{\mathcal C_y}A|_{\mathcal C_y}
=(A^*|_{\mathcal C_y})^*.
$$
这是原 $A$ 在商 $\mathcal H/\mathcal C_y^\perp$ 上的准确 Hilbert 实现。
由 $\mathcal C_y^\perp$ 的 $A$ 不变性，
$$
A_y^n=P_{\mathcal C_y}A^n|_{\mathcal C_y},
\qquad \|A_y^n\|\le\|A^n\|.
\tag{4.1}
$$
(3.5) 说明限制
$$
K_y=\mathscr K_y|_{\mathcal C_y}:\mathcal C_y\to H
$$
单射，并且其像等于 $\mathscr K_y\mathcal H$。结合 (2.4)、(3.4) 得
$$
\boxed{
K_y\text{ 是实际迹类拟亲和，}\qquad
TK_y=K_yA_y.
}
\tag{4.2}
$$
$\mathcal C_y$ 无限维：非零多项式 $p(A^*)$ 可分解为 $(A^*)^k$ 乘可逆算子，因而单射；
非零 $y$ 的有限轨道不能有多项式关系。

反向仍完全排除：
$$
\boxed{
X:H\to\mathcal C_y\text{ 有界且 }XT=A_yX
\quad\Longrightarrow\quad X=0.
}
\tag{4.3}
$$
确实，对有限物理孔输入 $f$，使用原固定的可闭右逆 $G$，而非新链的不可闭移级，
有 $T^nG^nf=f$，故
$$
Xf=A_y^nXG^nf.
$$
(4.1)、(1.3) 的四次衰减压过稀疏注入稿 (1.1) 的三次费用，右边趋零；
这类输入稠密，给 (4.3)。相同证明也排除全空间 $XT=AX$ 的非零有界解。

## 5. 原不变子空间与实际源范围仍须支付

任意真闭 $T$ 不变子空间 $L\subset H$ 给
$$
\mathcal M_{y,L}=\mathscr K_y^{-1}(L)
$$
作为原 $A$ 不变闭子空间。由 (3.4) 及 $L\ne H$，它一定不是整个 $\mathcal H$；
但本稿没有证明它非零。

特别，若 $\mathcal C_y=\mathcal H$，则 $\mathscr K_y$ 单射，且原 $A$ 单射，所以
$$
\mathscr K_y^{-1}(\ker T)
=\ker(\mathscr K_yA)=\{0\}.
\tag{5.1}
$$
因此原 $T$ 的已知无限维真核，不能仅凭这条稠密像紧交织直接拉回非零的 Haar 不变子空间。
对此前的 proper 单链 $U$ 或其他真实 $T$ 不变子空间，还需要同一来源的实际非零交点。

本稿新增的是原 Haar 全整数幂的共同范数、每个非零来源的全目标稠密迹类交织，以及每个实际循环商到完整 $T$ 的单向迹类拟亲和。它未证明 Haar 循环性、反向有界交织、Green 来源的除法费、$N=M$ 或普通 Hilbert ISP。

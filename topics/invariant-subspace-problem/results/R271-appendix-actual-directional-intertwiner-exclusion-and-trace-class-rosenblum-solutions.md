# R271 附录：实际慢边界到原移位的交织排除与反向迹类 Rosenblum 解

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本文始终在负整数边界 $H=\ell^2(\mathbb N_0)$ 上，$T$ 分别取原 $T_N,T_Y$，$B$ 是原加权后移，$S=B^*$。完整 carry 和 $Y$ 型完整 Cayley 逆均通过已发表的同一实际右逆保留。下列是两个原有界算子之间的结论，不是 Haar 表示与边界之间的交织。

## 1. 固定右逆、真空规范与准确迭代域

沿用[同一全尺度右逆](R271-appendix-single-actual-right-inverse-on-all-physical-exponential-scales.md)的记号
$$
X_\kappa=\left\{v:\sum_{q\ge0}e^{\kappa q}\|\mathsf P_qv\|<\infty\right\},
\qquad \mathscr E_\infty=\bigcap_{\kappa\ge0}X_\kappa,
$$
其中 $\mathsf P_q$ 是全部物理孔数投影。固定 $\lambda>2+2\log(3/2)$，只选该文的同一个 $\mathcal G_\lambda$。它满足
$$
T\mathcal G_\lambda=I\text{ 于 }X_\lambda,\qquad
\|\mathcal G_\lambda:X_{\kappa+\lambda}\to X_\kappa\|
\le e^{C_\lambda(1+\kappa)^2}.
\tag{1.1}
$$
令 $P_0=e_0\otimes e_0$，并固定
$$
G=(I-P_0)\mathcal G_\lambda.
\tag{1.2}
$$
约定 $(u\otimes v)x=\langle x,v\rangle u$，内积对第一变量线性。由于 $Te_0=0$，而 $I-P_0$ 在每个 $X_\kappa$ 上是压缩，(1.1) 对同一个 $G$ 原样成立，且
$$
P_0G=0.
\tag{1.3}
$$
这是固定一次的真空规范，不是按迭代阶数重选右逆。

对 $\kappa\ge0,n\ge1$，全部组合经过实际域
$$
X_{\kappa+n\lambda}\longrightarrow X_{\kappa+(n-1)\lambda}
\longrightarrow\cdots\longrightarrow X_\kappa.
$$
因此
$$
TG^n f=G^{n-1}f,\qquad T^nG^n f=f
\quad(f\in X_{\kappa+n\lambda}),
\tag{1.4}
$$
并有
$$
\|G^n f\|_\kappa
\le
\exp\!\left(C_\lambda\sum_{j=0}^{n-1}(1+\kappa+j\lambda)^2\right)
\|f\|_{\kappa+n\lambda}.
\tag{1.5}
$$
没有使用 $TG=GT$。

特别，若 $f\in H_{\le P}:=\bigoplus_{q=0}^P H_q$，则
$$
\boxed{
\|G^n f\|_\kappa
\le\sqrt{P+1}\,
\exp\!\left[
C_\lambda(1+\kappa+\lambda)^2n^3+(\kappa+n\lambda)P
\right]\|f\|.
}
\tag{1.6}
$$
$H_{\le P}$ 可以有无限整数支撑；(1.6) 仅使用 Cauchy–Schwarz 对有限个物理孔层求和。所有 $G^n f$ 都属于 $\mathscr E_\infty$。

## 2. 同一个原 B 的四次幂衰减

原权满足 $\|B\|=\alpha_0=e^{-20}<1$，并有
$$
d_j=\|B^{2^j}\|=e^{-\Lambda_j},\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.
\tag{2.1}
$$
这些是原权的实际范数：长度 $2^j$ 的任意连续整数段中，$v_2=k<j$ 的个数是 $2^{j-k-1}$，唯一的 $2^j$ 倍数之权不超过 $\alpha_j$；整数段 $1,\ldots,2^j$ 取等号。故
$d_j=\alpha_j\prod_{k<j}\alpha_k^{2^{j-k-1}}$，代入原权即得 (2.1)。亦见 [R109](R109-invariant-restriction-exact-quartic-type.md) 的同一 $d_j$ 公式；此处的整数段论证直接支付边界范数，不借未知限制的范数。

若 $n\ge2$ 且 $j=\lfloor\log_2n\rfloor\ge1$，则
$$
\Lambda_j\ge(100-105/2^j)16^j\ge\frac{95}{2}16^j
>\frac{95}{32}n^4.
$$
由 $\|B\|<1$，
$$
\boxed{\|B^n\|\le\|B^{2^j}\|\le e^{-cn^4},\qquad c=95/32,\quad n\ge2.}
\tag{2.2}
$$
同样 $\|S^n\|=\|B^n\|$。以下每个无穷和都是用 (1.6) 的三次正成本与 (2.2) 的四次负成本直接支付。

## 3. 一个方向的全部有界交织为零

**定理 1。** 若 $X\in B(H)$ 满足
$$
XT=BX,
\tag{3.1}
$$
则 $X=0$。

**证明。** 对任意固定 $f\in H_{\le P}$，(1.4) 和 (3.1) 给实际等式
$$
Xf=XT^nG^nf=B^nXG^nf.
$$
由 (1.6)、(2.2)，其范数不超过
$$
\sqrt{P+1}\,\|X\|\|f\|
\exp[-cn^4+C_\lambda(1+\lambda)^2n^3+n\lambda P],
$$
随 $n\to\infty$ 趋零。故 $X$ 在每个 $H_{\le P}$ 上为零。这些空间的并在原 $H$ 稠密，遂 $X=0$。证毕。

这里没有在未知 $M=\ker T$ 内寻找右逆，也没有将 $G$ 当作全 $H$ 上的有界右逆。证明只在每个固定有限物理孔输入上使用实际迭代域。

## 4. 反向 Rosenblum 算子的实际迹类像

记 $\mathcal S_1(H)$ 为迹类。固定同一个 $f\in H_{\le P}$ 和同一个 $y\in H$，定义
$$
\boxed{
K_{f,y}=\sum_{n=0}^\infty G^{n+1}f\otimes S^ny.
}
\tag{4.1}
$$
秩一项的迹范数是 $\|G^{n+1}f\|\,\|S^ny\|$。(1.6)、(2.2) 给
$$
\sum_{n\ge0}\|G^{n+1}f\|_\kappa\|S^ny\|<\infty
\qquad(\kappa\ge0).
\tag{4.2}
$$
其中 $n=0,1$ 仅是两个有限项。故 (4.1) 在原迹范数收敛，而且定义从 $H$ 到每个 $X_\kappa$ 的有界算子；所有尺度上的值是同一个 $H$ 极限。特别 $K_{f,y}H\subset\mathscr E_\infty$。

对 $N$ 项部分和直接计算，而不是形式交换无穷级数：
$$
T\sum_{n=0}^N G^{n+1}f\otimes S^ny
-\left(\sum_{n=0}^N G^{n+1}f\otimes S^ny\right)B
=f\otimes y-G^{N+1}f\otimes S^{N+1}y.
\tag{4.3}
$$
末项的迹范数由同一三次/四次估计趋零。因此
$$
\boxed{TK_{f,y}-K_{f,y}B=f\otimes y,\qquad P_0K_{f,y}=0.}
\tag{4.4}
$$
若 $f,y$ 均非零，(4.4) 本身证明 $K_{f,y}\ne0$。

所以 Rosenblum 算子
$$
\mathcal D_{T,B}:\mathcal S_1(H)\to\mathcal S_1(H),\qquad
\mathcal D_{T,B}(K)=TK-KB
$$
的实际像包含所有上述秩一源，因而在迹范数中稠密。最后一步仅使用有限整数支撑向量在 $H$ 稠密、有限秩算子在 $\mathcal S_1(H)$ 稠密；没有断言像闭或满射。

## 5. 反方向的闭迹类交织族及精确源恢复

取同一个规范右逆 $G$，令
$$
u_n=G^ne_0,\qquad
\boxed{L_y=\sum_{n=0}^\infty u_n\otimes S^ny\quad(y\in H).}
\tag{5.1}
$$
仍由 (1.6)、(2.2)，此级数在迹范数收敛，且
$$
\|L_y\|_1\le C_\lambda^{\rm tr}\|y\|,\qquad
L_y:H\to X_\kappa\text{ 有界}\quad(\kappa\ge0),
\tag{5.2}
$$
其中
$$
C_\lambda^{\rm tr}:=\sum_{n\ge0}\|G^ne_0\|\,\|B^n\|<\infty.
$$
由于 $Tu_0=0$、$Tu_n=u_{n-1}$，有限和的准确余项为
$$
T\sum_{n=0}^N u_n\otimes S^ny
-\left(\sum_{n=0}^N u_n\otimes S^ny\right)B
=-u_N\otimes S^{N+1}y.
$$
因此
$$
\boxed{TL_y=L_yB.}
\tag{5.3}
$$
(1.3) 给 $P_0u_n=0$（$n\ge1$）及 $u_0=e_0$，故
$$
\boxed{P_0L_y=e_0\otimes y,\qquad L_y^*e_0=y.}
\tag{5.4}
$$
于是
$$
\|y\|\le\|L_y\|\le\|L_y\|_1\le C_\lambda^{\rm tr}\|y\|.
\tag{5.5}
$$
特别，每个非零 $y$ 给一个实际非零迹类交织；$L_{e_0}e_0=e_0$。映射 $y\mapsto L_y$ 按上述内积约定是共轭线性，其像是 $\ker\mathcal D_{T,B}$ 内一个闭的、与共轭 Hilbert 空间等价的子空间。闭性直接由 (5.4)–(5.5)：若 $L_{y_j}$ 在迹范数收敛，则 $y_j=L_{y_j}^*e_0$ 在 $H$ 收敛，(5.2) 识别极限。这里没有分类 $\ker\mathcal D_{T,B}$ 的全部元素。

定理 1 与 (5.3) 的方向不同：前者排除 $XT=BX$，后者实际构造 $TX=XB$；没有从其中任一个交换等式推出另一个。

## 6. 同一个真实 W 上的精确限制

仍记
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
原 $BT=TB$ 保证 $BM\subset M$、$BN\subset N$，故 $B^nm\in N$ 对每个 $m\in M,n\ge1$ 成立。固定实际 $w\in W$，逐项有
$$
\langle m,S^nw\rangle=\langle B^nm,w\rangle=0
\quad(m\in M,n\ge1).
$$
把这一同源正交性代入已经收敛的 (4.1)、(5.1)，得到
$$
\boxed{
L_w|_M=e_0\otimes w,\qquad
K_{f,w}|_M=Gf\otimes w.
}
\tag{6.1}
$$
两式右端均作为从 $M$ 到 $H$ 的算子理解。特别 $L_wN=0$；因旧 [R187](R187-nonstandard-quotient-radical-and-boundary-dense-range-part.md) 已付 $e_0\in N$，有 $L_wM\subset N$。若 $w\ne0$，则
$$
L_ww=\|w\|^2e_0,\qquad L_w^*e_0=w.
\tag{6.2}
$$
这给出了一个实际紧交织的准确 $W$ 配对，而不是用任意闭包来源代替 $w$。

(6.1)–(6.2) 不矛盾：$L_w$ 在 $M$ 上只是把 $M/N$ 送入已有的真空线，它没有给 $G$ 保持 $N$、原 Green 图域的来源上界或 $W=0$。本文没有支付 $N=M$，也未把原边界构造搬到 Haar 未知不变子空间。新增的是原两型算子的方向性交织排除、同源迹类 Rosenblum 实际解、具有精确真空行恢复的反向闭交织族，以及该族在真实 $W$ 上的限制。

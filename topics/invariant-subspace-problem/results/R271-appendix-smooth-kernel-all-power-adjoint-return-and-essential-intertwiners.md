# R271：光滑核的全部固定幂实际伴随近右逆与交织本质范数

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与已有来源

在原负整数边界 $\mathcal H=\ell^2(\mathbb N_0)$ 上，保两种完整算子 $T=T_N,T_Y$，记
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathcal K=\overline{M\cap\mathcal E_\infty}.
$$
这里 $\mathcal E_\infty=\bigcap_{\lambda>0}X_\lambda$，
$$
\|u\|_{X_\lambda}=\sum_{p\ge0}e^{\lambda p}\|P_pu\|
$$
是原物理孔层的 $\ell^1$ 范数，不能换成另一个权 Hilbert 范数。

本稿使用已经证明的[同 G 光滑核创建修复](R271-appendix-boundary-smooth-kernel-creation-repair-and-faithful-calkin-corners.md)和[全部幂稠值](R271-appendix-smooth-kernel-core-all-powers-dense-range.md)。它们已付
$$
\mathbb Ce_0\subset\mathcal K\subset N\subset M,\qquad B\mathcal K\subset\mathcal K.
$$
本稿不重新证明或重新计算这些旧结论。

**新结论。** 对每个固定整数 $r\ge1$，有准确归一化幂 $S_{j,r}$，使其在 $\mathcal K$ 上的真实限制 $V_{j,r}$ 满足
$$
V_{j,r}\xrightarrow{\rm SOT}0,\qquad
V_{j,r}V_{j,r}^*\xrightarrow{\rm SOT}I_{\mathcal K},
\qquad \|V_{j,r}\|\le1. \tag{1}
$$
因此每个 $u\in\mathcal K$ 都有**实际 Hilbert 伴随**给出的序列
$$
v_j=V_{j,r}^*u,\qquad
\|v_j\|\le\|u\|,\qquad v_j\rightharpoonup0,\qquad V_{j,r}v_j\to u. \tag{2}
$$
不要求 $P_{\mathcal K}$ 保持任何 $X_\lambda$ 或 $\mathcal E_\infty$。

(1) 同时适用于全边界 $\mathcal H$，并传给 $\mathcal H$ 或 $\mathcal K$ 的任意闭 $B^r$ 不变子空间之商。以这些空间之一为定义域、以任意实际边界 $B^r$ 不变子商为终点的有界交织 $X$，均有
$$
\boxed{\|X\|_{\rm ess}=\|X\|.} \tag{3}
$$
这个等式保持所有有限矩形放大。特别是这些交织空间没有非零紧算子，$\{(B|_{\mathcal K})^r\}'$ 没有非零紧算子。

这是边界光滑核及指定商空间的结论。它没有证明未知 $M$ 的限制具有 (1)，没有证明 $\mathcal K=N$ 或 $N=M$。

## 2. 固定二进位支撑的原归一化幂

沿用原边界身份
$$
N_j=B^{2^j}/d_j,\qquad \|N_j\|=1,\qquad
\|N_j-E_j\|\le\eta_j,\qquad \eta_j\to0,
$$
其中 $E_j$ 消去第 $j$ 位的孔，
$$
E_jE_j^*=P_{j,0},\qquad E_j\xrightarrow{\rm SOT}0,\qquad
P_{j,0}\xrightarrow{\rm SOT}I.
$$
这些是完整 carry 的已付比较，不用纯模型替代 $B$。

写固定整数
$$
r=\sum_{b\in J(r)}2^b,\qquad p=|J(r)|.
$$
置
$$
c_{j,r}=\prod_{b\in J(r)}d_{j+b},\qquad
S_{j,r}=\prod_{b\in J(r)}N_{j+b}
=\frac{(B^r)^{2^j}}{c_{j,r}},\qquad
F_{j,r}=\prod_{b\in J(r)}E_{j+b}^*.
\tag{4}
$$
所有乘积只有固定的 $p$ 项。由逐项相减，
$$
\|S_{j,r}\|\le1,\qquad
\|S_{j,r}-F_{j,r}^*\|
\le\sum_{b\in J(r)}\eta_{j+b}\to0. \tag{5}
$$
又
$$
F_{j,r}^*F_{j,r}=\prod_{b\in J(r)}P_{j+b,0}\xrightarrow{\rm SOT}I.
\tag{6}
$$
对有限整数支撑，$F_{j,r}^*$ 最终消掉每个向量，故 $F_{j,r}^*\to0$ 强。由 (5)，$S_{j,r}\to0$ 强。$F_{j,r}\to0$ 弱，且由 (6)，$\|F_{j,r}u\|\to\|u\|$。

在全空间取 $F_{j,r}u$，(5)–(6) 已给
$$
S_{j,r}F_{j,r}u\to u,\qquad \|F_{j,r}u\|\le\|u\|. \tag{7}
$$

## 3. 同一 G 对固定多位创建的一次修复

前述创建定理已经对每个固定 $\lambda>0$ 支付
$$
\|E_j^*\|_{X_\lambda\to X_\lambda}\le e^\lambda,\qquad
\|[T,E_j^*]\|_{X_\lambda\to X_\lambda}\le\delta_{j,\lambda},
\qquad \delta_{j,\lambda}\to0.
\tag{8}
$$
可沿用其完整上界
$$
\delta_{j,\lambda}
=a_j+104\sum_{L\ge j}\sqrt{2L+3}\,
e^{\lambda(L+2)}e^{-770\,16^{L-1}}.
$$
这里保全部原 $N/Y$ carry，并非只取 $D$ 的交换子。

由有限 Leibniz 恒等式及 (8)，
$$
\|[T,F_{j,r}]\|_{X_\lambda\to X_\lambda}
\le e^{(p-1)\lambda}\sum_{b\in J(r)}\delta_{j+b,\lambda}.
\tag{9}
$$
这一步使用的是带物理域范数的有界估计；没有把强渐近交换延伸为对变化向量或无限高位乘积的结论。

固定原右逆 $G$ 和已付 $\lambda_*>\kappa_0$，有
$$
TGf=f\quad(f\in\mathcal E_\infty),\qquad
G\mathcal E_\infty\subset\mathcal E_\infty,\qquad
\|Gf\|\le C_*\|f\|_{X_{\lambda_*}}.
$$
对 $u\in M\cap\mathcal E_\infty$ 定义
$$
k_{j,r}(u)=F_{j,r}u-G[T,F_{j,r}]u. \tag{10}
$$
所有输入均在原 $G$ 的已付定义域。由 $Tu=0$ 和 $TG=I$，
$$
k_{j,r}(u)\in M\cap\mathcal E_\infty\subset\mathcal K.
$$
(9) 给
$$
\|k_{j,r}(u)-F_{j,r}u\|
\le C_*e^{(p-1)\lambda_*}
\left(\sum_{b\in J(r)}\delta_{j+b,\lambda_*}\right)
\|u\|_{X_{\lambda_*}}\to0.
\tag{11}
$$
于是
$$
\limsup_j\|k_{j,r}(u)\|\le\|u\|,\qquad
k_{j,r}(u)\rightharpoonup0,\qquad
S_{j,r}k_{j,r}(u)\to u. \tag{12}
$$
最后一式由 (5)–(7) 和 $\|S_{j,r}\|\le1$ 得到。

(10) 的来源是原同一个 $u$ 与同一个 $G$；它没有在未知粗糙核向量上无条件施加 $G$。

## 4. 从核心修复得到全部空间的实际伴随近右逆

记 $V_j=S_{j,r}|_{\mathcal K}$，这是 $(B|_{\mathcal K})^r$ 的真实多项式，且为压缩范数不超过 1 的算子。

对 $0\ne u\in M\cap\mathcal E_\infty$，(12) 给
$$
\|u\|^2
=\lim_j|\langle V_jk_{j,r}(u),u\rangle|
\le \liminf_j\|k_{j,r}(u)\|\,\|V_j^*u\|.
$$
更明确地，将左边的收敛标量除以
$\|k_{j,r}(u)\|\le\|u\|+o(1)$，可得
$$
\liminf_j\|V_j^*u\|\ge\|u\|.
$$
由 $V_j$ 为压缩，反向不等式成立，故
$$
\|V_j^*u\|\to\|u\|. \tag{13}
$$
令 $A_j=I-V_jV_j^*$。则 $0\le A_j\le I$，并且
$$
\|A_ju\|^2\le\langle A_ju,u\rangle
=\|u\|^2-\|V_j^*u\|^2\to0.
$$
先在上述稠密核心成立，再由 $\|A_j\|\le1$ 延伸到全部 $\mathcal K$，得到 (1)。

对任意 $u\in\mathcal K$，取 $v_j=V_j^*u$。因为 $V_j\to0$ 强，$v_j\to0$ 弱；由 (1)，$V_jv_j\to u$。这证明 (2)，完全没有要求 $v_j\in\mathcal E_\infty$。

全 $\mathcal H$ 的相同论证用 (7) 即可，不需核修复。

注意 (2) 对应的是归一化幂 $(B^r)^{2^j}/c_{j,r}$。若改成未归一化的 $B^{r2^j}$，原像是 $v_j/c_{j,r}$；本稿没有给它统一有界的费用。

## 5. 实际商上的身份

令 $\mathcal V$ 为 $\mathcal H$ 或 $\mathcal K$，$\mathcal L\subset\mathcal V$ 为任意闭 $B^r$ 不变子空间，$P=P_\mathcal L$、$Q=I-P$。其实际商由 $\mathcal L^\perp$ 实现。因 (4) 为 $B^r$ 的多项式，
$$
QS_j^{\mathcal V}P=0.
$$
商算子的同一个归一化幂是
$$
\widetilde S_j=QS_j^{\mathcal V}Q|_{Q\mathcal V}.
$$
由不变性及其伴随式，
$$
\begin{aligned}
\widetilde S_j\widetilde S_j^*
&=QS_j^{\mathcal V}Q(S_j^{\mathcal V})^*Q\\
&=QS_j^{\mathcal V}(S_j^{\mathcal V})^*Q
\xrightarrow{\rm SOT}Q.
\end{aligned}
\tag{14}
$$
同时 $\widetilde S_j\to0$ 强且范数不超过 1。所以每个这样的商都继承 (1)–(2)。商投影无需保持任何物理光滑域。

(14) 只对完整 $\mathcal V$ 的商作此断言，不把它转写成任意未知限制的同一性质。

## 6. 全部有界交织的本质范数

设定义域 $\mathcal V$ 为上一节任一空间，$A_\mathcal V$ 为其实际 $B^r$ 算子。设终点 $\mathcal U$ 为任意边界的实际 $B^r$ 不变限制或子商，$A_\mathcal U$ 为相应算子。由于不变限制与商上的多项式都是原多项式的相应压缩，
$$
R_j^\mathcal U=A_\mathcal U^{2^j}/c_{j,r},\qquad
\|R_j^\mathcal U\|\le1.
$$
定义域归一化幂记为 $R_j^\mathcal V$。若
$$
A_\mathcal U X=XA_\mathcal V,
$$
则
$$
R_j^\mathcal U X=XR_j^\mathcal V. \tag{15}
$$

任取 $u\in\mathcal V$ 与紧算子 $C:\mathcal V\to\mathcal U$，置
$$
v_j=(R_j^\mathcal V)^*u.
$$
已付 $\|v_j\|\le\|u\|$、$v_j\rightharpoonup0$ 和
$R_j^\mathcal Vv_j\to u$。紧性给 $Cv_j\to0$，于是
$$
R_j^\mathcal U(X+C)v_j
=XR_j^\mathcal Vv_j+R_j^\mathcal UCv_j\longrightarrow Xu.
$$
故
$$
\|Xu\|\le\|X+C\|\|u\|.
$$
取单位向量上确界，再对所有紧 $C$ 取下确界，得到
$$
\|X\|\le\inf_{C\ {\rm compact}}\|X+C\|=\|X\|_{\rm ess}.
$$
反向不等式总成立，证明 (3)。

在源和终点上作有限直和，使用同一个 $j$ 和归一化常数，所有步骤逐分量成立；向量范数仍有准确的上界。因此矩形矩阵交织的范数与其本质范数也相等。这里是交织算子空间的完全等距结论，不宣称任意外部 C* 代数都由此谱忠实。

## 7. 对原未知 M 的准确作用

若紧算子 $C:M\to M$ 与 $(B|_M)^r$ 交换，则
$$
C|_\mathcal K:\mathcal K\to M
$$
是上一节允许的紧交织，因而
$$
\boxed{C\mathcal K=0.} \tag{16}
$$
不要求预先知道 $C\mathcal K\subset\mathcal K$。

[R226A](R226-appendix-finite-rank-commutant-and-copy-projection.md)已经证明：当 $r=1$ 时，原 $M$ 的有限秩交换子准确为 $e_0\otimes w$、$w\in W=M\ominus N$，紧交换子均在交换代数根基中；它也已杀掉标准有限块纠错构造类。本文补充的是整个指定光滑核闭包上的 (1)、全部固定 $r$ 及上述所有交织的本质范数，不把旧 R226A 结论重新登记为新定理。

因为 $\mathcal K\subset N$，未知秩一 $e_0\otimes w$ 本来就杀掉 $\mathcal K$，所以 (16) 尚不排除 $W$。若以后确实证明 $\mathcal K=M$，才可把本稿的无紧交换子结论应用到全部 $M$ 并结合 R226A 得到 $N=M$；这个等号仍未支付。

固定幂 $B^r$ 的二进位归一化是证明的必要来源。本稿不将 (1)–(3) 外推到任意非恒定解析芽，不以全空间稠密或强渐近交换替代真实定义域。普通复 Hilbert 不变子空间问题仍未完成。

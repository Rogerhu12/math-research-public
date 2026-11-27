# R271 附录：原光滑核闭包的高位创建修复与忠实 Calkin 表示

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：本文的实际修复、强* 渐近交换和角代数结论已证明；不把光滑核闭包与 $N$ 或 $M$ 认同。

始终使用原负整数边界模型的 $T=T_N$ 或完整 $T_Y$、$B$ 及物理孔分级。令
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathscr E_\infty=\bigcap_{\kappa\ge0}X_\kappa,\qquad
K_\infty=\overline{M\cap\mathscr E_\infty},
\tag{1}
$$
所有闭包都是原 Hilbert 闭包。旧实际输入给
$$
\mathbb C e_0\subset K_\infty\subset N\subset M.
\tag{2}
$$
没有假定 $K_\infty=N$，也没有假定 $N=M$。

本稿使用[同一全尺度实际右逆](R271-appendix-single-actual-right-inverse-on-all-physical-exponential-scales.md)
的固定 $\mathcal G=\mathcal G_{\lambda_*}$，$\lambda_*>\kappa_0$，
以及[同一修正和有限孔行](R271-appendix-same-right-inverse-smoothing-correction-and-actual-kernel-cut-flux.md)。
特别
$$
T\mathcal G=I\quad\hbox{于 }X_{\lambda_*},\qquad
\|\mathcal G v\|\le C_*\|v\|_{\lambda_*},\qquad
\mathcal G\mathscr E_\infty\subset\mathscr E_\infty.
\tag{3}
$$
这里 $C_*<\infty$ 只依赖这一固定构造。

## 1. 真正负边界上的高位算子

令 $E_j$ 为第 $j$ 位的物理湮灭，$E_j^*$ 为物理创建。
原真实归一幂满足
$$
\mathsf N_j=B^{2^j}/d_j
=E_j+\eta_j E_j^*\mathsf N_{j+1},
\qquad \|\mathsf N_{j+1}\|=1,
\qquad \|\mathsf N_j-E_j\|\le\eta_j\longrightarrow0.
\tag{4}
$$
定义
$$
X_j=E_j+E_j^*.
\tag{5}
$$
$X_j$ 是自伴酉算子。这里使用的是负整数边界的翻转 $X_j$，
不是 Haar 表示中的乘法 $J_j$。

在当前边界 Hilbert 空间中，
$$
E_j\longrightarrow0\quad\hbox{强},\qquad
X_j\longrightarrow0\quad\hbox{弱}.
\tag{6}
$$
证明只需先取有限整数支撑向量：充分高的第 $j$ 位都为零，
故 $E_j$ 在此输入为零，而 $X_j$ 将其送到与任一固定有限支撑测试正交的坐标。
再用 $\|E_j\|=\|X_j\|=1$ 和稠密性延拓。
$E_j^*$ 不强趋零。

## 2. 全部局部 carry 的同源创建修复

把原算子写成
$$
T=D+\sum_{L\ge1}K_L,\qquad
D=\sum_{i\ge0}a_iE_i,\qquad a_i=(i+1)^{-2}.
\tag{7}
$$
这里 $K_L$ 是原真实有限头的相邻差，仅作用于前 $L+1$ 位，并有
$$
\|K_L\|\le52e^{-770\,16^{L-1}}.
\tag{8}
$$
这是已付的完整局部展开；$Y$ 型的全部 Cayley 逆已经包含其中。
单个位的有限头为纯湮灭，故 (7) 从 $L=1$ 开始。

局部算子最多改变 $L+1$ 个孔。对每个 $\lambda\ge0$，
按同一个输入孔层先作至多 $2L+3$ 个输出孔层的 Cauchy--Schwarz，再对输入层求和，得到
$$
\|K_L\|_{X_\lambda\to X_\lambda}
\le\sqrt{2L+3}\,e^{\lambda(L+1)}\|K_L\|.
\tag{9}
$$
创建满足 $\|E_j^*\|_{X_\lambda\to X_\lambda}\le e^\lambda$。
当 $L<j$ 时，$K_L$ 与 $E_j^*$ 精确交换。
而
$$
[D,E_j^*]=a_j(E_jE_j^*-E_j^*E_j)
$$
保孔，括号中算子在每个 $X_\lambda$ 上的范数为 $1$。

所以对 $j\ge1$，完整实际交换子满足
$$
\boxed{
\|[T,E_j^*]\|_{X_\lambda\to X_\lambda}
\le\delta_{j,\lambda}:=
a_j+
104\sum_{L\ge j}\sqrt{2L+3}\,
e^{\lambda(L+2)}e^{-770\,16^{L-1}}.
}
\tag{10}
$$
不但 $\delta_{j,\lambda}\to0$，而且
$$
\sum_{j\ge1}\delta_{j,\lambda}<\infty:
$$
第二项交换两个非负求和后只增加因子 $L$。
这些估计同时证明交换子保持 $\mathscr E_\infty$。

取同一个 $u\in M\cap\mathscr E_\infty$，定义
$$
k_j(u)=E_j^*u-\mathcal G[T,E_j^*]u.
\tag{11}
$$
每一项都在原 $\mathscr E_\infty$ 内。由于 $Tu=0$ 及 (3)，
$$
Tk_j(u)=[T,E_j^*]u-[T,E_j^*]u=0.
$$
故
$$
\boxed{
k_j(u)\in M\cap\mathscr E_\infty,\qquad
\|k_j(u)-E_j^*u\|
\le C_*\delta_{j,\lambda_*}\|u\|_{\lambda_*}.
}
\tag{12}
$$
(12) 在原实际核中修复同一个创建输入；并且对固定 $u$，全部误差范数可和。
没有先对某个纯尾模型投影，也没有使用未定义的全 $H$ 右逆。

## 3. 光滑核闭包的投影确实渐近交换

令 $P=P_{K_\infty}$、$Q=I-P$。
原 $B$ 保持每个 $X_\lambda$，并且与 $T$ 交换。
因此 $B(M\cap\mathscr E_\infty)\subset M\cap\mathscr E_\infty$，
由有界性可知 $K_\infty$ 对 $B$ 不变。
式 (4) 遂给
$$
Q\mathsf N_jP=0,\qquad
\|QE_jP\|\le\eta_j,\qquad
\|PE_j^*Q\|\le\eta_j.
\tag{13}
$$

另一方面，对 $u\in M\cap\mathscr E_\infty$，
(12) 给 $\|QE_j^*u\|\to0$。
因为这些 $u$ 在 $K_\infty$ 稠密，且所有 $QE_j^*P$ 的范数不超过 $1$，
$$
QE_j^*P\longrightarrow0\quad\hbox{强}.
\tag{14}
$$
合 (13)--(14) 得 $[P,E_j^*]\to0$ 强。
由 (6)，$[P,E_j]\to0$ 强对这个固定有界 $P$ 也成立。
因此
$$
\boxed{
[P,X_j]\longrightarrow0\quad\hbox{强*}.
}
\tag{15}
$$
最后一步的伴随没有任何换极限：$P,X_j$ 自伴使
$[P,X_j]^*=-[P,X_j]$。

(15) 只证明当前的 $P_{K_\infty}$。
对 $P_N$ 或 $P_M$ 使用 (14) 需要尚未证明的相应光滑核密度，
本稿没有作这一步。

## 4. 原边界的忠实 Calkin 代数及其全部角

在当前同一个边界表示上定义
$$
\mathfrak E_X=\{A\in B(H):[A,X_j]\longrightarrow0\ \hbox{强*}\}.
\tag{16}
$$
它是含单位 $C^*$ 代数。事实上
$$
[AB,X_j]=A[B,X_j]+[A,X_j]B,
\qquad
[A,X_j]^*=-[A^*,X_j],
$$
分别支付积与伴随；范数闭性由
$\|[A-A_n,X_j]\|\le2\|A-A_n\|$ 得到。

令 $\mathfrak U$ 为原物理 UHF 代数。
每个有限物理张量算子与充分高的 $X_j$ 精确交换，
所以 $\mathfrak U\subset\mathfrak E_X$。
结合 (15)，
$$
\boxed{
C^*(\mathfrak U,P_{K_\infty})\subset\mathfrak E_X.
}
\tag{17}
$$

对 $A\in\mathfrak E_X$、固定单位向量 $\xi$ 及任意紧算子 $C$，
(6) 给 $CX_j\xi\to0$ 范数，而实际强交换给
$AX_j\xi-X_jA\xi\to0$ 范数。因此
$$
\|A+C\|\ge\limsup_j\|(A+C)X_j\xi\|=\|A\xi\|.
$$
对单位 $\xi$ 取上确界并对紧 $C$ 取下确界，得到
$$
\boxed{
\|A\|_{\rm ess}=\|A\|,\qquad
\mathfrak E_X\cap\mathcal K(H)=\{0\}.
}
\tag{18}
$$
Calkin 商在 $\mathfrak E_X$ 上是忠实含单位 $*$ 同态，
因而也保持谱和正性：
$$
\sigma_{\rm ess}(A)=\sigma(A).
\tag{19}
$$

全部投影角也保留这个结论。
若 $P_1,P_2\in\mathfrak E_X$ 为投影、$A\in P_2\mathfrak E_XP_1$，
则把 $A:P_1H\to P_2H$ 零延拓可知
$$
\|A:P_1H\to P_2H\|_{\rm ess}=\|A\|.
\tag{20}
$$
当 $P_1=P_2\ne0$ 时，相应角的谱在其实际 Hilbert 像空间与 Calkin 代数中相同。
在有限放大上用 $\operatorname{diag}(X_j,\ldots,X_j)$ 重复同一证明，
又得完全等距。
所以新结论实际覆盖 $K_\infty$、$K_\infty^\perp$ 的这些角，
而不是只覆盖全空间的一个 UHF 表达式。

$K_\infty$ 非零，因为包含 $e_0$；它为真子空间，因为 $T\ne0$。
故 $P$ 与 $I-P$ 均为非零投影，(18) 还说明二者的像空间都无限维。
这里的忠实性不需要对未知普通 Haar 不变空间作假设。

## 5. 同一伴随来源还适用于这个更大的垂直空间

[同一实际伴随域定理](R271-appendix-same-right-inverse-adjoint-critical-physical-source-and-exact-range.md)
给出了 $D(\mathcal G^*)$ 的临界来源预算，以及
$\mathcal G^*\mathscr E_\infty\subset\mathscr E_\infty$。
其实际值域证明还可准确扩成
$$
\boxed{
D(\mathcal G^*)\cap K_\infty^\perp=\operatorname{Ran}T^*.
}
\tag{21}
$$
这里右侧依然是实际值域。

补齐此处的理由：对每个有限整数支撑 $f$，
原规范有限三角解 $Jf$ 满足
$$
\mathcal Gf-Jf\in M\cap\mathscr E_\infty\subset K_\infty.
$$
所以若 $w\in K_\infty^\perp\cap D(\mathcal G^*)$，
则
$$
\langle\mathcal G^*w,f\rangle=\langle w,Jf\rangle.
$$
又 $e_0\in K_\infty$，所以 $w_0=0$。
有限三角回代于是表明同一个 $\mathcal G^*w\in H$
是唯一形式解 $T^*h=w$；$T^*$ 有界把它变成实际 Hilbert 等式。
反向包含与 $\mathcal G^*T^*=I$ 仍直接来自 $T\mathcal G=I$。
这证明 (21)。

令 $I=M^\perp=\overline{\operatorname{Ran}T^*}$。
合 $T^*$ 及 $\mathcal G^*$ 保持 $\mathscr E_\infty$，得到
$$
\boxed{
T^*\mathscr E_\infty
=K_\infty^\perp\cap\mathscr E_\infty
=I\cap\mathscr E_\infty,\qquad
\overline{K_\infty^\perp\cap\mathscr E_\infty}=I.
}
\tag{22}
$$
因此 (15)--(20) 不包含 $P_{K_\infty}$ 保持正指数域的结论。
若能证明这个正交投影把 $\mathscr E_\infty$ 送回 $\mathscr E_\infty$，
则 (22) 才会迫 $K_\infty=M$，进而由 (2) 得 $N=M$。
当前没有证明这种实际域保持；
强* 渐近交换本身也不授权无界个数高位的乘积或任意孔阻尼。

新付清的是同一固定右逆的高位创建修复，以及由它导出的真正边界角代数。
原真实 $W$ 的 $\Gamma$、全部来源图域、$K_\infty=N$ 和 $N=M$ 仍保持开放。

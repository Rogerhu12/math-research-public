# R271 附录：一个真闭的单链限制、共同迹类像与严格单向稠密交织

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本文继续原负整数边界 $T=T_N,T_Y$、$B$、$S=B^*$，保持[同源迹类交织稿](R271-appendix-actual-directional-intertwiner-exclusion-and-trace-class-rosenblum-solutions.md)中固定的
$$
G=(I-P_0)\mathcal G_\lambda,\qquad P_0=e_0\otimes e_0,\qquad
u_n=G^ne_0,\qquad
L_y=\sum_{n\ge0}u_n\otimes S^ny .
\tag{0.1}
$$
$\lambda>2+2\log(3/2)$ 固定，所有幂先在原 $\mathscr E_\infty$ 上定义。该文已付
$$
Tu_0=0,\quad Tu_n=u_{n-1}\ (n\ge1),\quad
P_0u_n=0\ (n\ge1),\quad
\|u_n\|\le e^{A_\lambda n^3},
\tag{0.2}
$$
$$
\|B^n\|\le e^{-(95/32)n^4}\ (n\ge2),\qquad
TL_y=L_yB,\qquad P_0L_y=e_0\otimes y.
\tag{0.3}
$$
$L_y$ 是实际迹类算子，级数在每个物理指数输出范数上也绝对收敛。以下没有重选 $G$ 或删去完整 carry。

## 1. 真空规范右逆的闭包仍有闭值域

[平滑修正与有限孔伴随稿](R271-appendix-same-right-inverse-smoothing-correction-and-actual-kernel-cut-flux.md)已证 $\mathcal G_\lambda$ 可闭，且每个有限物理孔向量都属于 $\mathcal D(\mathcal G_\lambda^*)$。特别
$$
r_0:=\mathcal G_\lambda^*e_0\in H.
$$
所以在原定义域 $X_\lambda$ 上
$$
G=\mathcal G_\lambda-e_0\otimes r_0.
\tag{1.1}
$$
减去的是全 $H$ 上的有界秩一算子。因此 $G$ 可闭，且
$$
\overline G=\overline{\mathcal G_\lambda}-e_0\otimes r_0,\qquad
\mathcal D(\overline G)=\mathcal D(\overline{\mathcal G_\lambda}).
\tag{1.2}
$$
实际右逆恒等式和真空规范通过图极限给
$$
T\overline Gv=v,\qquad P_0\overline Gv=0
\quad(v\in\mathcal D(\overline G)).
\tag{1.3}
$$

置 $\widehat Y=\operatorname{Ran}\overline G$。若
$z_j=\overline Gv_j\to z$，则由 (1.3)
$v_j=Tz_j\to Tz$。闭图给 $Tz\in\mathcal D(\overline G)$ 和
$z=\overline G(Tz)$。故
$$
\boxed{\widehat Y\text{ 闭},\qquad
\widehat Y\subset e_0^\perp,\qquad
\widehat Y\cap\ker T=\{0\}.}
\tag{1.4}
$$
闭性并未使 $\mathcal D(\overline G)$ 成为全 $H$，也没有给 $\widehat Y$ 与 $\ker T$ 的正角。

## 2. 真闭 proper 的单链 T 限制

定义
$$
U_+=\overline{\operatorname{span}}\{u_n:n\ge1\},\qquad
U=\overline{\operatorname{span}}\{u_n:n\ge0\}.
\tag{2.1}
$$
由 (0.2)，
$$
U=\mathbb Ce_0\oplus U_+,\qquad U_+\subset\widehat Y,
\tag{2.2}
$$
其中直和是正交直和；最后的包含用到了 $\widehat Y$ 的实际闭性，而不是只看各个有限列。

$T$ 将每个 $u_n$ 送到前一列，所以 $U$ 是闭的 $T$ 不变子空间。记 $T_U=T|_U$。若 $v=ce_0+v_+\in U$ 且 $Tv=0$，则
$v_+\in\widehat Y\cap\ker T$，由 (1.4) 得 $v_+=0$。因此
$$
\boxed{U\cap M=\ker T_U=\mathbb Ce_0,\qquad M=\ker T.}
\tag{2.3}
$$
原两型的 $M$ 均无限维，见 [R185](R185-slow-additive-boundary-kernel-and-nonstandard-closed-ideal.md) 与 [R188](R188-critical-first-chaos-nonstandard-closed-principal-ideal.md)。故 (2.3) 立即排除 $U=H$。

另一方面，$u_n$ 线性无关：对任何有限非零线性组合作用最高次的 $T$ 幂，由 (0.2) 读出最高系数。因此
$$
\boxed{\{0\}\ne U\ne H,\qquad \dim U=\infty.}
\tag{2.4}
$$
这些是原 $T_N,T_Y$ 的实际不变子空间；原 $T$ 已另有无限核 $M$，所以本结论不构成普通 ISP 的完成。

所有广义核也可准确读出：
$$
\boxed{\ker T_U^r=\operatorname{span}\{u_0,\ldots,u_{r-1}\}
\quad(r\ge1).}
\tag{2.5}
$$
证明按 $r$ 归纳。若 $T_U^rv=0$，由 (2.3)
$T_U^{r-1}v=ce_0$；减去 $cu_{r-1}$ 后落入前一阶核。反向包含直接由 (0.2) 成立。因此这些有限维核的并在 $U$ 稠密。又每个 $u_n=Tu_{n+1}$，故
$$
\overline{\operatorname{Ran}T_U}=U.
\tag{2.6}
$$

旧 $e_0\in N=\overline{BM}$ 与 (2.3) 还给
$$
\boxed{U\cap N=\mathbb Ce_0,\qquad U\cap W=\{0\},
\quad W=M\ominus N.}
\tag{2.7}
$$
这里没有声称 $U\perp W$、$BU\subset U$ 或 $U+M$ 闭。

## 3. 每个非零源都有同一个稠密输出空间

对任意 $y\in H$，(0.1) 给 $\operatorname{Ran}L_y\subset U$，并且
$$
\boxed{
\ker L_y=
\left(\overline{\operatorname{span}}\{S^ny:n\ge0\}\right)^\perp .
}
\tag{3.1}
$$
若 $L_yx=0$，对每个 $n$ 由 (0.3) 有
$$
0=P_0T^nL_yx=P_0L_yB^nx
=e_0\langle x,S^ny\rangle.
$$
反过来，若所有这些系数为零，实际收敛级数 (0.1) 逐项为零，故 $L_yx=0$。这证明 (3.1)。

再设 $y\ne0$，并令 $k$ 是其最小非零整数坐标。置
$$
\beta_0=1,\qquad
\beta_j=\prod_{\nu=1}^j\alpha_{v_2(\nu)}\quad(j\ge1).
$$
对 $r\ge0$，原加权移位的有限列公式给
$$
L_y e_{k+r}
=
\sum_{n=0}^{r}
\frac{\beta_{k+r}}{\beta_{k+r-n}}\,
\overline{y_{k+r-n}}\,u_n.
\tag{3.2}
$$
最高列 $u_r$ 的系数是
$\beta_{k+r}\overline{y_k}/\beta_k\ne0$。
有限三角回代因而把每个 $u_r$ 写成
$L_y e_k,\ldots,L_y e_{k+r}$ 的线性组合。结合相反的范围包含，得到
$$
\boxed{\overline{\operatorname{Ran}L_y}=U
\qquad(y\ne0).}
\tag{3.3}
$$
这里使用全部原权 $\beta_j$；没有将其替换成均匀移位或只保首项。

特别 $S^ne_0=\beta_ne_n$ 的张成稠密于 $H$，所以 (3.1) 给
$$
\boxed{L_{e_0}:H\longrightarrow U
\text{ 单射、有稠密像、且为迹类，}\qquad
T_UL_{e_0}=L_{e_0}B.}
\tag{3.4}
$$
因此这是一个实际的单向拟仿射交织，即单射且像稠密的有界交织；没有声称两算子相似或双向拟相似。

## 4. 相反方向连非零有界交织也不存在

**定理。** 若 $X:U\to H$ 有界且
$$
XT_U=BX,
$$
则 $X=0$。

对固定 $k\ge0$，由 (0.2)
$$
Xu_k=XT_U^n u_{k+n}=B^nXu_{k+n}.
$$
其范数由 (0.2)–(0.3) 不超过
$$
\|X\|\exp[-(95/32)n^4+A_\lambda(k+n)^3]\longrightarrow0.
$$
所以 $Xu_k=0$ 对每个 $k$ 成立。有限链张成在 $U$ 稠密，故 $X=0$。这不仅排除反向的单射稠密交织，而且排除该方向的所有非零有界交织。所用来源是同一个实际链 $u_{k+n}$，没有假定 $U$ 内处处有界的 $T_U$ 右逆。

## 5. 原 W 的准确商映射

若 $0\ne w\in W$，前稿已给
$$
L_wN=0,\qquad L_w|_M=e_0\otimes w,\qquad L_w^*e_0=w.
$$
由 (3.3)，同一个 $L_w$ 因而诱导实际紧算子
$$
\widetilde L_w:H/N\longrightarrow U
$$
且其像稠密。$B$ 保持 $N$，故它与商算子 $\widetilde B$ 满足
$$
T_U\widetilde L_w=\widetilde L_w\widetilde B.
\tag{5.1}
$$
在 $M/N\simeq W$ 上，其值准确为 $w'\mapsto\langle w',w\rangle e_0$。这通常不是单射；不能把一个源 $w$ 的稠密输出升为整个 $H/N$ 与 $U$ 的单射稠密交织，也不能由 (2.7) 的零交得到正角。

本文新增的是由实际闭右逆保证的 proper 单链限制、全部有限广义核、迹类族的共同闭包像与准确核，以及该限制上严格的交织方向差异。两型的 $N=M$、实际 Green 范围和同源费用仍需原额外输入。

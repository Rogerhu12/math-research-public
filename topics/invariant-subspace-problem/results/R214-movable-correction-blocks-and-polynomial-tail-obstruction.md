# R214：可任意后移的真实纠错块与稳定边界空间正交补的多项式尾下界

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本文处理既有 R185/R188 的两个**实际**负整数边界模型。证明不删除 carry，不把近似核当成真核。它把此前对未知差空间 $M\ominus N$ 的 $\exp[-C m2^m]$ 尾下界，改善为依赖于一个固定非零坐标的多项式下界。它没有证明 $N=M$，没有把此边界结论移到原 Haar 表示，也没有解决普通 ISP。

## 1. 模型和精确输入

在 $\ell^2(\mathbb N_0)$ 上，令
$$
Be_0=0,\qquad Be_n=\beta_ne_{n-1},\qquad
\beta_n=\alpha_{v_2(n)}>0,
$$
$$
\mathsf N_j=B^{2^j}/d_j,\quad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},\quad
 a_j=(j+1)^{-2},
$$
并固定下列两算子之一：
$$
T=T_N=\sum_{j\ge0}a_j\mathsf N_j,
\qquad\hbox{或}\qquad
T=T_Y=\sum_{j\ge0}a_j\mathsf Y_j.
$$
两者均按范数收敛、与 $B$ 交换，且 $\|T\|\le6$。置
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\},
$$
$P_m$ 为到 $\mathcal F_m$ 的正交投影。既有 R187 已知 $e_0\in N$。

使用的实际权输入为
$$
\eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j},\qquad
0<\alpha_j\le1,
$$
$$
\mathsf N_j=\mathsf E_j+\eta_j\mathsf E_j^*\mathsf N_{j+1},
\qquad \|\mathsf Y_j-\mathsf E_j\|\le4\eta_j,
$$
其中 $\mathsf E_j$ 为纯孔消灭矩阵。

有限头上的 $T_p=T|_{\mathcal F_p}$ 是 $B_p=B|_{\mathcal F_p}$ 的无常数有限多项式，并且形式首阶为 1。因此
$$
T_p^{r+1}e_r=0\quad(r<2^p),\qquad T_pB_p=B_pT_p.
\tag{1.1}
$$
这里只用严格下三角性，不需要 Cayley 级数在整个空间绝对展开。

R185/R188 还已给下列精确修复事实：若 $u\in\mathcal F_q$、$\|u\|=1$、$q\ge2$，且
$$
\|Tu\|\le e^{-40\,4^q},
$$
则有 $y\in M$，满足
$$
\|y-u\|\le2e^{-20\,4^q},
\tag{1.2}
$$
且修正的整数支持全部高于原头 $\mathcal F_q$，事实上第一修正块从第 $64\,2^q$ 位开始。该事实由原文的逐步有限维右逆、真实空位进位预算及强收敛给出。

## 2. 固定低头、任意远块的纯右逆

固定整数 $r\ge0$。选取 $p\ge2$，使 $r+1<2^p$，以后始终保持 $r,p$ 固定。
取任意充分大的整数 $L$，要求
$$
L\ge64\,2^p.
\tag{2.1}
$$
新块为 $[L,2L)$，中间 $[p,L)$ 和块后坐标全取真空。

令
$$
D_L=\sum_{j=L}^{2L-1}a_j\mathsf E_j,
\qquad C_L=D_L^*,\qquad
\sigma_L^2=\sum_{j=L}^{2L-1}a_j^2.
$$
则
$$
\sigma_L^2\ge\frac1{16L^3},\qquad
\max_{L\le j<2L}a_j^2\le L^{-4}.
$$
在新块 $q$ 孔齐次空间上，单个位矩阵恒等式给
$$
\|C_Lv\|^2-\|D_Lv\|^2
=\sigma_L^2\|v\|^2-2\sum_{j=L}^{2L-1}a_j^2\|P_jv\|^2
\ge\left(\frac1{16L^3}-\frac{2q}{L^4}\right)\|v\|^2.
$$
对 $0\le q\le r+1<2^p\le L/64$，右侧至少为 $\|v\|^2/(32L^3)$。
故 $D_L:\mathcal K_{q+1}\to\mathcal K_q$ 有右逆 $R_q$，且
$$
\|R_q\|\le\sqrt{32}\,L^{3/2}=:b_L.
\tag{2.2}
$$
可明确取 $R_q=C_q(C_q^*C_q)^{-1}$，$C_q=C_L|_{\mathcal K_q}$。

由块真空 $h_0$ 递归令 $h_k=R_{k-1}h_{k-1}$。于是
$$
D_Lh_k=h_{k-1},\qquad \|h_k\|\le b_L^k,
\qquad h_k\in\mathcal K_k\quad(0\le k\le r+1).
\tag{2.3}
$$
这些仍是有限维、实际有界的右逆；这里只把块起点 $L$ 留作自由参数。

## 3. 真正右移后纠错，取得 $N$ 内固定头的族

定义
$$
h=\beta_{r+1}^{-1}e_{r+1}\in\mathcal F_p,
\qquad B_ph=e_r.
$$
置
$$
V_L=\sum_{k=0}^{r+1}(-1)^kT_p^kh\otimes h_k\in\mathcal F_{2L}.
\tag{3.1}
$$
省略的坐标为真空。由 (1.1) 和 (2.3)，
$$
(T_p\otimes I+I\otimes D_L)V_L=0.
\tag{3.2}
$$
又
$$
H_L:=\|V_L\|
\le\beta_{r+1}^{-1}\sum_{k=0}^{r+1}6^kb_L^k
\le\beta_{r+1}^{-1}(r+2)(6\sqrt{32})^{r+1}L^{3(r+1)/2}.
\tag{3.3}
$$
这里的常数依赖固定 $r$，允许很大；没有把右移逆范数当成 1。

真实进位逐链展开跨越空白间隔，给在整个模型输入空间上的估计
$$
\|(T-T_p\otimes I-I\otimes D_L)x\|
\le26\eta_{L-1}\|x\|.
\tag{3.4}
$$
说明：(a) 对 $i<p$，有限头项后的进位必须到达至少 $L$ 位，余项范数至多 $\alpha_L/\alpha_i\le\eta_{L-1}$；(b) 对 $p\le i<L$，全间隔真空使该算子作用同样至多此量；(c) 对块内 $i$，使用 $\|\mathsf N_i-\mathsf E_i\|\le\eta_i$ 或 $\|\mathsf Y_i-\mathsf E_i\|\le4\eta_i$；(d) 对 $i\ge2L$，真实算子严格杀掉整个 $\mathcal F_{2L}$。Cayley 低位项由有限头和真实逆差处理，正是 R188 的统一常数 26；该论证只使用 $L\ge p$，并不需要 $L=64\,2^p$。

故 $\|TV_L\|\le26\eta_{L-1}H_L$。因为
$$
26\eta_{L-1}\le26e^{-(770/16)16^L}\le e^{-40\,16^L}=e^{-40\,4^{2L}},
$$
可先将 $V_L$ 除以其真实范数 $H_L$，再用 (1.2)，最后乘回：得到 $y_L\in M$，且
$$
\|y_L-V_L\|\le2H_Le^{-20\,16^L}.
\tag{3.5}
$$
$V_L\ne0$，因为其原低头仍为 $h\ne0$。

低头有孔时，真正 $B$ 与 $B_p\otimes I$ 完全一致；低头全真空时，真正后移必须在新块遇到孔，故
$$
\|(B-B_p\otimes I)V_L\|\le\alpha_L H_L.
\tag{3.6}
$$
其输出整数指标至少是 $2^L-1$。

用 $B_pT_p=T_pB_p$、$B_ph=e_r$ 和 $T_p^{r+1}e_r=0$，有
$$
(B_p\otimes I)V_L
=e_r+\sum_{k=1}^{r}(-1)^kT_p^ke_r\otimes h_k.
\tag{3.7}
$$
令
$$
x_L=By_L\in BM\subseteq N.
$$
由 (3.5)—(3.7)，
$$
x_L=e_r+\sum_{k=1}^{r}(-1)^kT_p^ke_r\otimes h_k+\varepsilon_L,
\tag{3.8}
$$
$$
\|\varepsilon_L\|
\le H_L\left(\alpha_L+2\|B\|e^{-20\,16^L}\right)=o(1).
\tag{3.9}
$$
(3.3) 的多项式增长被真实权的超指数衰减压倒。

此外，(3.8) 的所有非 $e_r$ 项都垂直于 $\mathcal F_{L-1}$。主修正项在新块有孔，真实 borrow 输出至少 $2^L-1\ge2^{L-1}$，后续修复的后移输出更高。因此
$$
\boxed{x_L-e_r\perp\mathcal F_{L-1}.}
\tag{3.10}
$$
注意不能把阈值擅改成 $\mathcal F_L$，因为真正后移可能产生 $e_{2^L-1}$。

对 $r\ge1$，定义明确的有限常数
$$
C_r=1+\sum_{k=1}^{r}32^{k/2}\|T^ke_r\|.
$$
当 $L$ 充分大使 (3.9) 至多为 1 时，由 (2.3)、(3.8) 得
$$
\boxed{\|x_L-e_r\|\le C_rL^{3r/2}.}
\tag{3.11}
$$
可统一放宽 $C_r\le2(6\sqrt{32})^r$。$r=0$ 时主和为空，故 $x_L\to e_0$，也重获 $e_0\in N$。

## 4. 多项式下界与平滑正交见证的排除

**定理。** 固定 $r\ge1$。存在只依赖实际模型和 $r$ 的 $L_r<\infty$，使对任意 $f\in N^\perp$ 及任意整数 $L\ge L_r$，
$$
\boxed{
|\langle e_r,f\rangle|
\le C_rL^{3r/2}\|(I-P_{L-1})f\|.
}
\tag{4.1}
$$

证明：$x_L\in N$，故 $\langle x_L,f\rangle=0$。由 (3.10)—(3.11)，
$$
|\langle e_r,f\rangle|
=|\langle x_L-e_r,(I-P_{L-1})f\rangle|
\le C_rL^{3r/2}\|(I-P_{L-1})f\|.
$$
这证明了 (4.1)。它事实上作用于整个 $N^\perp$，不需要 $f\in\ker T$。

若 $0\ne f\in M\ominus N$，由 $e_0\in N$，其最小非零整数坐标 $r$ 满足 $r\ge1$。因此对所有充分大的 $m$，
$$
\boxed{
\|(I-P_m)f\|
\ge\frac{|f_r|}{C_r(m+1)^{3r/2}}.
}
\tag{4.2}
$$
这比此前 $\exp[-8(m+1)2^{m+1}]$ 的必要下界严格更强。

**推论。** 若 $f\in N^\perp$，且其二进位头尾对每个 $s>0$ 满足
$$
\|(I-P_m)f\|=o(m^{-s}),
$$
则 $f=0$。特别，$M\ominus N$ 中不存在非零的上述快速尾向量。

更准确地，定义整数支撑的最高位
$$
b(n)=\lceil\log_2(n+1)\rceil\quad(n\ge0).
$$
若 $f\in N^\perp$ 具有非零 $r$ 坐标，则
$$
\sum_{n\ge0}(1+b(n))^{3r}|f_n|^2=\infty.
\tag{4.3}
$$
因为有限的该加权和会使
$(m+1)^{3r/2}\|(I-P_m)f\|\to0$，与 (4.1) 矛盾。

## 5. 为什么此下界还不能证明饱和

任意慢的平方可和尾可以满足 (4.2)。一般 Hilbert 向量没有理由属于 (4.3) 的加权空间；加权平滑向量在环境空间中的稠密性也不能传给闭子空间 $M\ominus N$。

事实上，在较大的空间 $N^\perp$ 上，指数 $3/2$（$r=1$）是准确尺度。以 $T_N$ 为例，
$$
f=T_N^*e_0=\sum_{j\ge0}a_je_{2^j}\in M^\perp\subseteq N^\perp,
\qquad f_1=a_0=1.
$$
实际矩阵元在此首列严格为 1，所以这不是删除 carry 的近似。其尾满足
$$
\|(I-P_m)f\|^2=\sum_{j\ge m} (j+1)^{-4}\asymp m^{-3}.
$$
故一般 $N^\perp$ 上不可能把 $r=1$ 的下界改善为指数小于 $3/2$ 的统一幂。该向量属于 $M^\perp$，**并非** $M\ominus N$ 的反例；是否利用额外核方程 $Tf=0$ 进一步排除后者仍是具体缺口。

## 6. 使用文件

- [R185 源稿](../notes/2026-11-12-slow-additive-boundary-kernel-and-nonstandard-closed-ideal-0c-agent.md)：R185 实际有限块右逆、空位进位和强极限。
- [R188](R188-critical-first-chaos-nonstandard-closed-principal-ideal.md)：Cayley 对应的同一纯块模型、统一误差常数 26。
- [快速头残差与稳定像](../notes/2026-11-12-boundary-fast-head-residuals-enter-stable-range-and-quotient-norms-0c-agent.md)：先真正右移、归一化后修复、再乘回尺度的正确处理；本稿将其块起点独立化，并把固定 $e_r$ 的真实幂零长度 $r+1$ 用于多项式成本。

下一接口：同时使用 $f\in M$ 和 $f\perp BM$，研究是否可利用真实 $T^*$ 像消去 (3.8) 中的高孔补偿，从而取得超出一般 $N^\perp$ 的尾约束。不能仅重复已经饱和的 $r=1$ 一般正交补估计。

# 新输入：正确 Phi 两个已定义商矩阵在 $Q=0$ 的整行幺模消元

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

**尚未执行。** 本源码有两个事前冻结、分别首次运行的原输入 F 与 G：环境变量 ISP_Q0_MODEL 必须分别固定为 F 或 G，每个独立预算 **120 秒 / 1 GiB，外层 135 秒**。没有默认模型、没有资源失败后切换模型或续轮恢复。两个来源是不同的固定原矩阵。

本次唯一新目标，是在 $\mathbb Q[u]$ 上用真正行列式为一的双行 Bézout 变换，支付两个既有商行列式的进一步 $Q$ 整除幂。它不重求已成条目赋值、最小匹配、原最高矩阵、任何旧行列式或双轴 gcd；不进行新的模比较。

## 1. 唯一原输入与已付范围

上一条唯一实际 run46158891405 / job141021539125 已证明
$$
F=Q s^4(-L)^{15}F_*,
$$
$$
G=s^8\delta^{48}K_w(-M_n)^8\bigl(-(2L-Q)\bigr)^4G_*,
\tag{1}
$$
其中 $s=u-1,\delta=1-Q,K_w=Q+4s,L=Q-2s(u-2)$，
$M_n=2uL-L^2-u^2Q$，且
$$
F_*=\det M_F,\qquad G_*=\det M_G.
$$
两个商矩阵条目在 $\mathbb Z[u,Q]$；$M_F$ 为 $12$ 阶，$M_G$ 为 $14$ 阶。它们均来自正确原 Gram 理想：当前已付权环中 $F_*\in I_6$、$G_*\in I_6+(Vlow)$。所有原首项零纤维保持。

已付次数是
$$
(\deg_uF_*,\deg_QF_*)=(368,206),\qquad \deg F_*\le409,
$$
$$
593\le\deg_uG_*\le594,\qquad \deg_QG_*=302,\qquad \deg G_*\le633.
\tag{2}
$$
完整来源见
[原权矩阵精确提取与公共因子界](../results/R150-appendix-unit211-Phi-zero-corrected-exact-paid-matrix-extraction-and-common-curve-bidegrees-five-fifty-one.md)。

本次只处理旧物理权单位 $Q$。没有新 $u$ 多项式单位或任何几何头、$\lambda,t,D$ 的逆。整个来源范围仍是正确 Phi、distinct singleton、物理 $D\ne0$ 图；不扩大十三或十生成论文的系数环。

最终商矩阵的完整 profile-list SHA256 固定为：

| 输入 | 维数 | 既成商矩阵 profile |
|---|---:|---|
| F | 12 | ec03ed0d0eae88a7349a8423167b559d62c7504436e27980bbcd78969c11ed8a |
| G | 14 | a93eb7f9abf50874a215866708a9f95c182fafda4ba49680871c21c3f51e2a42 |

源码只按上次实际返回的八组短整数行、列尺度定义它们。F 使用 $Q,s,-L$ 的三组；G 使用 $s,-\delta,K_w,-M_n,-(2L-Q)$ 的五组。必要多项式精除用来形成唯一系数定义，随后只核上表 profile。没有执行任何旧赋值搜索、最小匹配或旧提取证明检查循环。

## 2. $Q$ 的完整系数容器

取其中一个固定矩阵 $M$，设它所有条目的最大 $Q$ 次数为 $d_Q$。程序将每个条目完整写成
$$
M_{ij}(u,Q)=\sum_{k=0}^{d_Q}m_{ij,k}(u)Q^k,\qquad m_{ij,k}\in\mathbb Q[u].
\tag{3}
$$
全部 $n^2$ 个原条目从 (3) 乘回后，后续使用固定宽度 $n(d_Q+1)$ 的行容器。

这不是模 $Q^{d_Q+1}$ 的截断，也不是有限代数商：原多项式的所有系数均在 (3) 中。新行变换只用 $\mathbb Q[u]$ 系数，故不增 $Q$ 次数；随后整行除 $Q$ 只降该次数。于是该固定容器始终精确包含整个二元多项式矩阵。

## 3. 真正 $\mathbb Q[u]$ 幺模双行变换

在当前列的两个非零 $Q^0$ 条目 $a(u),b(u)$ 上，实际返回
$$
g=sa+tb,\qquad a=gA,\qquad b=gB.
\tag{4}
$$
这里只使用 $\mathbb Q[u]$ 的真实 Bézout 和两个整除商，不把 $g$ 当权单位。由 (4) 还完整返回
$$
sA+tB=1.
\tag{5}
$$
因此
$$
E=\begin{pmatrix}s&t\\-B&A\end{pmatrix},
\qquad
E^{-1}=\begin{pmatrix}A&-t\\B&s\end{pmatrix}
\tag{6}
$$
都在 $\operatorname{Mat}_2(\mathbb Q[u])$ 中，且 $\det E=1$。

对两个完整二元原行 $R_1,R_2$ 定义
$$
R_1'=sR_1+tR_2,\qquad
R_2'=-BR_1+AR_2.
$$
源码不是只核两个选中条目：对 (3) 的全部坐标，逐项返回
$$
AR_1'-tR_2'=R_1,\qquad
BR_1'+sR_2'=R_2.
\tag{7}
$$
所以每个实际双行变化在全部 $u,Q$ 上都可逆。$a,b,g$ 或任何多项式主元的零点没有被删去。

每列的选行规则事前固定：在剩余非零条目中先选 $u$ 次数最小者，次数相同取最小行号。随后按行号递增执行 (4)–(7)。无模点、无素数、无结果后的重排。换行只带来明确的符号 $-1$，没有其他行尺度。用于 (4) 的 python-flint 0.9.0 fmpq_poly 接口采用普通有理多项式和 divmod；两条商、Bézout 与逆行身份均由源自身乘回。

固定一轮结束后得到
$$
E_0(u)M(u,Q)=\widetilde M(u,Q),\qquad
E_0\in\operatorname{GL}_n(\mathbb Q[u]),\quad \det E_0=\sigma\in\{1,-1\}.
\tag{8}
$$
不必展开巨大 $E_0$：完整逐步身份 (7) 与每个 $2$ 阶行列式一、换行符号给出其组合的准确来源。

## 4. 只有完整零行才精除 $Q$

设模 $Q$ 的真正行阶梯形有 $r$ 个非零行。程序检验剩余 $n-r$ 行的每一个列的 $Q^0$ 系数都为零，而非仅检验若干主元列。于是这 $n-r$ 个完整二元行确实逐行整除 $Q$。

定义 $M_{\rm next}$ 为上述零行除 $Q$、其他行不变的矩阵。每条受除行的所有 (3) 坐标均完整返回，故
$$
\widetilde M=
\operatorname{diag}(I_r,QI_{n-r})M_{\rm next}.
\tag{9}
$$
由 (8)–(9)，在整个 $\mathbb Q[u,Q]$ 中
$$
\det M=\sigma Q^{n-r}\det M_{\rm next}.
\tag{10}
$$
程序只有在 (7)、全部零行及 (9) 全部完成后，才输出一次有效轮回执，累加 $n-r$。轮内的若干主元 checkpoint 不增加已付指数。

重复上述新的整行步骤，若完成若干轮，可得到
$$
F_*=\varepsilon_F Q^{e_F}\det M_F^{\rm new}
\quad\hbox{或}\quad
G_*=\varepsilon_G Q^{e_G}\det M_G^{\rm new},
\qquad \varepsilon_F,\varepsilon_G\in\{1,-1\}.
\tag{11}
$$
这时 $e_F,e_G$ 只是实际证明的下界，除非另有下一节的满秩终点。即使期间资源触界，已经完整输出的各轮 (10) 仍是独立有效的原身份；没有从未完成轮猜测阶数。

## 5. 满秩终点、次数和绝对循环界

若某一轮的 $Q^0$ 行阶梯形有 $n$ 个非零主元，它的行列式是非零 $\mathbb Q[u]$ 多项式。由幺模变换，当前 $\det M\bmod Q$ 非零，故剩余矩阵不再被 $Q$ 整除，此时 (11) 的累计指数才是精确 $Q$ 赋值。

这里“主元非零”仅用于证明一个 QQ 多项式不恒零；程序没有反演它，也没有宣称它在每个 $u$ 点为单位。特殊 $u$ 零面仍保留在完整 (11) 中。

从 (2) 已有严格先验界
$$
\operatorname{ord}_QF_*\le409-368=41,
\qquad
\operatorname{ord}_QG_*\le633-593=40.
\tag{12}
$$
原因是除 $Q^e$ 不改 $u$ 次数，而商的总次数至少等于其 $u$ 次数。本源据此固定最多 $42$ 或 $41$ 轮的绝对循环上界；计时器更早触界就立即按真实边界停止。每个未满秩完成轮至少抽取一次 $Q$，所以已知非零性和 (12) 也保证在无资源限制的数学过程中终止。

(12) 说明不能把旧固定 $u=2$ 上模 gcd 的次数 $51$ 直接当成真实公共 $Q$ 赋值。

每个完成的 (11) 给新的次数：
$$
\deg_Q(F_*/Q^{e_F})=206-e_F,\quad
\deg_u(F_*/Q^{e_F})=368,\quad
\deg(F_*/Q^{e_F})\le409-e_F,
$$
$$
\deg_Q(G_*/Q^{e_G})=302-e_G,\quad
593\le\deg_u(G_*/Q^{e_G})\le594,\quad
\deg(G_*/Q^{e_G})\le633-e_G.
$$
当前物理权环内 $Q$ 已付，故新商仍是原必要纯权关系。本次不计算新商的模切片、gcd 或任何 QQ 公共曲线；若要进一步比较，必须先将两条实际 (11) 各自正式登记，再另选新输入。

## 6. 参数边界、依赖与唯一预算

本源只读取以下第一份源码在 def sylvester_models(pair) 之前的 $10491$ 字节必要定义，SHA256 为
7313f0bda9d11c57e91e51019b7fe2fdc4c2d3442638df54d1355539a71bf678。
AST 只移除旧顶层时钟、资源和日志语句，完整四依赖 SHA 与四参数身份检查保留。旧数学主循环、旧匹配、旧最高矩阵和旧模行列式函数均不导入或执行。

五个完整源码依赖，只由 runner 临时读取：

| basename | 全源 SHA256 |
|---|---|
| 2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py | 060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7 |
| 2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py | 0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335 |
| 2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py | 39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b |
| 2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py | 84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0 |
| 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py | 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7 |

原 b0ef 整除源码不是本次依赖，也不调用它的证明循环；八个短整数尺度就是旧实际回执中已确定的参数定义。

新源：
[2026-11-28-unit211-Phi-zero-corrected-QQ-Q-primary-unimodular-row-extraction-8542.py](2026-11-28-unit211-Phi-zero-corrected-QQ-Q-primary-unimodular-row-extraction-8542.py)。

冻结 blob：f6ffe1592022e69abe8746e97e436b86763b354b。

完整 SHA256：5971d0015ea65e5f8f2fc0c0ba6be7bbf5aea15292dc1383cd83c85dee3a877c。UTF-8 15320 字节。

分别由两个首次工作流固定 ISP_Q0_MODEL=F 与 ISP_Q0_MODEL=G。每次从最初入口起严格 **120 秒 / 1 GiB，外层 135 秒**；所有嵌套 alarm/setitimer 都夹到同一最初截止，非正调用也不会关闭外层保护。

输出只含固定参数身份、完整行返回计数、轮秩/零行数/已付指数、非零主元 profile、最终矩阵 profile 和准确次数。没有系数载荷、缓存或续轮状态入库。源码尚未执行，不预报任何秩、指数、终点或空性；任一真实触界均冻结该模型的本门，不加时、加内存、改主元序或恢复后继轮。

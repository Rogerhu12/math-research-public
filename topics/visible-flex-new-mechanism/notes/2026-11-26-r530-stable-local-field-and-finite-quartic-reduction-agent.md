# R530 v2：原局部场的准确重写与有限四次 history 张量

日期：2026-11-26。源码/请求说明及原式推导。
本文不新增 ODE 轨道、不宣称四偶端矩已有有限根。
`r530_compact_full_history_agent.py` 的本地开发情况单独保存在同日收据；
该旧源与收据冻结，本文只对应另起的 `r530_compact_history_v2_agent.py`。
v2 到本说明写成时只作了文本/AST 解析，未作新的本地科学执行。

## 1. 原 eta 的闭式，不用巨大整个 ruling 之差提取加速度列

对一个真紧单 profile $u$，写
$$
p=u',\quad r=u'',\quad t=u''',\quad
z=y+\eta,\quad e=hz-k,\quad Q=1+e^2 .
$$
所有 $J$ 都是同一实际右端的正尾积分。
R56 的局部 second 恢复记作 $K_s(u,u)$；其分子为
$$
V_K=(\eta_D/h,zP_D+B_D,e\eta_D/h).
$$
准确有
$$
\eta_D=\gamma a_h[u^2]+\upsilon a_k[u^2],
\tag{1}
$$
其中
$$
a_k[u^2]=\frac{Qr^2+2hJ(er^2)}{32h^2},
\tag{2}
$$
$$
a_h[u^2]=\frac{2Qpr-zQr^2-2hep^2
+J\{(1+k^2-h^2z^2)r^2-2h^2p^2\}}{16h^2}.
\tag{3}
$$
其空间导数是
$$
(a_k)'=\frac{Qrt}{16h^2},\qquad
(a_h)'=\frac{Q(p-zr)t}{8h^2}.
\tag{4}
$$
(2)(4)与原 R521/R482 已登记身份一致。
这里将完整 primitive (3) 写入实现，不重选其左常尾。

**推导。** 由 R56/R73
$$
P=\frac{J(Qr^2+2h^2p^2)}{8h}+\frac e8p^2,
\quad
B=\frac{p^2/4+(hu-ep/2)^2}{2h},
$$
$$
\eta_D=-\frac{T_{s\xi}}{2h}
+\frac{\gamma z-\upsilon/2}{2h}P'
+\frac\gamma{2h}B'-\frac12P_s .
$$
将真实速度 $h_s=\gamma$, $k_s=\upsilon$,
$\eta_s=\upsilon/(2h)$ 代入，分别收集 $\gamma$ 与 $\upsilon$。
使用右 collar 仅给的
$$
J(pr)=-p^2/2,
\quad
J((2hz-k)pr)=-(2hz-k)p^2/2-hJ(p^2),
$$
得到(2)(3)。对(3)逐项求空间导数，
所有 $p^2,pr,r^2$ 项准确相消，只剩(4)。
这没有用左尾为零；对一般单包 (2)(3)确实可有非零左常尾。
对真实 $\Delta=f\odot f-g\odot g$ 作相应二次差即可。

设 $W=2\gamma p+(\upsilon-2\gamma z)r$。
给出用于原 $V_{K,\xi\xi}$ 的准确下一导数：
$$
\eta_D'=\frac{QWt}{16h^2},
\quad
\eta_D''=
\frac{2heWt+Q(\upsilon-2\gamma z)t^2+QWu^{(4)}}{16h^2}.
\tag{5}
$$
对 $(1)$ 和 $(4)$ 真正作 $s$ 导数，保留
$\gamma_s=a,\upsilon_s=b$，即得所需 $K_s$ 导数。
这一步不把 $q_s=\Phi_M\Delta$ 省掉；它仍在真实 second 的导数中单列。

## 2. 当前 second history 的线性项与负平方项

取 $q=\Phi_A\Delta$，仍保完整第三投影 $t_j$。
原 R482 **未消第三历史**的(24)准确为
$$
\mathscr K=\mathscr R
+\mathscr L_S(q)-\mathcal E_S(q,q)
-4\mathbf w_y\cdot t-2\mathbf w_y\cdot\nu .
\tag{6}
$$
本节没有使用依赖 R480 母的第三历史消元(25)。

以真实分子直接评价
$$
\mathcal E_S(q,q)=\frac1h\int|V_q'|^2,
$$
$$
\mathscr L_S(q)=\frac2h\int V_q'\cdot V_{K(\Delta)}'
-\frac4h\int V_g'\cdot V_{K(g,q)}'.
\tag{7}
$$
$q$ 的真紧性来自 R521 原三矩和 E8 原左尾表；不能对其求积尾另置零。
式(2)(3)极化便给(7)的 $K(g,q)$。
具体为
$$
a_k[f,g]=\frac{Qf''g''+2hJ(ef''g'')}{32h^2},
$$
$$
a_h[f,g]=\frac{Q(f'g''+g'f'')-zQf''g''-2hef'g'
+J\{(1+k^2-h^2z^2)f''g''-2h^2f'g'\}}{16h^2}.
\tag{8}
$$
当前源码保两个不同评价方向：
先用原 full second 与 full third local 分子读整个 ruling，
再用 $\mathscr R=\mathscr K|_{A=t=\nu=0}$ 和(7)重建。
共同核对的是整个值而不是两个约 $10^{17}$ 的数相减后试图读出约1的加速度列。
加速度列直接用已经证明的 R521 正积分；此处不重做其证明。

## 3. 三个投影的固定有限张量及真实完整 chain

继续原 27 状态 note 的定义
$$
t_j=I_{j,y}(g,T(g;\Delta)),\qquad j=0,1,2.
$$
对真正原八基 $E_\alpha$，置
$$
B_{j,\alpha\beta}
=I_{j,y}\{g,\Phi_{E_\alpha}(g,\Phi_{E_\beta}\Delta)\}.
\tag{9}
$$
该 $3\times8\times8$ 表只依赖当前固定 profiles、完整右锚和原算子。
没有把它当作可独立操控的第三 response 坐标。
完整原第三的三个投影准确按
$$
t_j'=c_j(S,\gamma,\upsilon,a,b)
-\sum_{\alpha,\beta}M_\alpha A_\beta B_{j,\alpha\beta}
\tag{10}
$$
演化，其中 $c_j$ 由 R73 原
$$
\mathcal C_s(g;\Delta)=R[H(Y_g,K_s(\Delta))]
-\Psi_s(g,\Phi_M\Delta)
$$
读取，保全部变化-profile chain。
v2 同时直接计算右侧 mixed profile 与固定表(9)的收缩，
用它们比较真实第三投影；不计算或宣称完整 $T$ 端值已零。

## 4. 一个固定模型的公开请求

源：`scripts/r530_compact_history_v2_agent.py`。
请求：`computations/request-r530-compact-reduction-20261126.json`。
workflow：`.github/workflows/visible-r530-compact-reduction-20261126.yml`。

请求只做如下新 scope：原 R56 局部场与(1)–(5)的实现核对，
未消第三历史的(6)(7)核对，以及(9)(10)的有限 tensor 收缩。
同一单 job 依次使用最细包 Gauss 阶数24、48、96，gap阶数8。
所有副本、位置、最细包半宽 `4e-7`、中心10与公共幅
$\mathrm{width}^{7/4}/256$ 全部不变。
尤其取消初稿“各求积阶各自重算一次 $C_k=1$ 归一”；
加密只改变积分精度，不改变输入 profiles。

请求不运行 ODE、shooting、优化或 response rank。
原 runner 会实际 pull/read README 并移除凭据后才启动科学子程序；
仅原 stdout 小摘要，不产大数组、artifact、Release 或 Git 写入。
尚无本请求的公开 run 结果。

`grid.integral` 中的权是实际副本幅 $w^{1/4}$ 在齐次四次读出中提出的 $w$，不是一般低次函数的空间积分权。当前调用全部为四次：ruling 的 $2+2$ 或 $1+3$、第三投影和 B 的 $1+3$、Ch/Ck 的四次；history 线性项/负平方亦然。`right` 仍在每个真实32微包完整块内保全部尾和 gap，不另乘权或删尾；固定第三规范的 $\nu$ 项单独按 Gram 配对进入。

workflow 的用途已在 topic log 登记；公开执行只输出本固定模型的原收据。

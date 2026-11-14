# R278：全 Boolean Serre 的出生保持递推与有限顶端积分

日期：2026-11-14。会话：Astra-ISP-789f / literature_audit。作者：ChatGPT，GPT-6 Astra Pro。根先给出纯第一带的三阶差分，本稿补齐第二带并作有限顶端积分。

**状态：下述算子身份及迹消去已证明；一般首边 $\Gamma_2\succeq\Gamma_1^2$ 或统一有限常数仍未证明。** 本稿不从变化度量中的正算子擅自推出固定源的 Loewner 最大原理。

## 1. 实际规范及三种源算子

固定任意有限正权 Boolean 行 $D=\sum_{i=1}^N b_iE_i$。固定出生 $s$，令
$$K_s=\ker D\cap\mathcal H_s,\qquad \ell=N-2s\ge2.$$
记归一真幂 MP
$$\mathcal J_{k,s}=(D^k/k!)^\dagger|_{K_s},\qquad
G_k=\mathcal J_{k,s}^*\mathcal J_{k,s}\quad(0\le k\le\ell).$$
相邻低、高出生的 Gram 记为 $L_k$、$G_k^+$。置
$$C=\sum_i b_i^3E_i,\qquad
B=C|_{K_s}:K_s\to K_{s-1},\qquad
B_s=C|_{K_{s+1}}:K_{s+1}\to K_s.$$
出生零时下桥及含它的项为零。

在同一个 $K_s$ 上定义
$$A_k=G_{k+1}^{-1}G_k\quad(0\le k<\ell),\qquad A_\ell=0,$$
$$U_k=G_k^{-1}B^*L_{k+2}B\quad(0\le k\le\ell),$$
$$V_k=B_s(G_{k-2}^+)^{-1}B_s^*G_k\quad(2\le k\le\ell),
\qquad V_0=V_1=0.\tag{1.1}$$
$A_\ell=0$ 是真实最高第一上升块消失，不是虚构一个有限 $G_{\ell+1}$。
每个 $U_k,V_k$ 在 $G_k$ 度量中自伴且非负；例如
$$G_kU_k=B^*L_{k+2}B\succeq0,\quad
G_kV_k=G_kB_s(G_{k-2}^+)^{-1}B_s^*G_k\succeq0.$$
它们不因此在标准原内积或 $G_1$ 度量中非负。

使用 [R275 三次桥附录](R275-appendix-exact-cubic-bridge-for-shear-innovations.md) 已证的真 MP 两带分解，写实际两个下降 $D=X+Y$，其中 $X=D_1$ 保出生、降高度一，$Y=D_2$ 增出生一、降高度二。归一 MP 中
$$X\mathcal J_{k,s}=k\mathcal J_{k-1,s},\quad
X^*\mathcal J_{k,s}=(k+1)\mathcal J_{k+1,s}A_k,$$
$$Y^*\mathcal J_{k,s}=-\mathcal J_{k+2,s-1}B.$$
物理伴随给
$$YY^*\mathcal J_{k,s}=\mathcal J_{k,s}U_k,
\qquad Y^*Y\mathcal J_{k,s}=\mathcal J_{k,s}V_k.\tag{1.2}$$

## 2. 精确的出生保持 Serre 块

原 Boolean 关系为 $\operatorname{ad}_D^3D^*=0$。
在其中取出生保持块，只有两类词留下：纯 $X$ 与 $X^*$，或三个下降中恰一个 $Y$ 并以 $Y^*$ 为升项。因此完整块为
$$\operatorname{ad}_X^3X^*
+\operatorname{ad}_X^2[Y,Y^*]
+\operatorname{ad}_X[Y,[X,Y^*]]
+[Y,[X,[X,Y^*]]]=0.\tag{2.1}$$
这没有假设 $X,Y$ 交换。

直接用 (1.2) 及
$$[X,Y^*]\mathcal J_{k,s}=-2\mathcal J_{k+1,s-1}B,
\qquad [X,[X,Y^*]]\mathcal J_{k,s}=-2\mathcal J_{k,s-1}B$$
展开。对于 $k\ge2$，所有项均落在 $\mathcal J_{k-2,s}K_s$。去掉这个源单射后，纯第一带贡献是
$$k(k-1)\{(k+1)^2A_k-3k^2A_{k-1}
+3(k-1)^2A_{k-2}-(k-2)^2A_{k-3}\}.\tag{2.2}$$
$k=2$ 的末项因系数为零直接省略。

另三个项的准确贡献依次为
$$k(k-1)\{U_k-2U_{k-1}+U_{k-2}-V_k+2V_{k-1}-V_{k-2}\},$$
$$2\{(k-1)U_{k-1}-kU_{k-2}-(k-1)V_k+kV_{k-1}\},$$
$$2(U_{k-2}-V_k).\tag{2.3}$$
合并并除以 $k(k-1)$。若 $\Delta Z_k=Z_k-Z_{k-1}$ 表示向后差分，得到
$$\boxed{
\Delta^3[(k+1)^2A_k]
+\frac1k\Delta^2[kU_k]
-\frac1{k-1}\Delta^2[(k+1)V_k]=0,
\qquad2\le k\le\ell.
}\tag{2.4}$$
所有 $U,V$ 来自同一个实际 $C$ 与物理 MP，不是另设的独立正参数。

## 3. 有限顶端积分得到首边的准确身份

记 $p_k=(k+1)^2A_k$，并置 $p_{-1}=0$。由 (2.4)
$$\Delta^3p_k=F_k,
\qquad F_k=-\frac1k\Delta^2[kU_k]
+\frac1{k-1}\Delta^2[(k+1)V_k].$$
三次差分的有限求和给
$$p_j=(j+1)p_0+\frac{j(j+1)}2(p_1-2p_0)
+\sum_{k=2}^j\binom{j-k+2}2F_k.$$
用真实顶端 $p_\ell=0$ 解出 $p_1=4A_1$。

对 $U$ 部分作两次离散分部求和，准确得到
$$\sum_{k=2}^\ell\frac{\binom{\ell-k+2}2}{k}\Delta^2[kU_k]
=-\frac{\ell^2-1}{3}U_1
+(\ell+1)(\ell+2)\sum_{j=2}^\ell\frac{U_j}{(j+1)(j+2)}.$$
对 $V$ 部分，因 $V_0=V_1=0$，有
$$\sum_{k=2}^\ell\frac{\binom{\ell-k+2}2}{k-1}\Delta^2[(k+1)V_k]
=\ell(\ell+1)\sum_{j=2}^\ell\frac{V_j}{j(j-1)}.$$

于是首边算子满足完整身份
$$\boxed{\begin{aligned}
A_1={}&\frac{\ell-1}{2\ell}A_0
-\frac{\ell-1}{6\ell}U_1
+\frac{\ell+2}{2\ell}\sum_{j=2}^\ell
\frac{U_j}{(j+1)(j+2)}
-\frac12\sum_{j=2}^\ell\frac{V_j}{j(j-1)}.
\end{aligned}}\tag{3.1}$$
串长一时可约定 $A_1=0$，(3.1) 退化为恒等式 $0=0$；无需除零。串长零不使用此式。

目标首边准确等价于
$$G_1A_1\preceq I=G_1A_0.\tag{3.2}$$
(3.1) 把问题变成全部真实跨出生桥的带权积分控制，但右侧各桥不能逐项按 (3.2) 的度量判号。

## 4. 出生之间的精确迹消去

对所有出生恢复上标 $s$，$\ell_s=N-2s$。由定义，
$$\operatorname{tr}U_j^{(s)}
=\operatorname{tr}V_{j+2}^{(s-1)}.\tag{4.1}$$
这是同一对有限矩阵 $AB$ 与 $BA$ 的迹相等，且两边均非负。

将 (3.1) 乘 $\ell_s$ 后对所有 $\ell_s\ge1$ 的出生求迹。正 $U_j$（$j\ge2$）的系数为
$(\ell_s+2)/(2(j+1)(j+2))$，恰等于低出生中对应负 $V_{j+2}$ 的相反系数。因此所有这些项完全抵消，剩下
$$\boxed{\begin{aligned}
\sum_{s:\ell_s\ge1}\ell_s\operatorname{tr}A_1^{(s)}
={}&\frac12\sum_{s:\ell_s\ge1}(\ell_s-1)\operatorname{tr}A_0^{(s)}\\
&-\frac14\sum_{s\ge1:\ell_s\ge0}
\{(\ell_s+2)\operatorname{tr}U_0^{(s)}
+\ell_s\operatorname{tr}U_1^{(s)}\}.
\end{aligned}}\tag{4.2}$$
当 $\ell_s=0$，最后一项含 $\ell_sU_1$ 直接省略；其 $U_0$ 是真实最高出生的桥，仍保留。$\ell_s=1$ 时 $A_1=0$，上述边界系数仍准确。

这是一般权的精确加权迹身份；它不等于目标的范数界，也不能用迹循环性替代任意正向量态。目标矩阵包含 $G_1A_1$，在 (4.2) 左侧擅加不同 $G_1$ 会破坏 (4.1) 的抵消。

## 5. 固定度量最大原理仍缺什么

每个 $G_kU_k$、$G_kV_k$ 为正，但 (3.2) 使用 $G_1$。一般 $G_j$ 不交换；例如原四位权 $(1,2,3,5)$、出生一的 $G_1,G_2$ 已不交换。因此无法从 (3.1) 中直接删去所有带负系数的 $V_j$，也无法把正系数的 $U_j$ 当成一个可逐向量比较的正序列。

(4.1) 说明桥确实在出生之间传递同一有限能量，但目前仅用迹能无损闭合。要得到统一最大原理，需要一个保持原 $G_1$ 正态的跨出生运输，或把 (3.1) 的整个非交换和重写为同源正 Gram；两者均尚未证明。仅给 $\operatorname{tr}U_j=\operatorname{tr}V_{j+2}$ 不能声称该任务完成。

## 6. 独立精确校准

[脚本](../notes/2026-11-14-boolean-serre-first-edge-789f-next.py)直接由完整物理子集包含矩阵求各出生的 $G,L,G^+$，再由真实三次权删除生成 $B,B_s$。检查 $(N,s)=(4,1),(5,1),(6,2)$ 的所有合法递推及积分，实际输出

```text
PASS complete-Boolean birth-preserving Serre recurrences: 4
PASS finite-top integrated first-edge identities: 3
PASS weighted traces with even and odd top-birth boundaries: 2
No fixed-metric sign or universal adjacent bound is inferred.
```

精确验证只是校准公式与端点；一般恒等式的证明是 §§2–4。没有长计算，也没有使用本仓库 Actions。

一般出生首边、全部高度、原边界及普通 ISP 均仍开放。

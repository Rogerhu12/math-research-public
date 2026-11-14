# R239 附录：两异权尾的完整四矩返回几何及真实头条件障碍

日期：2026-11-13（UTC）。作者：boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：已证明；root 已独立核验全部旗、四矩递推、完整/裸最小化与强权反例；尚未证明原连续尾或实际见证源的线性返回费用界。

本文使用 [首段先消元稿](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md) 的原 Hilbert 范数、低出生链与完整最小修复。目的在于给一个已知 primitive Gram 相邻序成立的模型写出真正的头—尾 Schur 问题。本文不把相邻序直接当作返回费用估计。

## 1. 模型、全部旗与等权池约化

令有限头为 $\mathbb C^d$，$d\ge4$，标准头旗为
$$
W_k=\operatorname{span}\{e_0,\ldots,e_{k-1}\}.
$$
假设
$$
A W_k=W_{k-1}\quad(1\le k\le d),\qquad A^d=0.
\tag{1.1}
$$
两个原实际有限头 $A_m$ 都满足此条件。全部头内积仍为标准内积；本文没有将 $A$ 换成 Jordan 头后沿用旧范数。

尾算子取
$$
D=aE_1+bE_2+\varepsilon\sum_{j=3}^{M+2}E_j,
\qquad a,b,\varepsilon>0.
\tag{1.2}
$$
固定源孔数 $q\ge0$。沿用实际联合旗
$$
\mathscr C_{q,t}=\bigoplus_{i=0}^{d-t}e_i
\ker(D^{d-i}|_{\mathcal H_{q+t}}),\qquad 1\le t\le d,
$$
$$
\mathscr Y_{q,t}=\bigoplus_{i=0}^{d-t-1}e_i
\ker(D^{d-i-1}|_{\mathcal H_{q+t}}),\qquad 1\le t<d,
$$
以及
$$
Fc=Dc_1,\qquad (Sc)_t=Ac_t+Dc_{t+1}.
\tag{1.3}
$$
低出生是相对出生数不超过 $1$，高出生是相对出生数至少 $2$。在第 $q+t$ 层的
$U_{h,q+t}=\ker D^h\ominus\ker D^{h-1}$ 上，相对出生数为 $t-h+1$。
低链、裸最小源链和高完成均按这些正交子空间定义。

### 1.1 只可能有一类非零高返回源

按等权池的完整正交 primitive 串分解。若池内 primitive 向量出生于第 $j$ 层，则该串长度参数为
$$
L=M-2j.
$$
它与两个异权位张量后，同时约化 $D,D^*$，保持孔层，并酉等价于两个权 $a,b$ 的位加上 $L$ 个权 $\varepsilon$ 的池的对称部分。完整串分解及其端点已在
[两异权全出生 Gram 稿](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §9.1 证明。

每条这样的约化块，其相对 primitive 出生只可能为 $0,1,2$。这对短串也成立。确实，在任意相对第 $p\ge3$ 层，每个允许的头集合 $F\subseteq\{1,2\}$ 都有正池孔数 $p-|F|\ge1$。池删除在保持 $F$ 的对角项上非零，而异权位删除只减小 $F$。按头集合大小排列，这个矩阵三角且各存在的列都有非零的对应对角项，故 $D$ 在该层单射。连续应用即表明出生至少 $3$ 的所有删除核层均为零。

因此该串的绝对出生至多为 $j+2$。如果它在源第 $q$ 层非零，必须有 $j\le q$。高输出所需绝对出生至少为 $q+2$，所以：

- 若 $j<q$，该源块的高输出空间为零，因而 $B=0$、$L_{\rm eff}=0$；
- 若 $j>q$，它没有第 $q$ 层源，正交最小化时可删去整个零源块；
- 唯一可能产生高返回的是 $j=q$，且它的高出生恰好为 $q+2$。

所有分解均约化真实的伴随和正交投影，故完整逆、低链核与 Schur 补也按这些块分解。这不是先取逆再任意压缩。

在 $j=q$ 块，相对第 $0$ 层为一个真空。低前驱只有原第 $q$ 层，因此左源映射准确为
$$
E=A:\mathbb C^d\longrightarrow W_{d-1},\qquad
J_{\rm left}=AA^*|_{W_{d-1}}.
\tag{1.4}
$$
给定 $r\in W_{d-1}$，固定最小左前驱
$$
v=A^\dagger r\in(\ker A)^\perp,\qquad Av=r.
\tag{1.5}
$$

### 1.2 下文显式公式的长池边界

从现在起固定该 $j=q$ 块，并要求
$$
L=M-2q\ge d.
\tag{1.6}
$$
这样相对层 $2,\ldots,d$ 的四个异权占据状态都实际存在，所用 Gram 均为普通正定矩阵。层 $0,1$ 的缺失状态单独处理。没有使用奇异矩阵的形式逆。

§1.1 的唯一高返回块结论不需要 (1.6)。当 $L=0,1$ 时出生 $2$ 为空，高返回为零。其他短池必须保留真实缺失状态及右端约束；本文不把后面的长池公式原样用于这些短池。

## 2. 加权占据函数与四个真实矩

在相对第 $p$ 层写一个向量为
$$
u_p=
\sum_{\substack{I\subseteq[L+2]\\|I|=p}}
a^{I_1}b^{I_2}\varepsilon^{p-I_1-I_2}
f_p(I_1,I_2)e_I.
\tag{2.1}
$$
函数值及以下矩都可以是头向量。使用函数基
$$
1,\quad I_1,\quad I_2,\quad I_1I_2.
$$
其评价矩阵为
$$
T=
\begin{pmatrix}
1&0&0&0\\
1&1&0&0\\
1&0&1&0\\
1&1&1&1
\end{pmatrix}.
$$
令
$$
\begin{aligned}
\rho_{0,p}&=\varepsilon^{2p}\binom Lp,\\
\rho_{1,p}&=a^2\varepsilon^{2(p-1)}\binom L{p-1},\\
\rho_{2,p}&=b^2\varepsilon^{2(p-1)}\binom L{p-1},\\
\rho_{12,p}&=a^2b^2\varepsilon^{2(p-2)}\binom L{p-2}.
\end{aligned}
\tag{2.2}
$$
对 $2\le p\le d$，四者严格正。若函数系数列为 $\mathbf f_p$，其原范数为
$$
\|u_p\|^2=\mathbf f_p^* W_p\mathbf f_p,\qquad
W_p=T^*\operatorname{diag}(\rho_{0,p},\rho_{1,p},\rho_{2,p},\rho_{12,p})T.
$$
定义真实矩坐标
$$
m_p=W_p\mathbf f_p
=(m_{0,p},m_{1,p},m_{2,p},m_{12,p})^{\mathsf T}.
\tag{2.3}
$$
于是原范数准确等于
$$
\boxed{
\begin{aligned}
\mathcal N_p(m_p)={}&
\frac{\|m_{0,p}-m_{1,p}-m_{2,p}+m_{12,p}\|^2}{\rho_{0,p}}\\
&+\frac{\|m_{1,p}-m_{12,p}\|^2}{\rho_{1,p}}
+\frac{\|m_{2,p}-m_{12,p}\|^2}{\rho_{2,p}}
+\frac{\|m_{12,p}\|^2}{\rho_{12,p}}.
\end{aligned}}
\tag{2.4}
$$
这是将 $T^{-*}m_p$ 写出的恒等式，未改变范数。

在第 $1$ 层没有双占据状态，$m_{12,1}=0$，原范数为
$$
\mathcal N_1=
\frac{\|m_{0,1}-m_{1,1}-m_{2,1}\|^2}{L\varepsilon^2}
+\frac{\|m_{1,1}\|^2}{a^2}
+\frac{\|m_{2,1}\|^2}{b^2}.
\tag{2.5}
$$
第 $0$ 层只有 $m_{0,0}=v$，范数为 $\|v\|^2$。

### 2.1 真实伴随给完全去耦的矩递推

对任意 $F\subseteq\{1,2\}$，定义整层函数向量
$$
\Phi_{F,p}=\sum_{|I|=p}a_I I_F(I)e_I,
$$
其中 $a_I$ 表示 (2.1) 的完整占据权乘积。直接逐集合核验
$$
D^*\Phi_{F,p-1}=(p-|F|)\Phi_{F,p}.
$$
确实，在固定 $p$ 元集合 $J$ 上，能删除且保留 $I_F=1$ 的位共有 $p-|F|$ 个。因此，在函数基中
$$
D^*:\mathbf f_{p-1}\longmapsto
\operatorname{diag}(p,p-1,p-1,p-2)\mathbf f_{p-1}.
\tag{2.6}
$$
在低端只保留实际存在的列。转回矩坐标，$D$ 的作用是相同对角矩阵乘以上一层的矩，因而完整核方程 $(A+D)u=0$ 等价于
$$
A m_p+
\operatorname{diag}(p+1,p,p,p-1)m_{p+1}=0.
\tag{2.7}
$$
这里的 $A$ 仍是原有限头，作用于每个矩的头分量。它未与任何头伴随或 Schur 逆换序。

## 3. 所有完整链与所有裸低链的精确最小化

取 $u_0=v$，并令 $u_p=-c_p$（$p\ge1$）。于是完整核方程等价于
$$
Fc=r,\qquad Sc=0.
$$
由 (2.7)，其四矩准确为
$$
\boxed{
\begin{aligned}
m_{0,p}&=\frac{(-A)^p}{p!}v,\\
m_{1,p}&=\frac{(-A)^{p-1}}{(p-1)!}x_1,\qquad
m_{2,p}=\frac{(-A)^{p-1}}{(p-1)!}x_2
\quad(p\ge1),\\
m_{12,p}&=\frac{(-A)^{p-2}}{(p-2)!}y
\quad(p\ge2),
\end{aligned}}
\tag{3.1}
$$
其中自由初值的准确头空间为
$$
x_1,x_2\in\mathbb C^d,\qquad y\in W_{d-1}.
\tag{3.2}
$$
负阶项不出现；$m_{12,1}=0$。

这些公式保全部联合旗。第 $p$ 层的头支撑在 $W_{d-p+1}$；真空出生的矩 $m_{0,p}$ 甚至在 $W_{d-p}$。同时，完整核方程在每个头坐标上给
$$
D u_i=-\sum_{j>i}A_{ij}u_j.
$$
从最高头向下归纳即有 $D^{d-i}u_i=0$，故每一孔层都满足原逐头删除核旗。由 (3.2)，第 $d+1$ 层的全部矩为零；没有未付的末端输出。

反过来，任意完整合法链必满足 (2.7)，所以它唯一给出 (3.1) 的 $x_1,x_2,y$。因此
$$
\boxed{
\lambda(r)^2=
\min_{\substack{x_1,x_2\in\mathbb C^d\\y\in W_{d-1}}}
\left[
\mathcal N_1+
\sum_{p=2}^d
\mathcal N_p\!\left(
m_{0,p},m_{1,p},m_{2,p},
\frac{(-A)^{p-2}y}{(p-2)!}
\right)
\right].
}
\tag{3.3}
$$
这是整个原链空间的最小值，不是某一试探子空间的值。第 $0$ 层的 $\|v\|^2$ 不计入修复费。

### 3.1 裸低链对应逐孔自由的末矩

在第 $p$ 层，出生 $0,1$ 的正交和恰是函数
$$
1,\ I_1,\ I_2
$$
张成的空间。准确地说，反复应用 (2.6) 给
$$
\operatorname{Ran}(D^*)^{p-1}|_{\mathcal H_1}
=\operatorname{span}\{\Phi_{\varnothing,p},\Phi_{\{1\},p},\Phi_{\{2\},p}\}
=(\ker D^{p-1}|_{\mathcal H_p})^\perp
$$
在当前约化串上成立；三个上升系数均非零。该空间就是出生 $0,1$ 的正交和。出生 $2$ 是其正交补。

保持前三矩而自由改变末矩，正是同一低出生投影的全部原像。因而低投影的平方范数为
$$
\min_{z\in W_{d-p+1}}\mathcal N_p(m_{0,p},m_{1,p},m_{2,p},z).
\tag{3.4}
$$
$D^*$ 保低函数跨度，所以低输出方程只依赖前三矩。这些方程仍准确给 (3.1) 的前三行，且 $x_1,x_2$ 任意。逐孔低投影保头支撑：其出生 $0$ 分量只由 $m_{0,p}\in W_{d-p}$ 决定，出生 $1$ 分量在 $W_{d-p+1}$。故低链也在原联合旗内。

记裸最小低链为 $a(r)$，其范数为 $b(r)=\|a(r)\|$。于是
$$
\boxed{
b(r)^2=
\min_{x_1,x_2\in\mathbb C^d}
\left[
\mathcal N_1+
\sum_{p=2}^d
\min_{z_p\in W_{d-p+1}}
\mathcal N_p(m_{0,p},m_{1,p},m_{2,p},z_p)
\right].
}
\tag{3.5}
$$
全部最小化是有限维正定二次型最小化。初值在第 $1$、第 $2$ 层的矩可恢复，因此没有未商掉的参数核。

### 3.2 回归形式及真正未付的约束

置
$$
\omega_p=\rho_{0,p}^{-1}+\rho_{1,p}^{-1}
+\rho_{2,p}^{-1}+\rho_{12,p}^{-1}.
$$
逐孔最优末矩为
$$
z_p^\star=
\omega_p^{-1}
\left[
-\frac{m_{0,p}-m_{1,p}-m_{2,p}}{\rho_{0,p}}
+\frac{m_{1,p}}{\rho_{1,p}}
+\frac{m_{2,p}}{\rho_{2,p}}
\right].
\tag{3.6}
$$
准确完成平方给
$$
\mathcal N_p(m_{\rm low},z)=
\min_\zeta\mathcal N_p(m_{\rm low},\zeta)
+\omega_p\|z-z_p^\star\|^2.
\tag{3.7}
$$
因此完整费用与裸费用的区别，是在同时优化两个出生 $1$ 初值的同时，必须用同一个头向量 $y$ 满足
$$
z_p=\frac{(-A)^{p-2}y}{(p-2)!}
\quad\text{对每个 }p.
\tag{3.8}
$$
不能把逐孔最优 $z_p^\star$ 当作已经满足这个完整头递推。也不能在 (3.3) 中使用 (3.5) 的最优初值后省去再次最小化。

沿首段先消元稿的坐标，准确有
$$
\lambda(r)^2=b(r)^2+
\langle L_{\rm eff}a(r),a(r)\rangle,\qquad
\langle Q_-a(r),a(r)\rangle=\|A^\dagger r\|^2.
\tag{3.9}
$$
所以 (3.3)—(3.8) 是这两个真实正算子在当前模型上的完整有限接口。没有将它们替换成普通 $D$ 的压缩 Gram。

## 4. 强异权极限确实排除普适平方比较

本节固定 $A,d,L$，取
$$
\varepsilon=1,\qquad a=b=R\longrightarrow\infty.
\tag{4.1}
$$
取 $v\in(\ker A)^\perp$ 且 $A^3v\ne0$，令 $r=Av$。例如 $v=e_3$ 对任何满足 (1.1) 的头都合法。

### 4.1 裸费用趋于零

在 (3.5) 中取
$$
x_1=x_2=-Av/2.
$$
于是
$$
m_{1,p}=m_{2,p}=\frac p2\,m_{0,p}.
$$
逐孔试取
$$
z_p=(p-1)m_{0,p}\quad(p\ge2).
$$
第 $1$ 层及所有高层的无异权占据项均为零。代入 (2.4)—(2.5)，得到
$$
\begin{aligned}
b_R(r)^2\le{}&
\frac1{R^2}\sum_{p=1}^d
\frac{(2-p)^2}{2\binom L{p-1}}\|m_{0,p}\|^2\\
&+\frac1{R^4}\sum_{p=2}^d
\frac{(p-1)^2}{\binom L{p-2}}\|m_{0,p}\|^2
=O(R^{-2}).
\end{aligned}
\tag{4.2}
$$
这里是合法的裸范数上界：即使所选 $z_p$ 不是 (3.6) 的最优末矩，投到低出生空间后前三矩不变，范数只会减少。

### 4.2 完整费用有正的固定下界

写 $x=x_1+x_2$。完整链前三个无异权占据矩为
$$
\begin{aligned}
k_1&=-Av-x,\\
k_2&=A^2v/2+Ax+y,\\
k_3&=-A^3v/6-A^2x/2-Ay.
\end{aligned}
$$
准确有
$$
\boxed{
k_3+A k_2+\frac12 A^2k_1=-\frac16A^3v.
}
\tag{4.3}
$$
因此由加权 Cauchy 不等式，任意完整链都满足
$$
\boxed{
\lambda_R(r)^2\ge
\frac{\|A^3v\|^2}
{36\left[
\binom L3+\|A\|^2\binom L2+\frac14\|A^2\|^2L
\right]}
=:c_{A,L,v}>0.
}
\tag{4.4}
$$
只使用了原范数中前三个正项
$\sum_{p=1}^3\|k_p\|^2/\binom Lp$；其余项均非负。该下界与 $R$ 无关。

### 4.3 排除的准确算子不等式

令 $a_R=a_R(r)$，$L_R=L_{{\rm eff},R}$。由 (3.9)、(4.2)、(4.4)，
$$
\langle L_Ra_R,a_R\rangle
=\lambda_R(r)^2-b_R(r)^2\ge c_{A,L,v}/2
$$
对充分大 $R$ 成立。另一方面，
$$
\|L_Ra_R\|^2
\ge
\frac{\langle L_Ra_R,a_R\rangle^2}{\|a_R\|^2}
\longrightarrow\infty.
\tag{4.5}
$$
但
$$
\langle(I+Q_{-,R})a_R,a_R\rangle
=b_R(r)^2+\|v\|^2
$$
有界。因此不存在仅依赖固定 $A,d,L$ 的有限常数 $C$，使全参数族满足
$$
L_R^2\le C(I+Q_{-,R}).
\tag{4.6}
$$
特别，系数 $1$ 的平方比较已被这个模型严格排除。

这个族的完整 primitive Gram 仍满足已证的两异权全部出生相邻不等式及其倒数权加强。所以相邻 Gram 序本身不蕴含 (4.6)；完整头递推及 Schur 优化不能跳过。

## 5. 保留的范围与线性问题

本节反例没有排除较弱的
$$
L_{\rm eff}\le C(I+Q_-).
\tag{5.1}
$$
事实上在 (4.1) 中，直接在 (3.3) 取 $x_1=x_2=y=0$，便给准确上界
$$
\lambda_R(r)^2
\le
\sum_{p=1}^d\frac{\|A^pv\|^2}{(p!)^2\binom Lp}
\le C_{A,L}\|v\|^2,
\tag{5.2}
$$
常数与 $R$ 无关。由 (3.9)，这甚至给当前强权族上的
$L_R\le C_{A,L}Q_{-,R}$。因而强权例恰好允许 $L_R,Q_{-,R}$ 在相同尺度增长，不能用它否定线性目标。

反例中的 $a=b=R$ 不满足原连续尾的小范数条件。不能通过共同缩放得到“固定原 $A$、固定 $a=b=\delta\le1/m$、池权 $\varepsilon\to0$”的反例：将尾除以 $\varepsilon$ 时，核方程中的有限头同时变成 $A/\varepsilon$。本文一直在 (2.2) 显式保留 $\varepsilon$，没有偷换这个头。

对于固定原头、固定小异权及趋零池权，(3.3)—(3.8) 仍是完整正确的有限最小化，但本稿没有证明该极限的平方或线性比失控。一般原连续尾和同一 $w\in M\ominus N$ 产生的窄实际源，更没有被此环境族排除。当前可继续使用的目标是实际源上足够温和的线性比较或等价的真实返回预算。


## 6. 小尾范数仍不能消除任意单移位头的条件

本节给另一个明确的范围边界：令头随参数改变。它不涉及固定原 $A_m$ 的弱池极限，也不否定原 dyadic 两头的特殊结构。

固定 $d\ge4$、$L\ge d$、$\delta>0$。取一个真实正权单移位头 $A_\varepsilon$，前三条相关边准确为
$$
A_\varepsilon e_3=e_2,\qquad
A_\varepsilon e_2=\varepsilon e_1,\qquad
A_\varepsilon e_1=\varepsilon e_0.
\tag{6.1}
$$
若 $d>4$，其余边取任意固定的 $(0,1]$ 内正权；取 $0<\varepsilon\le1$，则 $\|A_\varepsilon\|=1$。尾取
$$
a=b=\delta,\qquad \text{池的共同权为 }\varepsilon.
\tag{6.2}
$$
固定 $v=e_3$、$r=A_\varepsilon v=e_2$，因此左最小费用恰为
$$
\mu(r)^2=\|v\|^2=1.
$$

### 6.1 最小化确实只剩三个标量

头指标与相对孔数之和是一个正交分级。$A_\varepsilon+D$ 把总级数准确降低一次；删除核的出生投影也保持这个分级。因此源 $r=e_2$ 的完整及裸最小链，都可正交投到总级数 $3$ 而不改变源、不增加范数。其他总级数只贡献零源链。

于是 (3.1) 中准确有
$$
x_1=-u_1e_2,\qquad x_2=-u_2e_2,\qquad
y=\varepsilon z e_1
$$
对两个复数 $u_1,u_2$ 和一个复数 $z$。非零孔层只有 $p=1,2,3$。令 $u=u_1+u_2$，则
$$
m_{0,1}=-e_2,\qquad
m_{0,2}=\frac{\varepsilon}{2}e_1,\qquad
m_{0,3}=-\frac{\varepsilon^2}{6}e_0,
$$
且
$$
m_{i,p}=p u_i m_{0,p},\qquad
m_{12,p}=p(p-1)z m_{0,p}.
\tag{6.3}
$$
这一步使用了真实单移位头的正交总级数，不能用于任意上三角头或直接用于两个原 $A_m$。

### 6.2 完整费用至少按 $\varepsilon^{-2}$ 增长

置
$$
P(p)=1-pu+p(p-1)z.
$$
仅保留无异权占据的三个正项，就得到
$$
\lambda_\varepsilon(r)^2
\ge
\varepsilon^{-2}
\sum_{p=1}^3
\frac{|P(p)|^2}{(p!)^2\binom Lp}.
\tag{6.4}
$$
二次多项式 $P$ 满足 $P(0)=1$，所以准确有
$$
P(3)-3P(2)+3P(1)=1.
$$
对这个恒等式用加权 Cauchy 不等式：
$$
\boxed{
\lambda_\varepsilon(r)^2
\ge
\frac{\varepsilon^{-2}}
{36\left[\binom L3+\binom L2+L/4\right]}
=:c_L\varepsilon^{-2}.
}
\tag{6.5}
$$
没有以参数试验替代这个正下界，也没有遗漏复参数的可能性。

### 6.3 裸费用保持有界

在 (3.5) 中取 $u_1=u_2=1/2$，并逐孔选择
$$
z_p=(p-1)m_{0,p}.
$$
与 §4.1 相同，无异权占据项全部为零。逐层代入带 $\varepsilon$ 的真实权 (2.2)，准确给
$$
\boxed{
b_\varepsilon(r)^2
\le
\frac1{\delta^2}
\left(\frac12+\frac1{72\binom L2}\right)
+\frac{\varepsilon^2}{\delta^4}
\left(\frac14+\frac1{9L}\right).
}
\tag{6.6}
$$
第 $1$ 层给 $1/(2\delta^2)$；第 $2$ 层只剩
$\varepsilon^2/(4\delta^4)$；第 $3$ 层给
$1/[72\delta^2\binom L2]+\varepsilon^2/(9\delta^4L)$。
这个上界对 $\varepsilon\downarrow0$ 有界。

因此在同一个裸最小状态 $a_\varepsilon=a_\varepsilon(r)$ 上，
$$
\boxed{
\frac{\langle L_{{\rm eff},\varepsilon}a_\varepsilon,
a_\varepsilon\rangle}
{\langle(I+Q_{-,\varepsilon})a_\varepsilon,a_\varepsilon\rangle}
=
\frac{\lambda_\varepsilon(r)^2-b_\varepsilon(r)^2}
{1+b_\varepsilon(r)^2}
\longrightarrow\infty.
}
\tag{6.7}
$$

### 6.4 排除范围及原头守卫

所以，线性比较 $L_{\rm eff}\le C(I+Q_-)$ 的常数不能只由头维数、头范数及尾范数上界控制，而完全忽略真实头权的条件。当前例始终有 $\|A_\varepsilon\|=1$，且完整尾满足
$$
\|D\|\le2\delta+M\varepsilon.
$$
给定任意小正上界，先固定足够小的 $\delta$、再令 $\varepsilon\downarrow0$，尾范数就保持在该上界之内。若要放在原第 $q$ 层，可取 $M=2q+L$ 并使用 §1.1 的池出生 $j=q$ 块；该块存在且保持全部真实旗。

本例的两个相邻小头权是 $[\varepsilon,\varepsilon]$，头本身随 $\varepsilon$ 改变。它没有证明固定原 $A_m$ 的线性比较失败。原底层 odometer 单移位的连续边权是 $\alpha_{v_2(k)}$，不能把 (6.1) 的任意权排列代入它；而两个实际头还是该底层单移位的指定多项式/有理函数，亦不得把它们直接叫作单移位。

本例同时说明：已证两异权 primitive Gram 邻阶序与一个普通小尾范数，仍不足以推出原需要的统一线性预算。后续必须使用两个原有限头的具体结构，或原 $w\in M\ominus N$ 所产生源的附加限制。

## 7. 真空出生块的三 Gram 观测：完整逆、规范约束和原头结构

本节是 §§1–4 四矩模型的准确坐标接口，不新增三 Gram 上界。
特别不把 §5 的平方比较反例、§6 的任意头线性反例或单个方向的
$\mu^2/\lambda^2$ 比值，冒充以下非交换观测量。

### 7.1 范围及原左坐标

继续同一二异常位加等权池的有限模型，并固定唯一可能产生高返回的
$j=q$ 池原始串。该串的相对真空记为 $\Omega_q$，长度为
$$
L=M-2q\ge d.
$$
本节每个头向量均张量这一固定单位真空；这一因子在记号中省略。
$A$ 为 §§1–4 的真实正则上三角头，$\ker A=\mathbb C e_0$。
置
$$
V=(\ker A)^\perp,\qquad R=\operatorname{Ran}A,\qquad
A_0=A|_V:V\longrightarrow R.
\tag{7.1}
$$
$A_0$ 是两个原 Hilbert 子空间间的有界同构，不是一个相似变换。
它的逆范数可以很大；下文并未先忽略该范数。

对 $v\in V$，令
$$
r=A_0v.
$$
因为 $\Omega_q$ 被整个纯尾 $D$ 杀掉，只有第 $q$ 孔层、头向量为 $v$
的左链已经满足全部低输出方程，且顶端源为 $r$。

另一方面，任何左零源链的第 $q$ 层都满足 $Au_q=0$，
所以其顶端头分量属于 $\ker A$。
上述链的其他层为零，且 $v\perp\ker A$，故它对全部左零源链正交。
因此它确为原左最小原像，并有
$$
\boxed{\mu(r)^2=\|v\|^2.}
\tag{7.2}
$$
这一步使用真实左核，不把一个方便构造的前驱误认成最小者。

### 7.2 完整与裸四矩费用的正矩阵

将 §§3–4 的两个真实最小化定义为 $V$ 上的正矩阵
$$
\boxed{
\lambda(A_0v)^2=\langle F_{\rm full}v,v\rangle,\qquad
\alpha(A_0v)^2=\langle F_{\rm bare}v,v\rangle,
}
\tag{7.3}
$$
其中 $\alpha(r)=\|\mathsf f^{-1}r\|$ 是真正裸最小费用。
这里 $F_{\rm full}$ 保留同一末矩 $y$ 的全阶递推；
$F_{\rm bare}$ 才允许每一阶独立消去末矩。
二者由原四矩的完整 Schur 补得到，不逐头删去未知量。

因为 $L\ge d$，前文的所有尾权分母在所用层上为正，
完整及裸最小化都定义于全部 $V$。
固定模型有限维，$A_0$ 单射，首输出非零时任一可行链都有正范数，
所以
$$
0<F_{\rm bare}\le F_{\rm full}<\infty.
\tag{7.4}
$$
不声称其最小特征值对任何小参数一致。

若 $G,J_{\rm bare},J$ 分别是完整右源、裸右源、左源 Gram，
则按原源范数的定义，准确有
$$
\boxed{
G=A_0F_{\rm full}^{-1}A_0^*,\qquad
J_{\rm bare}=A_0F_{\rm bare}^{-1}A_0^*,\qquad
J=A_0A_0^*.
}
\tag{7.5}
$$
这些算子全部作用在 $R$；$A_0^*$ 的输出空间是 $V$。
例如
$G^{-1}=(A_0^{-1})^*F_{\rm full}A_0^{-1}$，
所以 (7.5) 是真实正合同的逆，不交换两个 Gram。

### 7.3 廉价变换源恰读取完整费用矩阵的逆

原变换源为
$$
r^\flat=GJ^{-1}r.
$$
代入 (7.5) 时，需保留如下次序：
$$
\begin{aligned}
r^\flat
&=A_0F_{\rm full}^{-1}A_0^*
  (A_0A_0^*)^{-1}A_0v\\
&=A_0F_{\rm full}^{-1}v,
\end{aligned}
\tag{7.6}
$$
最后一步使用有界同构的准确恒等式
$A_0^*(A_0A_0^*)^{-1}A_0=I_V$。
因此
$$
\boxed{
\lambda(r^\flat)^2
=\langle F_{\rm full}^{-1}v,v\rangle.
}
\tag{7.7}
$$
大的 $A_0^{-1}$ 并不是在估计中被放弃；它与左源 Gram 的因子按上述
准确次序消掉了。剩下的 $F_{\rm full}^{-1}$ 仍是完整矩阵逆。

由 (7.2)、(7.3)、(7.7)，这个源块上的三 Gram 目标
$$
\mu(r)^2\le C\bigl(\alpha(r)^2+\lambda(r^\flat)^2\bigr)
$$
恰好等价于
$$
\boxed{I_V\le C\bigl(F_{\rm bare}+F_{\rm full}^{-1}\bigr).}
\tag{7.8}
$$
这是要证明的一个矩阵序，本文没有给出 $C$ 的统一上界。

一般仅有 Cauchy--Schwarz
$$
\|v\|^4\le
\langle F_{\rm full}v,v\rangle
\langle F_{\rm full}^{-1}v,v\rangle.
\tag{7.9}
$$
因此 $\mu(r)^4/\lambda(r)^2$ 只是 (7.7) 的下界；
除非 $v$ 落在 $F_{\rm full}$ 的单一特征子空间，不能用它代替
(7.7)。这正是单方向费用比不能判断 (7.8) 的原因。

### 7.4 同返回源规范在这些坐标中的准确形式

令
$$
T:V\longrightarrow\mathcal U,\qquad T v=\mathsf f^{-1}A_0v.
$$
这里 $\mathcal U$ 限制为该固定池串和相对真空首源对应的裸最小状态子空间；$T$ 是到这一子空间的有界同构，且
$$
T^*T=F_{\rm bare},\qquad
T^*\mathcal Q T=I_V,\qquad
T^*\mathcal P T=F_{\rm full},
\quad \mathcal P=I+\mathscr L.
\tag{7.10}
$$
尤其
$$
\mathcal K:=\ker(B_AT)
=\ker(F_{\rm full}-F_{\rm bare}).
\tag{7.11}
$$
理由是完整最小能量超过裸能量的部分，准确为
$\langle\mathscr L T v,T v\rangle$；
它为零当且仅当原裸链自身已无高返回。

所以同返回源规范 $a^\sharp=Tv^\sharp$ 对应
$$
\boxed{
v^\sharp\perp_{\,F_{\rm bare}+I_V}\mathcal K.
}
\tag{7.12}
$$
对任意 $v$，其规范校正满足 $e=v-v^\sharp\in\mathcal K$，
并在原度量中最小化
$$
\langle(F_{\rm bare}+I_V)u,u\rangle
\quad\text{且}\quad B_ATu=B_ATv.
$$
对 $e\in\mathcal K$ 只有
$F_{\rm full}e=F_{\rm bare}e$；
不能把它们在这些非等距坐标中都写成 $e$。

记
$$
\delta^2=\langle(F_{\rm bare}+I_V)e,e\rangle.
$$
由 (7.12)，
$$
\begin{aligned}
\delta^2
&=\langle(F_{\rm bare}+I_V)v,e\rangle\\
&\le
\bigl(\alpha(A_0v)+\lambda((A_0v)^\flat)\bigr)
\langle F_{\rm bare}e,e\rangle^{1/2}\\
&\le
\bigl(\alpha(A_0v)+\lambda((A_0v)^\flat)\bigr)\delta.
\end{aligned}
$$
第二行分别对 $F_{\rm bare}$ 内积和
$F_{\rm full}^{-1/2},F_{\rm full}^{1/2}$ 配对使用 Cauchy--Schwarz，
并用 $e\in\mathcal K$。
因此
$$
\delta\le\alpha(r)+\lambda(r^\flat).
\tag{7.13}
$$
这只是既有同源规范估计在四矩坐标中的复核，不重计为新规范定理。

### 7.5 两个实际头的额外结构及范围守卫

[R249 的真实头表示](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)
写原两型头（$d=2^m$）为同一加权移位 $B_m$ 的实系数有限幂级数。
其边权为 $\alpha_{\nu_2(k)}$，且对 $1\le k\le d-1$，
$$
\nu_2(d-k)=\nu_2(k).
$$
若 $\mathcal R e_i=e_{d-1-i}$，则
$$
\mathcal R B_m\mathcal R=B_m^*,\qquad
\boxed{\mathcal R A_m\mathcal R=A_m^*.}
\tag{7.14}
$$
多项式和截断有理式都保留这个恒等式。

但 $\mathcal R$ 把 $V=e_0^\perp$ 送到 $e_{d-1}^\perp$，
不是 $V$ 的自同构。因此 (7.14) 不能直接当成
$F_{\rm full}$ 或 $F_{\rm bare}$ 在同一个 $V$ 上的交换式。
更不能删掉原 $b_jN_j$ 的长跳跃，只用回文第一上对角线替代原头。

(7.8) 保留全部真实长跳跃和原末矩递推，是本节用于后续解析比较的接口。
原实际 $W$ 来源还同时满足已经支付的
$\alpha(r),\lambda(r^\flat)\le\beta+\mathrm{carry}$；
单独的 (7.12) 不代替这两项，更不代替真正窄 $\overline f$ 的来源。
本节仍只在所述 $j=q,L\ge d$ 模型内完成字典，没有把它当作原连续尾的
全源分解或无权 $N=M$ 的证明。

## 8. 反对角对称头仍不能单独支付三 Gram：八头起的准确反例

本节否定一个比原目标更宽的候选：
仅凭固定头维数、头尾范数上界、正则上三角和反对角对称，
不能给 (7.8) 的统一常数。
这里的头随 $t$ 改变，并非原两型 $A_m$；
原 $b_jN_j$ 长跳跃不能由这个模型替代。

### 8.1 回文头、固定源和可小的尾范数

固定任意 $d\ge8$，特别可以取 $d=2^m$、$m\ge5$。
对 $0<t<1$，令
$$
A_te_j=w_j(t)e_{j-1}\quad(1\le j\le d-1),\qquad A_te_0=0,
$$
其中
$$
w_1=w_{d-1}=1,\qquad
w_2=w_{d-2}=t^4,\qquad
w_3=w_{d-3}=t^2,\qquad
w_4=w_{d-4}=t,
\tag{8.1}
$$
其余权取 $1$；$d=8$ 时重复的中间定义一致。
因此
$$
\ker A_t=\mathbb Ce_0,\qquad
\|A_t\|=1,\qquad
\mathcal R A_t\mathcal R=A_t^*,\qquad
\mathcal R e_i=e_{d-1-i}.
\tag{8.2}
$$
尤其两个端点权都是 $1$，并非通过让整个头趋零制造反例。

取同一双异常尾
$$
a=b=\delta>0,\qquad \varepsilon=t^2,
$$
其中 $\delta$ 固定。固定池原始出生 $j=q$，令
$$
L=M-2q\ge d.
$$
以下均在这一固定单位原始串上。
尾的整个有限 Boolean 算子满足
$$
\|D_t\|\le2\delta+Mt^2.
\tag{8.3}
$$
故先固定任意小的 $\delta$，再令 $t$ 足够小，尾范数可以保持在预先给定的小上界内。
若希望同时用形式上的原窗口参数，可固定 $q=4d$、$M=2q+L$，
取 $\delta\le1/(4m)$ 及 $Mt^2\le1/(2m)$，则 $\|D_t\|\le1/m$。
这仍是有限任意权尾，不是原连续权尾。

令
$$
v=e_4,\qquad r_t=A_tv=t e_3.
\tag{8.4}
$$
由 (7.2)，这个源的真正左最小费用恒为
$$
\boxed{\mu(r_t)=1.}
\tag{8.5}
$$

### 8.2 全部最小化及完整逆都按总级数正交分块

在所选池原始串中，记尾相对孔数为 $p$，并在
$e_i\otimes\mathcal H_{q+p}$ 上取总级数 $i+p$。
纯单移位 $A_t$ 与尾删除 $D_t$ 都把总级数降低一。

所有原头截止、固定孔层及尾核旗投影均保持这个分解。
完整链约束和裸低出生约束因此也按总级数分别成立，
原 Hilbert 范数则是这些块的正交平方和。
对一个固定总级数的源，可把任意可行链正交投到该级数：
保留全部约束且不增加范数。

特别，边界头基向量 $e_\ell$ 的最小链只读取总级数 $\ell$，
不同 $\ell$ 的完整最小链彼此正交；裸最小链也彼此正交。
因此第7节的两个真实费用矩阵在
$V=\operatorname{span}\{e_1,\ldots,e_{d-1}\}$ 上都为对角矩阵：
$$
\boxed{F_{\rm full}(t),\ F_{\rm bare}(t)\ \text{在原头基中同时对角}.}
\tag{8.6}
$$
这不使用两个不同最小逆之间的交换式。

对 (8.4)，总级数是 $4$，第 $p$ 段的头只能是 $e_{4-p}$，
且 $1\le p\le4$。这些坐标满足全部原头截止。
相对孔数为 $p$ 的尾向量被 $D_t^{p+1}$ 杀掉；
又 $d-(4-p)\ge p+1$，所以逐头核旗也全部满足。
没有为了取得下界删掉一个可降低能量的头方向。

### 8.3 四个真矩和裸费用的完整上界

四矩式在本块给
$$
\begin{aligned}
m_{0,1}&=-t e_3,&
m_{0,2}&=\frac{t^3}{2}e_2,\\
m_{0,3}&=-\frac{t^7}{6}e_1,&
m_{0,4}&=\frac{t^7}{24}e_0,
\end{aligned}
\tag{8.7}
$$
而 $p\ge5$ 的全部矩为零。

全部完整可行参数恰为
$$
x_i=-t u_i e_3\ (i=1,2),\qquad y=t^3z e_2,
$$
于是
$$
m_{i,p}=p u_i m_{0,p},\qquad
m_{12,p}=p(p-1)z m_{0,p}.
\tag{8.8}
$$
这个参数范围由 §8.2 的正交投影和原四矩的完整参数化得到；
不是只在某一试探子族上取最小。

裸费用允许每一层独立消去最后一个矩。
取
$$
u_1=u_2=\frac12,\qquad m_{12,p}=(p-1)m_{0,p}.
\tag{8.9}
$$
池单独占据项在每层准确为零。
把 (8.7)--(8.9) 逐项代入原范数，得到
$$
\begin{aligned}
\alpha(r_t)^2\le{}&
t^2\left(\frac1{2\delta^2}
 +\frac1{288\delta^2\binom L3}\right)\\
&+t^6\left(\frac1{4\delta^4}
 +\frac1{72\delta^2\binom L2}
 +\frac1{64\delta^4\binom L2}\right)
+\frac{t^{10}}{9\delta^4L}.
\end{aligned}
\tag{8.10}
$$
因此存在只依赖固定 $\delta,L$ 的有限常数 $C_b$，使
$$
\boxed{\alpha(r_t)^2\le C_b t^2.}
\tag{8.11}
$$
(8.10) 只用于真正裸最小值的上界，未称试探链必为极小者。

### 8.4 真实完整费用的三点下界

对任意完整参数 (8.8)，记
$$
P(p)=1-p(u_1+u_2)+p(p-1)z.
$$
它是次数至多二且 $P(0)=1$ 的多项式。
池单独占据部分的残量是 $P(p)m_{0,p}$。
保留 $p=1,2,4$ 三个非负费用项，即得
$$
\lambda(r_t)^2\ge
t^{-2}\left(
 \frac{|P(1)|^2}{L}
 +\frac{|P(2)|^2}{4\binom L2}
 +\frac{|P(4)|^2}{576\binom L4}
\right).
\tag{8.12}
$$
第3层和全部含异常位的费用仍非负，所以删去它们只降低右侧。

对所有这样的二次多项式，Lagrange 恒等式准确为
$$
\frac83P(1)-2P(2)+\frac13P(4)=P(0)=1.
\tag{8.13}
$$
加权 Cauchy--Schwarz 给
$$
\boxed{
\lambda(r_t)^2\ge\frac{t^{-2}}{C_L},\qquad
C_L=\frac{64L}{9}+16\binom L2+64\binom L4.
}
\tag{8.14}
$$
该下界对全部完整参数成立，故对真正完整最小值成立。

### 8.5 廉价变换源趋零，三 Gram 的统一常数发散

现在必须使用 (8.6)，而不是把 (7.9) 的下界倒当等式。
因为 $e_4$ 是完整费用矩阵的特征向量，
$$
F_{\rm full}(t)e_4=\lambda(r_t)^2 e_4.
$$
于是第7节的准确变换源公式给
$$
\boxed{
\lambda(r_t^\flat)^2
=\langle F_{\rm full}(t)^{-1}e_4,e_4\rangle
=\lambda(r_t)^{-2}
\le C_Lt^2.
}
\tag{8.15}
$$
结合 (8.5)、(8.11)，
$$
\boxed{
\mu(r_t)=1,\qquad
\alpha(r_t)\longrightarrow0,\qquad
\lambda(r_t^\flat)\longrightarrow0.
}
\tag{8.16}
$$
因此任何满足本族三 Gram 比较的常数都至少为
$$
C(t)\ge\frac1{(C_b+C_L)t^2}\longrightarrow\infty.
\tag{8.17}
$$
固定 $d$、$\|A_t\|=1$、预定小尾范数上界和反对角对称均不能阻止这一点。

本族还通过单独的同返回源规范：
对足够小的 $t$，(8.11)、(8.14) 使
$\lambda(r_t)^2>\alpha(r_t)^2$，所以本一维总级数源块上的 $B_AT$
非零，核为零。其他总级数和池原始串都是正交约化块。
故本源的裸状态本身已对整个 $\ker B_A$ 按 $I+\mathcal Q$ 正交。
这说明把同源规范再加到反对角对称上，仍不足以支付 (7.8)。

### 8.6 与原实际来源的区别

(8.1) 含连续小瓶颈且没有原 $b_jN_j$ 的长跳跃，
所以它不是原两个 dyadic 头。
更具体地，纯第一上对角线满足
$$
P_{W_{d-s}}A_t(I-P_{W_{d-s+1}})=0\qquad(1\le s\le d-1)
$$
对每个链段都成立：原窄通量要求跨越至少两个头格，而这里仅跨一个。
因此本族没有构造出原真正的非零 $\overline f$ 或
$w\in M\ominus N$。

本节准确排除的是只用反对角对称、范数界和两个廉价费用来建立全环境
三 Gram 比较的路线；不反驳保留原长跳跃及其实际窄源的同型预算。
后续必须继续使用这些实际结构。

## 9. 对原线性目标的用途

[R271 实际二形式求和判据](R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md) 只要求原实际源上的 $\langle L_{\rm eff}a,a\rangle/\langle(I+Q_-)a,a\rangle$ 有足够温和的上界，并不要求平方比较。前五节严格关闭的是从一般 primitive 相邻界直接推出普适平方比较的路线；第六节进一步排除仅靠任意头维数/范数和小尾范数的统一线性比较。两个原头的指定结构和真实窄源未被这些环境反例排除，继续支付这一实际接口。

第八节进一步排除只加反对角对称、范数界、同源规范和两个廉价量的全环境三 Gram 捷径。其纯单步头的原跨格通量为零，没有构造真正窄源；原两个 dyadic 长跳跃头和实际来源仍须独立处理。

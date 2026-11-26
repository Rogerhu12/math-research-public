# R945 — 原有限 Selmer 的 Bockstein 指数与实际双新增广尺度

日期：2026-11-26。会话：Astra-rank2-Sha-7d29daa5-20261126 / global。
状态：已证明；本篇加强 R891 的固定 p 有限全群结论，并将其返回 R940 的原双新类。
此稿沿原 R891 的同一有限系统及共同格，不另选 canonical 来源；仍假设原 c_1 非零。

## 1. 原格、固定坐标与有限 Selmer 条件

沿 [R891](R891-original-ring-class-anti-kummer-and-one-prime-descent.md)
(1)–(3)、附录 B，固定原普通 p>211 及一个最高标签。取
O_0=Z_p[mu_18]、T_0=O_0(rho)，保原一次固定的共同格。
原完整系统 c_n 在 T=T_0 tensor O 中整，所有原范数、Euler、端点不改。

假设原 c_1 非零。按 R891(B7)–(B10)，一次固定一个 O_0 线性坐标
vartheta:O→O_0，使 c_1^0=vartheta(c_1) 非零，并在所有层取同一个 c_n^0。
原 balanced 整 Selmer S_0 是饱和秩一自由 O_0 模。选其本原生成元 z，写
$$
c_1^0=p^v z,\qquad v\ge0. \tag{1}
$$
单位已吸入 z。z 只用于证明坐标，原实际类仍是 c_1；
没有更换或重标定 c_n。

令 Sigma 为 K 中在 2、3、17、p 上的素点，并置
$$
C_0=\operatorname{Cone}\bigl(
 C^\bullet(G_{K,\Sigma},T_0)
 \longrightarrow C^\bullet(K_{\bar{\mathfrak p}},T_0)
\bigr)[-1],\qquad A_N=T_0/p^N.
\tag{2}
$$
令
$$
S_N=\ker\bigl(
 H^1(G_{K,\Sigma},A_N)\longrightarrow
 H^1(K_{\bar{\mathfrak p}},A_N)
\bigr). \tag{3}
$$
这里在 p 位为完整 H^1，在 barp 位为零，在固定坏位暂取完整 H^1，
Sigma 外未分歧。没有将 S_N 限制成整 Selmer 的约化像。
§5 将逐坏位证明，原表示下这些完整坏位群事实上全为零。

原十七惯性标量 -1 给 H^0(K,A_N)=0。
R921(39) 给 H^0(K_barp,A_N)=0 对每个 N 成立；
因此 H^1(K_barp,T_0) 无 p 挠，(2) 的 H^1 恰是饱和 S_0。
同样 H^1(C_0/p^N)=S_N，不出现 extended H^0 项。

连续 cochain 模 p^N 的短正合列于是给
$$
0\longrightarrow S_0/p^N S_0
 \longrightarrow S_N
 \xrightarrow{\beta_N} H^2(C_0)[p^N]
 \longrightarrow0. \tag{4}
$$
这里 beta_N 是全局 Selmer 复形的 Bockstein，不是 R921 某一局部线的读数。
固定有限 Sigma 的全局和局部上同调有限生成，故 H^2(C_0)_tors 有有限 p 指数；
不假设其自由部分为零。

## 2. 精确阶迫使真正的模 p 独立

**引理。** 若 b≥1、t∈H^2(C_0)[p^b] 有精确阶 p^b，并取
x∈S_b 满足 beta_b(x)=t，则 x mod p 与 z mod p 在
H^1(K,A_1) 中线性无关。

**证明。** 原 z 的模 p 像非零，由 S_0 的饱和性及全局 H^0 消失得知。
反设 x mod p=a(z mod p)。取 a 的 O_0 提升，仍记 a，令
y_b=x-a z∈S_b，其模 p 像为零。

若 b=1，这已经给 y_b=0，从而 t=0，矛盾。
若 b>1，系数短正合列
$$
0\longrightarrow A_{b-1}
 \xrightarrow{\iota_b:\,u\mapsto p u} A_b
 \longrightarrow A_1\longrightarrow0
\tag{5}
$$
及 H^0(G_{K,\Sigma},A_1)=0 给唯一
y∈H^1(G_{K,\Sigma},A_{b-1})，使 iota_{b*}y=y_b。

在 barp，H^0(K_barp,A_1)=0 使相同 iota_{b*} 在 H^1 单射。
因为 loc_barp(y_b)=0，故 loc_barp(y)=0。因此 y∈S_{b-1}，
不是只有全局 H^1 中的任意提升。其余局部条件由固定 G_{K,Sigma} 和 full 条件保持。

Bockstein 的准确自然性是
$$
\beta_b(\iota_{b*}y)=\beta_{b-1}(y).
\tag{6}
$$
可直接取 cochain 提升验证：若 dY=p^{b-1}Z，则
d(pY)=p^b Z，两边的连接类都是 [Z]。又 beta_b(az)=0，
所以 t=beta_{b-1}(y)，被 p^{b-1} 杀，与精确阶 p^b 矛盾。证毕。

此处没有假定 x 来自 T_0 上的整类；这正是 (4) 右端非零时需要处理的部分。

## 3. 原两点测试适用于这些残余类

先保留 R891(B2) 的固定坏位指数 C，使
$$
p^C H^1(K_w,A_N)=0\quad(w\mid 2,3,17,\ N\ge1). \tag{7}
$$
在 §5 核原角色之后才将其取为零。

假设 H^2(C_0)_tors 的 p 指数为 b>C+v。
取精确阶 p^b 的 t，并由 (4) 取 x∈S_b 提升。
§2 给 z mod p 与 x mod p 独立；同理它们的外部复共轭
z^c、x^c 在共轭表示中模 p 独立。

[原 finite-test 注](../notes/2026-11-16-original-endpoint-finite-test-chebotarev-refinement.md)
附录 A.2 本来就是对 H^1(K,T_0/p^b) 中的类陈述，不要求整提升。
其十七惯性两个整投影、最小系数环与 Sah/Nakayama 全像证明因而直接适用。
同该注 A.3 及 R891(B12) 的原 tau 条件合用，选一个原允许的分裂辅助 q，
在两实际素点的固定 Frobenius 坐标中得到
$$
\begin{pmatrix}
z(\mathrm{Fr}_{\mathfrak q}) & x(\mathrm{Fr}_{\mathfrak q})\\
z(\mathrm{Fr}_{\bar{\mathfrak q}}) &
x(\mathrm{Fr}_{\bar{\mathfrak q}})
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&1\end{pmatrix}
\quad\bmod p^b.
\tag{8}
$$
该 q 还平凡化 A_b 及其对偶，q≡1 mod p^b，并保原其它三槽的 tau 条件。
因为 x 原在 G_{K,Sigma} 中，q 两处未分歧；(8) 的零读数就是完整有限局部零。

再按 R891 正文选原 anti-Kummer 辅助 l。将 R891 附录 A 应用于同一
c_n^0，得到实际唯一下降类 kappa_{q,b}^0，其完整单侧有限—奇异读数为
$$
\kappa_{q,b}^0(\sigma)
=-c_1^0(\mathrm{Fr}_{\mathfrak q})=-p^v
\quad\bmod p^b .
\tag{9}
$$
这里 sigma 是原实际 tame 生成元的单位倍；另一 q 共轭位的奇异项不删除。
原系统保证该类在 barp 为零，Sigma 和 q 两处之外未分歧。
乘 p^C 后，它在固定坏位为零。

## 4. 全局互反给实际有限全群指数界

用原完美配对 T_0×T_0^c→O_0(1)，将
p^C kappa_{q,b}^0 与 x^c 作 cup product，再求全部局部不变量之和。

在固定坏位，第一类由 (7) 为零。在 p，第二类因 x 的 barp 条件为零；
在 barp，第一类为零。q 两处及 Sigma 外，两类均未分歧，cup 为零。
在 barq，x^c 读取 x 在 q 的值，由 (8) 为完整局部零。
复地方无贡献。

因此全局互反只剩 q 一项。第二类在 q 的未分歧读数为 1，
第一类的奇异读数为 (9)。有限局部 Tate 配对在这些原坐标中为乘法乘单位，
所以剩余项是
$$
\text{单位}\cdot p^{C+v}\ne0
\quad\hbox{于 }O_0/p^b,
\tag{10}
$$
与全局互反矛盾。由此证明
$$
\boxed{p^{C+v}H^2(C_0)_{\mathrm{tors}}=0.}
\tag{11}
$$
结合 (4)，对每个 N：
$$
\boxed{
p^{C+v}\,S_N
\subseteq (O_0/p^N)\,z.
}
\tag{12}
$$
(12) 保完整有限 Selmer 群，包含没有整提升的残余类。
证明没有将通常 core rank 改为一，也没有援引一个未核假设的 Kolyvagin-system 结构定理。

## 5. 逐坏位核原角色：本题可取 C=0

这里用的是已经登记的原 Hecke 角色导子，而非有理 H^1 消失的一般推断。
R900(1)–(2)、[R806 §7](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、R814 已付
$$
\lambda_i=\eta_i^{-1}\psi_0^3,\qquad
\mathfrak f_{\lambda_i}=(34\delta),\qquad
\rho_i=\lambda_i\varepsilon_{\rm cyc}^{-1}.
\tag{13}
$$
在 w 不在 p 上时，epsilon_cyc 在惯性上平凡，所以 rho_i 与 lambda_i
有相同惯性角色（换 reciprocity 仅取逆，以下单位判定不变）。

| w | 残余域大小 | (13) 的局部导子指数 | 实际非平凡惯性 |
|---|---:|---:|---|
| (2) | 4 | 1 | 非平凡角色来自 F_4^×，阶 3 |
| (delta) | 3 | 1 | 非平凡角色来自 F_3^×，阶 2 |
| (17) | 289 | 1 | 原 eta 像为 mu_18，psi_0 在此未分歧，阶 18 |

R806 §7 的原 unitary 表逐项为 2 处 Teich_mu3、delta 处 u mod delta、
17 处 vartheta_{-l_j}，其中 l_j=-5,1,7 均与 18 互素。unitary 的绝对值 twist 在惯性上平凡，
所以表中三处确给实际阶 3、2、18。特别 17 处的阶 18 来自这份原角色表与
原 eta 的满像，不能仅由导子指数为一推出。
每处导子指数恰为一，也确保惯性角色确实非平凡。
p>211 使这些阶与 p 互素，故可取惯性元 g_w 使
rho_i(g_w)-1∈O_0^×。对每个 N，
$$
H^0(K_w,A_N)=0,\qquad
H^0(K_w,A_N^\vee(1))=0.
\tag{14}
$$
第二式来自同一惯性角色的逆，因为 epsilon_cyc 在 w≠p 未分歧。

局部 Tate 对偶给 H^2(K_w,A_N)=0；w≠p 的有限局部 Euler 特征公式
#H^0·#H^2/#H^1=1 再给 H^1(K_w,A_N)=0。
因此
$$
\boxed{
H^j(K_w,A_N)=0\quad
(w\mid 2,3,17,\ N\ge1,\ j=0,1,2).
}
\tag{15}
$$
连续上同调的逆极限（各相邻有限群都为零）也给整 H^1、H^2 为零。
所以 (7) 确实可以取 C=0，不仅在有理系数成立。

于是 (11)–(12) 在本题成为
$$
\boxed{
p^v H^2(C_0)_{\mathrm{tors}}=0,\qquad
p^v S_N\subseteq (O_0/p^N)z\quad(N\ge1).
}
\tag{16}
$$
尤其 v=0 时，
$$
H^2(C_0)_{\mathrm{tors}}=0,\qquad
S_N=(O_0/p^N)z
\tag{17}
$$
通过原整 Selmer 的自然约化嵌入成立。

## 6. 返回 R940 的原双新类

[R940](R940-original-double-inert-descent-and-bounded-augmentation.md) 的 D 仍是 R908 附录 A 的固定真实 tame 尺度；
不因 (15) 而删去它，也不由 p>211 推 p∤D。
R940 的惰性检测集合仍选其原本原 z，两个惰性素数的完整群环及实际
N_{12}^{aug} 不变。

将 R940 中 abstract b_p 的选取替换成 (11)，即能取
$$
B_p=C+v+v_p(D).
\tag{18}
$$
完成 §5 的原坏位核对后，准确可取
$$
\boxed{B_p=v+v_p(D).} \tag{19}
$$
(18)–(19) 都不依赖 m 或那两个新增惰性素数。
所给的仍是原 kappa_{12,m} 的消失界及
H^1((p^{m-B_p},j_1,j_2)\otimes T) 中的唯一提升；
没有将 H^1(J) 误写成 J H^1。

(16) 控制的是固定 p 的有限全群与 p-Bockstein torsion；
它不证明原 c_1 非零，不证明原 ordinary 定位单射，不约束 R893 的
T-增广阶 s 为零，也不给跨 p 的 v 或非零结论。
若日后原完整 shadow 证明某个原坐标 c_1^0 在模 p 已非零，
则 v=0 的结论可直接使用，不必另假 residual classes 全由整类提升。

本证明仅用已经登记的原有限测试、原一侧关系、局部 Tate 对偶与全局互反；
未执行数学程序。

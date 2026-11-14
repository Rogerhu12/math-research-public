# R110：c⁷ 的真实非零第四方向与带基准成本的四块支付

日期：2026-11-14。**已证明；唯一新增原式探针已在公开 Actions 完成。** 本结果使用 run [43643100132](https://github.com/Rogerhu12/math-research-public/actions/runs/43643100132)、source 8efadbda14ed483c3393227d62bed4d3dea89087 的 c7_transverse_tail_probe 输出，以及 R101 的完整真实复制恒等式。没有在本地运行实际 m=8 探针。

结论有两层。第一，R107 的 a₇ 并不湮灭全部真实第四方向：一个既有方向的准确值为 −153664/75。第二，保留全部自身和连接成本后，存在有限真实同端口控制，使 R104/R106 的闭浸入四块上 m=8 pure D25 周期多项式次数进一步降到至多五。这里不声称完整第四函数或其他尾系数已经消失。

## 1. 完整原方向与准确的 pure 归一

沿用 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R99](R99-fourth-tangents-transverse-to-the-P1-character.md) 的完整八坐标第二算子和完整外槽第三算子。取

$$P=\Phi_{t_1},\qquad Q=\Phi_{p_1},$$

$$\tau(a;b,c)=Q(a,P(b,c))-P(a,Q(b,c)).\tag{1}$$

真实第四响应为

$$
K(F,\phi)=\mathcal B_P(\tau)
=2\tau(PD;D)-4\tau(\phi;\phi,PD)
+4P(\phi,\tau(\phi;D)),\qquad D=F-\phi^2.
\tag{2}
$$

这里的两输入记号按原式作对称极化。为了取纯四次通道，令 F=0、D=−q²，得到完整身份

$$
K_{\rm pure}(q)=
2\tau(P(q,q);q,q)
+4\tau(q;q,P(q,q))
-4P(q,\tau(q;q,q)).
\tag{3}
$$

没有删除一个外槽、局部项或右原函数。由于

$$\phi_\theta=\tfrac12(e^{-i\theta}q+e^{i\theta}\bar q),$$

完整第四齐次式的 −4 Fourier 模式是 (3) 的 **1/16**。这是原相位展开产生的比例；不是为了与已有数值吻合而另定归一。

取单位尾

$$q_c(\xi)=(c-\xi)^8,\qquad r=c-\xi,$$

并始终用真实右原函数

$$Jf(\xi)=\int_\xi^c f(\eta)\,d\eta,\qquad
D_\xi=-D_r,\qquad c\text{ 固定}.\tag{4}$$

公开实际直接复用未改动的完整 matrix_operator，得到 Kpure/16 的全部八项：

| c 次数 | r 次数 | 准确系数 |
|---:|---:|---:|
| 0 | 32 | 12644352/17825 |
| 1 | 31 | −1126024704/196075 |
| 2 | 30 | 47605365504/2384525 |
| 3 | 29 | −801105984/20735 |
| 4 | 28 | 2165204032/48165 |
| 5 | 27 | −1514756992/48165 |
| 6 | 26 | 2949843904/240825 |
| 7 | 25 | −153664/75 |

因此不仅 a₇ 已知非零，该方向的整个 D25 尾参数多项式也已确定：

$$
\boxed{\mathscr A_K(c)=\kappa c^7,\qquad
\kappa=-\frac{153664}{75}
=-\frac1{10}\frac{307328}{15}\ne0.}
\tag{5}
$$

未除 16 的 c⁷r²⁵ 系数是 −2458624/75。全部八项总次数均为 32，c⁸r²⁵ 系数为零；这里的非零是准确有理数，不是模素数余数的符号解释。

## 2. 保持同一个 a₇：尾代数、右锚与连续性

对任意常 scalar 端芽、完整 M=0 的真实有限块 B，采用 R95/R100/R107 的同一 canonical pure 输出，定义

$$
\mathscr A_B(c)=[r^{25}]\,V_{B,-4}[q_c](c-r),
\qquad
a_7(V_B)=[c^7]\mathscr A_B(c).
\tag{6}
$$

式 (6) 的 V 是整块完整第四 characteristic 成本；对它取指定尾系数与沿 s 积分交换。R95 给 deg 𝒜B≤8。R108 的五历史 action 准确计算的也是 (6)，没有重新选 normalization。

按照 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)，完整 canonical 成本由一个共同有限 profile 模板空间表示。将单位多项式尾及同一锚 (4) 代入这些模板，得到有限多项式。因此 (6) 是固定实线性泛函；它对实际有限光滑参数族连续，且不随后来的重复次数、端口连接或控制参数改变。

式 (6) 是有限尾代数的系数提取，不要求 c=0 是物理点。可以在共同正物理区间内比较 c 的开放范围，再作多项式唯一延拓。尾端右边为空时，局部尾积分与原全带右 collar 积分相同；没有改成左锚，也没有把某个全带 ruling 积分常数删除。

本稿并未把单位幂尾冒充一个已满足全部三矩、左右 collar 条件的全局 C∞ 圆。所用的是 R101 §3 已明确的抽象标量控制：同一个固定线性泛函作用于全部实际成本，成本有限且随参数连续。其证明不需要这个泛函必须是某一预先指定合法圆上的单点取值。

## 3. 先固定真实端口、连接和共同物理区间

固定 h₀>0 与反射不动的 scalar 常值 germ

$$(h,k,\omega)=(h_0,0,0).\tag{7}$$

由 R70 先固定一个紧的小光滑族 A(s)，|s|≤ε，其首末均为 (7)，frame I→I，并且 M_A(s)=sP。由 R71/R89 先固定同一 germ、frame I→I 的真实块 L，满足

$$M_L=0,\qquad T_L=\tau,\qquad V_L=v.\tag{8}$$

若原 τ 的实现位于另一 germ，就用真实零矩桥 C 搬运为 CLCᴿ。第三成本是 TC+τ−TC=τ；第四成本是 2VC+VL，全部放入 (8) 的 v。这里没有假定连接的第四成本为零。

另由 R70 固定真实基准连接 J，首末 scalar germ 均为 (7)，frame I→D，其中 D=diag(−1,1,−1)，且 M_J=0。记其完整未知成本为 T_J、V_J，位移也不预设为零。

将小族 A(s)、L、J 及它们的 scalar 反射和真实倒行全部纳入一个紧包络。h 有正下界、|ω| 有统一上界 W。一次选有界开区间 I=(a,b)，使 a>W，留下统一的 ξ+ω>0 间隙。以后只重复这些已固定块，不更改 I、ξ、尾参数 c 或 (4) 的规则。

对于任意后来指定的有限 T，取一个固定整数 m>T/ε，并令

$$A_t=A(t/m)^m,\qquad |t|\le T.\tag{9}$$

所有小块准确复位 scalar/frame，故 MA_t=tP，且重复不扩大 scalar 包络。位移、长度和三四阶自身成本会改变，均不被置零。

## 4. 真实复制支付任意指定 a₇，包括连接成本

按 [R101](R101-finite-replication-and-signed-fourth-character-costs.md) 定义

$$
C_t=A_tA_{-t},\qquad
Z(t,n)=A_tL^nA_{-t}(L^n)^R(C_{-t})^R.
\tag{10}
$$

其中倒行只对真实零矩阵大块使用其第四偶性。完整传递给

$$
M_Z=T_Z=0,\qquad
V_Z=E(t)+n(2v+tK),\qquad E(t)=E(-t).
\tag{11}
$$

E(t) 包含 At、A−t 的全部自身成本，与 n 无关；它不是被忽略的小量。

对固定泛函 (6) 取值，记 e(t)=a₇(E(t))、v₇=a₇(v)。由 (5)，

$$a_7(V_Z)=e(t)+n(2v_7+t\kappa).\tag{12}$$

先取有限 T，使 T|κ|>2|v₇|，再按 (9) 固定 m。对这个固定族，2v₇±Tκ 严格异号，e(T)=e(−T) 是固定有限数。故对任意给定 y∈R，可以选有限大整数 n，使 (12) 在 t=±T 的值位于 y 两侧。连续性和介值定理给一个实际有限 t，使

$$\boxed{a_7(V_Z)=y.}\tag{13}$$

现在取 y=−a₇(VJ)，并拼接

$$B=ZJ.\tag{14}$$

两块均 M=0，所以完整 fourth 准确相加：

$$
M_B=0,\qquad T_B=T_J,\qquad
V_B=V_Z+V_J,\qquad a_7(V_B)=0.
\tag{15}
$$

B 的 frame I→D，首末 germ 为 (7)。未知 TJ、VJ、v、E(t) 及真实累计位移都已明确记入；没有将 a₇(K) 非零直接误称为零基准的任意成本控制。

## 5. 四块真实闭合与次数至多五

对 (14) 应用 R104 的已付组装

$$\mathcal C=B\,\sigma B\,B^R\,(\sigma B)^R.\tag{16}$$

若 B 的本地位移为 Δ，则四块的本地位移依次为 Δ、AΔ、−Δ、−AΔ，其中 A=diag(1,−1,−1)；实际前缀 frame 依次为 I、D、I、D。因此全局位移之和准确为

$$\Delta+DA\Delta-\Delta-DA\Delta=0.$$

完整 M𝒞=T𝒞=0，所有常值芽和 frame/位置相接，得到共同正 I 上的有限 C∞ 正则浸入环带。完整第四成本仍是 2VB+2VσB；倒行没有将它变负。

R106 对完整 pure 尾递归给

$$
\mathscr A_{\mathcal C}(c)
=2\{\mathscr A_B(c)-\mathscr A_B(-c)\}
=4(a_7c^7+a_5c^5+a_3c^3+a_1c).
$$

代入 (15)，得到

$$
\boxed{\mathscr A_{\mathcal C}(c)
=4(a_5c^5+a_3c^3+a_1c),\qquad
\deg\mathscr A_{\mathcal C}\le5.}
\tag{17}
$$

这不与 R107 矛盾：a₇ 在 a₈=0 后沿单一正仿射轨道不变，但它在真实第四控制方向 K 上并非零，完整有限复制又支付了该方向的自身基准成本。

## 6. 公开实际记录与边界

新增实际仅计算 (3) 的一个既有真实方向；没有重跑 R99 查询、R100/R106 旧身份，没有求解实际几何路径，也没有构造合法全局 profile。

主[完整报告](../notes/actions-43643100132-1-c7_transverse_tail_probe/c7-transverse-tail-probe.json)为 2179 bytes，SHA-256 c6c2c4c886dc5f115569ab4dd36176530efcf80ed12bb83b3d19223a7a279746。完整八项数组 SHA-256 为 e37a582bd52a0a7028e2794cd0d6084f050dc4a65b5905d949c00e9dcecdf850。

实际用时 0.008047893 秒，峰值 RSS 25.11328125 MiB，611 次准确多项式操作，最大中间项数 10。新增[探针源码](../scripts/literature_c7_transverse_tail_probe.py)为 11020 bytes，SHA-256 98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b；复用原 matrix_operator 所在文件为 33718 bytes，SHA-256 f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70。

(13)–(17) 是基于已付真实控制定理的有限存在证明，没有给出重复次数、实际几何参数、长度或 reach 的数值清单。它仅支付指定 pure D25 尾系数层次。其余 tail 幂、完整 mixed 模式、第三/第四 ruling、全体 profile 合法性、高阶收敛、有限等距族、闭嵌入材料面和宏观幅度继续保留。

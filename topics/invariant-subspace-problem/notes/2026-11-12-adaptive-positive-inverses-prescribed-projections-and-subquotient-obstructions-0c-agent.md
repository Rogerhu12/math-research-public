# R204：自适应正逆、指定投影边界与不变子商中的分母障碍

日期：2026-11-12（UTC）。作者：root；critical_kernel 独立核验核心递归与边界构造。

状态：完整实际算子证明。正一阶及其逆随指定的可数资料选择；不声称某个固定逆同时对全部未知不变子商具有本稿的系数独立性。原慢符号的普遍限制值域与完整 ISP 仍开放。

## 1. 记号与结论

令
$$
H=L^2(\mathbb Z_2,\mu),\qquad
\mathfrak C=\{A\}',\qquad
\mathfrak U=C^*(I,A).
$$
这里 $\mathfrak U$ 为实际物理 UHF 代数。
记
$$
J_j=M_{\chi_j},\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad
S_j=I-2E_j.
$$
$J_j$ 两两交换且为自伴酉算子。
沿用 R164 的代数
$$
\mathfrak E=
\{T\in B(H):[T,J_j]\to0,\ [T^*,J_j]\to0
\text{ 于 SOT}\}.
\tag{1.1}
$$

固定有限放大次数 $d\ge1$，在 $H^{(d)}$ 上置
$$
\mathfrak E_d=
\{T:[T,J_j^{(d)}]\to0,\ [T^*,J_j^{(d)}]\to0
\text{ 于 SOT}\},
\qquad
\mathfrak U_d=M_d(\mathfrak U).
$$
这是含 $\mathfrak U_d$ 的 $C^*$ 代数。
本稿所有有限放大均使用同一个标量一阶行 $a$，即算子 $X_a^{(d)}$。

**定理1.1（可数资料的自适应边界）。**
设 $\mathfrak B\subseteq\mathfrak E_d$ 是范数可分的含单位 $C^*$ 代数，
并给定任意可数族 $h_r\in H^{(d)}$。
可取非负实系数
$$
a\in\ell^2\setminus\ell^1
$$
及实际闭一阶 $X=X_a$，使：

1. 所有 $h_r\in\operatorname{Dom}X^{(d)}$；
2. $L=(I+X)^{-1}\in\mathfrak C$ 有界、单射、稠密像、拟幂零，且
   $$
   \operatorname{Re}L\ge L^*L;
   \tag{1.2}
   $$
3. 存在有限位集 $F_n$，$\min F_n\to\infty$，使 $U_n=\prod_{j\in F_n}J_j^{(d)}$ 满足
   $$
   U_nTU_n\longrightarrow T\quad\text{强*，对所有 }T\in\mathfrak B,
   \qquad
   U_nL^{(d)}U_n\longrightarrow0\quad\text{强*};
   \tag{1.3}
   $$
4. 因而逐点强*极限给一个满射 $*$ 同态
   $$
   \Pi:C^*(\mathfrak B,L^{(d)})\longrightarrow\mathfrak B,
   \qquad
   \Pi|_{\mathfrak B}=\operatorname{id},\qquad
   \Pi(L^{(d)})=0.
   \tag{1.4}
   $$

若还希望固定 $\mathfrak U_d$，把 $\mathfrak B$ 换成
$C^*(\mathfrak B,\mathfrak U_d)$ 即可；它仍范数可分且包含于 $\mathfrak E_d$。

本稿随后证明：

- 对固定同一有限放大中任意预先指定的可数不变子商，可令同一个 $\Pi$ 固定相应旗投影；
- 在这些子商上，新选出的 $L_Q$ 对固定角代数中的系数没有非零单侧解析关系；
- 每个非零 Haar 不变子商的交换子代数都不范数可分；
- 每个这类子商的范数多项式代数没有有限有理模生成族；若子商循环，则还具有明确的稠密域不可闭交换算子。

“解析关系”必须满足一个明确的正收敛半径条件；不把单独一个原级数的收敛当作逐次取消后级数仍收敛。

## 2. 所需的真实高位接口

R164 已证，且在有限放大中逐式相同，
$$
N_j^{(d)}-\frac{I-J_j^{(d)}}2\to0\quad\text{强},
\qquad
N_j^{(d)}+(N_j^{(d)})^*\to I\quad\text{强*}.
\tag{2.1}
$$
另有
$$
V_j\to0\quad\text{于 WOT},\qquad
\sup_j\|V_j\|\le6,\qquad
\|V_j-S_j\|\le8\eta_j.
\tag{2.2}
$$
这些是实际进位关系的结论。

若 $M$ 对 $A^{(d)}$ 不变，$P=P_M$，则
$$
(I-P)N_j^{(d)}P=0,\qquad
P(N_j^{(d)})^*(I-P)=0.
$$
因此
$$
[P,N_j^{(d)}]
=P\bigl(N_j^{(d)}+(N_j^{(d)})^*\bigr)(I-P)\to0
\quad\text{强*}.
$$
由 (2.1) 及 $P,J_j^{(d)}$ 自伴，
$$
[P,J_j^{(d)}]\to0\quad\text{强*}.
\tag{2.3}
$$
故任意这样的不变投影都属于 $\mathfrak E_d$。
若 $N\subseteq M$ 为不变旗，子商正交实现的投影
$$
P_Q=P_M-P_N
$$
也属于 $\mathfrak E_d$。

后文还使用 R125 的闭域事实：有限柱同时是 $X_a^{(d)}$ 及其通常伴随的图核心，
有限系数截断在这个核心上收敛。
不将这种核心收敛延成任意域向量的原顺序系数截断收敛。

## 3. 同时满足 Gram 条件与增长 Walsh 乘积的递归

取 $\mathfrak B$ 单位球的一列范数稠密元素 $T_1,T_2,\ldots$，
以及 $H^{(d)}$ 单位球的一列范数稠密测试向量 $v_1,v_2,\ldots$。

先在抽象系数序号上分块。令 $K_0=0$，
递归选有限整数 $K_n>K_{n-1}$，使
$$
\sum_{k=K_{n-1}+1}^{K_n}\frac1k\ge n.
\tag{3.1}
$$
记
$$
I_n=\{K_{n-1}+1,\ldots,K_n\},\qquad b_n=|I_n|.
$$
这一步先固定每个有限块的长度，尚未选择任何物理位。

再按 $k=1,2,\ldots$ 递归选严格递增的物理指标 $j_k$。
若 $k\in I_n$，令当前块内已选前缀乘积为
$$
U_{\mathrm{prev}}=\prod_{\substack{\ell\in I_n\\\ell<k}}J_{j_\ell}^{(d)}.
$$
要求新指标 $j=j_k$ 同时满足：

- 对所有 $r\le k$ 和 $\ell<k$，
  $$
  |\langle V_j^{(d)}h_r,V_{j_\ell}^{(d)}h_r\rangle|
  \le2^{-k-\ell};
  \tag{3.2}
  $$
- 对所有 $r,s\le n$，
  $$
  \|[T_s,J_j^{(d)}]U_{\mathrm{prev}}v_r\|
  \le2^{-n}/b_n,
  \qquad
  \|[T_s^*,J_j^{(d)}]U_{\mathrm{prev}}v_r\|
  \le2^{-n}/b_n.
  \tag{3.3}
  $$

每一步的向量与条件都只有有限多个，且此时 $U_{\mathrm{prev}}$ 已固定。
(3.2) 由 $V_j^{(d)}\to0$ 于 WOT 保证；
(3.3) 由 $T_s,T_s^*\in\mathfrak E_d$ 保证。
因此可以同时满足，另令 $j_k>j_{k-1}$。

置
$$
a_{j_k}=\frac1k,\qquad a_j=0\quad(j\notin\{j_k\}),
\qquad
F_n=\{j_k:k\in I_n\}.
\tag{3.4}
$$
于是 $a\ge0$、$a\in\ell^2\setminus\ell^1$，
且
$$
\sum_{j\in F_n}a_j\ge n,\qquad \min F_n\to\infty.
\tag{3.5}
$$

### 3.1 增长乘积的交换误差确实可控

这一步不是从固定乘积长度的渐近交换擅自取一个移动长度。
对每个固定 $T$、当前前缀 $U$，
$$
[T,J_j^{(d)}U]v
=[T,J_j^{(d)}]Uv+J_j^{(d)}[T,U]v.
$$
$J_j^{(d)}$ 是酉算子，所以逐位使用 (3.3)，得到
$$
\|[T_s,U_n]v_r\|\le2^{-n},
\qquad
\|[T_s^*,U_n]v_r\|\le2^{-n}
\quad(r,s\le n).
\tag{3.6}
$$
对固定 $s$，先由测试向量的稠密性和统一算子范数界延到全部向量，
再由 $T_s$ 的范数稠密性延到全部 $\mathfrak B$，得到
$$
U_nTU_n\to T\quad\text{强*，对每个 }T\in\mathfrak B.
\tag{3.7}
$$
有限块的巨大长度只影响物理指标的选择，不出现在最终误差中。
这里没有给原先固定的一阶行重新排列系数；整行 $a$ 正是随资料构造的。

### 3.2 给定可数向量确实属于真实一阶域

固定 $r$。
当 $N>M\ge r$ 时，(3.2) 给
$$
\left\|\sum_{k=M+1}^N\frac1kV_{j_k}^{(d)}h_r\right\|^2
\le36\|h_r\|^2\sum_{k>M}k^{-2}
+2\sum_{M<\ell<k}\frac{2^{-k-\ell}}{k\ell}.
\tag{3.8}
$$
故部分和在 $H^{(d)}$ 中收敛到某个 $y_r$。
对任意有限柱 $v$，
$$
\langle y_r,v\rangle
=\lim_N\left\langle h_r,
\sum_{k=1}^N k^{-1}(V_{j_k}^{(d)})^*v\right\rangle
=\langle h_r,(X_a^{(d)})^*v\rangle.
$$
有限柱为伴随图核心，故
$$
h_r\in\operatorname{Dom}X_a^{(d)},\qquad X_a^{(d)}h_r=y_r.
\tag{3.9}
$$

## 4. 同一增长乘积消去真实正逆

正不可和一阶的已证空谱与最大增生性给
$$
T=I+X_a,\qquad L=T^{-1}\in\mathfrak C,\qquad \|L\|\le1.
$$
$L$ 单射、稠密像、拟幂零。
对 $y\in H$，令 $x=Ly$，则
$$
\operatorname{Re}\langle Ly,y\rangle
=\operatorname{Re}\langle x,Tx\rangle\ge\|x\|^2,
$$
得到 (1.2)。

以下直接核验所需逃逸，而不是只援引一个形式极限。
写
$$
X_a=X_a^0+K(a),\qquad
K(a)=\sum_j a_j(V_j-S_j)\in\mathfrak U,
\qquad
\|K(a)\|\le8\|a\|_2\|\eta\|_2.
$$
置
$$
\lambda_n=2\sum_{j\in F_n}a_j\ge2n.
$$
对任意固定有限柱 $v\in H^{(d)}$，
当 $F_n$ 位于其全部支撑之外时，
纯局部共轭把 $F_n$ 中的系数符号翻转，并产生标量中心 $\lambda_n$。
翻转后的高位作用是互相正交的创建项；
低位部分不变。因此
$$
\|(T^{(d)}-\lambda_n)U_nv\|\le C_v,
\qquad
\|((T^{(d)})^*-\lambda_n)U_nv\|\le C_v'
\tag{4.1}
$$
有与 $n$ 无关的有限常数。
例如第一式可取
$$
C_v=\|(X_a^0)^{(d)}v\|+(1+\|K(a)\|)\|v\|,
$$
第二式用纯伴随作同样选择。
有限柱的真实域与伴随域已由 R125 给定。

把第一式左乘 $L^{(d)}$，第二式左乘 $(L^{(d)})^*$，
得到
$$
\|L^{(d)}U_nv\|
\le\lambda_n^{-1}(\|v\|+\|L\|C_v)\to0,
$$
$$
\|(L^{(d)})^*U_nv\|
\le\lambda_n^{-1}(\|v\|+\|L\|C_v')\to0.
\tag{4.2}
$$
利用统一有界性及有限柱稠密性，
$$
U_nL^{(d)}U_n\to0\quad\text{强*}.
\tag{4.3}
$$
(3.7)、(4.3) 在代数生成元上给出极限；
有限非交换 $*$ 多项式上通过有界乘法传递，
再以范数逼近延到 $C^*(\mathfrak B,L^{(d)})$。
极限是压缩范数的 $*$ 同态，像恰为 $\mathfrak B$，证明定理1.1。

特别，
$$
\|L^{(d)}-B\|\ge\|\Pi(L^{(d)}-B)\|=\|B\|,
\qquad B\in\mathfrak B.
$$
结合三角不等式，
$$
\boxed{\operatorname{dist}(L^{(d)},\mathfrak B)\ge\frac12\|L\|>0.}
\tag{4.4}
$$

## 5. 固定任意预先指定的可数不变旗

给定
$$
N_r\subseteq M_r\subseteq H^{(d)},\qquad
A^{(d)}M_r\subseteq M_r,\quad A^{(d)}N_r\subseteq N_r.
$$
令
$$
\mathfrak B=C^*(\mathfrak U_d,\{P_{M_r},P_{N_r}:r\ge1\}).
\tag{5.1}
$$
它范数可分且包含于 $\mathfrak E_d$。
定理1.1 的 $\Pi$ 固定全部旗投影，
从而固定
$$
P_r=P_{M_r}-P_{N_r}.
$$
把 $Q_r=M_r\ominus N_r$ 作为子商的正交实现，记
$$
L_r=P_rL^{(d)}|_{Q_r}.
$$
$L^{(d)}$ 保持两端旗，故这就是其实际子商算子。

(1.2) 给任意 $0\ne x\in Q_r$，
$$
\operatorname{Re}\langle L_rx,x\rangle
=\operatorname{Re}\langle L^{(d)}x,x\rangle
\ge\|L^{(d)}x\|^2>0.
\tag{5.2}
$$
因此 $L_r$ 与 $L_r^*$ 的核都为零，$L_r$ 稠密像。
又它是 $L^{(d)}$ 的子商，故拟幂零。
令
$$
Y_r=L_r^{-1},\qquad\operatorname{Dom}Y_r=\operatorname{Ran}L_r.
\tag{5.3}
$$
这是稠密定义的真实闭算子。

在投影角上，
$$
\Pi_r:P_rC^*(\mathfrak B,L^{(d)})P_r
\longrightarrow P_r\mathfrak B P_r
\tag{5.4}
$$
固定角代数并消去 $L_r$ 的零延拓。
以下把这个角直接视为 $B(Q_r)$ 的子代数，不把零延拓的额外零谱点混入。

### 5.1 单侧解析系数独立性

设 $B_k\in P_r\mathfrak B P_r$，
并假设存在 $\rho>0$ 使
$$
\sum_{k\ge0}\|B_k\|\rho^k<\infty.
\tag{5.5}
$$
由于 $r(L_r)=0$，每个有限次移位级数
$\sum_{k\ge0}B_{k+\ell}L_r^k$ 都按范数绝对收敛。

若
$$
\sum_{k\ge0}B_kL_r^k=0,
$$
先作用 $\Pi_r$ 得 $B_0=0$。
于是
$$
\left(\sum_{k\ge0}B_{k+1}L_r^k\right)L_r=0.
$$
$L_r$ 稠密像，故括号为零。
重复得到全部 $B_k=0$。
对关系
$$
\sum_{k\ge0}L_r^kB_k=0
$$
同理：去掉常项后使用 $L_r$ 单射取消左因子。
因此
$$
\boxed{\text{满足正半径条件的左右单侧解析关系均只有零系数。}}
\tag{5.6}
$$
不要求 $B_k$ 相互交换或与 $L_r$ 交换。
有限多项式自然包含在该结论中。

只知道最初的 $\sum B_kL_r^k$ 收敛，不保证移位后的级数收敛；
本文明确使用 (5.5)，不遗漏这个条件。

### 5.2 共同域在子商中的识别

定理1.1 的可数族可以包含所需子商向量在 $Q_r\subset H^{(d)}$ 中的正交代表。
若 $h\in Q_r\cap\operatorname{Dom}X^{(d)}$，
正一阶的真实不变限制性质给
$$
T^{(d)}h\in M_r.
$$
令 $g=P_rT^{(d)}h$。
由于 $L^{(d)}$ 保持 $N_r$，
$$
L_rg=P_rL^{(d)}P_rT^{(d)}h=h.
$$
故
$$
h\in\operatorname{Dom}Y_r,\qquad
Y_rh=P_rT^{(d)}h.
\tag{5.7}
$$
这一步保证下面只知一阶域的生成向量可用于真实闭逆，
不是把全空间域直接压缩当作定义。

## 6. 每个子商角的有限有理模生成障碍

固定一个非零子商 $Q$，定义范数可分角代数
$$
\mathfrak B_Q=
\left.P_QC^*(\mathfrak U_d,P_M,P_N)P_Q\right|_Q.
$$
它包含 $A_Q$，也包含其范数多项式代数。
设 $\mathfrak D$ 是任意含单位、交换的子代数，满足
$$
\mathfrak D\subseteq\mathfrak B_Q\cap\{A_Q\}'.
\tag{6.1}
$$

**定理6.1。** 不存在有限族 $h_1,\ldots,h_s\in Q$，
使每个 $h\in Q$ 都有表示
$$
D_hh=\sum_{i=1}^sC_{h,i}h_i,\qquad
D_h,C_{h,i}\in\mathfrak D,\qquad\ker D_h=0.
\tag{6.2}
$$

**证明。**
反设存在这样一族。
在构造定理1.1 时把这些 $h_i$ 放入共同域资料，
并固定 $P_M,P_N$ 及 $\mathfrak U_d$。
由 (5.7)，$h_i\in\operatorname{Dom}Y$，其中 $Y=L_Q^{-1}$。

$L_Q$ 是 $A_Q$ 的强多项式极限：
全空间 $L\in\mathfrak C$，R88 的强多项式逼近在有限放大、限制及商中保留。
所以每个 $\mathfrak D$ 元素与 $L_Q$ 交换，并保持 $\operatorname{Dom}Y$、与 $Y$ 域交换。

将 (6.2) 分别用于 $Yh_j$，再取各单射分母的乘积，
得到共同单射 $B\in\mathfrak D$ 及矩阵 $C=(C_{ji})\in M_s(\mathfrak D)$，使
$$
BYh_j=\sum_iC_{ji}h_i.
$$
目前只知道 $h_i$ 在一阶域中，因此先左乘有界 $L_Q$：
$$
(BI_s-C L_Q)\begin{pmatrix}h_1\\\vdots\\h_s\end{pmatrix}=0.
\tag{6.3}
$$
矩阵条目交换，伴随矩阵恒等式给
$$
\Delta(L_Q)h_i=0,\qquad
\Delta(w)=\det(BI_s-Cw)=B^s+\sum_{k=1}^sE_kw^k.
$$
每个 $E_k\in\mathfrak D$。

任取 $h\in Q$，使用 (6.2) 并取消单射 $D_h$，得
$\Delta(L_Q)h=0$。
所以这个有界多项式在全部 $Q$ 上为零。
应用 (5.6)，常系数 $B^s=0$。
但 $B$ 单射且 $Q\ne0$，矛盾。证毕。

因此每个非零 Haar 有限放大不变子商的范数多项式代数，
都没有有理严格循环向量，亦没有任何有限有理模生成族。
本结论没有要求 $\mathfrak D$ 的所有非零元素单射；
只使用表示中明确要求为单射的分母。

## 7. 循环子商上的实际可闭性失败

另假设 $Q$ 对 $A_Q$ 循环，取一个循环向量 $v\ne0$，
并设 $\mathfrak D$ 满足 (6.1) 且包含 $A_Q$。
构造时令 $v\in\operatorname{Dom}Y$，置
$$
f=Yv.
$$
因为
$$
v=L_Qf
$$
且 $L_Q$ 为 $A_Q$ 的强多项式极限，$f$ 也循环。

还需明确图核心。
映射
$$
z\longmapsto(L_Qz,z)
$$
从 $Q$ 到 $Y$ 的图空间为有界同构。
$f$ 循环，所以
$$
\{(p(A_Q)v,p(A_Q)f):p\in\mathbb C[z]\}
$$
在完整图 $\operatorname{Graph}Y$ 中稠密。
因此 $v$ 的多项式轨道确为 $Y$ 的图核心。

若 $Bf=Cv$，其中 $B,C\in\mathfrak D$，
在这个图核心上有 $BY=C$，再延到全部 $\operatorname{Dom}Y$。
右乘 $L_Q$ 得到
$$
B=CL_Q.
$$
应用固定 $\mathfrak B_Q$ 且杀 $L_Q$ 的 $\Pi_Q$，得 $B=0$。
所以
$$
\mathfrak Dv\cap\mathfrak Df=\{0\},
\qquad
\overline{\mathfrak Dv}=\overline{\mathfrak Df}=Q.
\tag{7.1}
$$

在代数直和上定义
$$
Z(x+y)=y,\qquad
x\in\mathfrak Dv,\ y\in\mathfrak Df.
$$
它稠密定义并与 $\mathfrak D$ 按域交换。
取固定 $0\ne y\in\mathfrak Df$，以及 $y_n\in\mathfrak Dv$、$y_n\to y$，
则
$$
y-y_n\to0,\qquad Z(y-y_n)=y\ne0.
$$
故 $Z$ 不可闭。
这特别适用于每个循环 Haar 子商的范数多项式代数。

本文没有把该明确不可闭算子扩展成与整个 $\{A_Q\}'$ 交换的算子。
$L_Q$ 本身已在这个大交换子内，并使两条满交换子轨道有非零交。

## 8. 每个非零 Haar 子商的交换子都不范数可分

先回顾零延拓的高位性质，并给出其实际理由。
设 $B\in\{A_Q\}'$，将它零延拓为
$$
\widetilde B=P_QBP_Q\in B(H^{(d)}).
$$
记 $P=P_Q$。
$B$ 与 $N_{j,Q}$ 交换，故
$$
[\widetilde B,N_j^{(d)}]
=\widetilde B[P,N_j^{(d)}]+[P,N_j^{(d)}]\widetilde B.
\tag{8.1}
$$
由 (2.3) 前的强*结论，右侧强*趋零。
再分别使用 (2.1) 的
$N_j^{(d)}-(I-J_j^{(d)})/2\to0$ 强，
以及其伴随版本
$(N_j^{(d)})^*-(I+J_j^{(d)})/2\to0$ 强，
得到
$$
[\widetilde B,J_j^{(d)}]\to0,\qquad
[\widetilde B^*,J_j^{(d)}]\to0\quad\text{强}.
$$
即 $\widetilde B\in\mathfrak E_d$。
这也正是 R164 对子商交织零延拓的结论。

反设 $\{A_Q\}'$ 范数可分。
则由其全部零延拓、$\mathfrak U_d$ 以及两端旗投影生成的
$C^*$ 代数 $\mathfrak B$ 范数可分，且包含于 $\mathfrak E_d$。
应用定理1.1。
$\Pi$ 固定 $\mathfrak B$；
但 $L_Q\in\{A_Q\}'$，其零延拓既属于 $\mathfrak B$，
又被 $\Pi$ 消去。
因此 $L_Q=0$，与 (5.2) 在非零 $Q$ 上的单射性矛盾。

所以
$$
\boxed{
Q\ne0\quad\Longrightarrow\quad
\{A_Q\}'\text{ 不范数可分}.
}
\tag{8.2}
$$
特别 $\mathfrak C$ 不范数可分。
这里只用范数可分性；
从一个被固定的强稠密可数族，不能推 $\Pi$ 固定其强闭包。
本稿的 $\Pi$ 没有被声称为正常或强连续。

## 9. 量词与尚未闭合的慢符号接口

本稿的正逆是随预先指定的范数可分代数、旗和域向量共同构造的。
因此不存在把 R194 的某个固定 $L$ 无条件提升到所有未知子商的步骤。

固定旗之后得到的边界会保留原 UHF 中的慢符号 $S_N,S_Y$。
它消去的是新选出的正逆 $L$，没有把这些慢符号收入单锚全纯场。
所以没有由本稿推出
$$
I\in\overline{S_N\mathbb C[A]}^{\mathrm{SOT}}
\quad\text{或}\quad
I\in\overline{S_Y\mathbb C[A]}^{\mathrm{SOT}}.
$$

有理模生成失败、范数不可分、可闭性失败，都不是原 Haar 不变子空间非零性的证明。
上述 $Z$ 的定义域是稠密代数直和，其闭图并不是一个新闭不变分支。
完整 ISP 与本题 open.md 中的一般慢核和普遍范围缺口继续保留。

## 10. 证明依赖

- R125/R128：真实一阶闭域、伴随有限柱核心、正不可和空谱与不变限制；
- R164：高位渐近交换代数及子商交织零延拓；
- R194：正逆逃逸的先前固定源版本；本稿 §4 另给需要的完整估计；
- R199：严格正逆的普遍子商性质；本稿 (5.2) 给直接核验；
- R203：可数族 Gram 选择与有理模生成障碍的原空间版本。

所有增长乘积误差都在递归中逐项预付；
所有未知生成向量只要求一阶域；
伴随矩阵只用于已经有界的矩阵。

# 实际二阶乘子的进位差：次数权估计与严格的无界扰动例

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**全部下列估计已证明。** 本稿提供 l2_moments 的二阶 Dirac/Nelson 证明所需真实接口，不把二阶 gauge 的无界差当作 R122 的有界解析差。

## 1. 记号及目标

令 𝓝 为 Walsh 次数算子，

$$
\mathsf N\chi_F=|F|\chi_F,\qquad \Lambda=I+\mathsf N.
$$

记 𝓓=∪_{p≥0}H_{≤p}。它是每个 Λ 正幂的谱核心。

真实归一化幂和单坐标乘子为

$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,
$$

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
S_j=I-2E_j,\qquad K_j=V_j-S_j.
\tag{1.1}
$$

E_j 为物理第 j 位的矩阵单位。取

$$
\eta_*=\sup_j\eta_j<1/4,\qquad
\mathcal E_\eta=\left(\sum_{j\ge0}(j+1)\eta_j^2\right)^{1/2}<\infty.
\tag{1.2}
$$

本题 η_j≤exp(−770·16^j) 远强于这些要求。

给定

$$
f=a_*+\sum_i a_i\chi_i+\sum_{i<j}b_{ij}\chi_i\chi_j,
\quad
a\in\ell^2,\quad b\in\ell^2(\{i<j\}),
\tag{1.3}
$$

考虑有限系数实际/纯乘子之差

$$
R_{\rm fin}=\sum_i a_iK_i+
\sum_{i<j}b_{ij}(V_iV_j-S_iS_j).
\tag{1.4}
$$

本稿证明 R_fin 和 [𝓝,R_fin] 都在 B(D(Λ^{1/2}),H) 中收敛，并给

$$
\boxed{
\|R\Lambda^{-1/2}\|+
\|[\mathsf N,R]\Lambda^{-1/2}\|
\le
2000\,\mathcal E_\eta(\|a\|_2+\|b\|_2).
}
\tag{1.5}
$$

交换子首先定义在𝓓上；该域上 R𝓓⊂Dom𝓝，故不是纯形式记号。
末节还给一个明确 f，使 R 本身无界，说明 (1.5) 的半次权不能被无理由删除。

## 2. 局部字串的次数交换子

若 T 只作用于某个含 r 个物理位的有限集合，分解总次数为这些位上的𝓝_F加其余位次数。于是

$$
[\mathsf N,T]=[\mathsf N_F,T],
\qquad
\|[\mathsf N,T]\|
\le r\|T\|.
\tag{2.1}
$$

因为 𝓝_F−rI/2 的范数为 r/2，使用两个乘积的三角界即可。T 保持 Dom𝓝。

反复迭代 (1.1)，得到真实范数收敛字串展开

$$
N_j-E_j=
\sum_{\ell\ge1}
\beta_{j,\ell}\,
E_j^*E_{j+1}^*\cdots E_{j+\ell-1}^*E_{j+\ell},
\qquad
\beta_{j,\ell}=\prod_{k=j}^{j+\ell-1}\eta_k.
\tag{2.2}
$$

有限迭代余项范数≤β_{j,L+1}，故趋0。每个字串范数为1，支撑 ℓ+1 位；而

$$
\beta_{j,\ell}\le\eta_j\eta_*^{\ell-1}.
$$

因此 (2.1) 给

$$
\|[\mathsf N,N_j-E_j]\|
\le\eta_j\sum_{\ell\ge1}(\ell+1)\eta_*^{\ell-1}
=\eta_j\frac{2-\eta_*}{(1-\eta_*)^2}
\le4\eta_j.
\tag{2.3}
$$

这里的数值不依赖物理位 j，因为𝓝计的是占据个数，不是位指标大小。

范数级数和交换子级数都绝对收敛。对 x∈Dom𝓝，有限部分满足
𝓝T_Lx=T_L𝓝x+[𝓝,T_L]x，两端都收敛。𝓝闭性给极限算子保持 Dom𝓝，并满足相同等式。因此 (2.3) 是包含定义域的真实结论。

另由精确一位式 ∥N_j−E_j∥=η_j 和 (2.1) 的 r=1 情形，

$$
\|[\mathsf N,N_j]\|\le1+4\eta_j<2.
\tag{2.4}
$$

## 3. 逆因子的定义域与 K_j 界

由 N_j²=η_jN_{j+1} 和 ∥N_{j+1}∥=1，

$$
\|N_j^{2r}\|,\ \|N_j^{2r+1}\|\le\eta_j^r.
$$

故

$$
(I+N_j)^{-1}=\sum_{n\ge0}(-N_j)^n,\qquad
\sum_{n\ge0}\|N_j^n\|
\le\frac2{1-\eta_j}<3.
\tag{3.1}
$$

对每个幂使用 Leibniz 式，

$$
\sum_{n\ge1}\|[\mathsf N,N_j^n]\|
\le
\|[\mathsf N,N_j]\|
\left(\sum_{n\ge0}\|N_j^n\|\right)^2
<18.
\tag{3.2}
$$

所以逆的级数也在次数图范数下收敛。它保持 Dom𝓝，并有

$$
[\mathsf N,(I+N_j)^{-1}]
=-(I+N_j)^{-1}[\mathsf N,N_j](I+N_j)^{-1},
\quad
\|[\mathsf N,(I+N_j)^{-1}]\|\le18.
\tag{3.3}
$$

这一步没有把一个只在算子范数收敛的逆自动当作定义域保持算子。

从 V_j−(I−2N_j)=2N_j²(I+N_j)^{-1} 立即有

$$
\boxed{\|K_j\|\le2\eta_j+6\eta_j=8\eta_j.}
\tag{3.4}
$$

要估计交换子，使用不要求 N_j、E_j 交换的精确预解式恒等式

$$
K_j=-2(I+N_j)^{-1}(N_j-E_j)(I-E_j).
\tag{3.5}
$$

各因子都保持 Dom𝓝。由 (2.3)、(3.3)、∥I−E_j∥≤2 和
∥[𝓝,E_j]∥≤1，Leibniz 式给

$$
\begin{aligned}
\|[\mathsf N,K_j]\|
&\le2\bigl(18\eta_j\cdot2+
3\cdot4\eta_j\cdot2+3\eta_j\bigr)\\
&\le126\eta_j.
\end{aligned}
\tag{3.6}
$$

因此统一地

$$
\|V_j\|\le6,\qquad \|[\mathsf N,V_j]\|\le34.
\tag{3.7}
$$

这些粗常数充分使用了 η_*<1/4；后续不依赖任何尖常数。

## 4. 纯第一阶行和的半次权界

在 Walsh 基上，

$$
S_j=c_j-c_j^*+2P_j,\qquad
[\mathsf N,S_j]=c_j+c_j^*.
$$

对任意 u∈ℓ²，由逐层创建、删除、占据估计，

$$
L_u^0=\sum_j u_jS_j,\qquad
J_u^0=\sum_j u_j[\mathsf N,S_j]
$$

在 D(Λ^{1/2})→H 的算子范数中收敛，并满足

$$
\boxed{
\|L_u^0\Lambda^{-1/2}\|\le4\|u\|_2,\qquad
\|J_u^0\Lambda^{-1/2}\|\le2\|u\|_2.
}
\tag{4.1}
$$

例如创建在纯 q 层的范数≤√(q+1)∥u∥₂，删除≤√q∥u∥₂，占据≤√q∥u∥₂；输出层正交，故对所有层求和后给 (4.1)。对系数尾重复此估计得到所称范数收敛。

## 5. 二阶排序与全系数 ℓ² 控制

不假定混合真实与纯局部因子交换。逐对使用恒等式

$$
V_iV_j-S_iS_j=K_iS_j+V_iK_j\qquad(i<j),
\tag{5.1}
$$

得到

$$
R=
\sum_i a_iK_i+
\sum_i K_i L_i+
\sum_j M_jK_j,
\tag{5.2}
$$

其中

$$
L_i=\sum_{j>i}b_{ij}S_j,\qquad
M_j=\sum_{i<j}b_{ij}V_i.
$$

令

$$
r_i=\left(\sum_{j>i}|b_{ij}|^2\right)^{1/2},
\qquad
c_j=\left(\sum_{i<j}|b_{ij}|^2\right)^{1/2}.
$$

两族平方和都恰为 ∥b∥₂²。

### 5.1 错误位前的实际头有限

每个 M_j 是有限和，(3.7) 给

$$
\|M_j\|\le6\sqrt j\,c_j,\qquad
\|[\mathsf N,M_j]\|\le34\sqrt j\,c_j.
\tag{5.3}
$$

故

$$
\|M_jK_j\|\le48\sqrt j\,\eta_jc_j,
$$

$$
\|[\mathsf N,M_jK_j]\|
\le(34\cdot8+6\cdot126)\sqrt j\,\eta_jc_j
=1028\sqrt j\,\eta_jc_j.
\tag{5.4}
$$

由 Cauchy，

$$
\sum_j\sqrt j\,\eta_jc_j
\le\left(\sum_j j\eta_j^2\right)^{1/2}\|b\|_2.
$$

因此 (5.2) 的最后一组项及其次数交换子都是 H 上有界算子，且按范数绝对收敛。

### 5.2 错误位后的行和可以无界，但只损失半次权

由 (4.1)，

$$
\|K_iL_i\Lambda^{-1/2}\|\le32\eta_ir_i,
$$

$$
\|[\mathsf N,K_iL_i]\Lambda^{-1/2}\|
\le(126\cdot4+8\cdot2)\eta_ir_i
=520\eta_ir_i.
\tag{5.5}
$$

而 ∑η_ir_i≤∥η∥₂∥b∥₂。因此第二组项在
B(D(Λ^{1/2}),H) 中绝对收敛；不把它说成 H 上有界。

第一组项及其交换子分别由 8∑|a_i|η_i、126∑|a_i|η_i 控制。
合并 (5.4)—(5.5) 并放大固定常数，得到 (1.5)。

### 5.3 系数截断与真实交换子域

上述界只依赖 ∥a∥₂、∥b∥₂。故任意有限系数逼近都使 R_fin 及其交换子在相同的带权算子范数中收敛。

若 x∈𝓓，则 𝓝x仍在𝓓，且有限部分满足

$$
\mathsf NR_{\rm fin}x
=R_{\rm fin}\mathsf Nx+[\mathsf N,R_{\rm fin}]x.
$$

右端收敛，R_fin x 也收敛。𝓝闭性给

$$
Rx\in\operatorname{Dom}\mathsf N,\qquad
\mathsf NRx=R\mathsf Nx+[\mathsf N,R]x.
\tag{5.6}
$$

这确认了本稿的交换子确为真实域上的交换子。若纯二阶乘子 T₀ 已在𝓓定义，实际有限乘子就在𝓓逐点收敛为 T₀+R。

每个有限差 R_fin 均 C 对称，而 C 保持𝓓并与Λ交换；极限因此仍在𝓓上 B 对称，形式通常伴随为 R^#=CRC。它享有相同的带权界。

## 6. 对称 Dirac 块所需的 Nelson form 接口

在 H⊕H 取比较算子 Λ₂=diag(Λ,Λ)，进位扰动块为

$$
\mathscr R=\begin{pmatrix}0&R^\#\\R&0\end{pmatrix}
\quad\text{于 }\mathcal D\oplus\mathcal D.
$$

它对称，且 (1.5) 给

$$
\|\mathscr R x\|\le C_f\|\Lambda_2^{1/2}x\|
\le C_f\|\Lambda_2x\|.
\tag{6.1}
$$

由 (5.6)，其像在 DomΛ₂ 中。对 x,y∈𝓓⊕𝓓，

$$
\begin{aligned}
&\langle\mathscr Rx,\Lambda_2y\rangle
-\langle\Lambda_2x,\mathscr Ry\rangle\\
&\hspace{2em}=\langle[\Lambda_2,\mathscr R]x,y\rangle,
\end{aligned}
$$

所以

$$
\boxed{
\left|
\langle\mathscr Rx,\Lambda_2y\rangle
-\langle\Lambda_2x,\mathscr Ry\rangle
\right|
\le
C_f\|\Lambda_2^{1/2}x\|\|\Lambda_2^{1/2}y\|.
}
\tag{6.2}
$$

这正是纯二阶 Dirac 块的相同次数 form 界所需的实际补充。即使 R 不保𝓓，(6.1)—(6.2) 仍然合法；不再错误地迭代实际算子并假设次数每次只升2。

本稿不独立重写抽象 Nelson 截断引理；l2_moments 正在将该引理及纯二阶估计写成相配的完整证明。

## 7. 真实二阶进位差确实可能无界

固定一个 i，取非负 a_j（j>i）属于 ℓ² 而不属于ℓ¹，例如 a_j=(j+1)^{-1}。
令

$$
f=\chi_i\sum_{j>i}a_j\chi_j.
$$

其实际与纯乘子之差为

$$
R=K_i L+\sum_{j>i}a_jV_iK_j,\qquad
L=\sum_{j>i}a_jS_j.
\tag{7.1}
$$

最后一项由 ∑|a_j|η_j<∞ 有界。下面证明 K_iL 无界。

K_i≠0：由 (3.5) 的两端单位可知 K_i=0 会迫 N_i=E_i，与真实非零进位差 ∥N_i−E_i∥=η_i>0 矛盾。又 K_i∈𝓤，即实际 UHF 代数，因此可用作用于有限低 m 位的矩阵 K^{[m]} 在算子范数中逼近 K_i。选择 m>i 足够大，使 K^{[m]}≠0，且误差 ε 远小于 ∥K^{[m]}∥。取低 m 位单位向量 x，使 ∥K^{[m]}x∥≥∥K^{[m]}∥/2。

记

$$
L_{m,n}=\sum_{m\le j<n}a_jS_j,\qquad
A_{m,n}=\sum_{m\le j<n}a_j.
$$

有限纯模型上 L_{m,n} 的唯一谱点为 A_{m,n}，且
∥L_{m,n}∥≤3A_{m,n}。故可取相应有限位单位向量 y_n，使

$$
\|L_{m,n}y_n\|\ge A_{m,n}/2.
$$

把 x⊗y_n 张量上更高位参考常数1，所得 u_n 为有限柱单位向量。则

$$
\begin{aligned}
\|K_iL_{m,n}u_n\|
&\ge
\|K^{[m]}x\|\,\|L_{m,n}y_n\|
-\varepsilon\|L_{m,n}\|\\
&\ge
\left(\frac{\|K^{[m]}\|}{4}-3\varepsilon\right)A_{m,n}.
\end{aligned}
$$

选择 ε<∥K^{[m]}∥/24 后，右端趋无穷，因为 a∉ℓ¹。

L 中 j<m 的有限部分一致有界。对 j≥n，u_n 不依赖这些位，
S_ju_n=χ_ju_n，两两正交，所以剩余尾的范数恰为
(∑_{j≥n}a_j²)^{1/2}→0。由 K_i 有界，这两部分都不会消去上述发散。因此 ∥K_iLu_n∥→∞，由 (7.1) 知 R 无界。

这证明了低位进位误差乘无限一阶尾的真实问题；其小标量 η_i 并不把无界算子变成有界算子。(1.5) 给出的较低次数相对界才是可用的结论。

## 8. 后续域问题仍须另证

一般二阶 gauge 差包含有限解析因子乘无限一阶闭乘子，所以可能无界。
即使已通过 Dirac/Nelson 证明实际二阶闭乘子 C 自伴，也不能仅从
U_ζ𝓓=𝓓 就推得 U_ζDomX=DomX，更不能把这种差直接塞进 R122 的有界解析差定理。

本稿只解决实际进位的次数权、定义域和较低阶扰动接口。二阶全 H 循环性需另行处理 gauge 差的定义域及其在实际核上的值域结构。

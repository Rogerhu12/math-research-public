# R893：原五个 sum-Hom 的单分母完整纤维与初始 RR Schur 证书

日期：2026-11-16 UTC。会话：serre-public-astra-20261115。

本文补充 [R872 §§5–6](../notes/R872-original-point-jets-and-bounded-two-weight-RR-kernels.md) 的实际入口，保持原 $g_j=(1+\mathcal T^j)f$、$1\le j\le5$，不换成 R803 的负号优化方向或旧 R805 candidate。新增的是：从已指定的全局函数构成一个同权98的单分母表达式，在每个完整272维纤维中只用该分母的单位证，再以标量插值消去初始关系中的整个 A 块，使新矩阵的目标秩恰为原极除子次数。

这是准确证明和有限计算契约。原 R849 的523节点全局 DAG、R877 的零支 A、R827 的零支 B 和导数算子已有来源；其余六个同 $\zeta$ 分支的12个 A/B 右端现已由公开 run43849775574 成功完成，全部1380×12关系通过。真实七支次序为 [0,6,1,2,4,3,5]，准确单位解及其约化见 [R880 实际认证](R880-certified-original-seven-Galois-normal-inputs.md)。本篇的五个新初始 RR 核仍未计算，不预填其纤维、秩或极除子基。

## 1. 原来源、方向和标量

保持原 $Y/L$、$g(Y)=127$、原无基点铅笔 $(\tau,\sigma)$、$H=(\tau)_0$、$\deg H=272$，以及

$$
z=\sigma/\tau,\qquad
\mathcal V_n=\{z^a\beta_i:0\le a\le n-\epsilon_i\},\qquad
\epsilon=(0,1^{144},2^{127}).
$$

正常基次序不变。$\mathcal V_n$ 表示原 $H^0(nH)$ 在 $\tau$ 图的函数，维数

$$
d_n=272n-126\quad(n\ge1).
\tag{893.1}
$$

原权二截面已经带自己的 $82^2$ 尺度，S5 行已经带 $82^{10}$。本篇没有第二次乘除。

三个准确来源各有不同用途：

1. [R849](R849-certified-original-global-function-and-five-polar-ideal-DAGs.md) 的 U.1 单位系统指定真正的全局 $y_f=A/B$。完整1234行和原2420单位解仍是其准确叶；四个 CM 响应不能代替它。
2. [R877](R877-certified-original-canonical-A-and-global-y-normal-input.md) 及 R827 将同一 free1186 方向的 A、B 运输到正常 V5 坐标。新六支消费者按 R849 的真实 image_of_original_b 求七循环，保每支完整1380行关系；不把排序后的根标签当 $\sigma$ 次幂。
3. R809 的六个已完成准确 normal 向量
   
   $$
   c_j=\theta U_j/\tau^4,\qquad 0\le j\le5,
   \tag{893.2}
   $$
   
   给原 $h_{\mathcal T^j f}/h_f=c_j/c_0$。每个向量保14个原 $b,s$ 坐标、两组准确分子/分母及自己的 original_target_rational_scales。只按原记录施一次尺度。

这里 $s=1+2\zeta$、$s^2=-3$，不是局部参数；$b$ 是原曲线 $C_b:y^2=x^3+b$ 的域元素，不是整生成元 $B_{\rm fld}=\lambda b$。固定辅助素点为 $p_{\rm aux}=1000000753$、原 $\zeta=549966761$、$s=99932770$。原 b 的像由同一 place audit 读取，全部系数分母和 $\lambda$ 的单位性实际核验。

[R791](R791-certified-original-Hom-descent-and-eta-inputs.md) 的真实作用为

$$
\mathcal T^jf=D_{\rho_j^{-1}}\sigma^j(f),\qquad
\rho_j^6=\sigma^j(b)/b,\qquad
\mathcal T^7=[\zeta^2].
\tag{893.3}
$$

$\sigma$ 固定 $K,z,w,\beta_i$，只作用于原 L 系数。原 $c_j$ 已含这一真实同靶微分的相位，不能再给 $c_j/c_0$ 乘一次 $\rho_j$。

## 2. 同一个原导数，七个原分式

在 $\tau$ 图将 A、B 及其共轭理解为除以 $\tau^5$ 的正常多项式函数。对固定 j 置

$$
C=\rho_j^{-3}\sigma^j(A),\qquad D=\sigma^j(B),\qquad
u=A/B,\quad v=C/D.
\tag{893.4}
$$

因此 $v=y_{\mathcal T^jf}$，不是未经同靶运输的 $\sigma^j(y_f)$。

使用原 R827 正则导数 $\delta_\tau$、$g=\delta_\tau z$ 和正常 connection $\Gamma_\tau$。若 $a(z)$ 是正常列，则

$$
\delta_\tau\!\left(\sum_i a_i(z)\beta_i\right)
=\Gamma_\tau a+M_g a'.
\tag{893.5}
$$

消费已成原 $\tau$ 算子索引及其全部行块；每个索引实际上含17个16行块，末块覆盖256至271行。其准确含义来自原 unit-node 插值及完整加权/交换子证，不声称已展开特征零 $\Gamma$。

正常次数界给 $\delta_\tau(V_5)\subset V_7$。原 $\sigma$ 与 $\delta_\tau$ 交换，$\rho_j$ 是常数。若另一完成消费者已保存同源 $\delta B$ 或 $\delta^2B$，应逐字复用相应叶，不再做同一乘法。

定义

$$
F=A^2-bB^2,\quad F_j=C^2-bD^2,\quad
W=B\delta_\tau A-A\delta_\tau B,\quad
W_j=D\delta_\tau C-C\delta_\tau D,
\tag{893.6}
$$

$$
R=c_jF_jW,\qquad S=c_0FW_j,\qquad
\Delta=R-S,\qquad \Xi=CB-AD.
\tag{893.7}
$$

原 [R803](R803-original-single-map-reuse-and-mixed-Hodge-ratios.md) (803.19)–(803.22) 给

$$
r_j^x=\frac{x_{\mathcal T^jf}}{x_f}=\frac RS,\qquad
y_{g_j}
=-u+\frac{(v-u)(2+r_j^x)}{r_j^x-1}
-\frac{(v-u)^3}{(r_j^x-1)^3(u^2-b)}.
\tag{893.8}
$$

原 $F,W_j,c_0$ 均非零，而 $\Delta\ne0$：否则 $r_j^x=1$，会使 $\mathcal T^jf=\pm f$，与原 $\Phi_{21}$ 同态域及 $1\le j\le5$ 矛盾。这些是全局函数的非零结论，不是每个纤维中分母为单位的预设。

## 3. 准确取消 F 一次后的单分母

置

$$
\boxed{Q_j=BD^3\Delta^3,}
\tag{893.9}
$$

$$
\boxed{
P_j=-AD^3\Delta^3
+\Xi D^2\Delta^2(2S+R)
-\Xi^3c_0^3F^2W_j^3.
}
\tag{893.10}
$$

则在原函数域中

$$
\boxed{y_{g_j}=P_j/Q_j,\qquad Q_j\ne0.}
\tag{893.11}
$$

**证明。** 在 (893.8) 中代入 $v-u=\Xi/(BD)$、$r_j^x-1=\Delta/S$、$u^2-b=F/B^2$。初始公共分母为 $BD^3F\Delta^3$，相应分子为

$$
-AD^3F\Delta^3+\Xi D^2F\Delta^2(2S+R)-\Xi^3S^3.
$$

由 $S=c_0FW_j$，分子三项都含同一个 F。原 F 非零，准确约去一次，正好得到 (893.9)–(893.10)。未取立方根、未换 $\rho_j$，也未另除任意 content。稠密开集恒等式给整个原函数域恒等式。证毕。

从 $A,B,C,D\in V_5$、$c_j\in V_4$、$F,F_j\in V_{10}$、$W,W_j\in V_{12}$ 得

$$
R,S,\Delta\in V_{26},\qquad P_j,Q_j\in V_{98}.
\tag{893.12}
$$

98是按正常导数输入界得到的保守同权，不声称最小权。实现只保有限运算 DAG 和各纤维值，不展开整个 V98，也不把 Q 的零除子称为 $E_{g_j}$。

### 3.1 两图帧的精确区别

写 $t=\tau/\sigma$。若第二图直接用 $A_\sigma=t^5A_\tau$、$c_{j,\sigma}=t^4c_{j,\tau}$ 和 $\delta_\sigma=t\delta_\tau$，Wronskian 的截面导数项相消，得到

$$
W_\sigma=t^{11}W_\tau,\quad R_\sigma=t^{25}R_\tau,\quad
(P_{\rm formula,\sigma},Q_{\rm formula,\sigma})
=t^{95}(P_\tau,Q_\tau).
\tag{893.13}
$$

若保存的是 (893.12) 的98权截面，其真正第二图坐标是

$$
(P_{98,\sigma},Q_{98,\sigma})
=t^{98}(P_\tau,Q_\tau)
=t^3(P_{\rm formula,\sigma},Q_{\rm formula,\sigma}).
\tag{893.14}
$$

正常基同时按 $\beta_{i,\sigma}=t^{\epsilon_i}\beta_{i,\tau}$ 运输。额外 $t^3$ 是两截面的共同帧因子，不是原 y 的新极点。首 scope 在有限 $\tau$ 纤维评价，完整极除子始终沿原 R849，不沿未约分高权表达式推断。

## 4. 完整 Artin 纤维，只要求真正使用的 Q 为单位

对原合法常数 z=a，记 $\mathcal A_a=\pi_*\mathcal O_Y/(z-a)$，其维数为272。该代数可以非约化、非分裂。原 W(a) 是乘 w 的完整矩阵。已有原 $K_a=(e_0,We_0,\ldots,W^{271}e_0)$ 及逆者直接复用；缺失者才新计算完整 K 和逆并核两边乘回。K 不可逆时保存实际失败并跳过整个 a。

R885 已完成的原特征多项式 $\chi(z,T)$ 及原节点关系可以直接消费：

$$
\mathcal A_a\simeq\mathbf F_{p_{\rm aux}}[T]/(\chi(a,T))
\tag{893.15}
$$

由实际 K 的单位性认证。不得重算273个 charpoly 节点；新节点最多评价已有多项式并核完整 relation。可用多项式 xgcd 或整个272乘法矩阵验证 Q 的单位性，成功必须保

$$
Q_j(a)\,Q_j(a)^{-1}=1\quad\text{在整个 }\mathcal A_a\text{ 中。}
\tag{893.16}
$$

随后计算 $P_j(a)Q_j(a)^{-1}$，并保完整272坐标乘回 $Q_j(a)y_j(a)=P_j(a)$。

不另强求 $c_0,F,W_j$ 各自为单位，因为它们在单分母式中并未分别求逆。若 Q 不是单位，仅意味着该表示在此完整纤维不能使用：不剥去其失败因子，不只保成功的某个剩余域，不推断所有这些点都是原 y 的极点。该 j 可跳过 a，同一 a 对其他 j 的完整单位检验仍有效。

一旦 (893.16) 成立，原函数在该完整纤维上正则。全部 O/O、二挠及支点的全局极除子重数仍由 R849 已证的两图 Cartier 理想给出：

$$
I_{E_{g_j}}
=I_{E_f}^3(\sigma^j I_{E_f})^3
\bigl((u^2-b)(1-r_j^x)^3,\ (u+v)^3,\ (u^2-b)(v+r_j^xu)^3\bigr).
\tag{893.17}
$$

没有以孤立点值替代完整极除子，也没有从 (893.9) 构造伪极除子。

## 5. 原初始 RR 的全局维数和完整纤维注入

令 $E_j=(y_{g_j})_\infty$，其次数 $e_j$ 是 R791 已成原 Hom Gram 的结果。取 R872 指定 n，写 $\delta_j=272n-e_j$、$r_j=\delta_j-126$。本节 r_j 是核维数，不是 x 比值或原次数比。

原层满射

$$
\mathcal O(nH)^2\longrightarrow\mathcal O(nH+E_j),
\qquad(a,b)\longmapsto a-y_{g_j}b
$$

在每个 DVR 都无遗漏，其核为 $\mathcal O(nH-E_j)$。由于 $\delta_j\ge255>2g-2$，全局截面给满射，故关系核恰为

$$
\mathcal R_j=\{(a,b)\in V_n^2:a=y_{g_j}b\}
\simeq H^0(nH-E_j),\qquad \dim\mathcal R_j=r_j.
\tag{893.18}
$$

其像维数为 $d_n+e_j$。

选 N 个互异完整纤维，且每个原 Q_j 为单位。若

$$
272N>272n+e_j,
\tag{893.19}
$$

则 $H^0(nH+E_j)$ 在这些纤维上的评价单射：在整个长度272N子概形上为零的截面，只能属于负次数线丛的零空间。这包括非约化纤维及各剩余次数，不能将每纤维压成一个点。

令 $E_n$ 为 Vn 的完整正常评价矩阵，$Y_j$ 为各纤维乘 $y_j(a)$ 的直和矩阵。于是

$$
M_j=[E_n,-Y_jE_n],\qquad
\ker M_j=\mathcal R_j,\qquad
\operatorname{rank}M_j=d_n+e_j.
\tag{893.20}
$$

## 6. 三个标量插值块消去整个 A

按正常列 $(i,k)$ 排序，$E_n$ 的第 $(a_\ell,i)$ 行只有该 i 的幂 $a_\ell^k$。对每个 i 取前 $m_i=n-\epsilon_i+1$ 个节点。这些行组成 $I_A$，恰有 $d_n$ 行。方块 $(E_n)_{I_A}$ 是272个标量 Vandermonde 的直和，只出现 $m=n+1,n,n-1$ 三种长度。

节点两两差为单位即证明该块可逆。准确逆由相应 Lagrange 多项式给出，不形成新的 $d_n$ 阶 dense inverse。设 $I_A^c$ 为余行，置

$$
H=Y_jE_n,\qquad
\Lambda=(E_n)_{I_A^c}(E_n)_{I_A}^{-1},
$$

$$
\boxed{\mathcal S_j=H_{I_A^c}-\Lambda H_{I_A}.}
\tag{893.21}
$$

关系 $a-y_jb=0$ 的已选行唯一给

$$
a=(E_n)_{I_A}^{-1}H_{I_A}b.
\tag{893.22}
$$

全部余行等价于 $\mathcal S_jb=0$。因此

$$
\boxed{\operatorname{rank}\mathcal S_j=e_j,\qquad
\dim\ker\mathcal S_j=r_j.}
\tag{893.23}
$$

这是原全局极除子的准确次数给出的秩，不是用新模计算反过来命名原方向。

| j | n | e_j | N | d_n | Schur 行×列 | 目标 Schur 秩 | 完整核 r_j | padding |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|12|2970|23|3138|3118×3138|2970|168|250|
|2|8|1674|15|2050|2030×2050|1674|376|42|
|3|8|1800|15|2050|2030×2050|1800|250|168|
|4|13|3024|25|3410|3390×3410|3024|386|32|
|5|14|3339|27|3682|3662×3682|3339|343|75|

实现可为不同 j 保不同合法节点列表，但同一个 z 的 W、K、逆和原代数身份只有一份。先读旧0至7；新选择只补真实缺失的 K。若所有单分母都在同一组27纤维为单位，可按表取其前缀，但不把这种便利当成功假设。

## 7. 单位子式、所有行和准确核的三个层次

所有输入先固定到同一个原合法素点。原七支 unit-solve、六个准确 C、R827 正常导数和完整纤维单位证，使 (893.21) 的准确矩阵在该 DVR 上整。消费者必须实际取得：

- $\mathcal S_j$ 中一个原行列明确的 $e_j$ 阶单位子式；
- 以非主元列为自由坐标的完整 $d_n\times r_j$ B 核，和由 (893.22) 恢复的同尺寸 A 核；
- 全部 Schur 行的乘回、全部 N×272 原关系 $A-y_jB=0$，以及自由行恒等子块。

准确 char0 核不是把有限域数组改标签。它由同一个准确 $\mathcal S_j$、真实选中行列及

$$
B_{\rm pivot}=-\mathcal S_{I,J}^{-1}\mathcal S_{I,F},
\qquad B_F=I
\tag{893.24}
$$

定义。实际模单位子式证明它存在且整；(893.23) 已独立给 char0 秩恰为 $e_j$，所以其余准确行也为零。保存的模数组是这个准确 unit-solve 表达式的约化。完整模乘回核实源和实现未接错，但不单独替代全局秩论证。

每个方向只有在上述条件全部通过时，才可标记 complete_initial_RR_space_certified=true。若固定素点发生输入非单位、节点不足或秩不足，保已完成阶段并诚实返回本次充分证书未完成；不自动换曲线、twist、分支或负号。

## 8. 原 P0 与后继有界代表的帧

原 $P_0$ 是 $c_0$ 在 Y 上的像，$\tau(P_0)\ne0$。原曲线映射从 $[x-c_0]$ 定义，所以非零 $g_j$ 在 $c_0$ 取 O，$E_j(P_0)>0$。

因为 $nH-E_j$ 的次数 $\delta_j\ge2g+1$，它全局生成。可在完成的关系核中选一对真正截面 $(\mathsf A_j,\mathsf B_j)\in H^0(nH)^2$，其正常函数为 $a_j=\mathsf A_j/\tau^n$、$b_j=\mathsf B_j/\tau^n$，使

$$
a_j(P_0)\ne0,\qquad a_j=y_jb_j.
\tag{893.25}
$$

由 DVR 等式，b_j 在 P0 的阶恰为原 $E_j(P_0)$，故

$$
\operatorname{div}_{nH}\mathsf B_j=E_j+F_j^*,\qquad
\deg F_j^*=\delta_j,\quad P_0\notin F_j^*.
\tag{893.26}
$$

实际选择可用原 R872 点评价泛函，在新核中取首个具有单位 a 值的列。若进一步归一化，该准确标量必须是原 unit-solve 的非零值；不能用有限域标量替代 char0 常数。若未找到模单位值，保此选择未成。

这给 R872 后继所需的真除子及主函数输入。得到完整 $H^0(3H-F_j^*)$ 后，padding 分别为250、42、168、32、75；原273阶 jets 足够。若再取得恰有该 padding 阶的真实截面 $\mathsf v_j$，完整等式仍为

$$
G_j=\frac{\mathsf B_j/\tau^{n_j}}{\mathsf v_j/\tau^3},\qquad
E_j-e_jP_0=(D_j^{\rm std}-H)+(n_j-2)\chi+\operatorname{div}G_j.
\tag{893.27}
$$

首 scope 不冒称该后继小核、$\mathsf v_j$ 或418空间已完成，也不漏掉 $\tau^{3-n_j}$。初始关系核可直接复用到后续乘法的已知 kernel，不再做相同的大 RREF。

尤其，初始 N 只为 (893.19) 选择，并非对整个 $V_{2n}$ 的无条件注入长度。后继两锚 membership 若仅在这些有限纤维检验，仍须独立的完整维数/单位秩夹逼或足够纤维注入；不能默默把初始 N 当成所有高权空间的注入界。

## 9. 最小实际源与执行顺序

### 9.1 必须读取的完成叶

输入组至少包括：

- R849 final、523节点 DAG 和 source audit 中的 global function、Galois、六 C、五 pole/eta 根。只读取本次真正使用的叶，不因未来范数而自动续整个395MB载体。
- R877 零支 A、R827 零支 B，以及已成功的 R880 seven-index、六个 A/B pair、七循环和完整1380验算证书。按实际 [0,6,1,2,4,3,5] 对应 sigma_power=0..6，不能将六个输出文件的分支顺序直接当 sigma 次序。
- R809 的 normal_vectors.C0 至 C5：六 index、十二 coordinate group、S5 basis index 的 row mapping。每组按 coordinate_numerators / column_denominators × original_target_rational_scales 解码，原14列完整保留。normal_basis_index、z_degree 仍从 S5 索引取；超过4−epsilon的最高 V5 系数须确实为零。
- R791 的 R791-original-Hom-Galois-matrices.json.gz 及原 eta 次数源，包含 field_sigma_b、rho_iterates_zero_through_seven。不重算 Hom、Norm 或次数。
- R827 的 W/place/grid、已成八个 K，g、Gamma 两个 tau index 的全部34行块及原完整 operator-identity 证书。同源已成 δB 小stage以显式复用项加入。
- R885 的已成 $\chi(z,T)$ 与需要的原节点 relation，不重 charpoly 或左伴随。
- 选标记对时才需 R872 的 P0 point-linearization 和准确原点来源。273 jets 留给后继 padding，首 kernel 不重新生成。

全部按真实 producer/run/core/configuration/manifest 及逐文件 bytes/SHA 绑定。R827 原长任务未完成不妨碍消费其已完成的具体算子叶；不得把原失败或预算 receipt 改成 success。


已经读取的七支实际身份如下；这些数值只登记来源，没有另作数学：

| 项目 | 实际值 |
|---|---|
| run / source commit | 43849775574 / 4a459acc8e430dbfe0ff232493c5ce1a9f493ced |
| core SHA256 | 3094615c9d73d77119065bfa74321a5ab42ba8714fe6b09624725919e8b46d23 |
| configuration SHA256 | 839ee1e1709b319a4c980cf8dba2c32e34f6bf149ca4b15b0c0920d16e71bee9 |
| artifact / bytes | 14219900447 / 128117604 |
| 平台 ZIP SHA256 | 8e05d15a2a4008ac7091785653f94c062490205a53f444095bbfa5b35a7f91a4 |
| manifest bytes / SHA256 | 10527 / c7deae057a4c142265e237fb671404ccaa71443d67d23bfbe623a939856f1d1d |
| 最终证书 bytes / SHA256 | 17836 / 1392b1d2cf74725e439ca1034e3c230a624c713c22e64a344fecc65b42e01e55 |
| seven-index bytes / SHA256 | 6538 / 24b236efc15629932a903d6d33b9e85e77b3462191f6a27430c06f443c07852d |
| 完整1380×12解证 bytes / SHA256 | 89253 / e77ea57ba3d7e91292f120b9c2b30ad7068ce5ae93f298028e1a74e278d8ddd9 |

### 9.2 原子阶段

建议阶段依赖依次为：

1. source-audit：七支次幂次序、b/λ/ζ、rho、C尺度和算子身份。
2. six-Hodge-normal-reductions：只做指定素点尚未完成的六个准确 C 约化。
3. branch-normal-derivatives：只缺失的 δA/δB，保 (893.5) 和正常次数界。
4. node-original-algebra：旧 K 只读，新 K 才形成并两边乘回；与旧 $\chi$ 完整关联。
5. node-sum-single-denominator：P、Q、单位或非单位证、完整 y 值；每个 j 独立记录，失败不剥因子。
6. sum-normal-interpolation、sum-Schur：准确行列次序、三个 scalar interpolation 块、选中完整纤维。
7. sum-unit-minor、sum-complete-initial-kernel、sum-all-original-fiber-relations：原单位子式、完整A/B核及所有行。
8. 可选 sum-marked-pair：P0 非零 A 值及 (893.26) 的准确表达式。

每步先写临时文件，再原子落盘；预算在完成阶段边界检查。旧 stage 不改 tag，新 consumer 有自己的 core/source/tag。续算恢复同 tag 的完成阶段和当前指针；节点搜索上限与预算可增，不能重做已成算术。

数学身份固定五个原正号 sum-Hom、各 n/e/N、正常基/尺度、导数/群律/相位、输入完整身份、节点扫描次序和核的自由坐标规则。实际完成的节点及所选 minor 必须逐项写入阶段；不把“某个可逆矩阵存在”当已保存输入。

### 9.3 输出的准确含义

最终每个 j 同时保存：原 $g_j$ 的 Galois/phase 根、$P_j/Q_j$ DAG、所有完整纤维单位证、Schur 源行列、准确 unit-solve kernel、实际模 A/B 数组和全行证。成功仅关闭原完整 $H^0(n_jH-E_{g_j})$ 接口。

原 $E_j$ 的完整极除子以及原 $\mathcal L_j,\mathcal L_j^R,\mathcal R_j$ 身份继续按 R849/GP/R791 保留。本文没有判定 theta 二挠、Picard 支持、非 p 校准、Poincaré 周期或高度。新数组、残差、矩阵和机器回执只在一日 active artifact/carrier 续传；Git 仅收源码、参数、纸面证明和简明实际运行/SHA登记。

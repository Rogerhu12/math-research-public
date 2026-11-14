# R77：局部权三系数空间的真实有限可达性

状态：**已证明**。本稿把 R73 局部第三密度中“速度面积与三次速度”的整个有限系数空间提升为真实可达空间。证明不假设冗余 profile 表达式独立，也不把一条有限数值路径的 rank 当作普遍满射。它不包含权一项，不自动支付不同 scalar 端口的基准第三响应、完整第四 $P_1$ 或其他更高条件。

## 1. 固定算子空间与目标

设实际 scalar 状态

$$
S=(h,k,\omega),\qquad h>0,\qquad
h_s=v,\quad k_s=w,\quad \omega_s=\frac{w}{2h}.
\tag{1}
$$

所有 profile 用同一固定右 collar 与同一物理支。R73/R76 的局部第三项有几何导数权分解
$\mathcal C_s=\mathcal C_s^{[1]}+\mathcal C_s^{[3]}$。

对权三部分，对称加速度项可以准确抽成 $D_sP_{\rm acc}$，余下为

$$
\mathcal C_s^{[3]}
=D_sP_{\rm acc}
+\mathcal A(S)(w h_{ss}-v k_{ss})
+\sum_{j=0}^3\mathcal B_j(S)v^{3-j}w^j.
\tag{2}
$$

这里 $\mathcal A,\mathcal B_j$ 是完整三线性 profile 算子，最后两输入对称；也可以投到对角 $q\mapsto\mathcal C_s(q;q,q)$。$P_{\rm acc}$ 为速度二次式。因此实际路径首末为常值 germs 时，它的两个端值都零。

由 R56 有限分离闭合及原始式的有限代数运算，$\mathcal A,\mathcal B_j$ 落在一个固定有限维实算子空间。令

$$
V_3=\operatorname{span}_{\mathbb R}
\{\mathcal A(S),\mathcal B_0(S),\ldots,\mathcal B_3(S):S\in U\},
\tag{3}
$$

其中 $U$ 是任意充分小的状态开集，闭包含于 $h>0$。这里按真实 profile 函数身份取商，不预设形式基独立。

对任意首末常值 germ 的真实开路径 $C$，定义

$$
\mathcal S_3[C]=\int_C\mathcal C_s^{[3]}.
$$

R76 已构造同一初始 scalar 端口、frame 恒等、总矩阵零的真实有限 loop 族，准确满足

$$
T_{\mathcal L_t}=2t\,\mathcal S_3[C].
\tag{4}
$$

式 (4) 没有 $O(t^2)$；它来自真实长度变化、一般倒行的 $\Phi_M^2$ 项、共同补偿桥消去以及 R71 交换子控制。不能把它替换成只看某个局部密度的假控制。

**本稿主结论：** 对任意 $\tau\in V_3$，存在有限个这样的真实 loop，其组合总矩阵零、frame 恒等、首末 scalar germ 相同，并有准确完整算子身份 $T=\tau$。在有界的目标系数邻域可保持固定有限控制词与光滑参数依赖。

## 2. 动态约束下的状态开集确实可访问

控制分布为

$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega,
\qquad
[X,Y]=-\frac1{2h^2}\partial_\omega.
$$

本稿不用仅引用 bracket rank 代替真实路径。以下有限控制词给出所需局部端点右逆。

从固定 $S_*=(h_*,k_*,\omega_*)$ 到邻近目标 $S=(h,k,\omega)$：

1. 保持 $k$ 不变，把 $h_*$ 改到 $h$，此段 $\omega$ 不变。
2. 保持 $h$ 不变，把 $k_*$ 改到 $k$，此段准确增加
   $(k-k_*)/(2h)$ 的 $\omega$。
3. 取固定小 $\eta\ne0$，走矩形
   $h\to h+\eta$；
   在 $h+\eta$ 把 $k\to k+a$；
   $h+\eta\to h$；
   在 $h$ 把 $k+a\to k$。

第三步的准确净增量是

$$
\Delta\omega
=a\left(\frac1{2(h+\eta)}-\frac1{2h}\right).
$$

选取

$$
a=
\frac{\omega-\omega_*-(k-k_*)/(2h)}
 {1/(2(h+\eta))-1/(2h)}
$$

便准确到达目标。分母在小状态盒内一致不为零。所有单段用固定光滑 flat step，$h$ 与 $k$ 不同时改变；所以以上积分不因平滑改变，接缝全部 jets 为常值。取目标盒充分小可保 $h>0$，并得到一个固定段数、光滑依赖 $S$ 的真实 prefix $P_S$。$\omega$ 始终是真积分，不进行末端回填。

实际 frame 按其 ODE 积分，位置按 $\alpha_s=h^2T$ 积分；这里不指定单条 prefix 的 frame 或末位置。

## 3. 任意局部路径的 signature 可以送到同一个端口

设 $C$ 从 $S\in U$ 出发，末端允许是另一个状态。比较两个真实开路径

$$
P_SC,\qquad P_S.
$$

局部积分严格可加，故

$$
\mathcal S_3[P_SC]-\mathcal S_3[P_S]=\mathcal S_3[C].
$$

分别对这两条路径应用 R76 的 (4)，得到都从 $S_*$ 出发并回到 $S_*$、frame 恒等、矩阵零的 loop。取第一条 loop 与第二条的真实倒行，因各自矩阵为零，composition 没有遗漏交叉项。得到

$$
T=2t\,\mathcal S_3[C].
\tag{5}
$$

因此比较的两条开路径末端不同没有问题：R76 各自在内部沿自己的真实 scalar 倒行返回；最终 loop 的端口始终同为 $S_*$。

式 (5) 不声称 prefix 的局部第三项为零；它使用同一 prefix 的两个实际积分准确相减。

## 4. 实际路径积分张成整个 $V_3$

令 $W$ 是所有在 $U$ 的小邻域内、首末为常值 germs 的真实短路径的 $\mathcal S_3[C]$ 之实线性跨度。由 (2)，直接有 $W\subseteq V_3$。

证明反向包含，用有限维对偶。设线性泛函 $\ell$ 在 $V_3$ 上满足 $\ell(W)=0$。任取 $S_0=(h_0,k_0,\omega_0)\in U$。

### 4.1 面积系数必须被 $\ell$ 消去

取一个非零 $a\in C_c^\infty((0,L))$，设计真实路径

$$
h=h_0+\varepsilon a,\qquad
k=k_0+\varepsilon a',\qquad
\omega_s=\frac{\varepsilon a''}{2(h_0+\varepsilon a)},
\quad \omega(0)=\omega_0.
$$

首末 $h,k$ 及所有导数回到常值。整个 $\omega$ 变化为 $O(\varepsilon)$，并有

$$
\omega(s)=\omega_0+\frac{\varepsilon a'(s)}{2h_0}
+O(\varepsilon^2)
$$

在固定区间上一致成立；末端的 $\omega$ 漂移为 $O(\varepsilon^2)$，允许真实保留，并未强行设零。

由 (2)，

$$
\mathcal S_3[C_\varepsilon]
=
2\varepsilon^2
\left(\int_0^L(a'')^2\,ds\right)\mathcal A(S_0)
+O(\varepsilon^3)
\tag{6}
$$

在固定有限算子空间中成立。系数变化为 $O(\varepsilon)$，三次速度项为 $O(\varepsilon^3)$；对称加速度势的端项准确为零。又
$\int((a'')^2-a'a''')=2\int(a'')^2>0$。

对 (6) 施加 $\ell$ 并除以 $\varepsilon^2$，令 $\varepsilon\to0$，得 $\ell(\mathcal A(S_0))=0$。这对所有 $S_0\in U$ 成立。

### 4.2 四个三次速度系数也必须被 $\ell$ 消去

取固定光滑 step $H$，首末为 0、1，端点附近常值，并满足 $H'\ge0$、非恒零。对任意实 $(u,v)$ 取

$$
h=h_0+\varepsilon uH,\qquad
k=k_0+\varepsilon vH,\qquad
\omega_s=\frac{\varepsilon vH'}{2h}.
$$

$\omega=\omega_0+\varepsilon vH/(2h_0)+O(\varepsilon^2)$，所以全状态仍只变化 $O(\varepsilon)$。该路径两个控制速度始终共线，故

$$
k_s h_{ss}-h_s k_{ss}=0
$$

逐点准确成立，不只是首阶近似。于是

$$
\mathcal S_3[C_\varepsilon]
=
\varepsilon^3
\left(\int_0^L(H')^3\,ds\right)
\sum_{j=0}^3\mathcal B_j(S_0)u^{3-j}v^j
+O(\varepsilon^4).
\tag{7}
$$

积分系数严格正。取 $(u,v)=(1,0),(0,1),(1,1),(1,-1)$，对 (7) 施加 $\ell$ 并取极限，得到 $\ell(\mathcal B_j(S_0))=0$，$j=0,1,2,3$。

因此任何消去 $W$ 的线性泛函都消去 (3) 的全部生成元。有限维线性代数给

$$
\boxed{W=V_3.}
\tag{8}
$$

这一步不把极限路径当作实际控制。极限只用于证明两个**线性跨度**相等；有限维空间随后保证存在有限条非零、真实、有限长度路径，其实际 signatures 就构成 $V_3$ 的基。

## 5. 形式 Laurent 单项系数也真正属于可达空间

若准确展开给

$$
\mathcal A(S)=\sum_\alpha m_\alpha(S)A_\alpha,\qquad
\mathcal B_j(S)=\sum_\alpha m_\alpha(S)B_{j,\alpha},
$$

其中 $m_\alpha=h^{a_\alpha}k^{b_\alpha}\omega^{c_\alpha}$ 是不同 Laurent 单项，$a_\alpha$ 可为负整数，那么每个 $A_\alpha,B_{j,\alpha}$ 都属于 $V_3$。

证明仍用对偶：若 $\ell$ 消去 $V_3$，则
$\sum_\alpha m_\alpha(S)\ell(A_\alpha)=0$ 在状态开集上成立。乘以一个足够高的正 $h$ 幂，得到普通多项式身份，迫使每个实系数 $\ell(A_\alpha)=0$。对 $\mathcal B_j$ 同理。这个证明不要求 profile 系数之间线性独立。

因此公开 exact decomposition 中属于速度面积或三次速度部分的任何完整 profile 系数，都有真实可达解释，不能再仅被称为任意未付的形式列。权一的 $k_s\mathcal R$ 不在本结论内；特别 $\int k_s$、$\int h^{-1}k_s$ 等端口约束不能拿本定理绕过。

## 6. 从跨度到准确有限控制

由 (8)，选有限条真实路径 $C_1,\ldots,C_d$，使
$\mathcal S_3[C_1],\ldots,\mathcal S_3[C_d]$ 构成实际算子空间的一组基。对给定 $\tau\in V_3$，解有限线性关系

$$
\tau=\sum_{\nu=1}^d c_\nu\mathcal S_3[C_\nu].
$$

用 (5) 的真实 loop 取名义总参数 $t_\nu=c_\nu/2$，便得到每项准确响应。参数超出局部区间时，预先选有限重复次数，将每条参数缩入固定小区间。所有 loop 的矩阵为零，故组合时第三响应严格相加，得到 $T=\tau$。

对有界光滑目标族 $\tau(\lambda)$，固定同一真路径基，$c_\nu(\lambda)$ 光滑；在紧参数盒选统一重复次数。R70/R72 的辅助路径、完整圈数与端点右逆也可在这些紧邻域上一次选定，所以得到固定有限词与光滑依赖，而非随极限无限拼接。

这是一条准确存在与可达性证明。它没有给出该有限真路径基的最短长度、定量条件数或嵌入厚度；也没有把形式代表的 rank 当作 $d$ 的已知准确值。

## 7. 共同物理域与全部端点条件

(4)(5) 的原语、两个 prefixes 与所有辅助桥必须共用同一 $x$ 区间和右锚。可以先取状态的紧小盒、固定的一个面积 pulse 与四种 step、以及统一小 $\varepsilon,t$ 区间。第 2 节给固定段数的 prefix 族；R70/R72 在其紧参数邻域给固定有限辅助控制，并有一致的 $h>0$ 下界与有限 $\omega$ 范围。

在这些完整控制族选择后，固定一个位于所有 $-\omega$ 之外的共同紧物理区间。随后在这个固定区间的真实 profile 算子空间上做第 4 节对偶论证并选择有限真路径基。所有小 pulse 和 step 的端点 $\omega$ 漂移都是实际 ODE 的结果；每个 R76 loop 各自沿真实倒行支付，所以最终 scalar 端口严格回到 $S_*$。

矩阵零、frame 恒等来自各个完整真实 loop，不是只从局部密度或样本残差推断。位置位移仍未指定，可由完整 R45 四块结构处理；没有被当作已经闭嵌入。

## 8. 对当前准确 $P_1$ 关系的具体意义

公开 Actions 43630157008 的新上界关系中，两条标为
$h^{-5}h_s^2k_s$ 与 $h^{-4}k h_s^3$ 的局部列属于本稿的三次速度系数空间。它们的任意有限实线性组合，因而可以由真实有限第三 loop 准确合成。这里使用的是该列所代表的完整 profile 函数，不是单个点值。

仍需把真实基准桥的整个权一项及其端口矩条件带入完整关系，并同时记录全部其他项。后三个线性 moment 的可实现性不能由本定理取代。随后还要支付其他 Fourier 模式、$P_0$、第四 ruling、更高阶与有限等距族，以及闭嵌入、reach 和宏观运动完成标准。


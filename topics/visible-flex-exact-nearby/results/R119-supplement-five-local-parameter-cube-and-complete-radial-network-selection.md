# R119 续篇：五个实际局部参数的完整径向网络谱选择

2026-11-14，visible-exact / tail_connector。

**状态：已证明的完整径向网络结论。** 本篇在每个完整负窗仅用
低缩放一维、紧缩放三维、高缩放一维共五个实际坐标，选出同一
无限 profile 和同一个 fixed-stop 外参数，使全部 retained
非零 Fourier 网络同时可逆。不同频率在同一个盒中沿不同的固定
方向作条件积分，不为每个频率另分配一个幅度。因此没有旧
$r_U/N_U$ 的模式数损失。

关键补充是完整谱流计数，而非假设 generator 的上界小于 $1/8$。
每个真正控制片的相对传递都在同一个 near-identity symplectic
图内；固定外接线可以有 Cayley 极点，必须作为 selfadjoint
relation 保留。由此每个固定目标圆点在整条参数弦上的谱交点
总重数至多真实端口维数。它给下面原 incoming 单位的带权逆：
$$
 \boxed{\quad
 \|\mathcal W_M(I-U_M)^{-1}\mathcal W_M\|\le1,\qquad
 (\mathcal W_M)_i^2
   =2^{-48}J_i^{-3}M^{-17/16}D_{i,M}.
 \quad}                                                    \tag{Q.1}
$$
$D_{i,M}$ 在 (Q.8) 明确给出，分别保留三个真实缩放范围。

这是径向完整网络的参数选择，包括正片、有限 prefix 和真实无限
低尾。它没有把非径向算子误差除以 (Q.1) 后宣称收缩，也没有给
尚未计算的原 source-to-label 或最终层权赋予权限。新的实际
mixed pocket 型仍须在下一完整非径向接合中消费。

## 1. 固定频率的真正有限网络，及无限低尾的归属

使用[控制后全标签图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
的同一个 radial 家族和原 fixed-stop 对象。完整负窗记为 $i$；
其控制下降坡所在层为 $j=j(i)\ge8193$，$J=j+5$。每个层有两个
下降坡，所以以下从头按完整负窗计数，不把层数当端口数。

令
$$
 \delta_j=(2/25)2^{-j},\qquad
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 T_j=2^{65664}J^2\delta_j^{-9},\qquad M_*=A_{8193}.          \tag{Q.2}
$$
对 $M\in4\mathbb N$、$M\ge M_*$，保留所有满足
$A_{j(i)}\le M\le T_{j(i)}$ 的完整负窗，记集合 $\mathcal I_M$。
它是有限的连续链。两阈值递增，且 $A_{j+1}<T_j$；
取最后一个 $A_j\le M$ 的层即证非空。若
$n_M=|\mathcal I_M|$、$d_M=2n_M$，安全地
$$
 n_M<2(8\log_2M+321),\qquad d_M<4(8\log_2M+321)<M .
                                                               \tag{Q.3}
$$
最后一式在 $\log_2M>984$ 上成立：写
$\log_2M=984+q+r$、$q\in\mathbb N$、$0\le r<1$，
左边小于 $32804+32q<2^{16+q}<2^{984+q}$。

深于 $\mathcal I_M$ 的所有层都在第53束 (C.10) 的真正低窗。
其 (C.24)--(C.48) 给同一允许 $C^4$ 球上的无限尾强解、非零
实允许列和完整 affine 位移。把它们准确送到 retained 链右端。
这不是把无限多个低包置零，也不以一个有限截尾代替它们。
前面的有限真实 prefix 则从原实允许线正向传播；不除高度，
竖直线直接用完整 unitary reflection 表示。

[完整径向网络](R119-supplement-complete-radial-unitary-network-and-global-eigenphase.md)
(U.2)--(U.10) 因而逐字给
$$
 U_M=P_M\bigoplus_{i\in\mathcal I_M}S_{i,M},\qquad
                    (I-U_M)x_M=g_M.                     \tag{Q.4}
$$
$P_M$ 包含全部真实 positive 两端 cross、两个外允许线和固定
连接置换，$g_M$ 包含其全部源。两端线可以依赖其它 profile
坐标和外参数，但在下一节为这个 $M$ 选出的直线方向上固定。
不需要先给 prefix 一个未经证明的 BVP inverse。

## 2. 同一个五维盒，不按频率分配参数半径

在每个负窗原未用区间中，按三篇已证构造放置互不相交的三组
支集：低组中心 $c-\ell/4$、高组中心 $c$、紧组中心
$c+\ell/4$，每组都包括自己的两个局部相位补偿。

使用[低缩放曲线](R119-supplement-low-scaled-exact-phase-curve-and-current-mixed-form.md)、
[紧缩放三维图](R119-supplement-compact-scaled-three-parameter-phase-chart.md)
和[高振荡完整两态](R119-supplement-exact-two-phase-curve-complete-oscillatory-generator.md)
的原半径，明确为
$$
 \rho_\ell=2^{-1024}J^{-8},\quad
 r_\ell=2^{-1000}\Delta^2\rho_\ell^9,\qquad
 \rho_h=2^{-40}J^{-2},\quad r_h=2^{-1000}\rho_h^{13},
$$
$$
 K_*=2^{4000}J^{40},\quad L_*=1+K_*,\quad
 \rho_c=2^{-2240}J^{-2}\Delta^{-11}L_*^{-10},
$$
$$
 \sigma_c=2^{-2110}\Delta^{-5}L_*^{-4}\rho_c^9,\qquad
 R_c=2^{-2300}\Delta^{-5}L_*^{-5}\rho_c^{10}.              \tag{Q.5}
$$
真实五坐标 $\vartheta_i\in[-1,1]^5$ 定义
$$
 \alpha_{\ell,i}=r_\ell\vartheta_{\ell,i},\qquad
 q_i=(R_c/3)\vartheta_{c,i},\quad \vartheta_{c,i}\in[-1,1]^3,
 \qquad \alpha_{h,i}=r_h\vartheta_{h,i}.                  \tag{Q.6}
$$
三个局部 phase 泛函各自准确为零；因支集不交，总 phase 也
准确为零。因此原径向 $\bar\Gamma$、根 germ、两端波单位和
positive 片不变。总 $C^4$ 小于
$2r_\ell+2R_c+2r_h<2^{-79}$。其复扩张也在第53--55束原完整
球内；完整 joint 图及 mean 的重新授予见上述三篇的原范围。
这里径向 $\bar\Gamma$ 固定不表示非径向 $\Gamma^*$ 两列为零。

对固定 $M$，记 $\kappa_i=M^2/B_i$。只在 $i\in\mathcal I_M$
的五坐标中选择常向量
$$
 v_{i,M}=
 \begin{cases}
 (1,0,0),&16/B_i\le\kappa_i\le1/4,\\
 (0,v_i(\kappa_i),0),&1/4<\kappa_i<K_*,\\
 (0,0,1),&\kappa_i\ge K_* .
 \end{cases}                                             \tag{Q.7}
$$
中间三分量是紧图 (N.18) 的固定方向，
$\|v_i(\kappa_i)\|_1<1/16$。$B_i,\Delta_i,\kappa_i$ 沿该线不变；
方向不随当前共振向量或盒点更新。令 $v_M$ 为其直和，
$\|v_M\|_1\le n_M$。其余全部坐标固定。

径向 (L.21)、(N.34)、(O.40)，以及原完整实子区间
$K_i=2^{6000}J_i^8\delta_i^{-16}$，给在整个五盒上
$$
 -iS_{i,M}^*D_{v_{i,M}}S_{i,M}>D_{i,M}I_2,\qquad
 D_{i,M}=
 \begin{cases}
 2^{-31400}J^{-160}\delta^{73/2}M^5,&\kappa_i\le1/4,\\
 2^{-861000}J^{-8300}\delta^{131/4},&1/4<\kappa_i<K_*,\\
 2^{-14800}J^{-64}\delta^{61/2}M^{-3},&\kappa_i\ge K_* .
 \end{cases}                                             \tag{Q.8}
$$
以下核对完整单位和半径。低组的局部原 wave 型是
$2^{-780}\rho_\ell^8\Delta^3M^5B^{-3}$，乘真实 $r_\ell$，
再用原两端 Green 比较除 $8K_i^2$。由
$B<2^7J\delta^{-3/2}$，所得下界大于
$2^{-31212}\Delta^5J^{-155}\delta^{73/2}M^5$，故第一行安全。
高组原 (O.40) 是
$2^{-1800}\rho_h^{20}B K_i^{-2}M^{-3}$，而
$B=8\sqrt6\Delta\delta^{-3/2}>2^{10}\delta^{-3/2}$，
故它大于 $2^{-14590}J^{-56}\delta^{61/2}M^{-3}$。
紧组原 (N.34) 准确给
$$
 \frac{\Delta R_c\sigma_c}{2^9L_*\sqrt B K_i^2}
 =2^{-58979}\Delta^{-218}L_*^{-200}
                   J^{-54}\delta^{32}B^{-1/2}.
$$
用 $\Delta<4J$、$L_*<2^{4001}J^{40}$ 和
$\sqrt B<2^4\sqrt J\,\delta^{-3/4}$，它大于
$2^{-859619}J^{-8272.5}\delta^{131/4}$，覆盖第二行。

不同组在本窗其它位置的 profile 不进入所选局部两态积分；
其到原端口的传播已经由同一个全 $C^4$ 球的 $K_i$ 支付。
因此 (Q.8) 不是把单组原点的型移到一个未核实的新盒。

条件固定其它坐标时，只有 retained negative windows 改变，
所以 $D_{v_M}P_M=0$。由 (Q.4) 准确有
$$
 G_M:=-iU_M^*D_{v_M}U_M
       >D_M:=\operatorname{diag}_{i\in\mathcal I_M}
                              (D_{i,M}I_2)>0 .           \tag{Q.9}
$$
没有借任意 near-kernel 的频率定位；这是固定 $M$ 的整个空间。

## 3. 每个实际控制片有同一个无极点相对传递图

为了谱积分，不对 $G_M$ 的上界作未经证明的小量假设。
先证明每个所选局部片在整个实际盒内存在一个固定的
symplectic trivialization，使其完整传递 $T_i$ 满足
$$
                         \|T_i-I\|<2^{-20}.              \tag{Q.10}
$$

低组和紧组使用物理通量保持态
$(\sqrt B\,u,u_t/\sqrt B)$。它是自然态
$(u,u_t/B)$ 同乘 $\sqrt B$，所以准确径向矩阵仍为
$$
 \Delta\begin{pmatrix}0&1\\
 (F_\Xi+e)^2/4-\kappa F_\Xi-\tau F_\Xi'/2&0
 \end{pmatrix},\qquad F_\Xi=F-\tau\Xi'.
$$
当前四阶盒给该矩阵 norm 小于 $2^{30}\Delta(1+\kappa)$。
整个三支集连同其间间隔的长度不超过 $12\rho$。
低组有 $1+\kappa<2$，紧组有 $1+\kappa\le L_*$；
由 (Q.5)，两种情况下
$12\rho\,2^{30}\Delta(1+\kappa)<2^{-100}$。
真实积分方程于是给传递及其逆与恒等的差小于 $2^{-98}$。
可再把固定 $\Xi=0$ 的传递吸收到右侧外片；
剩余相对传递仍满足 (Q.10)。

高组不能因短支集就令 $k\rho$ 小。使用其真实固定光学区间，
$k=\sqrt\kappa$ 和 (O.14)--(O.16)：
$$
 S<1,\quad |V_\alpha|<A=2^{128},\qquad
 \|\partial_\alpha V_\alpha\|_{L^1}<H=2^{512}\rho_h^{-3}.
$$
$\mathsf C_1=0$ 给所有 $\alpha$ 共用准确长度 $S$；支集外端
$F,F'$ 和物理两行转换也固定。对平衡态
$(\sqrt k\,X_1,X_2/\sqrt k)$，自由 generator 是反对称的 $kJ$，
其余 norm 积分至多 $A/k$。原高门
$k\ge2^{1600}\rho_h^{-10}$ 因而给全双向传递 norm 小于2。
完整 Duhamel 及固定左基准给
$$
 \|U_\alpha U_0^{-1}-I\|
       \le8r_hH/k
       =2^{-485}\rho_h^{10}/k<2^{-20}.                   \tag{Q.11}
$$
这是实际两行比较，不是只比一个 WKB 相位。
$U_0$ 作为固定 symplectic 因子并入相邻外片即可得 (Q.10)。

这些变换只用于谱流计数。它们均固定于当前 $M$ 和所选组，
沿参数弦不变；不将其 norm 冒作原 source 或端口权的常数1。
原 Green 配对保留，故局部 scattering 的参数 generator
仍严格正定，虽其定量下界可与 (Q.8) 不同。

把 (Q.10) 按原准确两端公式化为普通酉 $S_i^{\rm loc}$。
令 $W=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$，
则该公式和 $|\alpha|\ge1$ 直接给
$\|W^*S_i^{\rm loc}-I\|<2^{-16}$。
令
$$
 V_i=W^*S_i^{\rm loc},\qquad
 C_i=i(I-V_i)(I+V_i)^{-1}=C_i^*,\qquad \|C_i\|<2^{-15}.
                                                               \tag{Q.12}
$$
这是全盒上的同一个 Cayley 图。沿 (Q.7) 的方向，
$$
 C_i'=2(I+V_i)^{-*}(-iV_i^*V_i')(I+V_i)^{-1}>0 .         \tag{Q.13}
$$
正性来自完整 profile Green 型及实际 incoming 到内部两态的
双向等价，不要求某个单侧 incoming 分量非零。

## 4. 任意目标圆点的完整谱流计数

固定其它所有坐标及外参数，在五盒的一条 $v_M$ 弦上变化 $s$。
对任意固定 $z\in\mathbb S^1$，原特征方程是
$$
 b=S_M(s)a,\qquad a=z^{-1}P_Mb.                         \tag{Q.14}
$$
把每个所选短控制片以外的部分准确消去。得到
$$
 a_{\rm loc}=P_z b_{\rm loc},\qquad
 b_{\rm loc}=\left(\bigoplus_i S_i^{\rm loc}(s)\right)a_{\rm loc},
                                                               \tag{Q.15}
$$
其中 $P_z$ 普通酉且不依赖 $s$。

这里须说明消元合法性。原负片及固定负子片的传递可逆，
其两端 transmission 是 $1/\bar\alpha\ne0$。
完整实正段的 DN cross 也非零：以一端零高度、单位导数的
基本解写另一端 Dirichlet 解，其 Wronskian 恒定且非零，
cross 为该非零端值的倒数乘固定非零通量因子。
等价的正段 unitary transmission 因而非零。
乘 $z^{-1}$ 不改变此性质。任意两个固定 lossless 两端口的
串联分母为 $1-r_1r_2$；有非零 transmission 就有 $|r_i|<1$，
故分母不为零。有限 prefix 接模长1的外 reflection 同样成立。
因此固定部分沿一维链逐段准确消去，无隐藏的 decoupled
kernel；(Q.14) 与 (Q.15) 的核双向等价，维数相同。
原无限低尾此时已经是 (Q.4) 中那个真实外 reflection，
不在这里重新作无穷消元。

令 $C(s)=\bigoplus_i C_i(s)$，
$Q_z=(\bigoplus_i W)^*P_z^*$。则 (Q.15) 等价于
$V(s)x=Q_zx$。不能假设 $I+Q_z$ 可逆。定义真正自伴关系
$$
 \mathcal A_{Q_z}
 =\left\{\left(\frac{(I+Q_z)x}{2},
                  \frac{i(I-Q_z)x}{2}\right):x\in\mathbb C^{d_M}\right\}.
                                                               \tag{Q.16}
$$
置 $E_z=\ker(I+Q_z)^\perp$。该关系的 domain 为 $E_z$，
值域可加任意 $E_z^\perp$；其单值部分 $A_z$ 是 $E_z$ 上
自伴矩阵。于是 (Q.15) 准确化为
$$
               [\,P_{E_z}C(s)|_{E_z}-A_z\,]y=0.         \tag{Q.17}
$$
这里没有遗漏 $y=0$ 的额外核：若 $(I+Q_z)x=0$，
原等式同时要求 $(I+V)x=0$，而 (Q.12) 使 $I+V$ 可逆，
故 $x=0$。

由 (Q.13)，(Q.17) 的导数严格正定。有限维 min--max
说明它的每条有序特征值严格递增；每条最多过零一次。
故整条弦内，原 $U_M(s)$ 经过任意给定 $z$ 的交点总重数满足
$$
       \#\{s:z\in\sigma(U_M(s))\}\ \text{按核重数计}
                              \ \le\dim E_z\le d_M.     \tag{Q.18}
$$
不需要其它特征值的间隙，也不需要沿弦固定某条特征向量。
此论证对每个目标 $z$ 单独成立；固定接线 $P_z$ 可以随 $z$
变化，不将它误称为与谱参数无关。

## 5. 立方体弦积分，不按频率增加参数

先固定频率 $M$、外参数及所有 $\mathcal I_M$ 之外的坐标。
剩余真正均匀参数域是 $[-1,1]^{5n_M}$。记
$$
 a_M=\min_{i\in\mathcal I_M}D_{i,M}>0,\quad
 \varepsilon_M=(2^{16}n_Md_MM^{17/16})^{-1},
 \quad \xi_M=a_M\varepsilon_M,
$$
$$
 L_M=1+\log(8/\xi_M),\qquad
                   \mathcal T_M=2^{16}n_Md_MM^{17/16}L_M. \tag{Q.19}
$$

沿每条 $v_M$ 弦，真实酉矩阵可取连续展开的 eigenphase
$\phi_k$；有限维自伴局部对数及解析分支给几乎处处
$$
 \phi_k'=\langle w_k,G_Mw_k\rangle
           \ge\langle w_k,D_Mw_k\rangle\ge a_M .          \tag{Q.20}
$$
重根的一阶分裂是该 eigenspace 上同一正定 generator 的限制。
利用 (Q.18)，对 $|1-e^{i\phi}|<\xi_M$ 的小圆弧作真实变量
代换，整条弦中坏集合长度小于
$4d_M\xi_M/a_M$，无论 eigenphase 是否跨过 $2\pi$。

在其补集上令 $R_M=(I-U_M)^{-1}$。完整谱分解给
$$
 \|D_M^{1/2}R_MD_M^{1/2}\|
 \le H_M(s):=\sum_k
       \frac{\langle w_k,D_Mw_k\rangle}{|1-e^{i\phi_k}|}.
$$
由 (Q.18)--(Q.20) 和
$|1-e^{it}|\ge2|t|/\pi$，弦上的积分满足
$$
 \int_{\rm good}H_M\,ds
   \le d_M\int_{\substack{-\pi\le t\le\pi\\
                       |1-e^{it}|\ge\xi_M}}
                          \frac{dt}{|1-e^{it}|}
   <4d_M L_M .                                         \tag{Q.21}
$$
这一步以真实谱流计数替代旧的 generator 上界，
未把某个巨大条件数放进 logarithm 外。

从弦积分回到均匀立方体时，准确几何因子是
$\|v_M\|_1/2\le n_M/2$。证明可从所有入流面直接参数化：
第 $k$ 个面的 Jacobian 是 $|(v_M)_k|$，面体积
$2^{5n_M-1}$；除以全立方体体积后求和即得该因子。
因而不产生 $2^{5n_M}$ 的额外损失，也不使用一个未经证明的
共同长度参数区间。

由 (Q.19)--(Q.21)，条件概率满足
$$
 \mathbb P\{\operatorname{dist}(1,\sigma(U_M))<\xi_M\}
       <2n_Md_M\,\xi_M/a_M
          =2^{-15}M^{-17/16},
$$
$$
 \mathbb P\{\text{非前项坏集且 }
             \|D_M^{1/2}R_MD_M^{1/2}\|>\mathcal T_M\}
       <2^{-15}M^{-17/16}.
$$
合并得
$$
 \mathbb P(\mathcal B_M)<2^{-14}M^{-17/16}.              \tag{Q.22}
$$
没有把不同频率的 $v_M$ 相加成一个不存在的全频正方向；
同一个概率空间中的每个事件各自作以上条件积分即可。

## 6. 一次公共选择，以及每个窗口自己的明确权

给所有五盒及原 normalized 外参数 $t\in[0,1]$ 取产品概率。
(Q.22) 对其它全部参数统一。因
$$
 \sum_{M\in4\mathbb N}M^{-17/16}
  =4^{-17/16}\sum_{r\ge1}r^{-17/16}
  <\tfrac14(1+16)<5 ,
$$
全部 middle 坏事件的并集概率小于 $5/16384$。
对每个真实 profile，原 fixed-stop 的新允许线
good-$t$ fibre 测度至少 $1-83/16384$。再次用 Fubini，联合
好集测度严格大于
$$
                         1-\frac{88}{16384}>0 .         \tag{Q.23}
$$
所以确有同一无限 profile 和同一个外参数，所有 retained
频率同时满足间隙 $\xi_M$ 和带权 resolvent 门。
负频率由实系数的共轭同时得到，不再另选一次度量。

下面把全频量 $\mathcal T_M$ 支付成各 active 层自己的权。
由 (Q.8)、$M\le T_j$，所有范围安全地有
$$
                  D_{i,M}>2^{-862000}J_i^{-8300}
                                      \delta_i^{115/2}. \tag{Q.24}
$$
最不利的高组使用 $M^3\le2^{196992}J^6\delta^{-27}$；
低组和紧组的 $\delta$ 幂更有利。
若 $x=\log_2M$，active 层的 $A_j\le M$ 给
$\delta_j^{-1}\le2^{320}M^8$、$J_j<8x+322$。因此
$$
 a_M^{-1}<2^{880400}(8x+322)^{8300}M^{460}.              \tag{Q.25}
$$

对任意 active 的当前层 $J$，$M\le T_j$ 还给
$x<20J$，所以 $n_M<322J$、$d_M<644J$，
$(8x+322)<161J$。代 (Q.25) 到 (Q.19) 得
$$
              L_M<2^{14}J,\qquad
              \mathcal T_M<2^{48}J^3M^{17/16}.          \tag{Q.26}
$$
这里可直接核对 logarithm：常数 $880400$ 小于 $108J$；
$\log(161J)<J/128$ 在 $J\ge8198$ 上先在首层成立且差的
导数为正；$460\log M<9200J$。其余
$\log(2^{19}n_Md_MM^{17/16})+1$ 小于 $25J$，
合计仍小于 $2^{14}J$。又 $322\cdot644<2^{18}$，
故最后常数是 $2^{16+14+18}=2^{48}$。

将 (Q.26) 逐窗口代入
$\|D_M^{1/2}R_MD_M^{1/2}\|\le\mathcal T_M$，
立即得到开头 (Q.1)，即
$$
 (\mathcal W_M)_i^2=
 \begin{cases}
 2^{-31448}J^{-163}\delta^{73/2}M^{63/16},
                                      &\kappa_i\le1/4,\\
 2^{-861048}J^{-8303}\delta^{131/4}M^{-17/16},
                                      &1/4<\kappa_i<K_*,\\
 2^{-14848}J^{-67}\delta^{61/2}M^{-65/16},
                                      &\kappa_i\ge K_* .
 \end{cases}                                             \tag{Q.27}
$$
由 $\mathcal W D^{-1/2}$ 的每个对角元不超过
$\mathcal T_M^{-1/2}$ 可验证该推论；没有把不同层的费用先取最坏值。

一个只为后续预算方便的统一上包络是
$$
 (\mathcal W_M)_i^{-2}
       <2^{864000}J^{8330}\delta^{-1073/16}.              \tag{Q.28}
$$
高组代 $T_j$ 后的准确 $\delta$ 费用为
$61/2+9(65/16)=1073/16$，bits 为
$14848+65664(65/16)=281608$，$J$ 幂为 $601/8<76$。
紧组用 $M<2^{2004}J^{41/2}\delta^{-3/4}$；
其新 $\delta$ 费用仅 $131/4+51/64=2147/64$，
$J$ 幂小于8325，bits小于863200。
低组 $M\ge4$ 只改善其 $M^{-63/16}$。
所以三者均进入 (Q.28)。

这说明本次完整谱选择并未留下旧 $M^{1894}$ 的局部最坏费用。
如只要一个无权、同角宽的固定阶端口合同，也可由 (Q.25)
和 $8x+322<9x$（$x>984$）得到
$(9x)^{8300}\le9^{8300}8300!e^x<2^{141100}M^2$；
故 $a_M^{-1}<2^{1022000}M^{462}$。由 (Q.19) 和 $n_M,d_M<M$，
$$
              \|R_M\|<2^{1022016}M^{466}.              \tag{Q.29}
$$
这里 $e^x\le M^2$ 使用 $\log2>1/2$。
(Q.1) 的逐窗口权比这个粗无权结论保留更多真实信息。

## 7. 原角宽、完整源和下一完整非径向门

原局部角权仍可同时保留。由 (Q.24)，
$-\log D_{i,M}<2^{14}J$；由 (Q.26)，
$\log\mathcal T_M<2^6J$。
而原 $M\ge A_j$、$h_j=8\delta_j^{1/256}$ 给
$2^{-800}Mh_j>2^{31j/256-837}$。
旧已付的分块比较在 $j\ge8193$ 使它大于 $2^{25}J$，
所以同一个选择仍满足
$$
 \|W_M^{-1}R_MW_M^{-1}\|\le1,\qquad
                (W_M)_i=e^{2^{-800}Mh_i}.             \tag{Q.30}
$$
没有重定义 $h_j,\zeta_j$ 或原标签。

产品连续性及闭间隙、闭 resolvent 条件给非空紧好集。
各曲线实际半径随层趋零，且第53束的真无限尾图保持产品连续。
可以沿外 $t$、各层五坐标顺序逐个取该紧集的最小坐标，得到
一个确定的实际共同点。这不是数值枚举了无穷参数数组。

(Q.1) 的完整源结论是：对 (Q.4) 的原 canonical incoming
单位，唯一解满足
$$
             \|\mathcal W_Mx_M\|
                       \le\|\mathcal W_M^{-1}g_M\|.     \tag{Q.31}
$$
$g_M$ 仍为所有负窗的两态 ordinary/weak particular、
完整 positive total-DN affine、两个外允许线的源，以及真实
high prefix 和无限 low 余尾的源。局部 Cayley 计数并没有把
这些源换成任意可免费指定的向量。
转回 bare flux 时，真实 $F^t$ 端荷仍由原源空间提供；
有序变换保完整材料密度、Jacobian 和 normal shear。
$M=0$ 的独立高度与通量积分以及 $M<M_*$ 的有限 head
不在本非零 retained 谱门中，继续由各自完整方程处理。

本篇的参数族也属于已经重付的实际 joint 全图，但 (Q.9)
使用的是径向 $P_M$ 固定及逐 Fourier 分解。
实际非径向的端图、$\Gamma^*$ 两列、全部邻片响应和不同
$\kappa$ 包之间的项不能因此被删除。
下一步须在同一权下比较完整实际网络，或直接在其 near-kernel
上付谱选择；尤其 (Q.28) 的 $1073/16$ 和实际
$\mathcal N_{i|j}$ 的 $31867/256$ 衰减必须逐项合账，
不能只说后者很小便授予 Neumann inverse。
原 source-to-label、物理重建、三个外部响应和最终
$\mathcal F=0$ 仍需在该共同参数点真正闭合。

以上为新的解析证明，没有本地数值实验或未运行的通过门。

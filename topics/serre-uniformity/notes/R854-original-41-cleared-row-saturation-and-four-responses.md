# R854：原 41 地方的全行饱和、逆范数界与四响应

日期：2026-11-16。本文是原 U.1 同一规范解的地方求值算法，不是新的全局关系重构。新数学只在本公开仓库 Actions 执行；本文及源码的本地检查仅限文本、AST、来源 SHA 和 schema。现有辅助素数 $1000000753$ 的 $518$ 位球以及尚未通过 A.1 的短候选，均不是本算法的 $41$ 处数值输入。

前置文件为 41C（正式 SHA256 `569aa684267e4c4ae76581ce6ad6c6b4fd2ad62b45869ed87809a4c22151eeee`）、原 U.1、SP、41S，以及 ZA（`268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97`）。本核首先输出 $A_0,A_1,B_0,B_1$ 的有保证精度的原 $L_{41}$ 球；单个 $Z$ 和五个椭圆一阶行是后继消费者，不把它们或原高度提前写成已完成。

## 1. 精确域和唯一未知

仍使用原 R781 的

$$
L_{41}=\mathbf Q_{41}[B,s]/(F_B(B),s^2+3),\quad
B=\lambda b,\quad \lambda=2^6 3^{180},\quad v_L=7v_{41}.
\tag{854.1}
$$

$F_B$ 是原首一 Eisenstein 七次多项式；$B$ 是统一化元，剩余域为 $\mathbf F_{41^2}=\mathbf F_{41}[s]/(s^2+3)$。保留原十四坐标顺序 $B^0,\ldots,B^6,sB^0,\ldots,sB^6$。原 $20$ 个实圆分坐标仅用于原全局方程系数的展开，不改变点的原定义域。

令 $F_n$ 是原 $1234$ 个五次截面的 $v^n$ 系数行，值在 $\mathbf Q[t]/g(t)$，$0\le n\le128$。全部 $1234$ 条真实整数行直接读取；原相位变换不重算。令原带符号矩阵 $Z$ 为旧 rational-blocks 所给的稀疏 $1234\times1214$ 整矩阵，其二十个 pivot 行和 free 对角尺度均保留。写

$$
G_n=F_nZ,\qquad G_0=0.
\tag{854.2}
$$

未知只有

$$
u=(A_0^{\rm coeff},\ldots,A_{1233}^{\rm coeff},
C_{p_0},\ldots,C_{p_{1185}})^t\in L^{2420}.
\tag{854.3}
$$

这里 $p_i$ 是原 chart 实际 pivot_columns；原 free_column $1186$ 置 $1$，另外二十七个 free 坐标置 $0$。本节的 $A_i^{\rm coeff}$ 是截面坐标，区别于最终 CM 响应 $A_0,A_1$。未知及其规范化完全等于已认证 U.1 的规范解，没有选另一条五次关系。

## 2. 不求 κ 逆的同解全行系统

原已成 R781 行给 $R_j$ 和 $K_j=\kappa^j$，$R_0=K_0=1$。冻结 R787 的准确 Laurent 规范为

$$
Y(v)=vy(v)=\sum_{j\ge0}\frac{-R_j}{246^3\kappa^{j+1}}v^j.
\tag{854.4}
$$

其原未清方程是 $vFA-YFC=0$，其中 $FC$ 在此记作 $G C$。对 $m=1,\ldots,128$，定义

$$
\mathcal C_m(C)=\sum_{j=0}^{m}R_{m-j}K_jG_jC,
\qquad
\mathcal A_m(A)=246^3 K_{m+1}F_{m-1}A.
\tag{854.5}
$$

原完整 cleared 方程恰为

$$
\mathcal A_m(A)+\mathcal C_m(C)=0.
\tag{854.6}
$$

因此新矩阵和右端为

$$
\mathcal M_m=
[\,246^3K_{m+1}F_{m-1},\ \mathcal C_m|_{\rm piv}\,],
\qquad r_m=-\mathcal C_m(e_{1186}).
\tag{854.7}
$$

每个方程在真实 $1,t,\ldots,t^{19}$ 基展开，得到 $2560\times2420$ 的 tall 矩阵 $\mathcal M$ 和同长右端 $r$。$m=0$ 的二十行由 $G_0=0$ 恒为零，仍在最终原 $129\times20\times14$ 检查中保留并核验。

**此处不是在同样数字行号上替换清分母方程。** 对每个 $m$，从原未清二十行到 (854.6) 的变换，是在 $L[t]/g(t)$ 上乘非零元素 $246^3\kappa^{m+1}$ 的完整 $20\times20$ 乘法矩阵。它准确可逆；新矩阵取全部块，未擅称原 U.1 选中行的同号子块仍可逆。原 U.1 的真实 $2420$ 阶单位图证明未清全矩阵列秩 $2420$，故 (854.7) 也有列秩 $2420$，且有同一个准确解。实际 $41$ 单位行以后由新算法选择。

这里的新计算是这些原准确系数在指定 $41$ 处的求值和组合。原 Laurent 行、$K_j$、$R_j$、$Z$、$F$ 都不重建。既不求 $\kappa^{-1}$，也不读或重算原十四个辅助素数 Schur 逆。

## 3. 初始整化和精度编码

读取每个原 $R_j,K_j$ 的 primitive_integer_vector 和 rational_scale；同时保两个真实比例，不能因乘积有共同 content 就遗漏尺度。可以取可明确复核的整数 $e_R,e_K\ge0$，使所有 $41^{e_R}R_j$、$41^{e_K}K_j$ 的十四乘二十坐标均整。按这些整向量组装

$$
M^{(0)}=41^{e_R+e_K}\mathcal M,\qquad
b^{(0)}=41^{e_R+e_K}r.
\tag{854.8}
$$

A 块使用 $246^3\,41^{e_R}(41^{e_K}K_{m+1})F_{m-1}$；C 块使用两条已整化向量的乘积，故两块的实际共同尺度严格相同。初始行变换是 $T^{(0)}=41^{e_R+e_K}I$，其每行下界为 $7(e_R+e_K)$。可随后按已知实际行赋值做更小整化，但每项须写入同一变换账本，不能抹去初始尺度。

有限精度以 $N=v_L$ 的整数指数记。第 $i$ 个 $B$ 次幂系数保至 $41^{\max(0,\lceil(N-i)/7\rceil)}$，两条 $1,s$ 坐标相同。后端可以用共同模数 $41^{\lceil N/7\rceil}$ 保存任意 lifts，运算后再按七个实际系数模数约化。所有 lifts 的差属于 $B^N\mathcal O_L$，不表示获得了未计算的高位。

加减乘只用整数模矩阵 API。rank、inverse、rref 仅在素数 $41$ 的剩余域限制标量矩阵上调用。禁止向仅适用于素数的 inverse/rank API 传 $41^q$。参考官方 python-flint 0.9 [nmod_mat](https://python-flint.readthedocs.io/en/stable/nmod_mat.html) 和 [fmpz_mod_mat](https://python-flint.readthedocs.io/en/stable/fmpz_mod_mat.html) 的接口限制。

## 4. 行饱和和准确变换

保持准确等式

$$
M^{(h)}=T^{(h)}\mathcal M,\qquad b^{(h)}=T^{(h)}r,
\qquad v_L(T^{(h)}_{ij})\ge w_i^{(h)}.
\tag{854.9}
$$

在剩余域上选实际独立行 $I$ 和同阶列 $J$，秩为 $r_h$；必须核选中 minor 可逆，并准确核全部剩余行等于它们的线性组合。令组合矩阵为 $E_h$。每个剩余域系数 $a+bs$ 按 $a,b\in\{0,\ldots,40\}$ lift 到 $\mathbf Z_{41}[s]$。这是整系数 lift，不必是 Teichmüller lift。

保独立行不变，把其他行 $j$ 改成

$$
M_j^{(h+1)}=
\frac{M_j^{(h)}-\sum_{i\in I}(E_h)_{ji}M_i^{(h)}}{B},
\quad
b_j^{(h+1)}=
\frac{b_j^{(h)}-\sum_{i\in I}(E_h)_{ji}b_i^{(h)}}{B}.
\tag{854.10}
$$

矩阵分子属于 $B\mathcal O_L$ 已由完整剩余域恒等式证明。右端不必仍整；源码单独保存其公共 $B$ 幂，不能假装右端可整除。可等价保持 $b^{(h)}=B^{-h}v^{(h)}$：独立行的 $v$ 乘 $B$，依赖行的 $v$ 取原整线性差。这样所有储存的 $v$ 仍整。

每个改动行的下界更新为

$$
w_j^{(h+1)}=
\min\bigl(\{w_j^{(h)}\}\cup
\{w_i^{(h)}:(E_h)_{ji}\ne0\}\bigr)-1.
\tag{854.11}
$$

未改行下界保持。实际行置换及系数、源行引用、除 $B$ 次数、输入/输出精度必须完整保存。

**停止性。** 原列秩为 $n=2420$，故非零 $n$ 阶行子式生成一个有限赋值的理想。若当前剩余秩 $r_h<n$，每个 $n$ 阶子式包含至少 $n-r_h$ 个依赖行；(854.10) 使这个子式理想的最小赋值严格下降至少 $n-r_h$。有限次后必有剩余秩 $n$。这使用完整子式理想，不能把某个实际恒零行被反复除 $B$ 叫作严格进展。有限精度若只见零余项，则请求更多系数；不得推准确奇异，也不得在没有精度的状态继续除 $B$。

## 5. 实际左逆范数证书

当真实剩余秩达到 $n$，取那 $n$ 个实际行 $I_*$，

$$
U=M^{(h)}_{I_*},\qquad L=U^{-1}T^{(h)}_{I_*}.
\tag{854.12}
$$

$U\in\mathrm{GL}_n(\mathcal O_L)$，故 $U^{-1}$ 整，$L\mathcal M=I_n$，并有

$$
v_L(L_{ij})\ge w_*:=\min_{i\in I_*}w_i^{(h)}.
\tag{854.13}
$$

不必材料化特征零 $L$ 或 $U^{-1}$。证书必须包含完整行变换来源、实际 $2420$ 阶剩余域逆乘回和 $w_*$。若某原规范候选 $\widetilde u$ 的全部 $2560$ 个原完整残差满足

$$
v_L(\mathcal M\widetilde u-r)\ge R,
\quad\text{则}\quad
u-\widetilde u\in B^{R+w_*}\mathcal O_L^{2420}.
\tag{854.14}
$$

可报告保守损失 $\gamma=\max(0,-w_*)$ 与 $R-\gamma$。如果核验用的是整化残差 (854.8)，须先减 $7(e_R+e_K)$，不可把整化尺度增益称原残差精度。四个准确泛函再各按其系数赋值下界传播；常数项亦按真实球精度处理。

## 6. 剩余域实现与单位 Dixon

对 $A+sB$ 的剩余域矩阵使用交错的限制标量表示

$$
\begin{pmatrix}A&-3B\\B&A\end{pmatrix}
\tag{854.15}
$$

（实际源码行列按每个原坐标的两个分量交错排列）。它是 $\mathbf F_{41}$ 上的真实矩阵；秩是原域秩的两倍。按完整坐标对的顺序取 rank profile，得到的 pivot 必成对；源码逐项断言。选中方块 inverse 的所有 $2\times2$ 块必须仍为 (854.15) 的形状，并全矩阵乘回。这样只依赖已公开的 nmod_mat(41)，没有未暴露的扩域 matrix API 或不固定 ABI。

饱和后只求一个规范右端。以 $v$ 和共同幂 $B^{-h}$ 保存右端，对 $U\widehat u=v$ 做 $B$-adic Dixon：

$$
d_k=(\bar U)^{-1}\overline{r_k},\quad
r_{k+1}=\frac{r_k-U\widetilde d_k}{B},\quad
\widehat u_{k+1}=\widehat u_k+B^k\widetilde d_k.
\tag{854.16}
$$

$\widetilde d_k$ 是未分歧整 lift，每步分子完整余项为零才可除 $B$。实际 $u=B^{-h}\widehat u$。每次仅矩阵乘向量，不重复剩余域大逆。所有已成数字、当前准确剩余及旧 SHA 链原子保存；硬断后只做下一未完成位。

在任一目标精度层结束时，必须回到全部原 cleared 行计算 (854.14)，不是仅验选中 unit 行，也不是只验新 Dixon 余项。原 U.1 已证规范解存在，故这个左逆误差证书给同一原点的四个数值响应，不要求先接受它们为短有理坐标。

## 7. 实际来源与断点

纯 IO adapter 已认证 POINTS 的 $270$ 个原成员、$529$ 节点逐字前缀于 $733$ 节点、十七个准确域常量和同一四响应。GLOBAL 的最小原数学叶闭包是 $1368$ 个文件：$1234$ 条原 F 行、$131$ 个原 R781 字段/Laurent 文件、原 chart/Z 两件及 CM 准确表达式一件。GLOBAL 的 $395061658$ 字节 opaque carrier 尚未本地下取；这个边界必须如实保留，公共 runner 在使用时核真实包 SHA、原 inventory、parent/child 身份和每个选取成员。

后继 public config 不填任何不存在的 $41$ 数值来源。数学 tag 绑定：原 $p=41$、原 $F_B,\lambda,s$、上述 source inventory、所有冻结 helper 源 SHA、41C/本文证明 SHA、free1186 与实际 pivot 列、正号 cleared 算子、初始尺度规则、剩余域 lift 规则及行饱和策略。预算、请求绝对精度排除在数学身份之外；改变算法或原图必须新 tag。

阶段至少包括：原来源 audit；实际 $41$ 系数精度层；A 行块与 C 列块；当前整矩阵及尺度；每次剩余 rank/profile/组合与准确行变换；首次 unit minor；逐位 Dixon current；全原残差及四响应。旧数学阶段原样复用。只读 IO、重新组装已成块的内存视图不标为新数学阶段。

增加精度时旧低位必须直接保留并作降精度相容核验；不能重做已成 rank/profile 或 Dixon 位。若完整高精度矩阵尚未到，只给需要的实际 precision request，保留现有变换和数字，不把不确定零当失败。工作大矩阵可在其替代 current 已原子提交后按明确 receipt 清理，完整 row-op/数字历史和最新必要块始终随一日 carrier 传递。

本核成功字段为 `actual_original_p41_four_response_balls_certified=true`；只有实际 unit-minor、inverse-norm 和 full-residual 证书都存在才可置真。`expanded_exact_L_coordinates_accepted`、`A1_exact_zero_proved`、`actual_Z_computed`、`actual_height_computed` 初 scope 一律为 false。后继若消费这些球继续原 [42]/sigma，必须用 41C 的实际 ball 分母识别及完整尾界，不能复用任何辅助素数球。

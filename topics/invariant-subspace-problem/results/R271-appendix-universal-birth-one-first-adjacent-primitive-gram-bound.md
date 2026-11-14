# R271 附录：任意有限正权的整个出生一 primitive 空间，首处相邻比较常数一

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；boundary 独立复核。

## 0. 范围与来源

本稿把有限正权行的**整个**出生一 primitive 空间纳入一个与位数、权比无关的比较：
$$
\Gamma_1\Gamma_2^{-1}\Gamma_1\prec\Gamma_0.
\tag{0.1}
$$
这里先对完整物理孔层求逆，再压缩到同一个 primitive 空间；没有改用环境 Gram 的错误对数凹不等式，也没有把某条对称线当作全空间。

此前四异常权加等权池的全出生结果见
[四异常权全出生附录](R271-appendix-four-exceptional-weights-full-birth-uniform-primitive-gram-bound.md)。
本稿去掉该权型限制，但只证明出生 $s=1$ 的首处相邻边。
任意出生、全部相邻高度的通用常数仍未获得。

实际精度矩阵与条件子集协方差的关系来自
[R239 倒数权对偶附录 §7](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)。
下面从完整 $D^r(D^*)^r$ 重新推导所需恒等式。
此前工作接口中已经指出：逐个单项式的矩阵系数可以不正；
本稿保留全部同支持位集合上的多项式，再作有限精确验证。

可运行的独立证书为
[同支持分组整数证书](../notes/2026-11-13-universal-birth-one-first-edge-support-certificates-1cf.mjs)；
原始 UTF-8 blob 为 `9117ecbd7118a0562055129df5a0365c8f11562b`。
证书仅使用 JavaScript 的精确 BigInt 加减乘和有限组合枚举，不用浮点数、优化器或外部符号包。

## 1. 真正的孔层、完整逆与定理

取 $N\ge4$ 个物理位和任意 $a_i>0$。
令 $\mathcal H_s$ 是标准正交平方自由基 $e_I$、$|I|=s$ 张成的空间，
$$
D=\sum_{i=1}^N a_iE_i,\qquad z_i=a_i^2,\qquad
a=(a_i)_{i=1}^N,\qquad A=\operatorname{diag}(a_i).
$$
在 $\mathcal H_1\cong\mathbb C^N$ 上，
$$
K=\ker(D:\mathcal H_1\to\mathcal H_0)=a^\perp.
$$
对 $0\le r\le N-2$ 定义
$$
F_r=\frac{D^r(D^*)^r}{(r!)^2}\bigg|_{\mathcal H_1},
\qquad
\Gamma_r=P_K F_r^{-1}|_K.
\tag{1.1}
$$
所有逆均为完整 $\mathcal H_1$ 上的逆。

**定理。** 对上述任意 $N$ 和正权，
$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1\prec I_K=\Gamma_0.}
\tag{1.2}
$$
严格号表示二次型对每个非零 $K$ 向量严格成立，不声称存在统一小于一的常数。

按既有真实最小逆与高度块字典，若 $A_2,A_3$ 是出生一的实际相邻第一下降块，则
$$
A_3A_3^*\prec4 A_2^*A_2.
\tag{1.3}
$$
此处只换回阶乘：$H_1=\Gamma_1$、$H_2=\Gamma_2/4$。
此处的出生层与原完整最小逆始终相同。

## 2. 从完整 Gram 推出真实精度

记
$$
e_k=\sum_{|I|=k}z_I,\quad z_I=\prod_{i\in I}z_i,\quad
M_k=\sum_{|I|=k}z_I\,1_I1_I^*,\quad
m_k=\sum_{|I|=k}z_I\,1_I.
$$
直接作用于 $e_I$ 给
$$
D^{k-1}e_I=(k-1)!\sum_{i\in I}\frac{\prod_{j\in I}a_j}{a_i}e_i,
\qquad
F_{k-1}=A^{-1}M_kA^{-1}.
\tag{2.1}
$$
当 $1\le k\le N-1$，$M_k$ 正定：
若全部 $k$ 元子集上的坐标和为零，交换任意两个坐标先迫各坐标相同，再由一个子集和迫其为零。
故 (1.1) 的完整逆确实存在。

在 $\mathbb Ca\oplus K$ 上消去 $\mathbb Ca$ 的完整 Schur 补，得
$$
C_k=F_{k-1}
-\frac{F_{k-1}aa^*F_{k-1}}{a^*F_{k-1}a}
=A^{-1}\left(M_k-\frac{m_km_k^*}{e_k}\right)A^{-1}.
\tag{2.2}
$$
这里用到了 $M_k1=km_k$、$1^*m_k=ke_k$。
于是
$$
C_ka=0,\qquad C_k|_K=\Gamma_{k-1}^{-1},
\qquad C_1=I-\frac{aa^*}{e_1}=P_K.
\tag{2.3}
$$
这也是质量 $z_I/e_k$ 的条件子集协方差乘 $e_k$ 后的同余。

由 $C_2|_K>0$，(1.2) 准确等价于
$$
C_3\prec C_2^2\quad\text{在 }K\text{ 上}.
\tag{2.4}
$$
以下证明 (2.4)，全程保留同一 $K$。

## 3. 一个次数十的真实矩阵多项式

写
$$
S=e_1,\quad Z=e_2,\quad W=e_3,\quad T=\operatorname{diag}(z_i),
\quad u=(S-T)a,\quad v=(Z-ST+T^2)a.
$$
由 (2.2) 得
$$
C_2=SI-2T+aa^*-\frac{uu^*}{Z},
$$
$$
C_3=ZI-2ST+3T^2+Saa^*-Taa^*-aa^*T-\frac{vv^*}{W}.
\tag{3.1}
$$
定义真正的矩阵多项式
$$
\mathcal M_N(z)=Z^2W\,A(C_2^2-C_3)A.
\tag{3.2}
$$
其每项总次数为十，系数为整数，且 $\mathcal M_N1=0$。

为完全避免根号和分母，可等价使用
$$
B_2=ZM_2-m_2m_2^*,\qquad B_3=WM_3-m_3m_3^*,
$$
$$
\mathcal M_N=W B_2A^{-2}B_2-Z^2B_3.
\tag{3.3}
$$
式中 $\sum_k(B_2)_{ik}(B_2)_{kj}/z_k$ 逐项是多项式，因为每个因子都含 $z_k$。

对 $i\ne j$，令 $x=z_i,y=z_j$，并记
$$
f(x)=S^2+2Z-3Sx+2x^2,\qquad
g(x)=Z-Sx+x^2.
$$
由 (3.1) 展开，或在 (3.3) 中合并 $\sum z_i^\ell$，得到
$$
\begin{aligned}
(\mathcal M_N)_{ij}=xy\{&
(2S-x-y)Z^2W\\
&-[f(x)(S-y)+f(y)(S-x)]ZW\\
&+(SZ+3W)(S-x)(S-y)W\\
&+g(x)g(y)Z^2\}.
\end{aligned}
\tag{3.4}
$$
对角项由
$$
(\mathcal M_N)_{ii}=-\sum_{j\ne i}(\mathcal M_N)_{ij}
\tag{3.5}
$$
确定。
证书对四、五、六变量还独立从 (3.3) 重建矩阵，逐系数核对 (3.4) 的同支持部分，因此不是只重复一套显式系数表。

## 4. 为什么有限个支持组精确穷尽任意位数

对每个单项式 $z^\alpha$，令其支持为
$J=\{i:\alpha_i>0\}$。
由 (3.4) 的 $z_iz_j$ 因子和 (3.5)，该单项式的系数矩阵只作用于 $J$。
把 $J$ 外变量全部置零后，其系数完全不变。
因此它与仅含 $|J|$ 个物理位的同一公式给出的系数完全相同，与环境 $N$ 无关。

令 $\mathcal M^{[J]}$ 为收集**恰好**支持 $J$ 的全部单项式所得矩阵。
则有准确恒等式
$$
\mathcal M_N=\sum_{\substack{J\subset[N]\\|J|\le10}}\mathcal M^{[J]}.
\tag{4.1}
$$
也可按零延拓后的容斥式定义
$$
\mathcal M^{[J]}=\sum_{U\subset J}(-1)^{|J|-|U|}\mathcal M_{|U|}(z_U).
$$
没有舍弃跨物理位项，也没有对真实矩阵作不保持正性的压缩替换。

支持数小于三时为零。
支持数等于三时，由 $C_3=0$（唯一三元子集的协方差为零）得
$$
\mathcal M^{[J]}=e_2(z_J)^2e_3(z_J)\,
A_JC_2(z_J)^2A_J\succeq0.
\tag{4.2}
$$
低支持项为零，故这里整个三变量表达式就等于恰支持三的分组。

剩下的支持数只有 $4,5,6,7,8,9,10$。

## 5. 四、五、六位同支持组：完整主子式整数证书

设 $m\in\{4,5,6\}$，定义
$$
K_m(z_1,\ldots,z_m)
=\frac{\mathcal M^{[\{1,\ldots,m\}]}{z_1\cdots z_m}.
\tag{5.1}
$$
这是总次数 $10-m$ 的对称实矩阵多项式，且 $K_m1=0$。
删去最后一个坐标得到 $(m-1)\times(m-1)$ 主块 $\widehat K_m$。

证书逐个生成全部 $\beta\in\mathbb N^m$、$|\beta|=10-m$，
从 (3.4) 精确提取 $\alpha=\beta+(1,\ldots,1)$ 的系数。
然后用子集 Laplace 递推，精确计算 $\widehat K_m$ 的每个前导主子式。
所有出现的系数均为严格正整数：

| 支持数 $m$ | 前导阶数 | 非零系数个数 | 最小系数 |
|---|---:|---:|---:|
| 4 | 1 | 52 | 1 |
| 4 | 2 | 298 | 1 |
| 4 | 3 | 832 | 2 |
| 5 | 1 | 107 | 5 |
| 5 | 2 | 916 | 24 |
| 5 | 3 | 3636 | 108 |
| 5 | 4 | 9996 | 324 |
| 6 | 1 | 120 | 12 |
| 6 | 2 | 1275 | 135 |
| 6 | 3 | 6170 | 1350 |
| 6 | 4 | 20325 | 10125 |
| 6 | 5 | 53094 | 263250 |

这里验证的是整个多项式，没有对权值抽样。
对任意 $z_i>0$，每个前导主子式都严格正，故
$$
\widehat K_m>0,\qquad K_m\succeq0,\qquad \ker K_m=\mathbb C1.
\tag{5.2}
$$
最后一步只用行和零：
任意 $x\in\mathbb C^m$ 的二次型等于
$(x_1-x_m,\ldots,x_{m-1}-x_m)$ 在 $\widehat K_m$ 上的二次型。

精确提取算法如下。
在 (3.4) 中先把大括号写为 $S,Z,W,x,y$ 的有限多项式。
对每一项 $cS^AZ^BW^Cx^dy^e$，欲取 $z^\alpha$ 的 $(i,j)$ 系数，
先从 $\alpha_i,\alpha_j$ 扣去 $1+d,1+e$，
再取 $e_1^Ae_2^Be_3^C$ 的对应系数。
后者递归选择一、二或三元子集；相同当前指数分组的选择数用准确二项式系数支付。
递归总次数严格下降，穷尽所有贡献。

主子式部分使用基数 $32$ 编码变量指数。
最高主子式总次数为 $20$，因此不会发生进位混淆；
所有键都在 JavaScript 精确整数范围内。
所有系数均用 BigInt。
程序不把缺失单项式误计为正：它要求每个主子式非零，且逐项拒绝非正系数，再核对上表。

## 6. 支持至少七的全部系数矩阵

总次数十且支持至少七的指数分拆只有下面七个。
同一分拆的其他单项式仅对应物理位的排列。

| 指数分拆 | 非对角系数情况 |
|---|---|
| $(4,1^6)$ | 全部不正，最大为 $0$ |
| $(3,2,1^5)$ | 只有两个特殊坐标之间为 $70$ |
| $(3,1^7)$ | 全部负，最大为 $-30$ |
| $(2^3,1^4)$ | 全部负，最大为 $-84$ |
| $(2^2,1^6)$ | 全部负，最大为 $-60$ |
| $(2,1^8)$ | 全部为 $-420$ |
| $(1^{10})$ | 全部为 $-840$ |

证书由 (3.4) 重新提取七个系数矩阵，核对上述符号和唯一例外。
行和零的对称矩阵若非对角项不正，其二次型就是正权差平方之和。

唯一例外 $(3,2,1^5)$ 仍严格可控。
把前两坐标记为 $x,y$，其余五坐标记为 $v_1,\ldots,v_5$。
系数为
$$
M_{xy}=70,\qquad M_{xv_i}=-34,\qquad
M_{yv_i}=-104,\qquad M_{v_iv_j}=-59\ (i\ne j).
$$
令 $\bar v=5^{-1}\sum_i v_i$、$X=x-\bar v$、$Y=y-\bar v$。
完整二次型准确等于
$$
100|X|^2+450|Y|^2+140\operatorname{Re}(\bar X Y)
+433\sum_{i=1}^5|v_i-\bar v|^2.
\tag{6.1}
$$
其两变量矩阵
$$
\begin{pmatrix}100&70\\70&450\end{pmatrix}
$$
行列式为 $40100>0$，故该系数矩阵亦半正定。

这样支持 $7$ 至 $10$ 的每个单项式系数矩阵均为半正定；
乘以正单项式并求和仍半正定。
这里没有把支持 $3$ 至 $6$ 的坏单项式拆开：
它们已经分别由 (4.2) 和完整 $K_m$ 主子式支付。

## 7. 拼回真实比较与严格性

由 (4.1)–(6.1)，任意 $N$ 和正权都有
$$
\mathcal M_N\succeq0.
$$
当 $N\ge4$，每个四位支持组在其常数向量的正交补上严格正。
若一个全向量不是常数向量，可选一个含两个不同坐标的四元子集；
该组二次型已经严格正，其他组均非负。
因此
$$
\ker\mathcal M_N=\mathbb C1.
\tag{7.1}
$$
由 (3.2) 的可逆对角同余，
$$
C_2^2-C_3\succeq0,\qquad
\ker(C_2^2-C_3)=\mathbb Ca.
$$
在 $K=a^\perp$ 上严格正。
最后用 (2.3) 的真实精度和 $C_2$ 的可逆同余，得到 (1.2)。

证书由 root 与 boundary 分别原样独立执行，全部 PASS；
四、五、六位从条件协方差的独立重建与显式系数逐项相等，
全部 $12$ 个前导主子式和全部 $7$ 个大支持分拆均通过。
结论由上述整数恒等和正系数验证给出。[命令行重放入口](../notes/2026-11-13-universal-birth-one-first-edge-reproduce.cjs)直接调用同一验证函数；终端离线期间只核其语法，不把它冒称终端运行。

### 7.1 同一任意正权族的末处相邻边

令 $h=N-2$，取倒数物理权 $b_i=a_i^{-1}$。
[R239 全出生倒数对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
给同一出生的准确同余
$
\Gamma_n(a)=Z_{\rm all}^{-1}B_1^*\Gamma_{h-n}(b)B_1,
\qquad
Z_{\rm all}=\prod_i a_i^2,
$
其中 $B_1:K_1(a)\to K_1(b)$ 是对角 $a_i^2$ 的限制，按原范数可逆。
将本稿首边应用于 $b$，得到
$
\Gamma_{h-1}(a)\Gamma_{h-2}(a)^{-1}\Gamma_{h-1}(a)
\prec\Gamma_h(a).
$
严格正矩阵的 Schur 邻居反转
$AB^{-1}A\prec C\Longleftrightarrow AC^{-1}A\prec B$
于是给
$
\boxed{
\Gamma_{h-1}\Gamma_h^{-1}\Gamma_{h-1}
\prec\Gamma_{h-2}.
}
$
所以本稿也支付全部任意正权出生一的末处边；$h=2$ 时它就是首边。
其余内部相邻阶仍不能由首尾两边推出。

## 8. 保留的缺口

本稿没有给出生 $s>1$ 的同样比较；
除 §7.1 的末处边外，也没有给出生一的其它内部相邻边，更没有给整个布尔下降算子的环境不等式。
既有有限模型到原连续尾的传递如被调用，仍须逐一保留对应的固定出生和高度。
原正常见证所需高出生源的完整比较与费用，不能由 (1.2) 免费获得。

## 9. 原完整无限正 $\ell^2$ 行的出生一首边

本节把 §§1–7 的有限模型结论真正传到无限原物理尾。
允许 $a=(a_i)_{i\ge1}>0$ 仅属于 $\ell^2$；
不要求 $\ell^1$，也不把无限对角 $A^{-1}$ 当成有界算子。

### 9.1 固定孔层上的准确算子与完整逆

令 $\mathcal H_p$ 是所有 $p$ 元有限子集的平方和空间。
在有限支撑向量上定义
$$
D_p:\mathcal H_p\to\mathcal H_{p-1},
\qquad D_p=\sum_i a_iE_i.
$$
对每个 $(p-1)$ 元集先用 Cauchy--Schwarz，再按输入集计数，得
$$
\|D_pf\|^2
\le \|a\|_2^2
\sum_{|J|=p-1}\sum_{i\notin J}|f_{J\cup\{i\}}|^2
=p\|a\|_2^2\|f\|^2.
\tag{9.1}
$$
所以 $D_p$ 有唯一有界延拓。
若 $a^{(N)}$ 是前 $N$ 位截断，同一估计给
$$
\|D_p(a)-D_p(a^{(N)})\|\le\sqrt p\,\|a-a^{(N)}\|_2.
$$
以下只使用这些准确固定孔层算子。

在 $\mathcal H_1=\ell^2$ 上置
$$
K=\ker D_1=a^\perp,\quad
F_0=I,\quad F_1=D_2D_2^*,\quad
F_2=\frac14D_2D_3D_3^*D_2^*.
\tag{9.2}
$$
记 $z_i=a_i^2$、$S=e_1(z)$、$Z=e_2(z)$、$W=e_3(z)$、
$T=\operatorname{diag}(z_i)$。
这些对称和均有限，且 $S,Z,W>0$。
有限支撑计算及 (9.1) 的范数极限给出完整空间上的恒等式
$$
F_1=SI-2T+aa^*,
$$
$$
F_2=ZI-2ST+3T^2+Saa^*-Taa^*-aa^*T.
\tag{9.3}
$$
因为 $T$ 紧，二者分别是正标量 $S I$、$Z I$ 的紧扰动。

它们没有核。
确实，$D_2^*f=0$ 等价于
$$
a_if_j+a_jf_i=0\quad(i\ne j).
$$
令 $t_i=f_i/a_i$，则所有二元和为零；取三个不同指标即得所有 $t_i=0$。
同样，$D_3^*D_2^*f=0$ 等价于
$$
t_i+t_j+t_k=0\quad(i,j,k\text{ 两两不同}).
$$
用两个共有两个指标的三元集相减，先得任意两个 $t_i$ 相等，再得它们全零。
这里只使用有限坐标的比值，未要求 $(t_i)$ 平方可和。

因此 $F_1,F_2$ 是正的可逆 Fredholm 算子；
它们在完整 $\mathcal H_1$ 上都有有界逆。
准确地定义
$$
\Gamma_r=P_KF_r^{-1}|_K,\qquad r=0,1,2.
\tag{9.4}
$$
这些也是 $K$ 上正可逆算子，且 $\Gamma_0=I_K$。

### 9.2 真实 Schur 精度与范数极限

仍令
$$
u=(S-T)a,\qquad v=(Z-ST+T^2)a,
$$
$$
C_2=F_1-\frac{uu^*}{Z},\qquad
C_3=F_2-\frac{vv^*}{W}.
\tag{9.5}
$$
所有向量和秩一算子有界。
由 $F_1a=2u$、$a^*F_1a=4Z$ 和
$F_2a=3v$、$a^*F_2a=9W$，
完整 $\mathbb Ca\oplus K$ Schur 补直接给
$$
C_2a=C_3a=0,\qquad
C_2|_K=\Gamma_1^{-1},\qquad
C_3|_K=\Gamma_2^{-1}.
\tag{9.6}
$$

对 $a^{(N)}$ 用同一完整 $\ell^2$ 公式定义 $C_{2,N},C_{3,N}$。
在前 $N$ 个坐标上它们正是有限模型的真实精度；
在其正交补上则分别为 $S_NI$、$Z_NI$。
故有限首边定理与 $S_N^2-Z_N>0$ 给
$$
E_N:=C_{2,N}^2-C_{3,N}\succeq0
\quad\text{于完整 }\ell^2.
\tag{9.7}
$$
而
$$
C_{2,N}\longrightarrow C_2,\qquad
C_{3,N}\longrightarrow C_3,\qquad
E_N\longrightarrow E:=C_2^2-C_3
$$
均为算子范数收敛：
$S_N,Z_N,W_N$ 收敛，
$T_N\to T$ 范数收敛，
$u_N,v_N$ 在 $\ell^2$ 收敛。
因此 $E\succeq0$。

### 9.3 固定四位组保留严格性

取 $f\notin\mathbb Ca$。
存在两个有限坐标使 $f_i/a_i$ 不同；再添加两个不同指标，得到一个固定四元集 $J$。
对 $N\ge\max J$，在前 $N$ 位上定义有限向量
$$
b_i=f_i/a_i\qquad(i\le N).
$$
§§4–7 的完整同支持分组，以及四位组 $K_4(z_J)$ 的严格正性，给
$$
\begin{aligned}
\langle E_Nf,f\rangle
&\ge
\frac{\prod_{i\in J}z_i}{Z_N^2W_N}
\,\langle K_4(z_J)b_J,b_J\rangle\\
&\ge
\frac{\prod_{i\in J}z_i}{Z^2W}
\,\langle K_4(z_J)b_J,b_J\rangle
>0.
\end{aligned}
\tag{9.8}
$$
第一步还保留了前 $N$ 位外的非负标量块。
最后的正数只依赖这个固定 $f,J$，不随 $N$ 变化。
令 $N\to\infty$，得到
$$
\boxed{E\succeq0,\qquad \ker E=\mathbb Ca.}
\tag{9.9}
$$
这一步没有用不成立的“有限维严格号自动传到极限”，
也没有对无限 $A$ 作有界可逆同余。

此外，
$$
E=(S^2-Z)I+\text{紧算子},\qquad S^2-Z>0.
$$
结合 (9.9)，$E|_K$ 是正可逆 Fredholm 算子。
所以对每个固定的正行 $a$，存在一个实际 $\varepsilon(a)>0$，
使
$$
\boxed{
\Gamma_1\Gamma_2^{-1}\Gamma_1
\preceq(1-\varepsilon(a))I_K.
}
\tag{9.10}
$$
这里由 (9.6) 作 $C_2^{-1}$ 同余；
没有声称 $\varepsilon(a)$ 对所有正 $\ell^2$ 行有统一下界。

### 9.4 对原连续尾的准确范围

原纯尾
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j
$$
满足本节全部假设。
因此对每个固定 $m$，**原完整连续尾**的整个出生一 primitive 空间满足 (9.10)；
对应真实第一下降块有
$$
A_3A_3^*\preceq4(1-\varepsilon_m)A_2^*A_2,
\qquad \varepsilon_m>0.
\tag{9.11}
$$
这一次不再依赖有限等权池或近似源，也没有遗漏尾位置。

结论仍只涉及出生一的首处相邻边。
本节没有无限维的最高孔层，所以不把有限倒数权末边搬到无限尾；
出生 $s>1$、其余相邻高度以及原正常来源的高出生费用仍然保留。

## 10. 原连续尾出生一首边：显式常数二与渐近极限

本节使用 §9 的原完整固定孔层算子，直接得到比常数四更强的原尾估计。
不改变出生层，也不引入有限等权池。

### 10.1 一般稀散正行的真实精度估计

先按 $\|a\|_2$ 缩放，使 $S=\sum_i a_i^2=1$；
量 $\Gamma_1\Gamma_2^{-1}\Gamma_1$ 在这种缩放下不变。
写
$$
z_i=a_i^2,\quad
\delta=\max_i z_i,\quad r_2=\sum_i z_i^2,\quad
e_2=(1-r_2)/2,\quad e_3=\sum_{i<j<k}z_iz_jz_k.
$$
令 $P=I-aa^*$，以下全部算子作用于同一 $K=a^\perp$。
置
$$
B=PTP|_K,\qquad p=PTa,\qquad w=P(T^2-T)a.
$$
则
$$
0\preceq B\preceq\delta I,\qquad
\|p\|^2=\sum_i z_i^3-r_2^2\le\delta r_2.
\tag{10.1}
$$
由于
$$
PT^2P|_K=B^2+pp^*,
$$
§9 的准确精度变为
$$
C_2=I-2B-\frac{pp^*}{e_2},
\qquad
C_3=e_2I-2B+3B^2+3pp^*-\frac{ww^*}{e_3}.
\tag{10.2}
$$
因此完整平方差为
$$
\begin{aligned}
C_2^2-2C_3={}&r_2I-2B^2
-\left(6+\frac2{e_2}\right)pp^*
+\frac2{e_2}(Bpp^*+pp^*B)\\
&+\frac{\|p\|^2}{e_2^2}pp^*
+\frac2{e_3}ww^*.
\end{aligned}
\tag{10.3}
$$
没有把 $(PTP)^2$ 当作 $PT^2P$；
两者的差正是上式中的 $pp^*$ 项来源。

保留全部负项、只舍两个明确正项，并估计交叉项，得
$$
C_2^2-2C_3
\succeq
\left[
r_2-2\delta^2-
\left(6+\frac{2+4\delta}{e_2}\right)\|p\|^2
\right]I.
\tag{10.4}
$$
再用 $r_2\le\delta$、$e_2\ge(1-\delta)/2$，得到可检查的充分条件
$$
\boxed{
C_2^2-2C_3\succeq
r_2\left[
1-\frac{\delta(10+2\delta)}{1-\delta}
-\frac{2\delta^2}{r_2}
\right]I.
}
\tag{10.5}
$$
当方括号严格正时，真实压缩逆满足
$$
\Gamma_1\Gamma_2^{-1}\Gamma_1\prec\tfrac12 I_K.
\tag{10.6}
$$
这是一般正 $\ell^2$ 行的充分条件，没有宣称它对任意权型自动成立。

### 10.2 原 $(j+1)^{-2}$ 尾的明确阈值

现在取原
$$
a_j=(j+1)^{-2},\qquad j\ge m,\qquad x=m+1.
$$
令
$$
S_x=\sum_{n=x}^\infty n^{-4},\qquad
R_x=\sum_{n=x}^\infty n^{-8}.
$$
归一后
$$
\delta=\frac{x^{-4}}{S_x},\qquad
r_2=\frac{R_x}{S_x^2},\qquad
\frac{\delta^2}{r_2}=\frac{x^{-8}}{R_x}.
$$
直接积分比较给
$$
S_x\ge\frac1{3x^3},\qquad R_x\ge\frac1{7x^7},
$$
从而
$$
\delta\le\frac3x,\qquad \frac{\delta^2}{r_2}\le\frac7x.
\tag{10.7}
$$
函数 $\delta(10+2\delta)/(1-\delta)$ 在 $0\le\delta<1$ 上递增。
代入 (10.5)，对 $x>3$ 得
$$
C_2^2-2C_3
\succeq
r_2\frac{x^2-47x+24}{x(x-3)}I.
\tag{10.8}
$$
$x=47$ 时分子等于 $24$，其后严格递增。
所以
$$
\boxed{
m\ge46\quad\Longrightarrow\quad
\Gamma_{1,m}\Gamma_{2,m}^{-1}\Gamma_{1,m}
\prec\tfrac12 I_{K_{1,m}},
}
\tag{10.9}
$$
并且原真实第一下降满足
$$
\boxed{A_3A_3^*\prec2A_2^*A_2.}
\tag{10.10}
$$
(10.9)–(10.10) 作用于原完整连续尾的整个出生一空间，非有限位置截断。

还可保留一个显式正差。
因
$$
S_x\le x^{-4}+\frac1{3x^3}=\frac{x+3}{3x^4},
\qquad
r_2\ge\frac{9x}{7(x+3)^2},
$$
(10.8) 的正下界至少为
$$
\kappa_x=\frac{9(x^2-47x+24)}{7(x+3)^2(x-3)}.
$$
由 $0<C_2\preceq I$ 和 $C_2^{-1}$ 同余，
$$
\boxed{
\Gamma_{1,m}\Gamma_{2,m}^{-1}\Gamma_{1,m}
\preceq\left(\frac12-\frac{\kappa_x}{2}\right)I,
\qquad x=m+1\ge47.
}
\tag{10.11}
$$

### 10.3 常数二是这条原尾首边的渐近极限

当归一后的 $\delta\to0$，
$$
r_2\le\delta\to0,\quad e_2\to\tfrac12,\quad e_3\to\tfrac16,
\quad \|p\|^2\le\delta^2,\quad
\|w\|\le\delta+\delta^2.
$$
由 (10.2)，在各自的完整 primitive 空间上，均有统一范数估计
$$
\|C_2-I\|\to0,\qquad
\|C_3-\tfrac12 I\|\to0.
$$
故
$$
\left\|
\Gamma_1\Gamma_2^{-1}\Gamma_1-\tfrac12 I
\right\|\to0.
\tag{10.12}
$$
原连续尾满足 $\delta\le3/(m+1)\to0$，所以其出生一首边的最佳 $\Gamma$ 比较常数趋于 $1/2$，
对应真实第一下降的最佳常数趋于 $2$。
这只说明该固定出生、固定高度的渐近行为；
不能由此推断高出生源或其余相邻边的费用。

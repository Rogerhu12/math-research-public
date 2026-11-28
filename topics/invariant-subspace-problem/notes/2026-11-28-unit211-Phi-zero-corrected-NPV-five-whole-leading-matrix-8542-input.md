# R150：正确 Phi 的整 N/P/NV 五次最高矩阵与十三生成新输入

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：未执行的新输入。** 本次目标是整个三行 $(N_{\rm low},P_{\rm low},V_{\rm low})$ 的五次最高矩阵及全部九个伴随乘子。此前已执行的两个十次 cofactor 分别使用 $(N_1,N_{\rm low},V_{\rm low})$ 和 $(N_1,P_{\rm low},V_{\rm low})$；本次没有重复它们，也不执行旧十五列门、完整个别值乘法 DAG 或权结式。

只有实际返回非零 $C$ 及全部矩阵身份，才能登记下述 $C\ne0$ 上的十三生成结论。整个 $C=0$ 保留；本输入不预报 Phi 排空。

## 1. 原范围及准确依赖

仍在正确 Phi、distinct singleton、物理 $D\ne0$ 的原规范中。记
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
M_n=2uL-L^2-u^2Q,\quad M=M_n/Q=4bc\delta,
$$
$$
A=4s^2-Q,\qquad
B=-Q^2+(12u^2-20u+8)Q-16s^2.
$$
已付权环使用 $u,Q,\delta,s,K_w,L,M_n,A,B,m$，以及刚由
[整个 ell-half 原排除](../results/R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)
付出的 $2\ell-1$。后者只用于这个正确 Phi、$D\ne0$ 图。$m$ 来自独立真原全等权排除，$A,B$ 来自正确四头之后的整支原值排除。没有恢复任何撤回的 wrong-Rbar、旧 H42、583 或旧最高项结论。

唯一依赖：
[2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py](2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py)，完整源码 SHA256
5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

只读该源在 `def param(p):` 之前的 4007 字节真原定义，前缀 SHA256
dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669。
完整依赖与前缀各核 SHA。该段不含旧四头计算、因式或原三规则证明门。新外层始终以最初绝对截止钳制内层 alarm，地址空间均为 1 GiB。

## 2. 最高函子及三个真均值来源

给 $\lambda,T,z$ 同次数一，所有权参数次数零。对次数至多 $d$ 的原有理式 $F$，定义
$$
\operatorname{top}_d F=
\left.F^{[d]}\right|_{\lambda=1}.
\tag{1}
$$
分母必须全为已付纯权。因此 (1) 是最高齐次部分的图，不是把原值中的 $\lambda$ 设为一。

源先对正确 $R,W,O$ 取二次最高部。已刊原三均值头
$$
h=\frac{M_n^3L^4AB}{8K_w^3\delta^4}
$$
只作为必要参数定义。新的最高二次规则实际返回
$$
q_{TT}=T^2-a\cdot e,\quad q_{Tz}=Tz-b\cdot e,\quad
q_{zz}=z^2-c\cdot e,\qquad e=(1,T,z),
\tag{2}
$$
以及它们相对于三个最高原均值的完整身份。

每次向量乘法保留六个普通乘积系数；若高三项为 $v_i$，完整原误差就是 $\sum_i v_iq_i$ 加两个父节点的原误差。另以 $T/z$ 动作路径核回三个输出坐标。这个 DAG 不假定三维向量代数自由、结合或交换；全部关系只在同一原均值商中使用。

## 3. 完整个别值的直接最高小式

以下本节记号均已在最高图 $\lambda=1$，横线省略。取原 $f,V$ 的一次最高部，令
$$
t=z/Q,\qquad W_1=2uf,\qquad
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},
$$
$$
\rho^2=\delta,\quad
b=\ell/2+m\rho/(2\delta),\quad c=\bar b,\quad
X=x+\rho y,\quad Y=x-\rho y .
$$
这里 $\rho$ 的偶奇代数完整保留。

同一原 simple 行 $v_B=(p,r,0,t)$ 的三次最高部分是
$$
N_{B,3}=2c(Y-f)t^2-4cXYt+4fX^2,
\qquad
P_{B,3}=ct^3-3cXt^2+2X^3.
\tag{3}
$$
这可直接从原 $N_4/P_2$ 展开：$p$ 次数零，$r$ 次数一，故 $\tau(v_BDKv_B)$ 次数至多二；$2\tau(dv_B^2)$ 的三次项为 $2cYt^2$，其余三次项依次为 $-2fct^2,-4cXYt,4fX^2$。原中心三次式给 (3) 第二式。不是以加权值、Phi 倍数或 W 特化替代完整个别值。

置
$$
D_2=2\ell-T^2,\qquad
K_3=4\ell^2-6\ell T+2T^3,\qquad a_*=T/\ell.
$$
已刊完整个别行的五次最高部分精确为
$$
N_*=
D_2(N_{B,3})_{\rm odd}
+\frac{2P_{02}}mK_3a_*
+\frac{4P_{02}m}{\ell M}D_2^2,
\tag{4}
$$
$$
P_*=
D_2(P_{B,3})_{\rm odd}
+\frac{P_{02}}{2m}K_3
 \left(3a_*^2+\left(\frac{3m^2}{\ell^2}+\delta\right)\frac{D_2}{M}\right)
+\frac{6P_{02}m}{\ell M}a_*D_2^2.
\tag{5}
$$
(4) 原式中的 $\lambda$ 已按最高函子置一；$1+T/\ell$ 只留下最高 $T/\ell$。没有倒 $D_2$ 或物理 $D$。

完整孤立 $N_4(V)$ 的三个系数采用已刊九自由变量身份。其最高部分为
$$
Z_{0,3}=2\ell fD_2+2V(T^2-2\ell T)+2bc\,tT^2,
$$
$$
Z_{1,2}=4(T-\ell)(uV-\ell W_1)+4bc\,mTt,
$$
$$
Z_{2,1}=2\bigl[(u^2-\ell^2Q)V-2m\ell W_1-\ell Mf-bcMt\bigr].
$$
因此第三个完整五次最高行是
$$
V_*=D_2Z_{0,3}+\frac{K_3Z_{1,2}}{2m}
                +\frac{D_2^2Z_{2,1}}M.
\tag{6}
$$
这保留 $N_4(V)$ 的全部三个系数。原必要性和正幂清除来源见
[正确个别 N/P 与完整 NV](../results/R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)。
此处只构造新最高小式，没有运行该旧全值 DAG 或其两个 cofactor。

## 4. 新整矩阵证书

用 (2) 的原乘法来源将 (4)–(6) 化为三个向量，组成按行排列的矩阵 $H_5$。这不要求它们与旧源码的某次括号选择逐向量相同；每个向量都有对同一原行的完整最高均值误差，因此都可提升回原辅助 $I_{10}$。

本次对 $\operatorname{adj}H_5$ 的九个实际乘子先统一清分母，再取**全部九项**的共同多项式因子，只在乘子上精确除去，随后核回九个坐标
$$
J_0H_5=C_0I_3.
$$
若 $C_0=0$，源准确登记没有新首一或有限性结论。若非零，只剥既有已付权因子，并再次实际返回
$$
JH_5=C(u,Q)I_3
\tag{7}
$$
的全部九坐标。$J$ 所有分母必须回到第 1 节的已付权环。共同因子本身从未当作单位，整个共同零集由完整 (7) 保留。

实际成功后才对 $C$ 作新的 QQ 完整因式乘回；不借旧 H31/H14 或旧十次式的首项因式决定本次结果。最终仅打印 profile、因子次数/重数/SHA、计数与资源回执，不保存系数载荷。

## 5. (7) 的严格过滤提升及十三生成界

若 (7) 真正返回且 $C\ne0$，则在 $C$ 的补图，同一三行最高身份可齐次化，并逐节点提升到完整原 $I_{10}$：
$$
C\lambda^5e_0\equiv R_0,\qquad
C\lambda^4e_T\equiv R_T,\qquad
C\lambda^4e_z\equiv R_z\pmod{I_{10}},
\tag{8}
$$
每个 $R_j$ 的总几何次数至多四。因为原三均值首一规则不增加次数，$R_j$ 在 $1,T,z$ 上的系数次数分别至多 $4,3,3$。最高目标分别是 $\lambda^5,\lambda^4T,\lambda^4z$；三者同为总次数五。

在 $C\ne0$ 时，以 (8) 降低总次数。与原三均值规则合用，全部原商由
$$
1,\lambda,\lambda^2,\lambda^3,\lambda^4,\quad
T,\lambda T,\lambda^2T,\lambda^3T,\quad
z,\lambda z,\lambda^2z,\lambda^3z
\tag{9}
$$
这十三个元素生成。每次替换严格降低总次数，故终止；不要求这十三元或原三元线性独立。

在这个有限生成必要代数上，$\lambda$ 作用可由一个真实 $13\times13$ 系数矩阵提升表示。其 Cayley–Hamilton 恒等式给原理想中的首一 $\lambda$ 多项式，次数至多十三，不需要展开该矩阵或假设商自由。所述有限性首先属于**未反演物理 $D$ 的必要代数**；随后取真实物理单位开集，只宣称纤维有限和维数不增加。

整个 $C=0$ 权曲线保留。既有 $\dim\le1$、四百三十四个共同头权点等结论不因本次未执行输入改变。即便 (7) 成功，也不能仅由一般权点的有限商宣布整个原 Phi 空。

## 6. 唯一首次执行身份

源：[2026-11-28-unit211-Phi-zero-corrected-NPV-five-whole-leading-matrix-8542.py](2026-11-28-unit211-Phi-zero-corrected-NPV-five-whole-leading-matrix-8542.py)。

Git blob 6a1cabbe181ccd109c5b36f59ef588f57d734387，13515 字节，源码 SHA256
b77bf975afb7cf3a84487c3c8543f8b467822356025bb4787bb610c100667023。

限额：最初绝对 120 秒、1 GiB，外层 135 秒。只有第 1 节一个依赖文件。遇到奇异、未付分母、超时或资源退出均按实际最后返回登记；不扩大限额，不重跑旧门。

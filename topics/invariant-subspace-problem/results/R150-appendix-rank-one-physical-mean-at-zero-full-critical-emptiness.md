# R150 补篇：物理参数为零的非零秩一均值，完整临界系统必有零三阶张量

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 结论与原方程范围

这里的“零”是物理参数 $s=0$，均值向量是非零的 $y=v(0)=e_0$；并非把均值向量设为零。采用原六模基、原矩阵 $K$、原 Hankel 二阶和三阶矩，不作正交简化，不预设 $MKM=0$，也不预设中心化线性算子 $A_yM=0$。

**定理。** 固定 $y=e_0$，设原最高方程及全部十一条二阶系数方程、六条均值梯度方程成立。写
$$
H=M+\frac12yy^{\mathsf T},\qquad M_{ij}=m_{i+j}\quad(0\le i,j\le5).
$$
则
$$
m_2=m_3=\cdots=m_{10}=0,\qquad T_3=0.
$$
反过来，任意 $m_0,m_1\in\mathbb C$ 给出的
$$
M=m_0e_0e_0^{\mathsf T}
+m_1(e_0e_1^{\mathsf T}+e_1e_0^{\mathsf T})
$$
连同最高方程唯一确定的 $V$，都满足完整系统。因此归一化分支的临界点集合恰为上述切向平面。对任意非零振幅 $y=ae_0$，按 $M=a^2\widetilde M,\ V=a^3\widetilde V$ 缩放后同样成立。

这是本有限标量分支的完整排除：不存在非零 $T_3$ 的解。它不宣告普通 Hilbert 空间不变子空间问题完成。

## 2. 使用的是完整的十七条原方程

沿用
[R150 中心化完整临界归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)
及
[原均值梯度的物理 Hessian 接口](R150-appendix-rank-one-full-mean-gradient-as-a-physical-hessian-kernel.md)。
设 $p=Ky$，令
$$
\mathcal L_y(M)
=J_3^{-1}\!\left[p_y(z)J_2(M)(z)\right].
$$
最高方程唯一给出
$$
V=\frac32\mathcal L_y(M)+\frac12y^3,\qquad
T_3=6\bigl(\mathcal L_y(M)-yM\bigr).
$$
这里乘积和张量收缩遵守原文的对称化约定。余下方程是
$$
N(Kv(z),Kv(z))\equiv0,\qquad
N=4MKM+6\bigl(\mathcal L_y(M)\bigr)_p,
$$
以及
$$
\Gamma
=2\tau_2(M)y+8MKMp
-12\mathcal L_y(M):(KMK)=0,\qquad
\tau_2(M)=\operatorname{tr}((KM)^2).
$$
第一项取关于 $z$ 的全部十一项系数，第二项保留全部六个坐标。没有把第一条曲线上的多项式恒等式加强为 $N=0$ 的矩阵恒等式。

本篇的十七个整系数多项式 $f_1,\ldots,f_{17}$，按 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 排列，精确取自
[原零与无穷均值整数系统](../notes/2026-11-14-rank-one-zero-infinity-centered-systems.json)
的 zero.equations。该文件逐行保存非零整数比例：
$$
\det(J_3)\,(\text{原方程该行})
=(\text{该行 scale})\,f_i.
$$
故在 $\mathbb C$ 上二者零点完全相同。原整数系统的生成器也已在同目录保存。

令
$$
c=m_0,\qquad d=m_1,\qquad
z=(m_2,\ldots,m_{10}).
$$
由上述原整数行直接可见，每个 $f_i$ 的次数至多二，没有常数项，并且
$$
f_i(c,d,0)=0. \tag{2.1}
$$
完整证书脚本也逐项检查线性纯切向项、二次纯切向项均为零。

## 3. 将大秩问题的上界降为一个小整数核

记 $\mathcal P_{\le5}^{+}$ 为十一变量、总次数一至五的复多项式空间。其单项式维数为
$$
\binom{16}{5}-1=4367.
$$
令 $\mathcal R$ 是全部
$$
m^\alpha f_i,\qquad |\alpha|\le3,\quad 1\le i\le17
$$
的线性包，共有
$$
17\binom{14}{3}=6188
$$
个指定生成行。显然每个 $\mathcal R$ 中的多项式都属于原十七方程生成的理想。

按单项式包含的横向因子 $z_j$ 的个数分解空间。在总次数一至五内：

| 横向因子个数 | 单项式数 |
| --- | ---: |
| 零个，即纯 $c,d$ 项 | $2+3+4+5+6=20$ |
| 恰好一个 | $9(1+2+3+4+5)=135$ |
| 至少两个 | $4367-20-135=4212$ |

由 (2.1)，$\mathcal R$ 位于没有纯切向项的空间 $\mathcal U$ 中。设
$$
\pi:\mathcal U\longrightarrow\mathcal U_1
$$
保留恰好一个横向因子的项，杀去至少两个横向因子的项。于是
$$
\dim\ker\pi=4212.
$$

如果乘子 $m^\alpha$ 含有横向因子，则 $\pi(m^\alpha f_i)=0$。其余乘子恰为 $c^a d^b$，$a+b\le3$，共有十个。因此 $\pi\mathcal R$ 是下述 **$170\times135$ 整数矩阵 $P$** 的行空间：

* 行按 $i=1,\ldots,17$，再按总乘子次数 $a+b=0,1,2,3$，每层按 $a=0,\ldots,a+b$ 排列；
* 列按 $c^a d^b m_j$，其中 $a+b=0,\ldots,4$，每层按 $a=0,\ldots,a+b$、最后按 $j=2,\ldots,10$ 排列；
* 行内容是原 $c^a d^b f_i$ 的恰好一个横向因子的系数。

我们构造了七个有理数域上独立的整数向量 $q_1,\ldots,q_7$，满足
$$
Pq_\ell=0\quad(1\le\ell\le7). \tag{3.1}
$$
以零起算的自由列为
$$
8,\ 26,\ 130,\ 131,\ 132,\ 133,\ 134,
$$
相应单项式是
$$
m_{10},\quad c\,m_{10},\quad
c^4m_6,\ c^4m_7,\ c^4m_8,\ c^4m_9,\ c^4m_{10}.
$$
每个 $q_\ell$ 在这七个坐标中的唯一非零项位于第 $\ell$ 个自由列，因此七向量独立。

完整向量由所附确定性整数消元脚本重建，随后对每个向量逐行进行原整数乘法：共 $170\cdot7=1190$ 个等式，每个整数余项都是零。生成器只作整数乘法、整除与最大公因数运算；没有数值容差。作为小型明示项，$q_1$ 仅在零切向次数的九列非零，依次为
$$
(-127249961315,\ 30837820800,\ -66901017600,\
-168602050560,\ 95491328000,\ 1812807034880,\
9064035174400,\ 40676703594496,\ 180166156584960).
$$
其余六个向量按同一精确算法生成；全部七个向量的规范 JSON 的 SHA256 为：

~~~text
039af344dfc85b2d77ad597cdf0cdfdac4f387875b7250ce363466f8a1adf5a5
~~~

由 (3.1) 得到特征零上界
$$
\dim_{\mathbb Q}\operatorname{row}(P)\le128,
\qquad
\dim_{\mathbb Q}\mathcal R\le4212+128=4340. \tag{3.2}
$$

## 4. 模七给出匹配的秩下界

对同一 $6188\times4367$ 整数系数矩阵直接模七消元，得到
$$
\operatorname{rank}_{\mathbb F_7}=4340. \tag{4.1}
$$
这是整系数矩阵的秩下界证书：消元中的 4340 个非零枢轴给出一个模七非零的整数子式，该子式在 $\mathbb Q$ 上也非零。因此
$$
\dim_{\mathbb Q}\mathcal R\ge4340. \tag{4.2}
$$
这里只使用整数子式非零的提升，没有根据有限域点集判断复数点集。

所附模七程序枚举与第 3 节完全相同的行。单项式用
$$
m^\alpha\longmapsto\sum_{j=0}^{10}\alpha_j8^j
$$
编码；总次数至多五，因而无进位混淆，编码亦在 JavaScript 精确整数范围内。列按总次数从五递减到一，每层按递增变量指标的单项式枚举排列。程序以三个二进制位平面保存 $\mathbb F_7$ 系数，逐次作精确域加法和非零枢轴归一化。$2$ 与 $4$ 的乘法是位平面的循环置换，负号使用 $7-a$，相加时把最高进位按 $8\equiv1\pmod7$ 回卷并将编码 $7$ 化为零。没有浮点消元。

本次各总次数的枢轴数量回执为：

| 枢轴单项式总次数 | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 数量 | 3 | 62 | 282 | 996 | 2997 |

合计为 4340。这是指定列序下的消元回执。

## 5. 秩相等强迫整个横向平方空间进入原理想

合并 (3.2)、(4.2)，得到
$$
\dim_{\mathbb Q}\mathcal R=4340.
$$
另一方面，
$$
\dim\mathcal R
=\dim(\mathcal R\cap\ker\pi)+\dim(\pi\mathcal R)
\le4212+128.
$$
等号成立迫使
$$
\mathcal R\cap\ker\pi=\ker\pi.
$$
因此总次数至多五、至少含两个横向因子的**每个**多项式均属于 $\mathcal R$。特别地，
$$
m_j^2\in\mathcal R\subset(f_1,\ldots,f_{17})
\quad(2\le j\le10). \tag{5.1}
$$
任一复数解代入 (5.1)，即有全部 $m_j=0$，$2\le j\le10$。

最后，当 $M$ 位于所述切向平面时，$yM$ 是三阶 Hankel 张量且
$$
J_3(yM)=p_yJ_2(M).
$$
$J_3$ 可逆，故 $\mathcal L_y(M)=yM$，从而 $T_3=0$。同时原 $K$ 在 $\operatorname{span}(e_0,e_1)$ 上恒为零，且
$$
p=Ke_0=(0,0,0,0,5,-1)^{\mathsf T},
\qquad MKM=0,\quad Mp=0,\quad y^{\mathsf T}p=0.
$$
于是 $N=0$。对称张量收缩给出
$$
(yM):(KMK)
=\frac13\bigl(\tau_2(M)y+2MKMp\bigr)=0,
$$
故 $\Gamma=0$。这也证明了定理中的反向和临界点集合的准确描述。

对于 $y=ae_0$，令 $M=a^2\widetilde M$。上述 $N,\Gamma,T_3$ 分别缩放为 $a^4,a^5,a^3$ 倍；$a\ne0$ 时归一化保留全部原方程，完成一般非零振幅情形。

## 6. 完整重建资料与后续范围

以下脚本均为本证明的明确有限证书，不另设独立审计或测试关卡：

* [模七大矩阵生成与消元](../notes/2026-11-14-rank-one-exceptional-mean-macaulay-f7.js)；
* [纯整数右核生成器](../notes/2026-11-14-rank-one-exceptional-mean-integer-kernel.js)；
* [原方程投影及 1190 项整数核等式](../notes/2026-11-14-rank-one-exceptional-mean-normal-projection.js)；
* [统一完整重建入口](../notes/2026-11-14-rank-one-exceptional-mean-rank-certificate.js)；
* [本分支小回执](../notes/2026-11-14-rank-one-physical-mean-zero-rank-certificate-receipt.json)。

从仓库根目录运行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-exceptional-mean-rank-certificate.js zero
~~~
入口从已保存的原十七式读取整数系数，重建七个核向量并逐行精确代入，核对上述 SHA256，再重建大矩阵的模七秩并检查上下界相等。大核数据不分块传送；生成算法、原系数、参数和哈希足以逐项恢复。

本篇已经覆盖 $s=0$ 的 $A_yM\ne0$ 候选以及旧 $A_yM=0$ 分支，无须再给本分支附加 $MKM=0$、本质变量数或均值内外条件。下一未闭分支继续按 open.md 排序处理；不能把本篇的特定均值结论外推到其余物理参数。

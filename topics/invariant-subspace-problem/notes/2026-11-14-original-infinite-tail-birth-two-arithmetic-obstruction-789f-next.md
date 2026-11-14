# 原无限连续尾出生二的严格算术障碍：完整有理证书

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：已证明。** 在原连续尾 $b_j=j^{-2}$、$j\ge2$ 的整个无限模型中，出生二首边的辅助 Turán 算术比较不能保持出生一的系数 $2$；下面一个有理 primitive 源甚至要求系数严格大于 $289/100$。这是原无限尾的结论，证明不把有限截断特征值外推为无限结果。

本稿反驳的是辅助算术式，不是原加强 S1。实际 $C_1\Gamma_0C_1=C_1^2$ 的非交换目标、真实桥以及 graph 预算均未被此证书否定。

重建文件：[纯有理脚本](2026-11-14-original-infinite-tail-birth-two-arithmetic-obstruction-789f-next.py)、[小回执](2026-11-14-original-infinite-tail-birth-two-arithmetic-obstruction-789f-next.json)。脚本只用 Python 标准库、整数与 `Fraction`，没有浮点数、外部库、随机采样或数值正定判据。

## 1. 真实无限源与所排除的不等式

取
$$
b_j=j^{-2},\quad z_j=j^{-4}\quad(j\ge2),\qquad
d=\sum_{j\ge2}b_jE_j,
$$
$$
K_2=\ker d\cap\mathcal H_2,\qquad
\Gamma_n=\left((d^n/n!)^\dagger|_{K_2}\right)^*
\left((d^n/n!)^\dagger|_{K_2}\right),\qquad C_n=\Gamma_n^{-1},
$$
且 $C_0=I$。完整 MP 和无限固定层的合法性沿用 R279、R296；以下估计实际只使用 R296 的完整残差变分式。

写 $e_t=e_t(z_{j\ge2})$。对 $f\in K_2$，置
$$
\Phi_f(I)=\sum_{\{i,j\}\subset I}\frac{f_{ij}}{b_ib_j}.
$$
R296 准确给出
$$
\langle C_n f,f\rangle
=\inf_{q\in\mathcal P_{\le1}}
\sum_{|I|=n+2}z_I|\Phi_f(I)-q(I)|^2.
\tag{1.1}
$$
常数包含在线性特征中，因为在第 $n+2$ 切片上 $\sum_i x_i=n+2$；无限常数系数对应物理行 $b\in\ell^2$，是合法 nuisance。

我们证明存在下面明确给出的有理 $f\in K_2$，使
$$
\boxed{e_4\|f\|^2+e_2\langle C_2f,f\rangle
>\frac{289}{100}\,e_3\langle C_1f,f\rangle.}
\tag{1.2}
$$
因此连较弱的辅助式
$$
e_4I+e_2C_2\preceq2e_3C_1
\tag{1.3}
$$
也已失败。真正算术缺陷还要在左侧加入非负的
$e_2\delta_2L_3^{-1}\delta_2^*$，故它的系数 $2$ 同样失败。这里不需要估计、替换或删除真实桥来主张原 S1 的反例。

## 2. 一个完全有限支撑的有理 primitive 源

令 $B=\{2,3,4,5,6,7,8,9\}$。以下对称矩阵 $u$ 的对角为零；表中给出上三角，其余由对称性确定：

| $i\backslash j$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 73 | 233 | 431 | 632 | 1101 | -1439 | -1031 |
| 3 |  | -341 | -572 | -796 | -1361 | 1736 | 1261 |
| 4 |  |  | -825 | -1055 | -1748 | 2144 | 1592 |
| 5 |  |  |  | -1229 | -2023 | 2369 | 1849 |
| 6 |  |  |  |  | -2520 | 2629 | 2339 |
| 7 |  |  |  |  |  | 2561 | 3990 |
| 8 |  |  |  |  |  |  | -10000 |

每一行的和都严格为零。定义
$$
f_{ij}=u_{ij}i^2j^2\quad(i,j\in B),\qquad
f_{ij}=0\quad\text{其余位置}.
\tag{2.1}
$$
则对 $i\in B$，
$$
(df)_i=\sum_{j\ne i}j^{-2}f_{ij}
=i^2\sum_{j\ne i}u_{ij}=0;
$$
在 $i\notin B$ 上也为零，所以 $f\in K_2$ 是原无限源。其准确范数为
$$
\boxed{N_f:=\|f\|^2=3155425218697472.}
\tag{2.2}
$$
最高多项式系数也是整数：
$$
a_{ij}:=\frac{f_{ij}}{b_ib_j}=u_{ij}i^4j^4.
\tag{2.3}
$$
不要求这个源单位归一；除以任意共同非零常数不改变 (1.2)。

## 3. $C_1$ 的合法无限尾上界

取实际齐次线性 trial
$$
q^{\rm tr}(I)=\sum_{i\in I\cap B}\theta_i+\theta_T|I\setminus B|,
\tag{3.1}
$$
其中按 $B$ 顺序
$$
(\theta_2,\ldots,\theta_9)=
(-6226873,3524959,34809,-6327741,-22311254,
-74665443,173824267,194042655),
$$
$$
\theta_T=2546340.
\tag{3.2}
$$
尾部系数在每个 $j\ge10$ 相同；相应物理向量为 $\theta_T(b_j)_{j\ge10}\in\ell^2$。因此 (3.1) 是原无限 nuisance 的一个合法元素，不能把它误称为截断模型的拟合。

记 $T_l=e_l(z_{j\ge10})$。将三元集按其与 $B$ 的交集 $J$ 分组，得到准确 trial 费用
$$
U_1=\sum_{h=0}^3\ \sum_{J\subset B,\ |J|=h}
z_JT_{3-h}
\left|\Phi_f(J)-\sum_{i\in J}\theta_i-(3-h)\theta_T\right|^2.
\tag{3.3}
$$
所以 $\langle C_1f,f\rangle\le U_1$。这个表达的所有 $T_l$ 系数非负，可以直接代入真正尾初等和的上界。

第 5 节的有理包围给
$$
\boxed{\langle C_1f,f\rangle\le U_1
\le256710514081572=:U_C.}
\tag{3.4}
$$
这里既没有提前压缩完整逆，也没有假设 trial 等于真正最优拟合。

## 4. $C_2$ 的完整有限回归下界

把 (1.1) 在第 4 切片的非负和限制到 $I\subset B$。任意合法无限线性 nuisance 在这些集合上的限制是任意八个线性系数；因此
$$
\boxed{\langle C_2f,f\rangle\ge
\min_{\alpha\in\mathbb R^8}
\sum_{I\subset B,\ |I|=4}z_I
\left|\Phi_f(I)-\sum_{i\in I}\alpha_i\right|^2=:L_2.}
\tag{4.1}
$$
这一方向由非负求和与完整 nuisance 限制直接证明。没有假设有限 MP 与无限 MP 之间存在未证的逆序关系。

令 $x_I\in\mathbb R^8$ 为 $I$ 的示性向量，并置
$$
G=\sum_{|I|=4,I\subset B}z_Ix_Ix_I^*,\qquad
r=\sum_{|I|=4,I\subset B}z_Ix_I\Phi_f(I),\qquad
v=\sum_{|I|=4,I\subset B}z_I|\Phi_f(I)|^2.
\tag{4.2}
$$
这是全部 70 个四元集、全部八个线性特征的完整回归。常数已在这八列中，不是遗漏的第九列。若 $\sum_{i\in I}\alpha_i=0$ 对所有四元集成立，通过只交换一个指标得所有 $\alpha_i$ 相等，再由四元和得其全为零；所以 $G>0$。

其条目还可直接写为
$$
G_{ii}=z_i e_3(z_{B\setminus\{i\}}),\qquad
G_{ij}=z_iz_j e_2(z_{B\setminus\{i,j\}})\quad(i\ne j).
$$
所有量均为所列整数与 $i^{-4}$ 的有理式。完整消元给
$$
L_2=v-r^*G^{-1}r.
\tag{4.3}
$$
重建器执行八步有理 $LDL^*$，严格检查每个主元为正、$G\alpha=r$ 逐项为零，并检查 (4.3) 等于 70 项的实际残差平方和。它得到
$$
\boxed{\langle C_2f,f\rangle\ge L_2
>3916693862057=:L_C.}
\tag{4.4}
$$
这些检查是所列有限有理证书的计算内容；不是额外的独立审核门槛。

## 5. 原无限尾的有理包围

无需使用 $\pi$ 的数值或猜测截断误差。设 $P=10^{40}$。对有限尾 $10\le j\le200$ 的 $e_0,\ldots,e_4$，初始化
$L_0=U_0=P$、其余为零，并按 $j=10,\ldots,200$ 及降序 $h=4,3,2,1$ 执行
$$
L_h\leftarrow L_h+\left\lfloor\frac{L_{h-1}}{j^4}\right\rfloor,
\qquad
U_h\leftarrow U_h+\left\lceil\frac{U_{h-1}}{j^4}\right\rceil.
\tag{5.1}
$$
正递推立即保证 $L_h/P\le e_h(z_{10\le j\le200})\le U_h/P$。另一方面单调积分比较给
$$
\sum_{j>200}j^{-4}\le\int_{200}^{\infty}t^{-4}\,dt
=\frac1{3\cdot200^3}=:R.
$$
任意非负行都满足 $e_a\le(\sum z)^a/a!$，所以
$$
\boxed{\frac{L_h}{P}\le T_h
\le\sum_{a=0}^h\frac{U_{h-a}}P\frac{R^a}{a!}.}
\tag{5.2}
$$
脚本只把右端再次向上舍入到同一个有理格点。再以准确有限 $e_j(z_B)$ 作正卷积，得到全行 $e_t$ 的有理界。

为使手工重建的最后一步很短，回执进一步放宽到共同分母 $Q=10^{20}$：

| 实际量 | 所用有理界 |
|---|---:|
| $e_2$ | $e_2\ge134987590086355098/Q$ |
| $e_3$ | $e_3\le718394563305357/Q$ |
| $e_4$ | $e_4\ge1596177316433/Q$ |

对 (3.3) 使用 (5.2) 的上界并向上取整得到 (3.4)。所有余尾、舍入与最终乘法的方向均与其使用目的相容。

## 6. 最后的整数证书

令
$$
A=1596177316433\,N_f+134987590086355098\,L_C,
$$
$$
B=718394563305357\,U_C.
$$
第 3—5 节给
$$
e_4\|f\|^2+e_2\langle C_2f,f\rangle\ge A/Q,
\qquad
e_3\langle C_1f,f\rangle\le B/Q.
$$
现在只剩两个准确整数运算：
$$
\boxed{A-2B=164902808383829666433686711554>0,}
$$
$$
\boxed{100A-289B=76950886685275842380281428244>0.}
\tag{6.1}
$$
这同时证明 (1.3) 严格失败及更强的 (1.2)。原辅助缺陷满足
$$
\langle\mathcal A_{2,1}f,f\rangle
\le2e_3\langle C_1f,f\rangle-e_4\|f\|^2-e_2\langle C_2f,f\rangle<0,
$$
因为真实桥费用非负。

## 7. 对后续同源比较的准确影响

相位支付后的出生二条件 Poincaré 式中，系数为一的正通道预算不能在原无限尾上无条件覆盖剩余均值方差；(6.1) 给出了同一实际源的严格反证。因此后续必须允许明确损失，或回到真正 $C_1^2$ 的源度量，而不能继续尝试证明错误的常数 $2$ 算术步。

证书没有给原加强 S1 的负向量：它只比较 $e_4I+e_2C_2$ 与 $e_3C_1$。更没有涉及完整 graph $T^*T$ 的 Schur 逆。最初的有限原权诊断只用于选取上面的整数源；最终证明完全由 (2.1)、合法无限 trial、完整八列有限回归和有理尾界组成。

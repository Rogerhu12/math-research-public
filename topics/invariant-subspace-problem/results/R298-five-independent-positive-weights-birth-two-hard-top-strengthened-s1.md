# 五位全部独立正权：整个出生二硬端加强首边的严格统一界

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：以下完整物理源定理已证明。** 它首次处理五位、五个独立正权的整个出生二硬端加强 S1；没有把此前 R292 的分组普通相邻序扩大解释。证明保留五维上源、四维低源、完整第一 MP 逆与真正顶层压缩逆，最后以一个有限整数多项式证书控制真实费用的迹。

## 1. 定理与实际源

在五位 Boolean Hilbert 空间的标准正交占据基中，任取
$$
b_i>0\quad(1\le i\le5),\qquad
 d=\sum_{i=1}^5b_iE_i,\qquad
 U=K_2(b),\quad V=K_1(b).
$$
这里
$$
\dim U=\binom52-\binom51=5,
\qquad \dim V=4.
$$
上源 $U$ 的最高合法高度是一，低源 $V$ 的最高合法高度是三。记
$$
G_1=\Gamma_{1,2},\quad C_1=G_1^{-1},
\qquad L_j=\Gamma_{j,1}\quad(j=1,2,3),
$$
$$
B=\left.\sum_i b_i^3E_i\right|_U,
\qquad
\Delta=\tfrac12(C_1B^*L_3-B^*L_2).
$$
没有定义非法的上源 $G_2$；硬端仅在精度端置 $C_2=0$。全部 $\Gamma_j$ 都是完整层 $d^j/j!$ 的 MP Gram，先取完整逆后压到所列 primitive 源。

**定理。** 对全部五个独立正权，有
$$
\boxed{
0\preceq G_1\Delta L_3^{-1}\Delta^*G_1
\preceq\frac{743}{782}I_U<I_U.
}
\tag{1.1}
$$
因此整个五维物理 $U$ 上的加强首边严格成立，而且
$$
\boxed{
C_1^2-\Delta L_3^{-1}\Delta^*
\succeq\frac{39}{782}C_1^2\succ0.
}
\tag{1.2}
$$
常数与五个权的大小、相对比值均无关。本文没有声称 $743/782$ 最优，也没有由此推出更大位数或原 graph 费用。

## 2. 把整个上源费用写成低源的真实迹

令
$$
e=\sum_i b_i^{-1}E_i^*,
\qquad A=e^*|_U:U\to V.
$$
[奇数硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)给
$$
\Delta^*G_1=-L_1A,
\quad
\mathcal K:=G_1\Delta L_3^{-1}\Delta^*G_1
=A^*L_1L_3^{-1}L_1A.
\tag{2.1}
$$
在低源所在的第一层，$[d,e]=3I$，所以 $dev=3v$ 对 $v\in V$ 成立。由于 $\mathcal J_{1,1}$ 是完整最小逆，$e|_V$ 在
$\mathcal H_2=U\oplus\operatorname{Ran}d^*$ 中的实际正交分解是
$$
e|_V=3\mathcal J_{1,1}+A^*.
$$
从而
$$
AA^*=P_Ve^*e|_V-9L_1.
\tag{2.2}
$$
现在只用真实有限维迹的循环性，不估计任何单项，得到
$$
\boxed{
\operatorname{Tr}_U\mathcal K
=\operatorname{Tr}_V\!\left[
L_3^{-1}L_1(P_Ve^*e|_V)L_1
-9L_3^{-1}L_1^3\right].
}
\tag{2.3}
$$
第二个负项必须保留；它正是由完整 MP 正交分解产生的抵消。因为 $\mathcal K\succeq0$，有
$$
\|\mathcal K\|\le\operatorname{Tr}_U\mathcal K.
\tag{2.4}
$$
因此只需对 (2.3) 的真实迹给统一上界。

## 3. 五维坐标只作相似，不改变物理伴随

置
$$
z_i=b_i^2,\qquad S=\sum_i z_i,\qquad Z=\prod_i z_i,
\qquad e_j=e_j(z_1,\ldots,z_5).
$$
使用可逆坐标映射
$$
x\longmapsto\operatorname{diag}(b_i)x\in\mathcal H_1.
$$
这些坐标的物理内积是 $x^*\operatorname{diag}(z_i)y$，低源条件是 $\sum_i z_ix_i=0$。下列矩阵通常不在普通欧氏内积下自伴；本文只计算算子乘积与相似不变的迹，未把普通转置替换为物理伴随。

定义
$$
P_{ij}=S\delta_{ij}-z_j,
\qquad \Pi=P/S.
\tag{3.1}
$$
$\Pi$ 是上述物理内积中的正交投影到 $V$ 坐标。第一阶完整物理 $dd^*|_{\mathcal H_1}$ 的算子坐标为
$$
F_{ij}=(S-2z_i)\delta_{ij}+z_j.
\tag{3.2}
$$
置 $d_i=S-2z_i$。其完整行列式为
$$
\det F=\prod_i d_i+\sum_i z_i\prod_{j\ne i}d_j
=4\delta,
$$
$$
\boxed{\delta=S^2e_3-4Se_4+12Z.}
\tag{3.3}
$$
完整伴随矩阵 $Q=\operatorname{adj}F$ 可逐项重建为
$$
Q_{ij}=-z_j\prod_{k\notin\{i,j\}}d_k\quad(i\ne j),
$$
$$
Q_{ii}=\prod_{k\ne i}d_k+
\sum_{k\ne i}z_k\prod_{\ell\notin\{i,k\}}d_\ell.
\tag{3.4}
$$
记
$$
\mathsf L=PQP,
\qquad \ell=4S^2\delta.
\tag{3.5}
$$
则完整逆后压缩的真实 $L_1$ 在五维空间延零后的坐标，准确为
$$
\boxed{\widetilde L_1=\mathsf L/\ell.}
\tag{3.6}
$$
这是 $\Pi F^{-1}\Pi$，不是 $(\Pi F\Pi|_V)^{-1}$。

## 4. 顶度量的压缩逆与对偶升降的完整矩阵

[R239 全出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)在低源顶高度三给
$$
L_3=Z^{-1}P_V\operatorname{diag}(z_i^2)|_V.
\tag{4.1}
$$
其逆在五维坐标中延零为 $\widetilde L_3^{-1}=\mathsf K/e_4$，其中
$$
\mathsf K_{ii}=\frac Z{z_i}\,e_3(z_{[5]\setminus\{i\}}),
\qquad
\mathsf K_{ij}=-\frac{Z^2}{z_i^2z_j}\quad(i\ne j).
\tag{4.2}
$$
各项实际上都是整数多项式。该式来自对角压缩逆的准确秩一 Schur：在原物理坐标中，
$$
L_3^{-1}=Z\left[
D^{-1}-\frac{D^{-1}bb^*D^{-1}}{b^*D^{-1}b}
\right],\qquad D=\operatorname{diag}(z_i^2),
\tag{4.3}
$$
右侧限制到 $V=b^\perp$，并在 $\operatorname{span}b$ 上延零。$b^*D^{-1}b=\sum_i z_i^{-1}=e_4/Z$，故 (4.2) 确实保留了压缩逆。

特别有完全多项式恒等式
$$
\mathsf K\mathbf1=0,\qquad z^*\mathsf K=0,
\qquad
P\operatorname{diag}(z_i^2)\mathsf K=Ze_4P.
\tag{4.4}
$$
这直接核对了 (4.2) 在四维低源中的逆性质。

完整 $e^*e$ 在同一坐标的矩阵是 $\mathsf T/Z$，其中
$$
\mathsf T_{ij}=\left(e_4-\frac{2Z}{z_i}\right)\delta_{ij}
+\frac Z{z_i}.
\tag{4.5}
$$
两侧 $\widetilde L_1$ 已投到 $V$，故在 (2.3) 中可直接使用完整 $\mathsf T/Z$，无须把压缩写进其内部。

## 5. 真实迹的精确整数多项式

定义
$$
\mathcal N_{
m raw}
=\ell\,\operatorname{Tr}(\mathsf K\mathsf L\mathsf T\mathsf L)
-9Z\,\operatorname{Tr}(\mathsf K\mathsf L^3),
$$
$$
\mathcal D_{
m raw}=Ze_4\ell^3.
\tag{5.1}
$$
由 (2.3)、(3.6)、(4.2)、(4.5)，
$$
\operatorname{Tr}_U\mathcal K
=\mathcal N_{
m raw}/\mathcal D_{
m raw}.
$$
完整整数展开给准确整除
$$
\boxed{
\mathcal N_{
m raw}=64ZS^6N,\qquad
\mathcal D_{
m raw}=64ZS^6D,\qquad D=e_4\delta^3.
}
\tag{5.2}
$$
因此
$$
\boxed{\operatorname{Tr}_U\mathcal K=N/D.}
\tag{5.3}
$$
这里 $N,D$ 都是次数十九的对称整数多项式。$N$ 有负系数；证明没有删除它们。

为看清分母严格正，令 $m_\lambda$ 表示对五个变量的**不同**指数排列各取一次的单项对称多项式。由 (3.3)，
$$
\boxed{
\delta=m_{(3,1,1,0,0)}
+2m_{(2,2,1,0,0)}
+3m_{(2,1,1,1,0)}
+12m_{(1,1,1,1,1)}.
}
\tag{5.4}
$$
故全部正权上 $\delta>0$、$D=e_4\delta^3>0$。这个正性没有依赖数值特征值。

## 6. 完整正系数证书与严格加强界

[精确生成器](../notes/2026-11-14-five-bit-hard-top-trace-certificate-789f.py)从 (3.1)–(5.1) 直接重建所有矩阵，逐项验证
$FQ=(4\delta)I$、(4.4)、(5.2)，并检查每一个系数。其[完整小回执及对称轨道表](../notes/2026-11-14-five-bit-hard-top-trace-certificate-789f.json)保存全部 79 个对称单项轨道；每行给指数分拆、不同排列数及 $N,D,743D-782N$ 的三个整数系数。该表可恢复整个多项式，而无需保存展开的大矩阵。

| 多项式 | 次数 | 非零单项数 | 负系数数 |
|---|---:|---:|---:|
| $\delta$ | 5 | 81 | 0 |
| $N$ | 19 | 4360 | 305 |
| $D$ | 19 | 4480 | 0 |
| $743D-782N$ | 19 | 4460 | 0 |

完整系数恒等证书给
$$
\boxed{743D-782N\text{ 的全部系数非负。}}
\tag{6.1}
$$
而且该多项式非零，所以在五个变量全正时严格为正。最大正系数比为
$$
\max_{[z^\alpha]N>0}
\frac{[z^\alpha]N}{[z^\alpha]D}
=\frac{743}{782};
$$
在指数排列 $(5,5,5,4,0)$ 上，分子系数为 $2229$、分母系数为 $2346$。分子中 305 个负系数在 (6.1) 中产生正贡献，均按原符号保留。没有从某一子支持或数值抽样推断全多项式。

由 (5.3)、分母正性和 (6.1)，
$$
0\le\operatorname{Tr}_U\mathcal K<\frac{743}{782}<1.
$$
再用 (2.4)，得到 (1.1)，并以同一个 $C_1$ 作左右合同得到 (1.2)。这完成定理。

回执最终状态为 `all_passed`。可用

```bash
python topics/invariant-subspace-problem/notes/2026-11-14-five-bit-hard-top-trace-certificate-789f.py
```

从整数输入重新生成完整证书；依赖为仓库既定的 `python-flint 0.9.0`。此次完整生成约 0.45 秒。证书的数学含义是 (5.2) 与 (6.1) 的全部有限整数恒等和符号，不是进程退出码或一次浮点谱计算。

## 7. 结论的准确范围

本定理关闭五位、全部五个独立正权、整个出生二硬端的加强 S1。它包含任意高度层次的五位权，也包含此前用于暴露未投影提升发散的两强弱位族，但没有局限于那个族的 $S_3$ 不变线。

普通首边在该上源上没有第二合法高度；这里证明的是保留真正低出生桥创新的加强硬端式。更大奇数位数的统一常数、全部出生的普适加强常数和原 graph 源费用仍未由本稿支付。后继一般归纳必须保留 (2.3) 中的混合项与负项；对未投影提升或单个矩阵因子的粗范数界不能替代这个证书。

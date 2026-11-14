# R119：正配平静态成本的完整线性乘子判据

日期：2026-11-14。**已证明。** 纸面有限维凸分析，没有新的计算。使用 [R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R114](R114-constrained-static-costs-and-real-zero-matrix-words.md) 及 [R117](R117-static-weight-one-reduction-and-reciprocal-costs.md)。

本稿给一个必要正性门，而不宣称第四成本有正性。静态配平门本身有准确的必要充分条件；把它用于完整真实路径时，只有必要性。

## 1. 静态集合与域

仍以 $S=(h,k,\omega)$、$h>0$ 表示常态，记

$$
D(S)=\tau(k)m_0(S)\in E_8,\qquad
c_\Lambda(S)=\tau(k)\Lambda([\ell_0(S)])\in\mathbb R,
$$

其中 $\tau(k)>0$、$m_0,\ell_0$ 均取 R114 的同一右锚完整相位定义。$\Lambda$ 先定义在包含局部密度与 $\mathcal R_8$ 的有限真实函数商上。

允许的状态集合记为 $\mathcal S$。以下纯静态定理只要求

$$
\operatorname{cone}\{D(S):S\in\mathcal S\}=E_8.
\tag{1}
$$

例如 R114 的四个 $(h,d)=(1,0),(1,1),(1,-1),(1,2)$、每组 $k=0,\pm1,\pm2$ 的二十个状态已经有 (1)。可以取包含它们的全部常态集合。

实际应用还要求 R114 的有限状态、正规块及连接族处于所讨论的真实控制范围内。公共物理区间按有限紧控制族先选，随后只增加圈数；本稿不保证任意预先规定的窄物理带、统一总长或控制盒仍含这个正锥。若另施这些限制，应重新检查 (1) 和真实连接前提，不能沿用全部常态的结论。

## 2. 静态正性与八维乘子等价

以下两条等价：

1. 对每个有限正配平表，

$$
t_j\ge0,\qquad \sum_jt_jD(S_j)=0,
$$

都有

$$
\sum_jt_jc_\Lambda(S_j)\ge0.
\tag{2}
$$

2. 存在固定线性泛函 $\mu\in E_8^*$，使对所有 $S\in\mathcal S$，

$$
\boxed{
\Lambda([\ell_0(S)])-\mu(m_0(S))\ge0.
}
\tag{3}
$$

这里八个乘子不依赖状态或路径。它们是矩约束的对偶变量，不是真实控制方向，也不授予成本取负。

### 证明：先构造有限的次线性函数

形成有限正锥

$$
\mathcal K=
\left\{
\left(\sum_jt_jD(S_j),\sum_jt_jc_\Lambda(S_j)\right):
t_j\ge0,\ J<\infty
\right\}.
$$

不假设它闭，也不假设任何 inf 能取到。由 (1)，对每个 $M\in E_8$ 至少有一个有限成本 $z$ 使 $(M,z)\in\mathcal K$。定义

$$
f(M)=\inf\{z:(M,z)\in\mathcal K\}.
\tag{4}
$$

先固定一个 $(-M,z_-)\in\mathcal K$。任意 $(M,z)\in\mathcal K$ 与它相加后是零矩表，故 (2) 给

$$
z+z_-\ge0.
$$

因此 $f(M)\ge-z_->-\infty$。另一方面正锥满射给一个有限上界，故

$$
-\infty<f(M)<+\infty\quad\forall M.
\tag{5}
$$

空表给 $f(0)\le0$，(2) 给 $f(0)\ge0$，所以 $f(0)=0$。

正锥缩放直接给 $f(aM)=af(M)$，$a>0$。任取近于两个 inf 的有限表再相加，然后令误差趋零，得到

$$
f(M_1+M_2)\le f(M_1)+f(M_2).
$$

这一步只使用逼近 inf，不把 inf 值当成实际表。于是 $f$ 是处处有限的次线性函数。

为明确其连续性，取 $E_8$ 的任意基 $e_i$，令

$$
C=\max_i\{f(e_i),f(-e_i)\}.
$$

因 $f(e_i)+f(-e_i)\ge0$，$C\ge0$。次可加性给

$$
|f(M)|\le C\sum_i|M_i|,\qquad
|f(M)-f(N)|\le C\sum_i|M_i-N_i|.
$$

故没有在这里偷用闭锥或紧性。

### 证明：支撑与反向

对次线性 $f$，有限维 Hahn–Banach 支撑给一个线性 $\mu$，满足

$$
\mu(M)\le f(M)\quad\forall M.
$$

每个单状态点属于 $\mathcal K$，所以

$$
c_\Lambda(S)\ge f(D(S))\ge\mu(D(S)).
$$

消去正因子 $\tau(k)$ 即为 (3)。

反向，把 (3) 乘各正权和正周期并相加；总矩阵为零使所有乘子项准确消去，得到 (2)。证毕。

## 3. 完整真实成本的必要门

设一个连续线性泛函 $\lambda$ 对所讨论范围内每个真实 $M=T=0$ 成本都非负。其线性延拓到这些成本的有限维跨度 $\mathcal U_4$ 仍按同一函数身份定义。

R102 已证明真实成本闭凸锥的 lineality 包含 $\mathcal R_8$。因此

$$
\lambda|_{\mathcal R_8}=0.
\tag{6}
$$

这里不是把实际有限成本半群与闭凸锥认作同一个集合：从对实际成本非负，到对其正锥及闭包非负，只用了线性与连续性。

一个单独的局部静态值 $[\ell_0(S)]$ 未必已经属于 $\mathcal U_4/\mathcal R_8$。所以先在有限维 ambient 函数商中选 $\lambda$ 的任意线性延拓 $\widetilde\lambda$；没有未定义地对域外对象直接评价 $\lambda$。

对任意 R114 的正配平表 $q$，其正规化构造给真实 $M=T=0$ 成本满足

$$
[V_N]/(2N)\longrightarrow q+\varepsilon q_{\rm reg}.
$$

左侧的 $\lambda$ 值非负。先令 $N\to\infty$，再令 $\varepsilon\to0$，得到

$$
\widetilde\lambda(q)\ge0.
$$

这仅把连续非负性传到有限维极限，没有声称极限就是一个实际路径的成本。第 2 节遂给某个 $\mu$：

$$
\boxed{
\widetilde\lambda([\ell_0(S)])\ge\mu(m_0(S))
\quad\text{对所有允许常态 }S.
}
\tag{7}
$$

因此，任何完整真实成本正性主张都必须先通过 (7)。

### 为什么延拓选择不会改变必要门

若两个 ambient 延拓之差为 $\psi$，则 $\psi$ 在 $\mathcal U_4/\mathcal R_8$ 上为零，因而在 R114 的全部静态正配平成本上为零。R114 的零配平判据给一个固定 $\nu\in E_8^*$，满足

$$
\psi([\ell_0(S)])=\nu(m_0(S)).
$$

把 $\mu$ 换成 $\mu+\nu$ 即消掉延拓差。因此必要门是内在的，虽然某个具体被积标量及其乘子分别依赖延拓。

## 4. 这不是完整路径正性的充分条件

(3) 只控制正配平常态的几何导数权零成本。真实连接还包含 R112 的导数权 $2,4$，并有 frame、水平微分约束与有限基准成本。即使全部静态状态都满足 (3)，也不能据此断言任意真实路径的 $\lambda(V)$ 非负。

同样，R117 的两个互反圈给的是**权一投影**的相反 leading 成本。直接推出 $\lambda(G)=0$，需要 $\lambda=\lambda_1\Pi_1$ 明确杀掉其他 profile 权。一般混合权正泛函可能仍看见未支付的其他成本；不能在没有最高权或正缩放极限证明时，把它们删掉。

若泛函确实只取权一，则 R117 的正、负互反对与 R114 极限使它在 $G$ 方向上必须为零。这是一个有条件的简化，不是对所有混合权泛函的结论。

## 5. 有限代数接口与余下工作

在 R114 的八坐标中写

$$
\mu(m_0(S))=\sum_{j=1}^8\mu_j\,m_{0,j}(S).
$$

代入其完整式 (1)，右侧是已知的八个 Laurent 几何函数。左侧由已保存的有限局部 profile 模板与 $\widetilde\lambda$ 的有限系数给出，可能含 $\log h$。所以必要门是一个参数维数有限、状态变量连续的 Laurent/log 不等式问题；不是有限采样一遍即可认证的有限组不等式。

乘以足够高的正幂 $h^n$ 可以清除负幂，但不能擅自删除 $\log h$ 项，不能把代表余项当真实函数独立。准确分离或正性仍须支付真实函数关系、允许状态域与全状态不等式。

本稿没有找到非零正性泛函，没有证明完整成本锥为全空间或存在零成本环；完整第四/ruling、更高阶、闭曲面嵌入与厚度门仍未完成。

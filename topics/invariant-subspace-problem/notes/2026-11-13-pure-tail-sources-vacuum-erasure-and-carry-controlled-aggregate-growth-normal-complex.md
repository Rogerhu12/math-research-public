# 纯远尾变化源的真空擦除与实际 carry 下的聚合发散

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：完整的真实见证必要条件。** 本文允许重构源完全逃向远物理尾，甚至弱趋零且没有范数收敛子列。只要这些源确为“头部真空张量任意远尾向量”，就有一个明确的尾擦除操作，将聚合配对送回同一个固定真空。这个操作不属于 $A'$；它仅作为配对中的有界辅助矩阵使用，并逐项支付与实际测试的交换误差。

结论补充 [R244 聚合转置预算主文](../results/R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)
的强收敛源情形。不构造有界聚合预算，也不把一般变化源自动视为纯远尾源。

## 1. 真见证与允许变化的源表

固定原实际
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
\mathfrak C=A',\qquad
B(u,v)=\langle u,Cv\rangle.
$$
内积对第一个变量线性，$C$ 为原反射共轭。
$\mathfrak C$ 交换且全部 $C$ 对称。
真空 $\Omega=1$ 对 $A$ 循环，$C\Omega=\Omega$。

固定非零正有限秩真见证
$$
\phi(F)=\sum_{i=1}^r\langle Ff_i,f_i\rangle,\qquad
\tau=\phi(I)=\sum_i\|f_i\|^2>0,\qquad
\phi(S\mathfrak C)=0,
\tag{1.1}
$$
并使用原慢 $S=S_N$ 或 $S_Y$ 在 $H$ 上单射的已证事实。
本稿不需要 $r$ 最小。

取 $m_n\to\infty$，分解
$$
H=K_{m_n}\otimes H_{m_n},\qquad
\Omega=\Omega_{<m_n}\otimes\Omega_{m_n}.
$$
允许每步有限个源，个数 $k_n$ 也可变化，但要求准确形式
$$
\boxed{
g_{\ell,n}=\Omega_{<m_n}\otimes z_{\ell,n},
\qquad z_{\ell,n}\in H_{m_n},
\quad 1\le\ell\le k_n.
}
\tag{1.2}
$$
$z_{\ell,n}$ 可以有任意相位、内部相关性和物理支撑，不要求有限柱。

取真实有界系数 $T_{i\ell,n}\in\mathfrak C$，使
$$
e_{i,n}=Cf_i-\sum_{\ell=1}^{k_n}T_{i\ell,n}g_{\ell,n},
\qquad
\varepsilon_n^2=\sum_i\|e_{i,n}\|^2\longrightarrow0.
\tag{1.3}
$$
定义实际聚合向量及总乘积预算
$$
h_{\ell,n}=\sum_iT_{i\ell,n}f_i,\qquad
H_n=\sum_{\ell=1}^{k_n}\|z_{\ell,n}\|\,\|h_{\ell,n}\|.
\tag{1.4}
$$
每个 n 的所有和均有限；不要求系数算子统一有界。

有界 $C$ 对称性及交换性给准确误差式
$$
\phi(F)=\sum_\ell B(Fh_{\ell,n},g_{\ell,n})
+\sum_iB(Ff_i,e_{i,n}),
\qquad F\in\mathfrak C,
\tag{1.5}
$$
$$
\left|\sum_iB(Ff_i,e_{i,n})\right|
\le\sqrt\tau\,\varepsilon_n\|F\|.
\tag{1.6}
$$

## 2. 尾擦除的准确定义

原反射共轭按物理头尾分解，
$$
C=C_{<m}\otimes C_m,\qquad
C_{<m}\Omega_{<m}=\Omega_{<m},\qquad
C_m\Omega_m=\Omega_m.
\tag{2.1}
$$
这是原反射在各位作翻转并复共轭的同一张量作用；
没有另行改变未知不变子空间或表示。

对 (1.2) 定义有界算子
$$
V_{\ell,n}
=I_{K_{m_n}}\otimes
|C_{m_n}z_{\ell,n}\rangle\langle\Omega_{m_n}|,
\qquad
W_{\ell,n}=V_{\ell,n}^*.
\tag{2.2}
$$
这里 $|u\rangle\langle v|$ 表示 $h\mapsto\langle h,v\rangle u$。
所以
$$
V_{\ell,n}\Omega=Cg_{\ell,n},\qquad
\|V_{\ell,n}\|=\|W_{\ell,n}\|=\|z_{\ell,n}\|.
\tag{2.3}
$$
定义擦除后的单个向量
$$
\boxed{
v_n=\sum_\ell W_{\ell,n}h_{\ell,n}.
}
\tag{2.4}
$$
它属于原前 $m_n$ 位柱空间
$K_{m_n}\otimes\mathbb C\Omega_{m_n}$，且
$$
\|v_n\|\le H_n.
\tag{2.5}
$$
不声称它由一张新的实际 $A'$ 系数表生成。

由 (2.3)，
$$
B(Fh_{\ell,n},g_{\ell,n})
=\langle W_{\ell,n}Fh_{\ell,n},\Omega\rangle.
$$
故 (1.5) 准确变成
$$
\boxed{
\phi(F)-\langle Fv_n,\Omega\rangle
=
\sum_\ell
\langle[W_{\ell,n},F]h_{\ell,n},\Omega\rangle
+\sum_iB(Ff_i,e_{i,n}).
}
\tag{2.6}
$$
$W_{\ell,n}$ 一般不在 $A'$；后续证明必须支付第一项。

## 3. 一致有界聚合预算已经不可能

对任意固定原 UHF 元 $D$，
令 $D^{[m]}$ 是前 $m$ 位矩阵且
$\|D-D^{[m]}\|\to0$ 的近似。
因尾擦除与所有前 $m_n$ 位矩阵严格交换，
$$
\sum_\ell
\|[W_{\ell,n},D]h_{\ell,n}\|
\le2\|D-D^{[m_n]}\|H_n.
\tag{3.1}
$$

**定理 3.1。** 在 (1.1)--(1.3) 下，$H_n$ 不能有有界子列。
特别，
$$
\boxed{H_n\longrightarrow\infty.}
\tag{3.2}
$$

证明：若 $H_n$ 有有界子列，(2.5) 使同一子列的 $v_n$ 有界。
进一步取 $v_n\rightharpoonup v$。
因为 $\mathcal A\subset\mathfrak U$，(2.6)、(3.1) 和 (1.6)
给
$$
\phi(F)=\langle Fv,\Omega\rangle
\qquad(F\in\mathcal A).
\tag{3.3}
$$
取 $F=SA^j$，使用湮灭式，得到
$$
0=\langle A^jSv,\Omega\rangle
=B(Sv,A^j\Omega)\qquad(j\ge0).
$$
真空循环性和双线性非退化性迫 $Sv=0$。
$S$ 单射给 $v=0$，再取 $F=I$ 得 $\tau=0$，矛盾。
所以没有有界子列，证明 (3.2)。证毕。

若固定 $k_n=k$ 且 $\sup_{n,\ell}\|z_{\ell,n}\|<\infty$，
则 Cauchy--Schwarz 给
$$
H_n\le
\left(\sum_\ell\|z_{\ell,n}\|^2\right)^{1/2}
\left(\sum_\ell\|h_{\ell,n}\|^2\right)^{1/2}.
$$
因此
$$
\boxed{
\left(\sum_\ell\|h_{\ell,n}\|^2\right)^{1/2}
\longrightarrow\infty.
}
\tag{3.4}
$$
同一结论允许 $k_n$ 增长，只要第一括号仍统一有界。

纯远尾源可以是远处的 Walsh 字符或任意归一化远尾向量。
它们可能弱趋零，因此这里不是强收敛源定理的直接代入。
合法极限通过 (2.6) 先擦除源，再对单个有界 $v_n$ 取弱极限；
没有交换两个变化弱向量的配对极限。

## 4. 原 A 的准确有限头截断误差

为了允许 $H_n$ 增长，下面从原递推直接计算 carry，
不用猜测单个 $\eta_m$ 就是 $A$ 的头截断误差。

写
$$
A=d_0N_0,\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},
\qquad \|N_j\|\le1,
\qquad 0<\eta_j\le e^{-770\,16^j}.
\tag{4.1}
$$
令
$$
\theta_j=\prod_{s=0}^{j-1}\eta_s,\qquad \theta_0=1,
$$
$$
A_{<m}
=d_0\sum_{j=0}^{m-1}
\theta_j E_0^*\cdots E_{j-1}^*E_j.
\tag{4.2}
$$
这是前 $m$ 位的已知有限矩阵，恒等作用于其后物理尾。
有限次代入 (4.1)，准确得到
$$
\boxed{
A-A_{<m}
=d_0\theta_m E_0^*\cdots E_{m-1}^*N_m.
}
\tag{4.3}
$$
因前后因子作用在不交张量坐标，且 $N_m$ 的物理块矩阵有单位下左角，
$\|N_m\|=1$。所以甚至有准确范数
$$
\boxed{
a_m^{\rm car}:=\|A-A_{<m}\|
=d_0\theta_m
\le
d_0\exp\!\left[-\frac{770}{15}(16^m-1)\right].
}
\tag{4.4}
$$
仅使用 $\|N_m\|\le1$ 得到同一上界已经足够。
这里的主指数是有限头之前全部 $\eta_s$ 的乘积，
而不是单个 $\eta_m$。

$W_{\ell,n}$ 与 $A_{<m_n}$ 严格交换，因此
$$
\|[W_{\ell,n},A]\|
\le2a_{m_n}^{\rm car}\|z_{\ell,n}\|.
$$
对每个固定整数 $j\ge1$，望远镜式给
$$
\boxed{
\|[W_{\ell,n},A^j]\|
\le2j\|A\|^{j-1}
a_{m_n}^{\rm car}\|z_{\ell,n}\|.
}
\tag{4.5}
$$
若 $p(t)=\sum_{j=0}^d p_jt^j$，记有限常数
$$
L_p=\sum_{j=1}^d j|p_j|\|A\|^{j-1}.
$$
(2.6) 遂给完整实际误差
$$
\boxed{
|\phi(p(A))-\langle p(A)v_n,\Omega\rangle|
\le
\sqrt\tau\,\varepsilon_n\|p(A)\|
+2L_p\,a_{m_n}^{\rm car}H_n.
}
\tag{4.6}
$$
这里每次固定 $p$，没有对全部单位球多项式声称统一 $L_p$ 上界。

## 5. 增长窗口内，连擦除后的向量也必发散

**定理 5.1。** 若除 (1.1)--(1.3) 外，还支付
$$
\boxed{
a_{m_n}^{\rm car}H_n\longrightarrow0,
}
\tag{5.1}
$$
则
$$
\boxed{
\|v_n\|\longrightarrow\infty,\qquad
\frac{v_n}{\|v_n\|}\rightharpoonup0.
}
\tag{5.2}
$$

证明：若 $v_n$ 有有界子列，取弱极限 v。
(4.6) 给
$$
\phi(p(A))=\langle p(A)v,\Omega\rangle
$$
对所有多项式成立。
两侧都是 $\mathcal A$ 上的有界线性泛函，故由范数多项式稠密性，
等式延拓到全部 $\mathcal A$。
随后用第3节的 $SA^j$、真空循环性和 $S$ 单射，仍得矛盾。
所以 $\|v_n\|\to\infty$。

再次由 (4.6)，对每个固定 $j$，
$\langle A^jv_n,\Omega\rangle\to\phi(A^j)$，从而
$$
\left\langle\frac{v_n}{\|v_n\|},(A^*)^j\Omega\right\rangle\to0.
$$
由于 $A$ 为 $C$ 对称且 $C\Omega=\Omega$，
$$
(A^*)^j\Omega=CA^j\Omega.
$$
这些向量张成稠密子空间。
归一向量范数为1，稠密测试遂给整个序列弱趋零。证毕。

例如，(4.4) 保证
$$
\log(1+H_n)=o(16^{m_n})
$$
足以支付 (5.1)。
写 $q_n=2^{m_n}$ 时，任何
$$
H_n\le\exp(O(q_n^3\log q_n))
$$
都在此预算之内。
更具体地，$H_n\le\exp(c\,16^{m_n})$ 且固定
$c<770/15$ 也足够。
这些是总向量乘积预算的充分条件，不是对系数算子
$\|T_{i\ell,n}\|$ 或实际存在的见证作未经证明的上界。

取 $p=1$，(4.6) 还给
$$
\langle v_n,\Omega\rangle\longrightarrow\tau>0.
\tag{5.3}
$$
因此发散不是把目标泛函一并擦除后的空结论：
真空分量保留了原非零锚，而整体范数仍必须增长。

## 6. 只近似为纯尾源时，必须乘聚合成本

若实际源只写成
$$
g_{\ell,n}
=\Omega_{<m_n}\otimes z_{\ell,n}+d_{\ell,n},
$$
则在 (2.6) 右边增加
$\sum_\ell B(Fh_{\ell,n},d_{\ell,n})$。
其绝对值至多
$$
\|F\|J_n,\qquad
J_n=\sum_\ell\|h_{\ell,n}\|\,\|d_{\ell,n}\|.
\tag{6.1}
$$
因此在额外条件 $J_n\to0$ 下，上述结论保持成立：
第3节按有界 $H_n$ 子列应用，第5节仍另需 (5.1)。

不能只凭每个 $d_{\ell,n}\to0$ 就省略 (6.1)，
因为聚合向量本来可能增长。
同样，“源在远尾上有一部分质量”不等于 (1.2)；
一般头尾纠缠源不自动适用。

### 6.1 固定有限 Walsh 头可以准确合回同一真空

固定 $m_0$，取有限个固定前 $m_0$ 位 Walsh 柱 $u_1,\ldots,u_d$。
它们不要求线性无关，也不要求 $d<r$。
对 $m_n\ge m_0$，把 $u_a$ 在中间位补真空，记头向量为 $u_a^{[m_n]}$。
现在允许准确源
$$
g_{\ell,n}=\sum_{a=1}^d u_a^{[m_n]}\otimes z_{a\ell,n}.
\tag{6.2}
$$

此处需要一个比真空循环性更强、但已经准确建立的原乘子事实。
[R253 §1](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)
给
$$
V_F=\prod_{j\in F}(I-N_j)(I+N_j)^{-1}\in\mathcal A,
\qquad V_F\Omega=\chi_F.
$$
所以对任意固定有限 Walsh 柱
$u_a=\sum_F\widehat u_a(F)\chi_F$，有限和
$$
\boxed{
X_{u_a}=\sum_F\widehat u_a(F)V_F\in\mathcal A,
\qquad X_{u_a}\Omega=u_a
}
\tag{6.3}
$$
准确成立。没有把一般循环逼近误作有界准确原像。
这些 $X_{u_a}$ 都有有限的实际算子范数。

为每对 $(a,\ell)$ 按 (2.2) 定义 $W_{a\ell,n}$，置
$$
v_{a,n}=\sum_\ell W_{a\ell,n}h_{\ell,n},\qquad
H_{a,n}=\sum_\ell\|z_{a\ell,n}\|\,\|h_{\ell,n}\|,
$$
$$
\boxed{
\widetilde v_n=\sum_{a=1}^d X_{u_a}v_{a,n},\qquad
\mathcal H_n=\sum_{a=1}^d\|X_{u_a}\|H_{a,n}.
}
\tag{6.4}
$$
有 $\|\widetilde v_n\|\le\mathcal H_n$。
$\widetilde v_n$ 不被声称仍为有限柱；
实际 $X_{u_a}$ 作用于有限柱时可有 carry。

擦除后每项的固定第二源是 $u_a$。
利用全部有界乘子的 $C$ 对称性及与 $F\in\mathfrak C$ 的交换性，
$$
B(Fv_{a,n},u_a)
=B(Fv_{a,n},X_{u_a}\Omega)
=B(FX_{u_a}v_{a,n},\Omega).
\tag{6.5}
$$
所以这些固定头项准确合并为
$\langle F\widetilde v_n,\Omega\rangle$。

交换误差中另有 $\|u_a\|$，但由 (6.3)，
$\|u_a\|\le\|X_{u_a}\|$。
因此 (4.6) 完整变为
$$
\boxed{
|\phi(p(A))-\langle p(A)\widetilde v_n,\Omega\rangle|
\le
\sqrt\tau\,\varepsilon_n\|p(A)\|
+2L_p\,a_{m_n}^{\rm car}\mathcal H_n.
}
\tag{6.6}
$$
对固定 UHF 测试的 (3.1) 也以 $\mathcal H_n$ 支付。

于是定理3.1中的 $H_n$ 可换成 $\mathcal H_n$：
$\mathcal H_n\to\infty$。
若再有 $a_{m_n}^{\rm car}\mathcal H_n\to0$，
则定理5.1给
$$
\|\widetilde v_n\|\to\infty,\qquad
\widetilde v_n/\|\widetilde v_n\|\rightharpoonup0,
\qquad
\langle\widetilde v_n,\Omega\rangle\to\tau.
\tag{6.7}
$$
证明逐字使用固定真空后的单向量弱极限，不要求减少到少于 $r$ 个固定头源。
其原因是这里的固定头向量有准确的有界实际乘子 (6.3)，
不是一般的固定 $H$ 向量。

若 (6.2) 仅近似成立，仍须另外支付 (6.1) 的
$\sum_\ell\|h_{\ell,n}\|\|d_{\ell,n}\|\to0$。
本节没有从一般变化源推出一个固定 $m_0$、固定有限 $d$ 的这种分解。


## 7. 当前接口与保留的缺口

本稿处理的是实际 $A'$ 重构表和真正的全行慢理想见证。
尾擦除只是一种已知的有界配对操作，不被声称保持未知核或不变子空间，
也没有变成一个实际右因子。

已有的固定源、强收敛源和变化阻尼结果仍按其原范围保留。
这里新增的是任意纯远尾源不必强收敛、固定有限 Walsh 头的准确合并，
以及在准确乘积 carry 预算内对纯尾情形中已经擦除的有限柱向量
$v_n$ 的发散和归一弱零。
它排除了把“源逃到远尾”单独当作躲开聚合预算的方法。

目前没有给 $H_n$、$v_n$ 或原删除成本的见证专属上界，
没有构造所需有界聚合表示，
也没有解决普通 Hilbert ISP。

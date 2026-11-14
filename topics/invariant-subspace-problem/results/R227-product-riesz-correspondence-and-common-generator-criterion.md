# R227：乘积参考的真实 Riesz 对应与共同乘积源的充要条件

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：以下双向有界线性对应、单个纯模型换因子判据及共同乘积生成条件完整。本文把同轮 R222 的单侧亏量条件提升为“存在某个 R16 乘积共同生成向量”的必要充分条件。没有排除非乘积循环向量作为共同生成向量，也没有把共同生成失败等同于所有循环第一因子分解失败。

## 1. 主要结论

记
$$
\mathfrak C=\{A\}',\qquad
\mathfrak E=\{E_j:j\ge0\}',\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
0<\eta_j\le e^{-77016^j}.
$$
这里 $\mathfrak E$ 是原 Haar 空间中全部纯位消灭/前移矩阵的交换子，不是边界表示中的另一个空间。

**定理1.1（乘积参考的有界线性对应）。** 设 $g$ 是一个归一化收敛乘积向量，在物理正交基中写局部向量为
$$
g_j=x_je_0+y_je_1,\qquad |x_j|^2+|y_j|^2=1.
$$
假设所有 $|x_j|\ge1/2$；有限前缀可以任取为物理 $e_0$，因此任意 R16 乘积尾都可补成这样的 $g$。则存在双向有界线性对应
$$
\mathfrak F_g:\mathfrak E\longrightarrow\mathfrak C,
\qquad
\boxed{\mathfrak F_g(P)g=Pg.}
\tag{1.1}
$$
映射及逆的范数有与 $g$ 无关的绝对上界。它一般不是代数同态。

于是对这个 $g$，
$$
\boxed{\mathfrak Cg=\mathfrak Eg}
\tag{1.2}
$$
作为 $H$ 中的实际集合成立，且两种有界实现的最小算子范数互相受绝对常数控制。不是只比较闭包。

现在给定有限个非零 R16 乘积向量，允许各有任意有限非乘积前缀。吸收有限头后写
$$
f_\nu=v_\nu\otimes h^{(\nu)}_{\ge d},\qquad
 t_j^{(\nu)}=h_j^{(\nu)}(1)/h_j^{(\nu)}(0),
 \quad t^{(\nu)}-1\in\ell^2.
$$

**定理1.2（共同 R16 乘积生成的准确判据）。** 以下条件等价：

1. 存在一个带任意有限前缀的 R16 收敛乘积向量 $g\ne0$ 和有界 $B_\nu\in\mathfrak C$，使 $B_\nu g=f_\nu$ 对全部 $\nu$ 成立；
2. 对全部 $\nu$，
   $$
   \boxed{\operatorname{Im}(t^{(\nu)}-t^{(1)})\in\ell^{4/3}.}
   \tag{1.3}
   $$

共同生成向量由 R16 已知循环。这里的必要性允许任意有界 $A$ 交换子，不能通过选择另一种有限换因子乘积来绕过。

## 2. 乘积参考的正交基与纯/真实局部算子

为定理1.1，选局部正交伴侣
$$
g_j^\perp=\overline{y_j}e_0-\overline{x_j}e_1.
$$
这是与 $g_j$ 正交的单位向量。置
$$
a_j=\frac{\overline{y_j}}{x_j},\qquad
b_j=-\frac1{x_j^2},
$$
$$
S_j^g=a_jI+b_jE_j,\qquad G_j^g=a_jI+b_jN_j.
\tag{2.1}
$$
直接计算给
$$
S_j^g g=g_j^\perp\otimes g_{\ne j},
\quad |a_j|\le2,\quad |b_j|\le4,
$$
$$
\|S_j^g\|,\|G_j^g\|\le6,
\qquad \|G_j^g-S_j^g\|\le4\eta_j.
\tag{2.2}
$$
所有纯 $S_j^g$ 彼此交换，所有真实 $G_j^g$ 彼此交换；未要求两族交叉交换。

对有限集 $J$，记
$$
g_J=\prod_{j\in J}S_j^g\,g.
$$
则 $g_J$ 就是在 $J$ 位换成正交伴侣、其余位保留 $g_j$ 的乘积向量。因此 $\{g_J\}$ 是正交归一族，且完整。

完整性的细节如下：$g$ 的乘积收敛给尾 $g_{\ge m}$ 趋于 Haar 参考尾。每个空间
$H_{<m}\otimes g_{\ge m}$ 是 $J\subset[0,m)$ 的 $g_J$ 张成；这些空间递增，且任意固定 Haar 有限柱向量可在其中逼近。所以其并稠密于原 $H$。

## 3. 真实乘积基是一个统一 Riesz 基

对 $K\subset[0,j)$，定义有限局部秩一头算子
$$
Q_{j,K}^g=
|g_{\varnothing,<j+1}\rangle\langle g_{K\cup\{j\},<j+1}|\otimes I_{\ge j+1}.
$$
对固定 $j$，有
$$
\sum_{K\subset[0,j)}(Q_{j,K}^g)^*Q_{j,K}^g\le I.
\tag{3.1}
$$
它把 $g_{K\cup\{j\}\cup L}$（$L\subset(j,\infty)$）送到 $g_L$。

在正交基上定义
$$
W_g g_J=G_J^g g.
$$
按位次序展开有限乘积差，得到
$$
\boxed{
W_g-I=\sum_{j\ge0}\sum_{K\subset[0,j)}
G_K^g(G_j^g-S_j^g)Q_{j,K}^g.
}
\tag{3.2}
$$
每个基向量上只有有限项非零；范数收敛由下式保证。固定 $j$，Cauchy–Schwarz 与 (3.1) 给其内和范数至多
$$
4\eta_j\left(\sum_{K\subset[0,j)}6^{2|K|}\right)^{1/2}
=4\eta_j37^{j/2}.
$$
置
$$
\rho=4\sum_{j\ge0}e^{-77016^j}37^{j/2}<\frac12.
\tag{3.3}
$$
例如 $16^j\ge j+1$，可用几何级数直接验证最后一个严格界。于是
$$
\boxed{
\|W_g-I\|\le\rho,\quad
\|W_g\|\le1+\rho,\quad
\|W_g^{-1}\|\le(1-\rho)^{-1}.
}
\tag{3.4}
$$

每个 $G_j^g$ 为 $A$ 的真实有限多项式，且 $b_j\ne0$。当 $J\subset[0,m)$，$G_J^g$ 的最高次数准确为 $\sum_{j\in J}2^j$，最高系数非零。这些二进位次数遍历 $0,\ldots,2^m-1$，故 $G_J^g$ 与对应单项式构成同一个多项式空间。由 (3.4)，$g$ 对 $A$ 循环；对纯代数的循环性由 $g_J$ 已给出。

## 4. 双向对应的完整构造

### 4.1 从纯交换子到真实交换子

取 $P\in\mathfrak E$，置 $f=Pg$。在基上定义
$$
Y_f g_J=G_J^g f.
$$
因为 $P$ 与全部 $S_j^g$ 交换，同一排序展开给
$$
Y_f=P+\sum_{j\ge0}\sum_{K\subset[0,j)}
G_K^g(G_j^g-S_j^g)P Q_{j,K}^g.
\tag{4.1}
$$
用 (3.1) 对 $P Q_{j,K}^g$ 作列估计，得
$$
\|Y_f-P\|\le\rho\|P\|.
$$
故
$$
\mathfrak F_g(P)=Y_fW_g^{-1}
$$
有界，且
$$
\|\mathfrak F_g(P)\|\le\frac{1+\rho}{1-\rho}\|P\|.
\tag{4.2}
$$
在实际稠密轨道上，
$$
\mathfrak F_g(P)p(A)g=p(A)f
\quad(p\in\mathbb C[z]).
$$
因此它与 $A$ 交换，并把 $g$ 送到 $Pg$。

### 4.2 从真实交换子到纯交换子

反过来取 $B\in\mathfrak C$，置 $f=Bg$。先在基上定义
$$
P^{(0)}g_J=S_J^g f.
$$
这次把低位取纯因子、高位取真实因子，有限乘积恒等式给
$$
\boxed{
P^{(0)}=BW_g-
\sum_{j\ge0}\sum_{K\subset[0,j)}
S_K^g(G_j^g-S_j^g)BW_g Q_{j,K}^g.
}
\tag{4.3}
$$
同样的列范数预算证明右边按范数收敛，且
$$
\|P^{(0)}\|\le(1+\rho)\|B\|\,\|W_g\|
\le(1+\rho)^2\|B\|.
\tag{4.4}
$$
所以 $P^{(0)}$ 延拓为有界 $P$。

为验证它确实与每个 $E_j$ 交换，使用纯局部的准确二次关系
$$
(S_j^g)^2=2a_jS_j^g-a_j^2I.
\tag{4.5}
$$
当 $j\notin J$，$S_j^gg_J=g_{J\cup\{j\}}$；当 $j\in J$，用 (4.5) 化为 $g_J,g_{J\setminus\{j\}}$ 的同一线性组合。由基上的定义，$P S_j^g=S_j^gP$ 在每个 $g_J$ 上成立，故在全空间成立。因为 $b_j\ne0$，$P E_j=E_jP$。

于是 $P\in\mathfrak E$ 且 $Pg=Bg$。由 $g$ 对两个代数的循环性，保持该值的交换子各自唯一，因此两步互为逆。定理1.1 及 (1.2) 得证。

这条对应只保持在参考向量 $g$ 上的值，并未宣称它保持算子乘积、核、值域或正性。

## 5. 纯模型中产品到产品的有界性是精确可判的

先把有限个例外位吸收到有限头，在剩余尾空间中作下面的纯模型论证，并为简记将该尾从0编号。设源与目标为完整归一化乘积 $g,h$，所有首坐标均非零。写物理比率
$$
s_j=g_j(1)/g_j(0),\quad t_j=h_j(1)/h_j(0),\quad
\delta_j=t_j-s_j,
$$
其中 $s-1,t-1\in\ell^2$。

纯局部唯一换因子为
$$
V_j^0=\frac{h_j(0)}{g_j(0)}(I+\delta_jE_j).
\tag{5.1}
$$
若存在有界 $P\in\mathfrak E$ 满足 $Pg=h$，那么对每个有限头长 $m$ 和任意 $v\in H_{<m}$，纯头代数的循环性给
$$
P(v\otimes g_{\ge m})
=\left(\bigotimes_{j<m}V_j^0\right)v\otimes h_{\ge m}.
\tag{5.2}
$$
理由是 $v=p(E_0,\ldots,E_{m-1})g_{<m}$，然后将 $P$ 交换过去。两尾的范数都为1，因此
$$
\boxed{\prod_{j<m}\|V_j^0\|\le\|P\|.}
\tag{5.3}
$$

另一方面，精确奇异值公式与局部归一化给
$$
\log\|V_j^0\|
=\frac12\log\frac{1+|s_j|^2}{1+|t_j|^2}
+\operatorname{arsinh}(|\delta_j|/2).
$$
在1附近作**双侧** Taylor 估计，得到
$$
\log\|V_j^0\|
=\frac12\bigl(|\delta_j|-\operatorname{Re}\delta_j\bigr)+r_j,
\qquad
\sum_j|r_j|<\infty.
\tag{5.4}
$$
例如余项绝对值可被
$C(|s_j-1|^2+|t_j-1|^2+|\delta_j|^3)$ 控制，右边可和。

因为单侧亏量非负，(5.3)—(5.4) 强制
$$
\sum_j\bigl(|\delta_j|-\operatorname{Re}\delta_j\bigr)<\infty.
\tag{5.5}
$$
反向若 (5.5) 成立，纯有限乘积由 (5.4) 一致有界，并在循环向量 $g$ 上准确收敛到 $h$，从而强收敛到一个有界 $P\in\mathfrak E$。

因此 (5.5) 对纯模型中给定产品对的有界换因子是必要且充分的。对满足定理1.1 假设的给定源 $g$，值保持对应立即把它变成实际 $A$ 交换子的同一必要充分条件。

## 6. 任意有限前缀不会绕过尾必要条件

为后面的共同生成判据，需要允许源和目标有任意有限前缀。

首先，若实际源为 $g=v\otimes g_{\ge d}$，可以改用
$$
\xi=e_0\otimes g_{\ge d}.
$$
沿真实低头无回绕有限链，有真正有限多项式 $p_v$ 使 $g=p_v(A)\xi$。于是 $B_\nu g=f_\nu$ 给
$$
B_\nu p_v(A)\xi=f_\nu.
\tag{6.1}
$$
扩大 $d$ 可使尾部全部 $|x_j|\ge1/2$，低头的 $e_0$ 本身逐位为物理 $e_0$，所以 $\xi$ 满足定理1.1。由其反向对应，存在 $P_\nu\in\mathfrak E$，使
$$
P_\nu\xi=f_\nu.
\tag{6.2}
$$

若目标为 $v_\nu\otimes h^{(\nu)}_{\ge d}$，取其一个非零低头物理坐标 $v_{\nu,F}\ne0$。将 $P_\nu$ 的输入低头固定为 $e_0$、输出低头取该坐标，得到有界尾算子
$$
P_{\nu,F}:H_{\ge d}\longrightarrow H_{\ge d}.
$$
因 $P_\nu$ 与每个高位 $E_j$ 交换，这个尾算子也与它们交换，并由 (6.2) 得
$$
P_{\nu,F}g_{\ge d}=v_{\nu,F}h^{(\nu)}_{\ge d}.
$$
除去非零标量后，§5 的纯尾必要性适用。因此不论有限前缀如何，每个目标尾都必须满足相对于同一源尾 $s_j$ 的 (5.5)。

这里没有把任意有限前缀的源乘子反过来有界除掉；只把它乘到现有交换子上，因而没有引入未经证明的 $A^{-1}$。

## 7. 共同乘积生成的必要充分性

现在证明定理1.2。

若存在共同 R16 源，§6 给某条 $s-1\in\ell^2$，使对全部 $\nu$，
$$
\sum_j\left(|t_j^{(\nu)}-s_j|-\operatorname{Re}(t_j^{(\nu)}-s_j)\right)<\infty.
\tag{7.1}
$$
同轮 R222 的序列引理（这里重写关键一步）给准确必要条件：令 $\delta=t^{(\nu)}-s$、$d_j=|\delta_j|-\operatorname{Re}\delta_j$，则
$$
|\operatorname{Im}\delta_j|^2\le2d_j|\delta_j|.
$$
由 Hölder，
$$
\sum_j|\operatorname{Im}\delta_j|^{4/3}
\le2^{2/3}(\sum_jd_j)^{2/3}(\sum_j|\delta_j|^2)^{1/3}<\infty.
$$
两条虚部相减，便得到 (1.3)。这是任意实际有界交换子共同生成的必要性。

反之若 (1.3) 成立，置
$$
b_j^{(\nu)}=\operatorname{Im}(t_j^{(\nu)}-t_j^{(1)}),\quad
w_j=(\sum_\nu|b_j^{(\nu)}|^2)^{1/3},
$$
$$
v_j=\max(0,1-\operatorname{Re}t_j^{(1)},\ldots,
1-\operatorname{Re}t_j^{(q)}),
\quad s_j=1-v_j-w_j+i\operatorname{Im}t_j^{(1)}.
$$
则 $s-1\in\ell^2$，并有
$$
\sum_{\nu,j}\left(|t_j^{(\nu)}-s_j|-\operatorname{Re}(t_j^{(\nu)}-s_j)\right)
\le\frac12\sum_jw_j^2<\infty.
$$
选择均值为正的归一化局部向量构成参考产品尾，其平方可和偏差保证 Haar 乘积收敛。再取物理 $e_0$ 的有限前缀，使 $|x_j|\ge1/2$。

§5 给每个目标尾的有界纯交换子，定理1.1 将其传为实际交换子；有限前缀由真正有限多项式补上。也可直接使用 R222 已写出的真实有限换因子强极限。这证明充分性及定理1.2。

## 8. 一个明确的实际共同乘积生成反例

取第一个向量为常向量1。第二个向量 $h$ 取归一化局部比率
$$
t_j=1+i(j+2)^{-2/3},
$$
各局部均值选为正实数。因为 $t-1\in\ell^2$，这个 Haar 乘积收敛，且由 R16 与常向量1一样对 $A$ 循环。

但是
$$
\sum_j|\operatorname{Im}(t_j-1)|^{4/3}
=\sum_j(j+2)^{-8/9}=\infty.
$$
因此不存在任何带任意有限前缀的 R16 收敛乘积向量 $g$ 和有界 $B_1,B_2\in\{A\}'$，同时满足
$$
B_1g=1,\qquad B_2g=h.
\tag{8.1}
$$
这个结论已经包含所有实际有界交换子，而非只排一个指定的有限乘积构造。

## 9. 对有限秩路线的准确含义

R222 已证明，在 (1.3) 的类中，任意全空间稠密像的交换子 $S$ 对该有限产品族拥有同时强主理想逼近，从而排除相应第一因子类中的有限秩湮灭见证。

本稿进一步说明，若要把那个证明按“另选一个 R16 乘积共同生成向量”的方式推广到任意复杂产品族，(8.1) 给出了实际反例。必须允许一个非乘积的循环共同生成向量，或直接证明一个不经共同生成的泛函分解/主理想近似。

特别，下列更强断言均未证明：

- (8.1) 中不存在任意非乘积循环 $g$；
- 正秩二泛函 $T\mapsto\langle T1,1\rangle+\langle Th,h\rangle$ 不存在某个循环第一因子的秩一表示；
- 上述泛函湮灭 $S_N\mathcal A$ 或 $S_Y\mathcal A$。

共同向量生成失败不自动排除泛函层面的合并，因为合并可以利用不同第二因子之间的抵消。也没有从全空间中的可排类或障碍推出任何普通闭不变子空间。主问题与一般有限秩正性接口仍开放。

## 内部依赖

R88 的原始 Riesz 展开方法；R162 的单位模参考对应提供特例，但本稿对任意产品参考的公式、两向范数预算及纯模型必要性均重证。R222 的共同序列构造在 §7 写出关键步骤。没有使用纯/真实对应是代数同态的错误断言。

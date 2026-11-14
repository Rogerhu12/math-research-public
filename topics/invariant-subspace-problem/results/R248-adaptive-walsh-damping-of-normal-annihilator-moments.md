# R248：正常湮灭矩的自适应逐位阻尼与真实变形核

日期：2026-11-13（UTC+8）。作者：normal_states；Astra-ISP-1cf8c51d 复核。

状态：以下逐位阻尼与变形模型结论完整证明；它们是工作接口，不是 [R244](R244-paired-domain-regularizers-and-normal-annihilator-factorization.md) 所需交换正则器的存在证明。特别不把新的有界变形模型与原模型等同，也不由拟仿射交织免费运输未知不变格。

## 1. 正常矩的准确条件

在原 Haar 空间上，令
$$
\mathfrak C=\{A\}',\qquad
V_F=\prod_{j\in F}V_j,\qquad V_F1=\chi_F.
$$
给定任意迹类正常泛函 $\phi$，记
$$
m_F=\phi(V_F),\qquad
h_F=(-1)^{|F|}m_F.
\tag{1.1}
$$
因为 $C\chi_F=(-1)^{|F|}\chi_F$，若固定真空表示
$\phi(F)=B(Fh,1)$ 存在，则 $h_F$ 正是该向量的 Walsh 系数。

总有
$$
|h_F|\le \|\phi\|\,6^{|F|}.
\tag{1.2}
$$
对每个固定有限 $G$，
$$
\boxed{h_{G\cup\{j\}}\longrightarrow0\qquad(j\to\infty,\ j\notin G).}
\tag{1.3}
$$
证明：实际 $V_j=I-2N_j+O(\eta_j)$，而 $N_j\to I/2$ 于 WOT，所以 $V_j\to0$ 于 WOT，且范数一致有界。因此 $V_GV_j\to0$ 于 WOT。迹类正常泛函可用有限秩逼近支付这个一致有界弱极限，得到 (1.3)。

(1.3) 不是平方可和结论。R240 的正秩一态已经说明，即使函数连续、严格正且循环，全部 $(h_F)$ 也可能不在 $\ell^2$ 中。

### 1.1 $S_Y$ 的实际矩递推

令 $a_j=(j+1)^{-2}$、$a_\Sigma=\sum_j a_j$、$Y_j=(I-V_j)/2$。
若 $\phi(S_Y\mathcal A)=0$，则对每个有限 $F$，
$$
\begin{aligned}
&(a_\Sigma-2a_F)m_F
+\sum_{j\in F}a_jm_{F\setminus\{j\}}
-\sum_{j\notin F}a_jm_{F\cup\{j\}}\\
&\hspace{2cm}
=4\sum_{j\in F}a_j\phi(Y_j^2V_{F\setminus\{j\}}),
\qquad a_F=\sum_{j\in F}a_j.
\end{aligned}
\tag{1.4}
$$
这是 $V_j^2=2V_j-I+4Y_j^2$ 和
$2S_Y=a_\Sigma I-\sum_j a_jV_j$ 的直接结果。
右端是真 carry，且
$$
\|Y_j^2\|\le9\eta_j.
$$
没有将它删掉。

对 $S_N$，令
$$
K=S_N-S_Y
=\sum_ja_jN_j^2(I+N_j)^{-1}.
$$
同一递推的右侧再减去 $2\phi(KV_F)$；其中
$\|K\|\le3\sum_j a_j\eta_j$。所有无限和均按算子范数绝对收敛。

目前这些等式和正常条件 (1.3) 尚未给出原固定真空向量 $h\in H$。下面给一个准确的、但会改变算子模型的 Hilbert 实现。

## 2. 稀疏保留无阻尼位的平方可和化

固定任意
$$\frac12<\sigma<1,\qquad \delta_j^{(0)}=(j+2)^{-\sigma}.$$
对一列 $0<\delta_j\le1$ 记 $\delta_F=\prod_{j\in F}\delta_j$。

**引理2.1。** 存在一个无限稀疏集 $I=\{j_1<j_2<\cdots\}$，可令 $j_n\ge2^n$，并置
$$
\delta_j=
\begin{cases}
1,&j\in I,\\
(j+2)^{-\sigma},&j\notin I,
\end{cases}
$$
使
$$
\boxed{\sum_{F\ {\rm finite}}\delta_F^2|h_F|^2<\infty.}
\tag{2.1}
$$

**证明。** 若 $\delta\in\ell^2$，由 (1.2)
$$
H(\delta):=\sum_F\delta_F^2|h_F|^2
\le\|\phi\|^2\prod_j(1+36\delta_j^2)<\infty.
$$
假设已经把有限多个坐标升级到1，其余仍为 $\delta^{(0)}$。此时仍有 $\delta\in\ell^2$。
将尚未升级的第 $j$ 个坐标改成1时，$H$ 的增加恰为
$$
(1-\delta_j^2)
\sum_{G:j\notin G}\delta_G^2|h_{G\cup\{j\}}|^2.
\tag{2.2}
$$
对每个固定 $G$，(1.3) 使该项趋零。
而统一支配级数为
$$
36\|\phi\|^2\sum_G36^{|G|}\delta_G^2<\infty.
$$
因此 (2.2) 在 $j\to\infty$ 时趋零。
递归选择 $j_n>\max(j_{n-1},2^n)$，使第 $n$ 次增加不超过 $2^{-n}$。
最后对递增的系数权用单调收敛，得到
$H(\delta)\le H(\delta^{(0)})+1$。证毕。

定义有界 Walsh 对角算子
$$
D_\delta\chi_F=\delta_F\chi_F.
$$
它是单射、稠密像的正收缩；每个有限柱向量属于其像。因为 $D_\delta\chi_{j_n}=\chi_{j_n}$，它不紧。
引理给真正的 Hilbert 向量
$$
h_\delta=\sum_F\delta_Fh_F\chi_F\in H.
\tag{2.3}
$$
若 $\phi(I)\ne0$，则 $h_\delta\ne0$，且其常数系数仍为 $\phi(I)$。

这一步用的是每个正常矩列的高位消失；没有假设任何原次数指数矩或原平方可和性。

## 3. 多项式下界支付真实算子变形

对于只作用于有限位块 $K$ 的算子 $B$，定义其局部对角相似
$$
B_\delta=D_{\delta,K}BD_{\delta,K}^{-1}.
$$
不同有限块的定义相容，并有
$$
\|B_\delta\|
\le\left(\prod_{j\in K}\delta_j^{-1}\right)\|B\|
\le\left(\prod_{j\in K}(j+2)^\sigma\right)\|B\|.
\tag{3.1}
$$
这里没有把全空间 $D_\delta^{-1}$ 宣称为有界。

[R171](R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md) 的准确局部展开为
$$
N_j=\sum_{r\ge j}\frac{\alpha_r}{\alpha_j}
 E_j^*\cdots E_{r-1}^*E_r,
$$
以及
$$
V_j=(I-2E_j)+\sum_{r\ge j+1}B_{j,r},
\qquad
\operatorname{supp}B_{j,r}\subset[j,r],\quad
\|B_{j,r}\|\le18\frac{\alpha_r}{\alpha_j}.
\tag{3.2}
$$
准确比率满足
$$
\frac{\alpha_r}{\alpha_j}
=\prod_{\nu=j}^{r-1}\eta_\nu
\le e^{-77016^{r-1}}\qquad(r\ge j+1).
\tag{3.3}
$$
将每个局部项按 (3.1) 变形。其额外成本至多
$(r+2)^{\sigma(r-j+1)}$，而 (3.3) 支付该成本及全部求和。
所以得到实际有界算子 $N_{j,\delta},V_{j,\delta}$，并有
$$
\|N_{j,\delta}\|\le\delta_j^{-1}+\varepsilon_j,\qquad
\|V_{j,\delta}\|\le3\delta_j^{-1}+18\varepsilon_j,
\tag{3.4}
$$
其中可取
$$
\varepsilon_j=
\sum_{r\ge j+1}(r+2)^{r+1}e^{-77016^{r-1}}\to0.
$$
每项局部交织经绝对范数极限给
$$
D_\delta N_j=N_{j,\delta}D_\delta,\qquad
D_\delta V_j=V_{j,\delta}D_\delta.
\tag{3.5}
$$

由于 $\sigma<1$，
$$\sum_ja_j\delta_j^{-1}<\infty.$$
于是两种慢算子都有有界变形
$$
S_{N,\delta}=\sum_ja_jN_{j,\delta},\qquad
S_{Y,\delta}=\frac12\sum_ja_j(I-V_{j,\delta}),
$$
且准确满足
$$
\boxed{D_\delta S=S_\delta D_\delta.}
\tag{3.6}
$$
同理 $A_\delta=\alpha_0N_{0,\delta}$ 有界。
稠密像交织保留所有有限代数关系，特别
$$
N_{j,\delta}=A_\delta^{2^j}/d_j,\qquad
N_{j,\delta}^2=\eta_jN_{j+1,\delta}.
\tag{3.7}
$$
由第二式迭代、(3.4) 的多项式范数增长及 $\eta_j$ 的超快衰减，
$N_{j,\delta}$ 拟幂零。因此 $I+N_{j,\delta}$ 可逆。
交织原 Cayley 恒等式并利用 $D_\delta$ 稠密像，得到
$$
V_{j,\delta}=(I-N_{j,\delta})(I+N_{j,\delta})^{-1}.
$$
故 (3.6) 是保留了实际递归与全部 carry 的真实模型，不是只在形式系数上作相似。

## 4. 湮灭方程成为新模型中的实际 Hilbert 核方程

下面说明交换无限级数所需的控制，避免由“形式矩”直接跳到闭域。

对每个固定有限 $F$，令
$$S\chi_F=\sum_Gc_G\chi_G.$$
有
$$
\boxed{\sum_G6^{|G|}|c_G|<\infty.}
\tag{4.1}
$$
纯单个位项作用于 $\chi_F$ 只产生至多两个 Walsh 字符，系数和及次数增加有统一界，故其求和由 $\sum a_j<\infty$ 支付。
对于支撑于 $[j,r]$、长度 $L=r-j+1$ 的 carry 项，作用后至多有 $2^L$ 个内部字符；系数 $\ell^1$ 范数至多 $2^{L/2}$ 倍向量范数，权 $6^{|G|}$ 至多再付 $6^{|F|+L}$。
(3.2)--(3.3) 因而支付全部 carry 和。$N$ 型的局部展开同样如此。

由 (4.1)，$\sum_Gc_GV_G$ 按算子范数收敛。它在 $1$ 上的作用等于 $S\chi_F=SV_F1$。
两侧均在 $\mathfrak C$ 中；$1$ 的循环性使其为分离向量，所以
$$
SV_F=\sum_Gc_GV_G.
\tag{4.2}
$$
因此
$$
\phi(SV_F)=\sum_Gc_Gm_G
$$
绝对收敛。

记 $s_{FG}$ 为 $S$ 在 Walsh 基上的矩阵元。原 $C$ 对称性给
$$
(-1)^{|F|}s_{FG}=(-1)^{|G|}s_{GF}.
\tag{4.3}
$$
局部相似及极限给
$(S_\delta)_{FG}=\delta_Fs_{FG}/\delta_G$。
所以对 (2.3) 的 Hilbert 向量，利用 (4.1)--(4.3)，
$$
\boxed{
B(S_\delta h_\delta,\chi_F)
=\delta_F\phi(SV_F).
}
\tag{4.4}
$$
等式中的系数和绝对收敛；也与有界 $S_\delta$ 对 $h_\delta$ 的普通 Hilbert 作用一致。

若 $\phi(S\mathcal A)=0$，则右侧为零。Walsh 字符完全，故
$$
\boxed{
S_\delta h_\delta=0,\qquad
\langle h_\delta,1\rangle=\phi(I).
}
\tag{4.5}
$$
特别，任何假想非零正有限秩正常湮灭者都会给这个状态适配变形中的非零实际核向量。

## 5. 变形仍保留 $A$ 的高幂强单位，不能据此消除慢核

在保留集 $I$ 上 $\delta_{j_n}=1$，故 (3.4) 及局部展开给
$$
\|N_{j_n,\delta}-E_{j_n}\|\to0.
$$
于是
$$
N_{j_n,\delta}\to I/2\quad\text{WOT}.
$$
更强地，置
$$
P_n=\frac2n\sum_{k=n+1}^{2n}N_{j_k,\delta}.
$$
在每个固定有限柱上，$2E_{j_k}-I$ 是互异高位 Walsh 翻转，平均向量的范数为原范数的 $n^{-1/2}$ 倍；carry 平均范数也趋零。
一致有界性遂给 $P_n\to I$ 强，且各 $P_n$ 是 $A_\delta$ 的高阶多项式，最低阶趋于无穷。
因此 $A_\delta$ 在所有有限放大不变子商上仍单射、稠密像，论证与 R140 的高幂强单位相同。

但这只适用于 $A_\delta$ 的固定正整数幂。它没有证明 $S_\delta$ 单射。若 (4.5) 成立，恰是该新的慢核仍须处理。
(3.6) 和原 $S$ 稠密像还给 $S_\delta$ 稠密像；因此可能的新核不是由丢失稠密像造成。

## 6. 为什么它尚不是 R244 的正则器

$D_\delta$ 不在 $\mathfrak C$ 中。事实上 $D_\delta1=1$，若它与 $A$ 交换，则由 $1$ 循环必有 $D_\delta=I$，但构造保留了无限多个严格小于1的坐标。

变形一般也不保持原 $C$ 对称性。不能从原 $S$ 的单射性，经一个只有稠密像的交织
$D_\delta S=S_\delta D_\delta$，就推出 $S_\delta$ 单射。
由原单射性只能知道
$$
\ker S_\delta\cap\operatorname{Ran}D_\delta=\{0\}.
$$
一个非零闭核可以与这个稠密像交为零；(4.5) 不证明 $h_\delta$ 属于该像。

甚至不能用一个非零原交换子把整个 $H$ 送入 $\operatorname{Dom}D_\delta^{-1}$ 来恢复原空间。若
$R\in\mathfrak C$ 且 $RH\subseteq\operatorname{Dom}D_\delta^{-1}$，
闭图定理使 $T=D_\delta^{-1}R$ 有界。
取 $j\notin I$ 趋于无穷，故 $\delta_j\to0$。令 $P_j$ 为包含第 $j$ 个 Walsh 字符的次数投影，$J_j=M_{\chi_j}$。
由 R164 的真实渐近交换，
$RJ_jx-J_jRx\to0$ 对每个固定 $x$ 成立；同时 $P_jRx\to0$，所以
$$
\|P_jRJ_jx\|\longrightarrow\|Rx\|.
$$
然而 $D_\delta^{-1}$ 在 $\operatorname{Ran}P_j$ 上至少放大 $\delta_j^{-1}$，从而
$$
\|P_jRJ_jx\|
\le\delta_j\|TJ_jx\|
\le\delta_j\|T\|\|x\|\to0.
$$
故 $Rx=0$ 对全部 $x$，即 $R=0$。

这不排除只对指定的有限输入验证配对域，也不排除别的交换正则器。
它准确说明：逐位噪声确实能把每个正常矩族变成一个 Hilbert 向量，并保留全部真实方程；当前代价是改变模型，而这种代价不能靠一个非零全域原交换正则器免费撤销。

## 7. 当前剩余问题

对真实假想湮灭者，(1.4)、(1.3) 和 (4.5) 都是已验证的必要结构。仍需二选一的额外推进：

- 在该状态适配变形中证明相应 $S_\delta$ 无核，或证明特殊的 $h_\delta$ 位于 $\operatorname{Ran}D_\delta$；
- 直接利用慢理想矩方程构造原 $\mathfrak C$ 中的指定输入配对正则器，并使其状态值非零。

本稿没有得到这一步，也没有把一般噪声平方可和化写成原固定真空分解。普通 ISP 与原慢符号的强主理想单位仍开放。


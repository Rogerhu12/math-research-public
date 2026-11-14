# R178：真实高阶 gauge 的渐近交换与双慢核的角度退化

日期：2026-11-12（UTC）。作者：literature。

状态：完整证明。本稿把 R164 的单高位结论推进到阶数趋于无穷的规范 dyadic gauge，并与 R169 的泛型核交零结合，得到未知双慢核必须满足的角度退化及闭图替代。它不排除单个非零核，也不排除某一对核的和恰好闭。

## 1. 主结论

令
$$
H=L^2(\{0,1\}^{\mathbb N},\mu),\qquad
\mu=\bigotimes_{j\ge0}\tfrac12(\delta_0+\delta_1),
$$
并沿用实际径向 odometer 算子 $A$。
记 $\operatorname{Lat}A$ 为闭 $A$ 不变子空间格。

对
$$
\zeta_n=e^{2\pi i/2^n},\qquad
U_n=U_{\zeta_n},
$$
规范 gauge 酉算子为
$$
(U_nf)(y)
=\exp\!\left(2\pi i\sum_{k=0}^{n-1}y_k2^{k-n}\right)f(y).
\tag{1.1}
$$
它满足
$$
U_nAU_n^*=\zeta_n A.
\tag{1.2}
$$

**定理1.1。** 对每个 $M\in\operatorname{Lat}A$，令 $P=P_M$。则
$$
\boxed{
[P,U_n]\longrightarrow0\quad\text{强*},\qquad
U_nPU_n^*\longrightarrow P\quad\text{强}.
}
\tag{1.3}
$$
同样结论适用于固定整数 $b$ 的
$U_{\exp(2\pi ib/2^n)}$。

该结论由固定有限多个高位的真实 pattern 算子证明。
不能仅把 R164 的各个单高位强极限相乘，因为相邻因子和测试向量都随 $n$ 变化。

现在设 $T\in\mathcal A\setminus\{0\}$ 满足 R169 的泛型两轨道共同核结论：
存在有限 dyadic 子群 $H_0$，使
$$
\ker T\cap\ker\gamma_\zeta T=\{0\}
\qquad(\zeta\notin H_0).
\tag{1.4}
$$
例如，$T$ 可以是至多两个独立加性慢方向上的非零实际
$\mathcal G$ 系数多项式演算。

**定理1.2。** 假设 $M=\ker T\ne\{0\}$，令
$$
M_n=U_nM=\ker\gamma_{\zeta_n}T,\qquad P_n=P_{M_n}.
$$
则对所有充分大的 $n$，
$$
M\cap M_n=\{0\},\qquad P_n\longrightarrow P_M\quad\text{强}.
\tag{1.5}
$$
加法映射
$$
\mathcal J_n:M\oplus M_n\longrightarrow H,\qquad
\mathcal J_n(x,y)=x+y
$$
单射，并满足
$$
\boxed{
c_n:=\inf_{(x,y)\ne0}
\frac{\|x+y\|}{(\|x\|^2+\|y\|^2)^{1/2}}
\longrightarrow0,\qquad
\|\mathcal J_n\|\longrightarrow\sqrt2.
}
\tag{1.6}
$$
若 $M+M_n$ 在某个无穷子序列上是闭的，则对应的有界规范投影
$$
E_n:M+M_n\longrightarrow M,\qquad E_n(x+y)=x
$$
满足
$$
\boxed{\|E_n\|\longrightarrow\infty}
\tag{1.7}
$$
沿该子序列成立。

因此 R169 的代数直和不能在这条规范 gauge 轨道上具有一致正的角度下界。
(1.7) 没有断言每一个 $E_n$ 都无界。

## 2. 真实高位 pattern 的两个强逼近

### 2.1. 模型恒等式与实际多项式

使用已证的真实进位关系
$$
N_j=A^{2^j}/d_j
=E_j+\eta_jE_j^*N_{j+1},\qquad
E_j=e_{10}^{(j)},\qquad
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{2.1}
$$
从而
$$
\|N_j-E_j\|\le\eta_j.
\tag{2.2}
$$
$E_j$ 是第 $j$ 位的物理升算子。
它不是事件乘法投影；本节只在低位柱函数上利用两者的实际作用关系。

固定正整数 $\ell$。
令 $J\subset\mathbb N$ 为任意 $\ell$ 元集合，$\sigma\in\{0,1\}^J$。
记物理事件投影
$$
\Pi_{J,\sigma}
=M_{\mathbf1_{\{y_j=\sigma_j\ (j\in J)\}}},
\tag{2.3}
$$
以及真实多项式
$$
F_{J,\sigma}
=\prod_{\substack{j\in J\\\sigma_j=1}}N_j
 \prod_{\substack{j\in J\\\sigma_j=0}}(I-N_j).
\tag{2.4}
$$
所有因子都是 $A$ 的多项式，彼此交换，且
$$
\|F_{J,\sigma}\|\le2^\ell.
\tag{2.5}
$$
每个 $A$ 不变空间都被 $F_{J,\sigma}$ 保持。

定义纯物理算子
$$
F^0_{J,\sigma}
=\prod_{\substack{j\in J\\\sigma_j=1}}E_j
 \prod_{\substack{j\in J\\\sigma_j=0}}(I-E_j).
$$
由有限乘积的逐因子望远镜展开及 (2.2)，
$$
\boxed{
\|F_{J,\sigma}-F^0_{J,\sigma}\|
\le2^{\ell-1}\sum_{j\in J}\eta_j.
}
\tag{2.6}
$$
这里不需要实际因子与纯因子相互交换；有限乘积差的望远镜式本身有效。

### 2.2. 柱函数上的精确式

若 $f$ 只依赖 $J$ 之前的有限多个低位，则
$$
E_jf=\mathbf1_{\{y_j=1\}}f,\qquad
E_j^*f=\mathbf1_{\{y_j=0\}}f
\qquad(j\in J).
\tag{2.7}
$$
这是参考向量 $(e_0+e_1)/\sqrt2$ 上的直接物理矩阵计算。
不同位的纯物理算子交换，所以
$$
F^0_{J,\sigma}f=\Pi_{J,\sigma}f.
\tag{2.8}
$$

令 $\bar\sigma$ 为逐位互补 pattern，即
$\bar\sigma_j=1-\sigma_j$。
在相同柱函数上，
$$
\boxed{
(F^0_{J,\bar\sigma})^*f=\Pi_{J,\sigma}f.
}
\tag{2.9}
$$
确切地，若 $\sigma_j=1$，互补因子为
$(I-E_j)^*=I-E_j^*$，它把常向量变为位 $1$ 事件；
若 $\sigma_j=0$，互补因子为 $E_j^*$，它给位 $0$ 事件。

(2.8) 与 (2.9) 使用了互补 pattern。
一般不能把 $(F^0_{J,\sigma})^*$ 直接当作同一个
$\Pi_{J,\sigma}$ 的逼近。

### 2.3. 任意固定向量上的强极限

令 $Q_m^{\rm cyl}$ 为条件期望到前 $m$ 位的正交投影，并记
$$
\omega_m(f)=\|f-Q_m^{\rm cyl}f\|.
$$
则 $\omega_m(f)\to0$。

若 $J\subseteq\{m,m+1,\ldots\}$，由 (2.5)—(2.9)，
$$
\begin{aligned}
\|(F_{J,\sigma}-\Pi_{J,\sigma})f\|
&\le(2^\ell+1)\omega_m(f)
 +2^{\ell-1}\sum_{j\in J}\eta_j\,\|f\|,\\
\|(F_{J,\bar\sigma}^*-\Pi_{J,\sigma})f\|
&\le(2^\ell+1)\omega_m(f)
 +2^{\ell-1}\sum_{j\in J}\eta_j\,\|f\|.
\end{aligned}
\tag{2.10}
$$
例如第一行先在 $Q_m^{\rm cyl}f$ 上使用 (2.8)，
再用 $\|F^0_{J,\sigma}-\Pi_{J,\sigma}\|\le2^\ell+1$
控制余项；实际与纯模型的差由 (2.6) 控制。

因此，在 $\ell$ 固定且 $\min J\to\infty$ 时，
$$
\boxed{
F_{J,\sigma}-\Pi_{J,\sigma}\to0\text{ 强},\qquad
F_{J,\bar\sigma}^*-\Pi_{J,\sigma}\to0\text{ 强}.
}
\tag{2.11}
$$
这些估计在所有 $\ell$ 元高位集合及其有限个 pattern 上一致。

对互补 pattern 再用一次 (2.11)，得到
$$
\boxed{
F_{J,\sigma}-F_{J,\bar\sigma}^*
\longrightarrow0\quad\text{强*}.
}
\tag{2.12}
$$
注意 (2.11) 的每个单独差仅被声称强收敛。
(2.12) 的强*收敛使用了两种互补逼近。

## 3. 任意不变投影与高位 pattern 渐近交换

固定 $M\in\operatorname{Lat}A$，令 $P=P_M$、$Q=I-P$。
实际多项式保持 $M$，所以
$$
QF_{J,\sigma}P=0,\qquad
QF_{J,\bar\sigma}P=0.
\tag{3.1}
$$
第二式取伴随给
$$
PF_{J,\bar\sigma}^*Q=0.
$$
因此
$$
\begin{aligned}
[P,F_{J,\sigma}]
&=PF_{J,\sigma}Q\\
&=P(F_{J,\sigma}-F_{J,\bar\sigma}^*)Q.
\end{aligned}
\tag{3.2}
$$
右端由 (2.12) 强*趋零；这里两侧 $P,Q$ 都固定。
于是
$$
[P,F_{J,\sigma}]\longrightarrow0\quad\text{强*}.
\tag{3.3}
$$

再由 (2.11)，对每个固定 $f$，
$$
[P,\Pi_{J,\sigma}]f
=[P,F_{J,\sigma}]f
 +P(\Pi_{J,\sigma}-F_{J,\sigma})f
 -(\Pi_{J,\sigma}-F_{J,\sigma})Pf
\longrightarrow0.
$$
因为 $P,\Pi_{J,\sigma}$ 都自伴，
$$
[P,\Pi_{J,\sigma}]^*=-[P,\Pi_{J,\sigma}],
$$
故
$$
\boxed{
[P,\Pi_{J,\sigma}]
\longrightarrow0\quad\text{强*}
\qquad(|J|=\ell\text{ 固定},\ \min J\to\infty).
}
\tag{3.4}
$$

这个证明同时处理了两个非对角块。
它没有将若干随位置变化的单高位强极限相乘。

## 4. 高阶 gauge 的两次极限

### 4.1. 固定宽度截断

对 $n\ge\ell$，定义只保留最高 $\ell$ 个参与位的酉乘法
$$
V_{n,\ell}
=M_{\exp(2\pi i\sum_{k=n-\ell}^{n-1}y_k2^{k-n})}.
\tag{4.1}
$$
它是集合
$$
J_{n,\ell}=\{n-\ell,\ldots,n-1\}
$$
的 $2^\ell$ 个 pattern 投影的线性组合，每个系数模长为一。
所以对固定 $\ell$，由 (3.4)，
$$
[P,V_{n,\ell}]\longrightarrow0\quad\text{强*}
\qquad(n\to\infty).
\tag{4.2}
$$

被丢掉的低位相位满足
$$
0\le\sum_{k=0}^{n-\ell-1}y_k2^{k-n}<2^{-\ell}.
$$
由 $|e^{it}-1|\le|t|$，
$$
\boxed{\|U_n-V_{n,\ell}\|\le2\pi\,2^{-\ell}.}
\tag{4.3}
$$
于是对每个固定 $f\in H$，
$$
\limsup_{n\to\infty}\|[P,U_n]f\|
\le4\pi\,2^{-\ell}\|f\|.
$$
先让 $n\to\infty$，再让 $\ell\to\infty$，得到
$$
[P,U_n]\to0\quad\text{强}.
$$
对伴随截断使用同一估计，得到强*收敛，证明 (1.3) 的第一式。

对于固定整数 $b$，把所有相位乘 $b$；
(4.3) 的右端改为 $2\pi|b|2^{-\ell}$，
其余证明不变。

### 4.2. 共轭投影的正确强极限

令
$$
P_n=U_nPU_n^*.
$$
必须把强收敛误差作用在固定向量上。
使用精确式
$$
\boxed{P_n-P=U_n[P,U_n^*].}
\tag{4.4}
$$
对固定 $f$，左乘酉算子不改变范数，故
$$
\|(P_n-P)f\|
=\|[P,U_n^*]f\|\longrightarrow0.
$$
这证明定理1.1。

这里没有把一个仅强趋零的算子族再右乘移动的 $U_n^*$ 来取极限。

### 4.3. 对固定核向量的显式误差

若 $f\in M$，则 $QF_{J,\sigma}f=0$。
利用 (2.10)、(4.1) 的有限 pattern 展开以及 (4.3)，有
$$
\boxed{
\begin{aligned}
\|f-P_nf\|
\le{}&2\pi\,2^{-\ell}\|f\|\\
&+2^\ell(2^\ell+1)\omega_{n-\ell}(f)\\
&+2^{2\ell-1}\ell e^{-770\,16^{n-\ell}}\|f\|,
\qquad n\ge\ell.
\end{aligned}
}
\tag{4.5}
$$
确切地，
$$
\|f-P_nf\|=\|QU_n^*f\|,
$$
再把 $U_n^*$ 换成 $V_{n,\ell}^*$；
每个 pattern 的 $Q\Pi_{J,\sigma}f$ 可换成
$Q(\Pi_{J,\sigma}-F_{J,\sigma})f$。

(4.5) 给出了依赖具体向量低位柱逼近的控制。
当前没有对未知核的单位球给 $\omega_m(f)$ 的一致衰减率。
因此仍不能任意令 $\ell=\ell(n)\to\infty$ 而忽略第二行。

虽然 $\zeta_n\to1$ 在普通圆周拓扑下成立，
$U_n$ 并不强趋 $I$：非平凡字符有
$\|U_n1-1\|^2=2$。
本稿证明的是这些高位振荡与实际不变投影的渐近交换。

## 5. 泛型双慢核的角度退化

### 5.1. 核交零与投影收敛同时成立

设 $T$ 满足 (1.4)，且 $M=\ker T\ne0$。
由 gauge 协变，
$$
\ker\gamma_{\zeta_n}T=U_nM.
$$
$U_nM$ 是 $A$ 不变空间，因为 $A U_n=\zeta_n^{-1}U_nA$。

有限 dyadic 子群必含于某个 $\mu_{2^h}$。
当 $n>h$ 时，$\zeta_n$ 的阶为 $2^n$，所以 $\zeta_n\notin H_0$。
R169 给
$$
M\cap M_n=0.
\tag{5.1}
$$
定理1.1 又给
$$
P_n\longrightarrow P\quad\text{强}.
\tag{5.2}
$$
这两条并不矛盾：交零没有提供角度的统一正下界。

### 5.2. 加法映射的最小模

固定单位向量 $f\in M$。
向量对 $(f,-P_nf)\in M\oplus M_n$ 满足
$$
\mathcal J_n(f,-P_nf)=f-P_nf.
$$
所以
$$
\boxed{
c_n\le
\frac{\|f-P_nf\|}
{\sqrt{1+\|P_nf\|^2}}
\longrightarrow0.
}
\tag{5.3}
$$
这也可结合 (4.5) 给具体 $f$ 的误差上界。

另一方面，
$$
\mathcal J_n\mathcal J_n^*=P+P_n.
$$
因此 $\|\mathcal J_n\|^2=\|P+P_n\|\le2$，且
$$
\langle(P+P_n)f,f\rangle
=1+\|P_nf\|^2\longrightarrow2.
$$
于是
$$
\|\mathcal J_n\|\longrightarrow\sqrt2.
\tag{5.4}
$$
退化发生在加法映射的下界。

### 5.3. 闭和时规范投影的范数

若 $L_n=M+M_n$ 闭，则 $\mathcal J_n$ 是
$M\oplus M_n$ 到 $L_n$ 的有界双射，
逆映射定理给有界规范投影
$$
E_n(x+y)=x.
$$
由 (5.1)，$f-P_nf\ne0$；否则 $f$ 同时属于两个核。
又有
$$
E_n(f-P_nf)=f.
$$
故
$$
\boxed{
\|E_n\|\ge\frac1{\|f-P_nf\|}.
}
\tag{5.5}
$$
沿任何闭和的无穷子序列，右侧趋无穷，证明 (1.7)。

单个 $n$ 的右侧仍是有限数。
本稿没有由 (5.5) 排除某个固定 $L_n$ 闭。

### 5.4. 有限族与可数族

R169 的更强代数结论说：
若各 gauge 位于不同的 $H_0$ 陪集，则相应核构成代数直和。
当 $n,m>h$ 且 $n\ne m$ 时，
$\zeta_n\zeta_m^{-1}$ 的阶为 $2^{\max(n,m)}$，
所以不属于 $H_0$。
因此
$$
M,\ M_{h+1},\ M_{h+2},\ldots
$$
的每个有限子族都是代数直和。

它们不具有一致的 Hilbert 直和估计。
除 (5.3) 已排除统一下界外，
从可数 Hilbert 直和到 $H$ 的未加权加法也不是有界映射：
对上述单位 $f$，所有充分大的 $n$ 都满足
$$
\langle P_nf,f\rangle=\|P_nf\|^2\ge\tfrac12.
$$
选 $k$ 个这样的不同指标，则
$$
\left\|\sum_{\nu=1}^kP_{n_\nu}f\right\|
\ge\tfrac{k}{2},\qquad
\left(\sum_{\nu=1}^k\|P_{n_\nu}f\|^2\right)^{1/2}
\le\sqrt{k}.
\tag{5.6}
$$
所以有限支持加法映射的上界常数也随子族大小发散。

(5.6) 只讨论未加权的规范加法。
它没有排除经过衰减权重的其他有界映射。

## 6. 有限核和的闭包是实际真不变空间

这一节解释为何不能把规范投影自动看作全 $H$ 的交换子。

设 $T_1,\ldots,T_s\in\mathcal A\setminus\{0\}$，
令 $M_i=\ker T_i$。
由于实际代数交换，
$$
\prod_{i=1}^sT_i
$$
杀掉每个 $M_i$，也杀掉其和的闭包。
R32 的忠实形式系数演算给 $\mathcal A$ 无零因子，因此
$$
\prod_{i=1}^sT_i\ne0.
$$
于是
$$
\boxed{
\overline{\sum_{i=1}^sM_i}
\subseteq\ker\!\left(\prod_{i=1}^sT_i\right)
\ne H.
}
\tag{6.1}
$$

特别，在 §5 中
$$
K_n=\overline{M+M_n}
$$
始终是 $H$ 的真闭 $A$ 不变子空间。
即使 $M+M_n$ 闭，其规范投影 $E_n$ 首先也是
$A|_{K_n}$ 的交换子，而不是自动属于全空间的 $\mathcal A$。

R169 的
$$
\overline{\operatorname{Ran}T+\operatorname{Ran}\gamma_{\zeta_n}T}=H
$$
是像空间陈述；它没有把 (6.1) 中的核空间闭和变为 $H$。

## 7. 两个代数直和核的精确闭图替代

下面的闭算子结论只使用两个闭子空间的交零。
应用时取 §5 的 $M,N=M_n$。

设 $M,N\subset H$ 闭、$M\cap N=0$，并置
$$
L=M+N,\qquad K=\overline L.
$$
定义
$$
\operatorname{Dom}E=L,\qquad
E:K\supset L\to K,\qquad E(x+y)=x
\quad(x\in M,\ y\in N).
\tag{7.1}
$$

### 7.1. 闭性、幂等与模交换

$E$ 稠密定义且闭。
确实，若
$$
z_j=x_j+y_j\to z,\qquad Ez_j=x_j\to x,
$$
则闭性给 $x\in M$、$z-x\in N$；
故 $z\in L$ 且 $Ez=x$。

又 $E(L)\subseteq M\subseteq L$，所以
$$
E^2=E\quad\text{在 }\operatorname{Dom}E=L\text{ 上}.
\tag{7.2}
$$
如果 $M,N$ 都 $A$ 不变，则 $L$ 被 $A$ 保持，而且
$$
EAz=AEz\qquad(z\in L).
\tag{7.3}
$$
这里是完整的域保持及交换式，没有把 $E$ 视为全域算子。

### 7.2. 有界当且仅当和闭

若 $L$ 闭，则 $K=L$，闭图定理给 $E\in B(K)$。

反之，假设 $E$ 在稠密域 $L$ 上有界。
它有唯一有界延拓 $\widetilde E$ 到 $K$。
对 $z_j\in L$ 趋于任意 $z\in K$，
$$
Ez_j\to\widetilde Ez.
$$
由 $E$ 闭，$z\in L$。
所以 $K=L$，即和闭。

因此
$$
\boxed{
E\text{ 有界}\quad\Longleftrightarrow\quad M+N\text{ 闭}.
}
\tag{7.4}
$$

### 7.3. 非闭和时的完整谱

假设 $M,N$ 都非零而 $L\ne K$。
那么 $E$ 是闭、稠密定义、无界的幂等算子。
它的点谱正好为
$$
\sigma_{\rm p}(E)=\{0,1\},
\qquad
\ker E=N,\quad \ker(E-I)=M.
\tag{7.5}
$$
若 $\lambda\ne0,1$，则
$$
(\lambda I-E)(x+y)=(\lambda-1)x+\lambda y.
\tag{7.6}
$$
利用代数直和分解，(7.6) 是 $L$ 到 $L$ 的双射。
故它在 $K$ 上单射，像恰为稠密真子空间 $L$，不是全 $K$。
因此
$$
\boxed{
\sigma(E)=\mathbb C,\quad
\rho(E)=\varnothing,\quad
\mathbb C\setminus\{0,1\}
\text{ 全为连续谱}.
}
\tag{7.7}
$$
本节没有声称 $E$ 与通常伴随同域，也没有声称它是 $C$ 自伴。

### 7.4. R114、R164 不排除其中的有界分支

若 $L=K$，则 $E\in\{A|_K\}'$。
R114 给
$$
\|E\|_{\rm ess}=\|E\|.
\tag{7.8}
$$
其零延拓也属于 R164 的渐近交换代数，以下直接验证而不依赖角代数的条件性引用。
令 $P_K$ 为到 $K$ 的正交投影，并把 $D=EP_K$ 看作 $H$ 上算子。
因为 $E$ 与每个 $N_j|_K$ 交换，且 $K$ 被 $N_j$ 保持，
$$
[D,N_j]=D[P_K,N_j]\to0\text{ 强},\qquad
[D^*,N_j^*]=[P_K,N_j^*]D^*\to0\text{ 强}.
\tag{7.9}
$$
这里使用 R164 已证的 $[P_K,N_j]\to0$ 强*。
再用真实强极限
$$
N_j-\tfrac12(I-J_j)\to0,\qquad
N_j^*-\tfrac12(I+J_j)\to0,
$$
分别得到 $[D,J_j]\to0$ 和 $[D^*,J_j]\to0$ 强，
即 $D$ 属于 R164 的 $\mathfrak E$。
所以相应的 Calkin 忠实性确实适用。

这些结论没有要求 $E=0$ 或 $I_K$。
若 $M,N$ 非零，则两者都无限维：
有限维非零 $A$ 不变空间上的限制既单射又拟幂零，
与有限维谱理论矛盾。
所以非平凡有界规范投影具有无限维像与核，
与“没有非零紧元”相容。

R32 的无零因子结论针对实际范数代数 $\mathcal A$。
这里的 $E$ 只先属于限制交换子；
其零延拓一般不与全 $H$ 上的 $A$ 交换。
不能未经证明把它放入 $\mathcal A$，
再以幂等关系排除。

因此已有本质范数刚性与非局部化结论，
尚未排除某一对 gauge 核的闭和。
本稿新增的约束是规范高阶轨道上有界分支的范数必须发散。

## 8. 应用范围与未解决边界

1. 定理1.1 适用于所有闭 $A$ 不变子空间，不预设它是某个已知乘子的核。
2. 定理1.2 使用 R169 的泛型两轨道共同核零；至少三个独立慢方向的一般演算不能仅凭 R173 的有限族共同核零直接套用两核角度结论。
3. 对 R169 的可和第一阶慢平方、带平方可和指数权的实际二次乘子，以及有限重叠双线性实例，若它们仍有非零核，则上述全部角度结论适用。
4. 固定 $\ell$ 的 pattern 证明与两次极限没有给未知不变空间单位球上的统一速度。任意增长位数的乘积仍需独立估计。
5. $M_n\to M$ 的投影强收敛不等于投影范数收敛，也不使 $M\cap M_n$ 非零。
6. (7.7) 是非闭代数直和的规范闭投影的谱；它不是某个实际慢多项式本身的谱分类。
7. 当前没有从角度退化推出 $M=0$，没有排除每个固定闭和，也没有完成本课题的一般单核或完整 Hilbert 不变子空间问题。

## 9. 依赖与新增内容

- [R12：归一化幂](../results/R12-normalized-powers-and-compact-commutant.md)：真实高位算子的基本模型。
- [R32：gauge 与形式系数](../results/R32-gauge-action-and-formal-coefficients.md)：实际 $\mathcal A$ 的 gauge 稳定和无零因子。
- [R114：限制交织的本质范数与非局部化](../results/R114-restriction-intertwiners-essential-norm-and-localization.md)：限制交换子既有刚性及其准确范围。
- [R164：不变投影的高位渐近交换](../results/R164-invariant-projections-high-bit-essential-rigidity.md)：单高位结论和 Calkin 忠实性；本稿重新证明多位接口，不从单高位极限直接乘积。
- [R169：双慢方向的两轨道分离](../results/R169-finite-gauge-koszul-cores-and-two-slow-mode-separation.md)：有限例外两核交零、有限 gauge 核代数直和及具体慢平方应用。
- [R173：秩控制的有限轨道数](../results/R173-rank-bounded-gauge-orbits-and-slow-polynomial-joint-cyclicity.md)：一般有限类秩的联合分离范围；本稿不把该有限族结论扩大成任意两轨道结论。

新增证明为：固定有限高位 pattern 的真实互补伴随逼近；
规范高阶 gauge 与全部不变投影的强*渐近交换；
双慢未知核的角度下界退化、有界规范投影范数发散；
以及有限核和的真不变闭包和非闭和时规范闭投影的完整谱。

# R271 附录：原正规尾 primitive 真幂最小逆的四分之七次下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue。

状态：**已证明。** 本文直接在原无限正规尾 $D_m=\sum_{j\ge m}(j+1)^{-2}E_j$ 的真实 $K_q$ 上构造一个单位源。它的单步最小原像至少为 $q^{7/4}/4$，同一个源的每阶真幂最小原像还有明确下界。构造保留全部未选位和无限远尾；有限强头、相邻暗对投影及远尾 canonical 塔的物理成本全部支付。因此不能将面向全部 primitive 源的现有多项式预算统一改成 $q^{3/2+o(1)}$。本文没有断言这些源来自实际窄 Schur 来源，也不反驳真实相邻 primitive Gram 的常数一候选。

## 1. 原尾结论与参数

固定整数 $m\ge5$ 和 $q\ge16m^2$。取
$$
k=\left\lfloor\frac{\sqrt q}{4}\right\rfloor,
\qquad n=q-k,
\qquad J=m+k+2n=m+2q-k.
\tag{1.1}
$$
于是 $k\ge m\ge5$、$J\ge q$。把原位分成三个连续部分：

- 强头 $[m,m+k)$，共 $k$ 个真实位置；
- 中间 $[m+k,J)$，共 $n$ 个相邻二位块；
- 原无限远尾 $[J,\infty)$。

所有权仍是原权 $a_j=(j+1)^{-2}$，没有改成等权池。本稿强头只是纯尾内的辅助位置，不是原有限矩阵 $A_m$。记
$$
S_J=\sum_{j\ge J}a_j^2,\qquad
\delta_J=\frac{a_J^2}{S_J},\qquad
\epsilon=\frac43\delta_J k^2,
$$
$$
x_*=(m+k)^{-4},\qquad \theta=\frac{S_J}{x_*}.
\tag{1.2}
$$
积分比较及 (1.1) 给
$$
\frac1{3(J+1)^3}\le S_J\le\frac1{3J^3},
\qquad \delta_J\le\frac3{J+1},
\qquad \epsilon\le\frac14,
\tag{1.3}
$$
以及
$$
\theta\le\frac{(m+k)^4}{3J^3}
\le\frac{16k^4}{3q^3}
\le\frac1{48q}<1.
\tag{1.4}
$$

**定理。** 存在下面明确构造的同一个单位向量
$$
f_{m,q}\in K_q^{(m)}=\ker D_m\cap\mathcal H_q^{(m)}
$$
使对每个整数 $h\ge1$，原完整孔层的真幂最小逆满足
$$
\boxed{
\bigl\|(D_m^h|_{\mathcal H_{q+h}^{(m)}})^\dagger f_{m,q}\bigr\|^2
\ge
(1-\epsilon)e^{-4/(m+k+1)-\theta}
\frac{(k+1)^{\overline h}}{(h!)^2S_J^h}.
}
\tag{1.5}
$$
这里 $(k+1)^{\overline h}=(k+1)\cdots(k+h)$。特别
$$
\boxed{\|D_m^\dagger f_{m,q}\|\ge\frac14q^{7/4}.}
\tag{1.6}
$$
满射性和固定层最小逆的存在沿用[原连续尾完整幂逆](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md) §3；下界证明实际上对每个满足 $D_m^hu=f_{m,q}$ 的原像都成立。

## 2. 一个可完全求解的饱和单玻色模

本节只是下界测试模型，随后将由有界交织从原空间导出，不能直接将其当成原尾。

在 $k$ 个强头位上取真实权
$$
\alpha_i=(m+i)^{-2},\quad x_i=\alpha_i^2,
\qquad1\le i\le k,
$$
并在一个标准单玻色模上取下降 $b e_r=\sqrt r\,e_{r-1}$。令
$$
\mathcal L=\sum_{i=1}^k\alpha_iE_i+\sqrt{S_J}\,b.
\tag{2.1}
$$
强头占据基 $e_I$ 与玻色基 $e_r$ 都正交归一。固定总次数 $k$，写 $r=k-|I|$。定义
$$
c_I=Z^{-1/2}(-1)^r\sqrt{r!}\,S_J^{-r/2}
\prod_{i\notin I}\alpha_i,
\qquad
F=\sum_{I\subseteq[k]}c_I e_I\otimes e_{k-|I|},
\tag{2.2}
$$
其中
$$
Z=\sum_{r=0}^k r!\,e_r(x_1,\ldots,x_k)S_J^{-r}.
\tag{2.3}
$$
所以 $\|F\|=1$。

对任意头集合 $I$，$r=k-|I|\ge1$ 时准确有
$$
\sum_{i\notin I}\alpha_i c_{I\cup\{i\}}
=-\sqrt{S_Jr}\,c_I.
\tag{2.4}
$$
因为左边有 $r$ 个相同的乘积项，$r\sqrt{(r-1)!}=\sqrt r\sqrt{r!}$。这逐坐标证明
$$
\mathcal L F=0.
\tag{2.5}
$$

第 $k+h$ 层对每个 $h\ge0$ 都以全部 $I\subseteq[k]$ 为索引，玻色孔数为 $r+h$。当 $h\ge1$ 时，下降到第 $k+h-1$ 层的矩阵按 $|I|$ 排列为三角矩阵，其玻色对角元是
$\sqrt{S_J(r+h)}>0$。因此这个矩阵可逆，$\mathcal L^h$ 到第 $k$ 层也可逆。

定义
$$
G_h=\sum_{I\subseteq[k]}
c_I\frac{\sqrt{(r+h)!/r!}}{h!S_J^{h/2}}
e_I\otimes e_{r+h},\qquad G_0=F.
\tag{2.6}
$$
用 (2.4) 计算 $\mathcal LG_h$：玻色项给系数中的 $r+h$，强头删除项给 $-r$，差为 $h$，正好消去阶乘的一阶。因此
$$
\mathcal LG_h=G_{h-1},\qquad\mathcal L^hG_h=F.
$$
由上面的可逆性，$G_h$ 是测试模型整个该层内的唯一原像，因而是真正最小原像。

令概率分布
$$
\Pr(R=r)=\frac{r!\,e_r(x)S_J^{-r}}{Z},\qquad0\le r\le k.
$$
准确最小能量为
$$
\boxed{\|G_h\|^2
=\frac{\mathbb E[(R+1)^{\overline h}]}{(h!)^2S_J^h}.}
\tag{2.7}
$$
这是固定正概率分布的上升阶乘矩；没有将一般 primitive Gram 断言为正矩。

## 3. 强头使这个真实测试能量至少为 $k/S_J$

全部 $x_i\ge x_*=(m+k)^{-4}$。记 $w_r=r!e_r(x)S_J^{-r}$。对 $0\le\ell\le k$，对称和的互补恒等式给
$$
\frac{w_{k-\ell}}{w_k}
=\frac{(k-\ell)!}{k!}\,S_J^\ell e_\ell(x_1^{-1},\ldots,x_k^{-1})
\le\frac{\theta^\ell}{\ell!}.
\tag{3.1}
$$
故 $Z/w_k\le e^\theta$，并且
$$
\Pr(R=k)\ge e^{-\theta},\qquad
\mathbb E[(R+1)^{\overline h}]
\ge(k+1)^{\overline h}e^{-\theta}.
\tag{3.2}
$$
代入 (2.7)，得到同一个测试源的全部真幂能量下界。

## 4. 原远尾的精确收缩分析和有界 canonical 提升

在原 $[J,\infty)$ 尾上记删除为 $D_J$，真空为 $\Omega$。对每个 $r\ge0$ 定义单玻色模分析
$$
T_r u
=\left\langle
\frac{(D_J^*)^r\Omega}{\sqrt{r!S_J^r}},u
\right\rangle e_r,
\qquad u\in\mathcal H_r^{(J)}.
\tag{4.1}
$$
此处取创建向量的线性行算子；明确说，$T_ru$ 的标量系数是 $\sum_{|I|=r}\sqrt{r!}\,S_J^{-r/2}(\prod_{i\in I}a_i)u_I$。平方自由系数计数给
$$
\left\|\frac{(D_J^*)^r\Omega}{\sqrt{r!S_J^r}}\right\|^2
=\frac{r!e_r(a_J^2,a_{J+1}^2,\ldots)}{S_J^r}\le1.
$$
最后一个不等式来自展开 $S_J^r$ 后保留全部互异指标项。因此 $T=\bigoplus_rT_r$ 是收缩，而且从创建列定义准确有
$$
\boxed{T_{r-1}D_J=\sqrt{rS_J}\,T_r.}
\tag{4.2}
$$
这对每个有限层成立，不要求待测原像位于创建像或某个对称子空间。

在层 $0,\ldots,k$ 上，(1.3) 满足[双 Fock canonical 塔](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)定理1.1的条件。取其真空出生列 $v_r$，即
$$
v_0=\Omega,\qquad
v_r=\sqrt{r!S_J^r}\,
D_{J,r}^\dagger D_{J,r-1}^\dagger\cdots D_{J,1}^\dagger\Omega,
\quad0\le r\le k.
\tag{4.3}
$$
这里 $D_{J,t}$ 是第 $t$ 层到第 $t-1$ 层的真实删除；(4.3) 是已付 canonical 顺次塔，此处不把它称为真幂 MP。该塔的完整条件数证明给
$$
\boxed{D_Jv_r=\sqrt{rS_J}\,v_{r-1},\qquad
1\le\|v_r\|\le(1-\epsilon)^{-1/2}.}
\tag{4.4}
$$
此外，(4.3) 的准确降阶或直接取内积给
$$
\boxed{T_rv_r=e_r.}
\tag{4.5}
$$
例如 $D_J^rv_r=\sqrt{r!S_J^r}\,\Omega$，与 (4.1) 完全匹配。

把测试源 (2.2) 的每个 $e_r$ 替换为 $v_r$，得到原强头加原远尾的向量
$$
\widehat F=\sum_{I\subseteq[k]}c_I e_I\otimes v_{k-|I|}.
\tag{4.6}
$$
由 (2.4)、(4.4)，
$$
(D_{[m,m+k)}+D_J)\widehat F=0.
$$
不同头集合正交，故
$$
\boxed{1\le\|\widehat F\|\le(1-\epsilon)^{-1/2},
\qquad(I\otimes T)\widehat F=F.}
\tag{4.7}
$$
上界只用到 $r\le k$ 的 canonical 塔。后面测试任意 $h$ 的原像时只使用对全部层均收缩的 $T$，不把 (4.4) 偷延伸到 $k+h$。

## 5. 中间所有原位由真实可交换暗对投影处理

将 $[m+k,J)$ 分成 $n$ 个连续二位块。对块权 $a,b>0$ 令
$$
h=\frac{b|10\rangle-a|01\rangle}{\sqrt{a^2+b^2}},\qquad
g=\frac{a|10\rangle-b|01\rangle}{\sqrt{a^2+b^2}},\qquad
\rho=\frac{2ab}{a^2+b^2},
$$
并令 $P=|h\rangle\langle g|/\rho$ 在其余孔层为零。逐位矩阵给
$$
P^2=P,\qquad (aE_1+bE_2)P=P(aE_1+bE_2)=0,\qquad
\|P\|=\rho^{-1}.
\tag{5.1}
$$
对全部中间块取张量积 $P_{\rm gap}$，记单位暗向量积为 $h_{\rm gap}$。它保孔数、与原完整 $D_m$ 交换，而且值域准确是 $h_{\rm gap}$ 张量全部强头和远尾空间。

[完整首个三维块稿 §5](R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)的原相邻权估计，或直接对每个
$\log\rho^{-1}\le2/(j+1)^2$ 求和，给
$$
\boxed{\|P_{\rm gap}\|\le e^{2/(m+k+1)}=:R.}
\tag{5.2}
$$
这不是正交投影；范数成本 $R$ 保留在全部下界中。没有删去这段原位后再直接比较完整最小逆。

现在定义原源
$$
\boxed{f_{m,q}
=\frac{h_{\rm gap}\otimes\widehat F}{\|\widehat F\|}.}
\tag{5.3}
$$
中间暗对有 $n=q-k$ 个孔，$\widehat F$ 有 $k$ 个孔，故总孔数恰为 $q$。由 (4.6)、(5.1)，$D_mf_{m,q}=0$；由单位暗向量和分母，它的原 Hilbert 范数为一。

## 6. 对原空间每个原像的下界

取任意 $u\in\mathcal H_{q+h}^{(m)}$ 满足 $D_m^hu=f_{m,q}$。先施加 $P_{\rm gap}$，再识别其值域中的单位暗张量因子，最后在远尾施加 $T$。所得向量 $U$ 属于“真实 $k$ 强头加单玻色模”的第 $k+h$ 层，且
$$
\|U\|\le R\|u\|.
\tag{6.1}
$$
由 (4.2)、(5.1)，这个有界映射在每个相关层都与完整删除精确交织。因此
$$
\mathcal L^hU=\frac{F}{\|\widehat F\|}.
$$
§2 已证明测试模型上的该原像唯一，故
$$
U=\frac{G_h}{\|\widehat F\|}.
$$
结合 (3.2)、(4.7)、(6.1)，
$$
\|u\|^2
\ge\frac{\|G_h\|^2}{R^2\|\widehat F\|^2}
\ge(1-\epsilon)e^{-4/(m+k+1)-\theta}
\frac{(k+1)^{\overline h}}{(h!)^2S_J^h}.
$$
对所有原像取最小，得到 (1.5)。源与测试的构造均不依赖 $h$。

对 $h=1$，用 $1-\epsilon\ge3/4$、$1/S_J\ge3J^3$、
$4/(m+k+1)\le1$、$\theta\le1$，得
$$
\|D_m^\dagger f_{m,q}\|^2
\ge\frac9{4e^2}(k+1)J^3
>\frac14(k+1)J^3
>\frac1{16}q^{7/2}.
$$
这里仅用 $e<3$、$k+1>\sqrt q/4$ 和 $J\ge q$。这证明 (1.6)。

## 7. 对实际研究路线的准确限制

对每个固定 $m\ge5$，(1.6) 随 $q\to\infty$ 表明原真正受限单步逆
$$
D_m:\ker D_m^2\cap\mathcal H_{q+1}^{(m)}\to K_q^{(m)}
$$
的最优右逆范数不可能是 $q^{3/2+o(1)}$；其最小原像正是完整 $D_m^\dagger$ 在 $K_q$ 上的限制。这个原尾结论强于“有限异权可能阻止一般尾平方和 gap”的范围说明。

原合法大窗内可取满足 $q\ge\max\{4\cdot2^m,16m^2\}$ 的 $q$，构造仍是原相同 $m,q$。但本文没有证明 $f_{m,q}$ 来自实际 $r_{m,q}(w)$、实际两费用来源图，或本文前两稿中的 $\zeta(r)$。因此它不否定仅在这些真实窄来源上的更强预算。

它也没有给相邻 $\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n$ 的反例。测试模型 §2 的标量阶乘矩本来满足相应凸性；原多步下界 (1.5) 与可能的相邻常数一并不矛盾。无权 $N=M$ 仍未由本稿推出。

### 7.1 这个测试准确只读取已付的真幂底项

把 §6 的“先 $P_{\rm gap}$，再识别暗张量因子，最后施加 $T$”在原第 $q+t$ 层的作用记为 $\mathcal A_t$。它的值域是测试模型第 $k+t$ 层，且由准确交织有
$$
\mathcal L^t\mathcal A_t=\mathcal A_0D_m^t.
$$
若 $u\in\ker D_m^t\cap\mathcal H_{q+t}^{(m)}$，右边为零；而 §2 已证明 $\mathcal L^t$ 从测试模型第 $k+t$ 层到第 $k$ 层是可逆方阵。因此
$$
\boxed{\mathcal A_t|_{\ker D_m^t\cap\mathcal H_{q+t}^{(m)}}=0
\qquad(t\ge1).}
\tag{7.1}
$$
该式可与任意额外原头因子的恒等算子张量，不改变结论。

在[准确真幂底项稿](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)的原第 $t$ 段，出生一输入属于 $W_{t,q+t}\subset\ker D_m^t$，全部高出生输入属于更小的 $\ker D_m^{t-1}$。所以 (7.1) 把它们一并杀掉。对该稿的正交分解 $\mathcal T x=b(r)+\mathcal I\xi$，本测试准确给
$\mathcal A_t(\mathcal T x)_t=\mathcal A_tb_t(r)$。

因此本文的坏绝对 primitive 逆是由已经分离并支付的真幂底项检测出来的。这一测试本身没有检测出生一修正，也没有给实际 $-\mathcal R\mathcal G^\dagger\zeta(r)$ 的高逆费用下界；不能由 (1.6) 推断剩余三 Gram 比较失败。

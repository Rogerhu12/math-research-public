# R271 附录：同一模型源的完整范数比较与原 primitive 十分之十九次幂下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。

状态：**已证明。** 本文在[归一创建行与原八分之十五次幂稿](R271-appendix-normalized-creation-row-and-original-primitive-fifteen-eighths-lower-bound.md)的同一原空间构造上，保留模型源的全部强位坐标，支付原源与模型源的完整范数比，将原单位 primitive 的单步 MP 下界进一步提高到 $q^{19/10}$。这仍是原真幂底项的结论，不是实际高出生修复费用的反例。以下所有逆先在完整物理孔层取最小值。

## 1. 完全相同的原源和准确变权模型

固定 $m\ge5$、$q\ge16m^2$，原尾为
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j.
$$
先允许任意整数 $1\le k\le q$。取最初 $k$ 个强位，中间 $q-k$ 个相邻暗对，以及从
$$
J=m+2q-k
$$
开始的完整无限远尾。记强位权为 $a_i$，$i\in[k]$，远尾平方权为 $z_j=(j+1)^{-4}$、$j\ge J$，并置
$$
S=\sum_{j\ge J}z_j,\qquad
z_*=\max_{j\ge J}z_j=(J+1)^{-4},\qquad
\delta=z_*/S,
$$
$$
\vartheta=S(m+k)^4,\qquad
\kappa=k\delta.
\tag{1.1}
$$
本节的一般比较假设 $\kappa<1$；最后的原参数选择会明确支付它。

用 $e_r=e_r((z_j)_{j\ge J})$ 表示远尾初等对称和，用
$$
E_s=e_s((a_i^{-2})_{i\in[k]})
$$
表示强位倒数平方权的对称和；二者不能混同。仍置 $e_0=E_0=1$。

前稿的原远尾单位创建向量为
$$
u_r=e_r^{-1/2}\sum_{|L|=r}\sqrt{z_L}\,|L\rangle.
$$
其准确归一创建行 $T_r v=\langle u_r,v\rangle\mathbf e_r$ 满足
$$
\|T_r\|=1,\qquad T_{r-1}D_J=c_rT_r,
\qquad c_r=r\sqrt{e_r/e_{r-1}}.
\tag{1.2}
$$
前稿在原强位和远尾上直接构造
$$
F_k=\sum_{I\subseteq[k]}(-1)^s
\frac{(k-s)!}{k!}\,a_I^{-1}|I\rangle\otimes D_J^s u_k,
\qquad s=|I|.
\tag{1.3}
$$
它准确满足 $(D_{\rm hd}+D_J)F_k=0$。张量中间单位暗态 $h_{\rm gap}$ 后得到原 $q$ 孔 primitive
$$
\widetilde f=F_k\otimes h_{\rm gap},\qquad
f=\widetilde f/\|F_k\|.
\tag{1.4}
$$
张量顺序按原强位、中间位、远尾读取。

前稿已经逐项证明的暗对斜投影及 (1.2) 给分析映射
$$
\mathcal A_t:\mathcal H_{q+t}^{(m)}
\longrightarrow\mathcal H_{k+t}^{\rm model},
\qquad
\|\mathcal A_t\|\le R=e^{2/(m+k+1)},
$$
$$
\mathcal A_{t-1}D_m=\mathcal L\mathcal A_t,\qquad
\mathcal L=D_{\rm hd}+C,\quad C\mathbf e_r=c_r\mathbf e_{r-1}.
\tag{1.5}
$$
它在整个原层上成立，不只在创建像上成立。原未选位的费用已包含在 $R$ 中。

同一个未归一源的模型像为
$$
\omega_k=\mathcal A_0\widetilde f
=\sum_{I\subseteq[k]}(-1)^s\frac{(k-s)!}{k!}a_I^{-1}
\left(\prod_{r=k-s+1}^{k}c_r\right)
|I\rangle\otimes\mathbf e_{k-s}.
\tag{1.6}
$$
模型次数 $k+t$ 在 $t\ge0$ 时有完整 $2^k$ 个强位标签；对 $t\ge1$，$\mathcal L$ 在相邻两层之间是具有严格正对角的可逆三角方阵。以下不把模型逆认成原 MP 逆，只通过 (1.5) 测试任意原像。

## 2. 原源与模型源的准确分组权

按强位孔数 $s$ 对 (1.3) 和 (1.6) 作正交分组。记对应平方范数分别为 $W_s$、$w_s$。由 $c_r$ 的准确乘积，
$$
\boxed{
w_s=E_s\,\frac{e_k}{e_{k-s}},\qquad
Z(x)=\sum_{s=0}^k w_sx^s,\qquad
\|\omega_k\|^2=Z(1).
}
\tag{2.1}
$$
特别 $w_0=1$。原分组则是
$$
W_s=\left(\frac{(k-s)!}{k!}\right)^2
E_s\,\|D_J^su_k\|^2,
\qquad
\|F_k\|^2=\sum_{s=0}^kW_s.
\tag{2.2}
$$

下面直接计算 $\|D_J^su_k\|^2$ 相对于其归一创建行的比例，而不分别将两个量与固定玻色权比较。对 $|L|=k-s$，
$$
(D_J^su_k)_L
=\frac{s!}{\sqrt{e_k}}\sqrt{z_L}\,
e_s((z_j)_{j\notin L}).
\tag{2.3}
$$
这来自每个新增的 $s$ 元集恰有 $s!$ 个删除次序。

在 $(k-s)$ 元集上取概率
$$
\mathbb P(L)=z_L/e_{k-s},
\qquad
b_L=e_s((z_j)_{j\notin L}).
$$
按并集为 $k$ 元集计数，准确有
$$
\mathbb E b_L=\binom{k}{s}\frac{e_k}{e_{k-s}}.
\tag{2.4}
$$
由 (2.3) 及 (1.2)，
$$
\boxed{
\frac{W_s}{w_s}
=\frac{\mathbb E b_L^2}{(\mathbb E b_L)^2}.
}
\tag{2.5}
$$
$s=0$ 时按恒等值一读取。由于 $b_L\le e_s$，
$$
\frac{W_s}{w_s}
\le
\frac{e_s e_{k-s}}{\binom{k}{s}e_k}.
\tag{2.6}
$$

对远尾对称和，准确计数给
$$
(r+1)e_{r+1}
=\sum_{|L|=r}z_L\sum_{j\notin L}z_j
\ge(S-rz_*)e_r.
\tag{2.7}
$$
假设 $k\delta<1$，将 (2.7) 从 $r=k-s$ 迭代到 $k-1$，再用 $e_s\le S^s/s!$，得到
$$
\boxed{
1\le\frac{W_s}{w_s}
\le(1-k\delta)^{-s}.
}
\tag{2.8}
$$
下界也直接来自 (2.5) 的方差非负。定义
$$
a=(1-k\delta)^{-1}\ge1.
$$
于是
$$
\boxed{Z(1)\le\|F_k\|^2\le Z(a).}
\tag{2.9}
$$
这保留了完整模型源的范数；不再只将它的一个坐标与原源范数比较。

## 3. 强位组合数支付全部源的额外损失

因为强位倒数平方权均不超过 $(m+k)^4$，
$$
\frac{E_{s+1}}{E_s}
\le\frac{k-s}{s+1}(m+k)^4.
$$
远尾对称和又满足
$$
\frac{e_{k-s}}{e_{k-s-1}}\le\frac{S}{k-s}.
$$
代入 (2.1)，对 $0\le s<k$ 得
$$
\boxed{(s+1)w_{s+1}\le\vartheta w_s.}
\tag{3.1}
$$
因此 $x\ge0$ 时 $Z'(x)\le\vartheta Z(x)$。从 $1$ 积分到 $a$ 得
$$
\frac{Z(a)}{Z(1)}\le e^{\vartheta(a-1)}.
$$
结合 (2.9)，得到本稿主要的源比较
$$
\boxed{
\|\omega_k\|^2\le\|F_k\|^2
\le e^\Lambda\|\omega_k\|^2,\qquad
\Lambda=\frac{\vartheta k\delta}{1-k\delta}.
}
\tag{3.2}
$$
同时由 $Z'(1)\le\vartheta Z(1)$，
$$
\boxed{\sum_{s=0}^k s\,\frac{w_s}{Z(1)}\le\vartheta.}
\tag{3.3}
$$

源比较中的指数从前稿单坐标估计的 $\vartheta$ 变成
$\Lambda=\vartheta k\delta/(1-k\delta)$。这里没有减去尚未支付的误差：改进来自准确保留 (2.1) 的全部坐标，以及 (2.5) 的真实导数方差。

## 4. 真幂模型逆的每个强位坐标

前稿给有限负二项式展开
$$
\mathcal L^{-h}
=\sum_{t=0}^{k}(-1)^t\binom{h+t-1}{t}
C^{-(h+t)}D_{\rm hd}^{t},\qquad h\ge1.
\tag{4.1}
$$
本节保留其全部输出坐标。对固定强位标签 $I$、$|I|=s$，只有原标签 $I\cup J$、$J\subseteq[k]\setminus I$ 对该坐标有贡献。若 $|J|=t$，删除系数为 $t!a_J$；将 (1.6) 代入，强位权、符号及相关 $c_r$ 逐项抵消。对全部 $J$ 求和后使用
$$
\sum_{t=0}^{k-s}\binom{h+t-1}{t}
=\binom{h+k-s}{k-s},
$$
得到
$$
\boxed{
(\mathcal L^{-h}\omega_k)_I
=(\omega_k)_I\,
\frac{\binom{k-s+h}{k-s}}
{c_{k-s+1}\cdots c_{k-s+h}}
=\frac{(\omega_k)_I}{h!}
\sqrt{\frac{e_{k-s}}{e_{k-s+h}}}.
}
\tag{4.2}
$$
其中标量模次数由所在层确定。所有强位标签正交，故
$$
\boxed{
\|\mathcal L^{-h}\omega_k\|^2
=\frac1{(h!)^2}\sum_{s=0}^{k}
w_s\frac{e_{k-s}}{e_{k-s+h}}.
}
\tag{4.3}
$$

迭代 $(r+1)e_{r+1}\le Se_r$，
$$
\frac{e_{k-s}}{e_{k-s+h}}
\ge\frac{(k-s+1)\cdots(k-s+h)}{S^h}.
\tag{4.4}
$$
若 $\vartheta<k+1$，(3.3) 给加权平均
$\mathbb E(k-s+1)\ge k+1-\vartheta>0$。函数
$$
x\longmapsto x(x+1)\cdots(x+h-1)
$$
在 $x\ge0$ 上单调且凸：它是具有非负系数的多项式，$h=1$ 时是仿射函数。因此 Jensen 不等式与 (4.3)–(4.4) 给
$$
\boxed{
\|\mathcal L^{-h}\omega_k\|^2
\ge
Z(1)\,
\frac{(k+1-\vartheta)\cdots(k+h-\vartheta)}
{(h!)^2S^h}.
}
\tag{4.5}
$$

## 5. 同一个原单位源的全部真幂下界

取任意原像 $v\in\mathcal H_{q+h}^{(m)}$、$D_m^hv=f$。由 (1.5)，
$$
\mathcal L^h\mathcal A_hv=\omega_k/\|F_k\|.
$$
模型真幂可逆，故
$$
R^2\|v\|^2
\ge\frac{\|\mathcal L^{-h}\omega_k\|^2}{\|F_k\|^2}.
$$
使用 (3.2)、(4.3) 得准确可用的一般界
$$
\boxed{
\left\|(D_m^h|_{\mathcal H_{q+h}^{(m)}})^\dagger f\right\|^2
\ge
\frac{e^{-\Lambda-4/(m+k+1)}}{(h!)^2Z(1)}
\sum_{s=0}^{k}w_s\frac{e_{k-s}}{e_{k-s+h}}.
}
\tag{5.1}
$$
若再有 $\vartheta<k+1$，则
$$
\boxed{
\left\|(D_m^h|_{\mathcal H_{q+h}^{(m)}})^\dagger f\right\|^2
\ge
e^{-\Lambda-4/(m+k+1)}
\frac{(k+1-\vartheta)\cdots(k+h-\vartheta)}
{(h!)^2S^h}.
}
\tag{5.2}
$$
这里每个 $h$ 使用 (1.4) 的同一个真实单位源。没有把 sequential MP 与真幂 MP 交换，也没有假定原逆与分析映射交换。

## 6. 原 $q^{19/10}$ 下界的统一参数

现在取
$$
\boxed{k=\lfloor q^{4/5}/4\rfloor.}
\tag{6.1}
$$
由 $q\ge16m^2$，有 $k\ge m$、$k\le q/4$ 和
$k+1>q^{4/5}/4$。于是
$$
J\ge7q/4,\qquad m+k\le2k.
$$
直接积分比较给
$$
S\le\frac1{3J^3},\qquad
S\ge\frac1{3(J+1)^3},\qquad
\delta\le\frac3{J+1}.
\tag{6.2}
$$
因此
$$
k\delta<\frac37<1,
$$
以及
$$
\frac{\vartheta}{k}
\le\frac{16k^3}{3J^3}
\le\frac{16}{1029}<\frac1{64}.
\tag{6.3}
$$
特别 $\vartheta<k+1$，(5.2) 的全部条件都成立。

对源比较指数，
$$
\Lambda
=\frac{k(m+k)^4z_*}{1-k\delta}
\le\frac{28k^5}{(J+1)^4}
\le\frac1{343}.
\tag{6.4}
$$
最后一步用
$k^5\le q^4/4^5$ 和 $J\ge7q/4$。再由 $m+k+1\ge11$，
$$
\Lambda+\frac4{m+k+1}
\le\frac1{343}+\frac4{11}<\frac12<\log2.
\tag{6.5}
$$
在 (5.2) 取 $h=1$，并用
$k+1-\vartheta\ge(63/64)(k+1)$，得到
$$
\begin{aligned}
\|D_{m,q+1}^{\dagger}f\|^2
&\ge\frac{k+1-\vartheta}{2S}\\
&>\frac{63}{64}\frac{q^{4/5}}8\,
3\left(\frac{7q}{4}\right)^3\\
&=\frac{64827}{32768}q^{19/5}
>q^{19/5}.
\end{aligned}
$$
因此
$$
\boxed{\|D_{m,q+1}^{\dagger}f\|\ge q^{19/10}.}
\tag{6.6}
$$
这排除原整个 primitive 源空间上统一的
$q^{19/10-\epsilon}$ 上界，其中 $m$ 固定、$\epsilon>0$ 固定。原合法边界窗口若还要求 $q\le e^{d^3/4}$，(6.6) 当然可限制到该窗口与上述下限的交集；没有更换 $D_m$ 或物理尾权。

## 7. 与尚未支付的实际高返回严格区分

仍与前稿一样，对 $u\in\ker D_m^h\cap\mathcal H_{q+h}^{(m)}$，(1.5) 与模型方阵的可逆性给
$$
\mathcal A_hu=0.
$$
所以这个更强的全坐标分析仍消去整个真幂零空间。它只是更有效地读取同一个原源的真幂最小原像，不读取与这些底项正交的出生一修正。

本文的 $q^{19/10}$ 不是实际
$S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)$
的下界，也没有证明所造 $f$ 来自原 $M$ 图或最优 Schur 的窄来源。普通 ISP、无权 $N=M$、相邻 primitive Gram 常数及实际高链源费用仍需继续。

本稿完成的是 (3.2) 的原源/完整模型源比较，以及由它推出的同源全阶 (5.1)–(5.2) 和原 $q^{19/10}$ 下界。所有范数、斜投影成本和强位组合数均保留在原 Hilbert 空间中。

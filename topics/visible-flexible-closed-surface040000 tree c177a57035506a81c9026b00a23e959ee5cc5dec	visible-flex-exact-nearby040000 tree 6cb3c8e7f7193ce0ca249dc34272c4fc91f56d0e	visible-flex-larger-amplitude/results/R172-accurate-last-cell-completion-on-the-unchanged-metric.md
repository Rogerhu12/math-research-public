# R172：在同一准确度量上的显式末格补全

## 1. 结论及其准确作用域

[R171](R171-accurate-radial-profile-and-one-sided-Arb-jets.md) 的准确相位积分定义物理总长 $S$，而当前有限数组最后保存的 binary64 数是数值端点标签 $E$。对第 27 轮接受态，$S-E$ 严格约为 $1.18734\times10^{-15}$。二者不能在完整区间覆盖中当成相等。

本结果给出一个**明确的新有限场定义**。它保留全部保存系数、中央及尾参数、七个物理 bumps 和准确目标度量

$$
g=ds^2+a_\delta(s)^2du^2,\qquad 0\le s\le S,
$$

只在最后一个 raw P1 单元内改变原 raw 与标量尾权的坐标输入。尾部半径和 Gauss 曲率始终在物理坐标 $s$ 上取值。新的末格与前片连续，完整 cut 值准确等于 R132 的平尾，包含所有零曲率角弧。内部导数由明确链式公式给出。

这不是对旧有限场逐值相同的声明，也不把旧 F、normal、实际 body、两 jet 拼接或全域误差直接转给新表示。原数组未改写；新表示有独立 schema 和内容绑定。本文只完成末端定义及其区间消费者，并未证明一个强目标闭曲面。

## 2. 输入与全部保护条件

绑定不可变输入 `notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz`，SHA256 为

`2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f`。

它含 131 个 P1 节点、31 个中央参数、16 个尾参数和 7 个物理参数。令 $b$ 为倒数第二个保存节点。$b,E$ 按其准确二进有理数解释，显示值为

$$
b=1.4873481783581288\ldots,\qquad
E=1.4889731783581288\ldots,\qquad E-b>0.00162499999999998.
$$

R171 的同一输入包提供准确 $S$，并严格包围 $S-b>0$。原末行 raw 系数逐个等于零。整个末格都在准确最后一片 phase bridge 内，且严格位于以下所有结束点之后：

- 原中央 seed 的支持；
- 冻结 coast reference 与 R153 窗；
- 全部七个物理 bump 的支持；
- 原角图 blend 和 R149 atlas 的 exit transition；
- R155 terminal ramp。

因此本格的角图准确是 $u=\xi$，seed/coast/bump 项为零，R155 权重为一。以上均由保存的完整定义比较，不能由文件名推断。

令 $r_0(u)=(r_n,r_m,r_l)$ 为第 $b$ 行保存 Fourier 多项式。原末格 raw 为

$$
r_{\rm old}(x,u)=\frac{E-x}{E-b}r_0(u),\qquad b\le x\le E.
\tag{1}
$$

原数值尾权使用两个实际运算结果

$$
e_t=\operatorname{binary64}(.42E),\qquad
L_t=\operatorname{binary64}(.58E).
$$

新消费者将这两个保存运算结果按准确 dyadic 常数记录。对本次输入，准确整数有理运算验证 $e_t+L_t=E$，而非仅使用十进制 $.42+.58=1$。定义原标量函数

$$
\eta(x)=S_5\!\left(\frac{x-e_t}{L_t}\right),\qquad
S_5(z)=10z^3-15z^4+6z^5
\tag{2}
$$

并在 $z\le0,z\ge1$ 分别截为 $0,1$。所以 $\eta(E)=1$。如果未来输入不满足上述准确等式，本版本直接拒绝，不偷偷改变权或忽略端点差。

## 3. 只移动 raw/权的末格参数

设

$$
t=\frac{s-b}{S-b},\qquad
\sigma(s)=b+(E-b)t,\qquad b\le s\le S.
\tag{3}
$$

在 $s\le b$ 保留原准确有限场；在末格定义

$$
\widehat r(s,u)=(1-t)r_0(u)=r_{\rm old}(\sigma(s),u),
\qquad \widehat\eta(s)=\eta(\sigma(s)).
\tag{4}
$$

R132 的尾函数仍采用准确物理常数

$$
a_c=4/5,\qquad c=17/50,\qquad w=23/50,
$$

以及原 16 个 dyadic 控制。对 $q=(|y|-c)/w$，令

$$
\kappa(y)=\frac{630}{w}q^4(1-q)^4\sum_{j=0}^{15}b_jB_j^{15}(q)
\tag{5}
$$

在 $0<q<1$ 内取此式，区间外为零。本轮参数的准确有理比较给 $0\le b_j\le6/5$，所以 $\kappa\ge0$ 且 $\kappa\le4725/736$。公式有端点四阶零点，$\kappa$ 至少为 $C^3$ 函数；此处不要求其第四导跨端点共同。

定义真实 current-radius 尾形状三元组

$$
T(a,u)=\kappa(a\sin u)
(\cos^2u,-\sin u\cos u,\sin^2u).
\tag{6}
$$

新完整 affine 背景是

$$
B(s,u)=\widehat r(s,u)+\widehat\eta(s)T(a_\delta(s),u).
\tag{7}
$$

**半径是 $a_\delta(s)$，不是 $a_\delta(\sigma(s))$。** 后一种替代一般使 cut 半径等于 $a_\delta(E)$，不能推出准确 $4/5$ 平尾迹。

对 $B=(N,M,L)$，在本格取 R155 的正 trace 变换

$$
d=N-L,\quad h=\sqrt{d^2+4M^2+4K_\delta(s)},
\qquad
(n,m,l)=\left(\frac{h+d}{2},M,\frac{h-d}{2}\right),
\tag{8}
$$

其中 $K_\delta(s)=-a_{\delta,ss}(s)/a_\delta(s)$ 是同一准确度量的曲率。当前末 phase bridge 的两个端相位导数均为零，起相位为准确保存的 $-1.45$ dyadic，终相位为 $-\pi/2$。因此相位是二者间的三次单调桥：严格内部 $\phi_s<0$ 且 $\cos\phi>0$，所以 $K>0$，cut 有 $K=0$。严格内部若使用一般平方根导数，消费者另外要求盒上 $h>0$。准确 cut 使用下一节的真实尾迹接口。

这不是把物理度量拉回到 $\sigma$。若作那种拉回，会产生 $\sigma_s^2ds^2$；本文没有这个因子，也没有声称 (7) 是旧位置图的重参数化。它是同一物理度量上的新有限二基本形式候选。其 Codazzi 缺陷仍要真实支付。

## 4. 连续接缝、准确 Gauss 和 cut 值

在 $s=b$，有 $\sigma(b)=b$、$t=0$，所以 (7) 与前片完整 affine 值及所有存在的角向导数共同。目标 profile 和 R155 变换亦共同，故完整 II 值连续。raw 的径向斜率可以在此改变；这不增加原构造中没有的全局 $C^1$-II 或 $C^3$ 曲面要求。

在 $s=S$，

$$
\widehat r=0,\quad\widehat\eta=1,\quad
a_\delta=4/5,\quad K_\delta=0.
$$

于是 $B=T(4/5,u)$。由 (6)，$N+L=\kappa\ge0$ 且 $NL-M^2=0$，从而 $h=N+L$，(8) 准确返回原尾 $T$。即使 $\kappa=0$，结论仍成立，不需要除以 $n$ 或赋给零平方根一个虚构导数。

内部的完整 Gauss 恒等式为

$$
nl-m^2=\frac{h^2-d^2}{4}-M^2=K_\delta(s).
\tag{9}
$$

因为 $h\ge|d|$，$n,l\ge0$。这些都是本格表示恒等式，不代替 Codazzi、实际标架或位置的误差分析。

从 (4)、准确 profile 连续性及 (5)–(8) 的连续运算，$(n,m,l)$ 在整个闭末格连续，cut 值在全角上统一趋于 $T(4/5,u)$。证明可直接用紧致性及向量范数的连续性；不以 $h$ 的严格正下界延拓到 cut。

准确 cut 的角一、二导由 $T(4/5,u)$ 本身求导。本文不将其自动称为任意 P1 输入的内部 $II_{uu}$ 一致极限，也不给 cut 指派 $E_s=0$。实际位置图的角两导极限、接合相等以及 R126 修复须另由真实 body 消费。

## 5. 全部内部 jet 与区间覆盖

从 (3) 得准确常数

$$
\sigma_s=\frac{E-b}{S-b},\qquad
\widehat r_s=-\frac{r_0}{S-b},\qquad
\widehat\eta_s=\eta'(\sigma)\sigma_s.
$$

对 (7) 分别按 $s,u,u^2,su$ 使用乘积和链式法则，半径项消费准确 $a_s$；(8) 的径向导数消费同一准确 $K_s$。因 $u=\xi$，不遗漏角图漂移，也不额外引入 $\sigma_s a_s$。所需的 $\kappa_y,\kappa_{yy}$ 来自同一个分段多项式；跨 $|y|=c,c+w$ 的盒并包所有可能分支，包括零支。

`scripts/fd2d_gc_accurate_last_cell.py` 提供 `AccurateLastCell`：

- `coordinates(t0,t1)` 同时包围准确物理 $s$、原参数 $\sigma$ 和 $\sigma_s$；
- `raw_box` 包含全部 31 模及其真实 $s,u,uu,su$ 导数；
- `weight_box` 包含 (2)–(4) 的真实值和径向导数；
- `profile_box` 调用 R171 准确末片，按归一片区间覆盖准确 $S$；
- `box` 组合 (7)–(8)，内部返回完整五 jet；准确 cut 只返回真实尾的角两 jet。

输入 $t_0,t_1$ 是准确有理数，故最后端点可用命名值 $t=1$，无需把准确 $S$ 舍入为某个新的 binary64 节点。原数组保持不可变，新表示的完整内容身份同时绑定其 SHA、R171 包、源及数学坐标规则。遇到包含退化 cut 的一般平方根导数盒，会明确返回待分片状态；不会以单点端值冒整个盒的导数界。

## 6. 与旧 raw/权坐标的统一定量比较

本节比较的是**同一准确 profile 和同一 R132 尾函数**下，末格采用原 raw/权坐标 $s$ 或新坐标 $\sigma(s)$ 所得的两个数学字段。它不比较旧 binary64 Gauss 程序和准确 profile，也不转移旧程序观测。

记 $\varepsilon=|S-E|$、$L=S-b$，在共同物理区间 $[b,\min(E,S)]$ 上，$|\sigma(s)-s|\le\varepsilon$。若 $C_{j,k}$ 是第 $j$ 个 raw 分量的各 Fourier 系数绝对值乘频率 $k$ 次幂之和，则

$$
\|\partial_u^k(\widehat r_j-r_{{\rm old},j})\|_\infty
\le \frac{\varepsilon}{L}C_{j,k},\qquad k=0,1,2.
\tag{10}
$$

证明：两者差的系数为

$$
(s-b)\left(\frac1{E-b}-\frac1{S-b}\right)c_j.
$$

若 $S\ge E$，用 $s-b\le E-b$ 得 (10)；若 $S<E$，用 $s-b\le S-b$ 得更小的 $\varepsilon C_{j,k}/(E-b)$，仍被 (10) 包住。三角函数各阶导数的绝对值不超过对应频率幂，故覆盖所有角度。

又因为 $S_5'(z)=30z^2(1-z)^2$，全局 Lipschitz 常数为 $15/8$，

$$
\|\widehat\eta-\eta\|_\infty\le\frac{15\varepsilon}{8L_t}.
\tag{11}
$$

把三元组识别为对称矩阵 $\left(\begin{smallmatrix}n&m\\m&l\end{smallmatrix}\right)$。令 $C_n,C_m,C_l$ 为 $k=0$ 的三项和，(6) 的 Frobenius 范数是 $\kappa$，所以

$$
\|\Delta B\|_F\le
\frac{\varepsilon}{L}\sqrt{C_n^2+2C_m^2+C_l^2}
+\frac{15\varepsilon}{8L_t}\frac{4725}{736}=:\mathcal E_B.
\tag{12}
$$

在相同 $K\ge0$ 上，(8) 的变换 $\Pi_K$ 是全局 $\sqrt2$-Lipschitz（Frobenius 范数）。事实上，记 $v=(d,2m)$，则 $h=|(v,2\sqrt K)|$，范数反三角不等式给 $|\Delta h|\le|\Delta v|$；进而

$$
\|\Delta\Pi_K\|_F^2
=\frac{(\Delta h)^2+(\Delta d)^2+4(\Delta m)^2}{2}
\le (\Delta d)^2+4(\Delta m)^2
\le2\|\Delta B\|_F^2.
$$

因此全角完整 II **值**的变化界为 $\sqrt2\mathcal E_B$，在退化点仍有效。它不是 II 所有导数、metric、reach 或实际曲面距离的误差界。对应全导数若被后验消费，仍按第 5 节对新完整场直接包围。

## 7. 可复现交付

主消费者为 `scripts/fd2d_gc_accurate_last_cell.py`，有限独立核为 `scripts/fd2d-accurate-last-cell-check.py`。输入绑定当前 2b 接受态及 R171 的 `metric-r136-arb-profile-01-packet.json.gz`。实际执行结果、源码 SHA、命名定义、独立标量比较和端点差界在本结果对应 closed manifest 中逐项记录；完整证明不依赖有限采样。

原保存字段和 profile 包保持原字节。后续消费必须明确选择本 schema，不能把它冒称旧 native 的同值重载或原 BVP 的再次收敛。真实完整核、全域误差、同一几何加密和强幅度条件仍继续支付。

### 本轮真实执行

独立核 `3939 / 54a8a1 → 514168` 自然退出 0，实耗 47.659609519 秒，峰值 RSS 105872 KiB。4 个内部或单侧端点的全部五 jet 与 4 个准确 cut 点的角两 jet 共 96 项，均包含独立 80 位 mpmath 相位反积分/微分得到的标量。它们是有限实现检查，连续包围由前文的准确区间运算与 R171 余项承担。

本次式 (12) 后的完整正 trace II 值比较界严格小于 $2.427632\times10^{-12}$，覆盖共同末格的全角；比较双方使用同一个准确 $g$ 和 R132 尾函数。没有执行 whole F/J、非线性 BVP、frame 或 body，也没有将这个 II 值界冒称 metric 或曲面距离界。

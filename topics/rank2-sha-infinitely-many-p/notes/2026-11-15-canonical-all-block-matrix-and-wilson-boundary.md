# 原全部中央块的固定四行矩阵与第二 forcing 的规范边界

日期：2026-11-15。**状态：显示接口与规范恒等式已证明；指定残差消去与非消失未证明。** 此 note 不登记新增中央零。它把 R595 的固定矩阵付到全部真实系数块，并明确 R606、R609、R619、R622 联用后仍保留的量。

## 1. 同一个原参数中的全块精确恒等式

保持 $p=6s-1>71$、$d=p+1$、$w=z^6$、$t=bu^6$、$z=uH(t)$ 和
$C=(1+t)^{-1/2}$。允许原 R606 的 $c'-c\in\mathcal O$，置
$$
\Lambda=K(t)\exp\{-6c'b^{-s}t^sH(t)^d\},
\qquad K=(\sigma(z(u))/u)^6.
\tag{1}
$$
所以 $\Lambda_0=1,\Lambda_1=-2/5$。这里 (1) 是特征零的同一个真实 sigma 来源，不只指模 $p$ 有限连接。

对 $h\ge1$ 令 $n_h=hs-1$。定义实际系数
$$
g_{m,h}=[w^{hs}](A_m e^{-mc'w^s}),\quad m=34,72,
$$
$$
d_{4,h}=[w^{n_h}](z^{-4}f_4e^{-6c'w^s}),\qquad
d_{1,h}=[w^{n_h}](z^{-1}f_1e^{-6c'w^s}).
\tag{2}
$$
同一留数变元逐项给
$$
b^{-n_h}g_{m,h}
=[t^{n_h}]\Lambda^{m/6}P_m C H^{-hd-1},
$$
$$
b^{-n_h}d_{4,h}
=[t^{n_h}]\Lambda C H^{1-hd},\qquad
b^{-n_h}d_{1,h}
=[t^{n_h}]\Lambda H^{4-hd}.
\tag{3}
$$
各幂在特征零按 (1) 定义。式 (3) 保全部 $H^{-hp}$，没有使用 $\bar H^p=1$；因此不把 $h\le5$ 的旧窗口外推。

令
$$
\Lambda_h^-=\sum_{j=0}^{n_h-2}\Lambda_jt^j,\qquad a=m/6.
$$
因 $n_h\ge3$，在 $[t^{n_h}]$ 中两个被删尾项的乘积不贡献。一次项只读取常数和一次系数，故最后两系数的完整消元准确给
$$
\boxed{
\begin{pmatrix}g_{34,h}\\g_{72,h}\end{pmatrix}
=\mathsf M
 \begin{pmatrix}d_{4,h}\\d_{1,h}\end{pmatrix}
+\mathbf R_h\qquad(h\ge1),
}
\tag{4}
$$
其中 $\mathsf M$ **就是** R595 的固定有理矩阵
$$
\mathsf M=
\begin{pmatrix}
17\cdot503/45&-17\cdot488/45\\
12\cdot1472/5&-12\cdot1467/5
\end{pmatrix},\qquad
\det\mathsf M=-266084/15.
\tag{5}
$$
完整余项为
$$
\boxed{
R_{m,h}=b^{n_h}[t^{n_h}]
\left\{
(\Lambda_h^-)^{m/6}P_m C H^{-hd-1}
-M_{m4}\Lambda_h^-C H^{1-hd}
-M_{m1}\Lambda_h^-H^{4-hd}
\right\}.
}
\tag{6}
$$
它只使用 $\Lambda_{\le n_h-2}$ 及原固定 $C,H,P_m$，但这些都是实际原系数，不能自由调整。

为核 (5) 不依赖 $h,p$，写 $H_1=-1/14,C_1=-1/2$。两个 forcing 权的一次系数差为
$$
C_1+(1-hd)H_1-(4-hd)H_1=C_1-3H_1=-2/7.
$$
而原 $m$ 行与 $a$ 倍第二 forcing 的差为
$$
a\{(a-1)(-2/5)+(P_m)_1+C_1-5H_1\}.
$$
这里 $hd$ 完全相消。代 $(P_S)_1=-53/7$、$(P_T)_1=-557/7$，得到
$$
M_{34,4}=(17/3)(503/15),\qquad
M_{72,4}=12(1472/5),\qquad M_{m,1}=m/6-M_{m,4}.
$$
所以 (4) 是全部 $h$ 的特征零精确式，强于仅在第一块省掉 $H^p$ 后比较。

## 2. 同一完整 Newton 的真实全尾分解

R618 对所有显示的 Gaussian 余项给
$$
v_p(g_{m,h}),\ v_p(d_{\ell,h})
\ge-\lfloor6(hs-1)\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}.
$$
固定矩阵 (5) 在当前素数处整，所以 (4) 对 $R_{m,h}$ 给相同下界。因 $d\tau_2<1$，下列全部级数收敛：
$$
\mathfrak D_\ell^{(m)}
=\sum_{h\ge1}(-1)^{h-1}(h-1)!(mc')^{-h}d_{\ell,h},
$$
$$
\mathfrak R_m
=\sum_{h\ge1}(-1)^{h-1}(h-1)!(mc')^{-h}R_{m,h}.
$$
因此原完整导数准确为
$$
\boxed{
j_m=M_{m4}\mathfrak D_4^{(m)}
    +M_{m1}\mathfrak D_1^{(m)}+\mathfrak R_m.
}
\tag{7}
$$
R606 已支付此处 $j_m$ 不因 $c'-c$ 改变。

$\mathfrak D_\ell^{(m)}$ 的分子是原 charge 六来源，但分母是 $mc'$。没有把它认作原普通负矩 $I_4,I_1$，也没有把它冒认为分母 $6c'$ 的同一个 Newton 中央。式 (7) 仍保整个非线性原残差。

## 3. 第二块与 R609 三个二次行的区别

记
$$
\mathbf c=(d_{4,1},d_{1,1})^t,\quad
\mathbf d_2=(d_{4,2},d_{1,2})^t,\quad
\mathbf a=(g_{34,1},g_{72,1})^t,
$$
并在本节模 $p$ 读取。改变 $c'$ 为 $c'+\eta$ 时，完整原指数乘法给
$$
\boxed{
\mathbf d_2\longmapsto\mathbf d_2-6\eta\mathbf c,\qquad
g_{m,2}\longmapsto g_{m,2}-m\eta a_m.
}
\tag{8}
$$
而 $\mathbf c$、R609 的三个 $Q_{44},Q_{41},Q_{11}$ 及首块 $\mathbf R_1$ 均不变：它们只读 Gaussian 首次出现之前的真实窗口。

结合 (4)，第二残差的准确改变是
$$
R_{m,2}\longmapsto
R_{m,2}+(6-m)\eta(\mathsf M\mathbf c)_m-m\eta R_{m,1}.
\tag{9}
$$
若原首层 $\mathbf a=0$，则 $\mathsf M\mathbf c=-\mathbf R_1$，(9) 压成
$$
\boxed{\mathbf R_2\longmapsto\mathbf R_2-6\eta\mathbf R_1.}
\tag{10}
$$
因此 (8) 与 (10) 正好配平，使原第二中央行保持。不能只移动 $\mathbf d_2$ 而保旧 $\mathbf R_2$。

特别，从对 $\eta$ 不变的三个 $Q$ 和首层约束中，不能自动读出整个 $\mathbf d_2$；当 $\mathbf c\ne0$ 时，(8) 仍有一个真实剪切方向。固定 R606 的规范 $c^\dagger$ 可以选择该方向，但它不提供删除 $\mathbf R_2$ 的等式。

一个确实不受 (8) 改变的量是
$$
\mathfrak D_p=\det(\mathbf c,\mathbf d_2).
\tag{11}
$$
本 note 没有证明它非零或把它化为 R609 三个 $Q$。

## 4. 两原完整中央同时零真正留下的第二关系

在 R606 的规范 Gaussian 中，令
$$
\mathbf q=\overline{\mathbf a/p},\qquad
C_*=\overline{b^sC_s},\qquad
\mathsf D=\operatorname{diag}(34,72).
$$
这里 $\mathbf q$ 只在首层 $\mathbf a=0$ 时定义，且是原实际一次除 $p$ 商。R606 的 $H^{-p}$ log 项仍包含在该实际商中。

如果原两个完整 $j_m$ 都为零，那么 (4) 及 R606 的两条 $\Xi=0$ 准确给
$$
\boxed{
\mathbf c=-\mathsf M^{-1}\mathbf R_1,\qquad
\mathbf d_2=-\mathsf M^{-1}
       (\mathbf R_2+C_*\mathsf D\mathbf q).
}
\tag{12}
$$
因此
$$
\boxed{
\mathfrak D_p
=(\det\mathsf M)^{-1}
 \det(\mathbf R_1,\mathbf R_2+C_*\mathsf D\mathbf q).
}
\tag{13}
$$
所有量来自同一原 sigma；没有把 $\mathbf q$ 或 $\mathbf R_h$ 当作自由目标列。式 (13) 明确指出下一实际不变量的对象，尚未说明其两边不可能相等。

另一方面，R609 在同一假设下仍只给
$$
a^6(Q_{11}-3bQ_{44})+18b\,a^3Q_{41}
=\frac54a+162b^s e_1^t\mathsf M^{-1}
 \begin{pmatrix}R^{\rm red}_{34,1}\\R^{\rm red}_{72,1}\end{pmatrix},
\qquad a=6pc.
\tag{14}
$$
这里 $R^{\rm red}_{m,1}=b^{-(s-1)}R_{m,1}$ 是 R595 除去 $b^{s-1}$ 后的第一残差，与 (7) 的完整 Newton 残差 $\mathfrak R_m$ 分开。单位 $5a/4$ 不能使整个右边自动为单位；(13) 也没有令左侧三个 $Q$ 消失。

## 5. 第二 Gaussian 不增加第二类约束

R622 的完整权满足 $\mathcal W_k\equiv1\pmod{p^{p-1}}$，故其首改变量在 $j_m$ 的精度 $p^p$ 才出现。R606 的 $\Xi$ 是 $j_m/p^2\bmod p$，在当前 $p>71$ 范围不受该高精度改变。

原完整 $j_m=0$ 已迫 $\bar g_{m,1}=0$，所以 R619/R622 的第一第二块修正又准确升入 $p^{p+1}$。把该修正重新代入 $\Xi$ 只是同一条件的再次运输，没有得到第三条独立算术零。

本 note 新付的是 (4)–(7) 的全块同源比较以及 (8)–(13) 的准确规范行为。残差消去、$\mathfrak D_p$ 的指定非零性和原真前缀上的收益仍需要新证明，不据此另登记已解决的中央子问题。

## 直接依赖

R595 的完整分子与四行留数；R606 的原规范 Gaussian、两 $\Xi$ 及真实一次商；R609 的固定 Wilson 二次关系；R618 的全余项尾；R619/R622 的完整第二块及同一个原中央运输。

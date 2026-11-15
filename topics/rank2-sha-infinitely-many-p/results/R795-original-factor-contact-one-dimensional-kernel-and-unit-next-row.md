# R795 — 原因子接触的一维核、真实下一单位行与唯一 Schur 缺陷

日期：2026-11-15。**状态：以下带明确交数门的结论已证明。**
本篇只识别 R782/R790 的因子接触矩阵。
它不把原整个 $\mathcal W_D$ 的首核设为一维，
也不证明指定因子缺陷恰含一次 $p$。

## 1. 实际交数门

保 R790 的同一 $G$、曲线 $C$ 和精确接触阶 $h$。
固定一个包含 $G$ 的 R782 profile，或取同一 $G$ 的实际 Gauss 包络。
记该齐次因子格（含常数 $1$）为 $\mathcal A$，
径向次数均不超过 $b$，常数 charge 均只能为常数。

R787 给同一个固定多项式 $L_*$，满足
$$
L_*\mathcal A\subset\mathcal W_b,\qquad
\operatorname{ord}_P L_*=1.
\tag{1}
$$
令 $\mathcal B_b$ 为 R680 的原十九角来源除子。
由于 $L_*G$ 是非零实际来源，它的除子为
$$
\operatorname{div}(L_*G)=C+E_L,\qquad E_L\ge0.
$$
$\mathcal B_b$ nef，所以
$$
\boxed{\mathcal B_b\cdot C
=\mathcal B_b^2-\mathcal B_b\cdot E_L
\le\mathcal B_b^2.}
\tag{2}
$$
这里未把 profile 包络与 $C$ 的线系相等，
也没有删除 $G$ 在中间固定角可能有的额外基点。

本篇使用准确门
$$
\boxed{h+1>\mathcal B_b\cdot C.}
\tag{3}
$$
一个完全显示的充分门是 $h+1>\mathcal B_b^2$，
其中平方仍按原十九个整数重数计算。

## 2. 因子核准确一维

定义同一个实际矩阵
$$
C_h:\mathcal A\longrightarrow\mathcal O[t]/t^h,
\qquad H\longmapsto H(t,\rho(t)).
$$

**定理。** 在 (3) 下，准确有
$$
\boxed{\ker\bar C_h=k\bar G.}
\tag{4}
$$
若接触恰为 $h$，增加第 $h$ 行后，
$$
\boxed{\bar C_{h+1}\ \text{全列单射。}}
\tag{5}
$$

**证明。** 设 $\bar H\in\ker\bar C_h$。
因 $\psi\equiv\rho\pmod{t^h}$，
$\bar H(t,\psi)\in t^h k[[t]]$。
于是实际截面 $L_*\bar H\in H^0(X,\mathcal O_X(\mathcal B_b))$
在 $C$ 上的限制，在原光滑点 $P$ 至少消失 $h+1$ 阶。
若该限制非零，其零除子总次数为 $\mathcal B_b\cdot C$，
与 (3) 矛盾。
所以 $F\mid \bar H$（先清共同 $d$ 分母；$F$ 不整除 $L_*$）。

又因 $\deg_Y\bar H\le b=\deg_YF$，
有 $\bar H=a(t)G$。
比较常数 charge，$G(t,0)=1$，
而 $\bar H(t,0)$ 是常数，所以 $a(t)\in k$。
反向 $G$ 本来就在核中，证明 (4)。

同一实际第 $h$ 行在 $G$ 上取值
$[t^h]\bar G(t,\rho)=V_0\ne0$。
因此它杀掉 (4) 中唯一的核，得到 (5)。$\square$

这证明了原 factor 的局部唯一性，
不是用维数或一般位置假设它唯一。
在已经付清的平衡族
$\kappa/\mathcal B_b^2\to1$、$h/\kappa\to9/8$ 中，
(3) 的显示充分门最终成立；
有限参数仍须逐个保 (3)，不能提前删线性项。

## 3. 去常数列后，真实非齐次矩阵全列为单位

取原整基
$$
1,\ a_1,\ldots,a_m
$$
并写
$$
C_h=[\,\mathbf e_0\mid H_h\,],
\qquad
G=1+\sum_{i=1}^m x_i a_i.
$$
由 (4)，
$$
\boxed{\bar H_h\text{ 全列单射。}}
\tag{6}
$$
因为任一非恒定列的核向量若延成常数坐标零的 $C_h$ 核，
只能是零倍 $G$。
所以 $H_h$ 的全部 Smith 因子为单位，
其整余核无 $p$ 挠。

选任意一个单位 $m\times m$ 子式，行集为 $I$。
它必包含第零行：
否则 $\bar H_I\bar{\boldsymbol x}=0$，
由单位性迫 $\bar{\boldsymbol x}=0$，
这与 $C_h(1,\bar{\boldsymbol x})=0$ 矛盾。

在原 $\mathcal O$ 上定义唯一的实际 pivot 解
$$
\boxed{\boldsymbol x^*=-H_I^{-1}(\mathbf e_0)_I,}
\tag{7}
$$
并在剩余行读取
$$
\boxed{
\Delta=(\mathbf e_0+H_h\boldsymbol x^*)_{I^c}.
}
\tag{8}
$$
因为原 normalized $\bar G$ 是 (4) 的唯一解，
$\Delta\in p\mathcal O^{\,h-m}$。

真正的原因子首 Bockstein，在这些完整整单位坐标中准确是
$$
\boxed{
\beta_{C_h}(\bar G)
\longleftrightarrow \overline{\Delta/p}.
}
\tag{9}
$$
因此：
$$
\boxed{
\text{原同格 normalized factor 可提升为接触 }h\bmod p^2
\iff\Delta\in p^2\mathcal O^{\,h-m}.
}
\tag{10}
$$
这里的 $\Delta$ 是实际原有理前缀的 Schur 余项；
没有用任意补列或自选高轴代替它。

对含常数列的 $C_h$，
整单位消元后恰为 $m$ 个单位列及单列 $\Delta$。
所以它最多只有一个非单位 Smith 方向，
其指数准确为
$$
\boxed{e=\min_jv_p(\Delta_j),}
\tag{11}
$$
若 $\Delta=0$ 则记 $e=\infty$，表示特征零核。
不在这里另假设 $C_h$ 的特征零秩；
而 (5) 已保证加入真实第 $h$ 行后的整个矩阵全为单位。
尤其不能从 (4)、(5) 推 $e=1$。

## 4. 对原全余列配对的具体意义

R790 的每个全 $\mathcal W_D$ 真左对 $(\lambda,\mu)$
给出 factor 真左行
$$
\nu(f)=\mu(6t^{h+2}QeVf).
$$
按 (7) 的同一整消元运输 $\nu$，记其剩余行部分为 $\nu_{I^c}$。
则原完整 forcing 的最后一项准确是
$$
\boxed{
\langle\nu,\beta_{C_h}(\bar G)\rangle
=\nu_{I^c}\!\left(\overline{\Delta/p}\right).
}
\tag{12}
$$
原固定主部项、$V^3$ carry、全部其它 $\mathcal W_D$ 列和同一个 $R$
仍按 R790(30) 原样保留。

因此在 (3) 的实际范围，可以研究一个确定的原 normalized factor
及其唯一单列整缺陷，
而不假设有可任意选择的 factor 族。
(12) 是否与原另两项相消仍未判定；
更没有把这个 factor 一维核当成原 $K_1(M)$ 一维。

## 5. 较小的原 H0(O(C)) 范围必须另行区分

R495 已付原整个
$H^0(X,\mathcal O_X(C))$ 及其同源整提升。
在这个较小来源中，不必先乘 $L_*$：
原点处使用同一整正则 frame，
任一接触至少 $h$ 的截面在 $C$ 上消到至少 $h$。
因此
$$
\boxed{
h>\kappa
\quad\Longrightarrow\quad
\ker\!\left(
H^0(X,\mathcal O_X(C))
\longrightarrow k[t]/t^h
\right)=kF .
}
\tag{13}
$$
证明是限制线丛 $\mathcal O_C(C)$ 的次数恰为 $\kappa$；
高于此次数的零迫限制恒零，
再由
$0\to\mathcal O_X\to\mathcal O_X(C)\to\mathcal O_C(C)\to0$
和 $H^0(X,\mathcal O_X)=k$ 得到核 $kF$。
同一第 $h$ 行若在 $F$ 上为单位，仍付下一行后的单射。
这条较小范围不声称有 profile 的全部系数列。

本篇 (3)–(6) 的新增范围是整个 R782 profile 或整个实际 Gauss 包络。
它用 R787 的同一 $L_*$ 返回及 (2)，
支付了中间角额外基点可能造成的区别。
不能将 (13) 的 $h>\kappa$ 直接替换 (3)，
也不能因较小来源已是一维核就先替全 profile 或全 $\mathcal W_D$ 作同样判断。

依赖：
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R787](R787-original-factor-return-and-whole-square-source-normal-kernels.md)；
[R790](R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)。

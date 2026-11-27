# R1135：原 Gaussian 两个低行的有限纤维约束

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明，纯纸面。** 本结论使用完整原 $X_{\rm ns}^+(p)$ 的实际 good 角色。
在 $p=4k+3\ge41$ 且 $p\mid B_{p-7},B_{p-11}$ 的分支中，
同一原 marked Gaussian frame 内，所有非对角共同纤维的无序点对至多一个。
该候选由两条明确公式给出，仍需原其余 good 行排除。
另一分支 $p\mid B_{p-7}$、$p\nmid B_{p-5}$ 有一个明确的
degree-one 行组合，其斜率的单位性仍开放。

这里的 $p\mid B_n$ 指 $p$ 整有理数 $B_n$ 为非单位。
没有将 Bernoulli 非单位等同于 Gaussian Hurwitz 系数非单位。
不声称两个 twist frame 合并后至多一个点对，也不声称原圆盘内点已排除。

## 1. 实际输入与完整低行

保持 [R1116](R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
及 [有限本征重建](../notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)
的同一规范：
$$
E_a:y^2=x^3+ax,\quad a\in\mathbf F_p^\times,\quad
D\Psi=\delta\in\mathbf F_p^\times,\qquad
\mathscr K(T,U)=T^{-1}+U^{-1}+\sum_{\ell\ge1}P_\ell(T,U),
$$
其中 $P_\ell$ 对称、总次数 $4\ell-1$。同一 centered 总次数 $p$ 层为
$$
M_w=\sum_{h=1}^{k}\frac{w^{2h}}{(2h)!}
 (TU)^{2h}P_{k+1-h}
+\frac{w^{2k+2}}{(2k+2)!}(TU)^{2k+2}(T^{-1}+U^{-1}).
\tag{1135.1}
$$
实际 good 集合及 centered 标签是
$$
\mathcal G_p=\{R:\ 2\le R\le p-3,\ R\ {\rm even},\
 V_{\omega^R}\ne0,\ p\nmid B_R\},\qquad
\Pi_R(z)=N_R\mathcal A_R(\gamma^2z),
\tag{1135.2}
$$
$$
\mathcal A_R(w^2)=[T^{p-R}U^R]M_w,\qquad
\gamma=\delta\lambda\beta_0^{1-p},\qquad
N_R=\frac{(\beta_0^{p+1})^R\delta^{R-1}}{2b_{\omega^R}R!}.
$$
所有尺度均为原来源的单位。比较同一 frame 的两点时，$N_R$ 共同；
跨 frame 时未作未经证明的归一。

写
$$
c_s=[T^{p-4-s}U^s]P_k,\qquad
d_s=[T^{p-8-s}U^s]P_{k-1},\qquad Z=w^2.
$$
(1135.1) 中 $h$ 的支撑立即给完整行
$$
\mathcal A_4(Z)=\frac{c_2}{2}Z-\frac{G_{p-7}}{24}Z^2,\qquad
\mathcal A_6(Z)=\frac{c_4}{2}Z+\frac{d_2}{24}Z^2
                     -\frac{G_{p-11}}{720}Z^3.
\tag{1135.3}
$$
证明中使用 $[U^0]P_\ell(T,U)=-G_{4\ell}T^{4\ell-1}$，
这是原 sigma 核的 $\zeta(T)$ 轴项。更高 $h$ 的最低 $U$ 次数已超过
$4$ 或 $6$；最高 principal 亦不贡献。因此没有遗漏高尾。

原方程 $x''=6x^2+2a$ 给
$$
G_8=\frac{a^2}{525},\qquad G_{12}=-\frac{2a^3}{53625}.
$$
把它们代入 R1116 已付的准确反射
$G_{p+1-r}=-(r-1)!\delta^{1-r}G_r$，得到
$$
G_{p-7}=-\frac{48a^2}{5\delta^7},\qquad
G_{p-11}=\frac{96768a^3}{65\delta^{11}}.
\tag{1135.4}
$$
两者对本范围全部为单位；$96768=2^9 3^3 7$。
只使用 $r=8,12\le p-3$，没有外推未付的高权层。

## 2. 双低指标分支：至多一个无序点对

[R1128](R1128-all-prime-linear-good-cuspidal-rank.md) 的实际低角色判据给
$$
p\mid B_{p-7}\Longrightarrow 4\in\mathcal G_p,\qquad
p\mid B_{p-11}\Longrightarrow 6\in\mathcal G_p.
\tag{1135.5}
$$
因为 $B_4=-1/30$、$B_6=1/42$ 在 $p\ge41$ 为单位，
这里确是原出现且 good 的两个角色。

假设两条件同时成立，并令同一原 frame 的两个不同实际点对应
$Z,Z'$。若全部实际 good 坐标相等，令
$S=Z+Z'$、$P=ZZ'$。第一条 (1135.3) 的差除以 $Z-Z'$ 给
$c_2/2-G_{p-7}S/24=0$；第二条给
$c_4/2+d_2S/24-G_{p-11}(S^2-P)/720=0$。
由 (1135.4) 可以准确反除，所以
$$
\boxed{\quad
 S=\frac{12c_2}{G_{p-7}},\qquad
 P=S^2-\frac{30d_2S+360c_4}{G_{p-11}}.\quad}
\tag{1135.6}
$$
因此非对角共同纤维若存在，其无序点对只能是
$X^2-SX+P$ 的两个根，至多一对。

这还是必要条件。须进一步检查判别式非零、两个根属于原实际范围，
并代入所有其余 $R\in\mathcal G_p$ 的原标签。
$P=0$ 和尚未排除的 $S=0$ 均保留。
尤其没有把两条 twist line 的合并范围替换为单条 fine 平方像。

## 3. 一低一高分支：原固定 affine minor

假设 $p\mid B_{p-7}$、$p\nmid B_{p-5}$。
低 $R=4$ 由 (1135.5) 实际出现；$R=p-5$ 是原 forced 角色，
且在本假设下 good。由 $P_\ell$ 对称与原支撑，
$$
\mathcal A_{p-5}(Z)=\frac{c_3}{2}Z+\frac{d_1}{24}Z^2.
\tag{1135.7}
$$
这与第一条 (1135.3) 的准确组合是
$$
d_1\frac{\Pi_4(z)}{N_4}
 +G_{p-7}\frac{\Pi_{p-5}(z)}{N_{p-5}}
 =\frac{\Delta_{\rm low}}2\gamma^2z,\qquad
\Delta_{\rm low}=c_2d_1+G_{p-7}c_3.
\tag{1135.8}
$$
两行的系数矩阵行列式恰为 $\Delta_{\rm low}/48$。
故若 $\Delta_{\rm low}\ne0$，这两个真实行已分离同一 frame 的点。
若 $\Delta_{\rm low}=0$，则完整行严格比例
$$
\mathcal A_{p-5}=-(d_1/G_{p-7})\mathcal A_4.
$$
本篇没有证明 $\Delta_{\rm low}$ 为单位，后续必须处理这个准确退化支。
不以“两条都出现”替代行独立，也不添未出现或非 good 的角色。

## 4. 来源、验证与范围

全部是上述完整核的有限系数恒等式及 R1128 的实际 mask 判据。
root 与 o1_theta 已纸核两条反射、完整支撑、消元与作用域；
没有数学程序执行，没有新增数值窗口。
同一来源的 Newton 节点、完整 good 余核及其固定非观测值
见所引有限重建笔记 §§7–9。后续继续原 $\Delta_{\rm low}$、
唯一剩余点对的其余实际行以及两 twist 的准确运输。

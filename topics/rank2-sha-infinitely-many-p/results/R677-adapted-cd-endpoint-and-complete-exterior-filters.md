# R677 — 同一双 S 适配测试的 cd 端点、仿射不相容与完整外部过滤

**状态：已证明。** 本文使用 R674 的同一个实际 $q_N^\dagger$。
它对固定 N 不依赖观察深度 n，全部系数由原完整十三阶矩阵决定。
本文将它代入 R675 的真实 cd 端点，并与 R671 的外部过滤逐项对齐。

结果有三部分：

1. 虽然两条 $t=0$ 冻结来源是原 S 的单位倍，$t=1$ 的 cd 端点在
   一个相对密度 1 子族上仍为非 S 来源，且完整质量、单位质量均非零单位。
2. 更强地，在原九约束及“两冻结来源均在 S 线”的整个实际仿射族中，
   即使放开归一负一系数，也不可能同时令这个 cd 端点落在 S 线上。
3. 同一个六步算子作用于 cd 外部的两块，留下准确相反的同一额外来源。
   所有质量和 log 移权完整保留；算术总和为零不使两块分别为零。

这里的固定辅助有限域只证明显示的特征零有理式非恒零；
从未把其有限域解当作当前研究素数处的实际测试。

## 1. 固定 N 的同一个实际适配测试

保原全部 ray、周期、坏集，
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad \kappa=p\lambda^2,\qquad N\in4\mathbf Z_{>0}.
$$
R674 的实际十三阶矩阵记为 $\mathbb A_{N,p}$。
前十二行是两条完整 S34 冻结来源，末行是
原 $\mathfrak j_{N,p}$。原核的十一列仍是
$$
v_{p,j}=(I-R_pA_p)e_j,\qquad
j\in\{0,1,2,3,4,13,15,16,17,18,19\}.
\tag{1}
$$
不是另选一个近似核或另解原九约束。

令 $P^{\rm old}$ 为原 R594 多项式。
对任意 $z_0\in K_{\mathfrak p}$，定义完整实际解
$$
\boxed{
\begin{pmatrix}a(z_0)\\d_0(z_0)\\d_1(z_0)\end{pmatrix}
=\mathbb A_{N,p}^{-1}
\begin{pmatrix}
-\mathcal T\mathscr U_{0,N,p}(P^{\rm old})\\
-\mathcal T\mathscr U_{1,N,p}(P^{\rm old})\\
z_0-\mathfrak j_{N,p}(P^{\rm old})
\end{pmatrix}.
}
\tag{2}
$$
随后加 $\sum a_j(z_0)v_{p,j}$，并作原 E 次数整逆，
得到同一测试族 $q_N(z_0)$。
其全部 $\lambda,\kappa,u=\kappa^N$ 依赖保持。
$z_0=1$ 正是 R674 已定义的 $q_N^\dagger$。

实际十三阶矩阵可逆，所以 (2) 枚举原九约束下、
两条冻结来源均为 S 倍数的全部测试：
$$
\mathscr U_i(q_N(z_0))=d_i(z_0)S,\qquad
\mathfrak j(q_N(z_0))=z_0 .
\tag{3}
$$
它是一个真正的一维仿射族，不由维数猜测其可解性。
$z_0=1$ 时 $d_0,d_1$ 均为单位，
而原负一系数严格为
$$
J_N^\dagger=\frac{\ell_0^2}{2b\Omega^2}
 \lambda^N\kappa^{-2N},\qquad \ell_0=-3\omega/5 .
\tag{4}
$$
以上均是 R674 完整矩阵的结论。

## 2. 将同一实际解代回 t=1 端点

R675 给全部原参数的端点映射
$$
\mathscr B_{N,p}(P)=\sum_{j=0}^5 c_j(P)\Xi_j,\qquad
\Xi_j=\sigma^{34}x^{17-3j}.
\tag{5}
$$
第一观察为 $\mathscr B$，第二观察准确为 $-\mathscr B$。
它保完整 C 单位补项以及 $-8b\Omega^6$ 第六矩。
以下将 (2) 的同一完整解代 (5)，不修改任何 $p_{abc}$。

为给明确的非零证书，对原有理式的固定余式取
$$
\kappa=u=0,\qquad \tau=(1+\lambda)^{-1}=2,\qquad
\lambda=-1/2,\qquad \omega=374\pmod{1009}.
\tag{6}
$$
这是 R674 的同一个辅助地点。
由其实际定义的两十三阶矩阵及 R675 全部端点矩阵，得到
归一系数 $\widetilde c_j=b^{1-j}c_j$：
$$
\begin{array}{c|rrrrrr}
\eta&\widetilde c_0&\widetilde c_1&\widetilde c_2&
\widetilde c_3&\widetilde c_4&\widetilde c_5\\ \hline
+1&384&512&440&770&241&734\\
-1&738&344&945&856&322&541
\end{array}\pmod{1009}.
\tag{7}
$$
这是 $z_0=1$ 的同一适配解，不是把 R675 的旧测试直接复用。
第二观察按原 integer quarter 的负号归一后给完全相同的六列。

特别质量余式在两种 $\eta$ 都非零。
因其为固定特征零有理式，清分母后应用原固定 CM 多项式单位密度引理，
并与 R674 的可逆/单位子族取交，得到：

**定理 1。** 在同一 ray 的一个相对密度 1 子族上，
所有 $N\in4\mathbf Z_{>0}$ 同时满足
$$
\boxed{
c_0(q_N^\dagger)\in\mathcal O^\times,\qquad
\mathscr B_{N,p}(q_N^\dagger)\notin K_{\mathfrak p}S .
}
\tag{8}
$$
R675 whole S34 principal 核给
$$
\boxed{
\mathcal A_{0,N}^{S,\dagger}(0)=(1-\lambda)c_0(q_N^\dagger)\in\mathcal O^\times,
\qquad
\mathcal A_{1,N}^{S,\dagger}(0)=-\mathcal A_{0,N}^{S,\dagger}(0).
}
\tag{9}
$$
这里 $\mathcal A_{i,N}^{S,\dagger}$ 是同一未切第二 Y 的 cd 返回行。
归一化只改变整体单位，不把非零质量换成中央导数。

一致性来自实际 $u,\kappa$ 的余式都为零；
同一个固定有理式控制所有 N。
没有使用逐 N 素数扫描，也没有将 (6) 的解当作实际 $q_N^\dagger$。

## 3. 即使归一负一系数自由，也不能同时适配端点

(2) 对 $z_0$ 仿射，所以 (5) 的每一个坐标也仿射。
原 S 线的前两个必要条件是
$$
c_0=0,\qquad 7c_2+53b c_1=0.
\tag{10}
$$
在归一坐标中，记其两条实际仿射式为
$$
E_0(z_0)=a_0+b_0z_0,\qquad
E_2(z_0)=a_2+b_2z_0 .
\tag{11}
$$
所有系数均由完整实际 (2)、(5) 定义。
$\mathbb A_{N,p}^{-1}e_{13}$ 是其真实 $z_0$ 方向；
不能把不同源上的一个质量方向替代它。

在相同辅助地点，完整计算给
$$
\begin{array}{c|rrrr|r}
\eta&a_0&b_0&a_2&b_2&a_0b_2-a_2b_0\\ \hline
+1&474&919&616&339&200\\
-1&277&461&540&91&265
\end{array}\pmod{1009}.
\tag{12}
$$
原十三阶行列式仍分别为 856、729。
证书同时验证原九行右逆、全部实际核及此方向；
(12) 不是只抽两条不相关的低矩。

两个固定有理行列式的分子都非恒零。
再次用同一个固定 CM 单位密度引理，实际
$a_0b_2-a_2b_0$ 在相对密度 1 子族上为单位。
因此：

**定理 2。** 在该子族上，对所有 N，
原九条约束及“两条 $t=0$ 冻结来源都在 S 线”
的整个实际仿射族中，没有任何 $z_0\in K_{\mathfrak p}$
能使 $t=1$ 的 cd 端点也在 S 线上。
此结论甚至不要求 $z_0\ne0$ 或 $z_0$ 为单位。

证明只需 (11)：若两个式子同时为零，
则 $a_0b_2-a_2b_0=0$，与单位行列式冲突。
前两个 S 线条件已经不相容，无需猜测其余三条。
这排除的是显示的同一测试适配问题，
没有排除改变真实观察、保全补域的其他算术关系。

## 4. 两个过滤器使用的真实集合

现在固定同一个 $q_N^\dagger$，只让 $n\ge N$ 变化。
记
$$
E_i(n)=\{Y_i\in p^n\},\qquad
CD_N=\{c,d\in p^N\},\qquad
\Gamma_n=E_0(n)\cap E_1(n).
$$
对所有 $n\ge N$，准确有
$$
\boxed{
I_n:=\Gamma_n\cap CD_N
=\Gamma_n\cap\{\mathcal E\in p^N\}.
}
\tag{13}
$$
这是 R664 的共同 E 深域。
它与未切第二 Y 的 $V_{i,n}:=E_i(n)\cap CD_N$
只在 $n=N$ 时相等；一般还须保
$$
O_{i,n}=V_{i,n}\setminus I_n,\qquad
X_{i,n}=E_i(n)\setminus CD_N.
\tag{14}
$$
所有以下积分仍用 R671 原 $q_N^\dagger$、
完整的 $(-\kappa)^{-n}Y_i$ unit Mellin 观察和实际门；
这些集合只显示其新增 cut，不删除 q 自身的门。

令对应完整行也以 $I,V,O,X$ 表示。
原真实来源恒等式为
$$
\boxed{\begin{aligned}
V_{i,n}(w)&=\lambda^{n+3N}\mathcal A_{i,N}^{S,\dagger}(w),\\
I_{i,n}(w)&=\mathcal C_{i,n}^{S,\dagger}(w),\\
O_{i,n}&=V_{i,n}-I_{i,n},\\
X_{i,n}+V_{i,n}&=\epsilon_i\lambda^{n+N}J_S .
\end{aligned}}
\tag{15}
$$
第一个式子保原 D 与全部 cd 核；
$4\mid N$ 使原符号幂准确为一。
第二个式子由 (13) 给，不能只因两序列有相同特征根就认同。

## 5. 同一个六步算子的完整 O/X 返回

记真实深度移位为 $\mathsf T:n\mapsto n+1$，并置
$$
P_6(\mathsf T)=\prod_{a=1}^6(\mathsf T-\lambda^2\kappa^a),
\quad U_6=\prod_{a=1}^6(1-\kappa^a),
\quad V_6=\prod_{a=1}^6(1-\lambda\kappa^a).
$$
三个乘积均按当前 ray 的原单位规范。
R674 已给
$$
P_6 I_{i,n}
=\epsilon_i d_i\lambda^{2n+2N+12}U_6J_S.
\tag{16}
$$
因为固定 N 的 $\mathcal A_{i,N}^{S,\dagger}$ 不随 n 变化，
(15) 立即但准确地给
$$
\boxed{\begin{aligned}
P_6 O_{i,n}
={}&\lambda^{n+3N+6}V_6\mathcal A_{i,N}^{S,\dagger}
-\epsilon_i d_i\lambda^{2n+2N+12}U_6J_S,\\
P_6 X_{i,n}
={}&\epsilon_i\lambda^{n+N+6}V_6J_S
-\lambda^{n+3N+6}V_6\mathcal A_{i,N}^{S,\dagger}.
\end{aligned}}
\tag{17}
$$
这是全 Mellin 函数身份，保全部质量和导数。
每一移位使用自己的原物理域，不把六步相加认作不动 cut。

相加 (17) 正是 R674 完整外部加浅域的返回；
额外的六维来源准确消去。分别的两块却保相反号的同一来源。
若原 $J'_S(0)=0$，仅得到
$$
\boxed{
(P_6O_{i,n})'(0)=
 \lambda^{n+3N+6}V_6\mathcal A_{i,N}^{S,\dagger\,\prime}(0),
\qquad
(P_6X_{i,n})'(0)=-(P_6O_{i,n})'(0).
}
\tag{18}
$$
没有给右边的额外导数赋零。

原 $J_S(0)=0$，而 (9) 的质量为单位，
所以无需任何中央导数假设，
$$
\boxed{
(P_6O_{i,n})(0)=
 \lambda^{n+3N+6}V_6\mathcal A_{i,N}^{S,\dagger}(0)\in\mathcal O^\times,
\qquad
(P_6X_{i,n})(0)=-(P_6O_{i,n})(0).
}
\tag{19}
$$
这两个真实过滤外部都不具有可免费删除的零质量。

R671 的七步过滤器与本篇确实满足
$$
P_7(\mathsf T)=\prod_{a=0}^6(\mathsf T-\lambda^2\kappa^a)
=(\mathsf T-\lambda^2)P_6(\mathsf T).
$$
因此它们的准确共同倍数返回为
$$
\boxed{
P_7O_{i,n}
=\lambda^{n+3N+7}(1-\lambda)V_6
 \mathcal A_{i,N}^{S,\dagger}.
}
\tag{20}
$$
这重获 R671 的同一个完整端点来源，而不是原 S；
(8) 和定理 2 说明为什么不能把两种返回的右端相认。

## 6. 单位质量造成的真实 log 项

对任何实际观察缩放 $r\in\mathcal O^\times$，
$$
F_r(w)=\langle r\rangle^{d_pw}F(w)
\quad\Longrightarrow\quad
d_p^{-1}F_r'(0)=d_p^{-1}F'(0)+\log\langle r\rangle F(0).
\tag{21}
$$
应用 (21) 到 (17) 的任一外部时，必须保 (19) 的单位质量。
两个质量只有在整条正确和式中按其真实系数补偿；
若两个 word 的观察缩放不同，不能直接删去两项 log。

同一 $q_N^\dagger$ 的 R665/R674 原 T 负一深差仍满足其已付
$P_6$ 非零公式。它使用 $b_LL\pm b_YQ$、真实 L 深门和返回后的坐标；
这不是 (13) 或 (14) 的单 Y cd cut。
本文既不以该非零行代入 (18)，也不把原 T 的浅域/外部附送为零。

本篇的实际推进是：完整识别两个过滤右端及同一额外来源，
并以原完整仿射系统排除同时适配两端点的尝试。
下一步若继续推进原算术总行，必须支付不同 word/cut 的真实运输，
或识别 (17) 中六维来源的额外算术关系；
不能重复利用总和为零来给 O、X 各自赋零。

## 7. 精确证书

- scripts/check-r677-adapted-cd-endpoint-and-exterior-filters.js
- scripts/check-r677-adapted-cd-endpoint-and-exterior-filters.json

输入仅为已发表的 R594、R674、R675 三份原数据。
脚本重建原核、十三阶实际定义的固定余式、端点全部六行、
$z_0$ 的完整方向和 (12) 行列式。
辅助模数 1009 不作研究素数样本；非零证书通过固定有理式
和原 CM 单位密度引理返回所有实际好素数及全部 N。

依赖：

- [R674](R674-original-double-s-arithmetic-adaptation-and-negative-one.md)：完整实际适配及同一六步过滤。
- [R675](R675-original-cd-endpoint-and-complete-six-source-return.md)：全参数端点、全部 C 第六矩和六系数。
- [R671](R671-fixed-depth-cd-return-and-original-exterior-filters.md)：原 cd 域和七步过滤。
- [R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)：原 T 负一深支及完整补域。

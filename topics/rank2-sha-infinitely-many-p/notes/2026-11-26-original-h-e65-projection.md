# 原 R548 正来源的真实两态轴及 degree390 全投影消费者

日期：2026-11-26。**结构恒等式已证明；本次新增的正来源边际投影尚待同一公开390运行，未预定其为零或非零。**

本注沿用 R961 已成功返回的原完整66维矩阵与原 E65 来源。
涉及整测度的结论沿用 R961 的普通射线与相容周期；有限 CM 证书本身在特征零。
新增消费者不重建另一套 CM 来源，只在同一次 R961 函数中复用
$\Pi_{65}$ 和全部既有除法函数。它检查的是 R548 的原正来源 $h$，
不是把原 $\rho_{\rm raw}$ 换一个轴重新命名为 $h$。

## 1. 原状态、真实置换与不可省去的根单位

记
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
g=3+\omega,\quad \bar g=2-\omega,\quad
v=4+\omega,\quad a=7+3\omega.
$$
输入顺序固定为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，并使用 R548 的完整
$$
\rho=-\frac1{84}\nu_\sigma^{\otimes6},\qquad
\eta=\omega^2 H_*\rho,\qquad h=\eta+\frac12\rho,
$$
$$
H=I_4\oplus\frac12
\begin{pmatrix}\omega^2&-\delta\\2+\omega&\omega^2\end{pmatrix}.
\tag{1}
$$
R548 已在共同二覆盖上证明
$(R_c)_*\rho=-\rho$ 和 $(R_c)_*\eta=\eta+\rho$；这里 $R_c$ 只反射
原 $c$。这些是完整六变量来源等式。

R961 标准第一行是
$(\delta,2\delta,g,\bar g,a,18)$。
对六个原输入作两个置换并在最后一项乘 $\omega^2$，得到实际行
$$
r_h=(\delta,2\delta,a,18,g,\omega^2\bar g).
\tag{2}
$$
令 $U$ 是实现 $r_h=r_{65}U$ 的单项式矩阵。对任意行 $r$，准确为
$$
rU=(r_1,r_2,r_5,r_6,r_3,\omega^2r_4).
$$
$U\bar U^t=I$，sigma 的根单位恒等式给 $U_*\rho=\omega^2\rho$。
特别 (2) 没有保留旧 $A$；它在原四个前输入中的实际系数已改变。

直接乘 (1)，最后两项逐项给
$$
r_hH=(\delta,2\delta,a,18,\omega^2v,-\omega),
\qquad
r_hR_cH=(\delta,2\delta,a,18,\omega^2,\omega\bar v).
\tag{3}
$$
因此两个原 CM7 因子转成真实 CM13 因子和原 sigma，而不是新选的
degree390 系数向量。

## 2. 全部多项式身份与准确边际尺度

用原 $r_\gamma=\sigma(\gamma z)/\sigma(z)^{N\gamma}$。
完整除法函数准确满足
$$
r_g r_{\bar g}=7X^2-4X+16=r_v+r_{\bar v},
\qquad
r_{\bar v}-r_v=-\delta(X^2+44X+16),
\quad X=x^3.
\tag{4}
$$
这也由 R548 两态恒等式在 (2) 的限制直接推出第一条。
消费者另外通过实际 CM 群律重建 $r_v$，逐系数核 (4)，不是用
若干 Taylor 项猜恒等式。原 CM7 的整个函数仍用同一次已重建对象。

记 R961 已核的候选为
$$
F=-\frac{
 \sigma(\delta z)\sigma(2\delta z)\sigma(gz)\sigma(\bar gz)
 \sigma(az)\sigma(18z)}
 {84\cdot9a}
=\sigma^{390}P(X).
$$
其完整 $P$ 次数64，最高系数一。
定义两个真实六 sigma 候选
$$
F_v=-\frac{
 \sigma(\delta z)\sigma(2\delta z)\sigma(az)\sigma(18z)
 \sigma(vz)\sigma(z)}
 {84\cdot9a},
$$
以及将 $v$ 换成 $\bar v$ 的 $F_{\bar v}$。于是
$$
F_v+F_{\bar v}=F,\qquad
P_v=\frac{P}{7X^2-4X+16}\,r_v,\qquad
P_{\bar v}=\frac{P}{7X^2-4X+16}\,r_{\bar v}.
\tag{5}
$$
显示除法在 $K[X]$ 中是整除，消费者全部回乘。
两者的 $z^6$ 系数分别为 $v/7$、$\bar v/7$。

对 (2) 的第一边际，$(9a)^{-1}(r_h)_*\rho=\omega^2F$；
由 (1)、(3)，$(9a)^{-1}(r_h)_*\eta=-\omega^2F_v$。
因此原正来源的准确第一边际为
$$
\boxed{
(9a)^{-1}(r_h)_*h=\frac{\omega^2}{2}(F_{\bar v}-F_v)
=\sigma^{390}P_h(X),\qquad
P_h=-\frac{\omega^2\delta}{2}
 \frac{P(X)}{7X^2-4X+16}(X^2+44X+16).}
\tag{6}
$$
$P_h$ 次数64，最高系数 $-\omega^2\delta/14\ne0$；
它的质量顶坐标65为零。式(6)并未据此断言其 E65 投影非零。

## 3. 在取边际以前支付完整共同 theta 张量

设 $L$ 是 R961 已支付的整框架，
$$
L\bar L^t=\operatorname{diag}
(390,25740,3564,2754,2244,1628).
$$
只将五个伴随行加倍：
$$
D=\operatorname{diag}(1,2,2,2,2,2),\qquad L_h=DLU.
\tag{7}
$$
$L_h$ 整且第一行是 (2)。$L_hH$ 的第一行由 (3) 整；
其余五行已乘2，正好清去 (1) 的分母，故 $L_hH$ 也整。
由于 $H\bar H^t=I$，两框架有同一个 Gram：
$$
L_h\bar L_h^t=(L_hH)\overline{(L_hH)}^t
=\operatorname{diag}(390,4\cdot25740,4\cdot3564,
                    4\cdot2754,4\cdot2244,4\cdot1628).
\tag{8}
$$
行列式范数是 R961 原范数的 $4^5$ 倍，仍素于 $7\cdot19$，
且当前 $p>211$ 全为单位。

在 $\mathcal O_K/2$ 中，每个非零类的 sigma 半特征相同；
CM 拉回的半特征正是原半特征的 norm 次方。
两框架每行的 degree 为偶，因而全半特征一致。
(8) 又支付全部 Gaussian 交叉项为零。
所以在取边际以前，两整个来源属于同一个
$$
\mathcal S_{390}\otimes
 \mathcal S_{4\cdot25740}\otimes\mathcal S_{4\cdot3564}\otimes
 \mathcal S_{4\cdot2754}\otimes\mathcal S_{4\cdot2244}\otimes
 \mathcal S_{4\cdot1628}.
\tag{9}
$$
由线性组合，$\mathcal H=(9a)^{-1}(L_h)_*h$ 也属于 (9)。
消费者逐项核两个整矩阵、全部 Gram、半特征奇系数个数以及两边逆。
这里没有从 (6) 的第一边际反推出 (9)。

## 4. 同一原投影、全部伴随与待返回的非零门

R961 已核原第一 principal 的
$$
\Pi_{65}=\frac{q_7(N_7)q_{19}(N_{19})}{(12\omega)(-12)}
$$
是完整66维的有理秩一投影，像为原 $KF_{65,1}$。
它在 $p>211$ 整。应用于 (5)、(6)，定义
$$
\Pi_{65}F_v=\alpha_vF_{65,1},\quad
\Pi_{65}F_{\bar v}=\alpha_{\bar v}F_{65,1},\quad
\Pi_{65}(\sigma^{390}P_h)=\alpha_hF_{65,1}.
$$
原 R961 的准确值给必须回乘的约束
$$
\boxed{
\alpha_v+\alpha_{\bar v}=\frac{25\omega}{72a},\qquad
\alpha_h=\frac{\omega^2}{2}(\alpha_{\bar v}-\alpha_v).}
\tag{10}
$$
消费者保全部66坐标，逐条核三条投影，而非只读最高项。

(7) 及 $L_hH$ 在两个 CM 核的六重积上都是双射。
R961 的完整奇 sigma 相位在7和19两个方向均为 $+1$，
因而对 $\mathcal H$ 保持原同时六重 trace 身份。
第一轴逆由同一个 E65 本征锚支付。
故以 (9) 中五个实际伴随的对应定义
$$
B_\ell=\prod_{i=1}^5N_{\bar\gamma_\ell,Z_i},\qquad
\mathcal C_h=
\frac{q_7(B_7)q_{19}(B_{19})}{(12\omega)(-12)}\Pi_{\mathbf Z},
$$
准确有整个张量身份
$$
\boxed{\mathcal C_h\mathcal H=F_{65,1}\otimes\Lambda_h,\qquad
       \Lambda_h(0)=\alpha_h.}
\tag{11}
$$
这里 $\mathcal C_h$ 的伴随 degree 是 (9)，不可抄成未双倍的 degree。

$\Lambda_h$ 由第一变量六阶矩除以 $720\Omega_p^6$ 整读取。
若本次返回 $\alpha_h\ne0$，只在其全域范数的固定分子分母之外，
它是一个完整五变量 Amice 卷积单位。
若本次 $\alpha_h=0$，结论仅为第一边际的目标投影为零；
不能据此将 $\Lambda_h$ 或整个投影张量判为零。

## 5. 实际中央行以及原 R548 测试的全部返回

(11) 运输到原 $b=17$ 模型时，继续使用 R961 的
$$
\nu_{F_{65,17},p}=\frac{65}{17\cdot175}\widehat\nu_{65,p}.
$$
因此对完整独立伴随测试 $b(\mathbf Z)$，
$$
\int_{Y\ {\rm unit}}\langle Y\rangle^{(p-1)v} b(\mathbf Z)
 \,d\nu_{\mathcal C_h\mathcal H_{17}}
=\frac{65}{17\cdot175}\widehat J_{65,p}(v)
                                  \nu_{\Lambda_{h,17}}(b).
\tag{12}
$$
同一个原 E65 坏中央使其一阶中央行为零。
这条行来自原 $h$，并未将质量或卷积乘积赋新的中央零。

所有 $q_7q_{19}$ 项保留
$\beta=\gamma_7^j\gamma_{19}^k$ 的全部 $E[\bar\beta]^5$ 纤维、
$\bar\beta^{-5}$、对称 theta 中心和六个角支。
分支测试使用 $D_{\beta,\zeta}
=\operatorname{diag}(1,\zeta/\bar\beta,\ldots,\zeta/\bar\beta)$。

对原输入行 $r$，必须在每一支使用 $rL_h^{-1}D_{\beta,\zeta}$。
消费者逐行全回乘原 $Y_s,W_t,W_\pm,L_{\rm mix},u_0,u_1,u_2$，
保所有原单位域、深管和 logarithm。
原 $P_j=I+(\kappa-1)\bar u_j^tu_j$ 在新坐标中为
$$
\mathcal A_j=I+(\kappa-1)b_jq_j,\quad
b_j=L_h\bar u_j^t,\quad q_j=u_jL_h^{-1},\quad q_jb_j=1.
$$
这些列、行和整个 rank-one 矩阵均在消费者回乘。
令 $\mathcal R=L_hR_cL_h^{-1}$，则 R548(41) 的实际测试在每支是
$$
\boxed{
\widetilde f(\mathcal A_1D_{\beta,\zeta}(Y,\mathbf Z))
-\widetilde f(\mathcal R\mathcal A_1
                       D_{\beta,\zeta}(Y,\mathbf Z)),
\qquad \widetilde f=f\circ L_h^{-1}.}
\tag{13}
$$
矩阵次序不可交换；完整原 $q$ 也作同一拉回。

(12) 与 (13) 同时给出一条新的可联立条件和准确的旧余项接口。
即使 $\alpha_h\ne0$，本注也没有据此将 R548(40) 中的任何混合项
直接置零。式(13)一般不是 (12) 的独立伴随测试。
真正联立消去仍须在这些相同来源与相同切域上完成。

## 6. 同次公开执行范围

新增代码位于既有
check-original-e65-six-sigma-projection.py 的同一个函数中。
它复用同一次 $\Pi_{65}$、原完整 source、division7 和 division37，
只新增 division13 群律，绝不调用另一个 CM producer。
原 R961 的成功门保持；新增回执键为 original_h_projection。

所有结构和三个完整投影均返回以后：

- $\alpha_h\ne0$ 记 PASS_NONZERO_MARGINAL，并报告准确全域范数；
- $\alpha_h=0$ 记 EXACT_ZERO_MARGINAL，保留完整失败边界，不说张量为零。

本注的非零门尚待下一次已协调的原390公开运行。
没有单独触发、新 workflow 或另存生成系数表。


## 本次原来源执行

状态：源码和完整证明已提交；实际运行结果待返回，不预置零或非零。

同一 `check-original-e65-full-cm-sixth-axis.py` v3 入口先完整重生 E65 的 degree390 CM7/19 来源和原 E89 的 degree178 来源，各一次；两新消费者共享同次来源。固定参数为 `workers=4`、`python-flint=0.9.0`、过定系统 `p=227`、精度5；所有旧局部/六jet/角帽/六sigma门保持。原 h 的零投影作为准确结果保留，不将它误报为整个伴随张量为零。只存脚本、参数、run和摘要；不保存可重算输出。

- 入口 SHA-256：`8cfe88309ec81ac50a363ede36350696c4818cff1c5d23cebe4868a87ad9f96b`。
- workflow SHA-256：`86567ee9a9c092d19c4144701933cd5118b6543573859663f6dc29e98f57c702`。
- request SHA-256：`e93377bdb70fef640febc7ae836bd4b66e8cc6f3373686812c9cc73ddf9838c7`。
- 五轴过定及全部 C24 helper：`204b014a969916e34b3404e4372d47010ad15013b1b54e26798431ec1f196abd`。
- 含原 h 投影的六sigma helper：`027b26c944a37d94e4e12f2d2c13dbd98c9188a6de4ee5cea40332e013dc85bc`。

2026-11-26 12:51:37 UTC 挂入触发路径；实际 source commit/run/job 由下一条回执补齐。

# R100：邻近二次目标、准确预 Newton 与真实参数族的共轭转移

2026-11-12，constructive-route。

**状态：已证明的中间结论，包含实际完整返回的数据。** 本文保留此前全部
550 段真实源和参数误差，给一个位于既有真实参数盒内的准确有限校正，
并证明将其接到 R31 的完整共轭转移公式。旧目标的一步参数预测约为
$-5.8174\,10^{-9}$，超出已付半径 $10^{-9}$；这个失败完整保留。
下面更换的是自由选择的旋转目标，不更换几何候选、真实参数族或参考曲面。

当前真实源仍包含尚未补回的局部二阶积分费用。因此本文不声称 R31
已通过，更不声称已完成等距 PDE 逆或本课题的闭面构造。

## 1. 一个准确、同量级小除数常数的新目标

令 $\varphi=(1+\sqrt5)/2$，取有限前缀

$$
(0,1,1,4,2,1,4,\underbrace{1,\ldots,1}_{17\text{ 个}},
8,1,1,7,3,7)
$$

并接 $\overline1$ 尾。准确矩阵乘法给

$$
\prod_a\begin{pmatrix}a&1\\1&0\end{pmatrix}
 =
\begin{pmatrix}
690433168&94331801\\
1251918455&171045842
\end{pmatrix},\qquad \det=1 .
$$

定义

$$
\rho_*=\frac{690433168\varphi+94331801}
                 {1251918455\varphi+171045842},
\qquad d_*=\pi\rho_* .
\tag{100.1}
$$

这是 full return 的旋转数；half return 的角是 $d_*$。消去
$\varphi^2-\varphi-1=0$，得到不可约本原整二次式

$$
1323907691653283951 X^2
-1460270480137213085 X
+402669666587037055=0.
\tag{100.2}
$$

其判别式准确为 $5$。矩阵行列式为 $1$，各正部分商至多为 $8$，
所以 R30 §3 的完整连分数证明给，对于全部 $k\ne0$，

$$
\|k\rho_*\|_{\mathbb Z}>\frac1{10|k|},
\qquad
|e^{2\pi ik\rho_*}-1|>\frac2{5|k|}.
\tag{100.3}
$$

因此 R31 (1.2) 的安全常数为 $K=5/2$，没有引入一个巨大分母的
任意有理平移。这里的全频结论来自整个准确连分数，不来自有限频率扫描。
由同一证明对 $2k$ 应用 (100.3)，还有
$\operatorname{dist}(k\rho_*,\mathbb Z+\tfrac12)>1/(40|k|)$；
但含真实首低阶相位的 PDE 传输须重新支付其完整算术门。

实际 Arb 计算给

$$
\rho_*=0.55150011188228709316755789744052316\ldots,
\quad
\rho_*-\frac{15121+\sqrt5}{27422}
 =2.13612716593842498524\ldots\,10^{-12}.
$$

(100.2) 的首系数远大于旧式的 $13711$。不得沿用旧系数所给的
R34 高频阈值、危险 norm 集或任何未重新检查的完整相位结论。
这里仅支付纯旋转除数。

## 2. 准确有限预校正与真实对象

所有 Fourier 范数采用 $2\pi$ 标签角 $x$。原始准确共轭是
$H=x+h$，$q$ 是 R48/R63 已检查的有限逆导数近似。
令同一实际 half return 为 $P_p$，写

$$
A_p=P_p\circ H=x+a_p .
$$

完整 550 段端点已经给出有限周期多项式 $P_0,P_1,P_2$，分别逼近
$a_{p_0},\partial_pa_{p_0},\partial_p^2a_{p_0}$；
它们的真实误差、整盒二阶参数界和宽度均沿用保存报告。
不假定这些有限多项式本身组成参数族。

对任意所选实角 $d$，置
$h_d=h\circ T_d,\ q_d=q\circ T_d$，以及

$$
E=P_0-h_d-d,\qquad e=q_dE,\qquad b=q_dP_1.
$$

在有符号有限均值 $\langle b\rangle$ 排零后，先选
$\mu$ 为 $-\langle e\rangle/\langle b\rangle$ 的准确 dyadic 中心，
再逐模选择准确 dyadic 多项式 $w$，其中 $w_0=0$，正频率选择自

$$
w_k=\frac{(e+\mu b)_k}{e^{ikd}-1},\qquad k>0 .
\tag{100.4}
$$

负频率取共轭。选择步骤只定义一个明确的有限对象；其余数随后用完整
准确乘积重新计算，因此没有把 $q$ 当成真逆、把 Arb 球中心当成真商，
也没有删掉选择误差。

定义准确的新共轭和参数

$$
J=\operatorname{id}+w,\qquad
H_{\rm new}=H\circ J,\qquad p_{\rm new}=p_0+\mu .
\tag{100.5}
$$

$H_{\rm new}$ 是一个明确的解析复合，不冒称为原来的有限 Fourier
多项式。若 $\|w'\|_0<1$，则 $J$ 为实保向次数一圆周微分同胚。

## 3. 有限残差及完整 Taylor 费用

记 $w_d=w\circ T_d$。完整的一阶剩余和保留的二阶多项式为

$$
R_1=E+\mu P_1+(1+h_d')(w-w_d),
$$

$$
R_2=R_1+E'w+\mu P_1'w
+\frac12P_0''w^2-\frac12h_d''w_d^2 .
\tag{100.6}
$$

这里每个有限乘积的全部频率均保留。注意 $P_0$ 是周期部分：
$1+P_0'$ 才是对应次数一提升的导数。将
$E'=P_0'-h_d'$ 代入，(100.6) 的线性空间项准确等于
$(1+P_0')w-(1+h_d')w_d$。

设 $s>0$，$u=\max(\|w\|_s,\|w_d\|_s)$，$s+u<\sigma$。
有限复合的完整余项不超过

$$
\frac{\|P_0'''\|_{s+u}+\|h'''\|_{s+u}}6u^3
+\frac{|\mu|}2\|P_1''\|_{s+u}u^2 .
\tag{100.7}
$$

这是逐点 Taylor 积分式结合 Wiener 复合不等式得到的；
第二项支付 $\mu P_1(x+w)$ 的二阶空间余项。

若真实端点与一阶参数误差在闭 $\sigma$ 带的 sup 界分别为
$\epsilon_0,\epsilon_1$，而整条真实参数线段上
$\|\partial_p^2 A_p\|_{s+u}\le T_\Gamma$，则 R63 的 Hardy 转换给

$$
\mathcal H(t)=\sqrt{1+\frac4{e^{2t}-1}},\qquad
\epsilon_{\rm source}=
\mathcal H(\sigma-s-u)(\epsilon_0+|\mu|\epsilon_1)
+\frac{\mu^2}2T_\Gamma .
\tag{100.8}
$$

这是实参数二阶 Taylor 式；不需要复参数域或第三参数导数。
**必须**先证整条线段包含于已经支付的真实参数盒。若没有这个包含，
(100.8) 只是一串形式数值，不给真实新参数上的结论。

于是

$$
\|P_{p_{\rm new}}\circ H_{\rm new}
       -H_{\rm new}\circ T_d\|_s
\le \|R_2\|_s+\text{(100.7)}+\epsilon_{\rm source}.
\tag{100.9}
$$

完整真实误差不因有限同调残差很小而消失。

## 4. 新共轭的实际局部逆

令 $m=\|w'\|_s<1$，则

$$
\|1/H_{\rm new}'\|_s
\le\frac{\|1/H'\|_{s+\|w\|_s}}{1-m}.
\tag{100.10}
$$

这是链式法则及 Wiener Neumann 级数。对半径 $r>0$，再在
$s+r+\|w\|_{s+r}$ 评价旧 $H$，链式法则给

$$
\|H_{\rm new}''\|_{s+r}
\le
\|H''\|_{s+r+\|w\|_{s+r}}(1+\|w'\|_{s+r})^2
+
\|H'\|_{s+r+\|w\|_{s+r}}\|w''\|_{s+r}.
\tag{100.11}
$$

以右侧为 $B$、(100.10) 为 $R$，若
$\kappa=RBr\le1/2$ 且 $R\epsilon\le r/2$，
R63 的同一 Wiener 收缩给真实 half return 共轭后的中心位移

$$
C_{\rm new,p_{\rm new}}=x+d+v,\qquad
\|v\|_s\le \frac{R}{1-\kappa/2}\epsilon .
\tag{100.12}
$$

这里 $\epsilon$ 是 (100.9) 的完整真实界。

## 5. 将既有整盒 full-return 预算准确转移

下面避免重新计算 550 段参数源。设旧完整 family 在 $S_0$ 带为

$$
F_p=x+\omega_0+u_p,\qquad \|u_p\|_{S_0}\le U_0
$$

并在同一整个真实参数盒有

$$
\|F_p{}_{,p}\|\le P,\quad
\|F_p{}_{,xp}\|\le Q,\quad
\|F_p{}_{,pp}\|\le T,\quad
\|F_p{}_{,xx}\|\le B,\quad
\|F_p{}_{,x}\|\le L .
\tag{100.13}
$$

(100.13) 的重复下标明确表示空间和参数偏导。
在本文实际输入中 $F_p=(H^{-1}P_pH)^2$，$U_0$ 可取旧 half-box
位移界的两倍，$L$ 可取已付 half 空间导数界的平方。

取 $s+\|w\|_s<S_0$，并令 $\omega=2d$。
为了在同一整盒构造

$$
\widetilde F_p=J^{-1}F_pJ=x+\omega+v_p,
\tag{100.14}
$$

在 $\mathcal A_s$ 的半径 $r_J$ 球上使用准确方程

$$
v_p=(\omega_0-\omega)+w+u_p\circ J
                  -w\circ T_\omega\circ(\operatorname{id}+v_p).
\tag{100.15}
$$

若

$$
m_*=\|w'\|_{s+r_J}<1,\qquad
|\omega_0-\omega|+\|w\|_s+U_0+\|w\|_{s+r_J}<r_J,
\tag{100.16}
$$

则 (100.15) 是统一收缩；得到整盒真实 family 的解析延拓，且

$$
V:=\sup_p\|v_p\|_s
\le\frac{|\omega_0-\omega|+U_0+2\|w\|_s}{1-m_*}<r_J.
\tag{100.17}
$$

后一严格小量门在实际代码中再次检查。不依赖未经验证的全复平面单叶性。

记

$$
a_i=\|w'\|_s,\ b_i=\|w''\|_s,\qquad
a_o=\|w'\|_{s+V},\ b_o=\|w''\|_{s+V},\qquad D=1-a_o>0.
$$

对准确恒等式 $J\circ\widetilde F_p=F_p\circ J$ 分别求
$x,p,xx,xp,pp$ 导数，完整得到

$$
\widetilde L=\frac{L(1+a_i)}D,\qquad
\widetilde P=\frac PD,
$$

$$
\widetilde Q=
\frac{Q(1+a_i)+b_o\widetilde L\widetilde P}D,\qquad
\widetilde T=\frac{T+b_o\widetilde P^2}D,
$$

$$
\widetilde B=
\frac{B(1+a_i)^2+L b_i+b_o\widetilde L^2}D .
\tag{100.18}
$$

所有交叉项保留，尤其没有遗漏
$J''(\widetilde F_p)\widetilde F_{p,p}^2$。

## 6. 有符号均值、参数域与最终门

设旧中心 $p_0$ 的真实 full twist 满足
$|\langle F_{p,p}(p_0,\cdot)\rangle|\ge\sigma_0>0$。
令 $m_0=\|w'\|_0<1$。真实均值只需实圆周预算：

$$
\left|\left\langle
\widetilde F_{p,p}(p_0+\mu,\cdot)
-F_{p,p}(p_0,\cdot)\right\rangle\right|
\le Q\|w\|_0+|\mu|T+\frac{P m_0}{1-m_0}.
\tag{100.19}
$$

证明：先比较 $F_{p,p}(p_0+\mu,J(x))$ 与
$F_{p,p}(p_0,x)$，实参数和实空间 MVT 给前两项。
再用
$\widetilde F_{p,p}=F_{p,p}(p,J(x))/(1+w'(\widetilde F_p(x)))$
得到最后一项。故从原真实下界减去 (100.19) 就是新真实下界。

若旧参数盒半径为 $\eta$，新中心只使用
$\widetilde\eta=\eta-|\mu|>0$，不扩大盒。
若 (100.12) 给中心 half 位移 $\epsilon_h$，且
$s+\epsilon_h<s_h$（$s_h$ 是该 half 界的宽度），准确平方恒等式 R77 给

$$
\|\widetilde F_{p_{\rm new}}-x-2d\|_s\le2\epsilon_h .
\tag{100.20}
$$

现在对真实 family $\widetilde F_p$ 使用 R31，初始共轭为恒等映射，
$M_0=R_0=1$；输入为 (100.18)、(100.19) 的正下界、(100.20)、
$\widetilde\eta$ 及 (100.3) 的 $K=5/2$。
实际代码保留每一个算术门的真/假，不将有限校正成功冒称为 R31 成立。

## 7. 本次确切输入与已经完成的实际校正

输入是已保存的完整 550 段端点

    data/phase_ring_continuation/step5_complete_flow_ci_43301401638/actual_endpoint.json.gz

及其所有原始 SHA 依赖。准确几何参数为

$$
p_0=-7789843107295549/4611686018427387904,\qquad
\eta=10^{-9}.
$$

旧目标的实际失败在
data/phase_ring_continuation/step5_half_prenewton_43306301976/report.json。
新目标的实际运行 43308150283 给

$$
\mu=-8.5765326650380538916480417157177567\ldots\,10^{-16},
$$

$$
\|w\|_{5/2048}<8.550795472\,10^{-12},\qquad
\|R_2\|_{5/2048}<7.9281450\,10^{-21}.
$$

$\mu$ 本身是报告中保存的准确 dyadic 分数，不以上面的小数替代。
完整真实端点残差界仍为
$7.6120461971\,10^{-13}$，经 (100.12) 得

$$
\epsilon_h<2.6781757090\,10^{-12}.
$$

新参数包含、保向和局部逆门均实际通过。旧局部二阶积分费用仍是主要项，
这份输出没有给出 R31 通过。不得把有限的 $10^{-21}$ 残差替代真实的
$10^{-13}$ 预算。

完整新报告为

    data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json

SHA256 为
030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a。
准确 $w$ 的全部系数及原始输入 SHA 同目录保存。
后处理器 fourfold_post_prenewton_R31_v1.py 检查同一报告、全部系数、
同一真实参数盒，再执行 §§5–6，不采样新的 ODE。
任何改善后的局部积分账必须先生成同身份的新完整端点，并重算预校正；
不能只替换报告里的一个显示误差数字。


## 8. 不依赖失效 runner 的实际有理 R31 预算

后处理 Python 作业 43309726544 在分配执行步骤前失败，job 的
steps 为 null；没有运行任何数学源码，原因尚未确定，原始失败另存。
这不妨碍使用已保存真实小报告中的有向界：在更宽 $5/2048$ 带上，

$$
\|w\|<9\,10^{-12},\quad
\|w'\|<1.2\,10^{-9},\quad
\|w''\|<4\,10^{-7}.
$$

以 $S=1/512-1/1048576$、$r_J=1/1048576$，§5 的全部真实域门
都可仅由这些界验证。文件
scripts/fourfold_post_prenewton_R31_exact.mjs 使用 BigInt 约分分数
计算，没有 binary64 舍入参与比较。原始两份 UTF-8 报告的 SHA256
在执行前逐字节核验；显示 Arb 球按中心加/减其显示半径转为有理外包，
没有将显示中点当成严格端点。

本次已实际执行的 27 个输入包含/连续域门全部通过，给出安全上界

$$
\widetilde P<0.010753000013,\quad
\widetilde Q<0.333126005101,\quad
\widetilde T<0.118326000189,\quad
\widetilde B<0.005574800022,
$$

以及真实下界
$\widetilde\sigma>0.0022316899840$。
新中心 full 误差的安全界为
$5.356352\,10^{-12}$。
选择 R31 的 $s_0=3/2048,\ \delta_0=1/4096,\ K=5/2$，
得到准确有理阈值所夹的小数

$$
5.9828759926908058587\,10^{-15}
<\epsilon_{\rm R31}
<5.9828759926908058589\,10^{-15}.
$$

因此当前 **error_smallness=false、parameter_margin=false、
analytic_domain_margin=true**。参数累计上界约为
$1.9201061216\,10^{-8}$，超过保守保留的半径
$9.99999\,10^{-10}$。这只是已选择充分预算未通过，不能推成真实
共轭不存在。完整分数、每个输入比较和实际失败保存在

    notes/2026-11-12-post-prenewton-exact-rational.json

这个 BigInt 计算确实已经执行；Python 后处理器仍标为未执行。
完整有理重放入口为

    node scripts/fourfold_post_prenewton_R31_exact.mjs

其重放会从同 SHA 原始小报告重新产生所有数学分数。
后续补回真实局部二阶积分时，必须先更新同一对象的真实端点和校正，
再重新支付这里的输入费用。

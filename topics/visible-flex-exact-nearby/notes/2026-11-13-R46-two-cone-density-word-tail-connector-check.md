# R46 两锥 density normal form：tail_connector 的独立短核

2026-11-13。审阅对象：
`results/R46-supplement-actual-two-cone-density-normal-form-and-base-Rstar.md`，
重点为 §§5–6。未改该冻结稿及其 source/native。

## 结论与范围

**本次范围内通过，未发现实质符号或乘积顺序缺口。**
新稿是从已有完整散射 word 及精确 symmetric-density covariance
识别整个首系数；不是从 principal return 单独猜出 R106 的 $b$。
两个 Fourier 锥的最终实系数分别为 $b(x)$ 和 $b(-x)$，但两者在
重新编号后的正频率方程中都是 $+iT_bD^{-1}$。负锥不能简单被称为
正锥的复共轭。

本次没有独立重跑约 $10^{200}$ 的全数值常数，也没有重新授予旧
strict/root/cap producer 的原生域；这些属于根代理正在执行的
完整 source/native 对照。本核验支持 §§5–6 的实际 operator
识别、必要的非酉误差和最终两锥代数，不扩大到高正 Sobolev 指标、
解析权、有效 cutoff、有限头逆或 nonlinear inverse。

## 1. 对照的原实际定义

对照了如下原文件的相关完整定义：

* R46 `actual-strong-scattering-and-return-operator-word` §§4–5 的
  $M=2\operatorname{diag}(Q_H,Q_H)\mathcal W_gJ_b\Phi_p(I+B_{original})$、
  $M_L=J_bM$、准确 $-\kappa^{-1}JM^*J\mathcal W_{st}M_L$；
* R46 `strict-negative-cauchy-phase-and-strong-remainder`
  (5.5)–(5.9)、(7.2)、(9.3)；
* R77 的明确 $P:f_-$ 从左根到右根、$B:f_+$ 从右根到左根，以及
  无角反射/平移的 $B=P$、自然提升 $R=P^2$；
* R106 `complete-actual-forward-phase` (4)–(6) 的全 one-form cut
  cancellation，及 `geometric-return-final-label` 的实际 $\Psi=J\circ\Phi$。

因此这里比较的是同一 old-object 的真实完整 word，不是新深 profile
的算子，也不是只有主特征映射的形式近似。

## 2. 半 word 的相位与方向

写真实规范化 root model 为 $2\gamma_0(0,p;q,0)$，其完整
conormal 因子是 $\kappa=(2\gamma_0)^2$。代入原 transfer word 给
$$
 M_B=q^*W_-p,\qquad M_C=p^*W_+q,\qquad
 U=M_B^*=p^*W_-^*q,\qquad V=M_C.
$$
这一步的 $\kappa$ 正好消去两个真实 $2\gamma_0$，不是假定
flux determinant 为1。

$p$ 的常 Airy 相位是 $e^{-i\pi/4}$，$q$ 的是
$e^{i\pi/4}$。故 $M_B$ 的常相位为 $-i$；取其 adjoint 后
$U$ 为 $i$，而 $V$ 本来就是 $i$。两者乘积的主常因子为 $-1$，
所以反馈 $I-UV$ 的主号为加号。

还须分清点的传播和函数的 label pullback。R77 的前向点映射为
$P$，故同支数据的 pullback 是 $Q_{P^{-1}}$。其 opposite physical
branch 从左到右的点映射为 $P^{-1}$，故数据 pullback 是 $Q_P$。
因此 $M_B$ 和 $M_C$ 的 map 方向相反；取 $M_B^*$ 后才使 $U,V$
具有相同的 $Q_P$ 主方向。这个检验排除了把两个 forward map
直接同向相乘的错误。

## 3. 完整首 one-form 与 R106 的识别

严格段的原 (5.7) 是真实输入 label 上
$$
 \widehat h_\sigma(\eta)=
 \int\frac{\mathcal F}{2\mu}(r,\Theta_\sigma(r,\eta))
                         \Theta_{\sigma,\eta}(r,\eta)dr.
$$
原物理频率为 $4|n|$，故 normal-form circle 系数为
$\widehat h/4$。R106 的 $h_{fwd}$ 已经使用保存的输入
$H(x)/4$ 并包含这个真实 Jacobian，所以最后不能再乘一次 $H'$、
4 或 $1/4$。

完整原 root phase 的 $V/(2q\sqrt\xi)$ 积分、固定-section Airy
项 $-5/(48qL^{3/2})$ 和 graph 的完整
$V+5/(16\xi^2)$ 项共同给 root 的实际 finite part。常几何项的
反向 graph 积分与固定 $L$ 项准确抵消到实际 cut；不是把它删除。
严格/root 接口处，R106 (5)–(6) 给两侧恰为
$\mp\epsilon J(V_r+\varsigma L_\theta)/4$ 的完整 one-form。
它们在取绝对值或 mean 之前逐点抵消。角 divergence、root transport
boundaries、regularized source 和 root field 都仍属于剩余的
$h_{fwd}$。

这组相同实际 density 的恒等式比“平均相等”强。新稿再使用准确的
$$
 Q_H^*A(f)Q_H=A((f/H')\circ H^{-1}),\qquad
 Q_HA(f)=A(H^*f)Q_H+E_HA(f)
$$
把完整 one-form 移到同一输出侧，$E_H$ 的全部 cross/mean 路径由
有限 order-two word calculus 支付。因此没有额外未知的 scalar
subprincipal coefficient 被留在 $b$ 中。

实际 $\chi=H\circ J\circ\Phi$ 及 R77/R101 的自然提升给
$\chi^{-1}P\chi=T_{d_*}$。保存的初始 $H$ 已在 $h_{fwd}$ 内，故
$$
 h(x)=h_{fwd}((J\circ\Phi)(x),p_\infty)(J\circ\Phi)'(x)
$$
正是正确的剩余 one-form pullback。原文件的同一个 $H$ hash 也由
consumer 检查。由径向反射，另一遍历在移动到输出前的系数为
$P_*h$，而 $P^*(P_*h)=h$；于是两条 positive-cone half word 都是
$$
 i(I+iA(h))Q_{d_*}
$$
模已付的二阶误差。这里未使用有限 Fourier 系数替换完整 nonmean。

## 4. Anti-linear 关系与非酉 circle 共轭

用原 real structure $\mathcal K$，确有
$\mathcal Kp\mathcal K=q$、
$\mathcal KW_+\mathcal K=W_-$。由于反线性共轭保留乘积次序，
$$
 \mathcal KU\mathcal K=q^*W_+^*p=V^*,\qquad
 \mathcal KV\mathcal K=q^*W_-p=U^*,
$$
$$
 \mathcal K(UV)\mathcal K=V^*U^*=(UV)^*.
$$
这里最后一行的 $V^*U^*$ 次序必不可少。

设 $Q=Q_C$，$\widetilde U=QUQ^{-1}$、
$\widetilde V=QVQ^{-1}$。尽管 $C$ 为实图，$Q$ 不是普通酉算子。
准确的未消误差为
$$
 \mathcal K\widetilde U\mathcal K-\widetilde V^*
 =E_C V^*Q^{-1}-Q^{-*}V^*E_C^*,\qquad
 E_C=Q-Q^{-*}.
$$
这显示两个 finite terms 的位置和号；新稿的两次最终 circle map
费用确实包含这两项。它不是用“$C$ 实”推出“$Q_C$ 酉”。
相反窗口须对整个乘积取 adjoint 后估计，不能沿用正窗口费用；
新稿明确保留了这一点。

## 5. 两锥的精确乘积顺序

从 positive half word 取 adjoint，再用 $\mathcal K i\mathcal K=-i$
和 $h$、translation 的实性，得到 negative half word
$$
 U_-\equiv V_-\equiv iQ_{-d_*}(I+iA(h)).
$$
写 $h_d(x)=h(x+d_*)$、$b=h+h_d$。展开完整两个因子至一次 phase，
二次 phase 项按已付 gain-two error 保留，则
$$
 (I-UV)_+\equiv I+(I+iA(b))Q_{2d_*},
$$
$$
 (I-UV)_-\equiv I+Q_{-2d_*}(I+iA(b)).
$$
两式的 $b$ 相同，但 ordering 不同。对正锥用
$Q_{2d_*}(\cdot)Q_{-2d_*}$ 后是
$I+Q_{2d_*}(I+iA(b))$，并不需要另换 $b$。
负锥用 **complex-linear** $J_{ref}f(x)=f(-x)$，所以 $i$ 不变，
$Q_{-2d_*}$ 变成 $Q_{2d_*}$，$A(b)$ 变成 $A(b(-x))$。
最后的 symmetric-to-ordered correction 已明确另付。

因此新稿 (D.32) 的两块都使用正的 $+\beta/j$ scalar arithmetic。
反射保留 mean 与完整 symmetric Fourier 权，所以 R102 的同一个
mean 区间以及 R106 的完整 nonmean bound 确可用于两块。

## 6. 本核验未授予的内容

没有由这个正确的 coefficient identification 推出实用 inverse。
两个 regular ports、root means 及其源列仍存在；$E_C$、cap、
cross-cone 和其它完整余项仍计入约 $10^{200}$ 的 base remainder。
该数值尚需实际有限头与有效高频门。新深尾的帽 realization 也须
另作已经说明的重新实例化。本核验不改变这些 scope 限制。

# R119 续篇：真实更新后长段内端 DN 的相对强界及连续 Jacobi 源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对上一续篇已经构造的真实 nonlinear annulus 解，
本篇证明其内端 Dirichlet-to-Neumann 导数在全部高频上的同宽强差小于
$2^{-8390}$。这个数是相对于实际内端高度/斜率单位的算子界，
没有除以尾标签的极小高模幅度。另给同一更新后 annulus 的连续
scalar Darboux-source Jacobi 解，明确保留完整 holonomy 源行。

由此在尾标签与长段联合消元后，长正段的非线性内端行已付；
混合尾本身的相对切口逆仍是独立未付的部分。

## 1. 同一实际解与三种强空间

沿用 [非线性筛选续篇](R119-supplement-nonlinear-screened-outer-to-inner-map.md)
的全部实际数据：
$$
 L=\omega(2^{24}-25/8),\quad 7/5<\omega<3/2,
 \quad \sigma_o=1/512,\quad \sigma_i=5177/400+1968,
$$
$$
 \sigma(t)=\sigma_o+\frac14\min\{L-t,4(\sigma_i-\sigma_o)\},
 \quad r=2^{-24},\quad r_0=2^{-8418}.
 \tag{J.1}
$$
真实解分成
$$
 h=h^0+z,
 \qquad \|h^0\|_{\mathcal Y_{\sigma_i}}<r_0,
 \qquad \|z\|_{\mathcal Y_{W_o}}\le r,
 \tag{J.2}
$$
其中 $h^0$ 的内端高度为同一 $f_B(a)$、外端高度0，$z$ 的内端高度0、
外端是任意已许 $\|f\|_{\sigma_o,2}\le2^{-29}$ 的数据。
$W_o$ 使用角权 $e^{\sigma(t)M}$ 和径向权 $q_o=e^{(L-t)/2}$。

本篇另外用 $W_i$，其径向权为 $q_i=e^{t/2}$，角权相同；
$W_0$ 则不带径向权。各 $\mathcal Y$ norm 均与该篇 (N.5) 相同，
逐模先分别取三个加权径向 jet 的 sup，再求和。源 norm $\mathcal F$
也保留同一次序。对 scalar mean 用相同径向权。
最重要的真实恒等式为
$$
 q_i(t)q_o(t)=e^{L/2},\qquad
 \|fg\|_{W_0}\le e^{-L/2}\|f\|_{W_o}\|g\|_{W_i}.
 \tag{J.3}
$$
这是完整 Fourier 卷积的强估计，适用于全部正负模式及 mean。

## 2. 内输入响应的真实 Green 与 Jacobi 解

沿用准确有限区间核
$$
 G_M(t,s)=-e^{2(s-t)}
 \frac{\sinh(M\min(t,s))\sinh(M(L-\max(t,s)))}{M\sinh(ML)}.
$$
若乘 $W_i$ 权比，$t>s$ 的指数衰减至少为 $e^{-M(t-s)}$；
$t<s$ 的衰减至少为
$$
 e^{-[(3/4)M-3/2](s-t)}\le e^{-(3M/8)(s-t)}.
$$
因而完整高度、一阶、二阶 Green 费用分别可取 $4,12,17$，总和小于64。
同一内端齐次 lift
$e^{-2t}\sinh(M(L-t))/\sinh(ML)$ 的完整费用仍为16。

在 $W_0$ 中，两半核的率分别至少是 $M$ 和 $M/4$；对应完整三 jet
费用为 $5,15,21$，总和也小于64。以上都在真实有限 $L$ 上成立。

固定外端 $f$，给内端高度变分 $\varphi\in\mathcal A_{\sigma_i,2}$。
令 $\xi=D_{f_B}\mathcal D(f_B,f)\varphi$，即非mean高度的真实 Jacobi
变化。完整 mean 继续按其小根微分，方程是
$$
 \xi=\xi_D+\mathcal G_D D\mathcal Q(h)\xi,
 \quad \xi(0)=\varphi,\quad\xi(L)=0.
 \tag{J.4}
$$
上一续篇已经逐项支付的带权理想差分给
$$
 \|D\mathcal Q(h)\xi\|_{\mathcal F_{W_i}}
 \le4096r\|\xi\|_{\mathcal Y_{W_i}},
$$
因为 $\|h\|_{\mathcal Y_{W_0}}<2r$。故 (J.4) 的线性扰动 norm 至多
$64\cdot4096r=1/64$，准确得到
$$
 \boxed{\quad
 \|\xi\|_{\mathcal Y_{W_i}}
 \le\frac{1024}{63}\|\varphi\|_{\sigma_i,2}
 <17\|\varphi\|_{\sigma_i,2}.
 \quad}                                                     \tag{J.5}
$$
同一解也是在 $\mathcal Y_{W_0}$ 中微分前篇实际 Dirichlet map 所得的解：
该空间的完整线性扰动同样小于 $1/64$，唯一性保证身份。
没有假设带内端宽输入的变化必须在整个区间保持常宽 $\sigma_i$。

## 3. 利用真背景分解支付内端相对 DN 差

记完整四状态为 $\mathcal S(h)=(P,K,U,V)$，包含 mean 小根 $K_0(h)$。
上一续篇对完整 mean 的导数证明给
$$
 \|\mathcal S(h^0)\|_{W_0}<4r_0,
 \qquad
 \|\mathcal S(h)-\mathcal S(h^0)\|_{W_o}<4\|z\|_{\mathcal Y_{W_o}},
 \qquad
 \|D\mathcal S(h)\xi\|_{W_i}<4\|\xi\|_{\mathcal Y_{W_i}}.
 \tag{J.6}
$$
例如第二式的线性部分费用为 $25/8$，mean 差分费用至多
$1024r$，二者之和小于4。它保留完整零模，未把 mean 与非零频率混算。

完整二次源的导数在每一项中都包含一个未微分的四状态因子，
余下逆/平方根系数在同一强 $W_0$ 代数中有界。
具体地，上一续篇 (N.14) 的直接证明可取总乘积系数64：
分子导数费16、分母逆小于2；微分分母产生的 $128N^2$ 项仍含
一个指定的未微分状态因子，其余 $N\le1/64$ 被系数64吸收。
因此分别代入 (J.6) 的背景两部分，用 (J.3)，得到
$$
 \|D\mathcal Q(h)\xi\|_{\mathcal F_{W_0}}
 <2048\big(r_0+e^{-L/2}\|z\|_{\mathcal Y_{W_o}}\big)
           \|\xi\|_{\mathcal Y_{W_i}}.
 \tag{J.7}
$$
这里2048是宽松常数；逐项乘积实际上给 $64\cdot4\cdot4=1024$。
本步骤使用强卷积与完整 mean 的显式差分，不交换 $\sup\sum$ 和
$\sum\sup$，也不从无权 Banach holomorphy 猜一个带权导数界。

若源 $F$ 只在变化角宽 $\sigma(s)$ 上有 $\mathcal F_{W_0}$ norm，
内端 Neumann 输出仍在 $\sigma_i$ 上。因为
$\sigma_i-\sigma(s)\le s/4$，准确端点核给
$$
 M\left|\int_0^L\partial_tG_M(0,s)F_m(s)\,ds\right|
 e^{\sigma_iM}
 \le12\sup_s e^{\sigma(s)M}|F_m(s)|.
 \tag{J.8}
$$
可用 $|G_t|\le3e^{-(M-2)s}$、$(3/4)M-2\ge M/4$ 直接积分。

记真实内端相对 DN 为
$\mathcal N_B(f_B,f)=2f_B+h_t(0)$，基态算子为
$-\mathsf C_L$，$\mathsf C_L=M\coth(ML)$。
将 (J.5)、(J.7)、(J.8) 代入 (J.4)，得
$$
 \|[D_{f_B}\mathcal N_B(f_B,f)+\mathsf C_L]\varphi\|_{\sigma_i,1}
 <2^{19}(r_0+r e^{-L/2})\|\varphi\|_{\sigma_i,2}.
 \tag{J.9}
$$
实际 $L/2>8418$、$e>2$，所以 $r e^{-L/2}<r_0$。由此得到全高频、
同一实际内端角宽的明确相对强界
$$
 \boxed{\quad
 \|D_{f_B}\mathcal N_B(f_B,f)+\mathsf C_L\|
 _{\mathcal A_{\sigma_i,2}\to\mathcal A_{\sigma_i,1}}
 <2^{-8390}.
 \quad}                                                     \tag{J.10}
$$
这里特意保留比 (J.9) 更大的余量。这个数控制整个高输入导数，不是
尾标签或几个模式的绝对 Taylor 系数。

## 4. 同一内输入的 mean 行

内端平均高度固定为真实尾给出的 $\lambda_B$，因此其变化为0。
mean 斜率按同一完整小根微分。由前篇 (N.12)，端点的真实背景四状态
norm 至多 $4(r_0+r e^{-L/2})$，所以
$$
 |D_{f_B}K_0(0)\varphi|
 <2^{13}(r_0+r e^{-L/2})\|\varphi\|_{\sigma_i,2}
 <2^{-8400}\|\varphi\|_{\sigma_i,2}.
 \tag{J.11}
$$
外端平均高度的变化准确保留为
$$
 \int_0^L aw\,D K_0(h)[\xi]\,dt,
 \tag{J.12}
$$
以及外端 mean 斜率 $w(L)DK_0(h(L))[\xi(L)]$（小根也依赖 $h_t$，
不能由 $\xi(L)=0$ 将它删掉）。全两迹转 grounded 时仍使用真实水平
变化及 normal/shear，未把 (J.10) 称作未经换元的动量 DN。

## 5. 更新后连续 scalar Darboux-source Jacobi 列

这一节加入真实连续 scalar 源 $e(t,\theta)$，其单位明确为
$$
 \delta K_t-D F_t(P,K,U,V)[\delta P,\delta K,\delta U,\delta V]
 =e,
 \qquad \delta P_t=\delta V-2\delta P.
 \tag{J.13}
$$
这是实际相对 Darboux 方程的普通体源，不是一个切口跳量。
要求 $E_e:=\|e\|_{\mathcal F_{W_0}}<\infty$，其 Fourier 求和包括 mean。
没有宣称所有 R37 metric-source 已自动满足这个具体归一化与角宽合同。

记
$$
 A_h=1+K+EU,\quad \rho=D^{-3/2},\quad
 j_h=\langle\rho A_h\rangle,\qquad
 m(t)=\delta M(t)/w(t)^2.
$$
完整 holonomy 恒等式在这个真实 exact 背景上线性化，准确给
$$
 \boxed{\quad
 m_t=-2m+\langle\rho A_h e\rangle,
 \qquad
 \delta K_0=D K_0(h)[\xi]+j_h^{-1}m.
 \quad}                                                     \tag{J.14}
$$
初值 $m(0)=m_B$ 是实际内侧 source holonomy 负荷，不能另设成0。
已付 $\|\rho A_h\|<2$、$|j_h^{-1}|<2$，所以准确积分式及强界为
$$
 m(t)=e^{-2t}m_B+\int_0^t e^{-2(t-s)}\langle\rho A_h e\rangle(s)\,ds,
 \qquad \|m\|_\infty\le|m_B|+E_e.
 \tag{J.15}
$$
源的全部高模可通过真实非径向系数贡献 mean；式子没有只取 $e_0$。

设 $Q_{\rm full}$ 为 (N.14) 的投影前完整二次源，定义实际系数
$$
 b_h=\Pi_\perp(\partial_KQ_{\rm full})j_h^{-1}.
$$
由前篇的完整商导数界，
$\|b_h\|_{W_0}\le128N<1024r$。
非mean Jacobi 方程因而准确是
$$
 \xi=\xi_D+\mathcal G_D
 [D\mathcal Q(h)\xi+b_hm+\Pi_\perp e].
 \tag{J.16}
$$
其中 $\xi_D$ 保留两端给定的非mean Dirichlet 数据；内端在宽度
$\sigma_i$、外端在宽度 $\sigma_o$，边界 norm 合计记为 $b_\partial$。
它在 $W_0$ 的费用至多16。

使用同一 $W_0$ Green 小于64、扰动小于 $1/64$，得到真正更新后的
连续强解及明确常数
$$
 \boxed{\quad
 \|\xi\|_{\mathcal Y_{W_0}}
 <17 b_\partial+67E_e+|m_B|/128.
 \quad}                                                     \tag{J.17}
$$
这对任意大小的线性输入成立，因为是同一线性 Jacobi 方程。
由 (J.14)–(J.15) 恢复全部 mean 斜率，再以唯一内端平均高度变分
$\dot\lambda_B$ 积分
$$
 \delta v_0(t)=\dot\lambda_B+\int_0^t aw\,\delta K_0\,ds.
 \tag{J.18}
$$
因 (J.16) 已解非mean residual，(J.14) 的准确 holonomy 恒等式和
$j_h\ne0$ 强迫剩余 mean residual 也为0。全部两迹及平均高度差由
(J.14)–(J.18) 输出，不额外指定第二个 mean Dirichlet 值。

给定实际 metric-source 时，仍需将其真实 Darboux RHS 换成 (J.13)
的单位，并支付有源水平 coframe、normal/shear 及全部 source 端点项。
本节只声明已经证明的 scalar 列，不删去这些后续合同。

## 6. 尾标签联合消元后只剩哪一块相对门

以同一实际尾迹记
$$
 T_f(a)=f_B(a),\quad T_k(a)=k_B(a),\qquad
 \mathcal F(a,f)=T_k(a)-\mathcal N_B(T_f(a),f).
$$
其真实导数准确是
$$
 \boxed{\quad
 D_a\mathcal F
 =D T_k+\mathsf C_L D T_f-\mathcal R_B D T_f,
 \qquad \|\mathcal R_B\|_{\sigma_i,2\to\sigma_i,1}<2^{-8390}.
 \quad}                                                     \tag{J.19}
$$
这就是与实际长段联合消元后的非mean Schur 行；mean 负荷及高度列由
§4–5 保留。对实际切口完整切向迹 $x=(DT_f b,DT_k b/M)$，最后一项
小于 $2^{-8390}$ 倍其完整高度侧强 norm，不涉及尾标签幅度的倒数。

因此长正段一侧已经有真正的相对邻域控制。尚需对混合尾自身的
$DT_k+\mathsf C_LDT_f$ 证明全部高输入的相对横截或带明确损失的强逆；
不能从 $\|D^2X\|$ 的绝对标签小量代替这一步。

[准确程序](../scripts/fourfold_updated_inner_dn_jacobi_20261113.py) 与
[完整报告](../notes/2026-11-13-R119-updated-inner-dn-jacobi-budget.json)
核全部真实权、Green、背景分解、mean/source 和 Schur 费用。

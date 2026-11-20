# R141 补充：选定成员的实际外 Robin 与 physical mean 残差值

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**状态：完整消费公式与新两标量合同；新公共数值尚未执行。**
本篇把已有的实际非线性边界残差值，传到同一个
$Q_{\delta_*}=Q_0+\delta_*Z$。旧 raw 端值、连续 repair、完整 $Z$ 端点和
全实参数外图全部只读。此处求的是值，不把 DN 导数、允许的 height 半径、
候选背景大小或普通主体源范数改称边界 RHS。

## 1. 同一成员、同一个外图、同一 height 输入

记 $Q^{\rm raw}$ 为原 ac1 moving 候选在 $R=25/8$ 的准确有理端值，
$Q_0$ 为其完整连续 repair，$Z$ 为原未除以幅度的完整193态连续方向。
三者的定义身份分别为

| 对象 | SHA256 |
|---|---|
| raw candidate | ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413 |
| continuous centre | 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47 |
| continuous direction | 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04 |

沿用 [NIF.3](R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md)
的原选定隐式 pair $(\delta_*,\mathcal H_*)$，同原 loss $1/250$，仅用已成
$$
 |\delta_*|<0.00000000009368259853002<d:=10^{-10}<r:=10^{-8}.
 \tag{O.1}
$$
$\mathcal H_*$ 是角回归共轭，绝不是外端 height。
下面的数值上界对完整 $|\delta|\le d$ 成立，故可限制到原 $\delta_*$；
没有选取一个代替它的新数值参数点，也未把选定 KAM 共轭授予整个族。

固定同一个原许可非均值 $f_B$，
$\|f_B\|_{\dot A^2}\le2^{-60}$。所有差分都保留这个相同的 $f_B$。
在固定物理 $\eta_0$ 上，完整度量定义
$E_\nu=E\exp(\nu w)$、$a_\nu=a$ 与
$\operatorname{supp}w=[1/20,9/50]$，配合
[原正帽第1节](R133-supplement-A0-contraction-and-translation-regularity.md)、
[真实长段 D.1--D.11](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
及 [cap--long 匹配 M.1--M.3](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)，
说明整个 exterior 的度量、两个端坐标及 normalized height 定义均不因
$\nu_0\mapsto\nu_0+\delta$ 改变。由同一完整长段解的唯一性，
其 $Q_\theta,d,c_0$ 是同一个非线性图。
这使用整个 exterior 的定义，绝不只凭某个局部普通源等于零。

## 2. 已完成的实际参考值

[最终 moving 候选的 F.20](R133-supplement-final-moving-centre-actual-regular-boundary.md)
和 [原实际恢复记录](../notes/2026-11-14-R133-moving0765-actual-R-boundary-restored.md)
证明，对于同一个上述 $f_B$，
$$
 R_B^0\ge\|J_\theta B^{\rm raw}
          +Q_\theta\mathcal Z^{\rm raw}-d(\mathcal Z^{\rm raw},f_B)\|_{A^0},
 \qquad
 R_C^0\ge\big|m_{\rm raw}^{-1}-C_{\rm ref}
                        -c_0(\mathcal Z^{\rm raw},f_B)\big|.
 \tag{O.2}
$$
这里 $\mathcal Z=(C-C_{\rm ref})_\perp$、
$B\circ\theta=u/v$、$C\circ\theta=1/v$、$m=\langle v\rangle$，
$J_\theta$ 是原 signed Hilbert 乘子。它在完整非均值 $L^2$ 上范数1，
真实 $Q_\theta$ 的完整乘子满足 $0<q_k<1$。

旧完整 gzip 容器84003字节，SHA256
`bb2767633225f19f27c6c2646ac47c1142352a3a03882c916868e079f0fb055a`，
在历史提交 `46f127c7153f5393dcd2a00f42d4c1d3662c294d` 的原路径
`topics/visible-flex-exact-nearby/notes/2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz`，
Git blob `aded3d60581649518060190c49e7d0524365ada5`。
它完整保留128个物理矩、全部无限尾与 alias、真实乘子误差、13个通过门、
独立物理均值以及 whole 原 $\eta$ 区间；此处只限制到 $\eta_0$。

只读其两条完整记录：

| 字段 | 原保存的 upper 球 |
|---|---|
| smaller_ball_complete_nonlinear_Robin_residual | [1.2583878575332272549321603899156131e-15 +/- 2.29e-50] |
| smaller_ball_complete_mean_C_residual | [2.0480039079869109807371951902951453e-19 +/- 1.26e-54] |

它们是原实际值证书；本篇不执行旧端值、物理矩、nonlinear cap/long 或
regular 乘子的任何生产器。对旧 record 的读取同时包含保存的端球半径。

## 3. 已完成的小输入与 moving 增量

只读以下完整旧证书：

| 旧实际对象 | 本篇消费的完整内容 |
|---|---|
| repaired outer 43601149891/1 | 全25门；right $u,v_\perp,m$ repair；固定物理角的全 $C$ 变化 |
| exact right $Z$ 43611611635/1 | 全14门；width0 的完整193态 $u,v_\perp$ 范数及准确独立 mean |
| full-delta outer 43615531666/1 | 全25门；完整 $r=10^{-8}$ 同伦、固定物理角 $C$ 变化与两个 DN 行 |
| selected NIF 43795909913/1 | 全16门及原 $\delta_*$ 的 (O.1) 限制 |
| WOBSA 43844596176/1 | 原完整18门、同选定成员与 physical endpoint 接收资格；不重算观察 |

令 $e_u,e_v,e_m$ 为 repaired summary 的三个 right-offset 上界，
$z_u,z_v$ 为 exact endpoint process 的 norms[0][0] 中 $u,v_{\rm nonmean}$
记录，$z_m$ 为该 process 的准确有理 independent mean。定义
$$
 E_u=e_u+d z_u,\qquad E_v=e_v+d z_v,\qquad
 E_m=e_m+d|z_m|.
 \tag{O.3}
$$
则 $u_\delta-u^{\rm raw}$ 的 $A^0$ 范数不超过 $E_u$，
$(v_\delta-v^{\rm raw})_\perp$ 不超过 $E_v$，而
$|m_\delta-m_{\rm raw}|\le E_m$。
这里的 full193 方向已经是物理单位；不另乘或除以原幅度。
repair 自身不随 $d/r$ 缩放，独立 mean 不由非均值范数替代。
这些仅是旧端点范数的线性组合，没有重算 Horner、旧全条带或方向。

令 $U,V$ 为 raw native 的 real $u,v_\perp$ 的 $A^0$ 上界，
$U_\sigma,V_\sigma$ 为其 $\sigma=1/8$ 条带上界。原 raw 和完整 $r$ 族
的真实均值下界都大于 $m_*:=29/5$；其符号沿原同伦保持负。
新 directed consumer 再检查
$$
 g:=m_*-V-E_v>0,\qquad b:=1-V/m_*>0.
 \tag{O.4}
$$
于是原与新端点的 $|v|\ge g$，raw 逆物理角 Lipschitz 常数不超过 $1/b$。

## 4. 同一个物理角中的完整 $B$ 值差

两角图均采用原奇 primitive 规范，
$$
 \theta_j(\phi)=\phi+\mathcal I(v_{j,\perp}/m_j),
 \qquad \mathcal I=\partial_\phi^{-1},\quad j=0,1,
 \tag{O.5}
$$
此处 $j=0$ 表 raw、$j=1$ 表 $\delta$ 成员。
在四重周期 $A^0$ 非均值空间上，$\|\mathcal I\|\le1/4$。
准确差为
$$
 \theta_1-\theta_0
  =\mathcal I\left(\frac{(v_1-v_0)_\perp}{m_1}
      -\frac{(m_1-m_0)v_{0,\perp}}{m_0m_1}\right).
$$
因此设
$$
 D_\theta=\frac{E_v+E_mV/m_*}{4m_*},\qquad
 D_\phi=D_\theta/b,
 \tag{O.6}
$$
则在同一物理 $\theta$ 上，两个真实 inverse-angle lifts 满足
$|\phi_1(\theta)-\phi_0(\theta)|\le D_\phi$。
证明是先把差放在同一 $\phi_1$，再用 $\theta_0^{-1}$ 的上述
Lipschitz 界。两张 degree-one 圆图使用相同奇 lift，没有任意常数位移。

原 Fourier 范数直接给
$\|u_0'\|_\infty\le8U_\sigma$、
$\|v_0'\|_\infty\le8V_\sigma$，因为
$|k|\le8e^{|k|/8}$。故
$$
 D_B:=\frac{E_u}{g}+\frac{U(E_v+E_m)}{g^2}
       +\left(\frac{8U_\sigma}{g}
                        +\frac{8UV_\sigma}{g^2}\right)D_\phi
 \tag{O.7}
$$
包围 $\|B_\delta-B^{\rm raw}\|_{L^\infty(\theta)}$。
确切拆分为
$$
 \left(\frac{u_1}{v_1}-\frac{u_0}{v_0}\right)(\phi_1)
       +\frac{u_0}{v_0}(\phi_1)-\frac{u_0}{v_0}(\phi_0).
$$
第一项用逐点商差，第二项用原商的真导数及 (O.6)。这是真实圆上的
两函数差，不是同阶 composition operator 减恒等的非法小范数假设。
完整物理 Fourier 尾隐含于精确复合函数中，未截断物理模。

## 5. 已付物理 $C$ 偏移与 reciprocal mean

记 $D_C^{\rm rep}$ 为 repaired summary 的
actual_fixed_physical_C_change_Aone_sixtyfourth，
$D_C^{(r)}$ 为 family summary 的
additional_full_physical_C_change_Aone_sixtyfourth。
原 family 源精确采用
$$
 D_C^{(r)}\ \ge\ r\,(\overline C^2+
             \overline C_\theta\,\overline C/4)
                    \|Z_v\|_{A^{1/32}},
 \tag{O.8}
$$
其中 $\overline C,\overline C_\theta$ 是整个 $|\delta|\le r$ 同伦的共同界，
保存公式见 fourfold_codazzi_full_delta_regular_Hs_outer.py 的 dC 分支。
在更小同伦内这些常数仍有效，所以
$$
 D_C:=D_C^{\rm rep}+\frac d r D_C^{(r)}
     =D_C^{\rm rep}+\frac1{100}D_C^{(r)}
 \tag{O.9}
$$
包围同一物理角上的 $\|C_\delta-C^{\rm raw}\|_{A^{1/64}}$。
这里只缩放原已证明的“共同导数界乘方向幅度”包络；并未声称非线性
$C(\delta)-C(0)$ 本身齐次，也未把 fixed repair 同时缩小。
正交去均值因此给
$\|\mathcal Z_\delta-\mathcal Z^{\rm raw}\|_{L^2}\le D_C$。
原与新 $\mathcal Z$ 的整个线段都在同一个 $10^{-12}$ 图域内：
可消费两端已付的完整 $A^0$ 入球门和该球的凸性。

真实物理 mean 是 $m^{-1}$，准确有
$$
 \left|m_\delta^{-1}-m_{\rm raw}^{-1}\right|
 =\frac{|m_\delta-m_{\rm raw}|}{|m_\delta m_{\rm raw}|}
 \le D_\mu:=\frac{E_m}{m_*^2}.
 \tag{O.10}
$$
它不是 moving mean 的直接差，更不是 $m_\delta-1$。
$C_{\rm ref}$ 在整个比较中为同一固定外度量数据，故准确抵消。

## 6. 从旧值与导数得到新实际值

取旧完整 family actual_DN 两条已成行
$$
 T=\|D_\mathcal Z d\|_{L^2\to L^2},\qquad
 M=\|D_\mathcal Z c_0\|_{L^2\to\mathbb R},
 \tag{O.11}
$$
分别由 Z_to_d_L2 与 Z_to_mean 的完整保存球给出。
它们是原完整低、高、mean-zero 物理输入空间的行，不只是 $P_H$ 压缩。
原复球全 nonlinear fixed-point 保证它们在上述整个真实线段有效。
固定同一个 $f_B$ 后，积分微分给
$$
 \|d(\mathcal Z_\delta,f_B)-d(\mathcal Z^{\rm raw},f_B)\|_{L^2}
 \le T D_C,\qquad
 |c_0(\mathcal Z_\delta,f_B)-c_0(\mathcal Z^{\rm raw},f_B)|\le M D_C.
$$
结合 (O.2)、(O.7)、(O.9)--(O.11)，新的完整输出为
$$
 \boxed{R_B^{\rm sel}=R_B^0+D_B+(1+T)D_C,\qquad
        R_C^{\rm sel}=R_C^0+D_\mu+M D_C.}
 \tag{O.12}
$$
它们给 [实际物理源对 S.19](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)
中带原负号的 Newton 输入
$$
 \begin{split}
 r_B&=-\{J_\theta B_{\delta_*}+Q_\theta\mathcal Z_{\delta_*}
                                      -d(\mathcal Z_{\delta_*},f_B)\},\\
 r_C&=-\{m_{\delta_*}^{-1}-C_{\rm ref}
                                      -c_0(\mathcal Z_{\delta_*},f_B)\}.
 \end{split}
 \tag{O.13}
$$
按 normalized physical-circle measure，
$\|\cdot\|_{H^{-5/6}}\le\|\cdot\|_{L^2}\le\|\cdot\|_{A^0}$，
且 (O.7) 的 $L^\infty$ 界也控制 $L^2$，所以
$\|r_B\|_{H^{-5/6}}\le R_B^{\rm sel}$、$|r_C|\le R_C^{\rm sel}$。
未除以 $\alpha$，也未预先乘未知 endpoint 坐标的 $\Theta$。
后继按原 WOB.7/S.2 两条真实 high/low affine 路径消费它们，
原 positive $H^{1/6}$ 与 negative $H^{-5/6}$ 外图仍是同一物理图的
各自延拓；本篇不在两窗口之间冒移一个未知解范数。

## 7. height、纯 $\nu$ 与尚未闭合的端口

本定理对任一同一许可背景 $f_B$ 的两个实际值成立；它没有供给一个
actual Newton height RHS。若 $y_B=s_Bf_B$ 也变动，准确方向仍是
$$
 \delta f_B=\frac{\delta y_B-f_B\,\delta s_B}{s_B},\qquad
 F_B=\||D|^2\delta f_B\|_{H^{-5/6}}.
 \tag{O.14}
$$
$2^{-60}$ 是背景的允许球，不能冒作该方向的大小。真正 far label
$k_B+C_L f_B-S_Lf_*-E_D(f_B,f_*)=0$ 的值与整体 height gauge 另付；
$(\delta_*,\mathcal H_*)$ 的共轭存在性不支付它们。

对固定物理状态、固定 same height 输入的纯 $\nu$ 列，完整 exterior
定义给其显式 Robin/mean/height 源为零；真实 state 的响应及 mean 输出
仍由原图的全微分产生。若改用 $Z$ 作为该列的已知 proposal，
它的实际边界 discrepancy 必须独立接入，不能再以显式源为零删掉。
负区、germ、root matching、独立 jumps、七高端口、原 finite-$\rho$ 和
两 WPN 总 RHS 的闭合均保持各自原资格；本篇两值不证明完整逆或曲面存在。

## 8. 新公共消费者的边界

纯数学模块只接受完整旧报告及有向 API。公共 owner 在任何 Arb 导入前，
先核全部当前字节、唯一历史84KB容器、原13/25/25/14/16/18门与完整
执行身份。原生产器只 pin 和 AST 读取，不导入执行。

新 principal targets 恰两项，依次为：

1. complete_selected_physical_Robin_Hminus5over6_upper；
2. complete_selected_independent_physical_mean_residual_upper。

每项先保存完整外舍球，再原子读回并显式 contains 原始 upper；
任何后继门仅使用读回后的 upper。中途失败保存完整已完成前缀和最后
预算阶段，不补 dummy height 或 future224/32 数字。
18个明确门与参数、字段、输入角色见独立运维合同。
新公共执行之前，本篇不给这两项任何伪造的新实际十进制结果。

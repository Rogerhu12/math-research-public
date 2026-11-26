# R144 actual：完整紧支撑均值中心的状态距离与全部 ordinary/flux 源

会话：visible-exact-astra-198c63d-20261126。日期：2026-11-26。

## 1. 本次实际结论

公共 Actions [run45797426031/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45797426031) 首次科学运行完成，child returncode=0，scientific complete/proved=true。全 7721 个闭单元、6143 个原 mean 接口、1156 个紧支撑单元和全部32 sine/32 nonconstant cosine模态被保留，27个完整新标量已保存，7722次checkpoint读回通过。

新的完整未除以振幅的同角坐标状态界约为 **1.978398124460e-5**；actual 的 `full_geometry_state_C0_sufficient_1e4` 为 **true**。这完成的是已经证明存在的 mean-exact 紧支撑中心到原 raw 候选的距离。真正非均值 GC 方程、非均值跳跃和其后的精确修正仍须完成；此处没有把新中心称为精确闭族。

完整原件：

- [scientific：27整球、全部范围与参数](../notes/localized_full_state_compact_sources_ci/run-45797426031-1/localized-full-state-and-compact-sources.json)，10486 B，Git blob `f7b66bcb9ee1d0fc45b52e3d86e6306ba6fe198c`，SHA256 `60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748`。
- [execution：完整输入、运行、读回与规则收据](../notes/localized_full_state_compact_sources_ci/run-45797426031-1/execution.json)，16110 B，Git blob `6683e76e103ac9d7ebbe5e30498a1312395e9d18`，SHA256 `f2b92ef6e63f5f54b6ebdd7997265f43100e6921a6da124b58d745b8c9d5104a`。
- [LC公式](R144-supplement-localized-full-state-C0-and-compact-source-receivers.md)、[CS完整 ordinary/divergence 分解](R144-supplement-compact-centre-ordinary-and-divergence-residual.md)、[本次执行合同](../notes/2026-11-26-R144-localized-full-state-and-compact-sources-contract.md)。

## 2. 相同对象和实际准入

原 candidate SHA256 `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`、完整 mean native `e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`、affine object `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` 均未换。固定

$$
\alpha=\frac{6890507429876859}{9007199254740992},\quad
\nu_0=-\frac{2572625729470897}{72057594037927936},\quad
\eta_0=-\frac{7789843107295549}{4611686018427387904}.
$$

旧 whole affine intrinsic box 只用来包住这个同一原中心；本次没有把其参数宽度误写为所选参数方向。19件当前小输入与10件不可变历史输入的 bytes、Git blob、SHA256及commit逐项一致；旧完整 mean 8058137 B 和原6144 cubic片全部恢复并校验。所有旧 mean/Green/Gamma、raw residual、compact moment、TM scalar gate、forward W、primitive/DFT目标调用均为0。

本次直接读 [TM actual](R144-supplement-actual-terminal-mean-small-root-and-density.md) 已证明的精确有理半径：

~~~text
rho = 21460056707081603122152938643711102791166498531461811749972659241455334243341969/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000
b = 13142628124696682772825015627534372899338540585644245009742038935869919279810971/50000000000000000000000000000000000000000000000000000000000000000000000000000000000000
~~~

它们逐字等于 TM 完整保存球的有理上端，未改成显示小数。TM 的12个mean/root/density门保持原结论，其旧粗 same-phi充分门false也保持原记录；这里的新界来自完整有限 Fourier 载体的逐格估计。

## 3. 完整同 phi 状态球

按原几何 C.1，所需范数是完整 physical moving 状态的

$$
\varepsilon_\phi=\max\{\|u_\xi-u\|_{C^0_{r,\phi}},
\|v_\xi-v\|_{C^0_{r,\phi}}\}.
$$

它包含mean和物理振幅。定义 $w=v-m$、$m_\xi=m+h_\xi$、$|h_\xi|\le b$，有

$$
u_\xi=u,\qquad
v_\xi-v=h_\xi j_\xi+\xi\chi w,\qquad
j_\xi=1+(1+\xi\chi)w/m.
$$

每个闭单元完整计算 $W_A\ge\|w\|_{A_0}$、$M_-\le|m|$ 和 $X\ge\chi$，再使用

$$
J_+=1+(1+\rho X)W_A/M_-,\qquad
E_\phi=bJ_++\rho XW_A.
$$

区外 $X=0$ 时仍保 $bJ_+$。原本 $\alpha$ 只乘一次，u在同phi处准确不变。保存的主球原样为

~~~json
{
  "decimal_exponent": "-84",
  "kind": "complete_decimal_ball_v1",
  "mathematical_direction": "upper",
  "midpoint_integer": "19783981244604355228450852648262197371682635730730763814381525091944624969714533",
  "radius_integer": "1"
}
~~~

该球含真实有向上界，实际判断使用其完整上端。已经完成的true门为 $\varepsilon_\phi\le10^{-4}$。后继若在同一坐标得到精确修正 $q_{\rm exact}-q_\xi$，必须再支付

$$
\|q_{\rm exact}-q_{\rm raw}\|_{C^0}
\le E_\phi+\|q_{\rm exact}-q_\xi\|_{C^0}.
$$

不能把中心距离单独当作最终精确状态距离。若改变intrinsic参数，仍按原几何比较及新的同对象资格分别支付。

## 4. 已完成的完整源与新跳跃

以下显示仅为完整球midpoint的十进制辨识；证明和后继输入只消费上面scientific中完整midpoint/radius/exponent球。

| 完整输出 | 显示值 |
|---|---:|
| 新 ordinary $f_u$ 的 $L^2_r$ | 8.104082664101e-8 |
| 新 flux $q_u$ 的 $L^2_r$ | 1.814378611651e-6 |
| 完整旧 $R_v-jR_0$ 接收系数 $\|c_v\|_\infty$ | 1.189370692572e0 |
| 紧支撑径向导数项 $f_{v,\chi}$ 的 $L^2_r$ | 9.756985585229e-5 |
| 新 flux $q_v$ 的 $L^2_r$ | 1.694187557396e-6 |
| 完整 first-row ordinary $F_u$ | 1.131800448910e-7 |
| 完整 second-row ordinary $F_v$ | 9.764441506945e-5 |
| first-row $H^{-2/3}$ | 1.323269448428e-5 |
| second-row $H^{-2/3}$ | 5.106438419468e-5 |
| second-row $H^{-1}$ | 2.610529132476e-5 |
| 完整 isotropic pair | 5.275107142510e-5 |
| 完整 anisotropic pair | 2.926756632289e-5 |
| 完整新 v 的 $A_0$ jump总和 | 2.690103586417e-12 |

五个新的receiver全部通过true径向长度或精确 $\int(\chi')^2\,dr$ 汇总。$R_v-jR_0$ 中原mean defect、$\xi\chi'$项、所有 changed coefficients 均已支付；没有用mean方程消掉非mean残差。first-row $H^{-2/3}$ flux仍带 $384^{1/3}$ 费用。u跳跃沿用原完整界，新v跳跃通过全6143接口和LC.16得到，未宣称任何非mean跳跃已经修复。

## 5. 完整保存、独立核验与执行

每个单元先保存完整candidate bytes，整件读回相等且每个球contains后，才将相同bytes原子写为正式checkpoint；下格仅消费保存读回上端。最终18个派生球也完成同样保存/读回。private trace的全部7721记录、14146645 B已整件核SHA256 `a5a7d905582cb4697475cd372f60ee977842220cf7145ec9a6dc371cdc61500a`，未接受尾为0；该可重建数组未发布。

root与global_geometry分别逐件读回science/execution，核全部31字段/27球、19/10输入、相同TM两个精确有理参数、全部完成计数、child0、full gate及private保存收据。执行事件提交 `ed2dcbc7acd4c99b58cb2ee2ca6d6f3b88198547`，实际science checkout `34221b7de2618031726f40fbbdb9629bf5a6cffb`；科学起止 2026-11-26T10:02:10.991496+00:00 至 2026-11-26T10:02:37.556227+00:00。Arb320bits，Python3.12.14/python-flint0.9.0/numpy2.3.5。5次pull/README核查，所存差异均为空，完整链SHA `1a9d844e55d0c62f33b20c001b7f9f93fa15fc3fff4fb3c4e6bf715af9c88aa7`。

只产生一次科学child，结果锁定。新结果没有恢复selected phase/参数资格、正侧完整逆、真正negative incoming、ν/phase Schur、全D² tame或非线性族；外jet/height/holonomy/位置周期、单一frame和regular caps仍依原open逐项完成。

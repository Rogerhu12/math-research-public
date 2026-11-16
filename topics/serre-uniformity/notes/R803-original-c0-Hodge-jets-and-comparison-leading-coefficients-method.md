# 原 c₀ Hodge 一阶与比较主函数首项的有限执行契约

日期：2026-11-16。状态：来源已经逐字节取得；以下是新公开 Actions 核的执行契约，未预填新值或非零结论。

数学依据为[原 c₀ 不分歧及比较首项证明](2026-11-16-original-c0-Hom-nonramification-and-comparison-leading-terms.md)的(C0.13)、(C0.18)、(C0.22)、(C0.24)。本计算保留原 $c_0$、$P_0=\phi(c_0)$、$t=a^3$、$C:y^2=x^3+b$ 与 $\omega_C=dx/(2y)$。这里的 $t$ 不指全局 primitive 元，输入也不是 $c_1$ 的点值。

## 1. 原来源与尺度

三组来源逐项绑定原 result、run、source commit、数学 core、完整 manifest、原配置指纹以及选入文件 bytes/SHA。

| 原来源 | 选入内容 | 本次用途 |
|---|---|---|
| R803，run43702905620 | 六组694×14准确坐标、原 M6 索引、四条补行、ratio interface、小原 $b$ 模型与原证书/meta | 六个 $U_j$ 的原全局定义及四行一阶公式 |
| R837，run43770995901 | 原 P₀ 评价、reflection minor、source audit、证书/meta | 原 $\Phi_0(P_0),\Phi_{73}(P_0)$ |
| R791，run43686308194 | 原 Hom/Galois 小文件、real descent/eta 输入、证书/meta | 五个原 $p_j/q_j=2+r_j$，保持原方向 |

R803 精确坐标文件同时保存整数尺度基坐标和无尺度基坐标。本核只读取
`coefficients_in_unscaled_original_M6_basis`；其对应原 $F_k$，不再乘或除 $82^6$。
原另一套基的尺度仍作为源检查固定为 $82^6=304006671424$。

R837 原值是
$$
\Phi_i=(82^2T_i)E_6/E_4^2,
$$
自带尺度 $82^2=6724$。先按原两坐标
$A+B\zeta=(A-B/2)+(B/2)s$ 运输到 $K$ 的 $(1,s)$ 基，$s=1+2\zeta$、$s^2=-3$；不得把这些值当作裸 $T_i(P_0)$。

R803 的原 $4/1722^3$ Hodge 标准化已经在准确坐标中恢复。本核不插入另一个1722因子、$\rho_j$ 或 CM 点相位。

## 2. 六组值与一阶

令 $A_{jk}$ 为上述无尺度坐标，$V_j=U_j/E_6$。原四条末行 recipe 必须逐项为
$$
(F_{690},F_{691},F_{692},F_{693})
=(E_4T_0,E_4T_{73},E_6,\eta_{\rm Ded}^{12}).
$$
核据原源实际验证 recipe 和完整1680行准确证书，然后只计算
$$
\begin{aligned}
V_j(0)&=A_{j,692}-A_{j,693}/(24s),\\
V_j'(0)&=-4\bigl(A_{j,690}\Phi_0(P_0)+A_{j,691}\Phi_{73}(P_0)\bigr)/6724
             -A_{j,693}/(12s).
\end{aligned}
$$
前690行带 $R^2$、$R=E_4^3/E_6^2=O(t)$，所以不进入本阶。这里没有新生成它们的 CM 值或 Fourier 系数。

六个输出均是原 $L=\mathbf Q(b,s)$ 的14个准确有理坐标。原 $b$ 的八项首一最小多项式逐字读取 R803 的 `original_b_model`，不改用整缩放 $B=\lambda b$，也不换椭圆扭曲。每个 $V_j(0)$ 的非零性由本次准确值检查，而不把纸面存在性冒作已运行数值。

## 3. 原微分及 λ 立方

对 $h=f,g_1,\ldots,g_5$，原定义是
$$
W_f=V_0,\qquad W_{g_j}=(V_0+V_j)^3/V_0^2.
$$
核检查 $V_0$ 和每个 $V_0+V_j$ 的准确非零，所有求逆均准确乘回。使用
$$
\frac{W_{g_j}'}{W_{g_j}}
=3\frac{V_0'+V_j'}{V_0+V_j}-2\frac{V_0'}{V_0}
$$
计算对数导数；共享的 $V_0^{-1}$ 只求一次并复用。输出还保留 $W_h$ 的值和普通一阶、$\lambda_h^3=108W_h(0)$ 及其一阶，以及 $\lambda_{g_j}/\lambda_f$ 的值和一阶。

原共同单位 $(1-2t)/(1-t)^2$ 在0的值1、一阶0。因此立方的一阶同样是 $108W_h'(0)$。全程不选立方根。

## 4. 真实七次 norm 与 trace

在原 $K=\mathbf Q(s)$ 基 $(1,s)$ 上，以
$$
1,b,b^2,\ldots,b^6
$$
为 $L/K$ 基。对任意原输入 $x\in L$，按原首一多项式构造7×7的乘 $x$ 矩阵。其行列式正是 $N_{L/K}(x)$，迹正是 $\operatorname{Tr}_{L/K}(x)$。这一定义本身保留所有七个真正共轭和原 $\sigma(b)$；它不是同靶 $T$ 的乘积。

本核准确计算六个
$$
M_h=N_{L/K}(108W_h(0)),\qquad
Q_h=\operatorname{Tr}_{L/K}(W_h'(0)/W_h(0)).
$$
输出两项原 $K$ 坐标，不先投影到 $\mathbf Q$。每个 norm 的完整乘法矩阵及7步非零 pivot 记录随阶段保存；trace 的原乘法矩阵也保存。只有这些七维常数问题，不构造曲线函数域的272维新乘法或任何全局大逆。

## 5. 五个原比较首项

从 R791 的 `degree_zero_basis[j-1].degree_zero_coefficient_dj_over_d0` 读取原 $r_j$，准确形成约分后的 $p_j/q_j=2+r_j$。不将原 $\kappa$ 或 $v^\dagger v$ 设为1。

对原
$$
\mathcal R_j=N_{L/K}(y_{g_j}^2-b)^{q_j}/N_{L/K}(y_f^2-b)^{p_j}
$$
输出
$$
\mathcal R_j=\kappa_jt^{14(p_j-q_j)}(1+d_jt+O(t^2)),
$$
其中
$$
\kappa_j=M_f^{2p_j}/M_{g_j}^{2q_j},\qquad
d_j=-\tfrac12(q_jQ_{g_j}-p_jQ_f).
$$
六个 $M_h$ 的两项有理坐标准确展开。$\kappa_j$ 保存为五节点准确整数幂 DAG，源叶为这六个实际 norm；全部分母非零已由实际 norm 检查。数百次幂不必展开成巨大整数。$d_j$ 的两项 $K$ 坐标准确展开，并记录第二坐标实际是否为零；不预填 $d_j\ne0$。

这些常数是原主函数比较在指定 $c_0$ 单项式帧中的标量与首单位项。它们不替代全部 Poincaré 刚性化、对称 theta 线丛比较、第二类 splitting 或指定高度。

## 6. 公共接口与断点

核心文件 `scripts/R803_original_c0_Hodge_jets.py`。

`RESULT=R803-original-c0-Hodge-jets-and-comparison-leading-coefficients`。

`FINAL=p41-original-c0-Hodge-jets-and-comparison-leading-coefficients-certificate.json`。

CLI 为 `--config <expanded-job> --out <output> --budget-minutes 300`。
expanded job 给三组原来源的绝对目录和逐文件清单；绝对目录、工作预算不进入数学身份。core、本文、c₀ 证明、三组原配置与全部选源 SHA 进入不可变 tag。

所有新数学阶段是根目录 `R803-c0-*.json.gz`：一个 source audit、六个 $V$ jet、六个 $W$/立方 jet、六个 norm/trace、五个比较首项，以及实际 complete 阶段清单。阶段先原子写临时文件再替换，重复启动只复用同 tag 的已成阶段。预算只在原子阶段之间停下；未完成 FINAL 不作成功证书。

入口直接检查原公开仓库 Actions 环境，并先调用 `sys.set_int_max_str_digits(0)`，使已成数千位原坐标的读取与写出不受 Python 默认4300位限制。该设置不改变任何数值。

成功只在全部6/6/6/5阶段完成后发布。最终证书显式保留未计算标志：没有新 Fourier、Hodge、CM torsion、原 $A/B$、整体函数域大矩阵、立方根、完整刚性化、高度或全 $p$ 排除结论。

所有新运算仅在本公开仓库 GitHub Actions。源码与小请求进 Git；原数据、准确大整数、输出 DAG 和一日源载体仅进对应临时 artifact。

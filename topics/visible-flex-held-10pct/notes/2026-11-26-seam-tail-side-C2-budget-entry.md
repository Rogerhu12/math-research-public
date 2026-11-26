# 新输入的尾侧 C² 修补与连续预算入口

日期：2026-11-26。此项准备
[seam_tail_correction.py](../scripts/resume_20261126/seam_tail_correction.py)，
供新 accepted 前缀和实际导出的同一共享 $R$ 尾图使用。
当前没有新场数值输出；已执行语法检查和 18 个实际 $R$ 端点恒等式校准。
旧桥、深帽、cell 7 或 warm 场的预算均不会自动转移到新场。

## 1. 输入必须是两个真实、完整绑定的端点

桥输入是新 `seam_bridge_cut_trace.py` 的 NPZ 及其绑定 JSON。
尾输入是原 shared-$R$ exporter 的 stage 0 及同一 manifest：
`literal_R_stage_with_exact_common_boundary_two_jets` 和
`selected_stages_share_one_literal_R_C2_definition`。
工具检查 stage 文件 SHA、mapHash、公共 mean-chain、原 accepted 包
及同一 source port，重新使用原 residual/solveTolerance 和背景配置核验。

尾 cut 必须是实际 canonical node 0，包含全部平面和高度 Fourier 的
0、1、2 阶系数。平面 V 系数加回真实背景的
$(R_c,1,0)e^{i\theta}$；高度采用真实 R58 背景导数，保存的扰动 mean
完整保留，且 cut mean 的位置值逐字核对原累计链。

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_tail_correction.py" \
  --bridge-trace "$WORK/current-cut-R-jets.npz" \
  --bridge-certificate "$WORK/current-cut-R-jets.json" \
  --tail-stage "$WORK/shared-tail/stage-0000.json.gz" \
  --tail-manifest "$WORK/shared-tail/manifest.json" \
  --source-port "$WORK/m24-linear-port.json" \
  --out "$WORK/tail-side-correction-budget.json"
~~~

可选 `--lengths` 给出精确有理长度列表；
默认另加入所提供 stage 0 宽度的一半。
超出该 stage 实际 $R$ 区间的长度会标成未覆盖，不拿缺失的邻 stage 当已有输入。
有原同图基线证书后才可通过 `--conditional-baseline` 传入
`metric,eta,beta`，以及可选 `radius,support` 的严格上/下界。
这个入口始终将组合值标为条件预算，不把任意输入的几个数字当成证书。

## 2. 显式修补作用在尾侧

令 $\Delta_j(\theta)$ 为实际桥减实际上尾在公共 $R$ cut 的完整第 $j$ 阶
径向 jet，$j=0,1,2$。选择 $\ell>0$，在
$R\in[R_c-\ell,R_c]$ 定义

$$
P(R,\theta)=\sum_{j=0}^2(-\ell)^j
H_j\left(\frac{R_c-R}{\ell}\right)\Delta_j(\theta),
$$

$$
\begin{aligned}
H_0(u)&=1-10u^3+15u^4-6u^5,\\
H_1(u)&=u-6u^3+8u^4-3u^5,\\
H_2(u)&=\tfrac12u^2-\tfrac32u^3+\tfrac32u^4-\tfrac12u^5.
\end{aligned}
$$

令新尾为 $F_{\rm tail}+P$，在 $R\le R_c-\ell$ 处保持原尾。
精确有 $P_{R^k}(R_c,\theta)=\Delta_k(\theta)$ 和
$P_{R^k}(R_c-\ell,\theta)=0$，$k=0,1,2$。
对角度再微分给出全部混合二阶等式，故是完整 Cartesian $C^2$ 接续。
修补跨越原公共 $R$ knots 时仍为同一光滑多项式，不破坏原内部 $C^2$。
原三重 Fourier 频率族也保持不变。

在 $z_b=Z_c+\mu_c$ 的原高度常数合同下，$\Delta_{0,0}=0$
先精确符号消去。其他 mean jet 若有差，修补会有明确零模；
**最终总 mean 在支撑内会改变**。原保存 mean 只是完整保留为固定基线，
没有被归零、重积分或替换；额外修补必须支付下面的误差。

$\Delta_j$ 指相同的 computable-real 桥迹表达式减原字面尾系数。
区间中点仅用于多项式上界的中心分解，绝不把中点指定为接缝目标值。

## 3. 连续全角和径向上界

对每个 Fourier 模，以精确有理数将该模的三条区间系数写为中心加半径，
先合并中心多项式，再对径向子区间转成 Bernstein 系数。
区间半径乘同一 Hermite 基导数界；角导数乘真实整数频率。
按每个径向盒先合并全部平面/高度模，最后取盒最大值。
所得

$$
b_{ij}\ge\sup\|\partial_R^i\partial_\theta^jP\|
$$

覆盖 $(i,j)=(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)$，
没有以采样替代连续角度或连续半径。

置 $r_-=R_c-\ell$。在 R58 的同一个真实背景
$g=E\,dR^2+R^2d\theta^2$ 上，$E\ge1$，故

$$
\|DP\|_g\le\eta,\qquad
\eta^2=b_{10}^2+\frac{b_{01}^2}{r_-^2}.
$$

R58 的 $|w|\le.41$ 和 meridional 主曲率不超过 $8$
给出 $|E'|/(2E^2)\le3.28$。在背景正交标架中，

$$
\begin{aligned}
H_{00}&\le b_{20}+3.28b_{10},\\
H_{01}&\le b_{11}/r_-+b_{01}/r_-^2,\\
H_{11}&\le b_{02}/r_-^2+b_{10}/r_-.
\end{aligned}
$$

因此可取

$$
\|\nabla_g^2P\|\le\beta
=\sqrt{H_{00}^2+2H_{01}^2+H_{11}^2}.
$$

平方根通过整数平方根有理外包，最终十进制显示再次向外取整。

## 4. 必须来自同一实际 map 的条件组合

若原尾在所用区间上有连续相对度量界 $\varepsilon_0$，
则修补后的同一目标度量误差满足

$$
\varepsilon_1\le
\varepsilon_0+2\sqrt{1+\varepsilon_0}\,\eta+\eta^2.
$$

若原尾相对真实背景的扰动 $V$ 还满足
$\|DV\|_g\le\eta_0$、$\|\nabla_g^2V\|\le\beta_0$，
且 $\eta_0+\eta<1$，则

$$
K_1\le\frac{8+\beta_0+\beta}{(1-\eta_0-\eta)^2}.
$$

若另有原位置范数上界 $\rho_0$、支撑下界
$s_0\le\langle F_0,n_0\rangle$，置
$t=2\sqrt{1+\varepsilon_0}\eta+\eta^2$。
只有 $t<1-\varepsilon_0$ 时，叉积不退化、法向取向保持，并可用

$$
\|n_1-n_0\|\le\frac{2t}{1-\varepsilon_0},\qquad
\|F_1\|\le\rho_0+b_{00},
$$

$$
\langle F_1,n_1\rangle
\ge s_0-b_{00}-\rho_0\frac{2t}{1-\varepsilon_0}.
$$

工具没有重新证明这些基线数字属于当前场；
只有真实同图证书和全部身份绑定补齐后，组合才是该场的证书。
尤其不能拿旧 warm `.25 H` 的已付界填入新 full-H 字段。

这个局部修补不改变目标 $g$，但改变实际尾图。
若用于满足同 $g$ 精化标准，还须用实际新场证明修补量随精化减小，
不能因为有限误差小就宣称得到精确等距极限。

# 实际 SO(3) 节点的向外包围与工作值费用

本件落实 R694 的实际节点值误差输入，承接
[连续积分函数包络](2026-11-26-direct-axisymmetric-continuous-integrand-envelopes.md)。
完整源码：
[so3_axisymmetric_outward_nodes.py](../scripts/resume_20261126/so3_axisymmetric_outward_nodes.py)。

本件只包围同一准确场的
$$
T(s,\phi)=\exp([\omega(s,\phi)]_\times)
 \{b(s)e_r(\theta_0(\phi))+c(s)e_z\}
$$
及 $T_\phi,T_{\phi\phi},T_s$，并支付这些节点向量的完整实际求值误差。
它不重定义固定标量度量，不冻结自由 core/H，也不删除旋转自由变量。
它不是 $F=G+h\Delta$ 的完整证书。积分权与 Peano 误差、core 逆图、
cap 以及完整六 jet 的加乘链由相邻完整消费者支付。

所有科学求值只允许在本公开仓库 Actions。
本次交付前仅做源码审读、AST/compile 和文本身份检查，未运行科学 fixture。

## 1. 相同对象与明确的工作重读

入口严格使用已刊 `a846d373…` 的 `ActualInput`，继承以下完整检查：

- 实际 `606e0048…` driver 报告与 `7f26ff35…` checkpoint 的完整 schema/model；
- 选定 initial/final 状态与其实际文件 SHA256；
- `4e65577d…` 独立 reference、observations、原 exact-node report、scalar gzip、prepare report；
- 同一准确 scalar profile definition、全部 affine 节点、完整 omega/core/H；
- 全部 160 个 fixed-chart core 系数及当前 core 的原三个固定系数；
- 每个依赖的实际字节身份。

没有硬编码某次 run 的 profile identity，也不将旧 q 场或 zero-closure 场改标签接入。
按实际报告的 integration order、angle block、root iterations/tolerance
重建真正 `7f26…` 算子；用其 `load_checkpoint` 读取完整当前向量。
重建后 model/identity 必须逐字相同，core、全部 omega node jets 和 H 必须保留实际 words。
暴露的 `.x` 为只读完整自由向量，准确 omega 与 fixed-chart core 也作只读副本。

工作值来自本次同源 `_meridians` 的真实重读。
不声称它与旧 run 中未保存的另一 BLAS batch、缓存或规约逐位相同。
记录旧工作参数、本次实际库版本和 fresh-read 计数。
后继应使用本件返回值，或继续支付它再次重读的差额。

部分径向查询一律使用 `label='arbitrary'`。
原 `integration/grid` 缓存键只含 angle block，隐含径向查询是完整原集合；
不能把部分胞伪作这些保留 label。
本件不调用完整 $F$、$J$ 或 $J^*$。

## 2. 准确节点与全部 Fourier 模式

准确网格是 $s_j=\alpha_jS+\beta_j$。
对整数胞号 $j$ 和 literal binary64 $u\in[0,1]$，
$$
s=(1-u)s_j+us_{j+1},\qquad
\ell=(\alpha_{j+1}-\alpha_j)S+\beta_{j+1}-\beta_j.
$$
$u$ 转成该 word 的准确 Fraction；没有先打印十进制改变值。
胞宽先作符号差再包围，必须获得严格正下界。
数值 `mesh[j+1]-mesh[j]` 只是工作 carrier。

六个 endpoint words 按原顺序
$(y_0,u_0,a_0,y_1,u_1,a_1)$ 定义物理 quintic。
令
$$
c_0=y_0,\ c_1=\ell u_0,\ c_2=\ell^2a_0/2,
$$
$$
e_0=y_1-c_0-c_1-c_2,\quad
e_1=\ell u_1-c_1-2c_2,\quad e_2=\ell^2a_1-2c_2.
$$
则
$$
c_3=10e_0-4e_1+e_2/2,\quad
c_4=-15e_0+7e_1-e_2,\quad
c_5=6e_0-3e_1+e_2/2.
$$
物理 $s$ 导数为 $\ell^{-1}\sum_{k=1}^5kc_ku^{k-1}$。
复用已刊 continuous input 的准确区间实现。

三个 world 通道为
$$
\omega_x=\sum_{m=0}^{M}x_m(s)\sin((2m+1)\phi),\quad
\omega_y=\sum_{m=0}^{M}y_m(s)\cos((2m+1)\phi),
$$
$$
\omega_z=\sum_{m=1}^{M}z_m(s)\sin(2m\phi).
$$
$M=160$ 时保全部 482 个通道。
先对每胞六个 power 系数作完整 Fourier 和，角导数 0、1、2 各自全付，
再在需要的 $u$ 上 Horner 求值。这只是有限和交换次序。
仅当一个 mode 的六个 literal endpoint words 全为准确零，才跳过它的零贡献。

工作侧仍使用原 `q._angular_nodes/_radial`。
准确宽度与其数值 Hermite 的差由末尾的真向量盒到工作 word 的距离整体支付。

## 3. 固定材料图及准确 $T_0$

固定图使用参考的全部初始系数 $c_m^0$，不是当前 core。
设 $\nu_m=2m,\ q_m=1-\nu_m^2$，
$$
\theta_0=\phi+\sum_m(q_m/\nu_m)c_m^0\sin(\nu_m\phi),
$$
$$
\rho_0=1+\sum_mq_mc_m^0\cos(\nu_m\phi),\quad
\rho_0'=-\sum_m\nu_mq_mc_m^0\sin(\nu_m\phi).
$$

`fixed_chart(phi)` 与 `chart_for_core(core,phi)` 返回
`theta/rho/rho_phi/er/et/phi`。
其中 frame 对应材料角 $\Theta_c(\phi)$。
`normal_frame(phi)` 返回普通参数 $\phi$ 的 frame；后继 $\Gamma_c$ 消费者不可混用。

参数可为 literal float、准确 Fraction 或两个准确 rational endpoints；
区间输入包围整个角区间。三角函数全部采用 `e091…` 的准确整数
Taylor/$\pi$ 包围，不以数值库 trig 作为严格 oracle。
本 API 不自行宣称 $\rho>0$，全角正下界留给完整 core 消费者。

准确参考规定
$$
U=T_0=b e_r(\theta_0)+c e_z,\qquad b^2+c^2=1,\quad c\ge0.
$$
准确 affine 点直接消费完整 `WholeAxisymmetricLaw.boxes`：
原 quintic prefix、analytic extension、完整 Hold、R690 无限 deep tail 全保。
近帽处用稳定 angle/sin/cos，不用浮点 $\sqrt{1-b^2}$ 提前抹零垂向分量。

完整所需 jets 为
$$
U_s=b_se_r+c_se_z,\quad U_\phi=b\rho_0e_t,\quad
U_{\phi\phi}=b(\rho_0'e_t-\rho_0^2e_r).
$$
工作 provider 的数值 normalization 原样保留，其费用没有假定为零。

## 4. 同一矩阵 Taylor 的快速形式和全局余项

对 $L\ge2,\ W=[w]_\times,\ z=w\cdot w$，由 $W^3=-zW$：
$$
P_L(W)=\sum_{j=0}^{L}W^j/j!=I+A_L(z)W+B_L(z)W^2,
$$
$$
A_L(z)=\sum_{k=0}^{\lfloor(L-1)/2\rfloor}
 \frac{(-1)^kz^k}{(2k+1)!},\quad
B_L(z)=\sum_{k=0}^{\lfloor(L-2)/2\rfloor}
 \frac{(-1)^kz^k}{(2k+2)!}.
$$
源码对这两个有限多项式及其一、二阶导数作准确区间 Horner。
这是原 degree-$L$ 矩阵 Taylor 的准确恒等式，没有换近似函数。

实 skew 指数的 simplex/Duhamel 公式给出
$$
\|D^k\exp(W)[A_1,\ldots,A_k]\|_2\le\prod_i\|A_i\|_2.
$$
指数因子均正交；$k!$ 个 simplex 的总质量是 1。
无需 $e^{\|W\|}$ 因子或小角条件。

若 $r\ge|w|,\ r_1\ge|w_\phi|,\ r_2\ge|w_{\phi\phi}|,\ r_s\ge|w_s|$，
可取
$$
e_0=r^{L+1}/(L+1)!,\quad e_1=r_1r^L/L!,
$$
$$
e_2=r_2r^L/L!+r_1^2r^{L-1}/(L-1)!,\quad e_s=r_sr^L/L!.
$$
一阶 $D\exp$ 的 Taylor 次数是 $L-1$，二阶 $D^2\exp$ 是 $L-2$。
这些余项对应完整链
$$
R_\phi=D\exp(W)[W_\phi],\quad
R_{\phi\phi}=D\exp(W)[W_{\phi\phi}]
 +D^2\exp(W)[W_\phi,W_\phi],\quad R_s=D\exp(W)[W_s].
$$

节点用 $V=w\times U,\ Z=w\times V$ 避免重复矩阵乘法。
全部产品法则为
$$
V_\phi=w_\phi\times U+w\times U_\phi,\quad
V_{\phi\phi}=w_{\phi\phi}\times U+2w_\phi\times U_\phi+w\times U_{\phi\phi},
$$
$$
Z_\phi=w_\phi\times V+w\times V_\phi,\quad
Z_{\phi\phi}=w_{\phi\phi}\times V+2w_\phi\times V_\phi+w\times V_{\phi\phi}.
$$
径向保 $V_s=w_s\times U+w\times U_s,\ Z_s=w_s\times V+w\times V_s$。
另保
$z_\phi=2w\cdot w_\phi,\ z_{\phi\phi}=2(|w_\phi|^2+w\cdot w_{\phi\phi}),\
z_s=2w\cdot w_s$。

因此对准确单位 $U$，向量余项为
$$
E_T=e_0,\quad E_{T_\phi}=e_1+e_0|U_\phi|,
$$
$$
E_{T_{\phi\phi}}=e_2+2e_1|U_\phi|+e_0|U_{\phi\phi}|,\quad
E_{T_s}=e_s+e_0|U_s|.
$$
每个分量扩大 $[-E,E]$ 即包含真向量。
一般 primitive 允许非单位 $U$，首项显式乘 $|U|$ 上界。

`IntervalSO3.rotation_jets` 以三单位基向量作列，给
`R/Rp/Rpp` 及命名 `DR[name]` 完整整数矩阵盒。
对任意 real-skew 方向 $[v]_\times$，其余项为 $|v|r^L/L!$。
独立 zero-closure binder 可组合这些纯 primitive；
不会为此放松本件实际 hDelta schema。

## 5. 到真实工作 word 的整体误差

设真分量在 $[a_i,b_i]/Q$，$Q=10^{72}$，本次工作 word 为 $\widehat t_i$。
准确分量费用是
$$
\epsilon_i=\max\{|a_i/Q-\mathrm{Fraction}(\widehat t_i)|,\
 |b_i/Q-\mathrm{Fraction}(\widehat t_i)|\}.
$$
向量费用用已刊 R694 的准确向上平方根
$$
\epsilon=\mathrm{sqrt\_upper}(\epsilon_1^2+\epsilon_2^2+\epsilon_3^2).
$$

由此整体支付本节点全部前向差异：准确 width 与数值 Hermite、
固定 chart 与全部 Fourier 求和、scalar carrier 与 normalization、
原 Rodrigues 分支/级数、实际 trig、矩阵乘法及向量内部全部加乘规约。
不需要未经证明的数值库 ulp 假设。
非有限、缺分量或错形状的工作值诚实失败，不产零费用。

这仍不是完整数值场证书。
后继必须将实际权重（含 signed partial weights）视为准确 literal 值，
用节点费用支付积分差，再加 Peano 与完整 $h\Delta$ 算术费用。
如果再次调用 `fields_torch`，须把其真工作六 jet 与所用工作节点的准确有理
重建比较，继续支付 block/规约改变。不能默认不同批次逐位相同。

## 6. 固定 API

~~~python
actual = load_actual(args)
evaluator = NodeOutwardEvaluator(
    actual, working_cache_directory=fresh_path, exp_order=24)
q, x = evaluator.q, evaluator.x
result = evaluator.evaluate(cells, literal_u, literal_phi)
~~~

`cells/local_u` 长度 $P$，独立 `phi` 长度 $A$。
对 `key in ('T','Tp','Tpp','Ts')`：

| 字段 | 内容与形状 |
|---|---|
| `working[key]` | 本次真实 `float64(P,A,3)` |
| `intervals[key]` | `(lower,upper)`；各为 SCALE 整数 `object(P,A,3)` |
| `component_error_upper[key]` | 准确 Fraction `object(P,A,3)` |
| `norm_error_upper[key]` | 准确 Fraction `object(P,A)` |
| `exp_remainder_upper[key]` | 向量 Taylor 余项，Fraction `object(P,A)` |
| `query` | 原 `q.make_query` 返回，含工作宽度和 partial 权 |
| `radial_addresses` | 准确 affine 定义、literal u、准确 s/宽盒与工作 carrier 差 |
| `phi_hex` | 全部 binary64 角地址 |

`working(...)` 可单独真读同源节点。
`enclose_node(cell,u,phi_interval)` 只产真盒，包括 omega/T0 四组 jets、
scalar boxes 和固定 chart；角区间输入不冒称单点工作值。

后继可直接复用 `q.make_query`、`q._integrate` 和只读 `.x`。
同 angle block 的数值 angular nodes 缓存可替换；
准确端自动只保当前胞的 Fourier power，多胞切换不累计巨型缓存。
已绑定 scalar point 盒可复用，不删除任何永久几何位置。
缓存策略不进入数学目标 identity。

## 7. 完整可执行入口与范围

~~~sh
python so3_axisymmetric_outward_nodes.py \
  --repo REPO --report ACTUAL_REPORT --checkpoint ACTUAL_CHECKPOINT \
  --reference-bundle ACTUAL_REFERENCE_NPZ --carrier ACTUAL_OBSERVATIONS_NPZ \
  --node-report ACTUAL_NODE_JSON --scalar-input ACTUAL_SCALAR_GZIP \
  --preparation-report ACTUAL_PREPARE_JSON --state final \
  --outdir OUTPUT --exp-order 24 --admission-seconds 600
~~~

默认消费全部原工作 integration 与 observation 节点的并集，
全部原 quarter-angle 地址保留。仅完全相同 binary 地址可合并重复求值；
本件不更改任何 objective 权重。

可传 `--requests`，schema 为
`actual-node-direct-axisymmetric-SO3-literal-requests-v1`；
`blocks` 每项含 `cells/local_u_hex/phi_hex`。
此时只宣称所列有限请求完成，不把子集冒作原全节点集合。

每个完整 block 后写 hash-chain journal。
自然预算到期返回已完成/未完成数量和真实 maxima；
部分读数不提升成完整 scope。
`--resume` 保同 source、实际 checkpoint、query plan、Taylor degree 与输出模式。
`--write-node-records` 可保存完整原始盒、工作值和 fees 的压缩 JSON，
只存 runner，不作为参数上传 Git。

完整 report 明确没有完成连续全曲面、core 逆图、cap、$h\Delta$ 六 jet、
reach、固定度量精化或非平凡连续相位族。
若实际费用因宽盒或不足 Taylor degree 较大，记录真上界，再提高求值精度；
这种求值加密不改变固定准确 profile、同一场系数或原求解问题。

## 8. 完整默认遍历的性能修订

未刊初稿 32c08ca2 源和说明保留在本次工作区；本次首次刊出的完整源是 1371e493。最终默认遍历按 angle block 为外层、原胞号为内层；同一个 phi block 的全 J923 个 angular-node 张量可真实复用全部 922 胞。旧 cell-major 顺序会在每胞切换全部 angle blocks，而工作缓存只保最后一个 block，导致重复全径向 Fourier 矩阵乘。此处只交换完整有限查询的遍历次序，全部同一 binary 地址、数学包围和逐节点工作值费用不变；新 `query_plan.traversal_order` 和完整源码 SHA 均绑定该选择，不能续用旧顺序 journal。显式 requests 仍保其明示的完整 block 顺序。

完整首次刊出源 SHA256：`1371e4936af27d2122a84bb720e8c67db5d0db712df42eec12a4579f91943f89`，43734B。root已完整审读源、主入口及证明；solver核实际工作接口，geometry独立核完整旋转 jets/Taylor 余项，全部为静态审查。完整600秒参数仅ready，不预填运行成功，也未在尚无606末场时排昂贵全节点计算。

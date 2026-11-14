# Saved stage43：R271 全列离散协变与频率平衡候选接口

2026-11-14，/root/geometry，GPT-6 Astra Pro，AI 辅助。本文交付独立源码与具体有限数组定义，尚未运行本次新科学计算。本地仅 AST 与只读源码检查；所有矩阵形成、精确参考和误差测量只在本公开仓库 Actions 执行。

## 1. 为什么现在只改已保存四 A 的算术表示

[actual47 捕获](2026-11-14-actual-request47-original-step-capture.md) 已使原41 shortJ、当前同次 observed shortJ、四个实际局部 A 的有理 RK4 成为可区分的对象。旧与新 observed 的完整矩阵字节相同。原 new519 行账还显示，把有理四级 map 直接代入旧 actual43 方向并没有使这个方向有效。

因此本入口只回答一个具体问题：对已经固定的四个 A，是否能用 [R271](../results/R271-discrete-RK-stage-gauge-covariance.md) 的完整逐级坐标输运，更准确地形成全部224个形状输入列及两条 mean 输出？它同时保留同一工作精度的原坐标直接 RK4 对照，由独立有理参考逐项比较。它不沿用旧方向做非线性试步，不重取根或局部 J，不承诺新的方向已经存在。

新源：

- computations/geometry_20261114_saved_stage_rk_covariance.py
- 27,929 bytes
- SHA256：01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548
- Git blob：5c578f325d6840fc835958652d6c663a6a9b8b56

新入口只使用 Python3.12.14 和 numpy2.3.5，以及冻结的输入读取助手 exact_20261114_single_step_rational_action.py（SHA9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e）。它不需要 Node、SciPy、原 public78 源恢复或 native worker。

## 2. 完全固定的输入

必须指定 actual47 的真实 capture result：

~~~text
da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403
~~~

冻结助手核四个完整226×224的原 binary64 A、原21数组 manifest、原 h/port/sigma、源身份、原状态及几何复现。新入口还从已绑定的小原件读取：

- window identity：2608bb3b27cfd16020fcdbaf2bae6c8c9b63cb85146d6c5198d1905b4f64e450；
- capture spec：f813683b76caf4ede4b73bdc2085880b669736c2cf967be981869f7f34de1d05；
- 原 orientation=1、spacing=2、M=112；
- 每个实际 field 的 r、w、原 x/h，以及原 window 中的 mu。

原 w2 记录继续保存在输入账中；不将它替换成 w 的平方。取 r/w 只是选择坐标所需的已保存输入，不以零形状公式替换完整非零 A。四个实际 A 的全部模式间耦合均保留。

## 3. 选定 frame 与每个实际级间接口

对每个偶频率 $m=2,4,\ldots,224$，工作精度中形成

$$
H_i=r_i^4
\begin{pmatrix}
1&0\\
m/\sqrt7&b_i/(\sqrt7\,m)
\end{pmatrix},
\qquad
b_i=\frac{\sqrt{12}\,\mu}{r_i^7w_i}.
$$

每个 H 的有限工作精度系数都保存。R271 对任意可逆的固定 frame 成立，不依赖这些有限数恰等理想无理系数。这里 H 在保存的线性化点冻结，不对随状态变化的 H 求额外导数，也不重新离散连续的 H' 方程。

形状的全224坐标由112个三角二元块组成。完整226扩展是 diag(H,I2)。令

$$
C_i=\operatorname{diag}(H_i,I_2)A_iH_i^{-1},
\quad
\Gamma_{ij}=\operatorname{diag}(H_iH_j^{-1},I_2),
\quad
E=\begin{pmatrix}I_{224}\\0_{2\times224}\end{pmatrix}.
$$

入口 frame 取 field a，engine 出口 frame 取 field d。具体递推是

$$
\begin{aligned}
\eta_a&=\Gamma_{a0}E,
&L_a&=C_a(\eta_a)_{\rm shape},\\
\eta_b&=\Gamma_{b0}E+\tfrac h2\Gamma_{ba}L_a,
&L_b&=C_b(\eta_b)_{\rm shape},\\
\eta_c&=\Gamma_{c0}E+\tfrac h2\Gamma_{cb}L_b,
&L_c&=C_c(\eta_c)_{\rm shape},\\
\eta_d&=\Gamma_{d0}E+h\Gamma_{dc}L_c,
&L_d&=C_d(\eta_d)_{\rm shape},\\
T_{\rm frame}&=\Gamma_{+0}E+
\tfrac h6(\Gamma_{+a}L_a+2\Gamma_{+b}L_b+
2\Gamma_{+c}L_c+\Gamma_{+d}L_d).
\end{aligned}
$$

每个 eta 和 L 都是完整226×224；A 的输入取前224行，准确反映原 mean 积分不反馈。两条 mean tangent 的各级值仍保留。field b、c 的 frame 系数如果实际相同，只有它们之间的 Gamma 取精确单位阵；两个不同的 A 仍分别使用。

源码明确保存全部12个所用 Gamma 接口、四个 C、四个 eta、四个 L，以及恢复前后的完整输出。它没有直接把每个 A 换成 C 后再省去 Gamma。

原坐标恢复次序为

$$
T_{\rm engine}=\operatorname{diag}(H_+^{-1},I_2)T_{\rm frame}H_0,
\qquad
T_{\rm stored}=P T_{\rm engine},
$$

其中 $P=\operatorname{diag}(I_M,\rho^{-1}I_M,I_2)$。原 port 只在最后作用于 Pi 行一次，mean 行不受 port 缩放。恢复右乘 H0 作用全部输出行，包括两条 mean 行。

这只是一个原步，最终已回原 Q/Pi 坐标。它不把 field d 的局部 frame 默认为另一原步的共享节点坐标；未来若直接在 frame 中跨步连接，仍需 R271 的共享节点及接口关系。

## 4. 同精度对照与精度记录

同时计算一个同工作精度的直接 RK4 对照：对固定的四个 A 和原 h，使用完整226×224 E、四次矩阵乘法及普通四级相加，最后同样仅付一次原 Pi port。两套输出都最后转成原坐标 binary64。

这两个 map 只是新的数值数组候选，不能冒作旧41的冻结短 J。后续独立参考将比较固定四 A 的完整有理 map、正确舍入的 binary64 RN 参考、以及两个实际候选的逐项误差。候选入口没有设置误差大小的科学通过阈值。

工作精度使用实际 numpy.longdouble，并记录 numpy_finfo_nmant、significand_bits、itemsize、max_exponent、字节序与 epsilon。Linux x87 常见格式会记录63个 fraction bits、64个 significand bits、80个活跃数值位，虽然 storage 常占16 bytes；不能称为 binary128。

保存 longdouble 时，x87 数值只保留每项前10个活跃小端字节，其余 storage padding 显式写0。这只规范原本不承载数值的填充，不改变数值。每个工作数组 descriptor 都带 encoding 元数据。真正 binary128 或 longdouble alias binary64 则按实际 finfo 单独记录，绝不只凭 numpy 的 f16 名称推断数值格式。

输入和所有候选完整原始字节留在 large-arrays/。工作数组和最终 f64 的不同 dtype 不混读；精确消费者只把最终226×224的 f64 map 当数学比较对象，对其他工作数组保全完整 bytes/SHA。

## 5. 可直接执行的 CLI 与输出合同

~~~sh
python "$C/geometry_20261114_saved_stage_rk_covariance.py" \
  --capture-directory "$FIXED47/native-stage43-local-j-probe" \
  --capture-result-sha256 da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403 \
  --out "$OUT/stage43-r271-candidates"
~~~

输出目录必须全新且独立于原输入目录。读取助手只做原件身份核，不执行原捕获程序。因其 source pin 检查，workflow 的 computations 检出仍须包含原三个 probe 源及冻结9c助手。

result.json 的 schema 为 saved-four-local-A-R271-frequency-balanced-RK4-candidates-v1，保留：

- completed、source_sha256、capture_result_sha256；
- input_binding 文件收据；其中 capture_result 原样沿用冻结助手的 file/bytes/SHA 收据；
- original_h 与 original_port_ratio 原 numberRecord；
- array_manifest 收据。其 JSON 是 object，schema为 saved-four-local-A-R271-working-arrays-v1，arrays为 descriptor list；
- candidate_maps 的两条完整原坐标 f64 map：
  r271-frequency-balanced-longdouble；
  direct-original-coordinates-longdouble。
- 每个 map descriptor 含 name/file/bytes/sha256/dtype/order/shape，最终 map 的 dtype 为 <f8、order C、shape [226,224]；
- full_original_output 别名第一条完整 map；shape_J 与 mean_rows 是其 [224,224] 和 [2,224] 原字节切片；candidate_components 也保存两套各自的切分与 cast 记录；
- 实际工作精度、全部 frame/接口/阶段矩阵、恢复次序及所有完整工作数组收据。

完成只表示两个完整有限候选已形成。native_accepted 与 task_completed 仍为 false。失败时保留已有数组、manifest、具体 phase 和 traceback，不把部分候选当成完成结果。

## 6. 后续用途与限制

[独立完整有理参考](../computations/exact_20261114_saved_stage_full_rational_reference.py) 接实际 result SHA，按上述单向合同读取候选；候选源没有反向依赖该新参考。参考可以复用 actual47 已完成的三个真实输入向量，不必重取43的完整大 artifact，也不重复 native 求值。

无论某候选是否更接近固定四 A 的有限有理参考，这都不直接提供新完整方向或 native 接受。若扩展到更多原步并用于预条件或近似 J，必须有新的矩阵身份、重新求方向，并回原完整非线性 evaluate、原 guards、原 sigma 和原验收。不能以旧方向在新 map 下的作用大小作通过门，也不能把有限数组参考误称为真连续 DF。

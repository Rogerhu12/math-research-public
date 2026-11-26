# 固定深谷度量的完整多轮分离 SOC 接线

**状态：已写完整后继源与运行参数；本后继尚未科学执行。** 这是既有 R683 半空间论证在实际新固定标量模型上的应用，不是新的 MFCQ、几何可行性或收敛定理。全部科学求值仍只在公开仓库 Actions；没有本地科学 fixture。

## 1. 唯一实际父与固定目标

公开 run [45762076394](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394) 的阶段 59–60 已返回实际完整固定深谷方向；逐字参数、源和数值见 [第 6 卷](2026-11-26-public-actions-45762076394-1-part-006.md)。本后继使用：

| 对象 | 实际 SHA-256 |
|---|---|
| 父 `deep-fixed-scalar-amplitude-first/final.npz` | `b788c32879aa5ff5ff3d5f2ed81b92205b54fc0da61a1a2b84ace8345a3f22eb` |
| 父完整 report | `eddd8331a5164ff99443a3044e736497a9dae447e9514ad8f9c2f26f12e2e9a8` |
| 固定准确 scalar profile | `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d` |
| 当前 observation carrier | `bdd9eb854432680009e2f1b4b6a03983d6ef01df46f93ff7a128d74a8af4124c` |
| 当前 symbolic nodes | `4786632e4269d484811c27a6fa05374387b18bb190d831d6957e64392f4bd535` |

原完整 driver 为 `d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95`。它对同一提前固定的 $g_n=ds^2+a_{\rm new}(s)^2d\theta^2$ 运行两次 64 预算方向，每次真实接受原半步，$\mu=0.01$；最大相对 Gram 从 $0.016536480593973855$ 降到 $0.01426432970666691$，Phi 从 $0.0008446466076168624$ 降到 $0.00032735551888962906$。最终有限曲率必要乘积 $0.9919954367406946$，幅度最大 $g=-0.04784623969218671$，全已知曲率/半径地址数为 2737/2731。两个内 QP 均未驻点。

后继从这个实际最终场继续；不从 moving-mean 分支迁入新的场、目标、Gram 或几何结论。全部原 metric mean/cross 行和自由 core/q/H 仍在，profile 不随当前场重新拟合。

## 2. 物理代码身份必须分别绑定

新 helper 并非修改旧 R671 guard 后冒称旧模型。它独立绑定真实组合：

| 责任 | 实际代码 |
|---|---|
| 新 context 的 `definition` 与 `geometry.fields_block` wrapper | `deep_valley_reference_factory.py`，`4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1` |
| 解析固定标量 `DeepValleyTail` | `deep_valley_tail_input.py`，`e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2` |
| `point.fields_at` 与基础完整 six-jet/J 代码 | `exact_reference_tail_lift.py`，`2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216` |
| 完整点 cotangent 模块本体 | 原 `fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad` |

4ae 的 `fields_block_observed` 是真实新 wrapper；其 code file 不是基础 2e。4ae 的 `point_adapter` 则调用基础实现，所以返回的 `fields_at` code file 确为 2e。二者在代码里分开核。模型定义必须与当前 context 全体相等，固定 profile 定义与 identity 重新一致，$\lambda=1$、`fixed_new_scalar_metric=true`、`target_is_a_moving_angular_mean=false`；当前 carrier 和 $M$ 也同一。

基础 six-jet 公式读取这个新 context 的 $h,f,k$，不读取旧 target。幅度 helper 的帽半径由同一 `problem.R` 绑定；新固定 $R$ 不作为变量，帽行仍只对自由 $H$ 求导。正负见证 $p$ 的全部自由 core 导数、曲率乘积的完整原坐标拉回都保持。既有 typed 不等式只依赖当前物理 jets 和固定预算，所以其链式求导在这个明确新 context 下仍适用；这不允许继承旧场的曲率/幅度证书。

## 3. 同一父点的有限修正与完整真实接受

[固定原父多轮分离应用](2026-11-26-fixed-parent-multiround-separated-SOC-application.md) 中的同父 $x$、原 QP $d$、有限行追加及原半空间投影逻辑逐项保持。每一轮从上一个**完整真实拒绝**中取新地点/搭档，在原父求完整行；所有已有行保留，原 $d$ 不变，全部 $r_i(d)$ 仍在原 full-trial 上重读。

具体仍解

$$
\min_e\frac12\lVert e\rVert^2,
\qquad Ce\leq\min\{b-Cd,-r(d)-\xi\},
\quad\xi=\tau\lVert d\rVert^3+\theta\max_i(r_i(d))_+,
$$

首批 $\tau=0,\theta=1/8$。所有旧线性不等式由直接 $C(d+e)$ 复读承担；实际 typed 非线性行另读。新增行若使原父 $b_i<0$，该修正分支诚实停止并要求 restoration 或另一合格父，不假定零步可行。无新行时也不重复不变的修正。

本版完整 body 从 d3c3 原源构造。真实 trial 直接调用 `problem.residual(point)`，不调用 moving-mean `_state`。每个修正独立计算同一固定目标的 $Az$ 与自己的模型收益，再读真 Phi、正密度/度量域、全网格+全永久地点曲率/幅度。只有全过才接受；原门槛及 $D_{\rm marked}=4.2,L=0.9,H_{\min}=1.01$ 不变。任何拒绝的新极值照样进入永久位置集合，原 ray 仍从原父的半步继续。

当前 fixed-scalar coarse 模块 `dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395` 与 R685 v5 全部保留。全 direct $J,J^*$、原 QP、H² 母范数、$\mu$ 单位、原正观测权和 fixed $a_{\rm new}$ 进入粗 Gram 的方式不改。新 reader 读取真实 `scalar_coarse_preconditioner/current_fixed_scalar_coarse_Gram`，不会将它们伪装成 R688 mean 字段。

每个原方向最多 8 轮，只分配一份追加容量 mmap。第一次完整复制旧行，之后仅写新增行，unused capacity 不进入投影。逐轮仍重建原投影 Gram，成本和实际调用逐项记录；不声称减少了科学调用或达到了更快收敛。下一原方向重新建立自己的真实父与 $d$，各方向内部的同父约束分别成立。

## 4. 完整源及实际运行入口

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `complete_deep_amplitude_rows_separation_soc.py` | 42740 | `f24765215124ce2615edd70fe15c9560000281938b254171a32dceb398e0e8ce` |
| `derive_deep_amplitude_separation_soc.py` | 32902 | `d80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec` |
| `fullclosed_deep_amplitude_separation_soc.py` | 90181 | `329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90` |
| `launch_deep_amplitude_separation_soc.py` | 25289 | `ca4048343c7ddccfd1662e7c3099d699a4715fe5c101c9cde3be024d0a76c7cc` |
| `read_deep_amplitude_separation_soc_report.py` | 27733 | `eb0c1f2e36d4fad37bc712bb72e26b7ca91ca6f1c7a10e9b648903df3d6b428d` |

新 deriver 逐字重建整个 d3c3 衍生 body；完整 report 的 schema、实际 body、runtime roles、固定 target 全程身份分别绑定。launcher 接受已刊 d3c3 父或自身完整已绑定的新 SOC 父，绝不重写原 `declared_derivation` 或 canonical model。父历史提取仍读完整当前 report 的所有 trial/working/final 地址，加入当前 carrier 的旧清单，并用原 exact location union 解析 grid 地址。

首批请求文件为 `computations/resume-20261126-deep-amplitude-fixed-parent-separated-SOC-first-steps.json`。它直接使用上述 b788，**2 个方向，每个原 QP 最大 256 次推进，每个方向最大 8 轮 SOC**；两个预算都可显式配置。$p=4,\epsilon=0.001,\mathrm{scale}=0.05$、centered Phi、$\eta$ 节点 885、完整 carrier/nodes/scalar 保持，`--damping-from-parent` 读真实父末 $\mu$。`target=1e-9` 沿用这个固定目标的明确数值阈值，不把它改称 README 的原求解容差。

新输出目录 `deep-fixed-scalar-amplitude-separated-SOC-first`，随后只运行新纯标量归因。归因给出原/修正每个 trial 的真失败类别和缺读、各轮固定原始 $d$/父身份、真实 K/D/product 与完整地点对象、真 Phi 收益、同一步 $q_0/q_z$、幅度值、预条件成本及 cache 容量/使用/磁盘字节。root 依实际返回继续几何和同 g 精化，不预设修正一定成功。

本地仅执行 stdlib 源构造、AST/compile、完整 body 字节重建与 argv 结构检查；几何代理静态核了新 factory/base/scalar 身份和直接残差接线。没有科学运行、没有新 fixture。有限接受也不支付全曲面相对误差 $10^{-6}$、同 g 加密下降、全部 $t$ 的嵌入/reach 或最终完成标准。

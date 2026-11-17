# 负曲率 hold 的完整共同二jet场及固定弧长规范化

**完整开前缀的数值证据。** 保留真实d644父的498个原quintic胞元，把已完成6529局部IVP的1600个胞元接上；仅用R637在局部首32胞作明确二jet桥，不重跑IVP，不解新BVP。随后整场采用同一个固定构造角网格N=4096的弧长规范化。全部2098胞、audit8192、每胞4个径向细分，共68,755,456个点的实际相对Gram算子范数最大 **1.18065979401e−7**，主曲率最大 **6.30193652889**。

这里的场只到s=1.02，未闭合。全径向极值仍为采样；全径向q_N严格正性、reach、全t路径及同g精确解收敛未由本项支付。

## 实际拼接及固定定义

正确标量是上一条的HoldProfile：κ在.002内降至−2.5、保持.02、再在.02内升至+1.5，后续正平台及末ramp按同一标量定义。本项只读该g已保存到1.02的场，不能使用旧inward或pulse标量替换。

左侧所有二阶jet由原M112/N2048算子、原Profile及保存的一阶jet作JVP后再补零到M320；没有以高模重算值替代。局部原数据的旧切口jet与重新读取的原左值逐项相等。令δv、δa为局部首导数及二阶导数减去旧值，w=s_32−s_0=.0004999999999988347。局部桥为

\[
F_b=F_{loc}-wP_1(u)\delta v-w^2P_2(u)\delta a,
\quad P_1=u-6u^3+8u^4-3u^5,\quad
P_2=\tfrac12u^2-\tfrac32u^3+\tfrac32u^4-\tfrac12u^5.
\]

δv、δa的系数最大值分别1.78815471516e−5、.00313571729047。首端0/1/2jet明确绑定原左值，桥末从节点32开始的所有原0/1/2jet逐项不变；两侧实际切口差[0,0,0]。共同数据定义每胞唯一quintic，故基场接缝C²。完整径向范围[0,1.02]，原cut=.995，桥末=.9954999999999988。

复用已冻结弧长引擎31782的数学定义：q_N是固定4096点对|F_φ|的真实三角插值，b=mean(q_N)、λ=a/b、c=(0,0,z_mean)，以∫_0^ψq_N=b∫_0^φρ定义ψ，取F_new=c+λ(F(s,ψ)−c)。候选的目标仍为原固定g=ds²+a²ρ²dφ²；实际角向误差|F_φ|²/q_N²−1保留，没有强置零。若q_N全域正，该有限角/共同quintic定义给C²坐标及曲面。更密audit网格只读同一个q_N，不更换构造。

## 实际整场读数

|量|读数|
|---|---:|
|新实际相对Gram最大值|1.1806597940111045e−7|
|最大值位置|s=.99500390625，旧角.7217379607001941，桥首胞u=.25|
|该处rr、角、mixed误差|1.11045187712e−7，1.11e−15，−2.87909124409e−8|
|原共同quintic同样本Gram|7.086651038443896e−7|
|新实际主曲率最大值|6.301936528886818|
|曲率峰位置|旧前缀s=.969625，旧角1.7755827619776297|
|实际角Gram余项最大值|4.951594689828198e−14|
|q_N样本最小值|.16601843096428714|
|各采样s上全角Lipschitz下界|.15909568175876831|
|核心0/1/2jet变化|3.14e−16，0，2.54e−16|

λ−1最大2.29283259046e−12，按旧角匹配的像点距离最大3.31143242861e−12；这是对应像点/候选Hausdorff匹配的数值，**不是同一材料点的位移**。新段未超过旧前缀的曲率峰。耗时127.58秒，未运行新的ODE求解。

## 复现与身份

S为本题scripts目录，所有输入/输出raw留scratch：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_c2_arclength_readout.py" --parent parallel-continue0995-m112.json.gz --local parallel-negative-hold-ivp.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --arclength-source "$S/parallel_20261117_pulse_arclength_readout.py" --corrected parallel-negative-hold-c2-w32.json.gz --assembled parallel-negative-hold-complete-base.json.gz --out parallel-negative-hold-complete-arclength-c4096-a8192.json --join-index 32 --construction-angles 4096 --angles 8192 --radial-subdivisions 4
```

SHA256：

- 原父：`d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`。
- 原局部IVP：`6529073f7ad1c5f041e5f7be921a2dab6f509768622153a770556d0460a5a6be`。
- 本桥接/完整读出源：`5f0390f929cf068c3648dc16b101df5382334c279f72376b1df8b61dcb431d13`。
- 冻结弧长引擎：`31782ba06d5414a7851284ce330a89d208b8d56c4f1d99421a804e2a78271266`。
- 正确HoldProfile源：`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
- 修正局部raw：`967d4f173c04f581366183465a34090b16fdd732ae5a3f1a3a3db8b49c5abc50`。
- 完整共同quintic raw：`aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15`。
- 实际report：`9060636046e7487156928bbb4b19cf1ae962d9d1207b2b22258051daa3bfe0ca`。

源强核原Frenet/Profile、标量源和弧长引擎SHA及两端实际jet；report区分原IVP、修正局部和完整基场身份，并明确`bvp_accepted=false`、`ivp_rerun=false`、`new_BVP_solved=false`。

后续[R638§6](../results/R638-global-positive-arclength-coordinates-for-two-prefixes.md)已严格结清本候选全域q_N/rho正性，原采样Gram/曲率/未闭合边界保持。

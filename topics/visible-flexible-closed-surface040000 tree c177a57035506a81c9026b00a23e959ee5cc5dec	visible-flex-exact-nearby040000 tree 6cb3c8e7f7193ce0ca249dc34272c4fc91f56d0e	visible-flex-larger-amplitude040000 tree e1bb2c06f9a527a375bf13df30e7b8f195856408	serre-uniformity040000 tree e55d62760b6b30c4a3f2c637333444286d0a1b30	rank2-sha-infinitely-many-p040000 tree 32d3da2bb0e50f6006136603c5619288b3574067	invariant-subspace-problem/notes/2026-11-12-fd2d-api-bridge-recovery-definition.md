# 执行器不可用后的 25%/75% 初猜恢复入口

## 范围和真实状态

此文件及三个 API 恢复源码是在 cloud executor unavailable 后从完整会话记录重建的文本。
创建 Git blob 不等于重新执行了数值计算。旧未推数值实体当前不可见，不冒称仍在本地或已恢复。
新的 CI/CLI 必须实际执行下面命令，产生另名 report、实体、manifest；不得沿用旧 exit 或旧 SHA 作为新结果。

父代理统一提交、更新 main 和执行；本子任务只创建 UTF-8、单件小于 100 KB 的 blob，
没有改 refs、索引或 workflow，也没有在 API 使用令牌。

## 已有准确输入

仓库 c57249ac7dbda27de4bb178052cf78f81d641643 及其后 main 已保存：

- notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json；
  SHA256 a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147。
- notes/2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz；
  SHA256 db7614138c5f55b77e23f04849af02c75db36a277064b64f684a8da574c68c51。
- 已闭 reader、positive_clock、balanced 中央 provider、R132 正 Bernstein 尾 provider。
  恢复脚本在实际运行时绑定每个源的 SHA256，两个主要输入 SHA 必须完全匹配。

通过 connector 读取的 main raw 源 Git blob 为
85f1ae7b93dc1313cbc46ebd01ad2d6e810fb08e。恢复 snapshot 保持所有有限方程和 lifting，
仅补上本会话已用的准确端点投影方法及显式端点诊断。
新 snapshot 是新文本身份；不冒称与旧不可见 snapshot 的文件 SHA 一致。

## 运行

在 topics/visible-flexible-closed-surface 工作目录，需 Python、NumPy、SciPy：

~~~sh
python -u scripts/fd2d-flat-prefix-bridge-api-recovery.py \
  --stem notes/2026-11-12-fd2d-api-bridge-recovery-01
~~~

所需三个新源码：

- scripts/fd2d_gc_raw_bridge_api_snapshot_01.py
- scripts/fd2d_flat_gc_codazzi_api_projector.py
- scripts/fd2d-flat-prefix-bridge-api-recovery.py

无需重跑旧 IVP，无需重跑 24+42 组参数 screen，更不另做非线性 BVP。
默认直接重做此前最有用的明确 bridge，然后做一次线性 Codazzi 最近方向。
输出：

- notes/2026-11-12-fd2d-api-bridge-recovery-01-amount025.npz
- notes/2026-11-12-fd2d-api-bridge-recovery-01-amount075.npz
- 同 stem 的 report.json 和 manifest.json

单件大于 1 MB 自动追加 .gz；大于等于 5 MB 明确报错。K7 的旧对应实体约 429 KB，
但新大小和 SHA 必须从实际 report 获取。已有 report 不覆盖，重跑须另 stem。

## 物理与有限表示

固定 T=.02，准确 balanced 中央系数全零，A=1.405、B=.495、gap=.91。
八个真实 Bernstein 尾控制全 1，切口 .8、固定 flat collar .34、cuff .32。
positive_clock 在此参考 T 上 x=s；角坐标是 root 的固定混合图
u=ξ+(1−β(x))(U_seed(ξ)−ξ)，混合区间 [.58,1.263603200988874]。
K7 有 n/l 频率 0,2,...,14、m 频率 2,...,14；113 径向节点、128 角格；
校正 113×23，参数16，总向量2615。

字段次序始终 n,m,l。准确中央和整圈真实尾 lifting 保留，
所有首末节点校正为零，cut 均值和高模不被省掉。
目标 gap 行按 .91 计算；若主求解目标是 .9，加载后重新计算完整 F，
该行成为 (.91−.9)/.9=1/90，其他有限方程和物理对象不变。

## Bridge 准确定义

保留实际前段到 s0=.5。令

\[
n_r(s)=\sqrt{(1-a_s)(1+a_s)}/a,\quad
g_0(u)=\log(n(s_0,u)/n_r(s_0)),\quad q_0(u)=m(s_0,u)/n_r(s_0).
\]

到 s=.9 以 S5(t)=10t³−15t⁴+6t⁵ 消除各向异性。
准确尾项从 .95 开始以同一 quintic 权加入，在当前 a(s) 处取
nT=κ(a(s)sin u)cos²u、mT=−κ(a(s)sin u)sin u cos u。内部取

\[
n=n_r\exp((1-S_5)g_0)+w n_T,\quad
m=n_r(1-S_5)q_0+w m_T,\quad l=(K+m^2)/n.
\]

cut 直接采用准确尾的完整三场，不在零 n 弧上除法。
从准确 lifting 中减去上述试场后，投影差的有限 Fourier 系数，
再准确重设首末校正为零。该后段只是初猜，不覆盖原实际 IVP 的身份。

命令行也提供 --handoff、--relaxation-end、--tail-start、
--derivative-carry 0 或 1，可重做此前 screen 中的明确单点。
carry=1 加 L(t−6t³+8t⁴−3t⁵) 乘真实起点的 log 比例/归一 m 一导。
默认 carry=0 正是此前选中的最低残差 bridge。

## 线性 Codazzi 最近方向

固定所有参数、首末校正，只改内部有限状态。
记线性残差 rC+Cδy；W 是正径向积分权、Fourier 常数模 √2 权、
以及 l 分量 .5 权。行平衡 R 仅改善 normal equation 的条件。
令 A=RCW⁻¹，方向

\[
\delta y=W^{-1}A^T(AA^T)^{-1}(-Rr_C).
\]

使用 sparse LU，再作两次同一线性方程舍入修正。
不迭代 Gauss、不改变 T/中央/尾，不另起非线性 BVP。
输出 bridge+.25δy 和 bridge+.75δy，并各自重算完整 F、全角 Gauss 和形式曲率。

数组含 x、corrections、parameters、vector、fields_n_m_l、material_u、
physical_s、candidate/trajectory SHA、modes、blend、profile_kind、tail_kind、
base_kind、amount、initializer_only=true。
更换径向网格只可作为新的初始化插值，不能沿用原 finite residual。

## 旧观察值，仅作历史对照

下面结果均是执行器不可用前真 exit 0 时观察到的值。
它们不是本次重建源的实际输出，也不声称旧二进制现在可见。

| 过程 | session / launch / completion | 真退出 | 历史范围 |
|---|---|---:|---|
| 最后有效前段后 24 组短衰减 | 83898 / 0cc875 / 1ecd6e | 0 | 17.4212925 s；保真前段到 .809，快速抹平会使 Codazzi 很大 |
| 前移 handoff 的 42 组 screen | 58142 / 09595c / af6827 | 0 | 70.5563862 s；选 .5→.9/.95 |
| 固定参数线性方向/有限步长 | 21581 / a8f4f7 / 8aa8ce | 0 | 4.75205994 s；下表 |
| 原 R134 正 n 修复交替 4×12 | 37949 / 0a84be / 81b6c8 | 0 | 35.5606983 s；无总体改良 |
| 全本征分支谱最近修复小核 | 15710 / 2da05e / e7edcd | 0 | 1.68365335 s；下节 |
| 谱最近修复交替 8 轮 | 92360 / 1099cd / 00bdee | 0 | 13.3490391 s；无总体改良 |

旧默认 bridge：raw最大残差12.253062797987699、全Gauss1.9090501731015719、
形式曲率7.277106244210154。

| 旧方向步长 | raw最大残差 | 全角Gauss | 形式曲率 | 最小n |
|---|---:|---:|---:|---:|
| .25 | 9.189797098490777 | 2.3382541228866325 | 7.001638467996436 | 0 |
| .75 | 3.0632656994969247 | 6.869729892456082 | 7.123311908510938 | −.049907557741054334 |

准确中央未改变；75% 内部少量负 n 由原生三场如实表达。
全 Gauss 仍很大，所以这些只是初猜，不能写成强核或连续后验通过。

原 R134 positive-n repair 交替没有优于75%初猜。
谱最近 repair 首轮 exact Codazzi 后 raw 降到2.9829530521408283，
但全Gauss10.122350428154503、形式曲率7.164481954328895；
第8轮恶化到 raw4.0619929122597345、Gauss14.577096646159864、曲率8.444344765570555。
不建议把这些负结果当新主初猜；没有必要重复全旧试算来给主线增加门槛。

## 谱最近修复的独立数学说明

对 S=Q diag(b,a)Qᵀ，a≥b，取同一主方向、
T=Q diag(y,x)Qᵀ。二维旋转直接给出：
固定 x≥y 时，Frobenius 距离以同向排列最小。
故准确最近 Gauss/cap 矩阵化为最小化
(x−a)²+(y−b)²，xy=K、|x|,|y|≤C、x≥y。

K>0 的两个闭分支为
x∈[√K,C] 或 x∈[−√K,−K/C]，y=K/x；
K<0 只有 x∈[|K|/C,C]、y=K/x。
每个分支的内部驻点满足

\[
x^4-a x^3+bKx-K^2=0.
\]

比较全部实驻点及端点即可。
K=0 比较 y=0、x=clip(a,0,C) 与 x=0、y=clip(b,−C,0)，含零矩阵。
无需固定 m，也不强制 n>0；边界 mask 原样保留。

旧有限小核：262个随机/角点，旋转协变误差1.42e−14；
与密集一维能量格相比最坏超差8.53e−14。
旧真实75%格上点态改变量平方和由原positive helper的20936.1085降到2012.21465。
但有限角投影后虽 Gauss1.849647、曲率7.044822，径向 Codazzi 约141.222，
所以点态距离更近本身不保证更好的全初猜。

## 尚未观察到的新 Frobenius 一致交替

最后拟建的 common-Frobenius projector 将 n/l 权设1、m权√2；
它与谱点态最近函数使用同一矩阵 L² 距离。
若 A 是准确lifting+有限角 affine空间、C是固定参数Codazzi affine子空间，
则 C⊂A，正交投影满足 PC PA=PC。
因此在有限节点 Hilbert空间内可形成真正同距离两集合交替；
进入C后到Gauss/cap集合的距离应不增，但不证明交集非空或 raw最大残差下降。

这项新入口的工具 cell g2:371 在 unavailable 期间一直没有返回，
没有获得进程session或执行退出；随后仅主动终止工具 cell。
不能把工具终止冒作某数值进程已启动或退出，也没有新数值结论。
若未来实际做此对照，必须另名、另报真实执行和距离。

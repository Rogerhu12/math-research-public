# 恢复源码的公开开发检查审计（2026-11-14）

## 结论与范围

公开 Actions [43625250205](https://github.com/Rogerhu12/math-research-public/actions/runs/43625250205) 的 recovery_development lane 已完整成功。它执行有界入口高度接口的人工测试、一维高度提案 helper 的人工测试及自由双线性 Gamma 准确代数证书。没有运行真实候选几何、profile 积分、优化或参数步，不能把本轮 passed 解释为课题达标。

执行源、发布器实际 pull 前后、readmes_read_commit 均为 12137a0394cac7a3036f49519108636b3b6209f0。回执报告两个 README 差异为空。本审计只通过连接器读取公开证据，不将 API 读取冒充 git pull。

## 1. 四份输出及来源绑定

原始目录：[actions-43625250205-1-recovery_development](actions-43625250205-1-recovery_development/)。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| bounded-entry-height-development-check.json | 3773 | 93534ae58b875d4006558fc6059ae16db904e19e826ed0671f5268cd292dacd7 |
| development-source-binding.json | 625 | 5dd58e621d0b4c33da5cdf8526e49bd02350d6254b1e32b8d66872fb5c6a3321 |
| height-feasible-initializer-development-check.json | 630 | 4c243a586729423459c1501a0fc43b692bdd94825b40013acf47054a9a45c4ee |
| pure-bridge-Gamma-exact.json | 1049 | 55047e291da21e413e41e406fff14c55b17a3ac0315d2d859a481a81703521d5 |

四份完整文本的重算 SHA、字节均与回执的 raw/storage 两项相符。回执为 21158 字节，SHA 为 7cf430199f74f6ba3c893c383a8f7dcc521abf132bc4da32f871b439e5bac4c8。

回执有 99 个来源。相对于[已核入口源](frame-entry-paired-repair-actual-audit-20261114.md) ac8ca0437b9617b63522eef5267d1b060144865c，逐路径 Git blob 比较证明 88 个脚本不变；新增五个脚本、修改发布器。五个新增脚本、发布器、workflow、request 均从本次准确提交重取字节并核 SHA；两 README 和原 seed JSON 也再次核验。完整 23 个有界高度运行依赖 SHA 与回执一致。整仓库 compare API 的 300 项截断列表不用于推断其余路径不变。

source-binding 文件强制的三份执行源全部准确相符：

- frame_entry_bounded_height.py：16235 字节，deac1dbb3410fc426bd1cbb84c126062a5ff61e2aa19c6fcdf1bbd9d0727b612。
- frame_height_feasible_initializer.py：15379 字节，fa379eb61996dfd0646e8ce99f5de88f51c105f13d1e5bea8cba0906525ed6a2。
- literature_pure_bridge_gamma_certificate.mjs：4889 字节，7711149edb4ccbd11ec5dd8acad03b81fb56de1c9b48480406a57e4402f8178c。

这些 blob 与环境失联后保全并审核的准确字节相同。有界高度脚本此前的本地人工检查中断，没有被追记为成功；本轮才提供其真实完整执行证据。另外两份新来源 h-bridge helper 与 N-polynomial engine 只是列入来源映射，本轮没有运行它们的真实研究目标。

## 2. 有界高度接口

人工完整位置二 jet Jacobian 相对误差最大 $1.03051\times10^{-8}$；direct metric/shape Jacobian 误差 $5.63456\times10^{-9}$。完整冻结 $a'''$ 与差分比较为 $1.54400\times10^{-10}$；固定高度参考的 $b_{0,s}$、$b_{0,ss}$ 比较分别为 $1.68062\times10^{-10}$、$1.60294\times10^{-9}$。

人工样本固定参考速度的绝对最大值为 1；准确 $-\sin\beta/\sqrt{1+v^2}$ 定义也直接给出 $|b_0|\le1$。这只限制固定参考项，不能自动限制加上当前自由高度系数后的总 $b$。

同一 $T$ 场与旧多项式入口逐项差为零，入口外局部位置 jet 差约 $2.04\times10^{-15}$，稀疏/密查询的全二 jet 差为零；完整冻结度量与同态评价精化身份均通过。新高度模型被明确标为不同物理场。固定参考的 $b_7$ 不会锁死从七阶开始的自由高度贡献，报告保留了这一范围。

## 3. 一维高度 helper 与 Gamma 证书

高度 helper 的人工 quartic 与直接数组 cost 最大差为 $2.710505431213761\times10^{-20}$，选中人工内部解 $\Delta=0.8$。正反 side、负斜率约束、不可行帽高、固定水平球失败分支、输入数组不变和完整成功/失败 JSON 往返均通过。它没有读取实际几何，没有应用实际系数步；其完整源码 SHA 与保全前最后版本相同，最大误差和人工解也与当时开发记录相同。

Gamma 证书采用 BigInt 准确分数及自由对称双线性算子；不假设算子结合律或交换律。十个差的单项式数全部为零，包含 $\Gamma=3DP_3$、$\Gamma$ 对 $A$ 变号为偶、$\Gamma_A(A)=0$、任意入历史的最高阶逆流及内部桥的 $P_2=\Gamma$。去掉本次 Node wrapper 添加的 source SHA 后，报告与此前独立执行的同一代数 core 结果完全相同。公开 Actions 也实际执行了此前尚未运行的 Node 文件写出/source-hash 外层。

这些是源码可执行性与准确代数恒等式的证据。下一真实短入口/有界高度初态、完整第四阶周期或全曲面标准均需另有实际结果。

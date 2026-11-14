# 纯 bulk 完整函数编译：开发通过与首次实算

状态：开发接口已通过；研究整函数关系尚未得出。

公开 Actions [43627888220](https://github.com/Rogerhu12/math-research-public/actions/runs/43627888220)，源 `fdb11652a1e255ac2cd8dd8d9bb847371ccde78d`，成功运行独立 Node formal-jet 证书与 Python 小代数。Node 的三项多项式差全部准确零；Python 的有符号右原函数、分部积分、shuffle、真实八矩交换子、常正算子及独立 $\tau_0$ 响应八项全 true。这里没有评价真实 profile、曲面、几何积分，也没有编译完整研究目标。

原始输出位于 `notes/actions-43627888220-1-p1_bulk_development/`：`tau0-independent-exact-check.json`、`p1-bulk-exact-toy.json` 和 `p1-bulk-source-binding.json`。producer SHA256 `f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70`；R56 依赖 Git blob `01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74`。

据此启动唯一 `p1_bulk_exact`，实际研究符号编译仍只在本公开仓库 Actions。比较完整 reciprocal pure drift 与28个真实第三控制响应，保留全部 history 的物理微分后才置 history 值零。只使用共同右 collar 合法的恒等变换；若找到准确系数关系，从原始未正规化目标和列重新验证。未找到关系只说明此不完备正规化流程未产生证书，不证明函数不在真实跨度中。

预算为240秒、500000系数节点、60000 profile atoms、80000 terms、250000 IBP calls、软RSS 2048MiB、消元有理数8192bits。资源退出保存阶段和原因，不能记为数学阴性。纯bulk检查不包含真实不同scalar桥的基准第三项，亦未支付其它相位、$P_0$、全部 ruling、有限等距族或本题几何比例。

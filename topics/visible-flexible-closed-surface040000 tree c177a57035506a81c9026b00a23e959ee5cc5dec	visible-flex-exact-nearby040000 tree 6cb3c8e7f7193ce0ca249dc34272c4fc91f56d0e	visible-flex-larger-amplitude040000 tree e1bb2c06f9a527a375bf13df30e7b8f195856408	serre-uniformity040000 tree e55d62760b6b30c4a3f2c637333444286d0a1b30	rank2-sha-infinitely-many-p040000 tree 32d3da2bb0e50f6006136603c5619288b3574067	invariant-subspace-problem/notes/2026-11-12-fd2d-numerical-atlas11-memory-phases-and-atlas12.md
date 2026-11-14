# atlas11真实分阶段记录与atlas12同式内存释放

atlas11（29402/15dc0f）真exit137，唯一child−9/41.417529646秒，0接受。
raw_node_start当前RSS197948KiB，raw_node_done当前290124/峰306180KiB；
没有endpoint_cell_done。实际RLIMIT CPU/AS/RSS均unlimited，最后host available约1.28GB；
这些不足以认定信号原因，原warm仍是唯一可用完整态。

准确代码消费关系给一个可实施改进：raw节点求值返回的全域lifting value/x/xi/
tail/profile参数包，在其Jac完成后不再被后续node Gauss、curvature或diagnostic消费。
先立即释放它；再构造curvature和high Gauss两Jac，释放仅这两者消费的fields_parameters，
随后组装独立8cell endpoint块。各函数输入、参数、算术和最终残差/Jac行顺序全部不变。
新v3源码另名；没有改旧v2或实际atlas定义。atlas12从同warm开始自然短批，不重转初值。
若再未知退出仍记录真实阶段，不以资源假设替代实际求解或数学结论。

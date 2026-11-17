# 材料角回拉的设计初值

既有q040、q045接受态在相同材料角下重建完整扰动，再投影到新角图；可选两个接受态的归一扰动secant。高模/完整reference lift都参与，原lift的周期三次样条只用于初值，不是接受解的定义。solver仍调用原精确core/reference及其全部导数。先把旧物理节点反解到共同子午坐标，再在新物理profile映射；保留已有节点并加物理/角图分段点。

单态预测δ按q²尺度，高支持系数按各harmonic的起始幂次；双态预测δ在q²上secant，其余归一物理扰动和支持矩在q上secant。这些都只是可修改初猜，不是分支存在结论。最后补齐当前core入口条件。正性、root、Jacobian、残差/接受门均没有变。

相同q=.045/M16/λ0恒等对照：新增分段点后1220点，材料角反解残差8.882e−16；与原保存场最大系数差1.674e−12，BC仍1.915e−11。只作初值核验，没有再次重解这个已接受态。

恢复依赖相邻 `complement_prefix_batch1/prepare_runtime.py` 和 `complement_q045/`，将本包两个py放入其scratch runtime。`identity_check.json` 保存实际命令、运行时source与接受态输入hash。当前新q05计算另行记终态，不能由此恒等核验推成功。所有checkpoint只在scratch再生。

# 独立公开 Actions：完整非线性构造的必要输入与持续执行

2026-11-26，Astra-larger-e4e2a2bf-20261126。第一run45762076394继续实际8a05同g求解及真实Haar目标；这里独立启动第二公开job，给完整SO3/单位meridian的新表示提供真实父输入和后续执行时间。job时钟不是课题停止理由，任一job退出也不是完成声明。

## 1. 完整执行身份与独立记录

新workflow为 `.github/workflows/visible-larger-so3-20261126.yml`，只由本题request02变化或手动dispatch触发，独立concurrency group，不取消第一job。Python3.12.14/NumPy2.3.5/SciPy1.17.0/单BLAS保持；新表示使用CPU torch2.5.1/float64。安装命令按[PyTorch官方历史版本页的2.5.1 CPU项](https://pytorch.org/get-started/previous-versions/)确定，实际安装build由job记录，不预填已成功。

完整controller `scripts/resume_20261126/public_actions_controller_parallel02.py` 为17261 B / `57493c11c761601cf1e3e31de19565f7686b8540331ed948ffb8cf37cc995adf`。源自完整原a9f694controller，仅将HANDOFF写入改为独立有界slot；main、科学recipe/启动/自然返回、Git凭据排除、规则pull核查、全分卷render、sync均逐AST相同。NFF仍立即pull --rebase再推，不强推；重新记录本slot读过的commit。原第一controller截取其旧current段时保留位于之前的新slot，两job各自runid索引与分卷不互相覆盖。根代理继续负责人工读规矩与普通提交。

完整request为 `computations/resume-20261126-actions-request-02.json`，独立队列为 `computations/resume-20261126-followups-02.json`。实际source commit/runid/每步SHA由真实运行回填。raw场、完整报告、角矩及工作数组只留各自runner，不使用artifact/Release/cache传递raw；不能根据上一run SHA假装取回数据。

## 2. 只再生新方向所必需的父链

首先保完整rebuild_a04_chain到continue的必要输入链。其后复制旧真实步骤的科学argv、父/输出路径和返回后明确cache清理，只执行这些依赖：

1. 完整永久位置manifest紧凑化。
2. 真实R671 full-phi initial与v3父续接。
3. 完整physical-mean p4父及face-PCG父。
4. 该父自身连续first，作为原幅度预算输入。
5. 原v1失败的prepare与完整v2求解。v1在任何方向前因记录构造错误失败，其已发现位置是v2和deep preparation显式输入，所以这里只再生这个位置来源，不重做或重新宣告失败结论。
6. 完整deep固定profile prepare及d3两条64方向，给新SO3入口一个真实完整父。

原已登记的纯诊断、SOC旁枝、7ebb/Haar与旧证书没有全部重跑。本次输入再生不重复申领旧结论。即使相同算法浮点输出与旧b788不同，也必须记录实际新report/bundle/carrier/nodes/scalar身份；新方向只读新文件，旧几何和误差数值不继承。准确profile定义仍由完整源绑定，工作盒的有限成本与请求精度单独记录。

## 3. 新表示的边界与接续

新候选采用单位切向场旋转、自由core/H和显式C²闭合lift；lift后真实Fs/E并非自动保持单位，完整Gram/J/J*必须包含它。当前只有完整来源与实现正在审查，不能把此编排文件当作新候选/新方向已运行。完整新科学源码和参数刊出后，直接追加到第二queue，不等用户确认。

新的坐标/正H²-type母范数会明确自己的身份，原q坐标范数不会被冒称不变；角向/径向变量和几何位置均须完整保留。所有连续范围、嵌入/reach、整面1e−6、同g实际加密至容差仍按README支付。第二job只准备执行场所，不是阶段收尾。

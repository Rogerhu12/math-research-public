# R144 新前向均值目标：实际6791格前缀与未完成原因

2026-11-26，visible-exact-astra-198c63d-20261126。

公开运行 [45770488571/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45770488571)，job139741670303。运行真实恢复全部5份原数据并核11个当前输入；Python/Arb源码在科学前通过AST。只有这一个新的前向目标被调用，没有重跑旧Gamma、旧mean Green、旧响应或原target生成器。

## 保存下来的实际范围

- 原目标：raw ac1、原nu0、整个原参数区间，固定u和j=v/m，腰Y(0)=1。
- 完成闭格数：6791/7721；保存右端为 $5731986528263291/4503599627370496$。
- scientific：4806B，SHA256 478a807d1caf93fd441949eca6565c1188b34ab44ba007c37b2221ffbe21782f。
- execution：11625B，SHA256 773e2e5eb43017e77a0a7460a697ebad30e55172a4f88c5cd01600cf3a326f1d。
- 完整科学返回码1；child wall3.4881442459999974秒，非timeout；完整新目标计数0。
- 私有行轨迹6791条、19064094B、SHA256 361ed5fcedde835356c885aea5951e63818e90a271b9fc2d3616f9fa7be6c763；未发布数组。

两份小输出在 notes/forward_mean_retraction_ci/run-45770488571-1/，science文件名forward-mean-retraction.json，执行文件名execution.json。均为complete=false/proved=false；三个全域门仍unknown，不是完整数值false。

## 实际异常及合法续点

job完整trace定位新consumer第268行：在保存abs(mean_shift)的lower时，recorded检查发现非有限数，抛出ValueError: finite complete new scalar。这发生在均值变化的商式求值后。此前全域D/G/propagated-initial/bulk/atoms、Y下界和v变化upper已作为整decimal balls保存在最后完成右端。

两个正的输入区间不保证以中心半径表示的宽乘积仍排除零，因此不能仅凭n>0、Y>0把随后商式当作有限数。后继应以正端点的单调公式构造倒数kernel，再乘有符号分子；C0上界使用明确的正lower端点。该修正不删除任何原参数、接缝或符号项。

后继只读保存的6791右端整球，继续未完成区间。原未保存的逐行witness不得推断不存在，也不从很大的upper推出真实违例。原native的接口位置应重新核对计数：失败行可能在保存右端前先增加过interface计数，故execution中的5731不能未经核对当作恰好完成前缀的接缝数。准确前缀由保存的common-cell数、右端和immutable原row共同绑定。

## 范围

本次没有得到完整前向结论，没有证明或排除原BVP。R144解析恒等式及所有原已成结果保持。继续真正续算该未完目标，同时R142低逆45761859526/1仍在运行；本记录不是课题完成报告。

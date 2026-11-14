# R199 恢复与 R204 新帽：实际执行和来源

2026-11-13。第五次环境失联后按根 README §8 保存的小 UTF-8 组；不传二进制或大数组，不修改 H/open/log/results 索引。

## 来源分离

原 R199 完整证明与两原 source 曾在 /tmp/fd2d-R199-20261113 真落盘，并完成真实 Node 重核 b83454/exit0；随后环境 unavailable，完整文本不在当前 V8 store。只读 main 确认这三条原路径均 404。因此这次用另名 source 和 recovered proof，全部新 SHA，不冒原 1169… / 71da… / 192f… 身份。原观察的完整已知身份及真实退出保存在第五失联 numerical ledger，原大文件仍待恢复。

R199 恢复稿仅保原 A>=1.28、Z 属 [.60,.73] 的定理；R204 是本次新推导的 A>=1.30、Z 属 [.40,.63] 的完整帽预算。R204 仍要求实际 entire-core 球包、窄板、held 排球、全局 reach 和同 g 等距/加密，未放宽目标。

## 真正执行的范围

公共有理 source 在实际 V8 中编译并执行两个 checkCap 与 centralThresholds，合计记录 2 ms。它用 BigInt 分数和准确 Cramer 公式枚举全部 polar 三平面交点；两方案各恰8点，全部条件通过。没有 OS 进程，因此不赋予虚构 exit0。报告记录 source SHA、全部分数及判据。

新的 orbit source 也实际 V8 执行了5个解析椭圆管位置两jet和5个平 collar 输运；完整公式/参数位于报告。Gram 最大差2.220446049250313e-16，曲率差4.440892098500626e-16，时间有限差分scaled最大9.670846531423501e-11，cuff两jet最大差1.1102230246251565e-16。此输入不是原193维保存场，未跑真实候选F/J、normal、LM、BVP或body。

## API 与重生

公共 CJS 导出 checkCap(name)、centralThresholds()、DESIGNS。name 为 recovered_original 时消费 R199，为 lower_window 时消费 R204。返回完整有理参数、参考高度严界、全部预算、所有8个极点和强比例。所有常数的小数是十进制准确有理数；report 的 decimal 只供阅读，判据由分子符号决定。

相位 CJS 导出 transportTwoJet、createOrientationOrbit、localGeometry。baseEvaluate(s,u,p) 必须返回完整 X/Xs/Xu/Xss/Xsu/Xuu 三向量；factory 仅在同一固定参数下做 R_alpha Y(s,u-alpha)，不生成帽或证书。alpha=2*pi*t/3；t 不是 gap。若参数对象被外部修改，则不满足固定输入假设。

例如在本题 scripts 目录可用 Node require 两个 CJS，并将 checkCap("recovered_original")、checkCap("lower_window") 与 centralThresholds() 的结果 JSON.stringify 保存。函数不依赖外部库或OS工具。

解析 fixture 是 X=(a(s)cosu,b(s)sinu,.5+.2s)，a=1+.1s²，b=.8+.04s³；全部一、二jet由该表达式逐项求导。五个(s,u,t)为(.1,.2,0)、(.35,.7,.2)、(.6,1.4,.5)、(.85,2.1,.75)、(1.1,3.4,1)。对时间使用h=1e-5中心差分，比较X、Xs、Xu的对应时间导数。平collar fixture是((.8-s)cosu,(.8-s)sinu,.625)，角u=.73、同五个t；在s=0比较全部空间两jet。

## 明确未付部分

R204 允许真实cut高度约.417或.625，并不证明那些现存有限场已经等距或满足reach。有限height指导窗还需准确高度误差控制。R199/R204 的 delta_E 都是无标签像集、含反射的E(3)商，whole-held 是整个核心对一个开球的排除；不能用中央gap或材料点位移替代。

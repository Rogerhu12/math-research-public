# root 显式支持函数核心：冻结有理门的实际作者回执

2026-11-10 UTC，Astra-visible-flex-db6f0b0e。
这是作者的有限有理检查，不是未参与者重跑或完整证明审查。

## 不可变来源

正文 notes/2026-11-10-db6f-root-explicit-support-core-visible-reach-v1.md：
commit 747186528fa80bb233d837b1685c84174dc02db3，
blob 823c3b7ecb90201ba9718dc1865a12ce83fb0046，23,092 UTF-8 B，
SHA256 b4b5c9d5154c9bcb09f4c077ca14d6ac05064ffb61e6b75f6017ce28c6f475fc。

从固定提交逐字回读后，提取唯一 javascript 围栏的正文，
不含围栏和末端换行，2,577 ASCII B，
SHA256 89177bfdeeff086902af009e32144960d121f2fee52358ded2753e9bd01369b0。
提取源与写入前冻结源逐字一致。SHA256由本次纯JavaScript计算，
实现先以标准 abc 向量核对；没有终端文件读取。

## 实际执行与完整工具状态

00:04:57 UTC：该固定表达式在 functions.exec 的 V8 中正常返回18项PASS；
同一cell随后执行的只读终端pwd被执行器拒绝
“No usable execution environment is available”，
所以该cell的最终工具状态为 Script failed。
拒绝发生于有理表达式已返回及两次clock回执之后，不是数学门失败，
也不给任何主solver退出码。

为隔离这两个状态，00:05:49 UTC重新在一个不调用终端的cell中
执行同一固定表达式，开始和结束clock均为该时刻；
functions.exec实际返回 Script completed，18项全部PASS。
这是本回执采用的独立cell作者运行身份。
不把同一作者的两次运行计作未参与者审查。

18项覆盖：支持导数与曲率半径界、固定弧与周期端区间、
有理阶跃见证、正C与上界、各真实位置导数预算、
带边扰动reach、完整初态直径、像支持下界、
握持区比例与全时reach比例。
关键精确值为：
P(271/400)=4126248288053/5120000000000>4/5；
R_epsilon=978121/6561000>1/8；
held下界127/1000，对D上界51/25给127/2040>3/50；
握持比下界197/680>1/4；reach比下界25/408>3/100。

没有PDE、隐函数求根、曲线/网格数组、主BVP/DN、终端数学程序，
也没有将数据文件经集成传输。
全文存在/支持凸性/滚动球/法锥/PDE组合/全E(3)审查另交未参与者；
当前正文仍是待审作者稿，不是闭曲面完成。

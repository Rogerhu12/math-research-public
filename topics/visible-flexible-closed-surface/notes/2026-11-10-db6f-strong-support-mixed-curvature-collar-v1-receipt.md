# 强支持核心与混合曲率短领：冻结作者标量回执

2026-11-10 UTC；作者侧实际检查，**不是独立审稿或独立 PDE 复算**。

## 1. 不可变正文与检查源

完整作者证明：

- 路径：notes/2026-11-10-db6f-strong-support-mixed-curvature-collar-v1.md。
- 固定提交：[cfb2162ebce4720312d28a0b82bf2a49fd14e529](https://github.com/Rogerhu12/math-research/blob/cfb2162ebce4720312d28a0b82bf2a49fd14e529/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-strong-support-mixed-curvature-collar-v1.md)。
- Git blob：2e5ba8bf0d21bb7ce9c82d7070e8fa70d5247546。
- UTF-8 大小：23,363 B。
- 正文 SHA256：0bb11a1acad3d19f2751cbaa554a0e727aaed192559e5b709281da0e78fb3955。

先对新路径实际取得 404，再通过已授权的小文本后备保存；随后从上述固定提交完整取回并与生成正文逐字比较一致。执行严格发生在这个冻结回读之后。

正文附录 A 含唯一 JavaScript 围栏。从固定回读内容按围栏提取、不包含其前后换行的源恰为 3,903 ASCII B：

SHA256 **585984c63dc98292a81842eb5bacf85ced413fcd89fc039bdf1f9fcb522d4805**。

整个正文和提取源的哈希均在执行前重新比较，围栏数量明确为 1；没有执行另一个手写副本。

## 2. 实际执行

执行者：tail_review_continued_2。执行环境：本会话 functions.exec 的隔离 JavaScript/V8 运行时。以完整提取字符串构造函数并求值其 IIFE，返回实际检查结果。

- 实际执行前时钟：2026-11-10 01:20:28 UTC。
- 实际执行后时钟：2026-11-10 01:20:28 UTC。
- 实际结果：**44 PASS，0 FAIL**。
- 工具实际返回正常 Script completed，没有抛出异常。
- 这是会话 JavaScript 的正常结束，**没有终端进程退出码**；不把它写成 Python 或 shell 的 exit 0。

全部比较用 BigInt 分子/分母和整数交叉乘法，不把浮点近似当作严格不等式。检查源内部使用 T=1/2000 仅作寿命选择 T<1/2000 的有理上包络；它不宣称已求出本文真正选择的 T。

## 3. 这 44 项检查支付什么

检查包括 q 与正则化上界、锥速度和固定角开缓冲、C 的正性区间、原双曲图与新增固定修改的完整一二阶预算、有界参数下的法锥扰动 reach 常数、新初态全图包络，以及固定 H、握持像距离和全 E(3) 商像距离所需有理比较。

其中直接核得

\[
R_\varepsilon=\frac{99940009}{1045950000}>\frac3{32},\qquad
D<\frac{1011}{500}<\frac{51}{25},
\]

及正文使用的

\[
\frac{\operatorname{diam}F_0(H)}D>\frac{197}{680}>\frac14,\quad
\frac{\delta_{\rm hold}}D>\frac{53}{204}>\frac14,\quad
\frac{\delta_{\rm E}}D>\frac7{136}>\frac1{20},\quad
\frac{\operatorname{reach}F_t(M)}D>\frac{25}{544}>\frac3{100}.
\]

程序只验证这些常数之间的精确代数比较；上述几何量实际满足输入界，仍依赖正文十节的完整证明。统一存在、正则化极限、有限传播、全圈位置、实际开重叠、同一度量、全法锥引理和全 E(3) 距离论证，均不由此程序独立证明。

## 4. 作者责任与未完成范围

root 提供本次 R56 强核和 R57 混合曲率参考修改的组合与预算；tail_review_continued_2 重推输入、预算并成稿。root 对本稿新组合不算未参与者独审人。当前完整作者稿及此回执等待未参与者全文审查。

本次实际执行：PDE 0、BVP 0、solver 0、矩阵 0、曲线/网格数组 0、终端数学运行 0。不读取主优化数据，不生成或上传数据文件。

构造仍有两条边界，正宽 T 非有效计算值，出口 Q=q_* 并非 flat。没有帽中心、闭曲面、主数值 G5、最终从种子独立复算或 README 完成结论。原 R56、R57 的回执仅作为各自来源，不冒充本稿新程序执行。

# R342：指定权负六纯核成本在预定一参数族上的总通量准确为零

日期：2026-11-15。**首次新公开观察已完成；结论只限预先声明的 profile 族。**

## 1. 实际结论及其范围

公开 run **43745111286**、job **132906586198**、source **f9f4030bfea092d5dfd82cf1989a0e13e73c1cdb** 成功完成。十项新增消费器检查全部通过；只读原 R144 的四个已发表 mixed 根，新的精确外积分得到

\[
\boxed{\Omega_{u_\lambda}(A)=0\quad\text{对每个实参数 }\lambda,}
\]

其中
\[
A=N^7G+\frac{315}{32}R_0+\frac{315}{16}R_2-\frac{315}{32}R_3
\in\mathcal U_{-6}\cap\ker\pi
\]
及 \(u_\lambda\) 如下一节。结果是整个 \(\mathbb Q[\lambda]\) 多项式为空非零系数表，不只是六个采样点的浮点零。

本次**没有得到非零见证**，没有证明 \(\Omega_u(A)\) 对任意紧光滑 \(u\) 恒零，也没有证明 R338 的消去泛函在整个 \(\mathcal U_{-6}\) 恒零。当前机器输出的准确状态为 declared_family_zero_universal_functional_unresolved。

[R338](R338-weight-minus-six-pure-response-total-flux-and-exact-tail-coordinate.md) 对全部响应纯核的消去结论保持；R144 的原完整成本非成员结论也保持。新的族零观察没有撤销它们，亦没有给完整 period、全 mixed 或主课题完成证书。

## 2. 运行前已固定的原式与输入族

[观察设计](../notes/weight-minus6-total-flux-observer-design-20261115.md) 由 R138 的原 pure 恒等式、五种真实 Leibniz 分配和 R207 的旧 pure 表准确给出上述 \(\pi A=0\)。这部分没有重新求纯投影矩阵或旧秩。

原列标签为
\[
R_0=\mathfrak B_L([P,R]),\qquad
R_2=\mathfrak B_P([L,R]),\qquad
R_3=\mathfrak B_P([L,S]).
\]
使用原相位规范，新的唯一观察是
\[
\Omega_u(A)=-4\int_1^4u'''(x)
\left(M^{N^7G}_{-2}
+\frac{315}{32}M^{R_0}_{-2}
+\frac{315}{16}M^{R_2}_{-2}
-\frac{315}{32}M^{R_3}_{-2}\right)(u,u)(x)\,dx.
\]

令 \(t=x-2\)，运行前的固定族为
\[
u_\lambda(x)=
\begin{cases}
t^8(1-t)^8\{1+\lambda(2t+3t^2+5t^3)\},&2\le x\le3,\\
0,&x\notin[2,3].
\end{cases}
\]
零延拓为 \(C^7\)，不称 \(C^\infty\)。完整观察在该族上至多五次；程序准确得到全部系数为零。设计中预设的六个候选参数 \(0,\ldots,5\) 只用于非零多项式的见证选择，本轮没有非零多项式，所以没有选择见证。

原 signed 积分为 \(\int_4^x\)，不是无条件换锚。消费器对每个可达积分逐层核其被积函数含正 profile 次数，由右侧零区间归纳，才在支撑内用保留完整常数的 \(\int_1^t\)。左侧真实尾未被称为零；最终外因子 \(u'''\) 在支撑外为零。此次没有锚、来源、容量或重组异常。

## 3. 已完成的新检查与实际资源

十项新增检查为：精确双变量乘法、物理单位宽导数、逐参数有符号右常数、两原颜色同实输入、嵌套常数、所有右端零值、拒绝无 profile 积分移锚、mixed 到整包的 \(-4\) 规范、四根有理组合、族零不冒普遍恒等。全部 passed。

这些小人工读取研究输入零次，旧开发调用零次。实际新观察也不重编原 forcing、平移链或四个原根，不重求 pure/self/rank/member。

| 实际项目 | 值 |
|---|---:|
| 新观察耗时 | 3.664958818999999 秒 |
| 有理乘积数 | 1,232,486 |
| 最大整数位数 | 169 |
| 最大参数次数 | 5 |
| 最大 \(t\) 次数 | 86 |
| 峰值 RSS | 51,272 KiB |
| 非零 \(\Omega_A\) 参数系数 | 0 |
| 非零见证 | 无 |

原声明上限为 120 秒、512 MiB、15,000,000 个有理乘积、8192 bits、\(t\) 次数160。没有延长上限或根据结果更换 profile。

## 4. 可追溯来源与输出身份

实际日志：[公开 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43745111286/job/132906586198)。

| 项目 | Bytes | SHA-256 |
|---|---:|---|
| 原 job UTF-8 日志 | 71,466 | 27f5423ad25625325d2dbe502edf82c5a9f7b4eb1451f0af6a84032d5b506ff1 |
| runner 临时 audit.json | 6,458 | fafb8df1127d9a675db9fe265cb3aa972f8212410ac5ad3eabd404384b33a36f |
| 新消费源码 | 29,116 | 0055fc41fcd972b5e8093d435f9df97724e83c6381b48129b7adab681f317770 |
| 实际冻结请求 | 4,789 | 59a2f1a1f32fca3977ceae2649005ae5e96b0289edac24b043bab11811419d52 |
| 独立 workflow | 4,141 | 015d58f1f26cd11cba80548ef6b899451a54792787dc7498b3c6c80ebcd1e8bf |

旧输入 run **43655713308**、source **d21c87a4d9341369a3dee35598ed88fb666cb99d**。原导出压缩文件 15,427 B / SHA-256 936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664；仅 runner 内存解压原文 80,081 B / cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb。旧主记录、receipt、两份生产源码及目标根身份亦按设计绑定。

程序成功返回的内部流程包含四根各一次求值、直接组合外积分与同次四积分的准确有理重组。本结果只引用已发布 stdout 与完整成功状态，不把未打印的中间数组添写成已经看过的独立证书。

遵守根规则15：不提交或上传原日志、机器结果 JSON 或其它可重算 payload，不建 artifact/Release。表内哈希标识原实际输出；源码、请求、这份人类结论保留。

## 5. 本轮实际拉取与接续边界

本轮公开实际 pull 于 **2026-11-15 18:09:37.097038 UTC** 完成，before 为本 run source，after 为 **f87548f9f12b6cac624040b52a4aac03f6dab4b7**。根 README 与本题 README 差异均为空，blob 仍分别为 21bd547f56590b7f2dd279d0297efb289a9b2783、d0432faff569c8e9af7ed4809847e12880976c11。

私有实际 pull 于 **18:09:39.657449 UTC** 完成，before/after 为 **043f20e3709f8693bc7e08d4c847fa8c7dd3f662**。根规则无差，本题 README 不存在；QUEUE 唯一行仍由本会话进行中。没有发布私有正文。

下一问题是保完整 Green 尾的泛函结构：判定此实际 \(A\) 的普遍 \(\Omega\) 是否有恒等消去，或找出真正新的可检测成本。一次族零不足以自动扩大搜索或重跑旧表达式。本结果完成即推，随即继续该理论子问题及 open 中其余未付门。

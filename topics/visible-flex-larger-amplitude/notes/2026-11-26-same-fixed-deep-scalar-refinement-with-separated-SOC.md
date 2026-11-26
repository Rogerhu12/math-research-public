# 同一固定 deep scalar 的精化层保留完整多轮 SOC

日期：2026-11-26。作者：Astra-larger-e4e2a2bf-20261126 / solver。

本条是既有 R683 有限半空间修正和现有固定 deep scalar 精化的完整接口应用；
不另立新的数学结论编号，不把算法接通登记成求解收敛。本次只构造并静态核验
完整小源码，没有本地科学计算，也没有新 fixture。实际方向、精化误差及几何
效果尚须由公开仓库 Actions 的真实输出支付。

## 1. 本次解决的接口缺口

已刊粗层 `fullclosed_deep_amplitude_separation_soc.py`（`329ebd…`）具有
同一原父点、同一原 QP 方向上的最多八轮分离 SOC。精化原体 `1745cf…`，以及
能够正确读取该 SOC 父来源的独立 ray 适配 `a616e8…`，都没有继承这套完整
globalization。仅允许读取父 report，不能据此称精化求解仍用同一个 SOC 算法。

这里以完整 `a616e8…` 为唯一派生基体，保留它的固定目标、精确 transfer、
母范数、全部变量、原 QP、当前固定 scalar coarse Gram、全点真实双筛和
父观测测度比较，移入与粗层 `329ebd…` 逐字相同的完整 SOC line search。
新 report schema 是
`complete-refined-fixed-deep-scalar-amplitude-separated-SOC-v1`。
旧的 d3、1745、a616、329e 源及其 report 均不修改或重命名。

## 2. 固定数学问题和父测度比较

数学目标始终是已独立固定的

$$
g_n=ds^2+a_{\rm new}(s)^2\,d\theta^2.
$$

同层迭代不从当前场重新选目标。跨层仍核对完整 exact profile、profile identity、
物理 eta 两端、width、输入 scalar 源及所有物理 lift 定义，保留共享的原 R 和
固定 core 字节。径向 restriction 保留旧的精确符号地点；增加模式保留全部旧
模式；增加角点采用保留全部旧角点的 dyadic 网格。全部原正权观测行和永久
地点都由已有精确 transfer 接入新层，原已算 metric/geometry 数值不继承。

数学 $a_{\rm new}$ 相同，并不保证跨层重算的浮点 a carriers 逐位相同。
设父数值 carrier 为 $a_p$，新层实际使用的 carrier 为 $a_f$，同一新场
在父观测地点上的新层未加权残差为

$$
e_f=|F_s|^2-1,\quad
f_f=\frac{F_s\cdot F_\phi}{a_f\rho},\quad
d_f=\frac{|F_\phi|^2}{(a_f\rho)^2}-1.
$$

令 $r=a_f/a_p>0$。同一当前物理 Gram 和当前 rho 在父归一化下准确满足

$$
e_p=e_f,\qquad f_p=r f_f,\qquad
d_p=r^2 d_f+(r-1)(r+1).
$$

最后一式是 $r^2(d_f+1)-1$ 的代数恒等形式；实现使用上述乘积形式避免单独
形成 $r^2-1$ 的相减。随后只用原父的实际正混合径向权、原角点和 orbit
权、原 p/epsilon/scale 及原 selected scalar evaluator，读同父数值测度的
Phi、centered Phi 与最大相对 Gram。当前 raw residual 已经存在，因此这里
不重算一个父 F 或父 J。

新层自身 QP 仍优化新层声明的完整正权测度。因而“自身 Phi 下降”并不自动
推出“父测度 Phi 下降”，也不推出不同网格最大误差单调；两类读数均报告，
只在相同测度内相减。未把不同层的原始 Phi 直接相减。

## 3. SOC 在新层上的责任没有减弱

每个新层原 QP 方向有一个固定父 x 和固定原方向 d。原 C 的全部前缀（含
全部已选曲率和幅度行）逐值保留；只有完整真实全步读数被几何或幅度拒绝，
才触发 SOC。每轮从上一轮真实拒绝候选取新的最坏地点，但所有新增行都回到
同一个原父 x 计算，不能把该候选变成新的父点。

每轮在同一个原全步 (x+Td) 上重新读取全部当前行的非线性值，并对全部旧行
和新行求 R683 的数值最小范数半空间修正。内缩政策仍是明确的
`tau*||d||^3 + theta*max_i(max(c_i(d),0))`；它不是已证 MFCQ 常数，也不修改
真实 `.992` 等接受阈值。新增点若在父上已违反约束，负父界限会明确阻断该
修正分支，不把零步冒充可行。

修正方向仍须重新支付当前同父 A*z/model 读数，以及完整真实 Phi、正密度
domain、全网格和全部永久任意点的曲率与幅度读数。仅全部真实筛选通过才接受。
未通过时继续有限分离；没有新行或达到明确轮数上限时回到原 ray 的半步。
每次真实读出的新极值，即使该候选被拒绝，也永久保存。单个预留容量 mmap
保留全部当前行，未使用容量从不进入投影；used/capacity/实际磁盘占用分别报告。

新层使用完整 f247 typed helper，其 deep factory / scalar / physical adapter
来源与当前实际 context 独立核对；不借用 moving-mean 或旧 R671 身份。
f247 的实际 M、载体和 profile 来自新层自身，而不是粗层维数。

八轮只是明确的计算预算。数值 projection 可行不是严格最小范数收敛证明，
有限 typed 行都过也不是全真实筛都过，更不是连续 reach 或 amplitude 证书。

## 4. 闭合来源和同算法政策

独立 `fixed_deep_soc_refinement_parent_binding.py` 明确列出 d3、1745、a616、
329e 及当前全体 fine+SOC 的 schema 与完整源 SHA。粗层 SOC 用它原有 d80
deriver 重建完整 body；当前 fine+SOC 用本次完整 deriver 重建 body；其他
literal ray 父按各自完整源字节核验。不执行 report 提供的任意代码路径，
不把一个 canonical physics 标签替代实际 driver 身份。

为了避免 helper 与完整 deriver 的 SHA 循环，已整体验证的调用方把当前
deriver 的固定身份显式传给 helper。helper 对当前 fine 父仍做完整 body
重建。返回来源路径用 repo-relative 名称；实际 report 中的来源内容没有被
重写，切换 runner 的 detached checkout 不会成为虚假的模型变化。

父已经实现完整 SOC 时，新层强制保留原 tau、theta、分离模式、每方向最大
修正轮数、typed helper SHA 和 projection SHA；driver、launcher、coordinator、
纯 reader 均显式核查。coordinator 从实际父读出政策和末阻尼。父若是已列
literal ray 版本，新层明确记录此处新增 SOC，不能声称父已使用同一算法。
本次默认 ray 起步政策为 tau=0、theta=1/8、最多八轮 rejected-extrema。

独立 launcher 在运行前重建整个新 body，保原命令生成链的 literal guard。
上游 argv 子过程失败时先显示真实 stdout/stderr 再抛出错误，不再只保留
外层 CalledProcessError。新的纯 reader 自行绑定完整新 schema，再读取每轮
实际失败类别、q0/qz、真实 gain、完整 K/D/最坏点、幅度、末面、Pg/tolerance、
预条件器真实 entry 计数和容量使用。它不加载 raw arrays，也不调用 F/J。

## 5. 完整源码身份

以下完整源码位于课题 `scripts/resume_20261126/`。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `fixed_deep_soc_refinement_parent_binding.py` | 4787 | `1761a0735489fbf08ed69bbd86cf076cf97825df60a139eac1ce26da32b93f9a` |
| `derive_refined_deep_amplitude_separation_soc.py` | 35960 | `06670b9f8d605e960c396d1595f09fba9b20559bd74729bf6a627985975165c6` |
| `fullclosed_refined_deep_amplitude_separation_soc.py` | 98607 | `d146b82aa978d7b9ddf4f642e6e9859bd4a79e328448f15fbeac9f581fc0a8a8` |
| `launch_refined_deep_amplitude_separation_soc.py` | 28946 | `8d97223fbf5acd268f199a61e6f513a83232bb390209a0735dbcca845986bc5a` |
| `refine_deep_amplitude_separation_soc.py` | 20035 | `8ce3b51b61ac48a252f0930a3696ef3c4078830bc3cc34b89fc55db90180ecff` |
| `read_refined_deep_amplitude_separation_soc_report.py` | 37311 | `9c83044c6ba2c98f9789329c9482f9d8e2fcb7f76b8d626dd983b1b7290f800a` |

仍需保留完整派生基体 a616（77131 B）及其来源；本次不修改该基体。
f247 typed helper、a2c6 projection、dcfa fixed scalar moments、R685 v5 和所有
完整旧物理源仍按原字节复用。没有替代旧文件的同名新版本。

## 6. 已做的静态核验和可执行入口

本地仅用标准库完成 AST/compile、完整 body 重建及纯命令行生成：86 个实际
driver flags 全部已声明且无重复，输入 raw 文件在该检查中不存在，未产生
科学输出。`statistics`、`objective_value`、`point_geometry`、lift/transpose
及 coarse lift/transpose 与 a616 的 AST 相同；SOC `LINE_SEARCH` 字符串与
d80 的粗层完整版本相同。construction 独立核了父 a 的重归一化与原函数；
geometry 独立核了闭合来源及同 x/d 修正交界，均未发现接口阻断。

`deep-fixed-scalar-refinement-separated-SOC-ready-steps.json` 是 ready 队列，
不是已经运行的结论。它预留读取当前已排
`deep-fixed-scalar-amplitude-separated-SOC-first/report.json` 的真实完整输出，
默认径向加倍、保 M/N、两方向各 256 次原 QP advances，再接独立纯 reader。
coordinator 支持明确增加 M 和 dyadic N；本 ready 配置不自动增加它们。
末阻尼、SOC 政策、目标和所有物理参数均从实际父读取。该父已在实际67–69返回，
ready元数据据真实结果填写8a0509 bundle/a8cf report身份，未把粗层输入b788冒作末场。

粗层已真实返回，但本ready未加入运行队列；当前先继续同层p4，之后按实际结果选择精化。实际新层 M/J/N、初始与末
最大误差、同父 Phi 差、每轮接受/失败、全部永久点和自身连续几何均仍待真实
返回；达到声明 stopping threshold 或 zero-direction exit 不能充作精化收敛，
更不能据此宣布课题完成。

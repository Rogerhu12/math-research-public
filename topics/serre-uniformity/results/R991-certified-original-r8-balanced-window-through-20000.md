# R991：原 r=8 balanced 系数的新窗口至 20000

维护会话：serre-public-astra-20261120-de0a3e3b。

## 1. 结论与准确范围

依照 [R989 的已证明执行方法](../notes/R989-original-r8-sparse-heat-and-Kronecker-window-method.md)，公开 GitHub Actions 完成了此前未覆盖的整个集合

\[
\mathcal P=\{p:1000<p\le20000,\ p\text{ 为素数},\
p\equiv5\pmod {12},\ p\bmod9\in\{2,5\}\}.
\]

该集合有 **349** 个素数，首项 1013、次项 1049、末项 19973。对其中每个素数，令 \(n=p-8\)，原模型
\(E^+:y^2=x^3+1\) 的 bare balanced Kronecker 系数均满足

\[
\boxed{c_{p-8}^{+}\ne0\pmod p.}                       \tag{991.1}
\]

在原 \(E^-:y^2=x^3-1\) 规范下，准确相位为
\(c_{p-8}^{-}=-c_{p-8}^{+}\)，所以同样为单位。使用已证明的
[R988 原完整 Cartier/trace 等价](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)，这也证明这 **349 个指定素数** 的原完整超奇异迹 \(S\ne0\)，从而对应的原 CM Cartier 链长为 1；没有替换成低权迹或不同的 CM 源。

本结论仅涵盖上述有限集合。它不证明一般 \(p\) 的单位性、O1 的同一个本原标签三个因子非零、原高层 normal 系数或高度非零，也没有完成 Serre 一致性。

## 2. 覆盖差集与执行身份

此集合与 R936/R939 已登记的旧 r=8 窗口 \(p\le1000\)、R973/R983 的四点输入完全不交。R963 的 \(1000<p\le100000\) 窗口只含 r=2、\(p\equiv11\pmod {12}\)，也与本集合不交。因此本次没有重算任何已成窗口。

| 项目 | 实际记录 |
|---|---|
| 源提交 | `3766ab06110a57ab35b95fe5469ed40cd5ce6564` |
| 公开 run | [44755320789](https://github.com/Rogerhu12/math-research-public/actions/runs/44755320789) |
| job | `136353398270` |
| 创建时间 | `2026-11-20T14:37:56Z`，即 Asia/Taipei 2026-11-20 22:37:56 |
| 运行环境 | Python，固定 `python-flint==0.9.0` |
| 数学 consumer | `scripts/original_r8_balanced_new_window.py` |
| 契约预算 | 620 秒；外层 subprocess 另有强制超时 |
| 实际数学用时 | `1.9989247780000028` 秒 |
| 请求／完成行数 | 349／349，顺序完整一致 |
| 终止状态 | `complete_nonzero_window`，exit code 0，job 全部成功 |
| 零与尾段 | 未发现零；没有未核零、失败或未完成尾段 |
| 存储 | 公开 stdout 与 runner scratch；没有上传 raw arrays、artifact 或 Release |

完整素数集合、每一行结果及前缀 hash 均在该公开 job 的 stdout 中。Git 中只保留方法、consumer 与本摘要回执。

## 3. 三条实际原源通道

主通道为 [R990 的原 Ramanujan–超几何固定 r 公式](R990-original-hypergeometric-fixed-r-coefficient.md)。令

\[
k=\lfloor p/12\rfloor,\quad m=(p-8)/3,\quad
B={}_2F_1(-k,k+4/3;4/3;z),
\]
\[
H=((1-z)B^2)^{-1},\quad
f_i=H_i/(1-3i)\ (0\le i\le m),\quad
Q=4+12zB'/B-z/(1-z).
\]

实际计算的是

\[
J_{p,8}=[z^m]Qf^{-8},\qquad
c_{p-8}^{+}=1260(-32)^mJ_{p,8}.                    \tag{991.2}
\]

每个素数还单独核查首共振恒等式
\(H_{(p+1)/3}=B(1)^{-2}\)。只在 \(i\le m<(p+1)/3\) 的单位分母范围内构造 \(f_i\)；没有把首共振单位当成目标 \(J_{p,8}\) 单位。

按预先提交的契约，**首两个新素数** 1013、1049 另外执行两条独立通道；其余行没有冒称经过三路独立计算。

1. 原 \(E^+\) Ramanujan 方程消去得到的 Chazy/CDQ 稀疏递推。其目标为
   \(c_{p-8}^{+}=420a_{(p-11)/3}\)，CDQ 始终使用全局指标 \(v_i=ia_i\)。
2. 原 \(E^-\)、\(g_2=0,g_3=4\)、无 Gaussian 的 sigma 低项与首个单 carry 卷积。此通道从原 \(\wp\) ODE 和 sigma/inverse 出发，保留原 \(-B_{\rm old}\) 首 pole、整数 binomial 除 \(p\) 的另一负号，以及 \(E^-\to E^+\) 的最终负号。

两条独立通道在这两个素数均与主通道完全一致：

| \(p\) | \(n\) | \(J_{p,8}\) | 主通道尺度 | \(c_n^+\) | \(c_n^-\) | CDQ \(M,a_M\) | sigma \(N,t,B_{\rm old}\) |
|---:|---:|---:|---:|---:|---:|---|---|
| 1013 | 1005 | 244 | 758 | 586 | 427 | 334, 286 | 168, 167, 392 |
| 1049 | 1041 | 663 | 528 | 747 | 302 | 346, 294 | 174, 173, 777 |

sigma 通道分别收缩 169/175 个低项和 167/173 个单 carry 项；低 sigma、逆级数及 \(\wp\) 关系的内部检查均通过。契约另要求若出现首零必须经这两条原源独立复核，才可按“已核首零”终止；此次没有触发该分支。

末行 \(p=19973,n=19965\) 给
\(J_{p,8}=19108\)、尺度 9552、\(c_n^+=6342\)、\(c_n^-=13631\)。它属于主通道完整窗口，未额外声明独立通道验证。

## 4. 源文件 pins

以下是此次 run 实际消费并核验的文件。consumer 自身及依赖证明均固定哈希；workflow 在数学执行前逐一核对 request 的源码 pins。

| 源路径（相对于本课题） | 字节 | SHA256 |
|---|---:|---|
| `scripts/original_r8_balanced_new_window.py` | 19780 | `96b3bbf3ec77c3c75a3870adebd9f348e7849f52b17dcda245f56229682f7160` |
| `notes/R989-original-r8-sparse-heat-and-Kronecker-window-method.md` | 19390 | `430459e1a80765b48efe83b1255a4f0a0bfbc7998dad5e8c3e039d2a8a76c4c0` |
| `results/R990-original-hypergeometric-fixed-r-coefficient.md` | 14943 | `5c35e72804eee83dde2c74af68232dea3a57c5d97ba39026a07329a7db25a7a1` |
| `results/R975-original-balanced-Kronecker-integral-heat-recurrence.md` | 10374 | `56ab77273393f6db838daea1a3973e1d9da69525eb120e665dccea88f64de101` |
| `results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md` | 15506 | `db82c7e799a7e54b7d91da329e4e6c113add5a98a519aab82df2a2e70de470a7` |
| `notes/R973-original-balanced-Kronecker-four-prime-execution-method.md` | 7083 | `32d4c836cacbb0467c668a4a968be62fe759cd188a3365bdfb9da9583d076269` |

对应 workflow `.github/workflows/serre-current-exact-research.yml` 为 3599 字节，SHA256
`987349aec643aa0076fc0a13492c50cdcabe12d4ce8aafa2c260ce3c1dd10966`；此次请求为 2235 字节，SHA256
`139a7e0de69d697ebf90048398e5c48bc2e760fdf82b04bb933bf70a9876216e`。

## 5. 完整输出回执与本地核验范围

下表的各对象使用 Python `json.dumps(..., sort_keys=True, separators=(',', ':'))` 的 UTF-8 字节；单对象不加换行。payload 为 `{contract,rows,summary}` 的同一规范 JSON，再加一个末尾换行。保留原始 JSON 数值类型，特别是 contract 中的 `620.0`，不可先经会改变该表示的转码再比较 hash。

| 对象 | 字节 | SHA256 |
|---|---:|---|
| 请求素数序列 | 见公开 contract | `51e395c239eeb5fe8c8a46cbebb75baebd32760f50195e76903c23e27488c0ed` |
| contract | 3462 | `3da439b0fdb86b5301936a8d73e569744c27e54fd5b31c11fb1f5017ea1525a2` |
| 349 rows | 237195 | `18db4db98b24d059bc9c315c21114217beede057a58f874baa1066ce4a303076` |
| summary | 4679 | `390f43e720772756e0dbed2c8b6cfd812068cdd1fc4ebc86891b995b7d9e4f64` |
| 完整 payload | 245369 | `fea55f009c33e1b120e50c1fd9ff2a23aba25c999d863f506a72105fabfb86aa` |

root 从公开 stdout 提取原始 JSON，独立做纯 IO/schema/hash 检查：请求集、完成集及 row 顺序一致；349 行均报告非零且首共振检查通过；只有预定 1013/1049 有三路独立检查并全部一致；无错误、无尾段、无未核零。全部 canonical hashes 与 stdout receipt 一致。此核验没有在本地重新执行任何数学计算。

本 request 已完整完成；仅修改本回执、索引和交接，不通过重写 request 触发旧窗口。后续研究继续原 near-p 系数的一般非零与 O1 的真实同标签条件。

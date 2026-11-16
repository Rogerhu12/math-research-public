# 2026-11-16：原 RR 首两任务的真实停止点及规则同步

可信度：下述为已取得的精确执行记录；没有完整 RR PASS，不推原 shadow 或主目标。

## 原输入与未完成范围

共同源码提交为 acf294c6e07c20618f2acc9dfab863c34e8c8cb9，固定 Sage 10.6 镜像为 sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。参数沿各原 ci request，不改原 18 源、36 尖点、D204、T/U/V 或全部绝对端点。源码、参数和日志足以重算；不保存可重算输出。

- 306 模型：[run43850251992](https://github.com/Rogerhu12/math-research-public/actions/runs/43850251992)，job133240631228，producer scripts/produce-original-shadow-rr-front.py。
- eta48 模型：[run43850252040](https://github.com/Rogerhu12/math-research-public/actions/runs/43850252040)，job133240628667，producer scripts/produce-original-shadow-rr-eta48.py。

两任务分别于 16:35:56、16:35:55 UTC 显示 “The operation was canceled”，距 job 启动约六小时，符合平台单任务时限。日志没有完整 RESULT 或最终 result SHA；不能把中间系数哈希当 RR 证书。

## 306 模型

整数 $\Phi_{17}$ 有 291 个非零项、双次数 $(18,18)$，完成于 0.295543 秒。其 terms SHA-256：

36d1433b249f994bf055b5317eb28ffd9153be2461643227509414b1bfcc1d27

准确消去中间变量并除回溯因子 $(V-T)^{18}$，于 757.025077 秒得到循环次数 306；coefficients SHA-256：

0939fd2612f1c44a9d3b87cc3e46f3114d3038c54bc9e8d379323fc647b9b5eb

最后阶段是 10:49:09 UTC、757.586470 秒的 “field: separability check”。对应代码对 $\mathbf F_{29}(T)[V]$ 的完整次数 306 多项式计算与导数的 gcd；直到取消未返回。中间坐标恢复、正规化、全尖点和 RR 均未开始。最后一次阶段记录 max_rss_kib=452028，不把它解释为整次运行的最终峰值。

## eta48 模型

相同循环关系的系数哈希与上面一致。代入 $V=T/t^{12}$ 并除 $X^{18}$ 后，得到总次数 576 的多项式；1019.436785 秒开始精确因子分解。

3471.642649 秒准确选中原 eta48 因子：四个次数 48 因子的初始权均为 $-24$，初始点 $(1,1)$ 的值依次为 13、2、0、18；四个次数 96 因子的初始权均为 $-48$，对应值为 3、17、12、1；各重数为 1。唯一初始值 0 的次数 48 因子给原分支。其 coefficients SHA-256：

b8c0a892e436474cce5e8bee48fd8ee735b4b3765d027f6013cbe56430e54532

最后阶段为 11:34:22 UTC、3472.047083 秒的 “field: exact intermediate U recovery”。代码在次数 48 的函数域中对原 $\Phi_{17}(T,Z)$ 与 $\Phi_{17}(Z,V)$ 求 gcd；直到取消未返回。尚未进入正规化或 RR。最后一次阶段记录 max_rss_kib=1632140，同样不代表最后峰值。

因此后续应准确改进可分性和原 $U$ 恢复；仅换小次数底模型仍保留相同 gcd 卡点，不能据模型次数预言已能完成。任何替代都须保留两条原 $\Phi_{17}$ 关系、原分支、绝对尖点、全 RR 维数与返回到同一 DS 的认证。

## 实际 pull 与规则 15 库存

本地执行环境于 16:31 UTC 不可用，真实重试报告 No usable execution environment is available。按根 README 第 8 条继续用小文本 API 非强推。现有只读公开 workflow 的实际 git pull --rebase 已在 16:36:18 UTC 成功：

- run43909317247，job133446561662；
- 实际 main/source 3086204af188e0a552af80e01b3e2cbeb277f8e5；
- 比较基准 4da966938068e26908c3726795a3b46eab135ea0；
- 根 README blob 21bd547f56590b7f2dd279d0297efb289a9b2783，课题 README blob 965ab236bbd6753acb812b45fcc36ae9b6f83b3c，差异为空；
- 同 head 的完整 tree 188653cdfea9876901d0807f8b591417d0b73f7a：课题 2540 个 blob、34275086 字节，没有超过 5 MB 的文件；
- 3 个既有真实输入块保持原规则 15 来源说明，无新增输出块。

这是公开 CI 稀疏只读 checkout 的实际 pull，不是本地工作副本恢复。下次实际 pull 最迟 17:20 UTC；每次仍核对两份 README 的差异。主目标未完成，继续原 P、真 RR、完整 shadow 及各原非零门。

## R910 首轮接口失败（16:57 UTC）

新 run43912835484/job133459031944/source d622da0c720cef993a131ad47fc3214e08f771bc 在通用子结式返回转换时触发 RecursionError（35.526秒），尚无RR证书。精确栈为 multi_polynomial.pyx 子结式列表转换到 libsingular 多元环时进入表达式编译；已改用直接 k[x,v][Z] 系数向量并仅读取线性项两系数，完整原数学门不变。详见 R910§7；不靠提高递归上限掩盖该转换。

## 后续规则同步（17:06:56 UTC）

实际终端pull在17:06:25仍报无可用环境；公开只读run43914883095/job133466239198成功执行git pull --rebase，head e3036ead5cb7310d0df3cd6d86f68496e2fa817d，对比53a72e4c8d98aeb1e289ba8dab2598c65ab6c88e，两README差异为空，原两blob不变。该head完整题树bd208553c16df55639f2a98877d5e10c1a639e9a有2546个blob、34353361字节，无超过5MB文件，仍只有3个既有真实输入块。下次实际pull最迟17:50 UTC；本地副本未恢复。

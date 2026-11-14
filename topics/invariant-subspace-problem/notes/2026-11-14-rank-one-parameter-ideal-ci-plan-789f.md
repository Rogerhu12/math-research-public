# R150 剩余有限异常集：参数域原理想证书入口

日期：2026-11-14 UTC。作者：normal_annihilator / Astra-ISP-789f。

**当前状态（迁移新规）：本课题已迁入公开 math-research-public，现直接使用本仓库自己的 Actions（根规则13）。旧跨仓库代跑 runner 和 ci-queue 不恢复。§3仅为旧投递历史；当前workflow见文末。** 尚无完成的 Gröbner/lift 结论。

本地入口为 `node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out /tmp/isp-789f-r150-q0 --characteristic 0 --coordinates original --algorithm slimgb --stage lift`；有限特征另用输出目录及32003。

## 1. 准确目标

已读原中心十七式、$A_y$ 全参数秩分类、泛参数有限 $\Sigma$、逐点小投影秩界、源点四及 $P_\pm,E_8$ 数域证书。所有 $\operatorname{rank}A_y=8$ 的均值及无穷远均已另文关闭。当前只需处理 $g\ne0$、$\operatorname{rank}A_y=9$ 的可能有限异常点，不能从已闭 $\operatorname{ess}T_3\le3$ 支持分类越界。

直接计算全部 $4354$ 阶子式的 gcd 并非唯一入口。若能给九个横向平方在原十七式理想中的显式参数域表示
$$
z_j^2=\sum_{i=1}^{17}c_{ij}(s,M)f_i(s,M),\qquad 2\le j\le10,
$$
且准确提取这些系数的公共分母 $D_*(s)$，则所有 $D_*(s)\ne0$ 的有限参数已有原特征零证明。剩余待算集合可改用 $D_*$ 的根；它不必等于已有最大子式 gcd $\Delta$。分母若只含已经分类的因子，即关闭当前全部有限余点。

## 2. 原输入及降低参数次数

新入口 `2026-11-14-rank-one-parameter-ideal-runner-789f.js` 只调用已发表的原整数系统生成器及可选原二项式平移。每个样本先乘回全部保存的 `scale`，恢复固定 $\det J_3$ 倍原式，再做整数 Newton 插值；只约去一个与参数无关的整数内容，不除任何参数多项式。

原未平移 $M$ 坐标中，十一条 $N$ 的参数次数至多十、六条 $\Gamma$ 至多五，所以只需 $s=0,\ldots,10$ 重建。九个目标使用准确逆二项式横向坐标的平方。平移坐标选项仍保留，可用于另一项算法尝试，其已证参数次数界为二十五。

最初仅作生成检查时，运行 `--generate-only --coordinates original`：约 1.5 秒，重建后在 $s=-1,11,12$ 的全部 $3927$ 个固定倍式系数均准确相符，生成的 Singular 输入为约 174 KB。该初始检查本身没有启动 Gröbner；后续本地与本仓库CI执行状态见文末。

## 3. 已停止的旧跨仓库入口（历史，不再执行）

第一项建议直接求特征零证书，命令只含通用计算参数：

```sh
sudo apt-get update -qq && sudo apt-get install -y --no-install-recommends singular && node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out "$OUT_DIR" --characteristic 0 --coordinates original --algorithm slimgb --stage lift
```

可并行开一项有限特征发现计算，将 `--characteristic 0` 改成 `--characteristic 32003`。它只用于了解标准基和可能分母因子，不能提升成特征零分类。每项建议 `timeout_minutes: 350`。

程序先计算原理想标准基，检查九个目标余式，再调用 `lift` 并准确检查 $I C=T$。随后从所有证书系数取分母，移到单参数多项式环求 lcm，剔除已经分类的 $s(s-2)(s+6)P_+P_-E_8$ 因子，输出剩余分母及因子。最高十六式已由原 $J_3$ 唯一解回，输出不遗漏任何原低梯度。

`receipt.json` 记录实际完成标记、原数据及稳定输入哈希、精确身份检查结果；输出证书和标准基压缩后保存，超过仓库单文件限制只保哈希及可复现入口。`denominator.sing` 给下一实际数域任务。若没有 `R150_DONE_EXACT_MEMBERSHIP` 及准确身份检查标记，不能把运行解释为完成。

## 4. 解释边界

只有特征零、全部九个实际原理想身份和其实际分母都得到后，才能做专门化覆盖。有限域标准基、若干整数参数的成功、算法未报错或一般参数下的零余式都不替代这一证书。若残余分母非平凡，仍须逐个不可约因子处理或改取另一证书减少分母；不能从分母出现即宣称存在额外临界点。

Singular 的 `lift`/`liftstd` 采用原生成元变换矩阵语义；参照其官方手册及源码文档：<https://github.com/Singular/Singular>，`doc/reference.doc` 中对应条目。这里只有通用计算接口，没有调用不适用于原系统的文献分类。

## 5. 后继参数域覆盖

如实际分母有额外因子，可用不同坐标/项序产生第二份原生成元证书，并按[逐目标 Bézout 拼接](2026-11-14-rank-one-certificate-open-cover-789f.md)取共同未覆盖根；该代数接口不预判任何当前计算结果。

## 本地执行恢复（2026-11-14 06:34 UTC）

官方通用 Linux 压缩包 `Singular-4.4.0-x86_64-Linux.tar.gz` 已在本环境用户可写目录解包，`Singular --version` 确认为4.4.0。来源：[官方用户目录安装说明](https://www.singular.uni-kl.de/public/pages/singular-download/109.html)、[官方二进制目录](https://www.singular.uni-kl.de/ftp/pub/Math/Singular/UNIX/)。保持包内目录结构，未改变系统包权限、代理或TLS。

本轮二进制位置 `/tmp/isp-789f-singular-runtime/singular-4.4.0/bin/Singular`；以临时 PATH 前置后运行本稿既有特征0命令，输出 `/tmp/isp-789f-r150-q0`。工具输出/receipt必须检查后才能判为完成；工作目录临时文件若失去，按上述官方来源重新解包，再从仓库脚本重放。有限域32003任务后于06:43 UTC启动，Singular子进程限1 GiB，输出 `/tmp/isp-789f-r150-p32003`；它仅供发现，不是特征零证明。

## 本仓库自有 Actions 与本地失败回执（迁移后）

根规则13现授权直接运行本仓库六课题的计算。新增 `.github/workflows/invariant-subspace-r150-parameter-ideal.yml` 以本工作流/原runner的路径push或手动触发，两个矩阵任务分别特征0和32003，单次计算330分钟、整任务350分钟。只用本仓库源，不读取或代跑其他仓库任务。工作流精确调用同一原17式入口；输出保存到本题 `notes/r150-actions-789f/<run>-<attempt>/char<characteristic>`，并保留30天artifact。

输出回推使用进程环境中的Actions token；每次实际pull先比较本仓库根/课题README的原始指纹，变化则保artifact交当前会话读取新规，不盲推。非快进立即rebase重推；所有同步检查提交号写入该次输出回执。凭据不写文件。压缩/5 MB限额和重建哈希继续遵守根规则8。

本地特征0实际从06:33:51至06:46:36，在 `R150_BEGIN_BASIS` 后异常结束；`exitCode=null`、无完成标记、无原理想身份，具体终止信号旧runner未记录，不能确定原因。[原始失败回执](2026-11-14-r150-local-q0-incomplete-789f.json)已保存。新runner开始记录子进程终止信号和临时输出位置，CI结束时可保尚未完成的中间输出，但任何这种文件都不算已证明证书。
